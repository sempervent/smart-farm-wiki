---
title: Field radio link classes — LPWAN, mesh, and IP bridges
page_type: entity
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - lora
  - mesh
  - halow
  - field-network
aliases:
  - LoRaWAN vs mesh vs HaLow classes
confidence: medium
review_status: unreviewed
---

# Field radio link classes — LPWAN, mesh, and IP bridges

## Purpose

Durable **link-layer** categories for field networks: **LoRaWAN** (star to gateways), **mesh** (multi-hop peer), **sub-GHz IP** (e.g. HaLow / 802.11ah segments), and **conventional Wi‑Fi** where range permits—so comparisons can reference **classes** instead of re-deriving tradeoffs.

## Scope

- **In scope**: Definitions, routing to **comparison** and **concept** pages.
- **Out of scope**: Site spectrum scans or interference reports.

## Knowns

- The vault holds **four-way** and **three-way** comparison analyses for field networking.
- **Node classes** G/R/S/H/W describe **roles** atop these links—see [`Field node classes (G/R/S/H/W)`](field-node-classes-off-grid-farm-roles.md).

## Assumptions

- **One** primary RF family per pilot until **DR-5**-class evidence in off-grid doctrine (see stop rules—not restated here).

## Related analyses

- [`Wi‑Fi HaLow vs LoRaWAN vs Meshtastic vs conventional Wi‑Fi`](../comparisons/wi-fi-halow-lorawan-meshtastic-conventional-wi-fi-farm-field-networking.md)
- [`Meshtastic vs HaLow vs conventional Wi‑Fi — off-grid farm operations`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md)
- [`Mesh and field networking strategy — off-grid Demory`](../analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md)

## Related source notes

- Concept-level: [`LoRa (radio)`](../concepts/lora-radio.md), [`Meshtastic`](../concepts/meshtastic.md), [`Wi‑Fi HaLow`](../concepts/wi-fi-halow.md)
- Batch: [`Off-grid power, field RF, and optional WAN — source index (Demory planning)`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md)

## Outstanding unknowns

- **Measured** throughput/latency and **battery** budgets per paddock after deployment.
