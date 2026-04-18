---
title: "Source note: Long-range “internet” over LoRa? (Raspberry Pi forums)"
page_type: source_note
status: active
created: 2026-04-17
updated: 2026-04-17
source_ids:
  - raw/processed/2026/long-range-internet-using-lora-raspberry-pi-forums.md
tags:
  - lora
  - forums
review_status: unreviewed
---

# Source note: Long-range “internet” over LoRa? (Raspberry Pi forums)

**Raw path:** [`raw/processed/2026/long-range-internet-using-lora-raspberry-pi-forums.md`](../../raw/processed/2026/long-range-internet-using-lora-raspberry-pi-forums.md)

**Summary**

Forum thread (2020) asking whether **LoRa** can support general **web browsing** across ~10 km; replies emphasize **spread factor vs throughput** tradeoffs, realistic **bytes/sec** expectations, regulatory constraints (Japan example), and alternatives (directional **Wi‑Fi**/microwave links). Community anecdote—not engineering sign-off.

**Claims worth carrying forward**

- High SF for range collapses effective throughput; “HTML pages” can still imply large assets unless stripped/blocked.
- Point-to-point IP expectations map poorly to typical LoRaWAN duty cycles and packet models.

**Downstream pages**

- [`LoRa (radio)`](../concepts/lora-radio.md)
- [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md)
