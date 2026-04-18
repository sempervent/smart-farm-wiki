---
title: "Source note: A deep look at Wi‑Fi HaLow vs LoRaWAN (Newracom)"
page_type: source_note
status: active
created: 2026-04-17
updated: 2026-04-17
source_ids:
  - raw/processed/2026/a-deep-look-at-wi-fi-halow-and-lorawan.md
tags:
  - wi-fi-halow
  - lorawan
  - lpwan
review_status: unreviewed
---

# Source note: A deep look at Wi‑Fi HaLow vs LoRaWAN (Newracom)

**Raw path:** [`raw/processed/2026/a-deep-look-at-wi-fi-halow-and-lorawan.md`](../../raw/processed/2026/a-deep-look-at-wi-fi-halow-and-lorawan.md)

**Summary**

Vendor blog comparing **LPWAN** positioning of **IEEE 802.11ah / Wi‑Fi HaLow** and **LoRaWAN**: throughput vs range tradeoffs, sub-GHz penetration, scalability claims (including references to academic work on LoRaWAN packet delivery under load), security framing (WPA3 vs LoRaWAN keying), ecosystem maturity, and example applications (video, signage, industrial IoT). Includes marketing links and competitive claims—corroborate independently.

**Claims worth carrying forward**

- HaLow is IP-based Wi‑Fi family tooling; LoRaWAN is typically gateway + network server star architecture.
- Practical LoRaWAN scalability can degrade at high device counts / long airtime due to collisions and duty cycle—application dependent.

**Downstream pages**

- [`Wi-Fi HaLow`](../concepts/wi-fi-halow.md), [`LoRa (radio)`](../concepts/lora-radio.md), [`LoRaWAN`](../concepts/lorawan.md)
- [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md)
