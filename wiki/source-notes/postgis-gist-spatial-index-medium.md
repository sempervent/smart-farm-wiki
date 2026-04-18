---
title: "GiST spatial index in PostGIS (Medium capture)"
page_type: source_note
status: active
created: 2026-04-21
updated: 2026-04-21
source_ids:
  - raw/processed/2026/postgis-gist-spatial-index-medium.md
tags:
  - postgis
  - postgresql
  - spatial-data
review_status: unreviewed
---

# GiST spatial index in PostGIS (Medium capture)

**Raw**: [`raw/processed/2026/postgis-gist-spatial-index-medium.md`](../../raw/processed/2026/postgis-gist-spatial-index-medium.md)

**Summary**: Explains **GiST** for spatial data via **bounding boxes** / MBRs—why naive cross-joins are expensive and how the index prunes candidate pairs before full geometry tests. Directly relevant to **performance** of boundary/parcel queries in **PostGIS**.

**Used by**

- [`Data storage (farm and edge stacks)`](../concepts/data-storage.md)
