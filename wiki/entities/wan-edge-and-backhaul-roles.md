---
title: WAN edge and backhaul roles — two-site and off-grid
page_type: entity
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - wan
  - starlink
  - lte
  - backhaul
  - two-site
aliases:
  - WAN CPE roles farm
confidence: medium
review_status: unreviewed
---

# WAN edge and backhaul roles — two-site and off-grid

## Purpose

Durable labels for **internet / site-to-site** paths: **WAN customer edge** (e.g. satellite or cellular CPE), **optional terrestrial** links, and **backhaul** as the **uplink** segment that carries MQTT/admin **when you choose cloud paths**—distinct from **field RF** bridges ([`RF and telemetry gateway roles`](rf-telemetry-gateway-roles-field-network.md)).

## Scope

- **In scope**: Role definitions, **degraded** expectations when WAN fades, pointers to stop rules and connectivity doctrine.
- **Out of scope**: Carrier account details, public IPs, or **your** contracted speeds.

## Knowns

- The **East Tennessee two-site** package discusses **Starlink / LTE** and **pilot vs scale** posture in the connectivity strategy (named Claxton/Demory anchors).
- Off-grid doctrine treats **W** nodes as **sheddable** relative to **Pcrit** field spine in the G/R/S/H/W model.

## Assumptions

- **Local-first** operation remains possible for **defined** workloads when WAN is absent—see dependency maps.

## Related analyses

- [`Connectivity strategy — Claxton home base and Demory farm site`](../analyses/connectivity-strategy-for-claxton-and-demory.md)
- [`Two-site smart farm network topology and WAN edge reference`](../analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md)
- [`Execution topology package — two-site smart farm (Mermaid)`](../analyses/execution-topology-package-two-site-smart-farm.md)
- [`Automation stop rules — two-site smart farm`](../analyses/automation-stop-rules-two-site-smart-farm.md) (CS-*, MV-* WAN drills)
- [`Local-first / WAN-optional operating model — Demory`](../analyses/local-first-wan-optional-operating-model-demory-farm.md)

## Related source notes

- [`Electrical, networking, and Starlink — inbox batch (2026-04-23)`](../source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md)

## Outstanding unknowns

- **Final** redundant WAN strategy per site after cost/coverage validation (see validation plans—not prescribed here).
