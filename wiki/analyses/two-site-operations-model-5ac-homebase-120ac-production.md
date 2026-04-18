---
title: Two-site operating model — 5-acre home base and 120-acre farm
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - two-site
  - operations
confidence: medium
aliases:
  - Two-site ops 5 ac 120 ac
  - Two-site operations model — home base on 5 acres, production on 120 acres
---

# Two-site operating model — 5-acre home base and 120-acre farm

## Purpose

Define how a **single farm business** runs when **family and command infrastructure** sit on a **~5-acre home base** (`SITE_HOME`) and **primary production and revenue** sit on a **~120-acre parcel** (`SITE_FARM`), separated by a **commute** (`COMMUTE_ONE_WAY`, planning default **~35 minutes** one way—**log and replace** with measured times).

This page is **operational**, not legal or tax advice. It stays **valid** while **enterprise mix** on the 120 acres is still open: it describes **where work and capital land**, not **which commodity** wins.

## Relationship to generic dual-site pattern

For a **production-led** two-site layout **without** the East Tennessee plan’s named sites, see the **generic** template (same commute/batching concerns, different placeholders):

- [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md)

## Decisions supported by this page

| Decision | This page provides |
|----------|-------------------|
| Where to place **CAPEX** (homestead vs production parcel) | Split tables; **irreversible** vs **relocatable** |
| What counts as a **worth-it trip** to the 120 | Batch rules, minimum on-site duration |
| What is **centralized** at home vs **distributed** in-field | Comms, broker, records authority, spares |
| **Emergency response** when distance and darkness matter | Tier link to coverage matrix + runbooks |

## Operating picture

### Site roles (non-negotiable facts from the business plan)

| Site | Size (planning) | Role |
|------|-----------------|------|
| `SITE_HOME` | ~5 ac | **Residence**; long-run **smart operations center** (network, broker, backups, workshop/lab, development). **Not** the primary commercial production land. |
| `SITE_FARM` | ~120 ac | **Primary production decision surface**: livestock, forage, crops, infrastructure tied to revenue. **All major enterprise bets** resolve here first. |

### Functions by location

| Function | Preferred location | Notes |
|----------|---------------------|--------|
| Broker, dashboards, config store, backup target | `SITE_HOME` | Stable power; daily physical access for ops |
| Field gateways, tank/pump sensing, gate position | `SITE_FARM` | Edge; must **fail safe** when backhaul is down |
| Livestock handling, stored feed, equipment | `SITE_FARM` | Mass and mess stay off the 5 ac |
| CAD, 3D printing for jigs/repair parts | `SITE_HOME` | Design at home; install at `SITE_FARM` |
| Authoritative business records | Choose one: `SITE_HOME` + cloud, or cloud with **offline export** | Write the choice in [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) or farmOS policy |

### Distance and batching

| Metric | Placeholder | How to update |
|--------|-------------|----------------|
| One-way commute | `COMMUTE_ONE_WAY` = ___ min | Log over seasons; use worst-case for surge planning |
| Typical productive visit | ___ h on site | Time study |
| Minimum trip worth driving | `MIN_VISIT_MINUTES` / abort rule | Policy: avoid **junk trips** that only “check the vibe” |

**Batch rules (edit as policy matures)**

- **Rule A**: No trip for trivial on-site work under `MIN_VISIT_MINUTES` unless a **Tier 1** condition is open (define Tier 1 on [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md) and [`Family labor and coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md)).
- **Rule B**: Fixed **days of week** for heavy `SITE_FARM` work; **surge weeks** override the template.

### Infrastructure split (living document)

| Asset | `SITE_HOME` | `SITE_FARM` | Notes |
|-------|-------------|-------------|--------|
| Internet / VPN termination | Primary | LTE fallback? Y/N | |
| MQTT broker / observability core | Primary | Edge buffer only if designed | [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md) |
| Backup power | UPS / small generator plan | Pump/generator at critical loads | |
| Trailer / load-out | Secondary | Primary | |

## Known facts

| ID | Statement |
|----|-----------|
| K1 | The **5-acre parcel is not** the primary production site in this plan. |
| K2 | The **120-acre parcel is** the main **production and revenue** locus. |
| K3 | Business intent is **profit-first**, then **low labor**, then **resilience** ([`Planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)). |

## Assumptions

| ID | Statement |
|----|-----------|
| A1 | `COMMUTE_ONE_WAY` is representative for **batch planning** until a drive log proves otherwise. |
| A2 | At least one adult can reach `SITE_FARM` within **acceptable** emergency delay for the chosen enterprises (define “acceptable” in the coverage matrix). |

## Open questions

| ID | Question |
|----|----------|
| Q1 | Is **overnight stay** at or near `SITE_FARM` allowed for calving, hay windows, or security? |
| Q2 | **Seasonal** road constraints (snow, mud, gate icing) on the route? |
| Q3 | Exact **boundary** and **easement** facts—deed vs mental map? |

## Iterative updates (over time)

- Replace placeholders with **logged** commute and visit durations.
- Add a **one-page map** of asset IDs when the spatial registry is live.
- Revisit **Rule A/B** after the first **telemetry pilot** (measured trip reduction vs alert hours).

## Related pages

- [`East Tennessee two-site farm business plan — two-site operating context`](east-tennessee-two-site-farm-business-plan-two-site-operating-context.md) — ET-specific narrative
- [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md) — generic logistics
- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md)
- [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md)
- [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)
