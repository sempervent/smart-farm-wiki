---
title: LoRaWAN vs Wi‑Fi HaLow vs Meshtastic — Demory farm sensor layer
page_type: comparison
status: active
created: 2026-04-25
updated: 2026-04-25
tags:
  - demory
  - lorawan
  - halow
  - meshtastic
  - sensors
review_status: unreviewed
confidence: medium
aliases:
  - Demory sensor layer RF comparison
---

# LoRaWAN vs Wi‑Fi HaLow vs Meshtastic — Demory farm sensor layer

## Question

For **`SITE_FARM` (Demory)**, **~120 acres**, **off-grid-first** field **sensing**, how do **LoRaWAN**, **802.11ah / Wi‑Fi HaLow**, and **Meshtastic (LoRa mesh)** compare on **coverage**, **power**, **ops**, **survivability**, and **IP vs sparse telemetry**?

**Scope**: **Field RF** for **sensors**—not **Starlink** as a **radio** (Starlink is **WAN** only—[`Farm sensor architecture — Demory`](../analyses/farm-sensor-architecture-demory-farm-site.md)).

**Wider four-way** (incl. conventional Wi‑Fi): [`Wi‑Fi HaLow vs LoRaWAN vs Meshtastic vs conventional Wi‑Fi`](../comparisons/wi-fi-halow-lorawan-meshtastic-conventional-wi-fi-farm-field-networking.md). **LoRaWAN vs Meshtastic only**: [`LoRaWAN vs Meshtastic for fixed farm telemetry`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md).

**Sources**: [`Demory farm sensor layer — official and operator-grade source cluster`](../source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md).

---

## ~120-acre coverage (assumptions)

| Stack | Coverage mental model | Planning notes |
|-------|----------------------|----------------|
| **LoRaWAN** | **Star** to **one or more** **gateways**; **km-class** **links** **possible** **with** **height** **and** **clearing** | **Terrain** **may** **require** **multiple** **G** **or** **tall** **mount** **—** **RF** **survey** **.** |
| **Meshtastic** | **Multi-hop** **mesh** **fills** **holes** **where** **nodes** **exist** | **Density** **and** **map** **≠** **RF** **;** **partitions** **possible** **.** |
| **Wi‑Fi HaLow** | **Sub-GHz** **IP** **links** **;** **range** **depends** **on** **AP/CPE** **and** **rate** | **Higher** **throughput** **than** **LoRa** **but** **not** **automatic** **farm-wide** **mesh** **.** |

**No** **single** **answer** **without** **terrain** **map** **+** **gateway** **locations** **(**not** **asserted** **here** **)** **.**

---

## Criteria (sensor-layer focus)

| Criterion | LoRaWAN | Wi‑Fi HaLow | Meshtastic |
|-----------|---------|-------------|------------|
| **Bandwidth** | **Very** **low** **(**application** **payloads** **)** | **Mbps-class** **IP** **where** **deployed** | **Low** **(**text** **/** **telemetry** **class** **)** |
| **Battery life** | **Excellent** **for** **sleeping** **Class** **A** **-style** **devices** | **Worse** **for** **always-on** **CPE** **vs** **deep** **sleep** **LoRa** | **Good** **leaf** **;** **higher** **when** **routing** |
| **Solar friendliness** | **Strong** **for** **sparse** **uplinks** | **Plan** **for** **AP** **+** **CPE** **load** | **Strong** **for** **small** **nodes** **;** **budget** **repeaters** |
| **Deployment complexity** | **Gateway** **+** **NS** **(**e.g.** **ChirpStack** **)** **+** **join** **model** | **802.11** **ops** **(**patching** **,** **segmentation** **)** | **Mesh** **map** **+** **firmware** **cadence** |
| **Gateway architecture** | **Central** **GW** **→** **NS** | **AP** **/** **bridge** **→** **LAN** | **Bridge** **→** **MQTT** **at** **G** |
| **Local survivability** | **Works** **without** **WAN** **;** **GW** **SPOF** **risk** | **LAN** **segment** **without** **WAN** | **Mesh** **local** **;** **partition** **risk** |
| **Maintenance burden** | **NS** **+** **GW** **health** | **Firmware** **/** **Wi‑Fi** **security** | **Mesh** **health** **+** **releases** |
| **IP-native** | **No** **(**app** **layer** **on** **NS** **)** | **Yes** | **No** **(**bridge** **for** **IP** **)** |
| **Sparse telemetry** | **Excellent** | **Overkill** **unless** **you** **need** **IP** | **Excellent** |
| **Richer edge** **/** **actuation** | **Limited** **by** **duty-cycle** **/** **rate** | **Better** **when** **IP** **needed** | **Limited** **;** **not** **PLC** **replacement** |
| **Observational sensors** | **Strong** **fit** | **Fit** **if** **IP** **sensors** **/** **throughput** | **Strong** **fit** |
| **Control** **/** **actuation** | **Usually** **downlink** **constrained** **;** **design** **carefully** | **Possible** **on** **IP** **path** | **Do** **not** **assume** **without** **engineering** **review** |

---

## Recommendation heuristic (wiki ops)

- **Default** **sparse** **soil** **/** **weather** **/** **tank** **:** **LoRaWAN** **or** **Meshtastic** **leaf** **—** **see** [`Sensor checklist matrix — Demory`](../analyses/sensor-checklist-matrix-for-demory-farm.md) **.**
- **Need** **IP** **throughput** **or** **MQTT** **on** **MCU** **at** **distance** **:** **HaLow** **segment** **where** **hardware** **ROI** **clears** **.**
- **Never** **treat** **Starlink** **as** **field** **sensor** **link** **.**

---

## Related

- [`Mesh and field networking strategy — off-grid Demory`](../analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md)
- [`Sub-GHz Wi‑Fi HaLow farm sensors deployment guide`](../analyses/subghz-wi-fi-halow-farm-sensors-deployment-guide.md)
