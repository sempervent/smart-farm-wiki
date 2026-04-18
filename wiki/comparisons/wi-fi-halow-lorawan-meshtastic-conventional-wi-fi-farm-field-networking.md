---
title: Wi‑Fi HaLow vs LoRaWAN vs Meshtastic vs conventional Wi‑Fi — farm field networking
page_type: comparison
status: active
created: 2026-04-18
updated: 2026-04-18
tags:
  - halow
  - lorawan
  - meshtastic
  - wi-fi
  - farm
review_status: unreviewed
confidence: medium
aliases:
  - Four-way farm RF comparison HaLow LoRa Meshtastic Wi-Fi
---

# Wi‑Fi HaLow vs LoRaWAN vs Meshtastic vs conventional Wi‑Fi — farm field networking

## Question

How do **802.11ah (HaLow)**, **LoRaWAN**, **Meshtastic (LoRa mesh)**, and **conventional Wi‑Fi/Ethernet** compare for **farm field** use—throughput, range, power, deployment, and ops burden?

**Scope**: **Field layer** (sensors, local IP, backhaul to gateway)—not **WAN** (Starlink/LTE) except as **egress** attachment point.

**Related (off-grid ops framing)**: [`Meshtastic vs HaLow vs conventional Wi‑Fi — off-grid`](meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md). **LoRa stack detail**: [`LoRaWAN vs Meshtastic`](lorawan-vs-meshtastic-fixed-farm-telemetry.md).

---

## Summary matrix

| Criterion | Wi‑Fi HaLow (802.11ah) | LoRaWAN | Meshtastic (LoRa mesh) | Conventional Wi‑Fi / Ethernet |
|-----------|-------------------------|---------|-------------------------|-------------------------------|
| **Throughput** | **Highest** in this set for **IP** links (Mbps-class claims in vendor/article captures—**validate**) | **Very low** (duty-cycle, ADR) | **Low** (text/telemetry class) | **Highest** at short range |
| **Range** | **Sub-GHz** **long** **links** with **CPE/AP** **design** | **km-class** **possible** **with** **gateway** **planning** | **Multi-hop** **mesh** **without** **IP** **everywhere** | **Tens** **of** **m** **per** **AP** **(2.4/5** **GHz** **)** |
| **Power draw** | **AP/bridge** **continuous** **>** **LoRa** **sleeping** **nodes** | **Very** **low** **end** **devices** | **Low** **with** **sleep** **;** **higher** **when** **routing** | **High** **if** **many** **APs** |
| **IP-native** | **Yes** **(Wi‑Fi** **stack** **)** | **No** **(LPWAN** **;** **app** **layer** **)** | **No** **by** **default** **(**bridge** **at** **gateway** **)** | **Yes** |
| **Mesh suitability** | **Infrastructure** **mesh** **possible** **but** **not** **automatic** | **Star** **to** **gateway** | **Peer** **mesh** **native** | **Ethernet** **tree** **/** **Wi‑Fi** **ESS** |
| **Sensor suitability** | **Good** **when** **you** **need** **IP** **sensor** **or** **MQTT** **on** **MCU** | **Excellent** **for** **sparse** **telemetry** | **Excellent** **for** **sparse** **telemetry** | **Good** **barn** **dense** |
| **Backhaul suitability** | **Good** **for** **IP** **bridge** **to** **barn** | **Poor** **for** **fat** **pipes** | **Poor** **for** **fat** **pipes** | **Best** **with** **fiber** **/** **Ethernet** |
| **Deployment complexity** | **Medium** **—** **AP** **+** **antenna** **+** **reg** | **Medium** **—** **gateway** **+** **join** **model** | **Medium** **—** **map** **+** **keys** | **Low** **/** **well** **known** |
| **Maintenance burden** | **Patch** **AP** **firmware** **;** **RF** **debug** | **Gateway** **+** **NS** **provider** **if** **used** | **Firmware** **churn** **;** **mesh** **health** | **Patch** **Wi‑Fi** **;** **boring** **wins** |

---

## Operational notes

- **No single winner**: split **layers** per [`mesh strategy`](../analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md)—**LoRa/Meshtastic** for **sparse**, **HaLow** where **IP** **throughput** **matters**, **Ethernet** where **possible**.
- **Security**: HaLow is still **802.11**-family attack surface—**segment** and **patch** ([`segmentation`](../analyses/network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md)).

---

## Sources (vault)

- HaLow narrative / PoC: [`how-to 10x HaLow`](../../raw/processed/2026/how-to-10x-the-reach-of-wi-fi-devices-with-wi-fi-halow-802-11ah-inbox-2026-04-23.md), [`IEEE 802.11ah Wikipedia`](../source-notes/ieee-802-11ah-wikipedia.md)
- Off-grid index: [`off-grid power/RF source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md)
