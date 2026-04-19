---
title: Farm data, farmOS, and agriculture lab builds
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - farmos
  - agriculture
  - farm-data
review_status: unreviewed
---

# Farm data, farmOS, and agriculture lab builds

**Narrative**: Small-scale **farm record-keeping** and **planning** often need an explicit data layer—**farmOS** (Drupal-based, GPL) is a community reference for **field/asset records**, modules, and self-hosting. Separately, a **homelab-adjacent** thread documents someone scaling a **~900 m² commercial-style agriculture lab** with QC, microcontrollers, and automation—commenters point to farmOS as a possible integration target for sensors and inventory-style workflows.

Together these sources connect **software** (farmOS hosting and extensibility) to **physical lab build-out** motivation without collapsing “farm management app” into generic homelab chatter.

**Canonical entity**: [`farmOS`](../entities/farmos.md)

**PostgreSQL / PostGIS (official first)**: [`PostgreSQL and PostGIS — official documentation primary cluster`](../source-notes/postgresql-and-postgis-official-documentation-primary-cluster.md) — use for **release-accurate** SQL and spatial behavior; Medium/blog primers below are **pedagogy only**.

**farmOS doc captures (batch)**: [`farmOS — documentation captures (inbox 2026-04)`](../source-notes/farmos-documentation-captures-inbox-2026-04-18.md) — Assets, logs, location, services, user guide (Evidence summary + `raw/` tables).

**Source notes**

- [`source-notes/farmos-overview-farmos-org.md`](../source-notes/farmos-overview-farmos-org.md)
- [`source-notes/agriculture-lab-build-2023-homelab-reddit.md`](../source-notes/agriculture-lab-build-2023-homelab-reddit.md)
- [`source-notes/postgis-complete-workflow.md`](../source-notes/postgis-complete-workflow.md) — PostGIS spatial DB workflow; background for **map-anchored** assets and queries.
- [`source-notes/postgresql-system-design-interviews-algomaster.md`](../source-notes/postgresql-system-design-interviews-algomaster.md) — Relational DB patterns (system-design framing).
- [`source-notes/postgresql-deep-dive-query-flow-medium-part-1.md`](../source-notes/postgresql-deep-dive-query-flow-medium-part-1.md) — PostgreSQL query path / internals primer.
- [`source-notes/geospatial-postgresql-enterprise-postgis-perry-robinson.md`](../source-notes/geospatial-postgresql-enterprise-postgis-perry-robinson.md) — Enterprise PostGIS narrative and setup themes.
- [`source-notes/postgis-gist-spatial-index-medium.md`](../source-notes/postgis-gist-spatial-index-medium.md) — GiST / bounding-box spatial indexing explainer.
- [`source-notes/postgis-day-2019-postgis-3-pdf.md`](../source-notes/postgis-day-2019-postgis-3-pdf.md) — PostGIS 3.0 deep dive slides (PDF).

**Backup and recovery (homelab / self-hosted)**

- [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](../analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md)
- [`Restore and recovery tiers — homelab farm systems`](../analyses/restore-recovery-tiers-homelab-farm-systems.md)
- [`Homelab backup stack — official captures`](../source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md) (restic, Longhorn, farmOS Docker capture)
- [`Source gap audit — backup/DR vs sub-GHz Wi‑Fi`](../analyses/source-gap-audit-backup-dr-and-subghz-wifi-2026-04-18.md)

**Related**

- [`Data storage (farm and edge stacks)`](../concepts/data-storage.md) — MQTT vs PostgreSQL/PostGIS; canonical documentation links
- [`Smart agriculture, Meshtastic, and LoRaWAN`](smart-agriculture-meshtastic-and-lorawan.md) — field sensors and gateways; farmOS as a **data sink** for records (distinct from LPWAN stacks)
- [`Homelab, self-hosting, and edge narratives`](homelab-self-hosting-and-edge-narratives.md) — where the ag-lab OP posted; overlaps with automation skill-building
- [`ESP32, ESPHome, and smart-farming builds`](esp32-iot-smart-farming-and-tooling.md) — MCU prototypes the OP anticipated for devices feeding automation
- [`Implementation backlog — strategic audit (P0–P3)`](../analyses/implementation-backlog-strategic-audit.md) — **Asset registry** and **spatial** naming targets
