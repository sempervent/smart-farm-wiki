---
title: Runbook — manual fallback for irrigation, gates, and pumps
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - sop
  - runbook
  - irrigation
review_status: unreviewed
confidence: low
---

# Runbook — manual fallback for irrigation, gates, and pumps

**Prerequisites**: [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md) (parent); **physical** valve/breaker labels on **`SITE_FARM`**. This runbook **specializes** the parent SOP for **water movement** systems.

## Purpose

**Manual safe state** when **automation**, **MQTT**, or **sensors** cannot be trusted for **irrigation**, **pumps**, and **motorized gates**.

## Irrigation / pumps

1. **Upstream shutoff first**—placeholders: `IRRIGATION_MASTER_VALVE_REF`, `PUMP_BREAKER_ID`.
2. **Relieve pressure** where needed per **install**.
3. **Verify** wetness at **emitters** or **outlet** before restoring.

## Gates

1. **Disconnect motor** per manufacturer; **physical latch** in **`GATE_SAFE_POSITION`**.
2. **Never** depend on MQTT for **escape prevention**.

## When to escalate

- **Buried line leak suspicion**—**shut** and **call** qualified help; not a wiki decision.

## Related

- [`Runbook — sensor false positive and alert triage`](runbook-sensor-false-positive-alert-triage.md)
- [`Runbook — power loss at remote site`](runbook-power-loss-remote-site.md)

---

*Trained personnel only for **lockout/tagout** on industrial pumps.*
