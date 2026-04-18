---
title: Farm parcels and land units
page_type: entity
status: active
created: 2026-04-21
updated: 2026-04-21
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

**Related**

- Sites: [`Five-acre home base (SITE_HOME) — ET two-site`](five-acre-home-base-site-home-et-two-site.md), [`120-acre production farm (SITE_FARM) — ET two-site`](120-acre-production-farm-site-farm-et-two-site.md)
- Topic: [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md)
