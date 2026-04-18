#!/usr/bin/env python3
"""
Extract text from PDF files into Markdown under raw/processed (or beside the PDF).

Uses PyMuPDF (fitz). Scanned/image-only pages may yield little or no text; OCR is
out of scope — use dedicated OCR tooling for bitmap-only PDFs.

Examples:

  uv run python scripts/pdf_to_markdown.py raw/processed/2026/example.pdf
  uv run python scripts/pdf_to_markdown.py --all-raw --force
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

try:
    import fitz  # PyMuPDF
except ImportError as e:  # pragma: no cover
    print("Install PyMuPDF: uv sync (see pyproject.toml dependencies)", file=sys.stderr)
    raise SystemExit(1) from e


def _repo_rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError:
        # PDF outside the repo (e.g. tests in /tmp)
        return path.resolve().as_posix()


def pdf_to_markdown(pdf_path: Path, title: str | None = None) -> str:
    """Return Markdown body (no frontmatter) for one PDF."""
    doc = fitz.open(pdf_path)
    parts: list[str] = []
    for i in range(len(doc)):
        page = doc.load_page(i)
        text = page.get_text("text") or ""
        text = text.strip()
        parts.append(f"## Page {i + 1}\n\n")
        if not text:
            parts.append(
                "_No extractable text on this page "
                "(may be image-only, scanned, or vector-only)._\n\n"
            )
        else:
            # Normalize excessive blank lines; keep paragraph breaks
            text = re.sub(r"\n{3,}", "\n\n", text)
            parts.append(text)
            if not text.endswith("\n"):
                parts.append("\n")
            parts.append("\n")
    doc.close()
    return "".join(parts).rstrip() + "\n"


def write_markdown(
    pdf_path: Path,
    out_path: Path | None,
    *,
    title: str | None,
    force: bool,
) -> Path:
    pdf_path = pdf_path.resolve()
    if not pdf_path.is_file():
        raise FileNotFoundError(pdf_path)

    if out_path is None:
        out_path = pdf_path.with_name(f"{pdf_path.stem}-extracted.md")

    if out_path.exists() and not force:
        raise FileExistsError(
            f"Refusing to overwrite {out_path} (use --force): run manually or delete first"
        )

    doc = fitz.open(pdf_path)
    page_count = len(doc)
    doc.close()

    display_title = title or pdf_path.stem.replace("-", " ").replace("_", " ").title()
    rel_pdf = _repo_rel(pdf_path)
    today = date.today().isoformat()

    body = pdf_to_markdown(pdf_path, title=title)
    pdf_name = pdf_path.name
    fm = f"""---
title: "{display_title} (extracted from PDF)"
source_pdf: {rel_pdf}
extracted: {today}
page_count: {page_count}
note: Machine-extracted text; verify against the PDF for tables, figures, and typography.
---

# {display_title}

**Source PDF:** [`{pdf_name}`](./{pdf_name}) — repo path `/{rel_pdf}`

"""

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(fm + "\n" + body, encoding="utf-8")
    return out_path


def discover_pdfs_under_raw() -> list[Path]:
    raw = REPO_ROOT / "raw"
    if not raw.is_dir():
        return []
    return sorted(p.resolve() for p in raw.rglob("*.pdf") if p.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert PDF text to Markdown beside the PDF.")
    parser.add_argument(
        "pdfs",
        nargs="*",
        type=Path,
        help="PDF files (repo-relative or absolute)",
    )
    parser.add_argument(
        "--all-raw",
        action="store_true",
        help="Process every *.pdf under raw/",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output .md path (only valid with a single input PDF)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing *-extracted.md files",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Override title in frontmatter",
    )
    args = parser.parse_args()

    paths: list[Path] = []
    if args.all_raw:
        paths = discover_pdfs_under_raw()
        if not paths:
            print("No PDF files found under raw/", file=sys.stderr)
            return 1
    else:
        for p in args.pdfs:
            p = Path(p)
            if not p.is_absolute():
                p = (REPO_ROOT / p).resolve()
            paths.append(p)

    if not paths:
        parser.error("Provide PDF path(s) or use --all-raw")

    if args.output is not None and len(paths) != 1:
        parser.error("--output requires exactly one input PDF")

    errors = 0
    for pdf in paths:
        try:
            out = write_markdown(
                pdf,
                args.output,
                title=args.title,
                force=args.force,
            )
            print(f"Wrote {_repo_rel(out)}")
        except FileExistsError as e:
            print(f"SKIP: {e}", file=sys.stderr)
            errors += 1
        except Exception as e:  # pragma: no cover
            print(f"ERROR {pdf}: {e}", file=sys.stderr)
            errors += 1

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
