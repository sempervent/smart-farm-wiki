---
title: Smart agriculture, Meshtastic, and LoRaWAN
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-20
tags:
  - agriculture
  - meshtastic
  - lorawan
review_status: unreviewed
---

# Smart agriculture, Meshtastic, and LoRaWAN

This topic bundles **field-scale IoT** patterns where long-range, low-power RF matters: **LoRaWAN** sensor-to-gateway deployments common in precision agriculture, and **Meshtastic** mesh nodes used for off-grid comms, environmental telemetry, and solar “infrastructure” radios around farms, ranches, and rural communities.

For **radio stack comparisons** (HaLow vs LoRa vs NB-IoT) and **DePIN**-adjacent LPWAN notes, see [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](field-network-iot-comparisons.md). For **MCU-side sensors and displays** often paired with gateways or local automation, see [`ESP32, ESPHome, and smart-farming builds`](esp32-iot-smart-farming-and-tooling.md).

**Concepts**

- [`Meshtastic`](../concepts/meshtastic.md)
- [`LoRaWAN`](../concepts/lorawan.md)
- [`Precision agriculture`](../concepts/precision-agriculture.md)

**Source notes (ingested 2026-04-17)**

- [`source-notes/building-solar-powered-meshtastic-community-network.md`](../source-notes/building-solar-powered-meshtastic-community-network.md)
- [`source-notes/how-to-build-solar-meshtastic-node-easy-way.md`](../source-notes/how-to-build-solar-meshtastic-node-easy-way.md)
- [`source-notes/meshtastic-nodes-basics-deployment-seeed.md`](../source-notes/meshtastic-nodes-basics-deployment-seeed.md)
- [`source-notes/solar-meshtastic-gps-esp32-outdoor.md`](../source-notes/solar-meshtastic-gps-esp32-outdoor.md)
- [`source-notes/lorawan-farmers-money-yields-tektelic.md`](../source-notes/lorawan-farmers-money-yields-tektelic.md)
- [`source-notes/semtech-lora-smart-agriculture-applications.md`](../source-notes/semtech-lora-smart-agriculture-applications.md)
- [`source-notes/precision-agriculture-wikipedia.md`](../source-notes/precision-agriculture-wikipedia.md)
- [`source-notes/remote-sensing-crop-mapping-rse-review.md`](../source-notes/remote-sensing-crop-mapping-rse-review.md) — RSE review: crop **land cover** products and remote sensing (large academic capture).

**Related topics**

- [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md) — LPWAN / HaLow comparisons and reference articles
- [`ESP32, ESPHome, and smart-farming builds`](../topics/esp32-iot-smart-farming-and-tooling.md) — ESP32 / ESPHome and smart-farming firmware next to RF deployments
- [`Homestead and regional gardening sources`](../topics/homestead-and-regional-gardening-sources.md) — small-farm and regional gardening raw references
- [`Off-grid solar power and storage (special topic)`](../topics/off-grid-solar-power-and-storage.md) — general PV/battery sizing for solar repeaters and field power (distinct from LoRa RF design)
- [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md) — farm **records/planning** software and ag-lab automation context adjacent to sensor deployments
- [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md) — **MQTT** as the app layer for **LoRa/LoRaWAN** sensor uplinks
