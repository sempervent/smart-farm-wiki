# Ingest workflow

**Goal:** Add sources to `raw/`, ground them in `wiki/source-notes/`, and update synthesis pages without mutating archived material.

**Git:** This repository may list `raw/**` in `.gitignore` so local source drops are not committed; only `**/.gitkeep` placeholders under `raw/` stay tracked to preserve directory layout. If your clone should track `raw/` in git, adjust `.gitignore` accordingly.

## Steps

1. **Drop or file raw content** under `raw/inbox/` — including **PDFs** and other binaries alongside markdown captures. After triage, move to `raw/processed/...` with stable **kebab-case** paths. Do not later rewrite processed text to “fix” meaning—add a new raw note if the source changes.

### PDF → Markdown (text extraction)

For **PDF** sources, generate a searchable Markdown extract beside the file (does **not** replace the PDF; no OCR for bitmap-only pages):

```bash
uv run python scripts/pdf_to_markdown.py raw/processed/2026/example.pdf
# or every PDF under raw/:
uv run python scripts/pdf_to_markdown.py --all-raw --force
```

Outputs `*-extracted.md` next to each `.pdf` with YAML frontmatter (`source_pdf`, `page_count`, `extracted` date) and per-page sections. **Verify** tables and layout against the PDF; link the extract from the matching `wiki/source-notes/` page if useful.
2. **Create or update a source-note** in `wiki/source-notes/` with frontmatter `page_type: source_note` and `source_ids` pointing at the raw path.
3. **Update entities, concepts, topics, analyses** as needed; add relative cross-links.
4. **Update `wiki/index.md`** so every intentional page is listed.
5. **Append `wiki/log.md`** with an `ingest` entry (`scripts/append_log.py` helps).
6. **Run** `uv run python scripts/validate_wiki.py --strict`.

When the full processed corpus (PDFs and `*-extracted.md` files) is present locally, also run **strict** raw checks:

```bash
uv run python scripts/validate_raw_pdf_links.py --strict
# or combined:
uv run python scripts/validate_wiki.py --strict --raw-pdf-links
```

**Policy:** `validate_raw_pdf_links.py` **without** `--strict` warns on missing local `raw/` targets and missing PDF extracts but **does not fail** (public CI). **`--strict`** fails when the corpus should be complete. Default CI runs `validate_wiki.py --strict` only (no `--raw-pdf-links`) and pytest invokes the raw script in non-strict mode. See [`docs/operations/raw-corpus-and-publishing.md`](../operations/raw-corpus-and-publishing.md).

## Done definition

Raw paths stable; source-notes and synthesis updated; index and log updated; validator clean.

See also: [`templates/ingest-checklist.md`](https://github.com/sempervent/llm-wiki-template/blob/main/templates/ingest-checklist.md) (in your clone: `templates/ingest-checklist.md`).
