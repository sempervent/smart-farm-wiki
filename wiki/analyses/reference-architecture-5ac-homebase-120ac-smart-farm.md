---
title: Reference architecture — 5-acre home base + 120-acre farm
page_type: analysis
status: draft
created: 2026-04-18
updated: 2026-04-25
review_status: unreviewed
tags:
  - architecture
  - two-site
  - telemetry
  - smart-farm
confidence: low
---

# Reference architecture — 5-acre home base + 120-acre farm

## Purpose

Give a **single first-draft** **logical** picture of the **smart-farm stack** for the staged **East Tennessee two-site business plan**: **`SITE_HOME_5AC`** as **control center**, **workshop**, **smart home**, and **data/telemetry hub**; **`SITE_FARM_120AC`** as **production** and **remote operations** target. **Not** a bill of materials—**boundaries**, **paths**, and **failure domains**.

**Business plan links**: [`Planning framework`](east-tennessee-two-site-farm-business-plan-framework.md), [`Smart technology and telemetry strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md), [`Two-site operations model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md). **Connectivity (WAN) strategy** (Claxton / Demory): [`Connectivity strategy — Claxton home base and Demory farm site`](connectivity-strategy-for-claxton-and-demory.md).

**Entity anchors** (modeled sites and systems—no parcel-specific claims): [`Five-acre home base (SITE_HOME)`](../entities/five-acre-home-base-site-home-et-two-site.md), [`120-acre production farm (SITE_FARM)`](../entities/120-acre-production-farm-site-farm-et-two-site.md), [`Field telemetry network — two-site`](../entities/field-telemetry-network-two-site.md).

---

## Package map (this wiki)

| # | Deliverable | Page |
|---|-------------|------|
| 1 | **Reference architecture** (this page) | **Mermaid execution views** (reference / pilot / degraded): [`Execution topology package — two-site smart farm`](execution-topology-package-two-site-smart-farm.md) |
| 2 | Telemetry **system of record** — boundaries & authority | [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md) |
| 3 | Asset registry & spatial model — **minimum standard** | [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) |
| 4 | Instrumentation **priority matrix** | [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md) |
| 5 | **Automation principles** (early / late / never) | [`Automation principles — two-site smart farm`](automation-principles-two-site-smart-farm.md) |
| 6 | **Degraded modes** & manual fallback | [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md) + [`Automation degraded modes SOP`](automation-degraded-modes-manual-fallback-sop.md) |
| 7 | **Remote access** & operational security | [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md) |
| 8 | **Network segmentation**, **site-to-site** **policy**, **internet** **exposure** | [`Network segmentation, site-to-site connectivity, and internet exposure`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md) |
| 9 | **Off-grid** **`SITE_FARM`** **(Demory)** — **power** **+** **field** **RF** **+** **optional** **WAN** | [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md) · [`Off-grid power doctrine — Demory farm site`](off-grid-power-strategy-demory-farm-site.md) · [`Mesh and field networking strategy — off-grid Demory farm`](mesh-and-field-networking-strategy-off-grid-demory-farm.md) · [`Off-grid farm execution topology — Demory (Mermaid)`](off-grid-farm-execution-topology-demory-mermaid.md) |

**Deeper technical stack** (MQTT, broker, radio paths): [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md). **Mermaid topology** (WAN, sites, telemetry plane, DC context): [`Two-site smart farm — network topology and WAN/edge reference (Mermaid)`](two-site-smart-farm-network-topology-and-wan-edge-reference.md). **Off-grid Demory** (solar+battery default, mesh-first): [`Off-grid farm execution topology — Demory (Mermaid)`](off-grid-farm-execution-topology-demory-mermaid.md).

