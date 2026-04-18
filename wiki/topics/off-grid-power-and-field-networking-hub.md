---
title: Off-grid power and field networking — hub
page_type: topic
status: active
created: 2026-04-24
updated: 2026-04-25
tags:
  - off-grid
  - field-network
  - mesh
  - wan
  - two-site
  - navigation
review_status: unreviewed
confidence: high
---

# Off-grid power and field networking — hub

**Purpose**: **Single entry** for readers asking “where is **off-grid power**, **field RF**, and **WAN** handled?”—spanning the **Demory `SITE_FARM`** doctrine, **two-site** connectivity (Claxton + Demory), and **cross-cutting** comparisons. Reduces hunting through [`index.md`](../index.md) analyses lists.

**What this hub owns**: **Routing** and **read order** for those themes. It does **not** replace the **first-class** Demory doctrine page (below)—that page remains the **deepest** map for off-grid-first **`SITE_FARM`**.

**What it does not own**: **kW**, **SKU**, or **permit** answers—those stay in site baselines, loads registers, and local engineering.

---

## Start here

| Situation | Open |
|-----------|------|
| **Off-grid-first production farm (`SITE_FARM` at Demory)** — solar/battery default, mesh/field RF, WAN optional, degraded modes | [`Off-grid systems doctrine package — Demory farm site`](off-grid-systems-doctrine-package-demory-farm-site.md) — **canonical doctrine map** |
| **Two-site WAN / Starlink / LTE / pilot vs scale** (both named sites) | [`Connectivity strategy — Claxton home base and Demory farm site`](../analyses/connectivity-strategy-for-claxton-and-demory.md) |
| **Field telemetry stack** (broker, SoR, gateways — both sites) | [`Field telemetry network — two-site`](../entities/field-telemetry-network-two-site.md) + [`Field telemetry reference architecture — homestead + 120-acre farm`](../analyses/field-telemetry-reference-architecture-homestead-120ac.md) |
| **Demory field sensors** (~120 ac, LoRaWAN / HaLow / mesh, Starlink = WAN only) | [`Farm sensor architecture — Demory farm site`](../analyses/farm-sensor-architecture-demory-farm-site.md) · [`Sensor checklist matrix — Demory farm`](../analyses/sensor-checklist-matrix-for-demory-farm.md) |
| **Provenance (NREL, Victron, Meshtastic, HaLow, Starlink captures)** | [`Off-grid power, field RF, and optional WAN — source index (Demory planning)`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) |
| **Homestead-scale solar vocabulary** (not Demory-specific) | [`Off-grid solar power and storage (special topic)`](off-grid-solar-power-and-storage.md) |

---

## Canonical (durable scope)

| Cluster | Page | Notes |
|---------|------|--------|
| **Demory off-grid doctrine** | [`Off-grid systems doctrine package — Demory`](off-grid-systems-doctrine-package-demory-farm-site.md) | Power domains, node classes **G/R/S/H/W**, WAN deps, stop rules **DR-*** |
| **Two-site WAN + topology** | [`Connectivity strategy — Claxton & Demory`](../analyses/connectivity-strategy-for-claxton-and-demory.md), [`Execution topology package — two-site (Mermaid)`](../analyses/execution-topology-package-two-site-smart-farm.md), [`Two-site network topology and WAN edge reference`](../analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md) | **Zoning** and pilot vs production paths |
| **Field roles (entities)** | [`Field node classes (G/R/S/H/W)`](../entities/field-node-classes-off-grid-farm-roles.md), [`RF telemetry gateway`](../entities/rf-telemetry-gateway-roles-field-network.md), [`WAN edge and backhaul roles`](../entities/wan-edge-and-backhaul-roles.md), [`Field radio link classes`](../entities/field-radio-link-classes.md) | **Roles**, not vendors |

---

## Supporting analyses and comparisons

| Page | Role |
|------|------|
| [`Mesh and field networking strategy — off-grid Demory`](../analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md) | Layering Meshtastic vs HaLow vs Wi‑Fi |
| [`Farm sensor architecture — Demory farm site`](../analyses/farm-sensor-architecture-demory-farm-site.md) | Reference / pilot / degraded Mermaid; Claxton visibility without Starlink as field RF |
| [`LoRaWAN vs Wi‑Fi HaLow vs Meshtastic — Demory farm sensor layer`](../comparisons/lorawan-wi-fi-halow-meshtastic-demory-farm-sensor-layer.md) | Sensing-layer criteria for ~120 ac |
| [`Meshtastic vs HaLow vs conventional Wi‑Fi — off-grid farm`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md) | Tradeoff matrix |
| [`Off-grid farm execution topology — Demory (Mermaid)`](../analyses/off-grid-farm-execution-topology-demory-mermaid.md) | Diagrams |
| [`Automation stop rules — two-site`](../analyses/automation-stop-rules-two-site-smart-farm.md) | **CS-***, **MV-*** drills touching WAN/power |
| [`LoRa, MQTT, and gateway bridges`](lora-mqtt-and-gateway-bridges.md) | DIY / MQTT bridge **topic** (mixed authority—see note on that page) |

---

## Local site context (named anchors)

- [`Demory farm — site intelligence`](../analyses/demory-farm-site-intelligence.md), [`Claxton home base — site intelligence`](../analyses/claxton-home-base-site-intelligence.md)
- Router: [`Local site and county intelligence`](local-site-and-county-intelligence.md)

---

## Related hubs

- [`Platform doctrine package — homelab / farm edge`](platform-doctrine-package-homelab-farm-edge.md)
- [`Backup and disaster recovery — doctrine hub`](backup-disaster-recovery-doctrine-hub.md)
- [`Business plan execution and pilot operations hub`](business-plan-execution-and-pilot-operations-hub.md)
- [`Two-site smart farm operations`](two-site-smart-farm-operations.md)
