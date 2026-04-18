---
title: Meshtastic
page_type: concept
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - meshtastic
  - lora
  - mesh
related_concepts:
  - concepts/lora-radio.md
  - concepts/lorawan.md
review_status: unreviewed
confidence: medium
---

# Meshtastic

**Meshtastic** is an open-source firmware ecosystem that uses **LoRa** radios to build decentralized, off-grid mesh networks for text, telemetry, and (with suitable hardware) position—typically without relying on cellular or internet backhaul for local peer relay. The shared physical layer is [`LoRa (radio)`](lora-radio.md); comparative LPWAN material (HaLow vs LoRa vs NB-IoT) lives under [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md).

In this wiki, Meshtastic appears alongside **LoRaWAN**-style star/topology deployments: Meshtastic emphasizes device-to-device mesh relay, while many farm sensor platforms use gateways and network servers (see [`LoRaWAN`](lorawan.md)).

**Grounded sources**

- [`source-notes/meshtastic-nodes-basics-deployment-seeed.md`](../source-notes/meshtastic-nodes-basics-deployment-seeed.md)
- [`source-notes/building-solar-powered-meshtastic-community-network.md`](../source-notes/building-solar-powered-meshtastic-community-network.md)
- [`source-notes/how-to-build-solar-meshtastic-node-easy-way.md`](../source-notes/how-to-build-solar-meshtastic-node-easy-way.md)
- [`source-notes/solar-meshtastic-gps-esp32-outdoor.md`](../source-notes/solar-meshtastic-gps-esp32-outdoor.md)

**Related**

- [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md)
- [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md)
