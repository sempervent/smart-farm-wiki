---
title: Execution gates — financial thresholds (phase advances)
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
review_status: unreviewed
tags:
  - business-plan
  - gates
  - finance
  - phases
confidence: medium
aliases:
  - Financial execution gates ET two-site
---

# Execution gates — financial thresholds (phase advances)

## Purpose

Consolidate **pass/fail financial criteria** for advancing the East Tennessee two-site plan across **business phases 0–4** (see [`10-year roadmap`](east-tennessee-two-site-farm-business-plan-10-year-roadmap.md)). These **financial gates** **sit beside**—do not replace—**research gates** **V1–Vn** and **decision gates** **G1–G3** in [`Validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md) and **major-spend** gates in [`Validation backlog — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md).

**Detail pages**: [`Revenue milestone model`](revenue-milestone-model-supplemental-to-salary-replacement.md) (milestones **M0–M4**, bridge years), [`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md) (contribution margin and labor tests), [`CAPEX, OPEX, and enterprise sequencing`](capex-opex-enterprise-sequencing-two-site-constraint.md) (spend, debt, unlocks).

**Rules**: **No fabricated dollars**—every threshold is a **named placeholder** to be filled from books, quotes, and lender constraints. **Optimism-driven spending** fails by design if evidence columns are empty.

---

## Identifier map

| ID | Meaning |
|----|---------|
| **Fin-G(0→1)** | Financial permission to treat Phase **0** work as complete and **enter** Phase **1** spend posture |
| **Fin-G(1→2)** | Permission to **unlock** Phase **2** CAPEX / herd scale posture (with **G1**) |
| **Fin-G(2→3)** | Permission to **scale** or add second stream (with **G2**) |
| **Fin-G(3→4)** | Permission to use **salary-replacement narrative** and Phase **4** architecture (with **G3**) |
| **M0–M4** | Revenue milestones—[`Revenue milestone model`](revenue-milestone-model-supplemental-to-salary-replacement.md) |
| **FC*** | Financial condition rows in tables below—**boolean** once filled |

---

## Fin-G(0→1) — Phase 0 complete → Phase 1 allowed

| # | Criterion | Pass logic | Evidence |
|---|-----------|------------|----------|
| FC0.1 | Baseline ledger | **M0** = **Y** (12-mo household + farm cash picture **started**) | Export / accountant attestation |
| FC0.2 | Household need bounded | `HH_NEED` **filled** as **range** `[HH_LOW, HH_HIGH]` **or** single placeholder with **review date** | Family worksheet |
| FC0.3 | Stop rules numeric | [`Vision` stop rules](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) **debt / automation** thresholds use **placeholders** `D%`, `N` weeks—not blank prose | Written table |
| FC0.4 | Working capital floor (homestead + farm ops) | `WC_MONTHS_MIN_P0` **≥** `___` months **liquidity** policy **documented** (not necessarily achieved—**policy** must exist) | Policy memo |
| FC0.5 | **No salary claim** | **No** document in **fundraising/lender** pack asserts **salary replacement**—narrative **quarantine** per revenue milestone page | Checklist |

**Aggregate pass**: `Fin-G(0→1) = FC0.1 ∧ FC0.2 ∧ FC0.3 ∧ FC0.4 ∧ FC0.5`.

---

## Fin-G(1→2) — Phase 1 → Phase 2 (operating business posture)

| # | Criterion | Pass logic | Evidence |
|---|-----------|------------|----------|
| FC1.1 | Research **G1** | **G1** = **PASS** (V1–V4 minimum + legal use)—**non-financial** prerequisite | Validation backlog |
| FC1.2 | Bridge years explicit | **Bridge table** in revenue milestone model has **rows** for each planning year touched—**no hidden** subsidy of farm by household | Same page |
| FC1.3 | Unit economics sanity | For **each** **active** enterprise row in worksheet: `CM_X` **computed**; **MVCM** test documented—[`Enterprise unit economics` §MVCM](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md) | Worksheet |
| FC1.4 | Split-site burden bounded | `R_SPLIT` = split-site incremental $ / **positive** contrib margin denominator—**policy**: advance only if `R_SPLIT ≤ R_SPLIT_MAX` **or** **exception** logged | Worksheet |
| FC1.5 | Major fence/water/herd CAPEX | **Only** if **G1** **and** **Fin-G(1→2)** **and** line tied to [`capex unlock matrix`](capex-opex-enterprise-sequencing-two-site-constraint.md) | Capital phasing table |

**Aggregate pass**: `Fin-G(1→2) = FC1.1 ∧ FC1.2 ∧ FC1.3 ∧ FC1.4` (FC1.5 applies **per** CAPEX line).

---

## Fin-G(2→3) — Phase 2 → Phase 3 (scale / second stream)

| # | Criterion | Pass logic | Evidence |
|---|-----------|------------|----------|
| FC2.1 | Research **G2** | **G2** = **PASS** | Validation backlog |
| FC2.2 | **M2** contribution margin | `CONTRIB_MARGIN_Y > 0` for **at least one** full calendar year **Y** **or** **documented** explicit subsidy with **end date** `T_SUBSIDY_END` | P&L |
| FC2.3 | Labor-charged materiality | **M3** **worksheet** **complete** (family shadow rate **band** + hours)—even if **M3** **dollar** target **not** met, **inputs** must exist to **fail consciously** | Labor log + worksheet |
| FC2.4 | Trailing margin stop | **Not** **two** consecutive years **negative** operating cash **after** labor charge—else **freeze** per [`Vision`](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) | P&L trend |
| FC2.5 | Debt service | If **any** **new** term debt since Phase 1: `DSR = debt service / gross farm revenue ≤ DSR_MAX` **or** **stop** scale | Lender schedule |

**Aggregate pass**: `Fin-G(2→3) = FC2.1 ∧ FC2.2 ∧ FC2.3 ∧ FC2.4 ∧ FC2.5`.

---

## Fin-G(3→4) — Phase 3 → Phase 4 (salary-replacement **narrative**)

| # | Criterion | Pass logic | Evidence |
|---|-----------|------------|----------|
| FC3.1 | Research **G3** | **G3** = **PASS** | Validation backlog |
| FC3.2 | **M4** salary band | Farm cash **≥** `FARM_SHARE_TARGET × HH_NEED` for **`N_M4`** consecutive years (placeholders) | Bank + books |
| FC3.3 | **No premature salary claim** | **M4** row **filled**—**executive summary** / external narrative may **only** use **salary replacement** language if **Fin-G(3→4)** **PASS** | Milestone table |
| FC3.4 | Benefits / off-farm | If **health** or **benefits** require off-farm work: **explicit** line in milestone model—**no** “full quit” claim | Written |

**Aggregate pass**: `Fin-G(3→4) = FC3.1 ∧ FC3.2 ∧ FC3.3 ∧ FC3.4`.

---

## Crosswalk: financial gates ↔ validation gates

| Financial gate | Requires (non-exhaustive) |
|----------------|----------------------------|
| **Fin-G(1→2)** | **G1** + bridge + unit economics |
| **Fin-G(2→3)** | **G2** + **M2**/subsidy rule + labor worksheet + DSR |
| **Fin-G(3→4)** | **G3** + **M4** |

---

## On failure

| Gate fails | Action |
|------------|--------|
| **Fin-G(1→2)** | **Defer** Phase **2** livestock/fence **scale** CAPEX; continue Phase **1** intelligence; **no** **blame**—update evidence |
| **Fin-G(2→3)** | **Freeze** scale; [`Recommended enterprise strategy`](east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md) **fallback** posture; **remediation** [`remediation backlog`](east-tennessee-two-site-farm-business-plan-remediation-backlog.md) |
| **Fin-G(3→4)** | **Do not** claim salary replacement; **do not** expand **debt** for **lifestyle** CAPEX |

---

## Related

- [`East Tennessee two-site farm business plan — revenue model and milestones`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md)
- [`Farm accounting baseline`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md)
- [`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md)
