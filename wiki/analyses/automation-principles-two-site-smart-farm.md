---
title: Automation principles — two-site smart farm
page_type: analysis
status: draft
created: 2026-04-18
updated: 2026-04-18
review_status: unreviewed
tags:
  - automation
  - two-site
  - operations
  - smart-farm
confidence: low
---

# Automation principles — two-site smart farm

## Purpose

State **what to automate early, late, or never** for a **5 ac control hub + 120 ac production** operation—**architecture and decisions**, not a shopping list. Complements [`East Tennessee two-site farm business plan — smart-tech strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) and [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md).

**Constraints**: **Travel time** between sites; **sensor** and **comms** **unreliability**; **maintenance** **capacity** of a **small** team; **aggressive automation** as **both** **leverage** and **recurring cost** (money + attention).

---

## Principles (ranked)

1. **Manual competence before remote actuation** — If you cannot run the system **by hand**, automation **hides** **risk**.
2. **Observe before optimize** — **Measurement** and **logging** **before** **closed-loop** control on **welfare**-critical paths.
3. **Fewer moving parts** — **One** **well-maintained** **water** stack beats **five** flaky gadgets.
4. **Fail known** — Prefer **documented** **safe defaults** over **clever** **recovery** nobody can **repeat** at **02:00**.
5. **Automation budget is not only CAPEX** — **Subscriptions**, **patching**, **triage** hours, **spares**—[`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md).

---

## Automate **early** (typical)

| Class | Rationale | Caveat |
|-------|-----------|--------|
| **Visibility** (tank, pump run, power at critical loads) | **Trip ROI** across `COMMUTE_ONE_WAY` | **False positives** → **triage** tax |
| **Structured logging** to **durable** store | Supports **SoR** for **instrument** history | **Not** a substitute for **books** |
| **Alerting** with **dedupe** | **Attention** routing | **Alert fatigue** = **disabled** alerts = **worse** than none |

---

## Automate **late** (after gates)

| Class | Gate examples |
|-------|-----------------|
| **Cameras everywhere** | **Policy**, **privacy**, **storage**, **bandwidth** |
| **Remote actuation** (gates, valves, feeders) | **Manual** **SOP**; **redundant** **sensing** where **welfare**-linked |
| **Full irrigation automation** | **Crop** commitment; **walk** **lines** first |
| **Fleet** of **LPWAN** nodes | **Pilot** **ROI**; **spares** **process** |

---

## Automate **never** (or never without human in loop)

| Item | Why |
|------|-----|
| **Animal welfare** decisions on **one** sensor | **Use** **redundancy** or **schedule** |
| **Loading / handling** for **market** | **Safety** + **quality** |
| **Response** to **stock** on **public** road | **Liability** |
| **“Set and forget”** **without** **patch** **cadence** | **Security** **debt** |

---

## Distance-specific rule

If **`MANUAL_INTERVENTION_TIME`** **>** **acceptable** **risk** **window** for a **system**, **downscope** **remote** **dependence** until **coverage** improves—[`Weekly coverage matrix`](weekly-coverage-matrix-two-site-farm-operations.md), [`Family labor coverage`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md).

---

## Links

- [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md)
- [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md)
- [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md)
- [`LoRaWAN vs Meshtastic`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md)
