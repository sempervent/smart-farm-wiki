# AGENTS.md — Operating contract

This file is the **highest-priority behavioral contract** for any automated or human agent working in this repository. When instructions conflict, **follow this document first**, then `README.md`, then task-specific prompts.

---

## Mission

This repository implements an **LLM-maintained markdown wiki**: a persistent, compounding knowledge base where:

- **`raw/`** holds **immutable** source material (notes, imports, excerpts, files).
- **`wiki/`** holds the **agent-authored synthesis** (entities, concepts, analyses, cross-links).
- **`docs/`** holds the **operator handbook** for humans and agents (read in-repo); it explains *how* the system works, not the domain knowledge itself. (In this fork, the **MkDocs site** is built from **`wiki/`** only; see `mkdocs.yml` and `docs/operations/publishing.md`.)

The **mechanical goal** is **deterministic, inspectable, markdown-first** workflows: plain files, clear paths, validation scripts, and reproducible doc builds.

### Domain mission and prose (Smart Farm Wiki)

**Why not duplicate long mission prose here:** `AGENTS.md` must stay a **short, stable contract**—rules agents load every session. **Mission statements, audience, values, and voice** belong in the wiki so they **version with synthesis**, appear on the **published site**, and can evolve without bloating the contract file.

**Canonical page:** [`wiki/concepts/smart-farm-wiki-mission-and-values.md`](wiki/concepts/smart-farm-wiki-mission-and-values.md) — mission, vision, audience, authoring values, and voice. Agents shaping **tone** or **scope** for new pages should read it alongside [`wiki/overview.md`](wiki/overview.md).

**Reasoning summary:** Separation keeps **behavioral law** (this file) distinct from **intellectual purpose** (wiki)—reducing merge conflict on policy vs prose, and keeping “what we believe about small-scale ag and appropriate technology” **editable by the same ingest/query workflow** as other concepts.

---

## Layer definitions

| Layer | Purpose | Mutable by agent? |
|-------|---------|-------------------|
| `raw/` | Provenance-grounded sources (markdown imports, **PDFs**, and other files); inbox → processed pipeline | **Append / file new sources only. Never edit processed or alter meaning of stored sources.** |
| `wiki/` | Structured knowledge pages, index, log | **Yes**, following rules below |
| `docs/` | Template handbook, architecture, workflows (MkDocs) | **Yes**, when improving operator documentation |
| `scripts/` | Validation and scaffolding | **Yes**, with tests and clear CLI contracts |
| `examples/` | Small worked examples (isolated from production paths) | **Yes**, keep realistic but minimal |

**Do not** treat `examples/` as the live wiki unless the user explicitly asks to promote content.

---

## File ownership model

- **Human or policy owner**: `AGENTS.md`, licensing, and high-level conventions. Agents may propose edits via PRs or patches; destructive convention changes require explicit intent.
- **Agent maintainer**: `wiki/**/*.md` (except obey immutability rules for any symlinked content), `wiki/index.md`, `wiki/log.md`.
- **Build / CI**: `.github/workflows/*`, `mkdocs.yml`, `pyproject.toml`, `uv.lock`.
- **Raw corpus**: files under `raw/processed/` are **write-once** after processing; `raw/inbox/` accepts new drops.

---

## Mandatory workflows

### Ingest

1. Add or confirm raw material under `raw/inbox/` (or processed pipeline per `docs/workflows/ingest.md`).
   - **PDFs** are first-class sources: move each to `raw/processed/...` under a stable **kebab-case** basename, run `uv run python scripts/pdf_to_markdown.py <path-to.pdf>` (or `--all-raw`) so a sibling **`*-extracted.md`** machine extract exists; the **PDF remains canonical** for figures and layout. Source-notes for PDFs must cite **both** the `.pdf` and the `*-extracted.md` in the body (and `source_ids` includes the `.pdf` path). See `docs/workflows/ingest.md` and `scripts/validate_raw_pdf_links.py` / `validate_wiki.py --raw-pdf-links` when the full corpus is local.
2. Create or update **`source-notes`** in `wiki/source-notes/` pointing to stable `raw/` paths.
3. Update relevant entity/concept/topic pages; add cross-links.
4. **Append** `wiki/log.md` with `ingest` entry (see Log format).
5. **Update** `wiki/index.md` if new pages were added or titles changed.
6. Run `uv run python scripts/validate_wiki.py` before commit.

### Query

