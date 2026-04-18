---
title: Field node classes (G/R/S/H/W) — off-grid farm roles
page_type: entity
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - field-network
  - telemetry
  - off-grid
  - architecture
aliases:
  - Field node classes G R S H W
confidence: medium
review_status: unreviewed
---

# Field node classes (G/R/S/H/W) — off-grid farm roles

## Purpose

Durable **architecture labels** for **field** nodes: **G** (gateway/spine), **R** (mesh repeater), **S** (sensor leaf), **H** (sub-GHz IP bridge, e.g. HaLow segment), **W** (WAN edge). These are **roles**, not product SKUs—analyses cite them to avoid re-typing the table.

## Scope

- **In scope**: Power posture expectations, **local-first** vs **WAN-dependent** behavior, pilot discipline (one spine family until evidence gates pass—see linked analyses).
- **Out of scope**: Vendor/model picks, per-site mount heights, or firmware versions (deployment evidence).

## Knowns

- The vault’s **canonical elaboration** with a full table and diagram is the Demory `SITE_FARM` doctrine (below).
- **W** is **egress**-oriented and is typically **not** in the **Pcrit** default for local delivery paths.

## Assumptions

- The same **letter taxonomy** may apply to other farms only after **local** validation (power, RF noise, coverage).

## Related analyses

- [`Field-node classes and communication roles — Demory farm site`](../analyses/field-node-classes-and-communication-roles-demory-farm.md)
- [`Mesh and field networking strategy — off-grid Demory`](../analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md)
- [`Off-grid infrastructure stop rules — Demory`](../analyses/off-grid-operational-decision-rules-power-and-networking-demory-farm.md) (DR-* gates)
- [`Field telemetry network — two-site`](field-telemetry-network-two-site.md)

## Related source notes

- [`Off-grid power, field RF, and optional WAN — source index (Demory planning)`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md)

## Outstanding unknowns

- Which **concrete** hardware instances will implement **G** vs **R** at each site after pilot recon.
- Whether a second **WAN** path is justified (economic and **DR-2** evidence).
