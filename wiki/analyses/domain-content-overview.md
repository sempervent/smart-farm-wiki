---
title: Domain content overview (Smart Farm Wiki)
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-18
review_status: unreviewed
tags:
  - domain
  - meta-synthesis
confidence: medium
---

# Domain content overview (Smart Farm Wiki)

This page **characterizes the subject-matter footprint** of this vault—not tooling or CI (see [`Repository analysis`](repository-analysis.md)). It is a **synthesis of how topics cluster** so readers and agents can navigate by **intent** (land use, connectivity, power, data, business, dwelling) rather than by folder name alone.

**Epistemic stance**: Most claims are **grounded in source-notes** pointing at `raw/processed/` imports; density and quality vary by batch. This overview does **not** assert agronomic, legal, or electrical prescriptions—it **maps what the wiki already holds**.

## North star

The corpus mixes **small-scale agriculture and homestead practice** with **instrumentation, networks, and automation** that could support monitoring, telemetry, or edge compute on a farm or in a lab. A useful mental model is **three overlapping rings**:

1. **Land and living systems** — soil, water, crops, livestock, ponds, regional gardening.
2. **Energy and infrastructure** — off-grid solar, storage sizing, pumps and hydrology, time sync where “infrastructure” includes clocks.
3. **Digital layer** — LPWAN and mesh radios, MQTT bridges, MCUs (ESP32), farm records (farmOS), homelab patterns that mirror edge operations.

Not every page sits in all three rings; many **source-notes** are single-import anchors waiting for denser synthesis.

## Strand A — Land, water, and biological production

**Themes**: Rotations and cover crops, sustainable cropping primers, hobby-farm and backyard livestock (poultry, cattle excerpts), pond construction and stocking, irrigation adjacency, horse-at-home basics.

**Hubs**

- [`Sustainable cropping, soil, and farm entry sources`](../topics/sustainable-cropping-soil-and-farm-entry-sources.md)
- [`Homestead and regional gardening sources`](../topics/homestead-and-regional-gardening-sources.md)
- [`Backyard livestock and homestead animal sources`](../topics/backyard-livestock-and-homestead-animals.md)
- [`Ponds, water features, and homestead hydrology`](../topics/ponds-water-features-and-homestead-hydrology.md)

**Concept anchor**

- [`Precision agriculture`](../concepts/precision-agriculture.md) — formal PA framing vs smallholder practice (Wikipedia-sourced note).

**Example analyses**

- [`Starting and stocking a pond — beautiful water feature`](starting-stocking-pond-beautiful-water-feature.md)
- [`Farm stocking — 120 acres vs 5 acres (research prompt)`](farm-stocking-120-acres-vs-5-acres-research-prompt.md) — forward-looking research brief, not settled doctrine.
- [`Long 360 tractor — no-start troubleshooting (synthesis)`](long-360-tractor-no-start-synthesis.md) — diesel utility tractor; web-sourced forum/manual pointers
- [`Ducks vs chickens — meat raising`](../comparisons/ducks-vs-chickens-meat-raising.md) — meat poultry comparison (ingested inbox sources)

## Strand B — Regional business, diversification, and shelter

**Themes**: Hobby-farm definitions, beginning-farmer programs (excerpts), **Tennessee**-leaning business checklists and licensing notes, agritourism revenue ideas, tiny-house and natural-building narratives where they intersect farm stays.

**Hubs**

- [`Tennessee hobby farm and small-farm business sources`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md)
- [`Agritourism, tiny housing, and natural building sources`](../topics/agritourism-tiny-housing-and-natural-building.md)

**Example analyses**

- [`Agritourism, tiny houses, Tennessee hobby farms`](agritourism-tiny-houses-tennessee-hobby-farm.md)
- [`Agritourism smart hobby farm — tiny houses and guest work stays`](agritourism-smart-hobby-farm-tiny-houses-guest-work-stays.md)

**Caveat**: Regulatory and tax content is **excerpt-level**; treat as pointers for professional advice, not compliance guidance.

## Strand C — Field and barn connectivity (LPWAN, mesh, Wi‑Fi HaLow)

