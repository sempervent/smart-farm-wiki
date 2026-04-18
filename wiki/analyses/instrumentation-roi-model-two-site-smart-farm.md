---
title: Instrumentation ROI model — where automation earns its keep first
page_type: analysis
status: draft
created: 2026-04-18
updated: 2026-04-18
review_status: unreviewed
tags:
  - telemetry
  - roi
  - two-site
  - automation
confidence: low
---

# Instrumentation ROI model — where automation earns its keep first

## Purpose

Translate **ranking** ([`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md)) into a **financial and labor framing**: what must be **measured** before scaling instrumentation, how **cost** and **benefit** sit in the books, and how **aggressive automation** shows up as **leverage** *and* **drag** (capex, subscriptions, triage time, security upkeep).

**Non-goals**: Vendor ROI calculators; claiming payback periods without filled inputs.

---

## Relationship to the priority matrix

| Tool | Role |
|------|------|
| **Priority matrix** | **Qualitative** score + **phase** fit + **manual-first** gates |
| **This ROI model** | **Quantitative shell**: trips, hours, $/yr placeholders—**pilot vs fleet** |

Use **both**: a row can **score high** on priority but **fail** ROI until **evidence** is logged.

---

## Required inputs

| Input | Description |
|-------|-------------|
| **Instrument ID** | Matches matrix row (`I1`, `I2`, …) |
| **Baseline** | **Manual** operating procedure and **measured** trips/hours (pre-pilot) |
| **Pilot scope** | Count of assets covered; **duration** (weeks) |
| **Capex** | Hardware + install + **your** labor hours valued at shadow rate |
| **Annual OPEX** | Subscriptions, SIMs, **spares**, **power** increment |
| **Triage burden** | **Hours/month** on alerts, false positives, dashboard checks |
| **Risk value (optional)** | **Avoided** loss events—**range**, not single hero number |
| **Split-site context** | **Extra** value if instrument reduces **`COMMUTE_ONE_WAY`** trips |

---

## Outputs supported

| Output | Decision |
|--------|----------|
| **$/yr avoided trip cost** | `trips_saved × (mile + time cost)` — compare to OPEX |
| **Net hours to farm** | `(field_hours_saved + travel_saved) − triage_hours` |
| **Payback range** | `capex / (annual net benefit)` — **only** when inputs filled |
| **Fleet scale ceiling** | When **subscription + triage** dominates—**stop** rollouts |
| **Book placement** | Which **accounts** in [`Farm accounting baseline`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md) receive spend |

---

## Assumptions

| Assumption | Rationale |
|------------|-----------|
| **Pilot before fleet** | **One** water level + **one** pump signal beats **ten** half-debugged channels. |
| **Triage is real labor** | Automation that **creates** **alerts** without **resolution** **SOP** **increases** **labor**. |
| **Remote site = asymmetric benefit** | Trip reduction ROI is **higher** when **distance** and **batching** are binding. |
| **Security and patching** | Homelab / self-hosted stacks carry **recurring** **owner** hours—**charge** to **automation** or **ops** line. |
| **No double-count** | If milestone model **already** credits **family hours saved**, do not **also** book as **cash** **unless** hired replacement. |

---

## Placeholders (do not fabricate)

| Symbol | Meaning |
|--------|---------|
| `T0` | Baseline period length |
| `N_TRIP0` | Baseline **unnecessary** trips to `SITE_FARM` per month |
| `N_TRIP1` | Post-instrument trips (pilot) |
| `C_MI` | **Fully loaded** cost per mile (vehicle + time optional) |
| `H_TRIP` | Hours per round trip |
| `R_SHADOW` | Shadow **$/hr** for family time |
| `CAPEX_I` | Total capital for pilot install |
| `OPEX_I_YR` | Annual recurring for this instrument cluster |
| `H_TRIAGE_MO` | Monthly triage hours |

---

## ROI worksheet — per instrument (template)

| Field | Instrument I___ | Notes |
|-------|-----------------|-------|
| Baseline trips / mo | | manual log |
| Pilot trips / mo | | after **same season** conditions |
| Trips saved / mo | `= max(0, baseline − pilot)` | |
| $/trip saved | `miles × C_MI + H_TRIP × R_SHADOW` (optional components) | |
| Annual trip $ benefit | `trips saved × 12 × $/trip` | **placeholder** |
| Annual OPEX | | subs + LTE slice + spares |
| Annual triage cost | `H_TRIAGE_MO × 12 × R_SHADOW` | |
| **Net annual benefit (cash + shadow)** | trip $ − OPEX − triage | |
| Simple payback (years) | `CAPEX_I / net annual` | **if** net > 0 |

---

## Leverage vs cost — explicit balance sheet

| Automation effect | **Cost side** | **Leverage side** |
|--------------------|---------------|-------------------|
| Remote visibility | CAPEX, OPEX, triage | Fewer trips; faster fault detection |
| Alerts | Triage labor; alert fatigue | Risk reduction if SOP exists |
| Actuators / control | Liability, maintenance; complexity | Labor reduction **only** with **training** |
| Data platform (farmOS, etc.) | Hosting, integration, backup | Single **source of truth** for **units** and **inventory** |

---

## Pilot vs fleet economics

| Stage | What to document | Gate to advance |
|-------|------------------|-----------------|
| **Pilot** | **Before/after** trip log; **incident** count (dry tank, pump fault) | **Net hours** ≥ 0 **or** **documented** **kill** |
| **Fleet** | **Marginal** OPEX per added node; **support** **ticket** rate | **OPEX + triage** **curve** **sublinear** vs nodes |

---

## Enterprise mix uncertainty

When **primary enterprise** is **not** fixed, **instrument** **I** may **only** apply to **subset** of revenue (e.g. stock water **only** if **grazing** path active). Add column **“Applies if scenario S___”** to the ROI table.

---

## Links

- [`East Tennessee two-site farm business plan — smart technology and telemetry strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)
- [`Manual fallback — degraded modes`](manual-fallback-degraded-modes-critical-operations.md)
- [`Validation backlog — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md)
- [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md)
