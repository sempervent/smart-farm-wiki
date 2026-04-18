#!/usr/bin/env python3
"""
Validate PDF ↔ machine-extract pairing under raw/ and wiki links pointing into raw/.

**Public / default mode (no ``--strict``):**

- Structural / safety checks still **fail** the run: malformed source-note conventions
  (PDF in ``source_ids`` without a body link to ``*-extracted.md``).
- Missing **local** targets (PDF without extract; wiki link to absent ``raw/`` file) are
  **warnings** only — the evidence corpus may be gitignored or absent in CI.

**Strict / local mode (``--strict``):**

- Missing local PDF extracts and missing wiki ``raw/`` link targets are promoted to **errors**
  (use when a full local ``raw/`` corpus is available).

``validate_wiki.py`` skips raw link existence by default; use
``validate_wiki.py --raw-pdf-links`` with or without ``--strict`` to mirror the policy above.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from wiki_common import (
    extract_markdown_links,
    infer_repo_root,
    load_frontmatter,
    resolve_markdown_path,
)


def collect_pdfs_under_raw(raw_root: Path) -> list[Path]:
    return sorted(raw_root.rglob("*.pdf"))


def check_pdf_extract_pairs(root: Path) -> list[str]:
    """Each on-disk PDF must have ``<stem>-extracted.md`` in the same directory."""
    errors: list[str] = []
    raw_root = root / "raw"
    if not raw_root.is_dir():
        return errors
    for pdf in collect_pdfs_under_raw(raw_root):
        expected = pdf.parent / f"{pdf.stem}-extracted.md"
        if not expected.is_file():
            rel_pdf = pdf.relative_to(root)
            rel_ex = expected.relative_to(root)
            errors.append(f"PDF missing machine extract: {rel_pdf} (expected {rel_ex})")
    return errors


def check_wiki_raw_link_targets(root: Path) -> tuple[list[str], list[str]]:
    """
    For each wiki markdown link resolving under raw/, report missing files as
    warnings (or errors when caller promotes them).
    """
    errors: list[str] = []
    warnings: list[str] = []
    wiki_dir = root / "wiki"
    if not wiki_dir.is_dir():
        return errors, warnings

    for page in sorted(wiki_dir.rglob("*.md")):
        rel_page = page.relative_to(root)
        text = page.read_text(encoding="utf-8")
        for _label, target in extract_markdown_links(text):
            resolved = resolve_markdown_path(page, target, root)
            if resolved is None:
                continue
            try:
                resolved.relative_to(root / "raw")
            except ValueError:
                continue
            if not resolved.is_file():
                warnings.append(
                    f"Wiki raw link target missing: {rel_page} -> {target!r} "
                    f"({resolved.relative_to(root)})"
                )
    return errors, warnings


def check_pdf_source_notes_link_extracts(root: Path) -> list[str]:
    """
    Source notes that cite a ``*.pdf`` in ``source_ids`` should also link the
    ``*-extracted.md`` sidecar in the body (searchable convention).
    """
    errors: list[str] = []
    sn_dir = root / "wiki" / "source-notes"
    if not sn_dir.is_dir():
        return errors

    for page in sorted(sn_dir.glob("*.md")):
        text = page.read_text(encoding="utf-8")
        fm, body = load_frontmatter(text)
        ids = fm.get("source_ids") or []
        if not isinstance(ids, list):
            continue
        pdf_ids = [x for x in ids if isinstance(x, str) and x.strip().lower().endswith(".pdf")]
        if not pdf_ids:
            continue
        for sid in pdf_ids:
            stem = Path(sid).stem
            expected_suffix = f"{stem}-extracted.md"
            ok = False
            for _lab, tgt in extract_markdown_links(body):
                if normalize_rel_raw_target(tgt).endswith(expected_suffix):
                    ok = True
                    break
            if not ok:
                rel = page.relative_to(root)
                errors.append(
                    f"{rel}: source_ids includes {sid!r} but body has no link to "
                    f"*{expected_suffix!r}"
                )
    return errors


def normalize_rel_raw_target(target: str) -> str:
    t = target.strip().split("#", 1)[0].split("?", 1)[0].strip()
    return t


def run_checks(
    root: Path,
    *,
    wiki_raw_targets: bool,
    source_note_extract_links: bool,
    strict_local_raw: bool = False,
) -> tuple[list[str], list[str]]:
    """
    ``strict_local_raw``: when True, missing on-disk PDF extracts and missing wiki ``raw/``
    targets are errors; when False, they are warnings only.
    """
    errors: list[str] = []
    warnings: list[str] = []

    pdf_pair_msgs = check_pdf_extract_pairs(root)
    if strict_local_raw:
        errors.extend(pdf_pair_msgs)
    else:
        warnings.extend(pdf_pair_msgs)

    if wiki_raw_targets:
        _e, w = check_wiki_raw_link_targets(root)
        errors.extend(_e)
        if strict_local_raw:
            errors.extend(w)
        else:
            warnings.extend(w)

    if source_note_extract_links:
        errors.extend(check_pdf_source_notes_link_extracts(root))

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate PDF/extract pairing and wiki links into raw/ (optional checks)."
    )
    parser.add_argument("--root", type=Path, default=None, help="Repository root.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "Require local raw corpus to be complete: missing PDF *-extracted.md pairs and "
            "missing wiki markdown targets under raw/ become errors (not warnings)."
        ),
    )
    parser.add_argument(
        "--no-wiki-raw-targets",
        action="store_true",
        help="Skip scanning wiki for raw/ markdown link targets.",
    )
    parser.add_argument(
        "--no-source-note-extract-links",
        action="store_true",
        help="Skip source-note convention check for *-extracted.md links.",
    )
    args = parser.parse_args()
    root = infer_repo_root(args.root)

    errors, warnings = run_checks(
        root,
        wiki_raw_targets=not args.no_wiki_raw_targets,
        source_note_extract_links=not args.no_source_note_extract_links,
        strict_local_raw=args.strict,
    )

    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)

    if errors:
        return 1
    if warnings:
        print(
            f"\n{len(warnings)} warning(s) (missing local raw targets or PDF extracts); "
            "use --strict to fail the run when the full corpus is present.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
