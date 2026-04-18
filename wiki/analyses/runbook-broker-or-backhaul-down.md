---
title: Runbook — broker or backhaul down
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - sop
  - runbook
  - mqtt
  - telemetry
review_status: unreviewed
confidence: low
---

# Runbook — broker or backhaul down

**Prerequisites**: [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md); [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md). Without an agreed **architecture**, this runbook is **theater**.

## Purpose

When **MQTT broker** or **IP backhaul** to **`SITE_FARM`** fails, **stop assuming** remote state matches reality; **verify physical** and **stabilize animals, water, and gates**.

## Detection

- **HA / dashboard**: entities **unavailable** or **stale** beyond **`STALE_THRESHOLD`** (define in architecture).
- **Broker**: no subscribers receiving; **ping** or **mgmt** port check from **authorized** host only.
- **Backhaul**: traceroute / **LTE modem** stats if documented.

## Immediate actions (order may vary)

1. **Classify**: broker-only vs **internet** vs **power** at gateway (see [`Runbook — power loss at remote site`](runbook-power-loss-remote-site.md)).
2. **Disable dangerous automation**: rules that **open water** or **unlock** on stale “OK” signals—per degraded SOP.
3. **Notify**: use **out-of-band** comms (cell call/SMS tree) per **weekly coverage matrix**.
4. **Log**: timestamp, **what** was disabled, **who** on-site—correlate after recovery.

## Recovery

- **Broker**: failback order—**persistent sessions**, **retained message** policy per architecture.
- **Backhaul**: **failover** SIM/path if designed; else **schedule** visit.

## Related

- *Telemetry system of record* — backlog P0 #6; [`Data storage (farm and edge stacks)`](../concepts/data-storage.md)

---

*Replace placeholders with **hostname**, **ports**, and **contact tree** internal to your opsec.*
