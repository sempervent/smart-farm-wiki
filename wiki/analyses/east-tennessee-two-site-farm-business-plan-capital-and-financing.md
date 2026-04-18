---
title: Capital plan and infrastructure sequencing
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - business-plan
  - finance
  - capex
confidence: medium
aliases:
  - East Tennessee two-site farm business plan — capital plan and phased infrastructure roadmap
---

# Capital plan and infrastructure sequencing

## Purpose

Sequence **capital** (and selective **financing**) for a **grazing-led**, **two-site** farm business: **infrastructure that unlocks production** on the **120-acre** parcel first; **homestead “brain”** spend in **small**, **justified** steps. This page stays **valid** while **exact dollars** and **lender terms** are unknown—it defines **order**, **gates**, and **what not to debt-fund**.

**Two-site economics (concept)**: [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md).  
**Fillable year table**: [`Capital phasing table — years 0 to 10`](capital-phasing-table-years-0-10-two-site-smart-farm.md).  
**Hub**: [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md).

## Decisions supported by this page

| Decision | This page provides |
|----------|-------------------|
| **Fence vs water vs telemetry** order | Sequencing table |
| **What** may be **financed** vs **cash-only** | Phase posture + checklist |
| **Debt service** vs **margin** evidence | Tie to Phase 2+ proof |
| **Homestead vs 120** CAPEX split | Principle: durable production vs **control center** |

## Capital principles

1. No **irreversible** fence or **major** dirt work before **Phase 1** land intelligence—except **no-regret** fixes (legal access, acute erosion, **acute** water failure).
2. Finance **durable** infrastructure **selectively** (fence, water development, power drops)—not **consumables** or **gadgets**.
3. **Homestead** compute/network CAPEX in **increments** with **homelab discipline** (backups, patch cadence).
4. Match **debt service** to **Phase 2+ margin evidence**, not optimism.

## Infrastructure sequencing (grazing-led)

| # | Item | Unlocks |
|---|------|---------|
| 1 | Legal boundary, **access**, use clarity | Everything else |
| 2 | Water development + distribution | Stocking density, welfare |
| 3 | Perimeter + interior fence **plan** | Rotation |
| 4 | Handling **MVP** (sort, load, vet) | Marketing, welfare |
| 5 | Truck/trailer class adequate for **chosen** exit | Revenue realization |
| 6 | Telemetry **backbone** after **manual** proof | Trip reduction with accountability |

**County-specific sequencing (Campbell `SITE_FARM` — Demory)** — Vault **WSS** capture shows **steep**, **gravelly** map units over much of a large AOI ([`Demory site intelligence`](demory-farm-site-intelligence.md)): treat **internal lanes**, **drainage**, **gate pads**, and **sediment control** as **Phase 1–2 peers** with fence/water—**not** “later prettification.” **Anderson `SITE_HOME` — Claxton**: prioritize **OSSS/power/ISP truth** before scaling **homelab/broker** CAPEX ([`Claxton site intelligence`](claxton-home-base-site-intelligence.md)); **parcel** verification still required.

**What changed**: Local **terrain** evidence **raises** earthwork/lane priority on the **production** county; it does **not** authorize **fence herd scale** without **G1** gates.

## Phased capital posture

| Phase | Typical infrastructure | CAPEX posture | Financing caution |
|-------|------------------------|---------------|---------------------|
| 0 | Maps, docs, basic tools, comms | **Minimal** | No term debt for **toys** |
| 1 | Soil/water tests, fence patches, **pilot** sensor | **Low**; grants/EQIP **if** eligible (not assumed) | Match loans to **validated** lease or **off-farm** income |
| 2 | Water **plan executed**, fence **as designed**, corral MVP, herd or stock purchase | **Moderate**; livestock as inventory where appropriate | Cattle **price** risk—size to **liquidity** |
| 3 | Scale rotation; optional hay **hire** or **gear**; marketing build | Selective finance on **depreciable** with **margin** | Equipment trap—**hire** until hours/year clear |
| 4 | Cold chain, direct sales assets, redundant comms | Tied to **salary-replacement** proof | Don’t borrow for **image** |

## OPEX buckets (for budgeting)

| Bucket | Examples |
|--------|----------|
| Land + lease | Cash rent in/out; property taxes |
| Livestock + feed | Purchase, mineral, vet |
| Equipment | Fuel, maintenance, repairs |
| Labor | Hired help (if any) |
| Tech | ISP, cell, cloud, spares; **LEO satellite (e.g. Starlink) service + spares** **when** **that** **is** **the** **WAN** |
| Insurance | Farm, liability, equipment |

**Starlink / farm WAN (sequencing discipline)**: **Defer** a **second** terminal or **redundant** **farm** **uplink** **until** **Phase 1** **comms** **proof**—see [`Two-site operations model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md) **WAN** table and [`Smart technology and telemetry strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md). **Do not** **debt-fund** **gadget** **radios** before **fence/water** gates in this plan’s phasing.

