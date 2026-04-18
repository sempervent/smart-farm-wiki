---
title: Off-grid degraded modes — power and connectivity (Demory farm)
page_type: analysis
status: active
created: 2026-04-24
updated: 2026-04-17
review_status: unreviewed
tags:
  - degraded-modes
  - off-grid
  - demory
confidence: medium
---

# Off-grid degraded modes — power and connectivity (Demory farm)

## Purpose

Extend **two-site** **degraded-mode** **thinking** **for** **`SITE_FARM`** **(Demory)** **when** **power** **and** **WAN** **fail** **independently** **or** **together** **—** **without** **duplicating** [`Manual fallback`](manual-fallback-degraded-modes-critical-operations.md) **prose** **.**

**Doctrine package**: [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md).

**Topology** **views** **:** [`Off-grid farm execution topology — Demory (Mermaid)`](off-grid-farm-execution-topology-demory-mermaid.md) **.**

```mermaid
stateDiagram-v2
  [*] --> Nominal
  Nominal --> N1 : WAN down only
  Nominal --> Pstress : SOC / PV fault
  N1 --> N2 : add power stress
  Pstress --> N2 : add WAN loss
  note right of N2 : N2 — paper rounds; battery-backed critical only
```

---

## Failure classes (farm-specific)

| Class | Symptoms | Safe assumption | Operator response |
|-------|----------|-----------------|-------------------|
| **P1** **—** **Deep** **battery** **SOC** **/** **load** **shed** | **Inverter** **sheds** **non-critical** **;** **some** **radios** **drop** | **Telemetry** **silence** **≠** **“** **fine** **”** **at** **the** **water** **.** | **Physical** **rounds** **;** **disable** **non-critical** **RF** **if** **policy** **says** **so** **.** |
| **P2** **—** **PV** **/** **charge** **fault** | **Reduced** **daily** **Wh** **budget** | **Starlink** **and** **high** **duty** **cameras** **may** **need** **to** **stay** **off** **until** **SOC** **recovers** **.** | **Runbook** **:** [`Runbook — power loss at remote site`](runbook-power-loss-remote-site.md) **.** |
| **N1** **—** **WAN** **down** **,** **power** **OK** | **No** **cloud** **;** **mesh** **/** **LAN** **may** **still** **work** | **Same** **as** **global** **LEO** **WAN** **impaired** **row** **on** [`Manual fallback`](manual-fallback-degraded-modes-critical-operations.md) **.** | [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md) **.** |
| **N2** **—** **WAN** **+** **power** **stress** **(both** **)** | **No** **egress** **;** **some** **nodes** **dark** | **Only** **battery-backed** **critical** **paths** **matter** **.** | **Paper** **rounds** **;** **genset** **policy** **if** **installed** **(**TBD** **)** **.** |

---

## What must still work (policy)

- **Welfare** **interlocks** **that** **do** **not** **require** **cloud** **.**
- **At** **least** **one** **local** **way** **to** **know** **tank** **/** **gate** **state** **(sight** **,** **float** **,** **local** **indicator** **)** **.**
- **Offline** **records** **discipline** **for** **anything** **that** **feeds** **books** **.**

---

## What Starlink enables in recovery (only when powered)

- **Coordinating** **with** **Claxton** **(**`SITE_HOME` **)** **,** **vendors** **,** **or** **weather** **when** **you** **choose** **to** **burn** **Wh** **on** **CPE** **.**

## What Starlink must not gate

- **Decision** **to** **drive** **for** **Tier-1** **animal** **or** **water** **risk** **—** **policy** **beats** **dashboard** **.**

---

## Related

- [`Connectivity dependency map — farm systems (Demory)`](connectivity-dependency-map-farm-systems-demory-farm.md)
- [`Off-grid infrastructure stop rules — Demory`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md)
- [`Automation degraded modes SOP`](automation-degraded-modes-manual-fallback-sop.md)
