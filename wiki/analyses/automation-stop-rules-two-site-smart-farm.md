---
title: Automation stop rules — two-site smart farm
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-17
review_status: unreviewed
tags:
  - automation
  - telemetry
  - two-site
  - governance
confidence: medium
---

# Automation stop rules — two-site smart farm

## Purpose

Execution-safe **stop**, **freeze**, and **no-scale** rules for automation and telemetry on the East Tennessee two-site package. Aggressive automation stays allowed as **philosophy**—but **scaling stops** when failure rates, upkeep load, or operator burden exceed budgets, or when manual validation has not passed.

This page does **not** assume instrumentation reduces labor by default ([`Smart technology strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md), [`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md)).

---

## When a system must not scale

Freeze fleet expansion or roll back to pilot scope if **any** row below holds after a documented remediation attempt:

| ID | Condition | Evidence |
|----|-----------|----------|
| **NS-1** | `FP_RATE > FP_RATE_MAX` for `T_FP_EVAL` consecutive weeks | [`ROI — false-positive cost fields`](instrumentation-roi-model-two-site-smart-farm.md#false-positive-cost-fields) |
| **NS-2** | `H_TRIAGE_WK` for this cluster exceeds allocated `H_TRIAGE_BUDGET_WK`, **or** total triage exceeds `H_TRIAGE_MAX` | Time logs; [`Enterprise unit economics`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md) |
| **NS-3** | Net labor hours ≤ 0 for **two** review periods per ROI worksheet | [`Instrumentation ROI`](instrumentation-roi-model-two-site-smart-farm.md) |
| **NS-4** | Marginal OPEX + marginal triage per node ≥ marginal trip-$ benefit (rolling quarter) | Sublinear benefit curve broken |
| **NS-5** | No named owner for patch/incident and `T_PATCH_MAX` elapsed | Security stop — [`Smart tech` § security](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md#security-obligations-non-negotiable) |
| **NS-6** | Actuation enabled without **PA-*** proof rows met | Immediate revert to observe-only |

**Scale** means more nodes, tighter alert thresholds, new integrations, or remote actuation beyond a proven pilot.

---

## Connectivity and WAN stop rules (CS-*)

Use when **Starlink**, **LTE**, **fiber**, or **any** **primary** **WAN** **path** **is** **part** **of** **the** **stack** **—** **see** [`Validation and pilot plan` § Connectivity validation](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation), [`Connectivity strategy — Claxton & Demory`](connectivity-strategy-for-claxton-and-demory.md).

Freeze new WAN-dependent scope (cloud integrations, second sensor cluster, second farm uplink, tighter alert routing to phone) **or** new **always-on** field RF at **`SITE_FARM`** if any row holds after one documented remediation attempt:

| ID | Condition | Evidence |
|----|-----------|----------|
| **CS-1** | Recurring WAN + cell (pilot) costs exceed stated value proxy (trip $/labor saved or written ops benefit) for two consecutive quarterly reviews | Separate ledger lines per connectivity validation; family decision to trim, pause, or pivot |
| **CS-2** | Primary uplink in production use ≥ 90 days but no seasonal WAN reliability log (outages, fade, handoff) | V10 incomplete—treat uplink as unproven |
| **CS-3** | Remote access inventory does not match [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md) before expanding pilot | Security stop—complete inventory first |
| **CS-4** | Operational reliance on dashboards / MQTT for welfare or “should I drive?” while G8 / WAN degraded drill not passed | Revert to manual rounds per [`Manual fallback and degraded modes`](manual-fallback-degraded-modes-critical-operations.md) |
| **CS-5** | **`SITE_FARM`** off-grid: new always-on IP radios, HaLow segments, or farm Starlink CPE added while [`Off-grid operational decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md) **DR-1** is open (network + CPE load not bracketed against battery / Pcrit) | Freeze scope per DR-1; complete energy budget row or explicit waiver in writing |

**CS-*** stack with **NS-***: connectivity or **field-power** fragility can justify a freeze even when false-positive rates look fine.

---

## What must be manually validated before rollout

**Rollout** = production reliance on an instrument for operations, or first actuation enable.

| Gate | Manual validation |
|------|-------------------|
| **MV-1** | Asset ID + location in registry matches physical install |
| **MV-2** | Baseline manual procedure documented (normal vs alarm) |
| **MV-3** | One season **or** `T_OBSERVE_MIN` weeks of observe-only data with labeled true vs false alerts |
| **MV-4** | Degraded-mode drill: broker down / LTE only — document who drives and how often |
| **MV-5** | Runbook link for this instrument class (triage, mute policy, escalation) |
| **MV-6** | Cyber: remote surface inventoried for this cluster |
| **MV-7** | WAN outage / Starlink fade drill documented (seasonal or simulated) per [`Automation degraded modes SOP`](automation-degraded-modes-manual-fallback-sop.md) / [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md)—who reverts to physical checks when WAN is impaired |
| **MV-8** | For **`SITE_FARM`** off-grid: local-only drill passed—telemetry path without WAN and documented behavior when battery/SOC is stressed (queue-only, mesh-up, gateway-down scenarios per [`Off-grid degraded modes — Demory`](off-grid-degraded-modes-power-and-connectivity-demory-farm.md)). Required before remote field visibility is treated as production-trusted at Demory. |

Missing any **MV-*** → no fleet rollout and no actuation. For instruments on off-grid **`SITE_FARM`**, **MV-8** applies; **CS-5** freezes new always-on RF/WAN scope while **DR-1** is open ([`Off-grid operational decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md)).

---

## Phase 1 observational only by default

Per [`Smart tech` stack posture](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md#stack-posture-by-phase), these systems remain **observational only** unless **PA-1–PA-6** and **MV-1–MV-7** are explicitly satisfied for that asset (**MV-8** as well for off-grid **`SITE_FARM`** field assets):

| System / class | Phase 1 default |
|----------------|-----------------|
| Stock water level / pump run / fault | Observe + alert only |
| Power visibility at pump / gateway | Observe only |
| Gate position sensor | Observe only — no remote latch release |
| Irrigation valves / schedulers | Observe only or deferred (see **AF-3** on [`Smart tech`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)) |
| Cameras | Observe only — no automated actions from CV |
| Herd GPS / collars | Deferred or pilot one unit — not fleet |

Remote actuation (pump control, gate motor, irrigation writes) requires exiting this table via proof gates **PA-*** on [`Smart technology strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md#proof-requirements-before-remote-actuation).

---

## Related

- [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md)
- [`Validation and pilot plan` § Connectivity validation](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation)
- [`Runbook — sensor false positive and alert triage`](runbook-sensor-false-positive-alert-triage.md)
- [`Execution gates — financial thresholds`](execution-gates-financial-thresholds.md)
- [`Trip batching and site visit policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md)
