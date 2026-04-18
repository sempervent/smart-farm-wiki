---
title: Demory farm — site intelligence (Campbell County, Tennessee)
page_type: analysis
status: active
created: 2026-04-22
updated: 2026-04-24
tags:
  - two-site
  - site-farm
  - campbell-county
  - demory
  - east-tennessee
review_status: unreviewed
confidence: medium
aliases:
  - SITE_FARM Demory site intelligence
---

# Demory farm — site intelligence (Campbell County, Tennessee)

**Planning anchor**: **Production farm / `SITE_FARM`** at **Demory**, **Campbell County**, Tennessee (place name as **planning label**—**not** a legal property abstract).

**Role entity** (`SITE_FARM`): [`120-acre production farm (SITE_FARM) — ET two-site`](../entities/120-acre-production-farm-site-farm-et-two-site.md). **Place entity**: [`Demory farm site (place)`](../entities/demory-farm-site.md). **County context**: [`Campbell County, Tennessee (two-site context)`](../entities/campbell-county-tennessee.md). **Package**: [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md).

**Epistemic rule**: **County** rent and **WSS AOI** statistics below are **evidence**, not proof that **every** acre matches the **~120 ac** planning figure or your deed. **Confirm** AOI ↔ operating boundary.

---

## Known (from processed / authoritative sources)

### County cash rent (2024 NASS)

| Practice (2024 county estimate) | Value | Notes |
|---------------------------------|-------|--------|
| **Non-irrigated cropland** | **$27.50 / acre** | Row in TN table: Campbell |
| **Irrigated cropland** | `--` (not published) |  |
| **Pastureland** | `--` (not published) |  |

**Source**: USDA NASS *Cash Rents County Estimates – 2024* (TN); [`nass-cash-rents-all-crops-tn-2024.pdf`](../../raw/processed/2026/nass-cash-rents-all-crops-tn-2024.pdf); [`*-extracted.md`](../../raw/processed/2026/nass-cash-rents-all-crops-tn-2024-extracted.md); aligned with [`NASS cash rents TN 2024`](../source-notes/nass-cash-rents-tn-2024-surveys-pdf.md). Figures are **survey estimates**, not your lease payment.

### Web Soil Survey — soil map tab (processed capture)

**Raw**: [`web-soil-survey-campbell-county-aoi-soil-map-tab-capture-2026-04-18.md`](../../raw/processed/2026/web-soil-survey-campbell-county-aoi-soil-map-tab-capture-2026-04-18.md). **Source-note**: [`Campbell County — WSS AOI soil map tab (capture)`](../source-notes/campbell-county-wss-aoi-soil-map-tab-capture-2026-04-18.md).

| Item | Value (this WSS session) |
|------|---------------------------|
| **Reported AOI total** | **558.6 ac** |
| **Largest map units (by acres in AOI)** | **FbF** Fullerton and Bodine gravelly silt loams, **25–70% slopes** — **~55%** of AOI; **FbD** 12–25% slopes — **~31%**; **TaF** Talbott–Rock outcrop complex 30–50% slopes — **~10%** |
| **Session warning** | Soil map **may not be valid** at displayed zoom; mapping scale **1:24,000** |

**Interpretation (cautious)**: The AOI is **strongly sloped** and **gravelly** in aggregate—consistent with **road/drainage/fence-on-contour** and **limited row-crop** thinking unless smaller **pockets** of better land exist **inside** the AOI (WSS “small areas of contrasting soils” caveat).

---

## Likely but still assumptions

| Topic | Assumption | Risk |
|-------|------------|------|
| **AOI = operating farm** | Capture reflects **production** land tied to Demory planning. | AOI **558.6 ac** ≠ **~120 ac** scenario label—could include **multiple** tracts or buffer; **re-draw** WSS AOI to match **management** boundary. |
| **Grazing / forage** | Sloped **pasture/hay** systems **fit** regional Extension patterns when **water + fence** are right. | **Endophyte**, drought, and **winter hay** demand can **outrun** generic “grazing-led” optimism—use UT/NRCS sources in [`Authoritative execution evidence cluster`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md). |
| **Water** | **Streams** layer appears in capture imagery—**riparian** and **TDEC** rules may constrain crossings and **waste stacking**. | **Field** + **regulatory** verification required. |

---

## Unknown (parcel-specific verification)

| Item | Action |
|------|--------|
| **Which acres are **farm** vs woodland vs building envelope** | Sketch + deed + walk; align to **paddock IDs** in [`Farm spatial model`](../analyses/farm-spatial-model-and-asset-registry-standard.md). |
| **Operational septic / well / ag structures** | County permits; **not** inferred from WSS. |
| **EQIP / NRCS practice eligibility** | **Site** visit and **CP** process—[`NRCS`](../source-notes/nrcs-ceap-e472a-e528r-fy2025-pdf.md) materials are **program** context only. |
| **Precise slope class distribution **on** the ~120 ac** | If AOI is larger, **clip** soils to **your** field polygons. |

