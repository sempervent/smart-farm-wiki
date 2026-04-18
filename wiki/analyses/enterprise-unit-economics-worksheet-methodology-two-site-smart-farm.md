---
title: Enterprise unit economics — worksheet methodology (two-site smart farm)
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-21
review_status: unreviewed
tags:
  - economics
  - two-site
  - worksheet
  - enterprise-mix
confidence: low
---

# Enterprise unit economics — worksheet methodology (two-site smart farm)

## Purpose

Provide a **repeatable worksheet pattern** and **pass/fail tests** for comparing **candidate enterprises** on the **same land and labor envelope**—without a single committed mix. Outputs feed [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md), [`Farm accounting baseline`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md), [`Revenue milestone model`](revenue-milestone-model-supplemental-to-salary-replacement.md), and [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md).

**Non-goals**: Picking “the” enterprise here; publishing dollar forecasts without evidence.

---

## Required inputs (gather before treating any row as “true”)

| Input | Description | Typical source |
|-------|-------------|----------------|
| **Enterprise list** | Named candidates with **primary product** and **exit channel** | [`Enterprise options analysis`](east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md) |
| **Unit definition** | What one “unit” is (head, lb sold, bed-night, acre rotation, etc.) | Owner definition; **stable** year to year |
| **Time horizon** | Planning years | Plan phases |
| **Split-site parameters** | `COMMUTE_ONE_WAY`, batching, `SITE_HOME` vs `SITE_FARM` tasks | [`Two-site operations model`](two-site-operations-model-5ac-homebase-120ac-production.md) |
| **Family labor envelope** | Hours/week by role; **surge** windows | [`Labor model`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md) |
| **Shadow labor rate band** | `SHADOW_LOW`–`SHADOW_HIGH` **$/hr** | Family policy—not tax reporting |
| **Automation posture** | Manual baseline vs instrumented | [`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md) |
| **Evidence hooks** | UT budgets, auction bills, processor quotes | [`Source-ingest campaign`](business-plan-source-ingest-campaign-east-tennessee-two-site.md) |

---

## Minimum viable contribution margin (MVCM) gate tests

**Contribution margin per enterprise** (cash basis for planning year):

`CM_X = P_X − V_X`

where `P_X` = revenue per unit, `V_X` = **variable** costs per unit (see accounting baseline—**no** full overhead allocation here).

### Pass/fail rules (placeholders—fill before scale)

| Test ID | Rule | Pass | Fail (do not scale enterprise X) |
|---------|------|------|----------------------------------|
| **MVCM-1** | **Positive unit margin** | `CM_X > 0` at **mid** price in `[P_LOW, P_HIGH]` | `CM_X ≤ 0` at **mid** price—**fix** channel or **cut** scope |
| **MVCM-2** | **Sensitivity** | `CM_X > 0` at **P_LOW** **or** **documented** hedge (contract) | **Negative** at **P_LOW** **and** **no** hedge—**high** optimism risk |
| **MVCM-3** | **Blended scenario** | For active scenario **S**, weighted `CM_S = Σ w_X CM_X` **> 0** | **Blended** **≤ 0**—**Fin-G(2→3)** **blocked** until **remediated** |

**Formula (blended)**:

`CM_S = Σ_X w_X × CM_X` with `Σ w_X = 1` (revenue weights or unit mix—**document** convention).

---

## Split-site logistics burden rules

**Incremental** split-site cost for enterprise **X** (not allocated overhead—**incremental** only):

`Δ_OPEX_SPLIT_X = (trips_X × 2 × COMMUTE_MI × $/mi) + time_trips_X × σ + cold_chain_X + duplicate_gear_X`

| Symbol | Meaning |
|--------|---------|
| `COMMUTE_MI` | One-way miles—**or** use **minutes** × **speed** assumption—**document** |
| `σ` | Shadow **$/hr** for drive time—use **band** |
| `trips_X` | Trips **attributable** to **X** per planning year |

**Burden ratio (gate)**:

`R_SPLIT_X = Δ_OPEX_SPLIT_X / max(CM_X × units_X, ε)`

| Rule | Pass | Fail |
|------|------|------|
| **SPLIT-1** | `R_SPLIT_X ≤ R_SPLIT_MAX` (placeholder) | **Logistics** **eats** margin—**consolidate** trips, **hire** custom, or **defer** enterprise |
| **SPLIT-2** | **Haul** + **processing** **in** `V_X` **or** **Δ_OPEX_SPLIT**—**not** **both** **double-counted** | Worksheet **error** |

**Consolidation**: If **same** trip serves **multiple** enterprises, **allocate** `trips_X` by **documented** rule (e.g. **by** **revenue**).

---

## Labor-cost treatment (family + hired + telemetry triage)

### Categories

| Category | Symbol | Notes |
|----------|--------|-------|
| Family field + handling | `H_FAM_X` | Hours/unit—**normal** week |
| Surge | `H_SURGE_X` | Worst window (calving, weather, market rush) |
| Hired | `H_HIRED_X` | **Cash** cost in `V_X` **or** overhead—**one** place |
| Telemetry / IT triage | `H_TRIAGE_X` | Alerts, false positives, patching, dashboard—**first-class** |

### Full labor charge (for **M3** milestone)

`L_CHRG_Y = (H_FAM_Y + H_SURGE_Y + H_TRIAGE_Y) × σ` with `σ ∈ [SHADOW_LOW, SHADOW_HIGH]`

**Not** tax W-2—**opportunity cost** for **go/no-go**.

### Low-labor optimization metric

`Λ_X = CM_X × units_X / (H_FAM_X + H_SURGE_X + H_TRIAGE_X)` = **contribution margin per **combined** hour**

Rank enterprises by `Λ_X` under **normal** and **surge**—**two** columns **minimum**.

### Telemetry triage rule

| Condition | Action |
|-----------|--------|
| `H_TRIAGE_X` **>** `H_TRIAGE_MAX` **per** week **sustained** | **De-scope** sensors—[`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md) |
| **False positive rate** **unbounded** | **Fail** **automation scale** gate—**not** a **finance** **pass** on **labor** |

