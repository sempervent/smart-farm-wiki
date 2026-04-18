---
title: Local site and county intelligence (East Tennessee two-site)
page_type: topic
status: active
created: 2026-04-22
updated: 2026-04-25
tags:
  - two-site
  - tennessee
  - anderson-county
  - campbell-county
  - routing
review_status: unreviewed
confidence: high
---

# Local site and county intelligence (East Tennessee two-site)

**Purpose**: Route readers from the **general** business plan into the **named** **Anderson** / **Campbell** **county** and **Claxton** / **Demory** **site** layer—without duplicating analyses. **Pair with** the **agency/extension** catalog: [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) (tables of ingested sources); **IA note** on why evidence can feel hard to spot: [`Ingest visibility gap — authoritative evidence vs published wiki (East Tennessee)`](../analyses/ingest-visibility-gap-authoritative-evidence-east-tennessee.md).

**Why this layer exists**: The package defaults (**~35 min** split, grazing-led thesis, validation **V\*** gates) need **local** **grounding**. **County** statistics (e.g. NASS rent **estimates**) set **ballpark** economics; **site** intelligence ties evidence to **`SITE_HOME`** vs **`SITE_FARM`**; **parcel** truth still **requires** field work—see [`missing data register`](../analyses/claxton-and-demory-missing-data-register.md).

**Entry from the plan**: [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) → this page → pages below. **Operations + telemetry hub** (unchanged): [`Two-site smart farm operations`](two-site-smart-farm-operations.md).

---

## What this hub owns

- **Routing** from **abstract** `SITE_HOME` / `SITE_FARM` roles to **named** places (**Claxton**, **Demory**), **county** context, **parcel** worksheets, and **gap** registers.
- **Links** to the **authoritative evidence** index (NASS, WSS, agency PDFs)—not duplicate tables from [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md).

## Start here

| Goal | Page |
|------|------|
| **County + site map (this page)** | You are here — use **Route map** below |
| **Field baselines** (measured loads, infra, utilities) | [`Local evidence package — East Tennessee two-site`](local-evidence-package-east-tennessee-two-site.md) |
| **Parcel structure** | [`Parcel intelligence package — East Tennessee two-site`](parcel-intelligence-package-east-tennessee-two-site.md) |
| **What evidence is still missing** | [`Claxton and Demory — missing data register`](../analyses/claxton-and-demory-missing-data-register.md) |

## Canonical vs supporting

| **Canonical** | **Supporting** |
|---------------|----------------|
| **Entities**: counties, places, `SITE_*` roles (linked in Route map) | **Site intelligence** analyses (known/assumed/unknown narrative) |
| [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) | [`Execution readiness gap audit`](../analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md) |
| [`Parcel intelligence package`](parcel-intelligence-package-east-tennessee-two-site.md) (hub) | Individual parcel worksheets |

---

## How to read this layer (kinds of page)

| Kind | What it is | Examples |
|------|------------|----------|
| **County context** | **Survey / regional** stats—not your deed | NASS rows; [`county comparison`](../comparisons/anderson-county-vs-campbell-county-operating-implications.md) |
| **Site / entity** | **Planning roles** and **named place anchors** | [`SITE_HOME`](../entities/five-acre-home-base-site-home-et-two-site.md), [`SITE_FARM`](../entities/120-acre-production-farm-site-farm-et-two-site.md); places [`Claxton`](../entities/claxton-home-base.md), [`Demory`](../entities/demory-farm-site.md) |
| **Execution-facing analyses** | **Known / assumed / unknown** + implications | [`Claxton…`](../analyses/claxton-home-base-site-intelligence.md), [`Demory…`](../analyses/demory-farm-site-intelligence.md) |
| **Parcel worksheets** | **Field tables** for deed/WSS/utilities—**placeholders** until evidence | [`Parcel intelligence package`](../topics/parcel-intelligence-package-east-tennessee-two-site.md) |
| **Local evidence package** | **Measured / reported / unknown** tables for **on-the-ground** inventory (not county stats)—**absorbs** field facts cleanly | [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md) (`SITE_HOME` / `SITE_FARM` baselines, infra, utilities, loads, field templates, parcel workflow) |
| **Unresolved data** | **Gaps** the vault **cannot** fill from files alone | [`missing data register`](../analyses/claxton-and-demory-missing-data-register.md) |