**What changed because of Starlink analysis**: Vault **spec PDFs** define **hardware classes** (**Mini** vs **Standard / kit**)—**OPEX** should **name** **subscription + spare cable/router**, not hide WAN under generic “tech.”

<h3 id="off-grid-demory-capital-sequencing">Off-grid SITE_FARM (Demory) — sequencing discipline</h3>

**Planning default** for the production parcel is **solar + battery** and **mesh-first / local survivable** telemetry—not grid-tied assumptions. That changes **what** gets funded **before** remote operations are trustworthy:

| Order | Fund first | Defer / shed |
|-------|------------|----------------|
| **A** | **Water + fence + handling** truth (same grazing-led spine as §Infrastructure sequencing) | “Smart” layers that do not reduce blind spots |
| **B** | **DC power domain** for **Pcrit**: inverter/charge control, **battery** protection, **labeled** **loads** for gateway and pump heads (per [`Off-grid power strategy — Demory farm site`](off-grid-power-strategy-demory-farm-site.md)) | Second **farm** **WAN** terminal, **HaLow** backhaul, **fleet** mesh nodes |
| **C** | **One** field **gateway** + **one** RF class (e.g. Meshtastic **or** one Wi‑Fi segment)—prove **local** path **without** **WAN** | Parallel stacks, always-on IP radios everywhere |
| **D** | **Metering or bracket** for **network + always-on electronics** as **Wh/day** against **battery days** (placeholder until measured)—[`Off-grid operational decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md) **DR-1** | New **always-on** **IP** **mesh** / **CPE** **until** **DR-1** **satisfied** |

**Labor / OPEX**: Off-grid sites add **electrical O&M** (terminals, corrosion, **battery** **cycles**, **genset** policy if any) on top of **RF** **field** **maintenance** already in [`Smart technology strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)—book as **tech + infra** time, not only subscription lines.

**Starlink at the farm** remains **optional backhaul**—sequence **after** B–C are **credible**, not as a substitute for **local** **gateway** **+** **power** **story** ([`Connectivity strategy — Claxton & Demory`](connectivity-strategy-for-claxton-and-demory.md)).

## Financing checklist (local thresholds)

- [ ] Debt service \< **X%** of trailing **gross farm revenue** (set **X**).
- [ ] Personal guarantee only with **written** worst-case exit.
- [ ] Operating line **not** used to buy **long-lived** assets.
- [ ] Equipment purchase **delayed** until **custom hire** quote compared honestly.

## Known facts

| ID | Statement |
|----|-----------|
| K1 | The plan constrains **minimal early spend**, **moderate phased** investment, **selective** infrastructure financing. |
| K2 | **Primary production CAPEX** targets the **120-acre** parcel; **control center** spend targets **home** ([`Two-site operating model`](two-site-operations-model-5ac-homebase-120ac-production.md)). |

## Assumptions

| ID | Statement |
|----|-----------|
| A1 | **Off-farm wages** subsidize the first **1–2** years of ramp. |
| A2 | **Used equipment** market exists for **some** categories in-region. |

## Open questions

| ID | Question |
|----|----------|
| Q1 | **FSA** / lender relationship and **programs**? |
| Q2 | **Internal hourly charge** for family labor in **books** (for margin truth)? |
| Q3 | **Insurance** requirements for **financed** equipment? |
| Q4 | **Working capital** line: size and **allowed uses**? |

## Iterative updates

- Copy **phasing dollars** into [`Capital phasing table — years 0 to 10`](capital-phasing-table-years-0-10-two-site-smart-farm.md) when quotes exist.
- Add **actual** debt covenants when signed.

## Authoritative program references (FSA / USDA — not application advice)

**Wiki role**: Point to **official** program descriptions and **beginning-farmer** entry pages so **Q1** above is answered with **primary** material, not forum lore.

| Material | Source-note |
|----------|-------------|
| FSA loan and state program **pages** (captures) | [`USDA FSA — program pages (captures)`](../source-notes/fsa-program-pages-capture-inbox-2026-04-18.md) |
| Beginning farmer **resource list** (TN + USDA links) | [`Beginning farmer resources (TN + USDA)`](../source-notes/beginning-farmer-resources-list.md) |
| farmers.gov beginning farmers hub | [`Beginning farmers and ranchers (USDA farmers.gov)`](../source-notes/beginning-farmers-and-ranchers-usda-farmers-gov.md) |

**Eligibility, deadlines, and forms** change—confirm with **your** FSA office. **Evidence cluster**: [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md).

## Related pages

- [`East Tennessee two-site farm business plan — revenue model and business milestones`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md)
- [`East Tennessee two-site farm business plan — risk register and mitigation strategy`](east-tennessee-two-site-farm-business-plan-risk-register.md)
- [`Recommended enterprise strategy — phased East Tennessee path`](east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md)
