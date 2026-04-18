---
title: Trip batching and site visit policy — two-site smart farm
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
review_status: unreviewed
tags:
  - two-site
  - operations
  - logistics
confidence: medium
---

# Trip batching and site visit policy — two-site smart farm

## Purpose

Operational policy for **`SITE_HOME` ↔ `SITE_FARM`** travel when **`COMMUTE_ONE_WAY` ≈ 35 min**. **Batching**, **low daily touch**, and **remote observability** are **mandatory design filters**—not nice-to-haves. **Routine unnecessary trips** are assumed to **destroy margin and morale**.

**Canonical distance math**: [`Two-site operating model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md) (**distance-tax rules**).

**Structural misfits**: [`Two-site structure disqualifiers`](two-site-structure-disqualifiers-east-tennessee.md).

---

## What justifies a trip

A visit is **justified** only if **at least one** applies **before** departure:

| Class | Justification | Examples (non-exhaustive) |
|-------|----------------|---------------------------|
| **J1 — Scheduled work order** | **Written** list of tasks with **minimum** **`H_VISIT`** | Fence repair block; working pens; loading; hay **window** work |
| **J2 — Tier-1 alert** | **Open** condition from [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md) **or** **documented** life-safety / major asset risk | Dry tank; pump fault; perimeter breach **where** **verified** |
| **J3 — Surge calendar** | **Pre-declared** surge (calving, shipping, storm recovery) | Overrides **normal** batch days |
| **J4 — Third-party** | Vet, buyer, inspector—**clock** **bounded** | Combine with **J1** when possible |

**Not** a justification: “**I’m worried**,” “**I haven’t been today**,” “**I’ll combine with errands**” **without** **J1–J4**.

**Junk trip** = none of **J1–J4** satisfied → **counts** toward **policy failure** (morale + review), not harmless.

---

## What must be batched

**Default**: Stack **all** **deferrable** physical work into **the fewest** **high-payload** blocks per week.

| Must batch | Rationale |
|------------|-----------|
| **Routine** animal moves / checks compatible with **non-daily** rhythm | **T1** target—[`two-site operating model`](two-site-operations-model-5ac-homebase-120ac-production.md) |
| **Maintenance** that is **not** time-critical | **DT-1** **minimum visit payload** |
| **Supply** delivery (feed, parts) | **Single** **truck** run with list |
| **Social / neighbor** stops | **Not** **farm** trips—**separate** mental account |

**Surge exception**: When **J3** is active, **batching** may **mean** “**stay**” or “**return** next day”—not **tiny** daily drops.

---

## What should be remotely observable (first-class)

**Priority order** aligns with [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md):

| Priority | Observable | Why |
|----------|------------|-----|
| **P1** | **Water** level / flow / pump **run/fault** | **Highest** trip-kill per dollar |
| **P2** | **Power** at critical loads (pump, gate opener) | **Silent** failures **hurt** |
| **P3** | **Gate** position / latch state **where** **legally** **and** **reliably** done | **Reduces** “did I leave it” trips |
| **P4** | **Weather / soil moisture** **at decision points** | **Schedules** **when** to **batch** field work—not **daily** scouting substitute |

**Rule**: If an observation **does not** **change** a **decision** **or** **eliminate** a **trip**, it is **not** **P1**—it is **nice-to-have** ([`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md)).

**Triage cap**: **`H_TRIAGE`** hours/week on alerts—hard ceiling per [`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md). **Overflow** = **de-scope** sensors, not **more** driving.

---

## Work patterns that indicate failure

| Signal | Interpretation |
|--------|----------------|
| **`trips_wk`** **rises** **without** **herd/crop** **scale** **change** | **Batching** or **telemetry** **failed**—**stop** adding **work** |
| **Rising** **junk trips** (self-reported or calendar audit) | **Morale** + **margin** leak—**enforce** **work orders** |
| **Alerts** **ignored** **after** **fatigue** | **Instrumentation** **design** **wrong**—**fewer** **channels**, **better** **rules** |
| **“Quick** **stop**” **visits** **multiplying** | **Distance tax** **denial**—re-read **DT-4** / **disqualifiers** |
| **Primary** operator **cannot** **hold** **off-farm** job **and** **pattern** | **Enterprise** **or** **labor model** **wrong**—not **willpower** |
| **Second** **person** **always** **dragged** **for** **safety** **on** **routine** tasks | **Under-invested** **facilities** **or** **wrong** **enterprise** **intensity** |

**Escalation**: Repeated failure signals → **formal** **review** against [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md) and [`Vision` stop rules](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md)—**freeze** **non-essential** **CAPEX**.

---

## Related

- [`Family labor model and coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md)
- [`Runbook — sensor false-positive alert triage`](runbook-sensor-false-positive-alert-triage.md)
- [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md)
