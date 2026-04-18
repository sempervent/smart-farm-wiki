---
title: CAPEX, OPEX, and enterprise sequencing — two-site constraint
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
review_status: unreviewed
tags:
  - economics
  - two-site
  - capex
  - sequencing
confidence: low
---

# CAPEX, OPEX, and enterprise sequencing — two-site constraint

## Purpose

Anchor **where and when** capital and recurring spend land across **`SITE_HOME`** and **`SITE_FARM`** when sites are separated by **`COMMUTE_ONE_WAY`** and work is **batched**. Define **forbidden debt cases**, **infrastructure unlock logic**, and **spend-stop conditions**—without inventing **your** dollar figures.

**Consumes**: [`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md), [`Farm accounting baseline`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md).

**Feeds**: [`Capital phasing table`](capital-phasing-table-years-0-10-two-site-smart-farm.md), [`Capital and financing`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md), [`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md), [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md).

---

## Required inputs

| Input | Description |
|-------|-------------|
| `SITE_HOME`, `SITE_FARM` | Roles (office, NOC, cold, tools vs field, livestock, crop) |
| `COMMUTE_ONE_WAY` | Minutes—**batching** and **trip ROI** |
| `PRIMARY_ENTERPRISES` | Ordered list with **validation status** per scenario |
| **Gate IDs** | **G1–G3**, **Fin-G(*→*)**, **V#** before each **capex** line |
| **Automation stack** | Self-hosted vs vendor—**OPEX** and **ops hours** |
| **Working capital policy** | Months of **operating cash** before **term** equipment |

---

## Forbidden debt-funding cases (hard stops)

**Principle**: No **new** term obligation to **fund optimism**. Aligns with [`Remediation backlog` §3 do-not-finance](east-tennessee-two-site-farm-business-plan-remediation-backlog.md).

| ID | Case | Forbidden until |
|----|------|-------------------|
| **FD-1** | **Equipment** (hay, loader, truck, major mower) **without** **hours/year** **proof** **and** **custom-hire** **quote** **compared** | **V#** **hired** proof + **worksheet** row |
| **FD-2** | **New** term debt when **`WC_MONTHS < WC_MONTHS_MIN`** per family policy | **WC** **restored** **or** **plan** **documented** |
| **FD-3** | **Personal guarantee** term debt **without** **written** **worst-case** **exit** + **household** **stress** **test** | **Stress** **doc** **Y/N** |
| **FD-4** | **Telemetry / homelab** **CAPEX** **stack** **when** **`H_TRIAGE` > `H_TRIAGE_MAX`** (see enterprise unit economics) | **Triage** **reduced** **or** **scope** **cut** |
| **FD-5** | **Fence/water/herd** **scale** **financing** **when** **G1** **FAIL** | **G1** **PASS** |
| **FD-6** | **Phase 4**-style **lifestyle** **build** (shop, barn aesthetic) **when** **Fin-G(3→4)** **FAIL** | **M4** + **Fin-G(3→4)** **or** **cash** **only** |

**Rule**: Any **proposed** **financed** line must cite **gate ID** in [`capital phasing table`](capital-phasing-table-years-0-10-two-site-smart-farm.md).

---

## Infrastructure unlock logic

**Unlock** = permission to **execute** CAPEX **commitment** (contract signed, wire sent)—not **maintenance**.

| Infrastructure class | Minimum gate bundle | Notes |
|----------------------|---------------------|-------|
| **Legal / access / survey** | **V8** + **FC0** baseline | Before **other** |
| **Water** (well, line, tank) | **V2** + **G1** (if tied to herd) + **Fin-G(1→2)** as applicable | **FD-5** |
| **Fence MVP** | **V3** + **V4** + **G1** | Sized to **stocking** **plan** |
| **Corral / load-out** | **V6** processing path + **G1** | **Haul** **real** |
| **Field gateway / tower** | **V10** + **pilot** ROI row | [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md) |
| **Homestead broker / server** | **Cyber** minimum from [`Remote access`](remote-access-operational-security-model-two-site-smart-farm.md) | **Not** **FD-4** **if** **triage** **unbounded** |

**Matrix (fill—placeholders only)**

| CAPEX line | Site | Unlocks after (gate IDs) | Financed? Y/N |
|------------|------|--------------------------|---------------|
| | | | |
| | | | |

---

## Spend-stop conditions (freeze / pause CAPEX)

| Trigger | Condition (placeholder) | Action |
|---------|---------------------------|--------|
| **SS-1** | Trailing **2**-year **operating** cash **negative** after **labor** charge | **Freeze** non-essential CAPEX—[`Vision` stop rules](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) |
| **SS-2** | `DSR > DSR_MAX` (debt service / gross farm revenue) | **No** **new** term—**pay** **down** **or** **revenue** |
| **SS-3** | **Automation OPEX** **>** **documented** **benefit** (trips + risk **$**) | **De-scope** per [`Vision` **C6**](east-tennessee-two-site-farm-business-plan-vision-and-constraints.md) |
| **SS-4** | **Key person** **unavailable** **>** `N` **weeks** | **Reduce** **livestock** **exposure**; **pause** **growth** **CAPEX** |
| **SS-5** | **MVCM-1** **fail** on **primary** enterprise | **No** **scale** **debt**—[`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md) |

---

## Outputs supported

| Output | Use |
|--------|-----|
| **Phasing table** | Family / lender—**evidence-backed** only |
| **Duplicate vs consolidate** | Second tank vs **hauling** |
| **Enterprise sequencing** | **Proof** before **permanent** infrastructure |
| **OPEX visibility** | Distance, duplication, telemetry subs |

---

## Assumptions (placeholders)

| Placeholder | Meaning |
|-------------|---------|
| `SITE_HOME` | **Office**, **cold**, **broker**, **tools** |
| `SITE_FARM` | **Field** infra, **livestock**, **irrigation** |
| `PRIMARY_ENTERPRISES` | Ordered list **TBD** |
| `WC_MONTHS_MIN`, `DSR_MAX`, `N` | **Fill** from policy / lender |

---

## Why two sites change the math

- **Duplicate vs consolidated** equipment and **cold** chain.
- **Telemetry**: CAPEX **pays** only if **trip**, **risk**, **labor** **net**—[`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md).
- **Family labor**: **Phased** spend must fit **surge**—[`Labor model`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md).

---

## Phasing table — CAPEX by site and phase (fill)

| Year / phase | `SITE_HOME` CAPEX | `SITE_FARM` CAPEX | Shared | Gates |
|--------------|-------------------|-------------------|--------|-------|
| 0–1 | | | | |
| 2–3 | | | | |

---

## OPEX buckets (split-site)

| Bucket | Driver |
|--------|--------|
| **Vehicle** | miles × trips × $/mi |
| **Duplication** | two links vs VPN |
| **Telemetry** | LTE, cloud, spares |
| **Hired relief** | surge **uncovered** |

---

## Enterprise sequencing vs phased capital (template)

| Enterprise / asset | Minimum proof | Defer large CAPEX until |
|--------------------|---------------|-------------------------|
| | | |

---

## Grounded sources (patterns, not your numbers)

- [`UT Extension — Farm Management Boot 2017 budgets`](../source-notes/ut-extension-fm-boot-2017-budgets-velandia-pdf.md)
- [`Tennessee hobby farm and small-farm business sources`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md)

---

## Related

- [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md)
- [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md)
- [`Own equipment vs custom hire under two-site logistics`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md)
- [`Business plan remediation backlog`](east-tennessee-two-site-farm-business-plan-remediation-backlog.md)

---

*Numeric blanks are intentional; evidence belongs in books and source-notes.*
