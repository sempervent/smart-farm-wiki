---
title: Claxton and Demory — missing data register
page_type: analysis
status: active
created: 2026-04-22
updated: 2026-04-22
tags:
  - two-site
  - anderson-county
  - campbell-county
  - validation
  - epistemics
review_status: unreviewed
confidence: high
aliases:
  - Missing data register Claxton Demory
---

# Claxton and Demory — missing data register

**Purpose**: List what **cannot** be known confidently from **current processed files** in this vault for **`SITE_HOME`** (**Claxton**, Anderson County) and **`SITE_FARM`** (**Demory**, Campbell County), and what **must** be gathered next. This is a **gap register**, not a substitute for deeds, surveys, or county offices.

**Epistemic stance**: **County-level** NASS tables and **one** Campbell **Web Soil Survey** session ([`Demory site intelligence`](demory-farm-site-intelligence.md)) **improve** context; they **do not** replace **parcel** truth. **Uncertainty is explicit** until evidence is filed.

**Anchors**: [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) · [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md) · [`Parcel evidence intake and validation workflow`](parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md) · [`Claxton home base — site intelligence`](claxton-home-base-site-intelligence.md) · [`Demory farm — site intelligence`](demory-farm-site-intelligence.md) · [`Validation and pilot plan — first 24 months`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) · [`Validation backlog and decision gates`](east-tennessee-two-site-farm-business-plan-validation-backlog.md).

**Legend — site**: **C** = Claxton / Anderson · **D** = Demory / Campbell · **Both** = both sites.

---

## 1. Parcel-specific land intelligence still missing

| Gap | Site | Why it matters | Resolve by | Blocks / informs |
|-----|------|----------------|------------|------------------|
| **Legal boundary + acreage** tied to operating map | Both | CAPEX, taxes, insurance, and **V8** use/structures depend on **deed** vs **mental map** | Deed, plat, survey if disputed; single **operating** polygon in GIS/sketch | **V8**; fence/water **eligibility**; **G1** |
| **WSS AOI clipped to ~5 ac / ~120 ac** operating footprints | **C** (homestead AOI none in corpus) | Map units for **homestead** garden/buildings unknown | Draw **WSS** AOI on **Claxton** footprint; export report | **V1**; homestead **build** siting |
| **WSS AOI aligned to management acres** (not 558.6 ac session blob) | **D** | Vault capture is **558.6 ac** ≠ **~120 ac** plan label—soil % by **field** wrong until clipped | Redraw AOI to **deed** or **operating** boundary; re-run **Soil Map** | **V1**, **V4**; **spatial model** [`MAP_AUTHORITY`](../analyses/farm-spatial-model-and-asset-registry-standard.md) |
| **Easements / ingress / shared lane** | Both | **Batching** and **emergency** access assumptions | Title search; neighbor letters; **drive** log | **Trip policy**; **R13** security; **V8** |

---

## 2. Buildability / septic / utilities data still missing