**Homelab backup / DR** (farmOS-class DB, containers, CSI volumes): [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md) · [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md) · [`Restore and recovery tiers — homelab farm systems`](restore-recovery-tiers-homelab-farm-systems.md) · [`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md) · [`Kubernetes platform backup / DR — Pi, k3s, Longhorn`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md) · [`Off-grid implications — backup and networking choices`](off-grid-implications-backup-and-networking-choices.md).

**Homelab Kubernetes platform** (Pi fleet, k3s, Longhorn, optional Rancher): [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md) · [`Platform strategy for farm and homestead services`](homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md) · [`Platform decision memo`](platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md) · **Provisioning runbook**: [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md).

---

## Placeholders (edit as you deploy)

| Symbol | Meaning |
|--------|---------|
| `COMMUTE_ONE_WAY` | Typical drive time **home → farm** (minutes)—drives **batching** and **acceptable outage windows** |
| `SITE_HOME_5AC` | Control center: LAN, **NOC**, workshop tooling, cold chain **option**, **primary** internet (**often** LEO satellite broadband such as **Starlink** **if** wireline absent—see WAN note below) |
| `SITE_FARM_120AC` | Production: paddocks, water, livestock/plant systems, **field gateways**, **weaker** or **no** wireline (**Starlink or LTE** uplink **when** justified—**not** assumed day one) |

### Starlink / WAN (explicit placement)

**Diagrams**: [`Two-site smart farm — network topology and WAN/edge reference (Mermaid)`](two-site-smart-farm-network-topology-and-wan-edge-reference.md).

| Site | Starlink-style LEO WAN | Architecture note |
|------|------------------------|-------------------|
| **`SITE_HOME_5AC`** | **Primary or backup** relative to any **future** fiber/cable | **Edge router + policy** sits **after** the terminal; **homelab** **does not** assume **flat L2** to the 120 ac—**VPN/overlay** reunifies **logic**, not **broadcast domains**. |
| **`SITE_FARM_120AC`** | **Conditional / deferred** | **Field gateways** need **some** uplink for cloud/MQTT; **whether** that is **second terminal**, **LTE**, or **shared** policy is a **Phase 1** decision—**avoid** funding **WAN duplication** before **water/fence** **gates**. |

**Enables**: **remote observability** and **admin** paths consistent with [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md).

**Must not silently become**: **proof** of **coverage** at **coordinates** (spec PDFs ≠ field); **substitute** for **safe physical defaults** at **`SITE_FARM_120AC`** when **backhaul** drops ([`Manual fallback`](manual-fallback-degraded-modes-critical-operations.md)).

**What changed because of Starlink analysis**: The **WAN box** in the Mermaid page is **labeled** Starlink **as an example** LEO path—this reference page **inherits** that placement **without** repeating vendor prose.

---

## Layered view (logical)

| Layer | Primary location | Role |
|-------|------------------|------|
| **Human ops** | Both; **brain** often at `SITE_HOME_5AC` | Decisions, **manual verification**, **sales/logistics** |
| **Records / books** | Usually `SITE_HOME_5AC` (office) | **Authoritative** for **financial** and **compliance** narrative—see SoR page |
| **Telemetry ingest** | `SITE_FARM_120AC` edges → backhaul → hub | **Measurements**; **not** automatically **legal** records |
| **Broker / message bus** | Hub **or** cloud—**decision** | **Transport**; **ephemeral** unless persisted per SoR rules |
| **History / DB / TSDB** | Hub **or** cloud | **Durable** **sensor** history when configured |
| **Dashboards / HA** | `SITE_HOME_5AC` | **Convenience** and **automation**; **can lie** if broker stale |
| **Alerts** | Phone / email / SMS | **Attention** routing—**not** a database |

**Authority rules** (detail): [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md).

**Video / NVR (explicit boundaries)**: IP **camera** stacks (e.g. **Frigate**) are **optional** and **not** **welfare**-grade proof alone; **`SITE_FARM`** **production** **dependence** is **deferred** per [`Local video / NVR — role and deferral boundaries (farm stack)`](local-video-nvr-role-and-deferral-boundaries-farm-stack.md). **Observability + secrets doctrine**: [`Observability, secrets, and trust bar — homelab / farm edge`](observability-secrets-and-trust-bar-homelab-farm-edge.md).

---

## Data and control flows (text diagram)

```text
[ Operators @ SITE_HOME_5AC ]  <--- commute --->  [ Field work @ SITE_FARM_120AC ]
        |                                                    |
        |  dashboards / alerts                               |  sensors / actuators / gateways
        v                                                    v
 [ Hub: broker + persistence + automation core ]  <---- backhaul (cell / fiber / PtP / mesh TBD)
        ^
        |  optional VPN / tunnel
        |
 [ Internet / DNS / remote admin paths ]  --->  see security model page
```

**Starlink note**: Replace generic “cell / fiber / PtP / mesh TBD” mentally with **documented** choices: **LEO satellite at homestead** is a **common** rural **primary**; **farm** uplink may **lag** homestead or use **LTE**—see [`Two-site operations model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md) WAN table.

---

## What “control center” must cover (minimum)

| Function | Why at 5 ac |
|----------|-------------|
| **Stable internet** (or planned failover) | Remote view of 120 ac **dies** otherwise |
| **Workshop + spares** | Field gateway **swap** without **city** detour |
| **Documentation** | **Runbooks** live **somewhere** durable—not only in heads |
| **Secure admin surface** | Patching **without** exposing **whole** farm LAN |
| **Optional cold / office** | Logistics and **food safety** paperwork |

---

## Scenarios (must be designed, not assumed away)

| Scenario | Design pressure |
|----------|-----------------|
| **`COMMUTE_ONE_WAY` too long for emergency** | **Tier** risks; **neighbor** / **hired** coverage; **reduce** need for **instant** remote fix |
| **Backhaul down** | **Local** logging or **safe defaults**; **increase** physical checks—[`Manual fallback`](manual-fallback-degraded-modes-critical-operations.md) |
| **Broker / cloud down** | Same as above; **no** silent confidence in dashboards |
| **Sensor wrong** | **Disable** closed-loop on that input; **manual** measurement—[`Sensor triage runbook`](runbook-sensor-false-positive-alert-triage.md) |
| **Maintenance backlog** | **Fewer** sensor types **beat** **more** half-maintained devices—[`Automation principles`](automation-principles-two-site-smart-farm.md) |

---

## Open items

- [ ] One-page **network list**: subnets, **VPN**, broker hostname, **who** can **admin** from where.
- [ ] **Map** `device_id` → `paddock_id` for **first** **N** instruments—[`Asset registry`](farm-spatial-model-and-asset-registry-standard.md).
- [ ] **Tabletop** exercise: **Friday night** **storm** + **LTE** **down** + **water** **unknown**.

---

## Links

- [`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md)
- [`East Tennessee two-site farm business plan — validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md)
