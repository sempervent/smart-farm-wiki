---
title: Revenue milestone model — supplemental income to salary replacement
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-21
review_status: unreviewed
tags:
  - revenue
  - business-plan
  - template
  - milestones
confidence: medium
---

# Revenue milestone model — supplemental income to salary replacement

## Purpose

Translate the business plan’s **economic arc** into **fillable milestones** and **explicit formulas** for **pass/fail**: **supplemental** cash first, then **positive contribution margin**, then **material** farm net after **labor charge**, then a **salary-replacement band**—without inventing **your** household budget.

**Pairs with**: [`East Tennessee two-site farm business plan — revenue model and milestones`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md). **Phase financial gates** (consolidated): [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md).

**Financial layer links**: [`Enterprise unit economics — worksheet methodology`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md), [`Farm accounting baseline`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md), [`CAPEX, OPEX, and enterprise sequencing`](capex-opex-enterprise-sequencing-two-site-constraint.md).

---

## Required inputs (must exist before claiming any milestone)

| Input | Symbol | Description |
|-------|--------|-------------|
| Household cash need | `HH_NEED` | Annual **household** cash from **all** sources—**placeholder** until family finance work; may be **range** `HH_LOW`–`HH_HIGH` |
| Farm share target | `FARM_SHARE_TARGET` | Share of `HH_NEED` for **replacement narrative**—**%** (e.g. `0.50`–`0.90`) |
| Off-farm cash + benefits | `OFFFARM` | Annual **off-farm** wages + **benefits imputation** if quitting is in scope |
| Contribution margin (farm) | `CONTRIB_MARGIN_Y` | For calendar year **Y**: revenue − **variable** costs (per **accounting baseline**—same story as management P&L) |
| Farm cash to household | `FARM_CASH_TO_HH_Y` | **Cash** actually available to household after **debt service**, **owner draw** policy, and **WC**—define **once** in a footnote |
| Family labor shadow band | `SHADOW_LOW`, `SHADOW_HIGH` | **$/hr** for **opportunity-cost** charge in **M3**—never a single point without range |
| Scenario | `S1`, `S2`, … | Enterprise mix—**milestones may differ** by scenario |
| Split-site + automation | — | **Telemetry OPEX** and **extra miles** in **CONTRIB_MARGIN** path—must not vanish |

---

## Milestone formulas (explicit)

Let **Y** = calendar year. **All comparisons use filled placeholders—no wiki defaults.**

| ID | Milestone | Formula / condition | Pass when |
|----|-----------|---------------------|-----------|
| **M0** | Baseline | Ledger exists | **M0** = **Y** iff 12-mo **household + farm** cash tracking **exists** |
| **M1** | Supplemental | `FARM_CASH_TO_HH_Y ≥ TH_M1` **or** `FARM_CASH_TO_HH_Y ≥ ρ_M1 × HH_NEED` | **ρ_M1**, `TH_M1` **filled**; **evidence**: bank categorization |
| **M2** | Positive operating | `CONTRIB_MARGIN_Y > 0` | **Strict inequality**—zero is **fail** unless **documented** subsidy row (see bridge) |
| **M3** | Material after labor charge | `FARM_NET_Y − L_CHRG_Y ≥ TH_M3` where `L_CHRG_Y = H_FAM_Y × σ` with `σ ∈ [SHADOW_LOW, SHADOW_HIGH]` | **Sensitivity** table **required**—two columns min |
| **M4** | Salary band | `FARM_CASH_TO_HH ≥ FARM_SHARE_TARGET × HH_NEED` for **each** of **`N_M4`** consecutive calendar years | **N_M4** **filled**; evidence **calendar** unless fiscal **documented** |

**Notation**: `TH_*` = threshold **$**; `ρ_*` = **fraction** of `HH_NEED`.

---

## No-salary-claim rule (hard)

1. **Do not** state or imply **salary replacement**, **quit your job**, or **farm supports household** at **replacement** level in **executive summary**, **lender decks**, or **public** narrative until **Fin-G(3→4)** **PASS** per [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md) **and** **M4** row **evidence** **complete**.
2. **Allowed** before that: **side income**, **learning**, **supplemental**, **pilot**, **pre-revenue**—with **dates**.
3. **Remediation** alignment: see [`Remediation backlog`](east-tennessee-two-site-farm-business-plan-remediation-backlog.md) salary narrative weakness.

---

## Bridge-year logic (anti-optimism)

**Definition**: Year **Y** is a **bridge year** iff:

`(OFFFARM_Y + FARM_CASH_TO_HH_Y) < HH_NEED` **and** the family **documents** an **explicit** **subsidy** or **off-farm** **plan** (savings draw, spousal income, **dated** **end** of subsidy).

**Rules**:

| Rule | Statement |
|------|-----------|
| B1 | Bridge years **must** appear in the **bridge table** below—**hidden** subsidy **fails** **Fin-G(1→2)** |
| B2 | **Maximum** consecutive bridge years **without** **M2** pass: **`BRIDGE_MAX`** (placeholder)—exceeding **triggers** **scale freeze** review |
| B3 | If **M2** fails **two** consecutive years—**freeze** scale per [`Vision` stop rules](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) and branching in [`Recommended enterprise strategy`](east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md) |

