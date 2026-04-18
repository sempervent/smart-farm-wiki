---
title: Data storage (farm and edge stacks)
page_type: concept
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - data
  - mqtt
  - postgresql
  - postgis
confidence: medium
review_status: unreviewed
---

# Data storage (farm and edge stacks)

On a smart farm, **data storage** spans at least two familiar layers: **short-lived streaming handoff** from sensors and gateways, and **durable structured storage** for assets, history, and maps.

## Messaging handoff (MQTT)

**MQTT** is a common **pub/sub** protocol between edge devices, brokers, and application services (for example after LoRaWAN or DIY LoRa bridges). Official specification and overview material:

- [MQTT — specification (overview and versions)](https://mqtt.org/mqtt-specification/)
- [MQTT Version 5.0 — OASIS Standard](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html)

In this vault, field-to-broker patterns are collected under [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md).

## Relational and spatial databases (PostgreSQL / PostGIS)

**PostgreSQL** is a general-purpose **relational** database; **PostGIS** extends it for **geometry and geography**—useful for parcels, boundaries, and asset locations.

- [PostgreSQL documentation (current)](https://www.postgresql.org/docs/current/)
- [PostGIS — documentation](https://postgis.net/documentation/)

Slide capture (complements the docs above): [`PostGIS Day 2019 — PostGIS 3.0 deep dive (PDF slides)`](../source-notes/postgis-day-2019-postgis-3-pdf.md).

Background captures (not a substitute for the manuals above):

- [`PostgreSQL — system design interviews (Algomaster capture)`](../source-notes/postgresql-system-design-interviews-algomaster.md)
- [`PostgreSQL internals — query flow (Medium, part 1 capture)`](../source-notes/postgresql-deep-dive-query-flow-medium-part-1.md)
- [`Geospatial PostgreSQL for enterprise — PostGIS deep dive (Perry Robinson capture)`](../source-notes/geospatial-postgresql-enterprise-postgis-perry-robinson.md)
- [`GiST spatial index in PostGIS (Medium capture)`](../source-notes/postgis-gist-spatial-index-medium.md)
- [`PostGIS — complete workflow (capture)`](../source-notes/postgis-complete-workflow.md)

Farm management and lab-build context: [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md).

## Related

- [`LLM Wiki pattern`](llm-wiki-pattern.md) — how provenance and synthesis relate in this repository
- [`Domain content overview`](../analyses/domain-content-overview.md) — “data” strand among land, networks, power, and time
