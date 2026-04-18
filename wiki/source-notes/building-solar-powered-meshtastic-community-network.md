---
title: "Source note: Building a solar-powered LoRa Meshtastic community network"
page_type: source_note
status: active
created: 2026-04-17
updated: 2026-04-17
source_ids:
  - raw/processed/2026/building-a-solar-powered-lora-meshtastic-community-network.md
tags:
  - meshtastic
  - lora
  - solar
review_status: unreviewed
---

# Source note: Building a solar-powered LoRa Meshtastic community network

**Raw path:** [`raw/processed/2026/building-a-solar-powered-lora-meshtastic-community-network.md`](../../raw/processed/2026/building-a-solar-powered-lora-meshtastic-community-network.md)

**Summary**

Blog-style piece on designing solar Meshtastic repeater infrastructure: Heltec WiFi LoRa 32 (v3) vs RAK4631 power tradeoffs, EU-oriented airtime assumptions (~0.1 W average for ESP32 without BT/screen/GPS), sizing panels and 18650 charging (rule of thumb ~10 Wp per 10 Wh for ~3 h full recharge), CN3791/CN3163/TP4056 charge-controller notes, regulator dropout affecting usable battery capacity, and measured Heltec + INA219 router consumption (~0.046 W at 5% airtime). Warns that a particular 4 W panel’s protection IC may sit on the solar path only—battery-side undervoltage protection may still be required.

**Claims worth carrying forward**

- Repeater role extends coverage without advertising presence; pairing a `SENSOR` node on shared power can surface repeater health while keeping the repeater “invisible.”
- Solar sizing must respect cell max charge current, not just panel wattage.
- Community references: MQTT-backed node maps, regional deployments (e.g. Ukraine 433 MHz mesh), Austin Mesh, Iffy Books resources.

**Downstream pages**

- [`Meshtastic`](../concepts/meshtastic.md)
- [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md)