1. Answer from `wiki/` + cited `raw/` paths; do not invent provenance.
2. If the answer should persist, **create or update** a durable wiki page (often `analyses/` or `concepts/`) and link it from `index.md` when appropriate.
3. **Append** `wiki/log.md` with `query` entry summarizing the question and where the answer lives.

### Lint

Periodic hygiene: link integrity, orphan reduction, stale-claim review, duplicate title checks, index alignment.

1. Run `uv run python scripts/validate_wiki.py` (use `--strict` in CI).
2. Fix or ticket broken links; add missing index entries for intentional pages.
3. **Append** `wiki/log.md` with `lint` entry.

---

## Maintaining `wiki/index.md`

- `index.md` is the **catalog and navigation surface** agents should read first.
- Organize by **page category** (overview, entities, concepts, topics, source-notes, analyses, comparisons, timelines, glossary).
- Each entry: **relative link** + **one-line description**.
- After adding/removing/renaming pages, update `index.md`. Run `uv run python scripts/rebuild_index.py` to compare index links to files on disk.

---

## Maintaining `wiki/log.md`

- **Append-only**: never rewrite or delete historical entries.
- New entries go **below** prior content unless the user explicitly migrates format (then log the migration in a new `policy` entry).
- Heading format (required):

```markdown
## [YYYY-MM-DD] ingest | Short source or batch title
## [YYYY-MM-DD] query | Short question summary
## [YYYY-MM-DD] lint | What was checked
## [YYYY-MM-DD] refactor | Scope of reorganization
## [YYYY-MM-DD] policy | Convention or AGENTS change
```

- Body: bullet summary of actions, files touched, and pointers to durable pages.

---

## Page taxonomy

Standard directories under `wiki/`:

| `page_type` | Typical path | Role |
|-------------|--------------|------|
| `overview` | `overview.md` | North-star summary of the wiki’s domain |
| `source_note` | `source-notes/` | Grounding note for a raw source |
| `entity` | `entities/` | Named subject (person, org, product, paper) |
| `concept` | `concepts/` | Idea or term of art |
| `topic` | `topics/` | Thematic bucket spanning entities/concepts |
| `analysis` | `analyses/` | Argument, evaluation, synthesis |
| `comparison` | `comparisons/` | Structured A vs B |
| `timeline` | `timelines/` | Chronology |
| `glossary` | `glossary/` | Definition-first entries |
| `operating_doc` | (rare; or root) | How the repo itself is operated |

---

## Naming conventions

- **Filenames**: `kebab-case.md` exclusively.
- **Titles**: Sentence case or title case — **one canonical title per page** in `title` frontmatter.
- **Stability**: Prefer renaming by adding `aliases` frontmatter and updating links; avoid churn.

---

## Linking conventions

- Use **relative Markdown links** only: `[text](../concepts/foo.md)` not absolute repo paths.
- **Obsidian**: `[[wiki links]]` optional; portable links must still exist as `.md` relatives for MkDocs-oriented tooling.
- **Wikilinks**: If you use `[[...]]`, ensure a parallel `.md` relative link exists for non-Obsidian consumers (CI may optionally enforce this later).

---

## Citation conventions

- When a claim depends on a raw source, cite **stable path + optional excerpt id**:

```markdown
See [raw/processed/2026/example.md](../../raw/processed/2026/example.md) — section “Key finding”.
```

- Prefer `source_ids` in frontmatter for machine-checkable linkage.

---

## Frontmatter schema

Optional YAML frontmatter is encouraged. Common fields:

| Field | Meaning |
|-------|---------|
| `title` | Display title (should match index) |
| `page_type` | One of the taxonomy types |
| `status` | `draft` \| `active` \| `deprecated` |
| `created` | ISO date |
| `updated` | ISO date |
| `source_count` | Integer (optional) |
| `source_ids` | List of stable ids or raw paths |
| `aliases` | Alternate titles |
| `tags` | List of short tokens |
| `supersedes` / `superseded_by` | For deprecation chains |
| `confidence` | `low` \| `medium` \| `high` (epistemic) |
| `review_status` | `unreviewed` \| `reviewed` \| `stale` |

**Rules**:

- `wiki/overview.md`, entity/concept/analysis/comparison/timeline pages: **must** include `title` and `page_type` for validation.
- `wiki/log.md` and `wiki/index.md`: **no** required frontmatter.

---

## Conflict and contradiction handling

- **Do not silently overwrite** competing claims. Prefer:
  - same page: add dated subsection with evidence and confidence; or
  - split: new analysis page with `supersedes` linkage.