**Themes**: LoRa PHY vs LoRaWAN vs Meshtastic mesh; vendor and Wikipedia comparisons; MQTT integration patterns; solar-powered repeater / node deployments; cellular LPWAN contrast.

**Hubs**

- [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md)
- [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md)
- [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md)

**Concepts**

- [`LoRa (radio)`](../concepts/lora-radio.md), [`LoRaWAN`](../concepts/lorawan.md), [`Meshtastic`](../concepts/meshtastic.md), [`Wi-Fi HaLow`](../concepts/wi-fi-halow.md)
- [`Decentralized physical infrastructure networks (DePIN)`](../concepts/depin.md) — adjacent token/incentives framing where cited.

**Example analysis**

- [`Tracking chickens — motion sensors over LoRa and MQTT`](tracking-chickens-motion-lora-mqtt.md) — bridges Strand A and Strand C.

## Strand D — Edge devices and farm-adjacent compute

**Themes**: ESP32 in IoT and “smart farming” README-style captures, ESPHome displays, comparison threads; farmOS as a structured record-keeping stack; agriculture homelab build narratives.

**Hubs**

- [`ESP32, ESPHome, and smart-farming builds`](../topics/esp32-iot-smart-farming-and-tooling.md)
- [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md)
- [`Homelab, self-hosting, and edge narratives`](../topics/homelab-self-hosting-and-edge-narratives.md)
- [`Docker, Kubernetes, Compose, and Bake (edge and homelab)`](../topics/docker-kubernetes-compose-and-bake.md)

**Concept**

- [`ESP32`](../concepts/esp32.md)

## Strand E — Power and site energy

**Themes**: Off-grid solar sizing narratives, battery bank calculators (excerpts), EcoFlow-style integrated kits, homestead wiring articles, remote field power for sensors.

**Hub**

- [`Off-grid solar power and storage (special topic)`](../topics/off-grid-solar-power-and-storage.md)

## Strand F — Building automation, displays, and consumer IoT

**Themes**: Matter/Thread and Home Assistant AI survey material; Magic Mirror and e-paper display builds—**not** agronomic core, but present as **home/ops** overlap (dashboards, alerts, UX for monitoring).

**Hubs**

- [`Smart home — Matter, Thread, and Home Assistant AI (special topic)`](../topics/smart-home-matter-thread-and-home-assistant-ai.md)
- [`Smart mirror and e-paper display builds`](../topics/smart-mirror-and-e-paper-displays.md)

## Strand G — Time, position, and resilient references

**Themes**: NTP and PTP primers, GNSS-disciplined Pi builds, GPS-alternative and PNT-adjacent articles—relevant where sensor networks need **coherent timestamps** or where positioning threads appear in imports.

**Hubs**

- [`Time synchronization — NTP and PTP sources`](../topics/time-synchronization-ntp-and-ptp.md)
- [`Position, navigation, and timing alternatives`](../topics/position-navigation-and-timing-alternatives.md)

**Synthesis**

- [`Timing on the farm — synthesis`](timing-on-the-farm-synthesis.md) — Bridges agronomic/labor timing with technical clocking.

**Concepts**

- [`Network Time Protocol (NTP)`](../concepts/network-time-protocol.md), [`Precision Time Protocol (PTP)`](../concepts/precision-time-protocol.md)

## Gaps and growth directions

- **Integration pages** that explicitly tie **soil/crop decisions** to **sensor placement** or **data model** (farmOS fields vs real paddocks) are still sparse compared to the volume of **standalone source-notes**.
- **Comparisons** beyond [`Raw vs wiki`](../comparisons/raw-vs-wiki.md) could grow (e.g. LoRaWAN vs Meshtastic for a fixed use case) when backed by new ingests.
- **Regional scope**: Several business and gardening notes skew **Tennessee / southeastern US**; other regions need parallel sources before generalizing.

## How to navigate

- **Broad map of domain entry points**: [`Knowledge synthesis`](../topics/knowledge-synthesis.md)
- **Vault mechanics**: [`Repository analysis`](repository-analysis.md)
- **Catalog**: [`index.md`](../index.md)

---

*Update this page when major new topic hubs land or when the domain focus of the vault shifts.*
