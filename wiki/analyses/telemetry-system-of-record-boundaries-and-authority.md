---
title: Telemetry system of record — boundaries and authority
page_type: analysis
status: draft
created: 2026-04-18
updated: 2026-04-18
review_status: unreviewed
tags:
  - telemetry
  - data-governance
  - two-site
  - smart-farm
confidence: low
---

# Telemetry system of record — boundaries and authority

## Purpose

Define **who is authoritative for what** across **records systems**, **telemetry pipelines**, **dashboards**, **alerts**, and **manual verification**—so the **5 ac hub** does not confuse **convenience** with **truth**. Supports the [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md) and the **business plan** smart-tech narrative.

**Non-goals**: Picking a single vendor; claiming one database solves everything.

---

## Systems in play (generic labels)

| System class | Examples (illustrative) | Typical failure mode |
|--------------|---------------------------|----------------------|
| **A — Farm records / ERP** | farmOS, ledgers, inventory | **Stale** if humans don’t update after field work |
| **B — Telemetry transport** | MQTT broker | **Ephemeral**; **last message** ≠ **ground truth** |
| **C — Durable telemetry store** | TSDB, PostgreSQL time series | **Correct** for **what was ingested**—**not** if sensors drift |
| **D — Dashboard / automation hub** | Home Assistant, Grafana | **Aggregates**; **can cache** wrong **state** |
| **E — Alert channel** | Push, SMS, email | **Delivery** ≠ **accuracy** |
| **F — Manual verification** | Stick, dip, eyes, head count | **Slow**, **authoritative** for **welfare** decisions when sensors disagree |

---

## Authority matrix (fill; no default “HA is truth”)

| Question | Authoritative source | Second opinion | Never trust alone |
|----------|----------------------|----------------|-------------------|
| **Did we move animals from paddock X?** | **A** (log in records) + **manual** confirmation | **Camera** (if policy allows) | MQTT “gate” topic |
| **What did we spend on feed last quarter?** | **Books** / **A** | | Broker |
| **Tank level right now for automation** | **Calibrated** sensor → **C** if deduped | **Manual** stick | **D** widget if broker stale |
| **Historical soil moisture trend** | **C** (if ingested) | Export + stats | **D** graph without raw series |
| **Is the pump actually running?** | **Physical** (sound, pressure), **then** **current**/**VFD** if instrumented | **C** if **edge** timestamps reliable | Alert text |

---

## Boundaries

### Records (financial / certification / inventory)

- **Authoritative** for **money**, **inventory**, **organic** records, **movement** logs **when** the law or buyer cares: **designated records system** + **human attestation**.
- **Telemetry** may **inform** records but does **not** replace **signed** or **entered** events unless **policy** says so.

### Telemetry (measurements)

- **Authoritative** for **“what the instrument reported at time T”** once stored in **C** with **provenance** (device id, firmware, calibration date).
- **Not** authoritative for **animal count**, **profit**, or **“all clear”** without **cross-check**.

### Dashboards

- **Convenience**; assume **stale** after **T_STALE** minutes if not designed otherwise. **Placeholders**: `T_STALE_HOME_ASSISTANT = ___`, `T_STALE_GRAFANA = ___`.

### Alerts

- **Routing** of attention—**not** a database. **Alert storms** are **operational** failures: tune **dedupe**, **escalation**, **mute** rules per [`Sensor triage runbook`](runbook-sensor-false-positive-alert-triage.md).

### Manual verification

- **Overrides** automation when **Class B** (sensor lying) or **welfare** doubt—[`Automation degraded modes SOP`](automation-degraded-modes-manual-fallback-sop.md).

---

## Write paths (avoid duplicate “truth”)

| Anti-pattern | Fix |
|--------------|-----|
| HA and TSDB both “the database” | **One** **writer** to **C**; others **read** or **subscribe** |
| farmOS and spreadsheet both asset list | **`MAP_AUTHORITY_LABEL`** + **one** export path—[`Asset registry`](farm-spatial-model-and-asset-registry-standard.md) |
| Retained MQTT as “state” | Treat as **hint**; **persist** **deduped** events to **C** if you need **audit** |

---

## Split-site note

When **`SITE_FARM_120AC`** uplink is **down**, **authority** for **remote** operators **shifts** to **unknown**—**dashboards** at **`SITE_HOME_5AC`** may show **last** value. **Label** UI: **“stale since …”** or **assume worst** for **water**—see [`Manual fallback`](manual-fallback-degraded-modes-critical-operations.md).

---

## Links

- [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md)
- [`farmOS Assets`](../source-notes/farmos-model-assets-documentation.md), [`farmOS Logs`](../source-notes/farmos-model-logs-documentation.md)
- [`Field telemetry reference architecture`](field-telemetry-reference-architecture-homestead-120ac.md)
- [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md)
