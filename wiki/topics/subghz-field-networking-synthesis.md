---
title: Sub-GHz field networking — synthesis
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - subghz
  - lorawan
  - meshtastic
  - wi-fi-halow
  - field-network
  - lpwan
  - two-site
review_status: unreviewed
confidence: high
aliases:
  - SubGHz networking summary
---

# Sub-GHz field networking — synthesis

**Purpose**: **One file** that maps **everything this wiki treats as sub-GHz field networking**—LoRa PHY stacks, **LoRaWAN**, **Meshtastic** mesh, **IEEE 802.11ah / Wi‑Fi HaLow**—and routes readers to **canonical** analyses, **comparisons**, **entities**, and **source clusters**. It does **not** replace detailed pages; it **indexes** them.

**Integration**: New RF captures should **activate** per [`AGENTS.md`](../../AGENTS.md): cluster **source-notes** get **Evidence summaries**; doctrine pages absorb **claims** that change architecture or stop rules. Start from [`Off-grid power and field networking hub`](off-grid-power-and-field-networking-hub.md) or the **source index** below—not this page alone.

---

## Scope — what “sub-GHz” means here

| In scope | Notes |
|----------|--------|
| **LoRa** physical layer | Chirp spread spectrum; shared by LoRaWAN and Meshtastic. |
| **LoRaWAN** | Star / gateway → network server → application; sparse telemetry, LPWAN. |
| **Meshtastic** | LoRa **mesh** (multi-hop), local survivability, bridges to IP/MQTT at gateways. |
| **Wi‑Fi HaLow** (802.11ah) | Sub-GHz **IP**-class links; different ops model than LPWAN. |
| **MQTT / app bridges** | How sensor traffic reaches brokers and consumers—not a radio layer, but wired throughout. |

| Adjacent / contrasted | Notes |
|------------------------|--------|
| **WAN** (Starlink, LTE, fiber) | **Not** a field sensor radio; see **WAN vs field RF** below. |
| **Conventional 2.4 / 5 / 6 GHz Wi‑Fi** | Compared in four-way analyses; not “sub-GHz” but part of the same **field networking** decisions. |
| **NB‑IoT / cellular LPWAN** | Mentioned in [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](field-network-iot-comparisons.md); not a primary East Tennessee stack in this vault. |

---

## Executive summary

- **Field sub-GHz** in this repo is organized around **sparse telemetry** (LoRaWAN or Meshtastic) vs **IP throughput where needed** (HaLow segments), always on an **off-grid-aware** power and **local-first** survivability story—especially for **`SITE_FARM` (Demory)**.
- **LoRaWAN** fits **star** coverage to one or more **gateways**; **terrain and gateway placement** dominate range claims—treat vendor numbers as **hypotheses**.
- **Meshtastic** adds **mesh relay** and community/off-grid voice; **density and partitions** matter as much as “range.”
- **Wi‑Fi HaLow** trades **802.11-style ops** (segmentation, patching, AP/CPE power) for **longer-range IP** than indoor Wi‑Fi—not automatic farm-wide mesh.
- **Starlink / LTE / fiber** are **WAN backhaul** roles; they must **not** be confused with **field sensor links** (canonical rule across sensor architecture pages).

---

## WAN vs field RF (non-negotiable)

**Starlink, cellular, and terrestrial broadband** answer “how does the farm reach the internet or site-to-site VPN?” **Sub-GHz field stacks** answer “how do **sensors and field nodes** reach a **gateway / broker** when Wi‑Fi or Ethernet is impractical?”

Authoritative articulation: [`Farm sensor architecture — Demory farm site`](../analyses/farm-sensor-architecture-demory-farm-site.md) (**Starlink = WAN only**). WAN strategy: [`Connectivity strategy — Claxton home base and Demory farm site`](../analyses/connectivity-strategy-for-claxton-and-demory.md). WAN **roles** as entities: [`WAN edge and backhaul roles`](../entities/wan-edge-and-backhaul-roles.md) vs [`RF telemetry gateway roles`](../entities/rf-telemetry-gateway-roles-field-network.md).

---

## Three stacks — mental model

| Stack | Shape | Best mental picture |
|-------|--------|---------------------|
| **LoRaWAN** | Star to GW + NS | **Sparse uplinks**, excellent sleep; **gateway** concentration risk. |
| **Meshtastic** | Mesh | **Multi-hop** fill-in; **map ≠ RF**; bridge at **G** to IP/MQTT. |
| **Wi‑Fi HaLow** | 802.11ah segment | **IP-native** where deployed; plan **AP/CPE** power and **security** like Wi‑Fi. |

