---
title: CAPEX, OPEX, and enterprise sequencing — two-site constraint
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - economics
  - two-site
  - capex
review_status: unreviewed
confidence: low
---

# CAPEX, OPEX, and enterprise sequencing — two-site constraint

## Purpose

Provide a **foundation** page for **where and when capital and recurring spend** land across **`SITE_HOMESTEAD`** and **`SITE_FARM`** when the two are separated by **`COMMUTE_ONE_WAY`** and **batch work** is required. This **connects** Strand **B** (business) to **D/E** (equipment, power, telemetry) without inventing **your** dollar figures.

## Scope

- **In scope**: Sequencing **questions**, **placeholder phasing table**, **OPEX categories** that repeat because of **distance**, links to **UT budget** and **enterprise** source-notes.
- **Out of scope**: Tax treatment, loan covenants, **guaranteed** returns.

## Assumptions (placeholders)

| Placeholder | Meaning |
|-------------|---------|
| `SITE_HOMESTEAD` | Smaller site; may concentrate **office, cold storage, tools**, **LAN**, **broker** (if self-hosted). |
| `SITE_FARM` | Production parcel; **field infrastructure**, **livestock facilities**, **irrigation**, **gateways**. |
| `PRIMARY_ENTERPRISES` | Ordered list **TBD** — drives which **CAPEX** is non-negotiable first. |

## Why two sites change the math

- **Duplicate vs consolidated**: Second **fuel tank**, **tool cache**, **generator**, **cold room** vs **hauling**—each has **capex + opex** (fuel, time, spoilage).
- **Telemetry**: **Fixed** tower/mast **CAPEX** only pays back if **uptime** and **enterprise** need justify it—see backlog [**P3 #24**](implementation-backlog-strategic-audit.md#p3--scale-resilience-tuning-and-economics-depth) (*instrumentation priority matrix*—standalone page pending) and [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md).
- **Enterprise sequencing**: Some enterprises require **proof** of market before **permanent** infrastructure—[`East Tennessee — profitable crops matrix`](east-tennessee-profitable-crops-matrix.md) orients; **UT** PDFs in [`source-notes/ut-publication-w1348-pdf.md`](../source-notes/ut-publication-w1348-pdf.md) etc. provide **worksheet** shapes.

## Phasing table (fill in)

| Year / phase | `SITE_HOMESTEAD` CAPEX (examples) | `SITE_FARM` CAPEX (examples) | Shared / either site | Notes |
|--------------|-----------------------------------|------------------------------|------------------------|-------|
| 0–1 | | | | **Dependency**: e.g. road access, water rights |
| 2–3 | | | | |
| 4–5 | | | | |

## OPEX buckets affected by distance

- **Vehicle**: miles × **trips/year** × **$/mile**; **time** × **labor rate** if opportunity cost matters.
- **Duplication**: two **internet** links, two **monitoring** stacks vs **VPN**—tie to [`Field telemetry reference architecture…`](field-telemetry-reference-architecture-homestead-120ac.md).
- **Spoilage / shrink**: if **cold chain** is wrong-site—link [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md).

## Grounded sources (ingested)

- [`UT Extension — Farm Management Boot 2017 budgets (Velandia)`](../source-notes/ut-extension-fm-boot-2017-budgets-velandia-pdf.md) — training-style budgets.
- Enterprise publication PDFs: [`ut-publication-w1348-pdf`](../source-notes/ut-publication-w1348-pdf.md) (cut flower budgets), sibling **D**-series notes—confirm titles inside PDFs.
- [`Tennessee hobby farm and small-farm business sources`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md) — regulatory **pointers**.

## Related

- [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md)
- [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) — **what** you are spending on.
- [`Own equipment vs custom hire under two-site logistics`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md)
- [`Business viability and farm economics — gap analysis`](business-viability-and-farm-economics-gap-analysis.md)

## Open items

- [ ] Fill phasing table with **real** priorities and **ballpark** CAPEX lines (internal only if sensitive).
- [ ] Attach **accountant**-ready **OPEX** split rule (home office %, mileage)—professional advice.

---

*Foundation document: numeric blanks are intentional.*
