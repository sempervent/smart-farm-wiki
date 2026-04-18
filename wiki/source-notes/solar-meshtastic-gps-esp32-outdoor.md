---
title: "Source note: Solar Meshtastic GPS node on ESP32 — power and mesh behavior"
page_type: source_note
status: active
created: 2026-04-17
updated: 2026-04-17
source_ids:
  - raw/processed/2026/solar-meshtastic-gps-node-esp32-long-term-outdoor.md
tags:
  - meshtastic
  - esp32
  - gps
  - solar
review_status: unreviewed
---

# Source note: Solar Meshtastic GPS node on ESP32 — power and mesh behavior

**Raw path:** [`raw/processed/2026/solar-meshtastic-gps-node-esp32-long-term-outdoor.md`](../../raw/processed/2026/solar-meshtastic-gps-node-esp32-long-term-outdoor.md)

**Summary**

Short build/field-test notes (Reddit/thread excerpt style): ESP32 + SX1276 LoRa + OLED + GPS with ~2500 mAh battery and small 3.7 V solar panel; order-of-magnitude active vs duty-cycled current; reliance on Meshtastic sleep/duty cycling for multi-day runtime; informal experiment where two “office” nodes query a third GPS node—observed staggered replies consistent with mesh broadcast/retry behavior. Includes comment thread note about TP4056-class charging.

**Claims worth carrying forward**

- GPS + ESP32 Meshtastic builds are power-hungry without aggressive sleep scheduling.
- Multi-node queries on a mesh can produce non-deterministic response ordering/timeouts—design UX and diagnostics accordingly.

**Downstream pages**

- [`Meshtastic`](../concepts/meshtastic.md)
- [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md)