**Deeper criteria** (coverage, power, survivability, IP vs sparse): [`LoRaWAN vs Wi‑Fi HaLow vs Meshtastic — Demory farm sensor layer`](../comparisons/lorawan-wi-fi-halow-meshtastic-demory-farm-sensor-layer.md).

---

## Start here — by reader goal

| Goal | Open |
|------|--------|
| **Router** — power + WAN + field RF together | [`Off-grid power and field networking hub`](off-grid-power-and-field-networking-hub.md) |
| **Demory off-grid doctrine** (power, **G/R/S/H/W**, DR rules) | [`Off-grid systems doctrine package — Demory farm site`](off-grid-systems-doctrine-package-demory-farm-site.md) |
| **~120 ac sensor architecture** (reference / pilot / degraded) | [`Farm sensor architecture — Demory farm site`](../analyses/farm-sensor-architecture-demory-farm-site.md) |
| **Checklist matrix** (use case × protocol × power) | [`Sensor checklist matrix — Demory farm`](../analyses/sensor-checklist-matrix-for-demory-farm.md) |
| **Mesh vs HaLow vs Wi‑Fi layering** | [`Mesh and field networking strategy — off-grid Demory farm`](../analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md) |
| **Two-site telemetry** (broker, SoR, both sites) | [`Field telemetry network — two-site`](../entities/field-telemetry-network-two-site.md), [`Field telemetry reference architecture — homestead + 120-acre farm`](../analyses/field-telemetry-reference-architecture-homestead-120ac.md) |
| **LPWAN / HaLow / NB-IoT article index** | [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](field-network-iot-comparisons.md) |
| **MQTT, bridges, DIY gateways** | [`LoRa, MQTT, and gateway bridges`](lora-mqtt-and-gateway-bridges.md) |
| **Provenance hub** (NREL, Victron, Meshtastic, HaLow, Starlink captures) | [`Off-grid power, field RF, and optional WAN — source index (Demory planning)`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) |
| **Sensor vendor / spec cluster** | [`Demory farm sensor layer — official and operator-grade source cluster`](../source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md) |

---

## Comparisons (wiki)

- [`LoRaWAN vs Wi‑Fi HaLow vs Meshtastic — Demory farm sensor layer`](../comparisons/lorawan-wi-fi-halow-meshtastic-demory-farm-sensor-layer.md) — **Primary** three-way for **`SITE_FARM`** sensing.
- [`Wi‑Fi HaLow vs LoRaWAN vs Meshtastic vs conventional Wi‑Fi — farm field networking`](../comparisons/wi-fi-halow-lorawan-meshtastic-conventional-wi-fi-farm-field-networking.md) — Four-way matrix (adds **conventional Wi‑Fi**).
- [`LoRaWAN vs Meshtastic for fixed farm telemetry`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md) — Star/gateway vs mesh; SPOF and ops.
- [`Meshtastic vs Wi‑Fi HaLow vs conventional Wi‑Fi — off-grid farm operations`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md) — Off-grid-first operations framing.
- [`Anderson County vs Campbell County — operating implications`](../comparisons/anderson-county-vs-campbell-county-operating-implications.md) — **Not** RF physics—**two-site** context for where telemetry and WAN assumptions differ.

---

## Concepts

- [`LoRa (radio)`](../concepts/lora-radio.md) — PHY vs stacks.
- [`LoRaWAN`](../concepts/lorawan.md) — LPWAN star model.
- [`Meshtastic`](../concepts/meshtastic.md) — LoRa mesh firmware ecosystem.
- [`Wi-Fi HaLow`](../concepts/wi-fi-halow.md) — 802.11ah sub-GHz Wi‑Fi.

---

## Analyses — architecture, gateway patterns, degraded modes

