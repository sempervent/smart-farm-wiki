---
title: Parcel intelligence — Demory farm site (East Tennessee two-site)
page_type: analysis
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - two-site
  - parcel-intelligence
  - site-farm
  - campbell-county
  - demory
source_ids:
  - raw/processed/2026/web-soil-survey-campbell-county-aoi-soil-map-tab-capture-2026-04-18.md
source_count: 1
confidence: medium
review_status: unreviewed
---

# Parcel intelligence — Demory farm site (East Tennessee two-site)

**Purpose**: **Parcel worksheet** for **`SITE_FARM`** at **Demory**, Campbell County, Tennessee. **Soils evidence**: one **Web Soil Survey** Soil Map tab session is in the vault—**AOI 558.6 ac** in that session **≠** the **~120 ac** planning label until you **clip** and re-run on the **operating** polygon.

**Anchors**: [`Demory farm site (place)`](../entities/demory-farm-site.md) · [`120-acre production farm (SITE_FARM)`](../entities/120-acre-production-farm-site-farm-et-two-site.md) · [`Demory farm — site intelligence`](demory-farm-site-intelligence.md). **Package**: [`Parcel intelligence package — East Tennessee two-site`](../topics/parcel-intelligence-package-east-tennessee-two-site.md).

**Authoritative capture (raw)**: [`web-soil-survey-campbell-county-aoi-soil-map-tab-capture-2026-04-18.md`](../../raw/processed/2026/web-soil-survey-campbell-county-aoi-soil-map-tab-capture-2026-04-18.md). **Source-note**: [`Campbell County — WSS AOI soil map tab (capture)`](../source-notes/campbell-county-wss-aoi-soil-map-tab-capture-2026-04-18.md).

---

## Location role

| Field | Value / status |
|-------|----------------|
| **Named anchor** | Demory (planning label), Campbell County, TN |
| **County / state** | Campbell County, Tennessee (FIPS **TN013** in WSS session) |
| **Planning role** | `SITE_FARM` — primary production surface (~**120 ac** scenario label) |

---

## Acreage and site function

| Field | Value / status |
|-------|----------------|
| **Planning acreage (scenario label)** | ~**120 ac** (not a deed abstract) |
| **Deed / survey acreage** | — *pending evidence in `raw/` + source-note* |
| **WSS AOI (this vault session)** | **558.6 ac** total in capture — **must not** be read as “120 ac soil mix” without **clipping** |
| **Primary functions** | Livestock/forage/crops, field telemetry, on-site labor (see site intelligence) |

---

## Soils

**Evidence type**: Web Soil Survey — **Soil Map** tab (HTML capture), session dated **2026-04-18** in filename.

**Vault summary (session AOI — not clipped to ~120 ac)**

Values below are **only** what appears in the **Soil Map** summary table in the raw capture; **percent of AOI** is **for this 558.6 ac session**, not for a deed.

| Map unit symbol | Map unit name (WSS) | Acres in AOI | % of AOI |
|-----------------|----------------------|-------------:|----------|
| CaC | Claiborne silt loam, 5 to 12 percent slopes | 5.2 | 0.9% |
| CaD | Claiborne silt loam, 12 to 25 percent slopes | 0.6 | 0.1% |
| CaE | Claiborne silt loam, 25 to 45 percent slopes | 10.2 | 1.8% |
| FbD | Fullerton and Bodine gravelly silt loams, 12 to 25 percent slopes | 174.4 | 31.2% |
| FbF | Fullerton and Bodine gravelly silt loams, 25 to 70 percent slopes | 309.3 | 55.4% |
| MaD | Minvale gravelly loam, 15 to 25 percent slopes | 3.4 | 0.6% |
| TaF | Talbott-Rock outcrop complex, 30 to 50 percent slopes | 55.5 | 9.9% |
| **Total** | *Totals for Area of Interest (WSS)* | **558.6** | **100%** |

**Session warnings (in raw)**: Soil Map **may not be valid** at displayed zoom; mapping scale **1:24,000**; enlargement beyond mapping scale can **misrepresent** line placement and **small contrasting inclusions**.

| Field | Value / status |
|-------|----------------|
| **Map units clipped to ~120 ac operating polygon** | — *pending redraw WSS AOI + new capture* |
| **Hydric / limiting factors** | — *use Soil Data Explorer / field eval per map unit; not filled here* |

---

## Slope

**From map unit names in this session** (aggregate story only): dominant classes include **12–25%**, **25–70%**, and **30–50%** complexes—see table above. **Field / clipped** distribution — *pending*.

| Field | Value / status |
|-------|----------------|
| **Terrain summary** | Steep/gravelly **dominant** in this AOI aggregate (see site intelligence) |
| **Steep-area % on ~120 ac** | — *pending AOI clip* |

---

## Hydrology

| Field | Value / status |
|-------|----------------|
| **Streams / ponds / wetlands (desktop)** | Streams layer appears in session imagery — **riparian / TDEC** rules — *field + regulatory verify* |
| **Floodplain / karst flags** | — *pending* |
| **Stock water / crossings** | — *design problem on sloped ground; see site intelligence* |

---

## Access

| Field | Value / status |
|-------|----------------|
| **Public road frontage / easements** | — *pending title / field* |
| **Internal lanes / gates / surface** | — *pending; high CAPEX on steep ground (site intelligence)* |

---

## Utilities

| Field | Value / status |
|-------|----------------|
| **Electric service** | — *pending utility* |
| **Broadband** | — *pending* |
| **Water (well / district / ag use)** | — *pending* |
| **Onsite sewage** | — *production structures — county program context only until permits filed* |

---

## Structures

| Field | Value / status |
|-------|----------------|
| **Existing ag / residential structures** | — *pending* |
| **Planned pads** | — *earthwork/sediment discipline per slope evidence* |

---

## Constraints

| Constraint | Evidence / note |
|------------|-----------------|
| Terrain / soils | **FbF / FbD / TaF** dominance in session AOI → fence, road, pad, and sediment constraints |
| Regulatory | **TDEC** / crossings / waste stacking — *not inferred from WSS alone* |
| AOI vs deed | **558.6 ac** session may include land outside **~120 ac** operating plan |

---

## Opportunities

| Opportunity | Depends on |
|-------------|------------|
| Grazing-led systems with **water + fence** right | Clip soils to **paddock** polygons; field soil tests |
| Telemetry ROI | Tank/gateway points where power and backhaul exist |

---

## Telemetry placement candidates

| Candidate | Power / backhaul | Notes |
|-----------|------------------|-------|
| Ridge / high points | — *candidate only* | LoRa/Meshtastic line-of-sight — *verify* |
| Barn / tank / pump | — *pending* | Observe-first automation (see smart-tech strategy) |

---

## Validation tasks

| Task ID / ref | Description | Status |
|---------------|-------------|--------|
| **V1** | Soils/slope: **clip** WSS to **operating** polygon — [`Validation plan`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) | Open until new AOI |
| Gap register | [`Claxton and Demory — missing data register`](claxton-and-demory-missing-data-register.md) — AOI vs **~120 ac** | Open |

---

## Unresolved questions

1. Which **sub-areas** of the session AOI are in the **~120 ac** operating footprint?
2. Deed lines vs WSS AOI boundary used for this capture?
3. Per-field soil tests and carrying capacity — *not in vault*.

---

## Related

- [`Claxton and Demory — missing data register`](claxton-and-demory-missing-data-register.md)
