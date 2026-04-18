---
title: Instrumentation ROI model — where automation earns its keep first
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-21
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

Translate **ranking** ([`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md)) into **decision-grade** framing: **what** must be **measured** before scaling, how **cost** and **benefit** sit in the books, and how **instrumentation** interacts with **labor** (**triage**, **false positives**, **upkeep**) and **security**. **Instrumentation does not automatically reduce labor**—it **may** reduce **trips** or **document** **risk**; **net** **hours** can be **negative** if **triage** **dominates**.

**Non-goals**: Vendor ROI calculators; claiming payback without filled inputs.

**Controls**: [`Smart technology and telemetry strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md), [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md).

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
| **Triage / false-positive / upkeep** | **Structured** fields below—**not** optional **footnotes** |
| **Risk value (optional)** | **Avoided** loss events—**range**, not single hero number |
| **Split-site context** | **Extra** value if instrument reduces **`COMMUTE_ONE_WAY`** trips ([`trip policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md)) |

---

## Triage time fields (labor — real)

| Symbol | Meaning | How to measure |
|--------|---------|----------------|
| `H_TRIAGE_WK` | **Hours/week** on **this** instrument cluster: **acknowledging** alerts, **dashboard** checks **caused** by **this** cluster, **correlation** with **other** signals | **Time log** **4+** **weeks** |
| `H_TRIAGE_MO` | `H_TRIAGE_WK × 52 / 12` (or direct monthly sum) | Worksheet |
| `N_ALERT_WK` | **Raw** **alerts**/week **from** **this** cluster (**before** **suppression**) | **Broker** / **tooling** **stats** |
| `N_TRUE_WK` | **Alerts** **week** **that** **required** **action** **or** **were** **true** **positives** | **Post-hoc** **label** **during** **pilot** |
| `FP_RATE` | **False-positive** **rate** **placeholder** = `(N_ALERT_WK − N_TRUE_WK) / max(N_ALERT_WK, ε)` | **Dimensionless**; **trend** **matters** |

**Ceiling**: Family **`H_TRIAGE_MAX`** **total** **across** **all** **instruments** per [`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md)—**overflow** → **de-scope** **before** **fleet**.

---

## False-positive cost fields

| Symbol | Meaning |
|--------|---------|
| `C_FP` | **Cost** **per** **unnecessary** **triage** **event** (shadow **$/hr ×** **minutes** **+** **morale** **tax** **optional** **scalar**) — **placeholder** |
| `N_FP_MO` | **Count**/month **of** **triage** **events** **classified** **as** **false** **positive** **after** **review** |
| `FP_COST_YR` | `N_FP_MO × 12 × C_FP` **or** `H_FP_MO × 12 × R_SHADOW` **where** `H_FP` = **hours** **on** **false** **alarms** |

**Rule**: **`FP_COST_YR`** **enters** **net** **benefit** **as** **subtract**—same **status** **as** **OPEX**.

---

## Upkeep burden fields (non-triage)

| Symbol | Meaning |
|--------|---------|
| `H_PATCH_MO` | **Patch** / **upgrade** / **container** **pulls** / **dependency** **fires** **attributable** **to** **this** cluster |
| `H_FIELD_MO` | **Physical** **site** **visits** **for** **sensor** **maintenance** **only** (**not** **normal** **farm** **work**) |
| `H_ADMIN_MO` | **Vendor** **portals**, **SIM**, **billing**, **certificate** **renewal** |
| `SPARES_YR` | **Expected** **replacement** **parts** **cost** (**$**) **/yr** (**antennas**, **radios**, **sensors**) |
| `UPKEEP_YR` | `(H_PATCH_MO + H_FIELD_MO + H_ADMIN_MO) × 12 × R_SHADOW + SPARES_YR` | **Placeholder** **until** **filled** |

---

## Decommission criteria (kill / freeze)

An **instrument** **cluster** **must** **de-scope**, **freeze** **fleet** **expansion**, or **remove** **when** **any**:

| ID | Criterion (pass/fail) |
|----|------------------------|
| **DC-1** | **`FP_RATE` > `FP_RATE_MAX`** **for** **`T_FP_EVAL`** **consecutive** **weeks** **after** **tuning** **attempt** |
| **DC-2** | **`H_TRIAGE_WK` > H_TRIAGE_BUDGET_WK`** **for** **this** **cluster** **where** **`H_TRIAGE_BUDGET_WK`** **is** **allocated** **share** **of** **`H_TRIAGE_MAX`** |
| **DC-3** | **Net** **annual** **benefit** **≤** **0** **for** **two** **review** **periods** **after** **pilot** **—** **see** **worksheet** |
| **DC-4** | **Security** **incident** **or** **unpatchable** **CVE** **on** **cluster** **with** **no** **owner** **within** **`T_PATCH_MAX`** |
| **DC-5** | **Enterprise** **path** **changes** **such** **that** **instrument** **no** **longer** **applies** **(e.g.** **no** **grazing** **—** **stock** **water** **ROI** **N/A)** |

**Action**: Document **kill** **in** **`wiki/log.md`** **refactor** **or** **policy** **entry**; **update** **priority** **matrix** **row** **status** **deprecated**.

---

## Outputs supported

| Output | Decision |
|--------|----------|
| **$/yr avoided trip cost** | `trips_saved × (mile + time cost)` — compare to OPEX + **FP_COST_YR** + **UPKEEP_YR** |
| **Net hours to farm** | `(field_hours_saved + travel_saved) − H_TRIAGE − H_FP − H_PATCH − H_FIELD − H_ADMIN` — **can** **be** **negative** |
| **Payback range** | `capex / (annual net benefit)` — **only** when inputs filled |
| **Fleet scale ceiling** | When **subscription + triage + upkeep** dominates—[`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) |
| **Book placement** | [`Farm accounting baseline`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md) |

---

## Assumptions

| Assumption | Rationale |
|------------|-----------|
| **Pilot before fleet** | **One** water level + **one** pump signal beats **ten** half-debugged channels. |
| **Triage is real labor** | Alerts **without** **resolution** **SOP** **increase** **labor**. |
| **Remote site = asymmetric trip value** | Trip reduction **can** **justify** **instrument** **where** **distance** **binds**—**not** **automatic**. |
| **Security and patching** | Charge **hours** **to** **automation** **burden**. |
| **No double-count** | If milestone model **already** credits **family hours saved**, do not **also** book as **cash** **unless** hired replacement. |

---

## Placeholders (do not fabricate)

| Symbol | Meaning |
|--------|---------|
| `T0` | Baseline period length |
| `N_TRIP0` | Baseline **unnecessary** trips to `SITE_FARM` per month |
| `N_TRIP1` | Post-instrument trips (pilot) |
| `C_MI` | **Fully loaded** cost per mile |
| `H_TRIP` | Hours per round trip |
| `R_SHADOW` | Shadow **$/hr** for family time |
| `CAPEX_I` | Total capital for pilot install |
| `OPEX_I_YR` | Annual recurring for this instrument cluster |
| `FP_RATE_MAX`, `T_FP_EVAL`, `H_TRIAGE_BUDGET_WK`, `T_PATCH_MAX` | Policy **ceilings** — **fill** |

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
| `H_TRIAGE_MO`, `FP_RATE`, `FP_COST_YR` | | **triage** **+** **false** **positive** |
| `UPKEEP_YR` | | **patch** + **field** + **admin** + **spares** |
| **Net annual benefit (labor-inclusive)** | trip $ − OPEX − FP_COST_YR − upkeep $ equivalent − triage $ | **triage** **at** **R_SHADOW** |
| Simple payback (years) | `CAPEX_I / net annual` | **if** net > 0 |

---

## Leverage vs cost — explicit balance sheet

| Automation effect | **Cost side** | **Leverage side** |
|--------------------|---------------|-------------------|
| Remote visibility | CAPEX, OPEX, **triage**, **FP cost**, **upkeep** | **May** reduce trips; **may** speed fault detection—**prove** |
| Alerts | Triage labor; alert fatigue | Risk reduction **if** SOP exists |
| Actuators / control | Liability, maintenance; complexity | Labor change **only** with **training** + **proof** |
| Data platform (farmOS, etc.) | Hosting, integration, backup | Single **source of truth** for **units** and **inventory** |

---

## Pilot vs fleet economics

| Stage | What to document | Gate to advance |
|-------|------------------|-----------------|
| **Pilot** | **Before/after** trip log; **incident** count; **`FP_RATE`**, **`H_TRIAGE_WK`** | **Net hours** ≥ 0 **or** **documented** **kill** (**DC-*** ) |
| **Fleet** | **Marginal** OPEX + **marginal** **triage** per added node | **Sublinear** **curve** **or** **stop** ([`stop rules`](automation-stop-rules-two-site-smart-farm.md)) |

---

## Enterprise mix uncertainty

When **primary enterprise** is **not** fixed, **instrument** **I** may **only** apply to **subset** of revenue (e.g. stock water **only** if **grazing** path active). Add column **“Applies if scenario S___”** to the ROI table.

---

## Links

- [`East Tennessee two-site farm business plan — smart technology and telemetry strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)
- [`Automation stop rules — two-site smart farm`](automation-stop-rules-two-site-smart-farm.md)
- [`Manual fallback — degraded modes`](manual-fallback-degraded-modes-critical-operations.md)
- [`Validation backlog — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md)
- [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md)