**Formula (subsidy end)**: If using **explicit subsidy** instead of **M2**, document **`T_SUBSIDY_END`**; **Fin-G(2→3)** **requires** either **M2** **or** **subsidy ended** with **replacement** path.

---

## Phase advance — revenue side (crosswalk)

| Phase transition | Revenue milestone / financial gate |
|------------------|--------------------------------------|
| 0 → 1 | **M0** + **Fin-G(0→1)** inputs |
| 1 → 2 | **M1** target **in progress** + **Fin-G(1→2)** (includes **G1**) |
| 2 → 3 | **M2** **or** **bridge** with end date + **Fin-G(2→3)** (**G2**) |
| 3 → 4 | **M3** **inputs** minimum + **M4** for **narrative** + **Fin-G(3→4)** (**G3**) |

Full criteria: [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md).

---

## Outputs supported

| Output | Decision |
|--------|----------|
| **M0–M4** pass/fail | **When** to claim supplemental vs replacement |
| **Bridge years** | Explicit **years** where farm **subsidizes** learning |
| **Scale freeze** | Tie to **negative** trailing margin—[`remediation backlog`](east-tennessee-two-site-farm-business-plan-remediation-backlog.md) |
| **Evidence list** | Bank, P&L, tax, sale bills **per** milestone |

---

## Assumptions

| Assumption | Note |
|------------|------|
| **Milestones are scenario-aware** | If **S2** replaces **S1**, **restate** targets |
| **Low-labor priority** | Milestone can **pass** on **revenue** but **fail** on **labor**—track **both** if policy requires |
| **Automation** | **Net** family hours: **field** − **efficiency** + **triage**—[`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md) |
| **Two sites** | **All-in** **channel** cost in **evidence**—haul **included** |

---

## Placeholder registry (fill with evidence—not wiki guesses)

| Term | Definition |
|------|------------|
| `HH_NEED` | **`$___`** — refresh **annually** |
| `FARM_SHARE_TARGET` | **`___`** (fraction) |
| `OFFFARM` | **`$___/yr`** + benefits note |
| `TH_M1`, `ρ_M1` | **$** or **fraction** for **M1** |
| `TH_M3` | **$** for material supplement |
| `N_M4` | Consecutive years for **M4** |
| `BRIDGE_MAX` | Integer |
| `CONTRIB_MARGIN` | Same as accounting baseline **variable** definition |

---

## Milestone ladder (evidence columns)

| ID | Milestone | Metric | Target (placeholder) | Evidence | Phase |
|----|-----------|--------|----------------------|----------|-------|
| M0 | **Baseline** | Ledger exists | **Y/N** | Spreadsheet export | 0 |
| M1 | **Supplemental** | `FARM_CASH_TO_HH` | `TH_M1` **or** `ρ_M1 × HH_NEED` | Bank | 1–2 |
| M2 | **Positive operating** | `CONTRIB_MARGIN_Y` | **> 0** | Management P&L | 2 |
| M3 | **After labor charge** | `FARM_NET − L_CHRG` | `≥ TH_M3` | Worksheet + log | 3 |
| M4 | **Salary band** | `FARM_CASH_TO_HH` | `≥ FARM_SHARE_TARGET × HH_NEED` × **N_M4** years | Bank + books | 4 |

---

## Bridge years (explicit)

| Calendar year | Scenario | Farm cash to HH | Off-farm | Combined vs `HH_NEED` | Subsidy / notes |
|---------------|----------|-----------------|----------|------------------------|-----------------|
| | | | | | |
| | | | | | |

---

## Revenue stream mix (by phase — edit)

| Phase | Primary streams (plan default) | Share of farm cash (est %) | Uncertainty flag |
|-------|--------------------------------|----------------------------|------------------|
| 0–1 | Lease / none / costs only | | |
| 2 | Grazing sales ± lease | | |
| 3 | + scale or second stream | | |
| 4 | + direct or value-add optional | | |

---

## Branching logic

| If… | Then… |
|-----|--------|
| **M2** missed **2** years | **Freeze** scale—[`Recommended enterprise strategy`](east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md) |
| **M4** met but off-farm needed for **health insurance** | **Do not** claim full replacement—**adjust** milestone |
| **Enterprise mix changes** | **Re-baseline** **M1–M4** |
| **Trailing margin negative** | **Scale freeze**—[`remediation backlog` §13](east-tennessee-two-site-farm-business-plan-remediation-backlog.md) |

---

## Known / assumed / open

| Class | Content |
|-------|---------|
| **Known** | Side business profit intent; **10-year** horizon |
| **Assumed** | `HH_NEED` stable enough to plan—**revisit yearly** |
| **Open** | Benefits replacement cost; **live** **scenario** **ID** |

---

## Links

- [`East Tennessee two-site farm business plan — 10-year roadmap`](east-tennessee-two-site-farm-business-plan-10-year-roadmap.md)
- [`Capital phasing table`](capital-phasing-table-years-0-10-two-site-smart-farm.md)
- [`Business risk register`](business-risk-register-two-site-smart-farm.md)
- [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md)
