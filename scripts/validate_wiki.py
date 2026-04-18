#!/usr/bin/env python3
"""
Repository integrity checks for the LLM Wiki template.

Exits non-zero on errors. Warnings do not fail unless --strict (warnings promoted).

**Raw corpus links:** Markdown links pointing under ``raw/`` (e.g. ``../../raw/processed/...``)
are **not** validated as existing files by default. The evidence corpus may be gitignored or absent in CI;
provenance is still recorded in the wiki, and ``mkdocs.yml`` already relaxes missing targets for
the static site build. Use ``--raw-pdf-links`` (or ``scripts/validate_raw_pdf_links.py``) when the
processed corpus is present locally to check PDF ↔ ``*-extracted.md`` pairing and raw link targets.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from wiki_common import (
    extract_markdown_links,
    infer_repo_root,
    is_kebab_md,
    is_under_raw_dir,
    load_frontmatter,
    normalize_link_target,
    requires_frontmatter_schema,
    resolve_markdown_path,
    LOG_HEADING_PATTERN,
)

REQUIRED_ROOT_FILES = [
    "AGENTS.md",
    "README.md",
    "LICENSE",
    "mkdocs.yml",
    "wiki/index.md",
    "wiki/log.md",
    "wiki/overview.md",
]

MUTABLE_RAW_PATTERNS = [
    re.compile(r"edit\s+[`']?raw/processed", re.I),
    # Avoid matching "immutable" (contains "mutable" as substring)
    re.compile(r"(?<!im)mutable\s+raw", re.I),
    re.compile(r"update\s+this\s+raw\s+file", re.I),
]


def parse_index_links(index_text: str) -> set[Path]:
    """Collect wiki-relative paths from markdown links in index.md."""
    targets: set[Path] = set()
    for _, target in extract_markdown_links(index_text):
        norm = normalize_link_target(target)
        if not norm or norm.startswith("/"):
            continue
        p = Path("wiki") / Path(norm)
        targets.add(p)
    return targets


def collect_wiki_pages(wiki_dir: Path) -> list[Path]:
    return sorted(wiki_dir.rglob("*.md"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate LLM Wiki repository structure.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (recommended for CI).",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repository root (default: parent of scripts/).",
    )
    parser.add_argument(
        "--raw-pdf-links",
        action="store_true",
        help=(
            "Also run PDF ↔ *-extracted.md checks and wiki links into raw/ "
            "(see scripts/validate_raw_pdf_links.py). With --strict, missing local raw "
            "targets and PDF extracts fail the run; without --strict, they are warnings only."
        ),
    )
    args = parser.parse_args()
    root = infer_repo_root(args.root)
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_ROOT_FILES:
        if not (root / rel).is_file():
            errors.append(f"Missing required file: {rel}")

    if not (root / "raw").is_dir():
        errors.append(
            "Missing raw/ directory (expected per AGENTS.md; track raw/**/.gitkeep if the tree is empty in git)"
        )

    wiki_dir = root / "wiki"
    if not wiki_dir.is_dir():
        errors.append("Missing wiki/ directory")
        return _finish(errors, warnings, args.strict)

    index_path = wiki_dir / "index.md"
    log_path = wiki_dir / "log.md"

    index_text = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""
    index_targets = parse_index_links(index_text)

    wiki_pages = collect_wiki_pages(wiki_dir)
    rel_wiki_paths = {p.resolve().relative_to(root) for p in wiki_pages}

    must_index = [
        p
        for p in rel_wiki_paths
        if p.parts[0] == "wiki"
        and p.name not in ("index.md", "log.md")
        and not p.name.startswith(".")
    ]
    for p in must_index:
        if p not in index_targets:
            warnings.append(f"Index entry missing for {p} (add a markdown link in wiki/index.md)")

    if log_path.is_file():
        for i, line in enumerate(log_path.read_text(encoding="utf-8").splitlines(), start=1):
            if line.startswith("## ") and not line.startswith("### "):
                if not LOG_HEADING_PATTERN.match(line.strip()):
                    errors.append(
                        f"log.md line {i}: log heading must match "
                        r"`## [YYYY-MM-DD] ingest|query|lint|refactor|policy | Title`"
                    )

    titles: dict[str, list[str]] = defaultdict(list)
    inbound: dict[str, set[str]] = defaultdict(set)

    for page_path in wiki_pages:
        rel = page_path.resolve().relative_to(root)
        text = page_path.read_text(encoding="utf-8")
        fm, _ = load_frontmatter(text)

        name = page_path.name
        if rel.parent == Path("wiki") and name in ("index.md", "log.md", "overview.md"):
            pass
        elif not is_kebab_md(name):
            warnings.append(f"Filename should be kebab-case.md: {rel}")

        if requires_frontmatter_schema(rel):
            if not fm.get("title"):
                errors.append(f"Missing frontmatter 'title' for {rel}")
            if not fm.get("page_type"):
                errors.append(f"Missing frontmatter 'page_type' for {rel}")
            title_key = str(fm.get("title", "")).strip().lower()
            if title_key:
                titles[title_key].append(str(rel))

        for _label, target in extract_markdown_links(text):
            norm = normalize_link_target(target)
            if norm is None:
                continue
            resolved = resolve_markdown_path(page_path, norm, root)
            if resolved is None:
                continue
            if not resolved.is_file():
                if is_under_raw_dir(resolved, root):
                    continue
                errors.append(f"Broken link in {rel}: target {norm!r} -> {resolved}")
            rel_resolved = resolved.resolve().relative_to(root)
            inbound[str(rel_resolved)].add(str(rel))

        if rel.parts[:1] == ("wiki",):
            for pat in MUTABLE_RAW_PATTERNS:
                if pat.search(text):
                    warnings.append(
                        f"{rel}: possible misleading guidance about raw/ mutability (matched /{pat.pattern}/)"
                    )

    for t, paths in titles.items():
        if t and len(paths) > 1:
            warnings.append(f"Duplicate title (case-insensitive) {t!r}: {', '.join(paths)}")

    for p in must_index:
        ps = str(p)
        if p in index_targets:
            continue
        has_inbound = False
        for src, tgts in inbound.items():
            if ps in tgts and src != ps:
                has_inbound = True
                break
        if not has_inbound:
            warnings.append(f"Orphan page (not in index and no inbound wiki links): {p}")

    if args.raw_pdf_links:
        try:
            from validate_raw_pdf_links import run_checks
        except ImportError as e:  # pragma: no cover
            errors.append(f"Could not import validate_raw_pdf_links: {e}")
        else:
            r_errors, r_warnings = run_checks(
                root,
                wiki_raw_targets=True,
                source_note_extract_links=True,
                strict_local_raw=args.strict,
            )
            errors.extend(r_errors)
            if not args.strict:
                warnings.extend(r_warnings)

    return _finish(errors, warnings, args.strict)


def _finish(errors: list[str], warnings: list[str], strict: bool) -> int:
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    if errors:
        return 1
    if strict and warnings:
        print("Strict mode: warnings treated as failures.", file=sys.stderr)
        return 1
    if warnings and not strict:
        print(f"\n{len(warnings)} warning(s); use --strict to fail CI.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
