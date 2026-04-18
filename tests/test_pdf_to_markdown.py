"""pdf_to_markdown.py extraction."""

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "pdf_to_markdown.py"


@pytest.fixture
def tiny_pdf(tmp_path: Path) -> Path:
    """Minimal one-page PDF with known text."""
    fitz = pytest.importorskip("fitz")
    pdf_path = tmp_path / "sample.pdf"
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 100), "HelloPdfMarker")
    doc.save(pdf_path)
    doc.close()
    return pdf_path


def test_pdf_to_markdown_writes_markdown(tiny_pdf: Path, tmp_path: Path) -> None:
    import importlib.util

    out = tmp_path / "out.md"
    spec = importlib.util.spec_from_file_location("pdf_to_markdown", REPO_ROOT / "scripts/pdf_to_markdown.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    path = mod.write_markdown(tiny_pdf, out, title="Sample", force=True)
    text = path.read_text(encoding="utf-8")
    assert "HelloPdfMarker" in text
    assert "Page 1" in text
    assert "source_pdf:" in text


def test_cli_help() -> None:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--help"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0
    assert "--all-raw" in proc.stdout
