---
title: Gateway and controller patterns — Demory farm (~120 acres)
page_type: analysis
status: active
created: 2026-04-25
updated: 2026-04-25
tags:
  - demory
  - gateway
  - lorawan
  - mqtt
review_status: unreviewed
confidence: medium
---

# Gateway and controller patterns — Demory farm (~120 acres)

**Purpose**: Operator patterns for aggregating long-range field sensors on a ~120-acre rural parcel where one tower may not see all edges. Pairs with [`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md) and entity pages for **roles** (not SKUs).

**Sources**: [`Demory farm sensor layer — official and operator-grade source cluster`](../source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md) (ChirpStack captures, LoRaWAN spec).

---

## Pattern A — LoRaWAN star to private NS (ChirpStack-class)

| Element | Role |
|---------|------|
| **Gateway(s)** | RF → network server; **diversity** reduces SPOF when terrain creates ridge/valley shadowing |
| **Network server** | Join, ADR, application payload routing |
| **MQTT / HTTP integration** | Egress to broker at controller |

**When**: Certified LoRaWAN sensors dominate; you accept star topology and explicit gateway planning.

**Risk**: Gateway impaired → silence from covered devices unless overlapping gateways or relocation.

---

## Pattern B — Meshtastic mesh + bridge to MQTT

| Element | Role |
|---------|------|
| **Mesh nodes** | R repeaters + S leaves; multi-hop without single-tower omniscience |
| **Bridge / G** | MQTT to broker; policy for default radio vs MQTT (0-hop) behavior |

**When**: Sparse telemetry and coverage holes; ops accept firmware cadence.

**Risk**: Mesh partition; not a substitute for welfare rounds.

---

## Pattern C — HaLow (802.11ah) IP segment

| Element | Role |
|---------|------|
| **AP / CPE** | Sub-GHz IP to sensor or bridge device |
| **Controller** | Same LAN policies as 802.11—patch, segment |

**When**: Higher throughput or IP-native devices; budget power vs LoRa sleep.

---

## Controller placement (farm vs Claxton)

| Option | Pros | Cons |
|--------|------|------|
| **Controller at Demory** (broker + store) | Low latency; WAN optional for local truth | Hands-on when LAN broken requires site visit |
| **Split SoR** (authoritative at farm, read replica at Claxton) | Remote visibility | Sync complexity; staleness rules |

Starlink only bridges WAN—not field RF.

---

## Related

- [`RF and telemetry gateway roles`](../entities/rf-telemetry-gateway-roles-field-network.md)
- [`Fixed gateway tower vs mobile or vehicle gateway`](../comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md)
- [`LoRaWAN vs Meshtastic for fixed farm telemetry`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md)
