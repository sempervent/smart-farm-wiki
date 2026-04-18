---
title: Farm on-site power system
page_type: entity
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - power
  - solar
  - infrastructure
confidence: medium
review_status: unreviewed
---

# Farm on-site power system

**What this entity is**: **Electrical energy** delivery and **backup** at farm scale: **grid** where present, **solar + storage**, **generators**, **transfer** hardware, and **loads** (pumps, coolers, field gateways). Distinct from **home** automation power except where the **homestead** backs a **shared** stack.

**Why it matters**: **Runbook**: [`Power loss at remote site`](../analyses/runbook-power-loss-remote-site.md) assumes **known** safe states for water and refrigeration; **off-grid** narratives in the vault inform **sizing** discussions but are not a single prescription.

**Canonical topic hub**: [`Off-grid solar power and storage`](../topics/off-grid-solar-power-and-storage.md).

**Does not claim**: Your service size, NEC compliance, or generator start procedure—**local** code and electrician sign-off.

**Related**

- [`Farm water infrastructure system`](farm-water-infrastructure-system.md) (pumps as loads)
- [`Field telemetry network — two-site`](field-telemetry-network-two-site.md) (gateway power at `SITE_FARM`)
