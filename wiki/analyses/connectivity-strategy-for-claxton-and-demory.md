---
title: Connectivity strategy — Claxton home base and Demory farm site
page_type: analysis
status: active
created: 2026-04-24
updated: 2026-04-24
review_status: unreviewed
tags:
  - two-site
  - connectivity
  - wan
  - starlink
  - east-tennessee
confidence: medium
aliases:
  - Two-site connectivity strategy (Claxton / Demory)
---

# Connectivity strategy — Claxton home base and Demory farm site

## Purpose

Give a **single canonical** statement of **how the two-site farm expects to reach the Internet and administer remote systems**, with **named places**: **`SITE_HOME`** — [Claxton](../entities/claxton-home-base.md) / [Anderson County](../entities/anderson-county-tennessee.md); **`SITE_FARM`** — [Demory](../entities/demory-farm-site.md) / [Campbell County](../entities/campbell-county-tennessee.md). This page **does not** replace the **diagram-level** Starlink/WAN analysis ([`Two-site smart farm — network topology and WAN/edge reference (Mermaid)`](two-site-smart-farm-network-topology-and-wan-edge-reference.md)) or the **logical stack** ([`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md))—it **routes** decisions and **names assumptions** for pilots and scale-up.

**Execution topology package** (reference / pilot / degraded Mermaid): [`Execution topology package — two-site smart farm (Mermaid)`](execution-topology-package-two-site-smart-farm.md).

**First-24-months validation track** (survey, power, WAN testing, remote access, cost stops): [`Validation and pilot plan` § Connectivity validation](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation).

**Supplementary diagrams** (telemetry plane, DC, HaLow overlay): [`Two-site smart farm — network topology and WAN/edge reference (Mermaid)`](two-site-smart-farm-network-topology-and-wan-edge-reference.md).

**Raw / spec grounding** (PDFs and captures, not operational truth at coordinates): [`Electrical, networking, and Starlink — inbox batch (2026-04-23)`](../source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md).

**`SITE_FARM` / Demory — off-grid-first planning stance**: **solar** **+** **battery** **default** **;** **local** **mesh** **/** **field** **RF** **before** **relying** **on** **Starlink** **/** **LTE** **for** **operations** **—** [`Demory farm — site intelligence`](demory-farm-site-intelligence.md) **§** **Off-grid-first** **,** [`Off-grid power strategy — Demory farm site`](off-grid-power-strategy-demory-farm-site.md) **,** [`Mesh and field networking strategy — off-grid Demory farm`](mesh-and-field-networking-strategy-off-grid-demory-farm.md) **.**

---

## Starlink / LEO broadband — role by site

| Site | Place (named) | **Role** | Operating note |
|------|-----------------|----------|----------------|
| **`SITE_HOME`** | Claxton (Anderson) | **Primary WAN candidate** *or* **backup** to future **terrestrial** (fiber/cable) where available | Treat **wireline as prove-it**: document **which uplink is primary** and **failover** before relying on dashboards for **welfare** decisions. |
| **`SITE_FARM`** | Demory (Campbell) | **Conditional** second uplink **or** **deferred** | Justify **hardware + subscription** with **Phase 1** traffic and **labor ROI**—avoid **duplicating** “brains” or **WAN** before **fence/water** gates ([`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md)). |

**Enables** (both sites, when deployed): batched trips with **remote checks**, admin/VPN paths, MQTT/cloud egress from **field gateways**, maps and comms while mobile.

**Must not silently become**: the **only** path for **authoritative books** without **offline export**; a substitute for **physical** water/livestock checks; **assumed** bandwidth for **dense camera mesh**; **proof** of **coverage at coordinates** (specs ≠ field—validate per [`Validation and pilot plan — first 24 months`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md)).

---

## Terrestrial Internet assumptions

- **Homestead / Claxton**: **Cable or fiber** may exist—**survey and log** addresses **before** locking **CAPEX**. If **wireline is absent or poor**, **LEO satellite** (e.g. Starlink-class) is a **realistic first stable Internet** for the **control center**; still **document** latency, data caps (if any), and **outage** behavior.
- **Farm / Demory**: **Buried fiber to the field** is **not** assumed **day one**. **Last mile** may be **LTE**, **satellite**, or **none**—**field gateways** should **buffer** and **fail safe** when **WAN** is **gone** ([`Manual fallback and degraded modes`](manual-fallback-degraded-modes-critical-operations.md)).

---

## LTE / cellular fallback assumptions

