---
title: Enterprise unit economics — worksheet methodology (two-site smart farm)
page_type: analysis
status: draft
created: 2026-04-18
updated: 2026-04-18
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

Provide a **repeatable worksheet pattern** for comparing **candidate enterprises** and **mixed strategies** on the **same land and labor envelope**—without requiring a single committed enterprise mix. Outputs feed [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md), [`Farm accounting baseline — chart of accounts and enterprise P&L structure`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md), and [`Revenue milestone model — supplemental income to salary replacement`](revenue-milestone-model-supplemental-to-salary-replacement.md).

**Non-goals**: Picking “the” enterprise here; publishing dollar forecasts without evidence.

---

## Required inputs (gather before treating any row as “true”)

| Input | Description | Typical source |
|-------|-------------|----------------|
| **Enterprise list** | Named candidates with **primary product** and **exit channel** | [`Enterprise options analysis`](east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md) |
| **Unit definition** | What one “unit” is (head, lb sold, bed-night, acre rotation, etc.) | Owner definition; must be **stable** year to year for comparison |
| **Time horizon** | Planning years for the worksheet (e.g. 1-yr rolling + 5-yr scenario) | Plan phases |
| **Split-site parameters** | `COMMUTE_ONE_WAY`, batching pattern, which tasks run at `SITE_HOMESTEAD` vs `SITE_FARM` | [`Two-site operations model`](two-site-operations-model-5ac-homebase-120ac-production.md) |
| **Family labor envelope** | Hours/week by role; **surge** windows | [`Labor model`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md), coverage matrix |
| **Shadow labor rate** | Imputed **$/hr** for family time (sensitivity band, not a paycheck) | Family policy; **never** single point without range |
| **Automation posture** | What is **manual baseline** vs **instrumented** scenario | [`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md), priority matrix |
| **Evidence hooks** | UT/extension budgets, auction reports, processor quotes—**per enterprise** | [`Source-ingest campaign`](business-plan-source-ingest-campaign-east-tennessee-two-site.md) |

---

## Outputs this worksheet supports

| Output | Consumer page / decision |
|--------|---------------------------|
| **Contribution margin per unit** (revenue − **variable** costs allocated to enterprise) | Scale / no-scale gates; milestone **M2** |
| **Cash timing profile** (when costs hit vs revenue) | Working capital; [`capital phasing`](capital-phasing-table-years-0-10-two-site-smart-farm.md) |
| **Labor hours per unit** (family + hired + **triage** for telemetry) | Low-labor priority; surge feasibility |
| **Split-site OPEX per unit** (miles, duplicate tools, cold chain) | [`CAPEX/OPEX sequencing`](capex-opex-enterprise-sequencing-two-site-constraint.md) |
| **Scenario branches** (e.g. grazing-led vs row vs mixed) | Uncertainty in enterprise mix—**parallel rows**, not one hidden default |

---

## Assumptions (explicit)

| Assumption | Why it matters |
|------------|----------------|
| **Contribution margin first** | Full allocation of **all** farm overhead to one enterprise often **lies**; use **ranges** and **sequential** allocation rules documented on the accounting baseline page. |
| **Family labor has opportunity cost** | Even if unpaid, it competes with off-farm income and sleep—use **shadow rate band** for **comparability**, not tax reporting. |
| **Automation is two-sided** | CAPEX + subscriptions + **false-positive triage** hours—see instrumentation ROI page. |
| **Two sites inflate or duplicate cost** | Same enterprise can have **different** unit economics if logistics force duplicate equipment vs consolidated hub. |
| **Enterprise mix is uncertain** | Maintain **at least two** named scenarios until validation closes the fork. |

---

## Placeholders until real numbers exist

Keep these as **literal placeholders** in working copies (spreadsheets or tables below); do not round fake precision.

| Placeholder | Meaning |
|-------------|---------|
| `U_X` | Physical **unit** for enterprise X (define once) |
| `P_X` | **Price** or **revenue per unit** — *range* `[ ___, ___ ]` |
| `V_X` | **Variable cash costs per unit** (see allocation rules) |
| `H_FAM_X` | **Family hours per unit** (normal week) |
| `H_SURGE_X` | **Extra hours per unit** in worst window |
| `H_AUTO_X` | **Triage / IT / dashboard** hours per unit attributable to automation |
| `D_MI` | **Delivery miles** or **trips** per unit affecting split-site OPEX |
| `CM_X` | **Contribution margin** = price − variable costs (cash basis section) |

---

## Worksheet A — Unit definition and channel

| Enterprise ID | Name | Primary unit `U_` | Primary exit channel | Notes (processing, haul, regulation) |
|-----------------|------|-------------------|----------------------|--------------------------------------|
| E1 | | | | |
| E2 | | | | |
| E3 | | | | |

---

## Worksheet B — Variable costs per unit (cash)

**Rule**: Only costs that **scale with production** in the planning year (feed, vet, fuel for field work, packaging, **incremental** hired labor). **Do not** bury mortgage or manager salary here—those go to overhead allocation on the accounting baseline page.

| Line | E1 | E2 | E3 |
|------|----|----|-----|
| Purchased inputs | | | |
| Veterinary / health | | | |
| Marketing / commissions | | | |
| Haul / transport allocated | | | |
| Processing fees | | | |
| **Variable subtotal** | | | |

---

## Worksheet C — Split-site logistics load per unit

Allocate **only the incremental** cost of **distance** and **site choice** (extra miles, duplicate cold storage, second internet if required for this enterprise).

| Line | Formula hint | E1 | E2 | E3 |
|------|--------------|----|----|-----|
| Trips per unit sold / produced | | | | |
| Miles per trip × $/mile | placeholder | | | |
| Time per trip × shadow $/hr | optional | | | |
| **Split-site incremental** | sum | | | |

---

## Worksheet D — Labor per unit (family + hired + automation triage)

| Line | E1 | E2 | E3 |
|------|----|----|-----|
| Family field hours | | | |
| Family admin / sales hours | | | |
| Hired hours | | | |
| Telemetry triage + IT hours | | | |
| **Labor total** | | | |

**Low-labor priority**: Rank enterprises by **labor per $ contribution margin** under **normal** and **surge**—two columns minimum.

---

## Worksheet E — Scenario matrix (enterprise mix uncertainty)

| Scenario ID | Description (e.g. “grazing-led + lease,” “mixed + direct”) | E1 share of revenue | E2 share | E3 share | Active? (Y/N) |
|-------------|--------------------------------------------------------------|---------------------|----------|----------|---------------|
| S1 | | ___% | ___% | ___% | |
| S2 | | | | | |

**Combined view** (after overhead allocation method chosen):

| Scenario | Blended CM (placeholder) | Peak cash need month | Binding labor constraint |
|----------|---------------------------|----------------------|--------------------------|
| S1 | | | |
| S2 | | | |

---

## Git-oriented practice

- **Version** worksheet assumptions in commit messages or a short **“Assumptions changelog”** subsection at the bottom of a working branch copy—not by silently overwriting tables.
- Prefer **one canonical table** in wiki + **linked** external sheet for numbers, with **date** in the sheet title.

---

## Links

- [`East Tennessee two-site farm business plan — revenue model and milestones`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md)
- [`Business viability and farm economics — gap analysis`](business-viability-and-farm-economics-gap-analysis.md)
- [`Own equipment vs custom hire under two-site logistics`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md)
