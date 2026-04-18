---
title: Tracking chickens with motion sensors over LoRa and MQTT (query synthesis)
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
source_ids:
  - raw/processed/2026/openmqttgateway-theengs-lora-gateway-v1-8-1.md
  - raw/processed/2026/home-assistant-lora-long-range-sensors-mqtt-exploration.md
  - raw/processed/2026/lorawan-mqtt-integration-iot-application-design-hivemq.md
tags:
  - lora
  - mqtt
  - poultry
  - sensors
confidence: medium
---

# Tracking chickens with motion sensors over LoRa and MQTT (query synthesis)

**Question**: How can you **track chickens** using **motion sensors** over **LoRa**, delivered to automation via **MQTT**?

**Scope note**: “Tracking” here usually means **activity**, **occupancy**, or **door/run presence** heuristics—not per-bird GPS—unless you add **RFID leg bands**, **BLE tags**, or cameras (not covered in the cited LoRa/MQTT batch).

## Recommended architecture (MQTT-centric)

1. **Edge node (coop/run)**  
   - **PIR** (or **mmWave** radar for fewer false trips) + **MCU** (e.g. ESP32-class) + **LoRa radio**.  
   - Firmware **debounces** motion, aggregates events (e.g. motion count per 5–15 minutes), sends **small binary/JSON payloads** on trigger or timer to save battery.

2. **Radio path** (pick one):  
   - **Plain LoRa** to a **gateway** that speaks MQTT — patterns in [`OpenMQTTGateway` LoRa gateway notes](../../raw/processed/2026/openmqttgateway-theengs-lora-gateway-v1-8-1.md) (subscribe/publish between LoRa and MQTT topics) and the **Home Assistant exploration** of **ESP32 + SX1276** point-to-point links ([`home-assistant-lora-long-range-sensors-mqtt-exploration.md`](../../raw/processed/2026/home-assistant-lora-long-range-sensors-mqtt-exploration.md)).  
   - **LoRaWAN** end-device → **network/application server** → **MQTT** uplink topics, as in the **LoRaWAN + MQTT integration** overview ([`lorawan-mqtt-integration-iot-application-design-hivemq.md`](../../raw/processed/2026/lorawan-mqtt-integration-iot-application-design-hivemq.md)) and **MultiTech**-style `lora/<DEV-EUI>/...` topic patterns ([`multitech-developer-resources-mqtt-messages-lora-topics.md`](../../raw/processed/2026/multitech-developer-resources-mqtt-messages-lora-topics.md)).

3. **Broker + automation**  
   - **Mosquitto** / cloud broker; **Home Assistant** MQTT integration or **Node-RED** to turn topics into entities, alerts, or history charts.

## Chicken-specific practical constraints

- **False positives**: wind, rodents, swinging feeders, and **door movement** can trigger PIR; consider **radar**, **beam break** at pop-hole height, or **two sensors** with simple logic.  
- **Duty cycle / rate limits**: **LoRaWAN** public networks often restrict how often nodes may transmit; bursty motion may need **edge aggregation** (count pulses locally, send summaries).  
- **What you learn**: sustained motion overnight might indicate **predator stress** or **thermal huddling**; midday spikes may be **dust bathing**—interpretation needs baselines (**confidence: low** without controlled experiments).

## Meshtastic and MQTT

A **Meshtastic** **MQTT** integration thread ([`meshtastic-lora-mqtt-bridge-reddit-thread.md`](../../raw/processed/2026/meshtastic-lora-mqtt-bridge-reddit-thread.md)) discusses **mesh ↔ MQTT** bridging and **default forwarding policy** (e.g. **0-hop** constraints). That stack is **messaging/telemetry-oriented** for the mesh ecosystem; for **structured HA sensor** flows, **OpenMQTTGateway**, **custom gateways**, or **LoRaWAN application MQTT** are typically simpler fits—see topic [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md).

## Where to read next

- Topic hub: [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md)  
- Livestock context: [`Backyard livestock and homestead animal sources`](../topics/backyard-livestock-and-homestead-animals.md)
