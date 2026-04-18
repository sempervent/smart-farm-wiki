---
title: Field telemetry reference architecture — homestead + 120-acre farm
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-25
tags:
  - telemetry
  - architecture
  - mqtt
  - edge
review_status: unreviewed
confidence: low
---

# Field telemetry reference architecture — homestead + 120-acre farm

## Purpose

Provide a **single first-draft reference** for how **sensors, gateways, uplink, broker, and operator interfaces** could fit together across **`SITE_HOMESTEAD`** and **`SITE_FARM`**—without claiming this is your deployed stack. Use it to spot **single points of failure (SPOFs)**, **missing boundaries**, and **where truth lives** for events.

**Package hub** (5 ac + 120 ac framing, SoR, security): [`Reference architecture — 5-acre home base + 120-acre farm`](reference-architecture-5ac-homebase-120ac-smart-farm.md).

**Demory `SITE_FARM` sensor stack** (long-range RF, gateways, Starlink as WAN only): [`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md) · [`Sensor checklist matrix — Demory farm`](sensor-checklist-matrix-for-demory-farm.md).

**Integration / package boundary**: New RF/sensor/vendor ingests **activate** into the relevant **cluster source-notes** (Evidence summary) and the **Demory** pages above—not into this reference as a dump. **Platform** (broker, TSDB, k3s observability) routes through [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md) and [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md). **WAN/power** scheduling ties to [`Off-grid power and field networking hub`](../topics/off-grid-power-and-field-networking-hub.md) and backup/DR when telemetry affects restore order.

## Scope

- **In scope**: Logical blocks, data paths, **assumptions**, and **questions** for a split-site, partly instrumented farm.
- **Out of scope**: Vendor selection, exact SKUs, **network security hardening** (link to future cybersecurity hub); regulatory compliance.

## Assumptions (edit freely)

| Placeholder | Meaning |
|-------------|---------|
| `SITE_HOMESTEAD` | Smaller site; may host **home LAN**, **Home Assistant or equivalent**, **internet uplink**. |
| `SITE_FARM` | Larger parcel; may have **weak broadband**, **solar/battery field power**, **LoRa/Meshtastic/LoRaWAN** at edges. |
| `BROKER_LABEL` | MQTT broker (self-hosted or cloud)—**TBD**. |
| `SOR_TELEMETRY` | System that is **authoritative** for long-term sensor history—**TBD** (TSDB, DB, vendor cloud). |

## Roles: Home Assistant, farmOS, MQTT, TSDB (draft binding)

| Layer | Typical role | Conflicts when… |
|-------|----------------|-------------------|
| **MQTT broker** | **Transport** and pub/sub between devices and services | **Retained** vs **live** state misunderstood |
| **Home Assistant** | **Automation**, dashboards, **consumer** device hub at homestead | Treated as **legal** record for **tax** or **certification** without export |
| **farmOS** | **Structured** assets, logs, **geometry** (when used) | Out of **sync** with **field** reality if not updated |
| **TSDB / PostgreSQL** | **Durable** telemetry history / joins to **map** | **Duplicate** writes from HA and **direct** ingest—**need SoR rules** (see backlog P0 #6). |

**farmOS model refs**: [`farmOS Assets`](../source-notes/farmos-model-assets-documentation.md), [`farmOS Logs`](../source-notes/farmos-model-logs-documentation.md).

## Connects the strands

| Strand | Connection |
|--------|------------|
| **C** | Radio **choice** and **gateway** SPOFs—[`LoRaWAN vs Meshtastic`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md), [`Fixed gateway tower vs mobile`](../comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md). |
| **D** | farmOS + HA + DB—[`farmOS vs lightweight`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md), [`Data storage`](../concepts/data-storage.md). |
| **G** | **Time** for correlated logs—[`Time synchronization`](../topics/time-synchronization-ntp-and-ptp.md). |

## Reference diagram (logical, text)

```text
[ Field devices @ SITE_FARM ]     e.g. soil moisture, tank level, gate sensor, camera (placeholders)
        | radio path (LPWAN / Wi‑Fi / mesh — TBD)
        v
[ Edge gateway / concentrator @ SITE_FARM ]   power: `FIELD_POWER_ASSUMPTION`
        | backhaul (cell / fiber / point-to-point / mesh — TBD)
        v
[ IP network ] --------------------> [ BROKER_LABEL ] <---- subscriptions --- [ Operator UI / HA / phone ]
        |                                      ^
        |                                      |
[ SITE_HOMESTEAD LAN ] -------------------------+
   (VPN or same LAN if bridged — TBD)
```

**Not drawn**: **time sync** (NTP/PTP/GNSS)—see [`Time synchronization — NTP and PTP sources`](../topics/time-synchronization-ntp-and-ptp.md).

## Key questions

1. **If `SITE_FARM` uplink dies**, what is still true locally? (Cached automations? Gate state unknown?)
2. **Who is authoritative for “tank is low”**—broker last message, field node, or a **database** deduplicated state?
3. **Where do alerts originate**—broker rule engine, Home Assistant, external SaaS? (Avoid **three** alert channels with no priority.)
4. **Power**: Which edges are **battery + solar** vs **grid**? What happens after **`BATTERY_DAYS_AUTONOMY`** cloudy stretch?
5. **Admin access**: How do you **reach gateways** for updates without exposing **everything** to the public internet?

## SPOF checklist (fill in)

| Component | If it fails… | Mitigation idea (placeholder) |
|-----------|----------------|-------------------------------|
| Internet at `SITE_HOMESTEAD` | You may lose **remote** view of `SITE_FARM` | Local alerts on-site; **degraded mode** SOP |
| Broker `BROKER_LABEL` | All MQTT consumers blind | **HA queue / bridge** strategy; broker redundancy—**TBD** |
| Field gateway | Subtree of sensors dark | **Spare** gateway? **Radio path** diversity? |
| Time sync | Correlated logs wrong | GNSS/NTP strategy per [`Timing on the farm — synthesis`](timing-on-the-farm-synthesis.md) |

## Decision criteria

| Choice | Favor when | Avoid when |
|--------|------------|------------|
| **Concentrate gateways** at one mast | Clear line-of-sight, simpler power | Single lightning/wind **failure domain** |
| **Distributed gateways** | Terrain blocks RF; need **mesh** | More **firmware** surfaces to patch |
| **Cloud broker** | No ops capacity | **Latency**, **privacy**, **outage** sensitivity |

## Links to related future or existing pages

- [`Data storage (farm and edge stacks)`](../concepts/data-storage.md) — PostgreSQL/MQTT docs entry.
- [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md) — patterns and sources.
- [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md) — radio tradeoffs.
- [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md) — records vs telemetry.
- [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md) — **authority** matrix for records vs telemetry vs dashboards.
- [`Spatial data and farm asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) — bind **device IDs** to places.
- [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md) — behavior when this architecture **breaks**.

## Open items

- [ ] Replace placeholders with **one-page** network list: subnets, VPN, broker hostnames (even if private).
- [ ] Add **ASCII or exported** diagram when stable.
- [ ] Align **admin** paths with [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md).

---

*First draft: logical only; validate against a real diagram and an electrician/radio path survey before relying on it for safety.*
