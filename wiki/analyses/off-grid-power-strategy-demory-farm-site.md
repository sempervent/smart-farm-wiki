---
title: Off-grid power doctrine — Demory farm site (Campbell County)
page_type: analysis
status: active
created: 2026-04-24
updated: 2026-04-17
review_status: unreviewed
tags:
  - off-grid
  - solar
  - battery
  - demory
  - site-farm
confidence: medium
aliases:
  - Demory off-grid power strategy
  - Off-grid power strategy Demory farm site
---

# Off-grid power doctrine — Demory farm site (Campbell County)

## Purpose

Give **canonical planning guidance** for **`SITE_FARM`** at **[Demory](demory-farm-site-intelligence.md)** (**Campbell County**) when the **business plan** treats the **production parcel** as **off-grid-first**: **solar + battery** as the **default** **electrical** **architecture**, **without** inventing **array kW**, **battery Ah**, or **NEC** **details** **—** those require **local** **engineering** **after** **measured** **loads** **.**

**Doctrine package** (full map: tiers, field nodes, WAN deps, degraded modes, stop rules): [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md).

**Sources (provenance)**: [`Off-grid power, field RF, and optional WAN — source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) (NREL modules 5–6, Victron *Wiring Unlimited*, captures).

**Paired pages**: [`Power domains and battery-backed infrastructure tiers — Demory`](off-grid-power-domains-and-battery-tiers-demory-farm.md), [`Mesh and field networking strategy — off-grid Demory farm`](mesh-and-field-networking-strategy-off-grid-demory-farm.md), [`Off-grid farm execution topology — Demory (Mermaid)`](off-grid-farm-execution-topology-demory-mermaid.md), [`Connectivity strategy — Claxton & Demory`](connectivity-strategy-for-claxton-and-demory.md) (**WAN** **secondary** **to** **local** **survivability** **at** **farm** **).**

---

## Architectural stance (policy)

| Stance | Meaning |
|--------|---------|
| **Off-grid-first** | **Utility** **tie** **is** **not** **assumed** **for** **core** **farm** **loads** **;** **design** **for** **standalone** **PV** **+** **storage** **+** **optional** **genset** **per** **NREL** **framing** **(DC/AC/hybrid** **coupling** **choices** **)** **.** |
| **Solar + battery default** | **Battery** **is** **the** **energy** **buffer** **for** **night** **,** **cloud** **,** **and** **surge** **loads** **;** **sizing** **is** **TBD** **.** |
| **Networking is a load** | **Always-on** **radios** **,** **gateways** **,** **and** **Starlink** **CPE** **draw** **real** **Wh/day** **—** **budget** **them** **with** **other** **infrastructure** **,** **not** **as** **“** **free** **”** **.** |

**What we do not claim here**: optimal **string** **voltage** **,** **BMS** **SKU** **,** **grounding** **solution** **—** cite **NEC** **/** **AHJ** **with** **a** **PE** **.**

---

## What should be powered continuously (policy)

| Category | Examples (illustrative) | Notes |
|----------|-------------------------|--------|
| **Safety / welfare interlocks** | **Pump** **controller** **logic** **that** **prevents** **dry** **run** **;** **gate** **fail-safe** **solenoids** **where** **required** | **Must** **fail** **safe** **without** **cloud** **;** **may** **still** **need** **local** **power** **discipline** **.** |
| **Core field gateway “spine”** | **One** **MQTT** **/** **edge** **node** **that** **aggregates** **sensors** | **Define** **“** **minimum** **uptime** **”** **vs** **duty-cycled** **repeaters** **(see** **mesh** **strategy** **)** **.** |
| **Minimal comms for operator** | **One** **mesh** **or** **LTE** **path** **for** **Tier-1** **alerts** **(policy** **)** | **Not** **every** **sensor** **—** **the** **smallest** **set** **that** **meets** **coverage** **matrix** **.** |

---

## What should be duty-cycled or event-driven

| Category | Examples | Notes |
|----------|----------|--------|
| **Mesh repeaters** **/** **Meshtastic** **nodes** | **Remote** **hills** **/** **fence** **line** | **Power-saving** **modes** **,** **light** **sleep** **,** **solar** **+** **small** **local** **battery** **per** **Meshtastic** **power** **docs** **(**[`source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md)**)** **.** |
| **Cameras** **/** **NVR** | **Motion** **or** **scheduled** **recording** | **Continuous** **4K** **everywhere** **is** **a** **luxury** **load** **—** **match** **to** **pilot** **phase** **.** |
| **Starlink** **/** **optional** **WAN** | **Powered** **only** **when** **egress** **or** **admin** **window** **needed** **(policy** **)** | **Treat** **as** **sheddable** **during** **deep** **SOC** **events** **unless** **you** **explicitly** **classify** **it** **as** **critical** **(**[`Off-grid degraded modes`](off-grid-degraded-modes-power-and-connectivity-demory-farm.md)**)** **.** |
| **Wi‑Fi HaLow** **/** **AP** **radios** | **High** **airtime** **when** **no** **traffic** | **Design** **for** **sleep** **/** **beacon** **interval** **tradeoffs** **—** **see** **comparison** **page** **.** |

---

## Solar + battery implications of always-on networking

- **NREL** **module** **6** **emphasizes** **O&M** **discipline** **(inspection** **,** **cleaning** **,** **fault** **response** **)** **—** **telemetry** **that** **reduces** **truck** **rolls** **still** **adds** **constant** **draw** **if** **always** **on** **.**
- **Always-on** **IP** **radios** **+** **edge** **compute** **compete** **with** **water** **pumps** **,** **cold** **chain** **,** **and** **winter** **hay** **handling** **for** **the** **same** **battery** **SOC** **—** **document** **priority** **loads** **before** **scaling** **RF** **fleet** **.**
- **Placeholder** **:** **`P_NET_ALWAYS_W`** **=** **___** **W** **(meter** **)** **;** **`E_NET_DAY`** **=** **___** **Wh/day** **.**

---

## Maintenance burden (operator-real)

| Area | Burden |
|------|--------|
| **Battery** **/ BMS** | **Cell** **balance** **,** **temp** **,** **contactor** **health** **—** **NREL** **O&M** **themes** **.** |
| **PV** **array** | **Soiling** **,** **snow** **,** **vegetation** **shading** **new** **growth** **.** |
| **Inverter** **/** **charger** | **Firmware** **,** **wiring** **torque** **checks** **(Victron** **discipline** **)** **.** |
| **Field** **network** **gear** | **Firmware** **churn** **on** **mesh** **;** **physical** **theft** **/** **lightning** **at** **120** **ac** **.**

---

## Pilot vs scale

| Phase | Power expectation |
|-------|-------------------|
| **Phase** **0–1** **(pilot** **)** | **One** **proven** **DC** **bus** **segment** **+** **one** **gateway** **+** **minimal** **always-on** **RF** **;** **measure** **before** **second** **array** **string** **or** **second** **battery** **bank** **.** |
| **Scale** | **Redundant** **PV** **,** **genset** **policy** **,** **load** **shedding** **bus** **—** **only** **after** **G1** **/** **water** **/** **fence** **gates** **per** **business** **plan** **.** |

---

## Related

- [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md)
- [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md)
- [`Runbook — power loss at remote site`](runbook-power-loss-remote-site.md)
- [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md)