---

## Outputs this worksheet supports

| Output | Consumer |
|--------|----------|
| **CM_X**, **MVCM** tests | **Fin-G(1→2)**, **Fin-G(2→3)** |
| **Cash timing** | Working capital; [`capital phasing`](capital-phasing-table-years-0-10-two-site-smart-farm.md) |
| **Labor hours per unit** | Surge feasibility; **M3** |
| **Split-site OPEX** | **R_SPLIT** gate; [`CAPEX/OPEX sequencing`](capex-opex-enterprise-sequencing-two-site-constraint.md) |
| **Scenario branches** | **S1/S2** parallel rows |

---

## Assumptions (explicit)

| Assumption | Why it matters |
|------------|----------------|
| **Contribution margin first** | Full overhead allocation to **one** enterprise often **lies**—use **ranges** |
| **Family labor has opportunity cost** | Shadow rate **band** for **comparability** |
| **Automation is two-sided** | CAPEX + subs + **triage** hours |
| **Two sites** duplicate or inflate cost | Same enterprise: different **CM** if logistics differ |
| **≥ two scenarios** until validation closes fork | |

---

## Placeholders until real numbers exist

| Placeholder | Meaning |
|-------------|---------|
| `U_X` | Physical **unit** for enterprise X |
| `P_X`, `P_LOW`, `P_HIGH` | Price **per unit** |
| `V_X` | Variable cash costs **per unit** |
| `H_FAM_X`, `H_SURGE_X`, `H_TRIAGE_X` | Hours |
| `D_MI` | Delivery miles / trips per unit |
| `CM_X` | `P_X − V_X` |
| `R_SPLIT_MAX`, `H_TRIAGE_MAX` | Policy **ceilings** |
| `ε` | Small positive to avoid divide-by-zero |

---

## Worksheet A — Unit definition and channel

| Enterprise ID | Name | Primary unit `U_` | Primary exit channel | Notes |
|-----------------|------|-------------------|----------------------|-------|
| E1 | | | | |
| E2 | | | | |

---

## Worksheet B — Variable costs per unit (cash)

| Line | E1 | E2 |
|------|----|-----|
| Purchased inputs | | |
| Veterinary / health | | |
| Marketing / commissions | | |
| Haul / transport | | |
| Processing fees | | |
| **Variable subtotal** `V_X` | | |

---

## Worksheet C — Split-site logistics load per unit

| Line | E1 | E2 |
|------|----|-----|
| Trips per unit | | |
| `Δ_OPEX_SPLIT` | | |
| `R_SPLIT` | | |

---

## Worksheet D — Labor per unit

| Line | E1 | E2 |
|------|----|-----|
| Family field | | |
| Admin / sales | | |
| Hired | | |
| Telemetry triage | | |

---

## Worksheet E — Scenario matrix

| Scenario | w_E1 | w_E2 | CM_S | Peak cash month | Binding labor |
|----------|------|------|------|-----------------|----------------|
| S1 | | | | | |
| S2 | | | | | |

---

## Git-oriented practice

Version assumptions in **changelog** subsection or commit messages; **date** external spreadsheets.

---

## Links

- [`East Tennessee two-site farm business plan — revenue model and milestones`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md)
- [`Business viability and farm economics — gap analysis`](business-viability-and-farm-economics-gap-analysis.md)
- [`Own equipment vs custom hire under two-site logistics`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md)
