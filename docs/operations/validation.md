# Validation

`scripts/validate_wiki.py` performs deterministic checks:

- Required repository files exist; `raw/` must exist as a directory (corpus files may be gitignored)
- `wiki/index.md` links cover all wiki pages (except `index.md` and `log.md`)
- `wiki/log.md` headings match `## [YYYY-MM-DD] kind | title`
- Internal markdown links resolve to existing files **except** targets under `raw/` — citation paths to the evidence corpus may be missing in public clones
- Frontmatter `title` and `page_type` on schema pages
- Kebab-case filenames (with exceptions for `index.md`, `log.md`, `overview.md`)
- Duplicate titles (heuristic) and orphan pages (warnings)
- Heuristic scan for misleading “mutable raw” language

Run locally:

```bash
uv sync
uv run python scripts/validate_wiki.py --strict
```

CI uses `--strict` so warnings fail the build.

## Integration quality (not a separate script)

`validate_wiki.py` checks **repository shape** and **link integrity** for the wiki tree. It does **not** automatically verify that:

- an ingest was **activated** into canonical pages, matrices, or hubs (`AGENTS.md` — **Ingest activation rule**);
- **Evidence summary** blocks exist on high-value **cluster** source-notes (`wiki/concepts/source-note-abstract-and-evidence-pattern.md`).

Treat **structural green + missing activation** as **debt**: fix in a follow-up or note scope in `wiki/log.md`.

## Raw references (`scripts/validate_raw_pdf_links.py`)

Validates PDF ↔ `*-extracted.md` pairing, wiki markdown links into `raw/`, and the source-note convention for PDFs. **Default (no `--strict`)**: missing local files under `raw/` are **warnings** only so public CI passes without the copyrighted corpus. **`--strict`**: treat those as **errors** when validating a full local tree.

See **[raw corpus and publishing](raw-corpus-and-publishing.md)** for Obsidian vs public site behavior and the MkDocs hook that neutralizes `raw/` links in the HTML build.
