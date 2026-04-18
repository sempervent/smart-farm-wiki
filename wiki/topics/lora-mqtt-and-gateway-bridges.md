---
title: LoRa, MQTT, and gateway bridges
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-21
tags:
  - lora
  - mqtt
  - gateway
  - home-assistant
review_status: unreviewed
---

# LoRa, MQTT, and gateway bridges

**Narrative**: **MQTT** is the usual **pub/sub** handoff from edge radios to **Home Assistant**, **Node-RED**, or cloud analytics. This hub collects **three patterns**: (1) **LoRaWAN → application server → MQTT** (vendor/blog and **MultiTech** topic docs), (2) **raw LoRa ↔ MQTT gateways** (**OpenMQTTGateway**, **ezcGman** DIY bridge, **MQTT Manager** “poor man” pairs), and (3) **Meshtastic ↔ MQTT** **policy** discussion (default **0-hop** behavior and when traffic returns to **LoRa**). A **Home Assistant** community write-up explores **ESP32 + SX1276** point-to-point **LoRa** to extend sensors beyond Wi‑Fi/Zigbee.

Together, these sources support designs where **battery nodes** in a **coop, run, or field** send **small payloads** to a **broker**—see [`Tracking chickens with motion sensors over LoRa and MQTT (query synthesis)`](../analyses/tracking-chickens-motion-lora-mqtt.md) for a livestock-oriented application sketch.

**Source notes**

- [`source-notes/multitech-developer-resources-mqtt-messages-lora-topics.md`](../source-notes/multitech-developer-resources-mqtt-messages-lora-topics.md)
- [`source-notes/meshtastic-lora-mqtt-bridge-reddit-thread.md`](../source-notes/meshtastic-lora-mqtt-bridge-reddit-thread.md)
- [`source-notes/home-assistant-lora-long-range-sensors-mqtt-exploration.md`](../source-notes/home-assistant-lora-long-range-sensors-mqtt-exploration.md)
- [`source-notes/mqtt-manager-lora-poor-man-gateway-instructables.md`](../source-notes/mqtt-manager-lora-poor-man-gateway-instructables.md)
- [`source-notes/lorawan-mqtt-integration-iot-application-design-hivemq.md`](../source-notes/lorawan-mqtt-integration-iot-application-design-hivemq.md)
- [`source-notes/ezcgman-lora-to-mqtt-gateway-esp32-ebyte.md`](../source-notes/ezcgman-lora-to-mqtt-gateway-esp32-ebyte.md)
- [`source-notes/openmqttgateway-theengs-lora-gateway-v1-8-1.md`](../source-notes/openmqttgateway-theengs-lora-gateway-v1-8-1.md)

**Related**

- [`Data storage (farm and edge stacks)`](../concepts/data-storage.md) — MQTT specification links and how messaging fits beside **PostgreSQL**/PostGIS
- [`Smart agriculture, Meshtastic, and LoRaWAN`](smart-agriculture-meshtastic-and-lorawan.md) — LPWAN field context; distinct from **plain LoRa** bridges
- [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](field-network-iot-comparisons.md) — when LPWAN vs other backhauls
- [`ESP32, ESPHome, and smart-farming builds`](esp32-iot-smart-farming-and-tooling.md) — MCU nodes at the **sensor** side
- [`Backyard livestock and homestead animal sources`](backyard-livestock-and-homestead-animals.md) — husbandry context for coop/run sensing goals
- [`Smart home — Matter, Thread, and Home Assistant AI (special topic)`](smart-home-matter-thread-and-home-assistant-ai.md) — HA as **MQTT** consumer
