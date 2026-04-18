---
title: Repository analysis (smart-farm-wiki)
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-18
review_status: unreviewed
tags:
  - meta
  - repository
  - tooling
confidence: high
---

# Repository analysis (smart-farm-wiki)

This page describes **what this repository is**, **how it is organized**, **how it is validated and published**, and **what the live wiki corpus looks like** at the time of writing. It complements the operator handbook ([`docs/architecture.md`](../../docs/architecture.md), [`docs/index.md`](../../docs/index.md)) by situating the **Smart Farm Wiki** content inside the **LLM-maintained wiki** pattern defined in [`AGENTS.md`](../../AGENTS.md) and [`README.md`](../../README.md).

## Purpose and lineage

- **Pattern**: Immutable **`raw/`** evidence, agent-maintained **`wiki/`** synthesis, human-facing **`docs/`** handbook (handbook is **not** part of the MkDocs site).
- **Upstream**: Template lineage is documented in [`README.md`](../../README.md) (`sempervent/llm-wiki-template`). This fork sets **`site_name`** to *Smart Farm Wiki* and **`site_description`** to an agriculture- and synthesis-oriented blurb in [`mkdocs.yml`](../../mkdocs.yml); the **GitHub remote** in that file points at **`sempervent/smart-farm-wiki`**.
- **Domain emphasis** (from topic hubs and source-notes): **small-scale and sustainable farming**, **livestock and homesteading**, **regional business and hobby-farm primers**, **field IoT** (LoRa, LoRaWAN, Meshtastic, Wi‑Fi HaLow), **off-grid power**, **homelab / Compose / Kubernetes**, **time sync (NTP/PTP)**, and **smart-home edge** topics—clustered for cross-linking, not as a single monolithic “farm manual.”

## Layer model (concise)

See the handbook’s diagram and table: [`docs/architecture.md`](../../docs/architecture.md). In short:

| Layer | Path | Published as HTML |
|-------|------|-------------------|
| Raw | `raw/` | No (provenance only; large corpus may be **gitignored** per repo policy—see [`README.md`](../../README.md)) |
| Wiki | `wiki/` | **Yes** — MkDocs `docs_dir` |
| Handbook | `docs/` | No (read in GitHub or editor) |
| Site output | `site/` | Build artifact (typically gitignored) |

## Corpus scale (approximate)

Counts are from the `wiki/` tree (Markdown files only):

| Area | Count | Role |
|------|------:|------|
| `source-notes/` | ~119 | Grounding notes pointing at `raw/processed/` (and related paths) |
| `topics/` | ~19 | Thematic hubs spanning concepts and sources |
| `concepts/` | ~11 | Definitions and term-of-art pages (includes mission/values) |
| `analyses/` | 13 | Query syntheses, research prompts, repo + domain overviews, equipment troubleshooting, timing + smart-mirror builds |
| `entities/` | 1 | Named-subject template/demo |
| `comparisons/` | 1 | Structured comparisons |
| `timelines/` | 1 | Chronology demo |
| `glossary/` | 1 | Definition-first entry |
| Root | `index.md`, `log.md`, `overview.md` | Catalog, append-only log, north-star overview |

**Total** wiki Markdown files: **~169** (including this page). The **bulk** of pages are **source-notes**, reflecting an ingest-heavy workflow.

## Tooling and contracts

- **`AGENTS.md`**: Highest-priority rules—ingest / query / lint, **`wiki/log.md`** append-only, immutability for processed raw, frontmatter and index expectations.
- **`scripts/`** (Python, `uv run`):
  - **`validate_wiki.py`** — Link resolution relative to repo root (wiki and repo-root files; links under **`raw/`** are not required to exist so CI works without the corpus), index coverage, log heading format, orphan hints, kebab-case, frontmatter for taxonomy pages; **`--strict`** promotes warnings (CI uses strict).
  - **`rebuild_index.py`** — Audit or regenerate index sections vs files on disk.
  - **`scaffold_page.py`** — New pages from `templates/`.
  - **`append_log.py`** — Correct `log.md` headings.
  - **`bootstrap.py`** — Directory scaffolding / renames.
  - **`wiki_common.py`** — Shared helpers for validators.
- **`tests/`** — Pytest coverage for validators and conventions (`test_validate_wiki.py`, `test_log_format.py`, `test_index_consistency.py`, `test_template_integrity.py`, `conftest.py`).
- **`pyproject.toml`** — `mkdocs` + `mkdocs-material`, `pymdown-extensions`, `pytest`, `PyYAML`; **`package = false`** (application repo, not an installable package).

## CI and publishing

- **`.github/workflows/ci.yml`** — On PR and push: `uv sync --frozen`, `validate_wiki.py --strict`, `pytest`, `mkdocs build --strict`.
- **`.github/workflows/docs.yml`** — On `main` (and manual dispatch): same checks, then **upload Pages artifact** and **deploy** to GitHub Pages.
- **`mkdocs.yml`** — `docs_dir: wiki`, Material theme, search plugin; **`validation.links.not_found: ignore`** so wiki citations to **`../../raw/...`** (outside the site tree) do not fail strict builds. Operator detail: [`docs/operations/publishing.md`](../../docs/operations/publishing.md).

## Strengths of the design

- **Inspectable**: Plain Markdown, relative links, git history; no opaque DB.
- **Deterministic checks**: Validator + tests gate merges; same commands locally as in CI.
- **Separation of concerns**: “How to run the wiki” lives in **`docs/`**; domain knowledge lives in **`wiki/`**; evidence in **`raw/`**.
- **Scalable ingest**: Source-notes pattern keeps provenance adjacent to synthesis.

## Risks and limitations

- **Raw not in clone**: If `raw/**` is excluded from git, **links from wiki to raw** remain valid **in-repo** for developers with files present but will **404** on the **published** site for those paths—by design the static site does not ship the raw corpus.
- **MkDocs vs validator**: The wiki validator resolves links to the **repository**; MkDocs intentionally **does not** require every `raw/` link to exist in `docs_dir`. Do not “fix” wiki links to fake pages under `wiki/` solely to satisfy MkDocs—use `validation` config and keep citations honest.
- **Corpus skew**: Heavy **source-note** count means **topic/ concept** coverage is uneven; **`wiki/index.md`** is the intentional navigation backstop—orphans are reported by the validator for cleanup.

## Where to go next

| Goal | Location |
|------|----------|
| Operator quickstart | [`docs/quickstart.md`](../../docs/quickstart.md) |
| Workflows | [`ingest`](../../docs/workflows/ingest.md), [`query`](../../docs/workflows/query.md), [`lint`](../../docs/workflows/lint.md) |
| Handbook index | [`docs/index.md`](../../docs/index.md) |
| Wiki catalog | [`index.md`](../index.md) |
| Chronology | [`log.md`](../log.md) |
| Domain overview (vault purpose) | [`overview.md`](../overview.md) |

---

*This analysis is a snapshot; when repository structure or policy changes materially, update this page and append [`log.md`](../log.md).*
