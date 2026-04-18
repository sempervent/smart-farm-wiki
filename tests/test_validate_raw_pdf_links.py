"""Tests for validate_raw_pdf_links.py."""

import subprocess
import sys
from pathlib import Path

import pytest


def test_validate_raw_pdf_links_passes_on_repo(repo_root: Path) -> None:
    proc = subprocess.run(
        [
            sys.executable,
            str(repo_root / "scripts" / "validate_raw_pdf_links.py"),
            "--root",
            str(repo_root),
            "--strict",
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout


def test_pdf_missing_extract_fails(tmp_path: Path) -> None:
    scripts = Path(__file__).resolve().parent.parent / "scripts"
    root = tmp_path
    (root / "raw" / "processed" / "2026").mkdir(parents=True)
    (root / "raw" / "processed" / "2026" / "orphan.pdf").write_bytes(b"%PDF-1.4\n")

    proc = subprocess.run(
        [
            sys.executable,
            str(scripts / "validate_raw_pdf_links.py"),
            "--root",
            str(root),
        ],
        cwd=root,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 1
    assert "missing machine extract" in proc.stderr.lower() or "PDF missing" in proc.stderr


def test_source_note_missing_extract_link_fails(tmp_path: Path) -> None:
    scripts = Path(__file__).resolve().parent.parent / "scripts"
    root = tmp_path
    (root / "wiki" / "source-notes").mkdir(parents=True)
    (root / "wiki" / "source-notes" / "bad-pdf-note.md").write_text(
        "---\n"
        "title: X\npage_type: source_note\n"
        "source_ids:\n"
        "  - raw/processed/2026/x.pdf\n"
        "---\n"
        "# X\n"
        "[pdf](../../raw/processed/2026/x.pdf)\n",
        encoding="utf-8",
    )

    proc = subprocess.run(
        [
            sys.executable,
            str(scripts / "validate_raw_pdf_links.py"),
            "--root",
            str(root),
            "--no-wiki-raw-targets",
        ],
        cwd=root,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 1
    assert "x-extracted.md" in proc.stderr or "extracted" in proc.stderr.lower()


@pytest.mark.parametrize("strict", [False, True])
def test_wiki_raw_missing_target_warning_or_error(tmp_path: Path, strict: bool) -> None:
    scripts = Path(__file__).resolve().parent.parent / "scripts"
    root = tmp_path
    (root / "raw").mkdir(parents=True)
    (root / "wiki" / "source-notes").mkdir(parents=True)
    # Same relative depth as real source-notes: ../../raw/ resolves to repo root.
    (root / "wiki" / "source-notes" / "note.md").write_text(
        "[missing](../../raw/processed/2026/not-there.pdf)\n", encoding="utf-8"
    )

    cmd = [
        sys.executable,
        str(scripts / "validate_raw_pdf_links.py"),
        "--root",
        str(root),
    ]
    if strict:
        cmd.append("--strict")
    proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True)

    if strict:
        assert proc.returncode == 1
        assert "ERROR" in proc.stderr or "missing" in proc.stderr.lower()
    else:
        assert proc.returncode == 0
        assert "WARNING" in proc.stderr or "Wiki raw link" in proc.stderr
