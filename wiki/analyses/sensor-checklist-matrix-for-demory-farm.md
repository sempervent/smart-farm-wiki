---
title: Sensor checklist matrix — Demory farm
page_type: analysis
status: active
created: 2026-04-25
updated: 2026-04-25
tags:
  - demory
  - sensors
  - matrix
review_status: unreviewed
confidence: medium
---

# Sensor checklist matrix — Demory farm

**Purpose**: **First-class** **planning** **matrix** **for** **long-range** **field** **sensing** **on** **`SITE_FARM` (Demory)** **(**~**120** **ac** **,** **off-grid-first** **)** **.** **Rows** **are** **classes** **—** **not** **committed** **SKUs** **or** **map** **coordinates** **(**validate** **in** **pilot** **)** **.**

**Canonical architecture**: [`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md).

**Comparison**: [`LoRaWAN vs Wi‑Fi HaLow vs Meshtastic — Demory farm sensor layer`](../comparisons/lorawan-wi-fi-halow-meshtastic-demory-farm-sensor-layer.md).

**Sources (vendors / protocol)**: [`Demory farm sensor layer — official and operator-grade source cluster`](../source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md).

**Legend**

| Column | Meaning |
|--------|---------|
| **Msg pattern** | Typical **uplink** cadence / class (**sparse** = min–hourly) |
| **Range role** | How the **radio** **behaves** **across** **~120** **ac** **(**star** **/** **mesh** **/** **IP** **segment** **)** |
| **GW dep** | **Gateway** **/** **NS** **/** **AP** **dependency** **(**H** **=** **high** **)** |
| **Offline** | **Usable** **local** **truth** **without** **WAN** **(**Y** **/** **partial** **/** **N** **)** |
| **Integ** | **Typical** **integration** **(**MQTT** **→** **broker** **→** **HA** **/** **farmOS** **/** **TSDB** **)** |
| **Env** | **Enclosure** **/** **weather** **hardening** **assumption** |
| **Maint** | **Ops** **burden** **(**L** **/** **M** **/** **H** **)** |
| **Pilot** | **P** **=** **good** **pilot** **candidate** **;** **N** **=** **defer** |
| **Phase** | **0** **=** **instrument** **/** **learn** **;** **1** **=** **pilot** **;** **2** **=** **scale** |

---

## Matrix

| Use case | Device / class | Protocol | Msg pattern | Power | Range role | GW dep | Offline | Integ | Env | Maint | Pilot | Phase | Notes / open questions |
|----------|----------------|----------|-------------|-------|------------|--------|---------|-------|-----|-------|-------|-------|------------------------|
| Soil moisture / temp / salinity | LoRaWAN soil probe (vendor ecosystem) | LoRaWAN | Sparse (15m–1h) | Solar + batt | Star to GW | H | Y | MQTT via NS | IP6x vendor | M | P | 0–1 | **Verify** **depth** **/** **soil** **type** **;** **Decentlab** **/** **Dragino-class** **captures** **in** **source** **cluster** |
| Soil EC | LoRaWAN EC-capable probe | LoRaWAN | Sparse | Solar + batt | Star to GW | H | Y | MQTT | IP65+ | M | P | 1 | **Calibration** **drift** **;** **temperature** **compensation** |
| Weather station | LoRaWAN met pack | LoRaWAN | 10m–1h | Solar + batt | Star / taller mast | H | Y | MQTT | Mast + surge | M | P | 0–1 | **Wind** **/** **icing** **on** **ridge** **—** **unvalidated** **here** |
| Rainfall | Tipping bucket → LoRaWAN encoder | LoRaWAN | Event + heartbeat | Batt | Star to GW | H | Y | MQTT | Funnel clog risk | L–M | P | 0 | **Manual** **as** **SoR** **for** **total** **season** **?** |
| Tank / pond level | Ultrasonic / pressure → LoRaWAN | LoRaWAN | 15m–1h | Solar + batt | Star to GW | H | Partial | MQTT | Condensation | M | P | 1 | **Local** **sight** **/** **float** **for** **welfare** **truth** **per** **dependency** **map** |
| Gate / fence line | Open-closed sensor, LoRaWAN | LoRaWAN | Event | Batt | Star to GW | H | Y | MQTT | Outdoor | L | P | 1 | **Not** **sole** **proof** **of** **stock** **containment** |
| Pump / irrigation state | VFD / pressure / flow → gateway | LoRaWAN or wired | 1–5m | Wired or solar | Star | M | Y | MQTT / Modbus bridge | Wet location | M–H | P | 1–2 | **Safety** **interlocks** **local** **—** **not** **WAN** **.** |
| Site power / solar telemetry | Inverter / BMS → IP or LoRaWAN bridge | Mixed | 1–5m | N/A | Barn concentrator | M | Y | MQTT | Indoor / combiner | M | P | 1 | **Align** **with** **Victron** **/** **solar** **captures** **in** **RF** **index** |
| Microclimate (temp/RH) | LoRaWAN sensor | LoRaWAN | 15–60m | Batt | Star | H | Y | MQTT | Radiation shield | L | P | 0 | **Placement** **vs** **grazing** **damage** |
| Perimeter / presence (animal) | **Only** **if** **justified** | LoRaWAN / camera on HaLow | Event / stream | Solar / PoE | Star or IP segment | H | Partial | MQTT / RTSP | Harsh | H | N | 2 | **High** **false** **positive** **risk** **;** **defer** **without** **use** **case** |
| Infra health (enclosure temp, water in box) | LoRaWAN or Meshtastic | LoRa / mesh | 15–60m | Batt | Mesh or star | M | Y | MQTT | IP65 | L | P | 0 | **Gateway** **box** **condensation** |
| Meshtastic environmental | Meshtastic + sensor module | Mesh | 5–30m | Solar + batt | Multi-hop | M | Y | MQTT bridge | Field | M | P | 0–1 | **Firmware** **churn** **;** **map** **health** |
| HaLow IP sensor / bridge | 802.11ah CPE | HaLow | App-dependent | PoE / solar | Point-to-point / segment | M–H | Y | MQTT / IP | Outdoor CPE | H | N | 1–2 | **Use** **when** **IP** **throughput** **wins** **over** **LoRa** |
| Starlink (WAN only) | Starlink CPE | — | N/A | AC / site power | N/A | — | N/A | — | Outdoor | M | N | — | **Not** **a** **sensor** **radio** **—** **egress** **only** **.** |

---

## How to use

1. **Pick** **one** **RF** **family** **per** **pilot** **until** **stop** **rules** **pass** **(**[`Mesh strategy`](../analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md)**)** **.**
2. **Pair** **each** **row** **with** **SoR** **rules** **(**[`Telemetry SoR`](../analyses/telemetry-system-of-record-boundaries-and-authority.md)**)** **.**
3. **Reconcile** **with** **degraded** **modes** **(**[`Sensor degraded modes — Demory`](sensor-degraded-modes-and-failure-rules-demory-farm.md)**)** **.**

---

## Related

- [`Sensor power and duty-cycle assumptions — Demory`](sensor-power-and-duty-cycle-assumptions-demory-farm.md)
- [`Field-node classes and communication roles — Demory`](field-node-classes-and-communication-roles-demory-farm.md)
