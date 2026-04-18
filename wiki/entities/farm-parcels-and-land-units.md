---
title: Farm parcels and land units
page_type: entity
status: active
created: 2026-04-21
updated: 2026-04-23
tags:
  - land
  - gis
  - farmos
  - identity
confidence: medium
review_status: unreviewed
---

# Farm parcels and land units

**What this entity is**: The **abstract pattern** of how **land** is subdivided for **management**—**parcels**, **paddocks**, **zones**, **fields**, **access roads**—and how those units get **stable IDs** in records and maps. This page does **not** replace a deed or a farm map; it **points** to the vault’s **minimum standard** for naming and authority.

**Why it matters**: Telemetry, grazing plans, and **system of record** entries must attach to **the same** land objects; mixed CRS or ad hoc names cause silent mismatch between **dashboards** and **field truth**.

**Canonical analysis**: [`Farm spatial model and asset registry standard`](../analyses/farm-spatial-model-and-asset-registry-standard.md) (IDs, `MAP_AUTHORITY_LABEL`, device naming).

**Product touchpoint**: [`farmOS`](farmos.md) asset/geometry model—see source-notes on **Assets** / **Logs**.

**Does not claim**: Your parcel boundaries, acreage to the tenth, or conservation program enrollments.

**Authority chain (land capability — generic workflow)**

1. **Federal soil survey data**: Use **Web Soil Survey** / **SSURGO** map units for **labeling** capability classes and limiting factors on **your** tracts (no substitute for field verification). See [`Web Soil Survey & 3D Elevation — captures`](../source-notes/web-soil-survey-and-elevation-captures-inbox-2026-04-18.md) and [`Execution readiness gap audit`](../analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md) §1.
2. **Local buildability / wetness**: County **septic / SSDS** rules and **site morph** drive structures—not wiki tables. See [`Tennessee — onsite sewage / septic (captures)`](../source-notes/tn-onsite-sewage-septic-captures-inbox-2026-04-18.md).
3. **Operating IDs**: Once map units and permit classes are known **for your sites**, attach **stable `PARCEL-*` / `PADDOCK-*` IDs** per [`Farm spatial model and asset registry standard`](../analyses/farm-spatial-model-and-asset-registry-standard.md).

**Related**

- Sites (roles): [`Five-acre home base (SITE_HOME) — ET two-site`](five-acre-home-base-site-home-et-two-site.md), [`120-acre production farm (SITE_FARM) — ET two-site`](120-acre-production-farm-site-farm-et-two-site.md)
- Named places (ET two-site): [`Claxton home base (place)`](claxton-home-base.md), [`Demory farm site (place)`](demory-farm-site.md); counties: [`Anderson County (two-site context)`](anderson-county-tennessee.md), [`Campbell County (two-site context)`](campbell-county-tennessee.md); **parcel worksheets**: [`Parcel intelligence package — East Tennessee two-site`](../topics/parcel-intelligence-package-east-tennessee-two-site.md)
- Topic: [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md)
- Evidence index: [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md)
