---
title: LoRaWAN
page_type: concept
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - lorawan
  - lpwan
  - agriculture
related_concepts:
  - concepts/lora-radio.md
  - concepts/meshtastic.md
  - concepts/precision-agriculture.md
review_status: unreviewed
confidence: medium
---

# LoRaWAN

**LoRaWAN** is a low-power wide-area networking stack built on **LoRa** physical-layer modulation (see [`LoRa (radio)`](lora-radio.md)), commonly used for long-range, battery-operated sensors that talk through **gateways** to application backends.

For agriculture, LoRaWAN is frequently positioned for soil moisture, microclimate, irrigation, and livestock monitoring—often as part of vendor “end-to-end” IoT offerings. Treat vendor range, lifetime, and ROI figures as **claims** and validate for your region and deployment class.

**Grounded sources**

- [`source-notes/lorawan-farmers-money-yields-tektelic.md`](../source-notes/lorawan-farmers-money-yields-tektelic.md)
- [`source-notes/semtech-lora-smart-agriculture-applications.md`](../source-notes/semtech-lora-smart-agriculture-applications.md)
- [`source-notes/lora-wikipedia.md`](../source-notes/lora-wikipedia.md)

**Contrasts**

- **Meshtastic** (see [`Meshtastic`](meshtastic.md)) typically targets mesh peer relay for local comms; LoRaWAN targets managed star-of-stars sensor uplinks.

**Related**

- [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md)
- [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md)
