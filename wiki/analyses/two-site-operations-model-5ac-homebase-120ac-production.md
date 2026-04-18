---
title: Two-site operations model — home base on 5 acres, production on 120 acres
page_type: analysis
status: draft
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - two-site
  - operations
  - template
confidence: medium
aliases:
  - Two-site ops 5 ac 120 ac
---

# Two-site operations model — home base on 5 acres, production on 120 acres

## Purpose

Give a **repeatable operating picture** for a **family** farm business split across:

| Site | Label | Planning size | Role |
|------|-------|---------------|------|
| **Home base** | `SITE_HOME` | ~**5 acres** | **Not** primary commercial production—residence, **control center**, workshop/lab, future smart-house + **telemetry brain** |
| **Production** | `SITE_FARM` | ~**120 acres** | **Primary** land-based revenue and field operations |

**Separation**: `COMMUTE_ONE_WAY` (planning default **~35 minutes**—**measure and log**).

This page is an **operational** companion to the business plan’s [`Two-site operating context (ET plan)`](east-tennessee-two-site-farm-business-plan-two-site-operating-context.md) and the generic [`Dual-site operations model — non-agritourism`](dual-site-operations-model-non-agritourism.md).

## Key decisions this page supports

| Decision | How this page helps |
|----------|---------------------|
| **Where CAPEX lives** (home vs farm) | Split table + **irreversible** vs **portable** |
| **Batch size** worth a trip | **Minimum productive duration** at `SITE_FARM` |
| **What must be duplicated** vs centralized | **Spares**, **comms**, **records authority** |
| **Emergency response** | **Who**, **how fast**, **without** comms |

## Operating model (fill in)

### Site roles

| Function | Preferred location | Notes |
|----------|-------------------|-------|
| **Broker / dashboards / backups** | `SITE_HOME` | Stable power, daily physical access |
| **Field gateways, tank sensors, pump controls** | `SITE_FARM` | Edge; **degraded** when backhaul down |
| **Livestock handling, equipment** | `SITE_FARM` | |
| **Development / CAD / 3D print for jigs** | `SITE_HOME` | |
| **Primary financial / legal records** | `SITE_HOME` or cloud **with** offline export | **Pick one authority** |

### Distance economics (placeholders)

| Metric | Placeholder | Source / update |
|--------|-------------|-----------------|
| One-way drive | `COMMUTE_ONE_WAY` = **___ min** | Seasonal log |
| Round-trip + task budget | **___ h** typical field visit | Time study |
| **Minimum** visit worth driving | **___ h** productive work **or** **abort** | Policy |

### Batch rules

- **Rule A**: No trip for **under `MIN_VISIT_MINUTES`** on-site work unless **Tier 1** alert (define Tier 1 on [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md)).
- **Rule B**: **Fixed** **dow** for `SITE_FARM` heavy work (link [`Family labor and coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md)).

## Infrastructure split (editable)

| Asset | `SITE_HOME` | `SITE_FARM` | Spare / notes |
|-------|-------------|-------------|---------------|
| Internet / VPN | Primary | LTE fallback? `Y/N` | |
| MQTT broker | Primary | Edge cache? `Y/N` | [`Runbook — broker down`](runbook-broker-or-backhaul-down.md) |
| Generator / backup power | Homelab UPS | Field pump? | |
| Trailer parking | | Primary | |

## Known / assumed / open (site-agnostic)

| Class | Content |
|-------|---------|
| **Known (from plan)** | Two parcels; **5 ac not** primary production; **profit-first** brief |
| **Assumed** | `COMMUTE_ONE_WAY` representative until logged |
| **Open** | Road **seasonal** passability; **exact** **gate** locations; **overnight** stay policy at `SITE_FARM` |

## Links

- [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)
- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md)
- [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md)
- [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md)
