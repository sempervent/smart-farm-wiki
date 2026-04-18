---
title: Weekly coverage matrix — two-site farm operations
page_type: analysis
status: draft
created: 2026-04-21
updated: 2026-04-21
tags:
  - two-site
  - operations
  - labor
  - template
review_status: unreviewed
confidence: low
---

# Weekly coverage matrix — two-site farm operations

## Purpose

A **fillable weekly grid** to make **who is responsible for eyes-on** at **`SITE_FARM`** and **`SITE_HOMESTEAD`** explicit when travel time is **`COMMUTE_ONE_WAY`**. Use it to expose **gaps** (no one within **`MAX_RESPONSE_TIME`**) **before** they become emergencies. Not a substitute for contracts or employment law—**placeholders** only.

## Scope

- **In scope**: Roles, shifts, **minimum checks**, handoff notes.
- **Out of scope**: Payroll, insurance classification, **24/7 professional** coverage (unless you add rows).

## Assumptions

| Placeholder | You define |
|-------------|------------|
| `SITE_HOMESTEAD` | Smaller / family base |
| `SITE_FARM` | Production parcel needing **regular** presence |
| `COMMUTE_ONE_WAY` | Typical drive (e.g. **35 min**) |
| `MAX_RESPONSE_TIME` | Worst acceptable delay for **Tier 1** issue (water off, escaped animal)—**your** risk tolerance |
| `ROLE_OWNER` | Primary decision-maker |
| `ROLE_PARTNER` | Optional |
| `ROLE_COVERAGE` | Neighbor, employee, **hired hand**, **nobody** |

## Minimum checks (edit to your enterprises)

Define **what “covered” means** in minutes and tasks:

| Check type | `SITE_FARM` | `SITE_HOMESTEAD` |
|------------|-------------|------------------|
| **Tier A** (daily non-negotiable) | e.g. water, feed, **eyes on livestock** | e.g. **pets**, **freezer**, **basement leak** |
| **Tier B** (2–3×/week) | fence walk, gate test | garden irrigation |
| **Tier C** (weekly) | equipment fluid levels | fuel for generator |

## Matrix template (copy and fill)

**Week of:** `YYYY-MM-DD`

| Day | Primary on call | Location morning (`H`/`F`/away) | Location afternoon | Tier A done @ `SITE_FARM` Y/N | Tier A done @ `SITE_HOMESTEAD` Y/N | Notes / handoff |
|-----|-----------------|-----------------------------------|--------------------|-------------------------------|------------------------------------|-----------------|
| Mon | | | | | | |
| Tue | | | | | | |
| Wed | | | | | | |
| Thu | | | | | | |
| Fri | | | | | | |
| Sat | | | | | | |
| Sun | | | | | | |

**Legend**: `H` = `SITE_HOMESTEAD`, `F` = `SITE_FARM`, **away** = neither (vacation, travel).

## Key questions

1. **Is there any day** where **no qualified person** can reach `SITE_FARM` within `MAX_RESPONSE_TIME`? If yes, what **changes**—neighbor agreement, fewer animals, remote water shutoff **with** verified install?
2. **Sick days**: Same matrix with **`ROLE_OWNER` = unavailable**—what breaks?
3. **Telemetry**: Which Tier A checks can **shorten** a visit vs which are **welfare**-mandated **in person**?

## Decision criteria

| If you discover… | Then… |
|------------------|-------|
| **Two consecutive days** with no `F` visit and Tier A requires daily | **Stop** expanding herd/crop until coverage fixed |
| **Same person** seven days **every** week | Schedule **burnout** risk; add row **paid** or **shared** |
| **Automation** “covers” Tier A | Must cite [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md) |

## Links to related future or existing pages

- [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md) — **why** batching and equipment home base matter.
- [`Agritourism business plan — guest hub on 120 acres, family home 35 min away`](agritourism-dual-site-business-plan-five-and-120-acres.md) — **contrast**: guest/caretaker model vs this matrix.
- *Incident response — livestock emergency (owner remote)* — **not yet filed**; see **[P1 #8](implementation-backlog-strategic-audit.md)** in the implementation backlog.
- [`Spatial data and farm asset registry standard`](spatial-data-and-farm-asset-registry-standard.md) — **where** checks apply (paddock, tank).
- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md) — what **remote** visibility can do.

## Open items

- [ ] Agree **Tier A** list with everyone named in the matrix.
- [ ] Post **printed** copy in both kitchens or **shared calendar** with reminders—wiki is not the runtime unless you use it daily.

---

*First draft: treat as a **living schedule**, not a one-time essay.*
