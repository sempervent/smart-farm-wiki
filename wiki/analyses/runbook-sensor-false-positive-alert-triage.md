---
title: Runbook — sensor false positive and alert triage
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - sop
  - runbook
  - observability
review_status: unreviewed
confidence: low
---

# Runbook — sensor false positive and alert triage

**Prerequisites**: [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md); [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) (**which** sensor is **where**). See backlog **P2 #19** for future **observability** depth.

## Purpose

When **alerts fire** but reality is unclear—**stuck sensor**, **RF noise**, **bad calibration**—avoid **alert fatigue** and **wrong** manual actions.

## Triage order

1. **Severity**: **animal welfare** / **water** / **escape** first—override **nuisance** channels per policy.
2. **Corroborate**: second **independent** sensor or **camera** (if policy allows) or **human** eyes.
3. **Time series**: spike vs **stuck flatline**—different root causes.
4. **Disable automation** acting on **bad** input—[`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md).

## Record-keeping

- **Incident log**: device ID, **firmware**, **last calibration**, **weather**—feeds **firmware lifecycle** policy later.

## Related

- [`Runbook — manual fallback for irrigation, gates, and pumps`](runbook-manual-fallback-irrigation-gates-pumps.md)

---

*“Mute alert” is never step one without **physical verification** on Tier A risks.*
