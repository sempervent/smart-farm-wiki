---
title: RF and telemetry gateway roles — field network
page_type: entity
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - gateway
  - lora
  - mqtt
  - telemetry
aliases:
  - Field gateway LoRa to MQTT
confidence: medium
review_status: unreviewed
---

# RF and telemetry gateway roles — field network

## Purpose

Separate **field** “gateway” ( **RF → IP** / **MQTT** aggregation, buffering) from **WAN** customer-premises equipment—both are “gateways” in English but have different **failure modes**, **power tiers**, and **backup** implications.

## Scope

- **In scope**: Logical roles (fixed tower vs mobile, bridge to broker, local buffer when cloud absent).
- **Out of scope**: Specific vendor stacks unless cited as examples on comparison pages.

## Knowns

- The two-site stack treats **broker path** and **SoR** authority as first-class—see field telemetry entity and SoR analysis.
- Comparisons exist for **fixed vs mobile** and **LoRaWAN vs Meshtastic** for fixed telemetry.

## Assumptions

- At least one **G-class** spine exists where the doctrine applies—see [`Field node classes (G/R/S/H/W)`](field-node-classes-off-grid-farm-roles.md).

## Related analyses

- [`Field telemetry reference architecture — homestead + 120-acre farm`](../analyses/field-telemetry-reference-architecture-homestead-120ac.md)
- [`Telemetry system of record — boundaries and authority`](../analyses/telemetry-system-of-record-boundaries-and-authority.md)
- [`Fixed gateway tower vs mobile or vehicle gateway`](../comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md)
- [`LoRaWAN vs Meshtastic for fixed farm telemetry`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md)

## Related topics

- [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md) (ingest router; not a source note)

## Related source notes

- None required at entity level; see ingests linked from the topic above when a claim needs `raw/` grounding.

## Outstanding unknowns

- **Which** RF families are in play per paddock after pilot (mesh vs LoRaWAN vs HaLow segment)—deployment decision, not wiki-invented.
