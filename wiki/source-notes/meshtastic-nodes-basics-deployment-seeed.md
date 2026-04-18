---
title: "Source note: Meshtastic nodes — basics and deployment (Seeed Studio guide)"
page_type: source_note
status: active
created: 2026-04-17
updated: 2026-04-17
source_ids:
  - raw/processed/2026/the-complete-guide-to-meshtastic-nodes-basics-and-deployment.md
tags:
  - meshtastic
  - deployment
review_status: unreviewed
---

# Source note: Meshtastic nodes — basics and deployment (Seeed Studio guide)

**Raw path:** [`raw/processed/2026/the-complete-guide-to-meshtastic-nodes-basics-and-deployment.md`](../../raw/processed/2026/the-complete-guide-to-meshtastic-nodes-basics-and-deployment.md)

**Summary**

Long-form introduction aimed at deployers: hardware stack (LoRa chip e.g. SX1262, MCU ESP32 vs nRF52840, antenna, power), detailed Meshtastic **roles** (Client, Client Mute, Client Base, Router, Router Late, Repeater, Sensor) and how mis-set Routers can harm mesh performance, using public node maps before adding infrastructure, range factors (band, antenna, elevation, environment, legal power limits), solar/off-grid framing with SenseCAP Solar Node examples, kit vs DIY tradeoffs, and common mistakes (placement, antenna, region settings, redundant routers, solar undersizing, transmitting without antenna).

**Claims worth carrying forward**

- Role selection and map-based planning are first-class “ops” concerns—not only hardware.
- Repeater = silent relay; Sensor = periodic telemetry—useful patterns for unattended field installs.

**Downstream pages**

- [`Meshtastic`](../concepts/meshtastic.md)
- [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md)
