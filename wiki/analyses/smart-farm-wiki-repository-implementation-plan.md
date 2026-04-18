---
title: Smart Farm Wiki — repository implementation plan (business plan integration)
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-18
review_status: unreviewed
tags:
  - meta
  - information-architecture
  - business-plan
  - two-site
confidence: medium
aliases:
  - Wiki implementation plan business plan
---

# Smart Farm Wiki — repository implementation plan (business plan integration)

## 1. Implementation summary

The **East Tennessee two-site farm business plan** and **operational artifacts** are largely **already implemented** under `wiki/analyses/` with **index** and **knowledge-synthesis** entry points. What remains is **structural**: a **dedicated topic hub** (hub-and-spoke) so the business-plan cluster is discoverable without reading `index.md` linearly; **tight links** from **overview**, **domain content overview**, and **strategic implementation backlog**; optional **secondary topic hubs** from [`information-architecture-decision-safe-operations`](information-architecture-decision-safe-operations.md) only where they **add navigation** without **duplicating** analyses.

**Principles**

- **No ornamental pages**: one **two-site operations topic** hub, not a duplicate “summary of summaries.”
- **Foundational first**: hub + inbound links + `overview.md` **before** optional telemetry/security topic splits.
- **Evidence later**: numeric **CAPEX**, **revenue**, **salary** targets stay **placeholders** until **family** supplies data; wiki tracks **validation IDs** instead of inventing numbers.

---

## 2. Proposed file tree

### New files to create

| Path | Role |
|------|------|
| `wiki/topics/two-site-smart-farm-operations.md` | **Topic hub**: spokes to ET business plan framework, dual-site ops models, operational artifacts, runbooks, comparisons—**single** navigation surface for “5 ac + 120 ac + telemetry.” |

**Optional later** (only if navigation pressure justifies; analyses already cover substance):

| Path | Role |
|------|------|
| `wiki/topics/field-telemetry-and-backhaul.md` | Hub: field telemetry ref arch, LoRa/MQTT topic, instrumentation matrix, comparisons—**avoid** if [`knowledge-synthesis`](../topics/knowledge-synthesis.md) + analyses suffice. |
| `wiki/topics/spatial-data-and-farm-map-hygiene.md` | Hub: farm spatial model, PostGIS/farm data topic, registry standard—**optional**. |

### Existing files to update (inbound links / one section each)

| Path | Update |
|------|--------|
| [`wiki/overview.md`](../overview.md) | Add bullet: ET two-site **business plan hub** + topic hub (when created). |
| [`wiki/index.md`](../index.md) | Under **Topics**, add **Two-site smart farm operations** entry; keep **Analyses** list in sync. |
| [`wiki/analyses/domain-content-overview.md`](domain-content-overview.md) | Short pointer under business/strand to **planning framework** + topic hub. |
| [`wiki/analyses/information-architecture-decision-safe-operations.md`](information-architecture-decision-safe-operations.md) | Mark **two-site topic hub** as **shipped** or link file when created. |
| [`wiki/analyses/implementation-backlog-strategic-audit.md`](implementation-backlog-strategic-audit.md) | Cross-link **operational artifacts** + **hostile review** as **done** / **next** as appropriate. |
| [`wiki/topics/knowledge-synthesis.md`](../topics/knowledge-synthesis.md) | Add **topic hub** link alongside existing business-plan bullets. |
| [`wiki/analyses/east-tennessee-two-site-farm-business-plan-framework.md`](east-tennessee-two-site-farm-business-plan-framework.md) | Add **“Topic hub”** outbound link in Links section when `two-site-smart-farm-operations.md` exists. |

**Do not create** separate pages for: executive summary duplicate, third “index of the index,” or per-strand business-plan copies.

---

## 3. Page-by-page change plan

Status: **exists** = already in repo; **planned** = recommended next edit.

| Filename | Title | page_type | Purpose | Dependencies | Key outbound links | Key inbound to add |
|----------|-------|-----------|---------|--------------|--------------------|--------------------|
| `topics/two-site-smart-farm-operations.md` | Two-site smart farm operations | topic | **Navigation hub** for 5 ac home base + 120 ac production + plan + artifacts + runbooks | ET framework, dual-site analyses | Framework, executive summary, recommended strategy, `two-site-operations-model-5ac-*`, field telemetry ref arch, hostile review, validation backlog | From `overview.md`, `domain-content-overview.md`, `knowledge-synthesis.md`, `framework.md` |
| `overview.md` | Wiki overview | overview | North-star entry | — | +1 bullet: two-site business plan + topic hub | — |
| `index.md` | Wiki index | meta | Catalog | — | Topic entry for hub | — |
| `analyses/domain-content-overview.md` | Domain content overview | analysis | Strand steering | — | Link to ET framework or topic hub under business strand | From hub “related” |
| `analyses/information-architecture-decision-safe-operations.md` | Information architecture — decision-safe operational brain | analysis | IA target | — | Update “first drafts” / hub list with **topic** path | — |
| `analyses/implementation-backlog-strategic-audit.md` | Implementation backlog — strategic audit | analysis | P0–P3 build list | — | Point to completed operational artifacts + hostile review | — |
| `topics/knowledge-synthesis.md` | Knowledge synthesis | topic | Cross-cutting entry | — | Topic hub URL | — |
| `analyses/east-tennessee-two-site-farm-business-plan-framework.md` | ET two-site farm business plan — planning framework | analysis | Plan hub | — | `topics/two-site-smart-farm-operations.md` | — |

