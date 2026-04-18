---
title: Tennessee two-site — official parcel, GIS, flood, and climate portals (primary references)
page_type: source_note
status: active
created: 2026-04-25
updated: 2026-04-25
source_ids: []
tags:
  - tennessee
  - two-site
  - parcel
  - gis
  - flood
  - climate
  - evidence
review_status: unreviewed
confidence: high
---

# Tennessee two-site — official parcel, GIS, flood, and climate portals (primary references)

**Purpose**: **Stable pointers** to **official or primary** web tools used for **desk research** on **`SITE_HOME`** (Anderson County, Claxton) and **`SITE_FARM`** (Campbell County, Demory)—**without** embedding parcel-specific outcomes in the wiki. **Use** with [`Parcel evidence intake and validation workflow — two-site`](../analyses/parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md) and [`Tennessee two-site — evidence hardening audit (2026-04)`](../analyses/evidence-hardening-audit-east-tennessee-two-site-2026-04.md).

**Not provenance for**: Legal boundaries (use **deed**, **survey**, **recorded plat**); utility depths (use **811 locate** + as-builts); soil **management** interpretations (use **local** NRCS + Extension).

## Evidence summary

| Field | Content |
|-------|---------|
| **Abstract** | Primary **URL index** for **desk** research on **Claxton** / **Demory** planning anchors: TN statewide parcel viewer, county assessor entry points, WSS, USGS elevation, FEMA flood maps, NOAA climate normals—**no** parcel outcomes embedded. |
| **Authority mix** | **State** / **county** `.gov` tools + **federal** agencies (NRCS, USGS, FEMA, NOAA)—no third-party aggregators as authorities. |
| **Decision relevance** | **Screening** access, drainage, flood **hazard**, soils **process**, seasonal **norms**—supports parcel worksheets and **V\*/G\*** gates; **does not** replace deed, survey, or local floodplain determination. |
| **Canonical wiki links** | [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md) · [`Parcel intelligence package`](../topics/parcel-intelligence-package-east-tennessee-two-site.md) · [`Parcel evidence intake workflow`](../analyses/parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md) · [`Evidence hardening audit (2026-04)`](../analyses/evidence-hardening-audit-east-tennessee-two-site-2026-04.md) |

**Key claims** (public-safe):

- **TN Property Viewer** and county assessor maps are **not** legal surveys—official disclaimer language applies.
- **FEMA** MSC is for **NFIP** map **desk** screening; **LOMR** / local admin may supersede.

**Open questions / follow-ups**

- **Homestead** WSS AOI capture in `raw/` when filed.
- **Nearest** NOAA station choice vs on-farm **weather** telemetry.

---

## Statewide — property and assessment mapping

| Resource | URL | Role |
|----------|-----|------|
| **TN Property Viewer** (Comptroller / TNGIC) | [tnmap.tn.gov/Assessment/](https://tnmap.tn.gov/Assessment/) | State **map viewer** for **assessment** parcels; search by county, owner, address, parcel ID; **includes** imagery and **FEMA flood** overlay options per viewer documentation. **Disclaimer**: map ≠ legal survey. |
| **TN Comptroller — Property Assessments** | [comptroller.tn.gov/office-functions/pa/](https://comptroller.tn.gov/office-functions/pa/) | Hub for **assessment** programs, **parcel data stewardship**, links to **RE assessment** search tools. |
| **TN Real Estate Assessment Data (parcel search)** | [assessment.cot.tn.gov/RE_Assessment/](https://assessment.cot.tn.gov/RE_Assessment/) | **Searchable** assessment records (coverage per state disclosure—not all functions are statewide uniform). |

---

## County assessor — Anderson (SITE_HOME)

| Resource | URL | Role |
|----------|-----|------|
| **Anderson County Property Assessor — GIS** | [acassessor.com/geographic.html](https://www.acassessor.com/geographic.html) | County **GIS** entry; links **Web App** for parcel visualization. **Disclaimer** on site: mapped data **not** a legal survey—verify with **deed** / **County Clerk**. |
| **Anderson County Property Assessor — search** | [acassessor.com/search.html](https://acassessor.com/search.html) | Property **search** landing. |

---

## County assessor — Campbell (SITE_FARM)

| Resource | URL | Role |
|----------|-----|------|
| **Campbell County — Property Assessor** (official county site) | [campbellcountytn.gov/elected-officials/property-assessor/](https://campbellcountytn.gov/elected-officials/property-assessor/) | **Office** hub: reappraisal cadence, contact, links to **state** search tools for maps/values. |

---

## Soils — national (operating area)

| Resource | URL | Role |
|----------|-----|------|
| **Web Soil Survey (WSS)** | [websoilsurvey.nrcs.usda.gov](https://websoilsurvey.nrcs.usda.gov/) | **NRCS** — define AOI, soil map, **interpretations** for land use. **Process** capture in vault: [`Web Soil Survey — product home page (capture)`](web-soil-survey-home-page-inbox-2026-04-18.md). |
| **SSURGO / gSSURGO** (data products) | [nrcs.usda.gov/wps/portal/nrcs/detail/soils/survey/geo/?cid=nrcs142p2_053627](https://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/survey/geo/?cid=nrcs142p2_053627) | **National** soil survey **data** products—**not** a substitute for WSS workflow on **your** AOI. |

---

## Elevation / topography (United States)

| Resource | URL | Role |
|----------|-----|------|
| **USGS National Map / 3DEP** | [usgs.gov/the-national-map-data-delivery](https://www.usgs.gov/the-national-map-data-delivery) | **Elevation** and **topographic** products; use for **rough** slope/drainage desk context—**field** verify. |
| **USGS TN** | [usgs.gov/centers/tennessee-water-science-center](https://www.usgs.gov/centers/tennessee-water-science-center) | Regional **water** science context; **not** parcel engineering. |

---

## Flood hazard (United States)

| Resource | URL | Role |
|----------|-----|------|
| **FEMA Flood Map Service Center** | [msc.fema.gov/portal/home](https://msc.fema.gov/portal/home) | **Official** **NFIP** **map** search and **FIRMette** exports. **Use** for **regulatory** flood zone **desk** screening—**confirm** with **local** floodplain admin if building or insuring. |
| **FEMA — Flood zones explained** | [fema.gov/flood-insurance/rate-map/flood-zones](https://www.fema.gov/flood-insurance/rate-map/flood-zones) | **Educational** context for **zone** letters—**not** a site determination. |

---

## Climate — normals and historical climate (United States)

| Resource | URL | Role |
|----------|-----|------|
| **NOAA NCEI — U.S. Climate Normals** | [ncei.noaa.gov/products/land-based-station/us-climate-normals](https://www.ncei.noaa.gov/products/land-based-station/us-climate-normals) | **Normals** (temperature, precipitation, etc.) for **station**-based planning—pick **nearest** representative station; **not** microclimate at a fence line. |
| **NOAA — Climate.gov** | [climate.gov](https://www.climate.gov/) | **Portal** for **regional** climate narratives and tools—**supporting** context only. |

---

## Related vault batches

- **Excavation / locate**: TN811 captures in [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md).
- **Fencing / watering / irrigation PDFs**: same batch (UT Extension **PB1541**, **PB1641**; NRCS **NEH Part 652**, CPS **614** hub page).
- **Authoritative index**: [`Authoritative execution evidence cluster — East Tennessee`](authoritative-execution-evidence-cluster-east-tennessee.md).