- **LTE** is the **usual** **backup or parallel** path where **tower coverage** exists—**drive-test** and **log** **bars vs usable data** at **pins** that matter (gates, tanks, barn), not only at the driveway ([`Validation and pilot plan`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) **V10** angle).
- **Assume** **carrier CGNAT**, **variable** routing, and **possible** **throttling**—**do not** depend on **stable inbound** to **field CPE** for **admin** without **outbound-initiated** tunnels or a **rendezvous** you control ([`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md)).
- **Satellite WAN impaired** (rain fade, obstruction, **power loss at terminal**) should **fall through** to **LTE** **where** **provisioned**—otherwise treat as **comms down** for **remote trust** ([`Automation degraded modes SOP`](automation-degraded-modes-manual-fallback-sop.md) failure class **A2**).

---

## Local-only versus WAN-dependent systems

| Class | Examples (illustrative) | WAN required? |
|-------|---------------------------|---------------|
| **Local-only / must run disconnected** | Gate **fail-safe** defaults, **tank level** at pump (local interlocks), **LoRa/Meshtastic** **sensor mesh** to a **field gateway** **without** cloud, **NVR** **recording** on-site | **No** for **core safety**; gateway may **buffer** uploads |
| **WAN-nice** | **Home Assistant** dashboards at home, **Grafana** history, **email/SMS** alerts | **Yes** for **real-time** remote view—**degraded** = **stale or silent** |
| **WAN-dependent (by design)** | **Cloud MQTT**, **hosted** TSDB, **remote** **patch** **windows**, **off-site backup** **only** if **no** **local** replica | **Yes**—**document** **outage playbook** |

**Architecture boundary**: [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md) — **telemetry vs SoR**, **broker** placement.

---

## Power dependencies and outage implications

- **Starlink (and most CPE)** **needs continuous power**: **WAN loss** during **utility outage** may be **even if** **radios** still work locally—**do not** equate **“generator on”** with **“Internet up”** without **explicit** **UPS/branch** design for **modem/terminal** (see **DC / AC** patterns in [`Network topology (Mermaid)`](two-site-smart-farm-network-topology-and-wan-edge-reference.md) and power entities [`Farm on-site power system`](../entities/farm-on-site-power-system.md)).
- **LTE routers** share the same rule: **no power** → **no fallback path**.
- **Local mesh / LoRa** may **outlive** **WAN** **if** **gateways** and **sensors** stay powered—**alerts** may **silence** **without** implying **“all clear”** at the **animal** or **water** level.

---

## Cost implications

- **OPEX**: treat **ISP + cellular + LEO subscription** as **explicit** line items (not **generic “tech”**)—see [`Capital plan and infrastructure sequencing`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md) **Tech** row and **Starlink / farm WAN** sequencing note.
- **Deferral discipline**: **second** terminal or **redundant** **farm** **WAN** **after** **Phase 1** **comms proof**—align with [`Two-site operations model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md) **WAN** table.
- **Spares**: budget **cable, router, or radio spares** **proportionally** to **revenue** **risk** of **silent telemetry**—not **zero**, not **infinite**.

---

## Remote access and security implications

- **LEO path** is still **untrusted Internet** (**Z3a** in the security model)—**encrypted tunnels**, **scoped** creds, **no** **flat** **admin** from **satellite** “privacy” **feel** ([`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md)).
- **CGNAT / dynamic** addressing favors **outbound** VPN or **controlled** **rendezvous**—**document** **one primary** **admin pattern**.

**Network policy** (segmentation of cameras, gateways, telemetry, admin, and user devices; **site-to-site** assumptions; **VPN**/**overlay**; **what** **may** **be** **Internet-reachable**): [`Network segmentation, site-to-site connectivity, and internet exposure — two-site smart farm`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md). **MV**/**CS** hooks: [`Remote access…` § Execution and validation hooks](remote-access-operational-security-model-two-site-smart-farm.md#execution-and-validation-hooks).

---

## Farm functions: WAN required vs must tolerate WAN loss

| Function | WAN expectation | If WAN is gone |
|----------|-----------------|----------------|
| **Livestock welfare** (water, escape) | **Helpful**, not **proof** | **Physical rounds**; **local** **alarms**; **no** **dashboard** as **SoR** |
| **Irrigation / pumps** (safety interlocks) | **Optional** for **core** **interlock** | **Local** **logic**; **manual** **override** per **runbook** |
| **Telemetry history / dashboards** | **Required** for **cloud** **history** | **Buffer** at **edge**; **stale** **OK** **if** **labeled** |
| **Books / compliance records** | **Often cloud**—**must** have **offline** **export** **policy** | **Paper** **or** **local** **file** **per** **SoR** |
| **Trip batching / “should I drive?”** | **Uses** WAN for **remote** **peek** | **Assume** **unknown**—**drive** **if** **Tier-1** **or** **policy** **says** **so** ([`Trip batching and site visit policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md)) |

---

## Pilot phase vs scale phase — connectivity expectations

| Phase | Expectation |
|-------|-------------|
| **Pilot (Phase 0–1 / first proofs)** | **Prove** **one** **honest** **uplink story** per site **where** needed: **drive-tests**, **logged** **outages**, **degraded** **drills**. **Defer** **second** **farm** **terminal** **unless** **G8**/manual baseline **and** **V10** **evidence** **require** it. **LTE** may be **enough** for **early** **field** **egress**. |
| **Scale (later phases)** | **Redundancy** **only** **after** **ROI**: **dual path** (e.g. **LEO + LTE**), **spares**, **higher** **alert** **routing** **maturity**. **Still** **no** **welfare** **dependence** on **WAN** **without** **manual** **fallback** ([`Manual fallback and degraded modes`](manual-fallback-degraded-modes-critical-operations.md)). |

**Gates and calendar**: [`Validation and pilot plan — first 24 months`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md); **phase bands**: [`Phase timeline`](../timelines/east-tennessee-two-site-farm-business-plan-phase-timeline.md).

---

## Related pages (execution spine)

| Kind | Link |
|------|------|
| **Business plan package** | [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) |
| **Planning framework** | [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md) |
| **Smart technology & telemetry** | [`Smart technology and telemetry strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) |
| **Two-site operations (distance tax + WAN table)** | [`Two-site operations model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md) |
| **Execution dossier (Phase 0–1)** | [`Execution dossier hub — Phase 0–1`](execution-dossier-hub-phase-0-1-east-tennessee.md) |
| **Reference architecture** | [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md) |
| **Starlink / WAN diagram analysis** | [`Two-site smart farm — network topology and WAN/edge (Mermaid)`](two-site-smart-farm-network-topology-and-wan-edge-reference.md) |
| **Degraded modes (runbooks)** | [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md), [`Automation degraded modes — manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md) |
| **Remote access & security** | [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md) |
| **Segmentation & internet exposure** | [`Network segmentation, site-to-site connectivity, and internet exposure`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md) |

---

## Operations hub

**Router**: [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md).