**Already exists (no new file; optional incremental edits only)**

| Filename | Notes |
|----------|--------|
| `analyses/east-tennessee-two-site-farm-business-plan-*.md` (13 files) | Business plan package—**stable**; revise only when **hostile review** or **validation** closes items. |
| `analyses/two-site-operations-model-5ac-homebase-120ac-production.md` etc. (8 artifacts) | Operational matrices—**fill** placeholders over time. |
| `analyses/*runbook*.md` | SOP-class analyses—link from topic hub. |
| `comparisons/lorawan-vs-meshtastic-*.md` (4 files) | Linked from smart-tech + hub. |

---

## 4. Minimum coherent merge set (one PR)

The **smallest** change set that makes the business-plan work **structurally navigable**:

1. **Create** [`wiki/topics/two-site-smart-farm-operations.md`](../topics/two-site-smart-farm-operations.md) — **done**: hub-and-spoke tables, links only.
2. **Update** [`wiki/overview.md`](../overview.md) — **done**: bullet 7 for two-site plan + implementation plan.
3. **Update** [`wiki/index.md`](../index.md) — **done**: Topics entry.
4. **Update** [`wiki/topics/knowledge-synthesis.md`](../topics/knowledge-synthesis.md) — **done**: topic hub link.
5. **Update** [`wiki/analyses/east-tennessee-two-site-farm-business-plan-framework.md`](east-tennessee-two-site-farm-business-plan-framework.md) — **done**: “Topic hub” section.
6. **Append** [`wiki/log.md`](../log.md) — **pending** on merge: `refactor | Topic hub + implementation plan`.

**Remaining optional** from this set: patch `domain-content-overview`, `information-architecture-*`, `implementation-backlog-strategic-audit` per Phase B.

Run `uv run python scripts/validate_wiki.py --strict`.

This is **foundational navigation**; it does **not** require filling **numeric** placeholders.

---

## 5. Phased execution order

| Phase | Scope | Outcome |
|-------|--------|---------|
| **A — Navigation (P0)** | Minimum coherent merge set above | Hub-and-spoke **discoverable** |
| **B — IA alignment (P1)** | Patch `domain-content-overview`, `information-architecture-*`, `implementation-backlog-strategic-audit` | Strategic docs **reflect** shipped pages |
| **C — Evidence binding (P1)** | Where plan cites **validation**, ensure [`validation-backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md) IDs match [`validation-backlog-before-major-spend`](validation-backlog-before-major-spend-two-site-smart-farm.md) **G*** gates | Traceable **gates** |
| **D — Optional topic hubs (P2)** | `field-telemetry-and-backhaul`, `spatial-data-and-farm-map-hygiene` **only** if **orphan** report or user requests | Deeper **topic** layering |
| **E — Numeric fill (ongoing)** | Revenue, capital phasing, revenue milestones, vision stop rules—**family data only** | **Decision-safe** economics |

---

## 6. Pages that should remain placeholders until evidence exists

Keep **`status: draft`** or explicit **TBD** tables for:

| Page | Why |
|------|-----|
| [`east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md) | **`HH_NEED`**, channel prices |
| [`revenue-milestone-model-supplemental-to-salary-replacement.md`](revenue-milestone-model-supplemental-to-salary-replacement.md) | Milestone **$** and **years** |
| [`capital-phasing-table-years-0-10-two-site-smart-farm.md`](capital-phasing-table-years-0-10-two-site-smart-farm.md) | **Row $**, financing **terms** |
| [`east-tennessee-two-site-farm-business-plan-vision-and-constraints.md`](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) | **Numeric** stop rules |
| [`family-labor-model-and-coverage-matrix-two-site-smart-farm.md`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md) | **Named** roles, **real** **hours** |
| [`instrumentation-priority-matrix-two-site-smart-farm.md`](instrumentation-priority-matrix-two-site-smart-farm.md) | **Scores** after **pilot** |
| [`validation-backlog-before-major-spend-two-site-smart-farm.md`](validation-backlog-before-major-spend-two-site-smart-farm.md) | **Pass** checkboxes **until** evidence files |
| [`east-tennessee-two-site-farm-business-plan-hostile-internal-review.md`](east-tennessee-two-site-farm-business-plan-hostile-internal-review.md) | **Revise** after **first** **year** of **books** |

Do **not** mark **framework**, **enterprise options**, **recommended strategy**, **roadmap**, **runbooks**, or **comparisons** as “waiting for evidence” for **structure**—they are already **decision-grade** at **qualitative** level.

---

## Links

- [`Business plan wiki — Git-friendly execution sequence`](business-plan-wiki-git-execution-sequence.md) — PR batches, commit order, landing order, **minimum usable state**
- [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)
- [`Hostile internal review`](east-tennessee-two-site-farm-business-plan-hostile-internal-review.md)
- [`Information architecture — decision-safe operational brain`](information-architecture-decision-safe-operations.md)
