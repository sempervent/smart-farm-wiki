---
title: Parcel evidence intake and validation workflow — two-site
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - two-site
  - parcel
  - workflow
  - provenance
  - execution
review_status: unreviewed
confidence: high
---

# Parcel evidence intake and validation workflow — two-site

**Purpose**: **Deterministic** path from **field / desk evidence** → **`raw/`** → **source-notes** → **parcel worksheets** and **site baselines**—without **inventing** boundaries, APNs, or utility facts.

**Hub**: [`Parcel intelligence package — East Tennessee two-site`](../topics/parcel-intelligence-package-east-tennessee-two-site.md).

**Local evidence package**: [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md).

**Worksheets**: [`Parcel intelligence — Claxton home base`](../analyses/parcel-intelligence-claxton-home-base-east-tennessee-two-site.md) · [`Parcel intelligence — Demory farm site`](../analyses/parcel-intelligence-demory-farm-site-east-tennessee-two-site.md).

---

## What counts as evidence

| Tier | Examples | Wiki treatment |
|------|----------|----------------|
| **Primary** | Deed, recorded plat, survey, well permit, stamped engineering | Cite `raw/` path; quote short legal only with care |
| **Secondary** | County GIS print, tax card, FSA map | **Reported**—note capture date and layer |
| **Tertiary** | Satellite, neighbor statement | **Reported** or **assumption**—**field verify** for fences |

---

## Intake steps

1. **Drop** immutable file under `raw/inbox/` (or pipeline per [`docs/workflows/ingest.md`](../../docs/workflows/ingest.md)); **do not** rewrite processed sources.
2. **Create or update** `wiki/source-notes/<stable-name>.md` with **frontmatter** `source_ids` / path and **what** the file **does** and **does not** prove.
3. **Update** the **parcel worksheet** row: **Fact class** (measured / reported / assumption / unknown), **source**, **date**.
4. **Cross-link** **site inventory** / **infrastructure** / **utility** baselines when the fact is **operational** (gate width, easement width)—**not** duplicate legal description on every page.
5. **Append** [`wiki/log.md`](../log.md) **`ingest`** entry.
6. Run **`uv run python scripts/validate_wiki.py`**.

---

## Validation rules (two-site)

| Check | Pass criteria |
|-------|----------------|
| **APN / deed alignment** | Single **authoritative** line in worksheet; conflicts get **dated** note + **confidence** |
| **Acreage** | **NASS** / **WSS** stay on [`site intelligence`](../analyses/demory-farm-site-intelligence.md); **worksheet** may hold **field** **measured** sub-areas |
| **Utility account** | **Not** in wiki in full—**redacted** in `raw/`; wiki lists **provider** + **unknowns** only |
| **Fence = parcel line?** | **Never** assumed—**Unknown** until survey or corner tie |

---

## Conflict handling

If new evidence **contradicts** an old row: **do not** silent delete—add **dated** subsection on worksheet or [`missing data register`](claxton-and-demory-missing-data-register.md) with **supersedes** pointer and **review_status** if needed.

---

## Decision gates

| Decision | Blocked until |
|----------|----------------|
| Capital fence line | **Survey** or **staked** agreement + **title** review |
| Permanent water line easement | **Recorded** easement or **deed** **language** |
| Official farm address for permits | **County** / **911** **confirmed** |

---

## Related

- [`Site inventory — Claxton`](site-inventory-baseline-claxton-home-base-east-tennessee.md) · [`Site inventory — Demory`](site-inventory-baseline-demory-farm-site-east-tennessee.md) · [`Infrastructure baseline`](infrastructure-inventory-baseline-two-sites-east-tennessee.md) · [`Utility baseline`](utility-and-service-baseline-two-sites-east-tennessee.md)