---

## Route map

### County context (compare + evidence index)

| Topic | Page |
|-------|------|
| **Anderson County (operating object)** | [`Anderson County, Tennessee (two-site context)`](../entities/anderson-county-tennessee.md) |
| **Campbell County (operating object)** | [`Campbell County, Tennessee (two-site context)`](../entities/campbell-county-tennessee.md) |
| **Anderson vs Campbell — operating tradeoffs** | [`Anderson County vs Campbell County — two-site operating implications`](../comparisons/anderson-county-vs-campbell-county-operating-implications.md) |
| **Agency/extension ingests** (NASS, WSS captures, DOR, FSA, septic, CISA…) | [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) |
| **Strategic “what’s still missing”** (execution-grade) | [`Execution readiness gap audit`](../analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md) |

### Anderson County + Claxton (`SITE_HOME`)

| Topic | Page |
|-------|------|
| **Entity (planning role)** | [`Five-acre home base (SITE_HOME) — ET two-site`](../entities/five-acre-home-base-site-home-et-two-site.md) |
| **Place anchor** | [`Claxton home base (place)`](../entities/claxton-home-base.md) |
| **Site intelligence** | [`Claxton home base — site intelligence (Anderson County)`](../analyses/claxton-home-base-site-intelligence.md) |
| **Site inventory baseline (field recon)** | [`Site inventory baseline — Claxton home base`](../analyses/site-inventory-baseline-claxton-home-base-east-tennessee.md) |
| **Parcel worksheet** | [`Parcel intelligence — Claxton home base`](../analyses/parcel-intelligence-claxton-home-base-east-tennessee-two-site.md) |

### Campbell County + Demory (`SITE_FARM`)

| Topic | Page |
|-------|------|
| **Entity (planning role)** | [`120-acre production farm (SITE_FARM) — ET two-site`](../entities/120-acre-production-farm-site-farm-et-two-site.md) |
| **Place anchor** | [`Demory farm site (place)`](../entities/demory-farm-site.md) |
| **Site intelligence** | [`Demory farm — site intelligence (Campbell County)`](../analyses/demory-farm-site-intelligence.md) |
| **Site inventory baseline (field recon)** | [`Site inventory baseline — Demory farm site`](../analyses/site-inventory-baseline-demory-farm-site-east-tennessee.md) |
| **Parcel worksheet** | [`Parcel intelligence — Demory farm site`](../analyses/parcel-intelligence-demory-farm-site-east-tennessee-two-site.md) |
| **Farm sensor architecture (long-range, WAN-optional)** | [`Farm sensor architecture — Demory farm site`](../analyses/farm-sensor-architecture-demory-farm-site.md); [`Sensor checklist matrix — Demory farm`](../analyses/sensor-checklist-matrix-for-demory-farm.md) |
| **Utility locate — Tennessee 811** | [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md) (TN811 captures; **not** legal advice) |

### Validation and gaps

| Topic | Page |
|-------|------|
| **First 24 months — proofs and pilots** | [`Validation and pilot plan — first 24 months`](../analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) |
| **Backlog tasks + gates** | [`Validation backlog and decision gates`](../analyses/east-tennessee-two-site-farm-business-plan-validation-backlog.md) |
| **Parcel unknowns register** | [`Claxton and Demory — missing data register`](../analyses/claxton-and-demory-missing-data-register.md) |

---

## Related

- [`Business plan execution and pilot operations hub`](business-plan-execution-and-pilot-operations-hub.md) — validation when site evidence gates **G\*/V\***
- [`Off-grid power and field networking hub`](off-grid-power-and-field-networking-hub.md) — **`SITE_FARM`** Demory doctrine entry
- [`Domain content overview`](../analyses/domain-content-overview.md) — strand map; local evidence **feeds** Strand **B** and **A** decisions
- [`Farm parcels and land units`](../entities/farm-parcels-and-land-units.md) — IDs and **authority chain**
