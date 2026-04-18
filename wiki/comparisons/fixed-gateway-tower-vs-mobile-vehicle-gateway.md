---
title: Fixed gateway tower vs mobile or vehicle gateway
page_type: comparison
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - gateway
  - lora
  - telemetry
review_status: unreviewed
confidence: medium
---

# Fixed gateway tower vs mobile or vehicle gateway

## Question

For **LPWAN backhaul** from a **large parcel**, do you invest in a **fixed mast / tower** gateway with **wired or stable uplink**, or rely on a **vehicle-mounted** gateway that **bridges** when present?

## Criteria

| Criterion | Fixed tower / barn gateway | Mobile / vehicle gateway |
|-----------|----------------------------|---------------------------|
| **Coverage** | **Persistent** RF hearability if sited well | **Intermittent**; good for **sweeps** or **herding** workflows |
| **Backhaul** | Fiber/cellular **fixed** (if available) | **Hotspot** or **return to yard Wi‑Fi** |
| **SPOF** | Lightning, **power**, **theft** at remote shed | **Crash**, **forget to enable**, **battery** |
| **OPEX** | **Internet** + **power** + **maintenance** climb | Fuel, **human** time, **mount** wear |
| **Best when** | **Always-on** telemetry (tanks, pumps, gates) | **Periodic** rounds; **mesh** gap-fill |

## Tradeoff summary

- **Fixed** wins for **24/7** situational awareness; **mobile** wins for **sparse** coverage extension without **tower** CAPEX.
- **Split sites**: a **fixed** gateway at **`SITE_FARM`** may still need **VPN** or **MQTT** to **`SITE_HOMESTEAD`**—see [`Field telemetry reference architecture — homestead + 120-acre farm`](../analyses/field-telemetry-reference-architecture-homestead-120ac.md).

## Links

- [`LoRaWAN vs Meshtastic for fixed farm telemetry`](lorawan-vs-meshtastic-fixed-farm-telemetry.md)
- [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md)
- [`Gateway architecture — fixed tower vs vehicle vs mesh`](../analyses/implementation-backlog-strategic-audit.md) *(title in backlog P2 #17—this page implements the comparison)*

---

*Tower safety, zoning, and **guying** are out of scope—use qualified installers.*
