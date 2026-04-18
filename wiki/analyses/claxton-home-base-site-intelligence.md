---
title: Claxton home base — site intelligence (Anderson County, Tennessee)
page_type: analysis
status: active
created: 2026-04-22
updated: 2026-04-23
tags:
  - two-site
  - site-home
  - anderson-county
  - claxton
  - east-tennessee
review_status: unreviewed
confidence: medium
aliases:
  - SITE_HOME Claxton site intelligence
---

# Claxton home base — site intelligence (Anderson County, Tennessee)

**Planning anchor**: **Homestead / `SITE_HOME`** in **Claxton**, **Anderson County**, Tennessee (unincorporated community; **not** a deed abstract).

**Role entity** (`SITE_HOME`): [`Five-acre home base (SITE_HOME) — ET two-site`](../entities/five-acre-home-base-site-home-et-two-site.md). **Place entity**: [`Claxton home base (place)`](../entities/claxton-home-base.md). **County context**: [`Anderson County, Tennessee (two-site context)`](../entities/anderson-county-tennessee.md). **Package**: [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md).

**Epistemic rule**: This page **synthesizes county-level and vault sources**. **Parcel-specific** soils, septic, and utilities require **your** WSS AOI, permits, and utility lookups—not defaults here.

---

## Known (from processed / authoritative sources)

| Topic | What we can say | Source |
|-------|-----------------|--------|
| **Cash rent — county** (2024 survey) | **Non-irrigated cropland** cash rent **$28.50/acre** (county estimate). **Irrigated cropland** and **pastureland** shown as **not published** (`--`) for Anderson in this table row. | USDA NASS *Cash Rents County Estimates – 2024* (TN); see [`nass-cash-rents-all-crops-tn-2024.pdf`](../../raw/processed/2026/nass-cash-rents-all-crops-tn-2024.pdf), [`*-extracted.md`](../../raw/processed/2026/nass-cash-rents-all-crops-tn-2024-extracted.md); values **verified** from PDF text layout (same table as [`NASS cash rents TN 2024`](../source-notes/nass-cash-rents-tn-2024-surveys-pdf.md)). |
| **Regional role** | Anderson County includes **Oak Ridge** and **Knoxville MSA**-adjacent development patterns; Claxton sits in that **broad** economic/utility shadow (qualitative). | General geography—**not** a guarantee for a **specific street** address. |

---

## Likely but still assumptions (disconfirm with field evidence)

| Topic | Assumption | Why it might be wrong |
|-------|------------|------------------------|
| **Utilities / connectivity** | **Better odds** than Campbell production parcel for **retail fiber**, **same-day parts**, and **service trades** (homelab / “brain” hosting). | Rural pockets and dead zones exist; **verify** ISP maps and neighbors. |
| **Septic / buildability** | **5 ac** homestead can usually support **OSSS** planning **if** soils/perc cooperate—**not** automatic. | [`Septic captures`](../source-notes/tn-onsite-sewage-septic-captures-inbox-2026-04-18.md) are **process**-oriented; **site morph** is local. |
| **Soils / productivity** | **No** Web Soil Survey AOI for Claxton is in the current `raw/processed/` corpus—**do not** infer map units here. | Run **WSS** (or consultant soil eval) on **your** footprint. |

---

## Unknown (requires parcel-specific verification)

| Item | Action |
|------|--------|
| **Exact map units, hydric flags, limiting factors** | WSS / SSURGO AOI on **homestead** polygon; field walk with county soil survey context. |
| **Septic / SSDS class and setbacks** | County environmental health; **TDEC** rules—see septic source-notes. |
| **Electric service size, transformer location, easements** | Utility provider; **not** wiki. |
| **Floodplain / sink / karst** | FEMA maps + local overlays + walk (East TN variability). |
| **Drive time Claxton ↔ Demory farm** | **Business plan** uses **~35 min** one-way as structural default—**measure** with repeated real drives and seasonality. |

---

## Implications (two-site plan)

| Domain | Implication |
|--------|-------------|
| **Buildability** | Treat **residence + shop + OSSS** as the **first** civil engineering thread; **do not** scale farm CAPEX until **home-base** water/septic/power baselines are clear. |
| **Access** | **Prefer** vendor and family staging here; **batch** trips to Campbell per [`Trip policy`](../analyses/trip-batching-and-site-visit-policy-two-site-smart-farm.md). |
| **Soils / productivity** | **Homestead** soils matter for **garden / orchard / outbuildings**; **not** a substitute for **SITE_FARM** soil intelligence. |
| **Water / hydrology** | Roof catchment, septic drainfield hydrology, and **yard** grading are **local**; separate from **pasture** water development on `SITE_FARM`. |
| **Utilities / site work** | **Logical home** for **network head-end**, **backup power**, **MQTT broker**, and **patch cadence** per [`Reference architecture`](../analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md)—**if** power and cooling are adequate. |
| **Labor / travel** | **Control-center** role: scheduling, records, phone coverage—paired with **distance tax** on daily-touch fantasies at the farm. |
| **Automation / telemetry** | **Observe-first** automation and **alerting** land here; **field** endpoints stay tied to [`Farm spatial model`](../analyses/farm-spatial-model-and-asset-registry-standard.md) IDs. |
| **Business-plan sequencing** | **Phase 0–1**: prove **comms**, **books**, and **family coverage** from **home base** before **fleet** telemetry on **SITE_FARM**—see [`Execution dossier hub`](../analyses/execution-dossier-hub-phase-0-1-east-tennessee.md). |

---

## Related

- [`Site inventory baseline — Claxton home base`](site-inventory-baseline-claxton-home-base-east-tennessee.md) — **field** **inventory** (structures, access, storage)—**measured** facts land here; complements this **synthesis**
- [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md) — full **baseline** map (infra, utilities, loads, templates)
- [`Parcel intelligence — Claxton home base`](parcel-intelligence-claxton-home-base-east-tennessee-two-site.md) — structured **parcel worksheet** (placeholders until WSS AOI filed)
- [`Claxton and Demory — missing data register`](claxton-and-demory-missing-data-register.md) — **Parcel** gaps not yet filled from vault sources
- [`Demory farm — site intelligence (Campbell County)`](demory-farm-site-intelligence.md)
- [`Anderson County vs Campbell County — operating implications`](../comparisons/anderson-county-vs-campbell-county-operating-implications.md)
- [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md)
