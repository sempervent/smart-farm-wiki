---
title: Off-grid infrastructure stop rules — power and networking (Demory farm)
page_type: analysis
status: active
created: 2026-04-24
updated: 2026-04-17
review_status: unreviewed
tags:
  - operations
  - off-grid
  - demory
confidence: medium
aliases:
  - Off-grid operational decision rules Demory farm
---

# Off-grid infrastructure stop rules — power and networking (Demory farm)

## Purpose

Executable **stop** **rules** **and** **simplification** **triggers** **(**placeholders** **allowed** **)** **for** **when** **to** **add** **RF** **,** **power** **more** **CPE** **,** **or** **stop** **scaling** **telemetry** **at** **Demory** **—** **aligned** **with** [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) (**CS-5**, **MV-8**) **and** [`Connectivity validation`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation).

**Doctrine package**: [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md).

---

## Rules (fill private thresholds)

| ID | Rule |
|----|------|
| **DR-1** | No new always-on IP radio until `P_NET_ALWAYS_W` (or bracketed Wh/day for networking) is metered and budgeted against battery days of autonomy (placeholder). Stacks with [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) **CS-5**. |
| **DR-2** | No second farm WAN terminal until [`Connectivity strategy`](connectivity-strategy-for-claxton-and-demory.md) Phase 1 proof rows pass. |
| **DR-3** | If triage hours exceed trip savings for telemetry, freeze fleet ([`Stop rules`](automation-stop-rules-two-site-smart-farm.md))—off-grid does not exempt this. |
| **DR-4** | HaLow or new mesh hop only if [`Meshtastic vs HaLow vs Wi‑Fi`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md) shows ROI vs Meshtastic or Ethernet for that use case. |
| **DR-5** | Pilot phase: one gateway + one RF class + one WAN path maximum until G8 / V10 evidence is honest. |

---

## Pilot vs later scale (summary)

| Phase | Networking + power |
|-------|---------------------|
| **0–1** | Measure loads; one mesh cluster; optional Starlink on a sheddable branch. |
| **Later** | HaLow backhaul segments, redundant gateway, dual WAN only with O&M budget. |

---

## Simplification triggers (de-scope before adding)

| Trigger | Response |
|---------|----------|
| **`P_NET`** **or** **network** **Wh/day** **unmeasured** **vs** **battery** **days** **of** **autonomy** | **Freeze** **new** **always-on** **radios** **(**stacks** **with** **CS-5** **)** |
| **Triage** **hours** **>** **trip** **savings** **(**DR-3**)** | **Freeze** **sensor** **fleet** **;** **manual** **rounds** **first** |
| **MV-8** **drill** **fails** **(**local-only** **/** **SOC-stressed** **)** | **No** **new** **automation** **until** **drill** **passes** |
| **Second** **RF** **class** **before** **first** **is** **boring** | **Violates** **DR-5** **—** **stop** **adding** **hops** |

---

## Related

- [`Off-grid power doctrine — Demory farm site`](off-grid-power-strategy-demory-farm-site.md)
- [`Mesh and field networking strategy — off-grid Demory farm`](mesh-and-field-networking-strategy-off-grid-demory-farm.md)
- [`Local-first / WAN-optional operating model — Demory`](local-first-wan-optional-operating-model-demory-farm.md)
- [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md)