---

## Implications (two-site plan)

| Domain | Implication |
|--------|-------------|
| **Buildability** | **Steep, gravelly** map units favor **smaller building pads**, **cut/fill discipline**, and **sediment control**—align with [`Rural road and driveway erosion`](../topics/rural-road-and-driveway-erosion-sources.md) and **NRCS** engineering when scaling **lanes** and **pads**. |
| **Access** | **Internal roads** and **gates** are **high-leverage** CAPEX; **mud/ice** and **grade** affect **batching** and **trailer** class (see [`Two-site ops model`](../analyses/two-site-operations-model-5ac-homebase-120ac-production.md)). |
| **Soils / productivity** | Expect **variable** crop suitability; **hay/pasture** economics tie to **slope**, **fertility**, and **lime/fertilizer** reality—not **county average** rent alone. |
| **Water / hydrology** | **Stock water**, **crossings**, and **ponding** are **design** problems on sloped ground; **telemetry** for tanks and **remote** observation pays off **here** first. |
| **Utilities / site work** | **Power drop** location, **three-phase** availability, and **solar** siting are **site** decisions; may be **weaker** retail service than Anderson **home base**—**verify**. |
| **Labor / travel** | **Heavy** on-site hours; **justify** trips from Claxton with **batching**; **avoid** **daily-touch** enterprises that ignore **distance tax**. |
| **Automation / telemetry** | **Gateway / backhaul** placement and **power** at **ridge or barn** points; **LoRa/Meshtastic** range and **vegetation** tied to **terrain**. |
| **Business-plan sequencing** | **Phase 1**: **land intelligence** (soils, water, fence **plan**, **handling** MVP) before **herd scale**; **Phase 2** margin tied to **real** operating cadence—see [`Recommended enterprise strategy`](../analyses/east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md). |
| **Off-grid-first** **power** **+** **field** **network** | **Planning** **default** **:** **solar** **+** **battery** **;** **local** **mesh** **/** **LPWAN** **before** **WAN** **dependency** **—** **see** **canonical** **hub** **below** **.** |

---

## Off-grid-first power and connectivity (canonical)

When **`SITE_FARM`** **is** **modeled** **as** **off-grid-first** **(**solar** **+** **battery** **default** **;** **WAN** **optional** **)** **,** **use** **these** **pages** **(**not** **standalone** **essays** **)** **:**

| Page | Role |
|------|------|
| [`Off-grid power strategy — Demory farm site`](off-grid-power-strategy-demory-farm-site.md) | **Continuous** **vs** **duty-cycled** **loads** **;** **networking** **as** **electrical** **load** **.** |
| [`Mesh and field networking strategy — off-grid Demory farm`](mesh-and-field-networking-strategy-off-grid-demory-farm.md) | **Meshtastic** **/** **HaLow** **/** **Wi‑Fi** **roles** **;** **what** **must** **work** **without** **WAN** **.** |
| [`Off-grid degraded modes — power and connectivity`](off-grid-degraded-modes-power-and-connectivity-demory-farm.md) | **SOC** **+** **WAN** **failure** **classes** **.** |
| [`Off-grid operational decision rules — power and networking`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md) | **DR-*** **gates** **.** |
| [`Off-grid farm execution topology — Demory (Mermaid)`](off-grid-farm-execution-topology-demory-mermaid.md) | **Reference** **/** **pilot** **/** **degraded** **diagrams** **.** |
| [`Meshtastic vs Wi‑Fi HaLow vs conventional Wi‑Fi — off-grid farm operations`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md) | **Operational** **comparison** **.** |
| [`Off-grid power, field RF, and optional WAN — source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) | **Raw** **/** **PDF** **provenance** **.** |

---

## Related

- [`Parcel intelligence — Demory farm site`](parcel-intelligence-demory-farm-site-east-tennessee-two-site.md) — structured **parcel worksheet** (vault WSS table + pending clip to ~120 ac)
- [`Claxton and Demory — missing data register`](claxton-and-demory-missing-data-register.md) — **Parcel** gaps not yet filled from vault sources
- [`Claxton home base — site intelligence (Anderson County)`](claxton-home-base-site-intelligence.md)
- [`Anderson County vs Campbell County — operating implications`](../comparisons/anderson-county-vs-campbell-county-operating-implications.md)
- [`Farm parcels and land units`](../entities/farm-parcels-and-land-units.md)
