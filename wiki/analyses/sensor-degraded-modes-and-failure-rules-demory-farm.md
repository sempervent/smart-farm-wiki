---
title: Sensor degraded modes and failure rules — Demory farm site
page_type: analysis
status: active
created: 2026-04-25
updated: 2026-04-25
tags:
  - demory
  - sensors
  - degraded-mode
review_status: unreviewed
confidence: medium
---

# Sensor degraded modes and failure rules — Demory farm site

**Purpose**: Explicit failure semantics for field telemetry on Demory: what still works when WAN, gateway, or RF degrades, and what must never be inferred from stale MQTT alone.

**Parent architecture**: [`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md).

**Power / connectivity doctrine**: [`Off-grid degraded modes — power and connectivity (Demory)`](off-grid-degraded-modes-power-and-connectivity-demory-farm.md) · [`Connectivity dependency map — farm systems (Demory)`](connectivity-dependency-map-farm-systems-demory-farm.md).

---

## Failure classes (sensor-relevant)

| Mode | Symptom | Allowed operator inference | Not allowed |
|------|---------|---------------------------|-------------|
| **D1 — WAN loss** (Starlink/LTE) | No remote Claxton visibility | Local broker / farm UI still authoritative for what they hold | Assume cloud == field truth |
| **D2 — Broker unreachable** | Automation / HA partition | Physical verification; local logs on controller | Act on “last MQTT” for welfare without sight |
| **D3 — LoRaWAN GW impaired** | Subset of sensors silent | Geographic hole hypothesis; rotate rounds | Assume sensor == OK |
| **D4 — Mesh partition** | Meshtastic islands | Treat as comms loss; local text within island | Merge routing state across partition without rejoin |
| **D5 — Power shed** | Non-Pcrit RF off | Manual priority list per stop rules | Starlink before gateway battery policy—wrong order |

---

## Rules (normative for wiki operations design)

1. Welfare and safety interlocks must not traverse WAN only ([`Connectivity dependency map`](connectivity-dependency-map-farm-systems-demory-farm.md)).
2. Alert floods → [`Runbook — sensor false-positive alert triage`](../analyses/runbook-sensor-false-positive-alert-triage.md).
3. Broker / backhaul down → [`Runbook — broker or backhaul down`](../analyses/runbook-broker-or-backhaul-down.md).

---

## Related

- [`Sensor power and duty-cycle assumptions — Demory`](sensor-power-and-duty-cycle-assumptions-demory-farm.md)
- [`Automation stop rules — two-site smart farm`](../analyses/automation-stop-rules-two-site-smart-farm.md)
