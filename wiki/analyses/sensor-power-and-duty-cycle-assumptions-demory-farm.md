---
title: Sensor power and duty-cycle assumptions — Demory farm site
page_type: analysis
status: active
created: 2026-04-25
updated: 2026-04-25
tags:
  - demory
  - sensors
  - power
  - lorawan
review_status: unreviewed
confidence: medium
---

# Sensor power and duty-cycle assumptions — Demory farm site

**Purpose**: Planning assumptions for field node power and message cadence on Demory (off-grid-first)—not site measurements. Validate with metering and SoC logs before scaling.

**Architecture**: [`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md).

**Power domains (farm-wide)**: [`Power domains and battery-backed infrastructure tiers — Demory`](off-grid-power-domains-and-battery-tiers-demory-farm.md).

**Protocol references**: LoRaWAN duty-cycle / ADR — [`lorawan-specification-v1-1.pdf`](../../raw/processed/2026/lorawan-specification-v1-1.pdf) (see extract); Meshtastic power notes in [`Demory farm sensor layer — source cluster`](../source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md).

---

## Assumptions (explicit placeholders)

| Topic | Assumption | Validate by |
|-------|------------|-------------|
| **S-class leaf** | mW–W average; solar + small pack common | Measured load budget per node |
| **LoRaWAN uplink** | Sparse intervals (minutes–hours); regional duty-cycle caps | NS metrics + RF plan |
| **Meshtastic** | Higher active draw when routing; sleep when leaf | Firmware telemetry / bench |
| **HaLow CPE** | Higher continuous draw than LoRa sleep; budget airtime + idle | PoE / solar sizing |

---

## Solar friendliness (design heuristic)

LoRaWAN / Meshtastic leaf nodes are often easier to keep on small panels and modest batteries than always-on HaLow AP—compare [`LoRaWAN vs Wi‑Fi HaLow vs Meshtastic — Demory`](../comparisons/lorawan-wi-fi-halow-meshtastic-demory-farm-sensor-layer.md).

---

## Related

- [`Sensor checklist matrix — Demory farm`](sensor-checklist-matrix-for-demory-farm.md)
- [`Time-smart sensors — 120 ac to 5 ac`](../analyses/time-smart-sensors-120ac-to-5ac-homestead.md)
