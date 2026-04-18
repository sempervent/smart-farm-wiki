---
title: Demory farm sensor layer — official and operator-grade source cluster
page_type: source_note
status: active
created: 2026-04-25
updated: 2026-04-25
source_ids:
  - raw/processed/2026/lorawan-specification-v1-1.pdf
  - raw/processed/2026/architecture-chirpstack-open-source-lorawan-network-server-documentation.md
  - raw/processed/2026/getting-started-chirpstack-open-source-lorawan-network-server-documentation.md
  - raw/processed/2026/connecting-a-gateway-chirpstack-open-source-lorawan-network-server-documentation.md
  - raw/processed/2026/halowlink-user-guide-2-11-2.pdf
  - raw/processed/2026/halowlink-1-user-guide-2-7-5.pdf
tags:
  - demory
  - lorawan
  - chirpstack
  - halow
  - meshtastic
  - sensors
review_status: unreviewed
confidence: medium
---

# Demory farm sensor layer — official and operator-grade source cluster

**Purpose**: **Provenance spine** for **`SITE_FARM` (Demory)** long-range **field sensing**: **LoRaWAN** norms, **private NS** (ChirpStack captures), **802.11ah / HaLow** hardware guides, **Meshtastic** operator docs, **sensor vendor** pages in the vault, and **WAN** (**Starlink**) as **egress**—not as the field RF layer. **Does not** replace RF engineering, licensed survey work, or regulatory review.

**Canonical synthesis**: [`Farm sensor architecture — Demory farm site`](../analyses/farm-sensor-architecture-demory-farm-site.md) · [`Sensor checklist matrix — Demory farm`](../analyses/sensor-checklist-matrix-for-demory-farm.md) · [`LoRaWAN vs Wi‑Fi HaLow vs Meshtastic — Demory farm sensor layer`](../comparisons/lorawan-wi-fi-halow-meshtastic-demory-farm-sensor-layer.md).

**Batch index** (mixed marketing + docs): [`Inbox batch — 2026-04-18`](../source-notes/inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md).

**RF / power / WAN index** (NREL, Victron, Meshtastic, HaLow articles, Starlink captures): [`Off-grid power, field RF, and optional WAN — source index (Demory planning)`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md).

---

## LoRaWAN — protocol (authoritative text)

| Source | Raw |
|--------|-----|
| LoRaWAN L2 1.1 specification (PDF) | [`lorawan-specification-v1-1.pdf`](../../raw/processed/2026/lorawan-specification-v1-1.pdf) · [`*-extracted.md`](../../raw/processed/2026/lorawan-specification-v1-1-extracted.md) |

**Wiki concepts**: [`LoRaWAN`](../concepts/lorawan.md) · [`LoRa (radio)`](../concepts/lora-radio.md).

---

## ChirpStack — private LoRaWAN network server (documentation captures)

| Topic | Raw |
|-------|-----|
| Architecture | [`architecture-chirpstack-open-source-lorawan-network-server-documentation.md`](../../raw/processed/2026/architecture-chirpstack-open-source-lorawan-network-server-documentation.md) |
| Getting started | [`getting-started-chirpstack-open-source-lorawan-network-server-documentation.md`](../../raw/processed/2026/getting-started-chirpstack-open-source-lorawan-network-server-documentation.md) |
| Connecting a gateway | [`connecting-a-gateway-chirpstack-open-source-lorawan-network-server-documentation.md`](../../raw/processed/2026/connecting-a-gateway-chirpstack-open-source-lorawan-network-server-documentation.md) |
| Introduction (two captures) | [`introduction-chirpstack-…`](../../raw/processed/2026/introduction-chirpstack-open-source-lorawan-network-server-documentation.md) · [`introduction-chirpstack-…-1.md`](../../raw/processed/2026/introduction-chirpstack-open-source-lorawan-network-server-documentation-1.md) |

---

## Wi‑Fi HaLow — HaLowLink user guides (vendor PDF)

| Source | Raw |
|--------|-----|
| HaLowLink user guide 2.11.2 | [`halowlink-user-guide-2-11-2.pdf`](../../raw/processed/2026/halowlink-user-guide-2-11-2.pdf) · [`*-extracted.md`](../../raw/processed/2026/halowlink-user-guide-2-11-2-extracted.md) |
| HaLowLink user guide 2.7.5 | [`halowlink-1-user-guide-2-7-5.pdf`](../../raw/processed/2026/halowlink-1-user-guide-2-7-5.pdf) · [`*-extracted.md`](../../raw/processed/2026/halowlink-1-user-guide-2-7-5-extracted.md) |

