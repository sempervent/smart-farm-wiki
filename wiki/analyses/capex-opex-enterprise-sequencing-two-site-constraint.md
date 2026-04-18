---
title: CAPEX, OPEX, and enterprise sequencing — two-site constraint
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-18
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

Anchor **where and when** capital and recurring spend land across **`SITE_HOMESTEAD`** and **`SITE_FARM`** when sites are separated by **`COMMUTE_ONE_WAY`** and work is **batched**. Connect **phased capital**, **enterprise choice**, **split-site logistics**, **family labor**, and **automation** (as both **line items** and **risk reduction**) without inventing **your** dollar figures.

**Consumes**: [`Enterprise unit economics — worksheet methodology`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md), [`Farm accounting baseline`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md).

**Feeds**: [`Capital phasing table`](capital-phasing-table-years-0-10-two-site-smart-farm.md), [`East Tennessee two-site farm business plan — capital and financing`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md), [`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md).

---

## Required inputs

| Input | Description |
|-------|-------------|
| `SITE_HOMESTEAD`, `SITE_FARM` | Roles (office, NOC, cold, tools vs field, livestock, crop) |
| `COMMUTE_ONE_WAY` | Minutes—drives **batching** and **trip ROI** |
| `PRIMARY_ENTERPRISES` | Ordered list with **validation status** per scenario |
| **Gate IDs** | Which **V#/G#** must pass before each **capex** line |
| **Automation stack choice** | Self-hosted vs vendor; **OPEX** and **ops hours** policy |
| **Working capital policy** | Months of **operating cash** before **term** equipment |

---

## Outputs supported

| Output | Use |
|--------|-----|
| **Phasing table** (below) | Board / family alignment; lender narrative (evidence-backed only) |
| **Duplicate vs consolidate** decisions | Second tank, cold, gen-set vs **hauling** |
| **Enterprise sequencing** | What **proof** precedes **permanent** infrastructure |
| **OPEX visibility** | Distance-inflated **fuel**, **time**, **spoilage**, **LTE**, **telemetry** subs |

---

## Assumptions (placeholders)

| Placeholder | Meaning |
|-------------|---------|
| `SITE_HOMESTEAD` | Smaller site; may hold **office**, **cold storage**, **tools**, **LAN**, **broker** (if self-hosted). |
| `SITE_FARM` | Production parcel; **field infrastructure**, **livestock facilities**, **irrigation**, **gateways**. |
| `PRIMARY_ENTERPRISES` | Ordered list **TBD** — drives which **CAPEX** is non-negotiable first. |
| **Scenario fork** | **S1 / S2** enterprise mixes may require **different** **first** **infrastructure**—keep **parallel** rows until validation. |

---

## What stays placeholder until evidence exists

| Item | Fill with |
|------|-----------|
| **$** in phasing table | Quotes, bids, **UT budgets** scaled to your units—not wiki guesses |
| **Trips/year** | Odometer + **batch** log |
| **Water / fence** line items | Well report, NRCS plan, **engineer** if needed |
| **Financed rows** | **Only** after [`do-not-finance` / validation gates](east-tennessee-two-site-farm-business-plan-remediation-backlog.md) satisfied |

---

## Why two sites change the math

- **Duplicate vs consolidated**: Second **fuel tank**, **tool cache**, **generator**, **cold room** vs **hauling**—each has **capex + opex** (fuel, time, spoilage).
- **Telemetry**: Fixed tower/mast **CAPEX** pays back only if **trip reduction**, **risk**, and **labor** net out—[`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md), [`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md), [`Field telemetry reference architecture`](field-telemetry-reference-architecture-homestead-120ac.md).
- **Automation**: Budget **hardware**, **subscriptions**, **patching**, and **triage** as **first-class** OPEX—not “savings.”
- **Family labor**: **Phased** spend must fit **surge** windows—[`Labor model`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md).
- **Uncertainty**: **Do not** sequence **large** **single-enterprise** **assets** before **market** and **processing** gates when mix is open—[`Enterprise options`](east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md).

---

## Phasing table — CAPEX by site and phase (fill in)

| Year / phase | `SITE_HOMESTEAD` CAPEX (examples) | `SITE_FARM` CAPEX (examples) | Shared / either site | Depends on gate / scenario |
|--------------|-----------------------------------|------------------------------|------------------------|----------------------------|
| 0–1 | | | | e.g. access, **water rights**, **legal** |
| 2–3 | | | | |
| 4–5 | | | | |
| 6–10 | | | | |

---

## OPEX buckets affected by distance and two-site ops

| Bucket | Driver | Notes |
|--------|--------|-------|
| **Vehicle** | miles × trips/year × $/mile; time × shadow $/hr | Link to **unit economics** worksheet |
| **Duplication** | two internet links, two monitoring stacks vs **VPN** | [`Field telemetry reference architecture`](field-telemetry-reference-architecture-homestead-120ac.md) |
| **Spoilage / shrink** | wrong-site cold chain | [`Dual-site operations model`](dual-site-operations-model-non-agritourism.md) |
| **Telemetry** | LTE, cloud, spares | **Automation** as **cost** |
| **Hired relief** | when family **cannot** cover surge | Explicit **row**—not hidden in “misc” |

---

## Enterprise sequencing vs phased capital (template)

| Enterprise / asset | Minimum proof | **Defer** large CAPEX until |
|--------------------|-----------------|----------------------------|
| | | |
| | | |

---

## Grounded sources (ingested — patterns, not your numbers)

- [`UT Extension — Farm Management Boot 2017 budgets (Velandia)`](../source-notes/ut-extension-fm-boot-2017-budgets-velandia-pdf.md) — training-style budget **line-item** shapes.
- Enterprise publication PDFs: [`ut-publication-w1348-pdf`](../source-notes/ut-publication-w1348-pdf.md) (example enterprise worksheets), sibling **D**-series notes—confirm titles inside PDFs.
- [`Tennessee hobby farm and small-farm business sources`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md) — regulatory **pointers**.

---

## Related

- [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md)
- [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md)
- [`Own equipment vs custom hire under two-site logistics`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md)
- [`Business viability and farm economics — gap analysis`](business-viability-and-farm-economics-gap-analysis.md)
- [`Business plan remediation backlog`](east-tennessee-two-site-farm-business-plan-remediation-backlog.md) — water, WC, fence OPEX, **do not finance** rules

---

## Open items

- [ ] Fill phasing table with **priorities** and **evidence-backed** ranges (internal spreadsheet OK).
- [ ] Attach **accountant**-ready **mileage** and **home office** allocation rules—professional advice.
- [ ] Tie each **financed** line to a **validation gate ID** in [`capital phasing`](capital-phasing-table-years-0-10-two-site-smart-farm.md).

---

*Numeric blanks in the wiki are intentional; evidence belongs in books and source-notes.*