- Call out unresolved tension explicitly; log significant merges in `log.md`.

---

## Stale-claim handling

- Mark uncertain or dated material with `review_status: stale` or a visible callout.
- Prefer incremental updates; if replacing, use `superseded_by` and keep a short redirect note in the old page body.

---

## Orphan page handling

- A page is **orphan** if no other wiki page links to it **and** it is not listed in `index.md`. Validation reports orphans; fix by adding inbound links or index entries.

---

## Proposing new pages

1. Pick `page_type` and path per taxonomy.
2. Copy from `templates/` using `uv run python scripts/scaffold_page.py`.
3. Fill frontmatter, write minimal viable content, cross-link, update `index.md`, append `log.md`.

---

## Filing answers back into the wiki

- Ephemeral chat answers → durable **`analyses/`** or **`concepts/`** page when reuse is likely.
- Include **question context**, **answer summary**, **links** to sources and related wiki pages.
- Log under `query` with pointer to the new page.

---

## Incremental maintenance

- **Prefer small, frequent edits** over full rewrites.
- When refactoring, batch by theme; log under `refactor`.
- Reserve large-scale reorg for explicit user approval.

---

## Raw sources are immutable

- **Never** edit files in `raw/processed/` except **append-only** logs if a dedicated log file exists and policy allows.
- Corrections belong in **wiki** or new raw notes with clear provenance, not silent fixes to archived sources.

---

## Log is append-only history

- Do not delete or rewrite past `## [...]` entries in `wiki/log.md`.
- Typo fixes: only if they do not change meaning; prefer a new correction entry.

---

## Preserving user intent and provenance

- Follow explicit user instructions for scope and tone.
- When summarizing sources, preserve distinctions the user cares about.
- Prefer quoting short phrases from raw over paraphrase when ambiguity is high.

---

## Relative links for Obsidian and MkDocs

- Wiki links must work when opened as a folder vault in Obsidian **and** when processed by static analyzers.
- Avoid spaces in filenames; use `kebab-case.md`.
- For assets, prefer `raw/assets/` or documented attachment paths in `docs/operations/obsidian.md`.

---

## Agent session checklist

1. Read `AGENTS.md` (this file) and `wiki/index.md`. When authoring substantive **domain** synthesis, also read [`wiki/concepts/smart-farm-wiki-mission-and-values.md`](wiki/concepts/smart-farm-wiki-mission-and-values.md) for mission, audience, and voice alignment.
2. Identify layer: raw vs wiki vs docs change.
3. Run `uv run python scripts/validate_wiki.py` before and after substantive edits.
4. Update `wiki/index.md` when navigation should change.
5. Append `wiki/log.md` for ingest/query/lint/refactor/policy work.
6. Keep commits scoped and messages descriptive.

---

## Definition of done

| Task | Done when |
|------|-----------|
| **Ingest** | Raw filed (for **PDFs**: sibling `*-extracted.md` + source-note cites both); source-notes + synthesis updated; log + index updated; validator passes; run `--raw-pdf-links` when the full `raw/` corpus is present locally |
| **Query** | Answer cites wiki/raw; durable page created/updated if needed; log appended |
| **Lint** | Validator clean (`--strict` in CI); orphans/titles addressed or explicitly deferred in log |

---

## Scripts reference

| Script | Role |
|--------|------|
| `scripts/bootstrap.py` | Create missing dirs/files; optional rename placeholders |
| `scripts/validate_wiki.py` | Repository integrity checks; links under `raw/` need not resolve by default (corpus may be uncommitted); optional `--raw-pdf-links` when corpus is local |
| `scripts/validate_raw_pdf_links.py` | PDF ↔ `*-extracted.md` pairing, wiki links into `raw/`, PDF source-note extract links (also via `validate_wiki.py --raw-pdf-links`) |
| `scripts/rebuild_index.py` | Audit or regenerate index sections |
| `scripts/append_log.py` | Append a correctly formatted log entry |
| `scripts/scaffold_page.py` | New page from `templates/` |
| `scripts/pdf_to_markdown.py` | PDF text → `*-extracted.md` beside the file (PyMuPDF; not OCR) |

---

## Non-goals

- Opaque databases, proprietary formats, or undocumented codegen as the source of truth.
- Turning `wiki/` into an unbounded dump without structure.

When uncertain, **add a note in the wiki**, **cite raw**, and **log the decision**.