| Gap | Site | Why it matters | Resolve by | Blocks / informs |
|-----|------|----------------|------------|------------------|
| **OSSS / septic class + setbacks** | **C** (primary residence/shop) | Homestead **expand** (shop, ADU) and **health** | County environmental health; perc/morph if required | **Phase 0–1** homestead CAPEX; **capital plan** sequencing |
| **Septic / SSDS for ag structures** (if any) | **D** | **Employee** facilities, **cooler**, **wash**—if on path | Same + **TDEC** / county rules ([`septic captures`](../source-notes/tn-onsite-sewage-septic-captures-inbox-2026-04-18.md)) | **V8** structures path; **Phase 2+** |
| **Electric service size, transformer, single- vs three-phase** | Both | **Pump**, **cold**, **broker**, **homelab** loads | Utility **will-serve** / **meter** data | **Capital plan**; **smart-tech** **broker** placement ([`smart-tech strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)) |
| **ISP / fiber / LTE** at **address** and at **field pins** | **C** primary; **D** for telemetry | **Telemetry** and **office** work **truth** | ISP maps; **V10** drive tests at **tanks/gates** | **V10**; **G8** path; **instrumentation** priority |
| **Domestic vs ag power accounting** (if split meters) | Both | **Books** and **margin** truth | Utility account structure | **Revenue model**; **Schedule F** hygiene (not tax advice) |

---

## 3. Soil / slope / hydrology questions still unresolved

| Gap | Site | Why it matters | Resolve by | Blocks / informs |
|-----|------|----------------|------------|------------------|
| **Map unit + limiting factors on each field polygon** | **D** (partial WSS); **C** unknown | **Rotation**, **lime**, **wet** no-go | **Clip** WSS; **walk** with map; optional **soil test** grid | **V1**, **V4**; **enterprise strategy** row-crop vs grazing |
| **Hydric / ponding / seasonally wet** areas | **D** | **Fence**, **lanes**, **winter** traffic | Field observation + **wet** year photos | **V2** water routing; **R14** erosion |
| **Riparian / stream buffers / TDEC** | **D** (streams in WSS imagery) | **Crossings**, **waste stacking**, **civil** liability | **TDEC** / county **field** visit | **V2**; **risk register** R10/R14 |
| **Karst / sink / cave risk** | Both (ET variable) | **Structure** and **waste** siting | Local **cave** maps; walk | **V8**; **buildability** |

---

## 4. Access / road / drainage / erosion unknowns

| Gap | Site | Why it matters | Resolve by | Blocks / informs |
|-----|------|----------------|------------|------------------|
| **Private road maintenance + liability** | Both | **Who** plows, **who** pays **grading** | Easement docs; neighbor agreement | **OPEX**; **trip** reliability (**Q2** [`two-site ops`](two-site-operations-model-5ac-homebase-120ac-production.md)) |
| **Grade, crown, culverts, rolling dips** on **primary** haul route | **D** (steep AOI); **C** driveway | **Mud/ice** → **batching** failure | **Bad-weather** drive log; **photos** | **Validation** access row; **R14** |
| **Internal farm lanes** — base, width, sediment | **D** | **Hay**, **stock**, **equipment** **cost** | Engineer sketch or **NRCS**; **rain** **event** notes | **Capital plan** earthwork line; **G1** |
| **Gate locations + winter icing** | **D** | **Labor** and **animal** **welfare** | Tagged **walk**; **V3** segments | **Trip policy**; **labor** surge |

---

## 5. Market / rent / county-economic unknowns

| Gap | Site | Why it matters | Resolve by | Blocks / informs |
|-----|------|----------------|------------|------------------|
| **Your** pasture/hay/lease **rate** vs **NASS 2024** county **cropland** row | **D** | NASS is **survey estimate**, **not** pasture lease; **Anderson $28.50** vs **Campbell $27.50** is **ballpark** only | **Signed** comps; **broker** conversations; **auction** **notes** | **V7**; **fallback** thesis ([`recommended enterprise strategy`](east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md)) |
| **Processing slots + haul shrink** to **your** chosen outlets | **D** | **V6** **all-in** **per** **head** | Processor **calls**; **mileage** **log** | **V6**; **G1** **margin** |
| **Property tax + ag classification** outcomes | Both | **Cash** **plan** | County assessor; **DOR** **ag** **rules** ([`ag exemption`](../source-notes/tn-revenue-agricultural-exemption-jan2023-pdf.md) context) | **Revenue** **milestones**; **entity** choice (professional) |

---

## 6. Infrastructure reconnaissance still required

| Gap | Site | Why it matters | Resolve by | Blocks / informs |
|-----|------|----------------|------------|------------------|
| **Well reports / pump tests / seasonal flow** | **D** | **V2** **herd** **ceiling** | **Pump** test; **log** **drawdown** | **V2**, **V4**; **water** **CAPEX** |
| **Fence segment condition by length** | **D** | **V3** repair tiers | Tagged photos + rough feet | **V3**; fence order |
| **Handling MVP (corral, load-out) as-built** | **D** | **V6** marketing / welfare | Walk + measure | Phase 2 timing |
| **Cold chain / power** at **processing** **adjacent** **loads** | **D** | **Shrink** **and** **regulatory** **risk** | **Trial** **haul**; **thermometer** **log** | **Revenue** **model** **processing** **row** |

---

## 7. What can be learned from desktop sources

| Source type | What it can answer (still approximate) | Cannot replace |
|-------------|----------------------------------------|----------------|
| **Web Soil Survey** (new AOI per site) | Map units, slopes, **broad** **limitation** classes on **drawn** polygon | **Perc**, **wet** spots under trees, **illegal** **fill** history |
| **FEMA NFHL / local flood layers** | **Zone** **hints** for **insurance** **and** **build** **setbacks** | **Field** **flood** **behavior** in **convective** **events** |
| **USGS / 3DEP** | **Drainage** **context**, **slope** **distribution** | **Pipe** **sizes**, **legal** **drainage** **rights** |
| **NASS Quick Stats / county rent PDFs** | **County** **economic** **ballpark** | **Your** **lease**; **pasture** **specifics** **when** **NASS** **`--`** |
| **FSA / NRCS** **public** **pages** | **Program** **eligibility** **surface** | **Signed** **contracts**, **EQIP** **approval** |

---

## 8. What requires on-site inspection, survey, or county-office interaction

| Class | Examples | Typical owner |
|-------|----------|----------------|
| **County office** | Zoning **V8**, **septic** **permits**, **assessor** **classification** | Environmental health, planning, property assessor |
| **Licensed survey / PE** | **Boundary** **disputes**, **structural** **pads** **on** **steep** **ground** | Surveyor, **geotech** **when** **warranted** |
| **Field inspection** | **Fence** **walk**, **wet** **year** **lanes**, **tank** **levels**, **predator** **pressure** | **Family** + **optional** **consult** |
| **Utility** **truck** **roll** | **Transformer** **location**, **line** **extension** **quotes** | Power **co-op** / **utility** |
| **Professional services** | **Title**, **entity**, **tax** **elections** | Attorney, **CPA** |

---

## Related

- [`Anderson County vs Campbell County — operating implications`](../comparisons/anderson-county-vs-campbell-county-operating-implications.md) — **over-generalization** risks
- [`Execution readiness gap audit`](execution-readiness-gap-audit-east-tennessee-operational-knowledge.md) — **execution-grade** **evidence** **themes**
- [`Pilot and recon checklists`](../analyses/pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md) — **copy-paste** **rows**

---

*This register should shrink as evidence lands in `raw/processed/` + source-notes; log significant closes in [`log.md`](../log.md) under **lint** or **ingest**.*
