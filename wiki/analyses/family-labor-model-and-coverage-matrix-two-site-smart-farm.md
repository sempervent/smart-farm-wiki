---
title: Family labor model and coverage matrix — two-site smart farm
page_type: analysis
status: draft
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - labor
  - two-site
  - family
  - template
confidence: medium
---

# Family labor model and coverage matrix — two-site smart farm

## Purpose

Make **who can respond** at **`SITE_FARM`** and **`SITE_HOME`** **explicit** for a **three-generation** family labor pool (**father / son / grandson** placeholders below). Pair with **travel time** (`COMMUTE_ONE_WAY`) so **coverage gaps** show up **before** calving season or equipment failure.

**Does not**: Replace employment law advice; **does** force **honest** “nobody available” rows.

## Key decisions supported

| Decision | Use |
|----------|-----|
| **Max herd / enterprise complexity** | If coverage **cannot** meet **Tier 1** response → **reduce** exposure |
| **Hired help / neighbor** | **Trigger** when matrix shows **systematic** gaps |
| **Automation priority** | Gaps that **telemetry** can **narrow** vs **cannot** (animal handling) |
| **Surge calendar** | Pre-block **off-farm** commitments |

## Roles (assign real names locally)

| ID | Role | Typical availability | Primary skills | Hard constraints |
|----|------|---------------------|----------------|------------------|
| R1 | **Primary ops** (e.g. father) | `HRS_WK` = ___ | Stockmanship, equipment | Off-farm: `Y/N` |
| R2 | **Secondary** (e.g. son) | ___ | Trailer, tech stack | |
| R3 | **Tertiary** (e.g. grandson) | ___ | Physical tasks, learning | School / age limits |

## Coverage matrix — weekly (template)

**Legend**: ✓ = primary responsible · ○ = backup · — = cannot cover · **T** = travel from other site acceptable within `MAX_RESPONSE_TIME` (define minutes: ___).

| Time block | `SITE_HOME` (min checks / homelab) | `SITE_FARM` (eyes-on / field) | Notes |
|------------|-------------------------------------|-------------------------------|-------|
| Mon AM | | | |
| Mon PM | | | |
| Tue AM | | | |
| … | | | |
| Sun | | | **Exception** rows for surge |

Copy rows or use [`Weekly coverage matrix — two-site farm operations`](weekly-coverage-matrix-two-site-farm-operations.md) for a **finer** grid.

## Tiered response (define)

| Tier | Example | Target response | Who |
|------|---------|-----------------|-----|
| **T1** | No water / escape / pump dead | ≤ **`T1_MAX_MIN`** | |
| **T2** | Fence down non-critical | ≤ **`T2_MAX_HOURS`** | |
| **T3** | Telemetry flaky | Next batch visit | |

## Surge windows (placeholders)

| Window | Enterprise driver | Coverage rule |
|--------|-------------------|---------------|
| **Calving** (if applicable) | | |
| **Hay weather** | | |
| **Shipping / haul** | | |

## Known / assumed / open

| Class | Content |
|-------|---------|
| **Known** | Family labor **as default** staffing model in business plan |
| **Assumed** | At least **two** adults **often** available **most** weeks—**validate** |
| **Open** | **CDL** / **trailer** coverage across **how many** people? **Neighbor** **agreement**? |

## Links

- [`East Tennessee two-site farm business plan — labor model and weekly rhythm`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md)
- [`Two-site operations model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md)
- [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md)
- [`Manual fallback and degraded modes`](manual-fallback-degraded-modes-critical-operations.md)