**Also**: [`IEEE 802.11ah Wikipedia excerpt`](../source-notes/ieee-802-11ah-wikipedia.md) · subGHz deployment narrative in [`Off-grid power/RF source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md).

---

## Meshtastic — operator documentation (web captures)

| Topic | Raw |
|-------|-----|
| Device configuration (two captures) | [`device-configuration-meshtastic.md`](../../raw/processed/2026/device-configuration-meshtastic.md) · [`device-configuration-meshtastic-1.md`](../../raw/processed/2026/device-configuration-meshtastic-1.md) |
| Modules | [`modules.md`](../../raw/processed/2026/modules.md) |
| Technical specifications | [`technical-specifications.md`](../../raw/processed/2026/technical-specifications.md) |
| Telemetry module configuration | [`telemetry-module-configuration.md`](../../raw/processed/2026/telemetry-module-configuration.md) · [`telemetry-module-configuration-1.md`](../../raw/processed/2026/telemetry-module-configuration-1.md) |

**Also**: Meshtastic captures in [`Off-grid power/RF source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) (getting started, power configuration).

---

## Field sensor vendors — product pages (vault captures; validate before buying)

**Soil / weather / EC (LoRaWAN-class marketing pages in batch)**

| Product line (capture) | Raw |
|------------------------|-----|
| Decentlab DL-SDD / DL-SMTP / DL-TRS | [`dl-sdd-…`](../../raw/processed/2026/dl-sdd-soil-moisture-temperature-and-salinity-profile-for-lorawan-decentlab-lorawan-sensor-devices-for-environmental-monitoring.md) · [`dl-smtp-…`](../../raw/processed/2026/dl-smtp-soil-moisture-and-temperature-profile-for-lorawan-decentlab-lorawan-sensor-devices-for-environmental-monitoring.md) · [`dl-trs12-…`](../../raw/processed/2026/dl-trs12-dl-trs11-soil-moisture-temperature-and-electrical-conductivity-sensor-for-lorawan-decentlab-lorawan-sensor-devices-for-environmental-monitoring.md) |
| Decentlab soil / weather pages | [`lorawan-soil-moisture-temperature-and-electrical-conductivity-sensor.md`](../../raw/processed/2026/lorawan-soil-moisture-temperature-and-electrical-conductivity-sensor.md) · [`lorawan-weather-station-solar-powered-iot-weather-station.md`](../../raw/processed/2026/lorawan-weather-station-solar-powered-iot-weather-station.md) |
| Dragino-class LSE01 / SE01 / SE02 pages | [`lse01-lorawan-soil-moisture-ec-sensor.md`](../../raw/processed/2026/lse01-lorawan-soil-moisture-ec-sensor.md) · [`se01-lbls-…`](../../raw/processed/2026/se01-lbls-lorawan-soil-moisture-ec-sensor.md) · [`se02-lb-…`](../../raw/processed/2026/se02-lb-lorawan-soil-moisture-ec-sensor.md) |
| LSE01 power analysis (PDF) | [`lse01-v1-0-0-power-analyze.pdf`](../../raw/processed/2026/lse01-v1-0-0-power-analyze.pdf) · [`*-extracted.md`](../../raw/processed/2026/lse01-v1-0-0-power-analyze-extracted.md) |

**Treat as product marketing**, not independent validation—pair with **field trials** and **regional RF** planning.

---

## Starlink — optional WAN / backhaul (not field RF)

Starlink is **WAN CPE** / **backhaul** for **egress** and **remote visibility** from [`SITE_HOME`](../entities/five-acre-home-base-site-home-et-two-site.md)—see [`WAN edge and backhaul roles`](../entities/wan-edge-and-backhaul-roles.md) and [`Connectivity strategy — Claxton & Demory`](../analyses/connectivity-strategy-for-claxton-and-demory.md). **Captures** (specs, enterprise FAQ): [`Electrical, networking, and Starlink — inbox batch (2026-04-23)`](../source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md) and entries under [`Off-grid power/RF source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md).

---

## Gateway / controller roles (wiki entities)

- [`RF and telemetry gateway roles — field network`](../entities/rf-telemetry-gateway-roles-field-network.md) — LPWAN / mesh → MQTT / broker.
- [`Kubernetes edge control-plane roles`](../entities/kubernetes-edge-control-plane-roles.md) — if the **controller** is **k3s**-hosted.
- [`Field node classes (G/R/S/H/W)`](../entities/field-node-classes-off-grid-farm-roles.md) — **G** vs **W** distinction.
