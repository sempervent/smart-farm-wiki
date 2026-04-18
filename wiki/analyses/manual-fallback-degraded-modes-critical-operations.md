---
title: Manual fallback and degraded modes — critical operations
page_type: analysis
status: draft
created: 2026-04-17
updated: 2026-04-18
review_status: unreviewed
tags:
  - operations
  - resilience
  - two-site
  - automation
confidence: medium
---

# Manual fallback and degraded modes — critical operations

## Purpose

List **critical operations** for the **two-site** **grazing-led** **operation** and define **manual fallback** when **automation**, **comms**, or **power** **degrades**. **Does not** replace vault **runbooks**—**indexes** them and adds **family** **coverage** **context**.

**Architecture package**: [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md), [`Automation principles`](automation-principles-two-site-smart-farm.md).

**Parent SOP**: [`Automation degraded modes and manual fallback`](automation-degraded-modes-manual-fallback-sop.md)

---

## Scenario model (explicit)

Design degraded behavior for travel, outages, sensor failure, comms failure, and maintenance burden—not only “broker down.”

| Scenario | What breaks | First response | Sustained posture | Labor tax |
|----------|-------------|----------------|-------------------|-----------|
| `COMMUTE_ONE_WAY` too long for urgency | Time to site | Tier risk; neighbor / call tree | Reduce closed-loop dependence | Extra checks or hired relief |
| Backhaul down (farm → hub internet) | Remote visibility | Assume stale data; physical round | Increase visit frequency (bounded) | Trip count ↑ |
| Broker / cloud down | MQTT / integrations | Disable auto acting on stale topics | Local safe defaults | Triage ↓ if alerts quiet (dangerous calm) |
| Sensor wrong (Class B) | Bad input to logic | Triage runbook; manual measure | Remove sensor from control until fixed | Debug time |
| Maintenance backlog (unpatched / dirty sensors) | Drift, false alarms | Mute is not fix—clean, calibrate, replace | Fewer channels until healthy | Ops hours or contract |

**Placeholder**: `COMMUTE_ONE_WAY = ___` min; `MAX_ACCEPTABLE_TIME_TO_WATER_VERIFY = ___` min (policy).

## Key decisions supported

| Decision | Use this page |
|----------|----------------|
| **Minimum** **viable** **manual** **capability** | If row has **no** **manual** **fallback** → **do not** **depend** **on** **automation** |
| **Spares** **inventory** | **Critical** **spare** column |
| **Who** **responds** **when** **telemetry** **lies** | Link **coverage** [`Family labor and coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md) |

## Critical operations matrix (fill)

| Op ID | Operation | **Normal** (automated / monitored) | **Degraded** trigger | **Manual fallback** | **Safe default** | **Spares / kit** | Runbook link |
|-------|-----------|-----------------------------------|----------------------|---------------------|------------------|------------------|--------------|
| O1 | **Water** to stock | Tank level / pump status | **No** **telemetry** **or** **pump** **fault** | **Visual** **tank** **check**; **backup** **haul** **plan** | Pump **off** **if** **electrical** **fault** **unknown** | **Hose**, **breaker** **labels**, **generator** **plan** | [`Power loss — remote`](runbook-power-loss-remote-site.md) |
| O2 | **Perimeter** **security** | Fence **visual** **+** **optional** **alarm** | **Unknown** **state** | **Walk** **or** **ATV** **patrol** **on** **schedule** | **Isolate** **animals** **to** **sacrifice** **paddock** **if** **needed** | **Fence** **repair** **kit** | |
| O3 | **Move** **stock** | **Planned** **rotation** | **Gate** **remote** **down** | **Manual** **gate** | **Closed** **vs** **open** **per** **policy** | **Tools**, **chain** | [`Manual fallback — irrigation/gates/pumps`](runbook-manual-fallback-irrigation-gates-pumps.md) |
| O4 | **Comms** **/** **alerting** | **MQTT** **→** **phone** | **Broker** **down** | **Scheduled** **physical** **check** **increases** | **Assume** **worst** **until** **verified** | **Paper** **checklist** **in** **truck** | [`Broker or backhaul down`](runbook-broker-or-backhaul-down.md) |
| O5 | **Haul** **/** **marketing** | **N/A** | **Truck** **down** | **Hired** **haul** **#** | | **Backup** **contact** | |
| O6 | **Processing** **appointment** | Calendar | **N/A** | **Phone** **tree** | | | |

Add **O7+** for **your** **context** (loading, **hay** **barn**, **cold** **storage**).

## Degraded-mode principles

1. **Assume** **telemetry** **wrong** **until** **corroborated** ([`Sensor false positive / alert triage`](runbook-sensor-false-positive-alert-triage.md)).
2. **Increase** **visit** **frequency** **when** **comms** **down**—**bounded** **by** **labor** **reality** (coverage matrix).
3. **Document** **“good** **enough”** **manual** **state**—**not** **perfect** **pasture** **during** **outage**.

## What must never be “automation-only”

| Item | Why |
|------|-----|
| **Animal** **welfare** **checks** **during** **extreme** **weather** | **Sensors** **miss** **down** **animal** |
| **Loading** **for** **sale** | **Safety** **+** **bruising** **=** **money** |
| **First** **response** **to** **escape** **on** **public** **road** | **Liability** |

## Known / assumed / open

| Class | Content |
|-------|---------|
| **Known** | Vault **runbooks** **exist** **for** **broker**, **power**, **triage**, **water** **manual** |
| **Assumed** | **Vehicle** **always** **available** **for** **emergency** **trip** |
| **Open** | **Neighbor** **call** **list**; **vet** **after-hours** |

## Links

- [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md)
- [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md)
- [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md)
- [`Two-site operations model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md)
- [`Field telemetry reference architecture`](field-telemetry-reference-architecture-homestead-120ac.md)
