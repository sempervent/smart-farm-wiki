---
title: Entity layer — operating objects gap audit
page_type: analysis
page_subtype: meta_audit
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - meta
  - entities
  - information-architecture
review_status: unreviewed
confidence: medium
---

# Entity layer — operating objects gap audit

## Purpose

Record **what was missing** in `wiki/entities/` for **repeatable operating objects** (roles and categories that analyses referenced repeatedly without a stable link target), and **what this pass added**. Complements [`Structural audit — page ownership, entity gaps, and hub routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md).

**Rule**: No **site-specific** hardware choices, deed facts, or legal names—those stay on worksheets, source-notes, or future **named** entity pages when evidenced.

---

## Gap summary (before)

| Area | Issue | Direction |
|------|--------|-----------|
| **Field architecture** | G/R/S/H/W **node roles** lived only inside Demory analyses | **Entity** + link from [`Field telemetry network — two-site`](../entities/field-telemetry-network-two-site.md) |
| **Gateways** | “Gateway” used for **RF→IP** and **WAN CPE** interchangeably | Split: **RF/telemetry gateway** vs **WAN edge / backhaul** entities |
| **Storage / backup** | Longhorn vs central NAS vs **tier labels** scattered across DR analyses | **Entities** pointing at restore tiers + storage-role analyses |
| **Labor / markets / legal** | Business plan chapters held tables; no **durable category** pages | **Generic** labor roles, market **channels**, legal **model** placeholders |
| **Platform** | k3s/etcd/Rancher “roles” explained in analyses only | **Control-plane** entity as router |
| **Infrastructure taxonomy** | Water/power entities existed; **cross-domain buckets** for inventory matrices were implicit | **Categories** entity |

---

## Added (this pass)

See **Entities** in [`index.md`](../index.md) — operating-object cluster — and the pages listed in [`wiki/log.md`](../log.md) under the matching refactor entry.

**Habit**: When an analysis introduces a **third** explanation of the same role label, add or extend an **entity** and replace prose with a link.

---

## Related

- [`Structural audit — page ownership, entity gaps, and hub routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md)
- [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md)
- [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md)
