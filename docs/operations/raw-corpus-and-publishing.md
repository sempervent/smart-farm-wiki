# Raw corpus, Obsidian authoring, and public publishing

## Why `raw/` may be absent from git

Copyrighted **source artifacts** (PDFs, full imports) are often **not committed** to the public repository. The wiki still records **provenance** with relative markdown links such as ``[`source`](../../raw/processed/2026/example.pdf)`` so that:

- **Locally**, with a full `raw/` tree, Obsidian and other editors resolve those paths for the repository owner.
- **Public CI** clones do not need those files on disk for validation or MkDocs to succeed.

## What public CI validates (default)

| Check | Behavior |
|-------|----------|
| `uv run python scripts/validate_wiki.py --strict` | Wiki link integrity **except** targets under `raw/` (may be missing). Structural rules, index, frontmatter, etc. |
| `uv run pytest` | Includes `scripts/validate_raw_pdf_links.py` **without** `--strict`: missing local PDF/extract pairs and missing wiki `raw/` targets are **warnings**, not failures. |
| Source-note convention | PDF in `source_ids` **must** include a body link to the corresponding `*-extracted.md` **pattern** (structural check; still fails if malformed). |

## Strict / local validation (optional)

When the full evidence corpus is present (private machine or optional CI job):

```bash
uv run python scripts/validate_raw_pdf_links.py --strict
# or
uv run python scripts/validate_wiki.py --strict --raw-pdf-links
```

`--strict` promotes **missing** local `raw/` link targets and **missing** PDF `*-extracted.md` sidecars from warnings to **errors**.

## Public MkDocs site: no broken `raw/` links

`mkdocs.yml` registers a **hook** (`scripts/mkdocs_neutralize_raw_links.py`) that rewrites markdown links whose targets contain `raw/` into a non-navigable `<span class="raw-source-ref">` with a **title** showing the path. Obsidian **source files are unchanged**; only the **built HTML** is affected.

Styling: `wiki/stylesheets/raw-source-refs.css`.

## Obsidian workflow

Keep authoring **normal markdown links** to `raw/` as today. They remain clickable in Obsidian when the files exist locally. The published site shows italic/help-styled text instead of a broken hyperlink.

**Evidence summary blocks** on source-notes should phrase **key claims** so they stay intelligible when `raw/` links are neutralized in HTML—cite **authority** (agency, vendor doc, statute) in prose, not only paths (`wiki/concepts/source-note-abstract-and-evidence-pattern.md`).

## Related

- [`validation.md`](validation.md) — full validator reference  
- [`publishing.md`](publishing.md) — MkDocs / GitHub Pages  
- [`../workflows/ingest.md`](../workflows/ingest.md) — ingest and PDF extracts