| Page | Role |
|------|------|
| [`Gateway and controller patterns — Demory (~120 acres)`](../analyses/gateway-controller-patterns-demory-120-acre-farm.md) | NS, mesh bridge, HaLow segment, controller placement. |
| [`Gateway naming and role assignment standard`](../analyses/gateway-naming-and-role-assignment-standard.md) | RF telemetry vs **WAN CPE** naming. |
| [`Field node classes and communication roles — Demory farm`](../analyses/field-node-classes-and-communication-roles-demory-farm.md) | Roles aligned to **G/R/S/H/W**. |
| [`Sensor degraded modes and failure rules — Demory farm site`](../analyses/sensor-degraded-modes-and-failure-rules-demory-farm.md) | Stale MQTT vs welfare truth. |
| [`Sensor power and duty-cycle assumptions — Demory farm site`](../analyses/sensor-power-and-duty-cycle-assumptions-demory-farm.md) | Placeholder cadence—validate before scale. |
| [`Sub-GHz Wi‑Fi (HaLow) — farm sensors deployment guide`](../analyses/subghz-wi-fi-halow-farm-sensors-deployment-guide.md) | Operator checklist / outline. |
| [`Off-grid implications — backup and networking choices`](../analyses/off-grid-implications-backup-and-networking-choices.md) | Power/WAN vs backup windows. |
| [`Connectivity dependency map — farm systems (Demory)`](../analyses/connectivity-dependency-map-farm-systems-demory-farm.md) | What depends on what. |
| [`Source gap audit — backup/DR vs sub-GHz Wi‑Fi (2026-04-18)`](../analyses/source-gap-audit-backup-dr-and-subghz-wifi-2026-04-18.md) | Evidence map for HaLow vs homelab/farm backup topics. |
| [`Two-site smart farm — network topology and WAN/edge reference`](../analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md) | **Mermaid** WAN + telemetry plane. |
| [`Smart technology and telemetry strategy — control center on 5 acres`](../analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) | **AA/AF/PA/SO** controls; stop rules. |
| [`Telemetry system of record — boundaries and authority`](../analyses/telemetry-system-of-record-boundaries-and-authority.md) | Records vs telemetry vs dashboards. |

---

## Entities — roles and link layers

- [`Field node classes (G/R/S/H/W) — off-grid farm roles`](../entities/field-node-classes-off-grid-farm-roles.md)
- [`RF telemetry gateway roles — field network`](../entities/rf-telemetry-gateway-roles-field-network.md)
- [`Field radio link classes — LPWAN, mesh, and IP bridges`](../entities/field-radio-link-classes.md)
- [`WAN edge and backhaul roles`](../entities/wan-edge-and-backhaul-roles.md)

---

## Standards (naming and boundaries)

- [`Field node identity and naming standard`](../analyses/field-node-identity-and-naming-standard.md)
- [`Gateway naming and role assignment standard`](../analyses/gateway-naming-and-role-assignment-standard.md)
- [`Site-to-site network role boundaries standard`](../analyses/site-to-site-network-role-boundaries-standard.md)

---

## Source clusters and notable batches

| Kind | Page |
|------|------|
| **Demory planning index** | [`Off-grid power, field RF, and optional WAN — source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) |
| **Sensor layer cluster** | [`Demory farm sensor layer — official and operator-grade source cluster`](../source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md) |
| **Tennessee batch** (LoRaWAN, ChirpStack, Meshtastic, Decentlab, HaLow) | [`Inbox batch — 2026-04-18`](../source-notes/inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md) |
| **Electrical / Starlink batch** | [`Electrical, networking, and Starlink — inbox batch (2026-04-23)`](../source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md) |

**Illustrative Meshtastic / solar node sources** (operator-grade mixed authority): [`Building solar-powered Meshtastic community network`](../source-notes/building-solar-powered-meshtastic-community-network.md), [`How to build a solar Meshtastic node the easy way`](../source-notes/how-to-build-solar-meshtastic-node-easy-way.md), [`Meshtastic nodes basics and deployment (Seeed)`](../source-notes/meshtastic-nodes-basics-deployment-seeed.md), [`Solar Meshtastic GPS ESP32 outdoor`](../source-notes/solar-meshtastic-gps-esp32-outdoor.md).

---

## Related topics (narrative and precision ag)

- [`Smart agriculture, Meshtastic, and LoRaWAN`](smart-agriculture-meshtastic-and-lorawan.md)
- [`Precision agriculture`](../concepts/precision-agriculture.md) — concept; see source-notes from [`Field network IoT comparisons`](field-network-iot-comparisons.md) for LPWAN article links.

---

## Runbooks touching field / backhaul

- [`Runbook — broker or backhaul down`](../analyses/runbook-broker-or-backhaul-down.md)
- [`Runbook — power loss at remote site`](../analyses/runbook-power-loss-remote-site.md)
- [`Runbook — sensor false positive and alert triage`](../analyses/runbook-sensor-false-positive-alert-triage.md)

---

## Meta

- **Catalog**: [`index.md`](../index.md) — full wiki index (this page is a **focused slice**).
- **Package artifact backlog** (matrices, Evidence queues): [`Package artifact backlog — canonical East Tennessee packages`](../analyses/package-artifact-backlog-canonical-packages-east-tennessee.md).
