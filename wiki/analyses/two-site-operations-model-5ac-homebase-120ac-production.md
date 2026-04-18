---
title: Two-site operating model — 5-acre home base and 120-acre farm
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-21
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

Define how a **single farm business** runs when **family and command infrastructure** sit on a **~5-acre home base** (`SITE_HOME`) and **primary production and revenue** sit on a **~120-acre parcel** (`SITE_FARM`), separated by **`COMMUTE_ONE_WAY`** (planning default **~35 minutes** one way—**measure and log**; **do not** plan on “it feels shorter”).

This page is **operational**, not legal or tax advice. It stays **valid** while **enterprise mix** on the 120 acres is still open: it describes **where work and capital land**, not **which commodity** wins.

**Binding stance**: **`COMMUTE_ONE_WAY ≈ 35 min` is a structural tax**, not a rounding error. **Routine unnecessary trips** are treated as **margin and morale destroyers**. **Batching**, **low daily physical touch**, and **remote observability** are **first-class design filters**—not optional optimizations.

## Relationship to generic dual-site pattern

For a **production-led** two-site layout **without** the East Tennessee plan’s named sites, see:

- [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md)

**Package overlays** (stricter policy + disqualifiers):

- [`Trip batching and site visit policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md)
- [`Two-site structure disqualifiers`](two-site-structure-disqualifiers-east-tennessee.md)
- [`Enterprise unit economics — worksheet methodology`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md) — **`R_SPLIT`**, **MVCM** gates

## Decisions supported by this page

| Decision | This page provides |
|----------|-------------------|
| Where to place **CAPEX** (homestead vs production parcel) | Split tables; **irreversible** vs **relocatable** |
| What counts as a **worth-it trip** to the 120 | Links to **trip policy**; **distance-tax** tiers |
| What is **centralized** at home vs **distributed** in-field | Comms, broker, records authority, spares |
| **Emergency response** when distance and darkness matter | Tier link to coverage matrix + runbooks |
| Whether an enterprise **survives** the split | **Distance-tax rules** + [`disqualifiers`](two-site-structure-disqualifiers-east-tennessee.md) |

## Operating picture

### Site roles (non-negotiable facts from the business plan)

| Site | Size (planning) | Role |
|------|-----------------|------|
| `SITE_HOME` | ~5 ac | **Residence**; long-run **smart operations center** (network, broker, backups, workshop/lab, development). **Not** the primary commercial production land. |
| `SITE_FARM` | ~120 ac | **Primary production decision surface**: livestock, forage, crops, infrastructure tied to revenue. **All major enterprise bets** resolve here first. |

### Functions by location

| Function | Preferred location | Notes |
|----------|---------------------|-------|
| Broker, dashboards, config store, backup target | `SITE_HOME` | Stable power; daily physical access for ops |
| Field gateways, tank/pump sensing, gate position | `SITE_FARM` | Edge; must **fail safe** when backhaul is down |
| Livestock handling, stored feed, equipment | `SITE_FARM` | Mass and mess stay off the 5 ac |
| CAD, 3D printing for jigs/repair parts | `SITE_HOME` | Design at home; install at `SITE_FARM` |
| Authoritative business records | Choose one: `SITE_HOME` + cloud, or cloud with **offline export** | Write the choice in [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) or farmOS policy |

---

## Distance-tax rules (explicit)

**Definition — distance tax**: The **recurring operational penalty** of **not** being co-located with production: **round-trip drive time**, **vehicle OPEX**, **loaded labor** while driving, **context switching**, **inability to do “five-minute checks”**, and **morale cost** when trips are **frequent but low value**.

**Symbols (placeholders—fill with evidence; do not invent local dollars here)**

| Symbol | Meaning |
|--------|---------|
| `COMMUTE_ONE_WAY` | Minutes one way; **planning default ~35** until superseded by **P90** from a **season** of logged drives |
| `T_RT` | Round-trip **drive** time = `2 × COMMUTE_ONE_WAY` (minutes) |
| `τ_ctx` | Non-driving friction per visit (gear, fuel, boots, mental handoff)—**minutes**, measured |
| `H_VISIT` | **Productive on-site hours** planned for a visit (work-order scope) |
| `mi_rt` | Round-trip **miles** (odometer or maps **worst-case**) |
| `$/mi` | Vehicle marginal cost **per mile** (your books) |
| `σ` | **Loaded** hourly cost of operator time **including** drive (replacement wage or opportunity rate—**policy**) |
| `trips_wk` | Expected **count** of `SITE_HOME → SITE_FARM → SITE_HOME` cycles in a **normal** week for an enterprise |

**Core formulas (cash + time sanity)**

| ID | Formula / rule |
|----|----------------|
| **DT-0** | **Forbidden optimism**: Do **not** plan using **`COMMUTE_ONE_WAY` below your logged P90** without a full season of drive logs and a **documented** reason (road change, move—rare). |
| **DT-1** | **Minimum visit payload**: Let `H_block = (T_RT + τ_ctx)/60 + H_VISIT`. A “trip” must carry **`H_VISIT ≥ H_VISIT_MIN`** **unless** **Tier-1** emergency (see [`trip policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md)). **`H_VISIT_MIN`** is a **family policy** placeholder—set it high enough that **junk trips** hurt. |
| **DT-2** | **Incremental split OPEX** (for worksheet linkage): per [`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md), **`Δ_OPEX_SPLIT_X`** captures **trips**, **miles**, **time**, **cold chain**, **duplicate gear**—**not** double-counted with haul rows (**SPLIT-2**). |
| **DT-3** | **Split burden ratio**: **`R_SPLIT_X = Δ_OPEX_SPLIT_X / max(contribution margin_X, ε)`** — enterprise **X** fails **SPLIT-1** if **`R_SPLIT_X > R_SPLIT_MAX`** (placeholder ceiling). |
| **DT-4** | **Trip frequency cap (normal ops)**: If a business model **requires** **`trips_wk > TRIPS_WK_MAX`** **and** **no** **resident** operator at `SITE_FARM` **and** **no** **hired** daily presence, classify as **[`disqualified`](two-site-structure-disqualifiers-east-tennessee.md)** or **redesign** (telemetry, batching, enterprise change). **`TRIPS_WK_MAX`** is **not** generous—treat frequent driving as **structural failure**. |

**Morale and attention tax (non-cash, real)**

| ID | Rule |
|----|------|
| **DT-5** | **Junk trips** (drive out for “peace of mind” with **no** prior work order and **no** open **Tier-1** condition) **count** toward burnout and **invalidate** “low labor” claims in family review. |
| **DT-6** | **Batching is not optional** where physical work can be stacked: **spread** visits across the week **without** telemetry-backed reason → **policy failure**, not “being diligent.” |

**Distance-tax tiers (for ranking enterprises)**

| Tier | Touch expectation | Structural fit with ~35 min split |
|------|-------------------|-----------------------------------|
| **T0 — Episodic** | Long intervals; surge weeks predictable | **Fits** if batched + telemetry |
| **T1 — Weekly batch** | 1–3 **non-emergency** visit blocks / week | **Default** target band for family ops |
| **T2 — Multi-touch** | **>3** planned weekly visits **or** unpredictable **extras** | **High tax**—must show **`R_SPLIT`** acceptable |
| **T3 — Daily physical** | Needs **eyes/hands most days** | **Poor fit** **without** resident labor or **crew**—not baseline |

### Distance and batching (metrics table)

| Metric | Placeholder | How to update |
|--------|-------------|----------------|
| One-way commute | `COMMUTE_ONE_WAY` = ___ min | **Log** AM/PM; use **P90** for planning |
| Typical productive visit | ___ h on site | Time study |
| **Tier-1** alert conditions | Listed in [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md) + trip policy | Keep **short**—alert fatigue = failure |

**Batch rules (strict)**

- **Rule A**: No `SITE_FARM` visit for **trivial** on-site work under **`H_VISIT_MIN`** unless **Tier-1** open **or** **scheduled** surge block.
- **Rule B**: Fixed **days of week** for heavy `SITE_FARM` work; **surge weeks** override the template **explicitly** on the calendar.
- **Rule C**: **Telemetry** that **only** duplicates what a **two-minute walk** would fix **without** reducing **trips** is **not** “automation success”—it’s **dashboard theater** (see [`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md)).

### Infrastructure split (living document)

| Asset | `SITE_HOME` | `SITE_FARM` | Notes |
|-------|-------------|-------------|-------|
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

- Replace placeholders with **logged** commute and visit durations (**P90**, not best day).
- Revisit **distance-tax tiers** after **every** enterprise change—**R_SPLIT** must be recomputed.
- If **junk trips** persist, treat as **operating model failure**, not a **willpower** problem: redesign **telemetry**, **batch policy**, or **enterprise mix** ([`disqualifiers`](two-site-structure-disqualifiers-east-tennessee.md)).

## Related pages

- [`East Tennessee two-site farm business plan — two-site operating model`](east-tennessee-two-site-farm-business-plan-two-site-operating-context.md) — **package narrative**
- [`Trip batching and site visit policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md)
- [`Two-site structure disqualifiers`](two-site-structure-disqualifiers-east-tennessee.md)
- [`Enterprise options analysis`](east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md)
- [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md)
- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md)
- [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md)
- [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)
