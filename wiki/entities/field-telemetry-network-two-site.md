---
title: Field telemetry network — two-site
page_type: entity
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - telemetry
  - mqtt
  - lora
  - two-site
aliases:
  - Two-site field telemetry stack
confidence: medium
review_status: unreviewed
---

# Field telemetry network — two-site

**What this entity is**: The **logical system** connecting **field devices** at **`SITE_FARM`** (and sometimes **`SITE_HOME`**) to **gateways**, **backhaul**, **MQTT broker**, **consumers** ([`Home Assistant`](home-assistant.md), DB, alerts), and **records**—as **one** cross-cutting stack, regardless of whether radios are LoRaWAN, mesh, or Wi‑Fi.

**Why it matters**: Splitting discussion only by **radio** without **broker / SoR / security** context produces **sideways** analyses; this entity is the **anchor** for “the **whole** path.”

**Canonical analyses**

- Package map: [`Reference architecture — 5-acre home base + 120-acre farm`](../analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md)
- Stack detail: [`Field telemetry reference architecture — homestead + 120-acre farm`](../analyses/field-telemetry-reference-architecture-homestead-120ac.md)
- Authority: [`Telemetry system of record — boundaries and authority`](../analyses/telemetry-system-of-record-boundaries-and-authority.md)

**Gateway classes** (tradeoffs, not one vendor): [`Fixed gateway tower vs mobile or vehicle gateway`](../comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md), [`LoRaWAN vs Meshtastic for fixed farm telemetry`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md).

**Does not claim**: Your broker hostname, VLAN layout, or chosen radio—**placeholders** stay in architecture pages until deployed.

**Related**

- [`farmOS`](farmos.md) — agronomic **records** side of the same data story
- Glossary: [`System of record (farm data)`](../glossary/system-of-record-farm-data.md)
