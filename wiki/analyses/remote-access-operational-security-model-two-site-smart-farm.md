---
title: Remote access and operational security model — two-site smart farm
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-24
review_status: unreviewed
tags:
  - security
  - operations
  - two-site
  - remote-access
confidence: medium
---

# Remote access and operational security model — two-site smart farm

## Purpose

**Canonical** **operational** **security** **model** **for** **remote** **administration** **of** **field** **gateways**, **brokers**, **and** **homelab** **services** **across** **`SITE_HOME_5AC`** **(hub)** **and** **`SITE_FARM_120AC`** **(remote** **production** **)** **—** **architecture** **and** **policy**, **not** **vendor** **shopping** **lists** **.** **Aligns** **with** [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md) **and** **business** **plan** **risks** **around** **homelab-as-prod** **and** **two-site** **theft** **/** **slow** **response** **.**

**Companion** **(segmentation** **/** **site-to-site** **/** **what** **may** **face** **the** **Internet** **)** **:** [`Network segmentation, site-to-site connectivity, and internet exposure — two-site smart farm`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md) **.**

**WAN** **roles** **(Claxton** **/** **Demory** **)** **:** [`Connectivity strategy — Claxton home base and Demory farm site`](connectivity-strategy-for-claxton-and-demory.md) **.**

**Non-goals**: Full OT/IT **compliance** program; **zero trust** vendor pitch; **replacing** **a** **private** **network** **diagram** **in** **your** **runbook** **store** **.**

### Starlink / LEO WAN — security stance (transport, not trust)

**Connectivity** **facts** **(primary** **/** **backup** **/** **deferred** **per** **site** **)** **are** **on** [`Two-site operations model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md) **and** [`Smart technology and telemetry strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) **.** **Diagrams** **:** [`Execution topology package — two-site smart farm (Mermaid)`](execution-topology-package-two-site-smart-farm.md) **,** [`Two-site smart farm — network topology and WAN/edge reference (Mermaid)`](two-site-smart-farm-network-topology-and-wan-edge-reference.md) **.**

| Principle | Implication |
|-------------|-------------|
| **LEO** **satellite** **WAN** **is** **still** **Z3** **/** **Z3a** | **Same** **encryption** **and** **identity** **burden** **as** **cable** **/** **LTE** **—** **no** **“** **private** **link** **”** **exception** **.** |
| **CGNAT** **/** **dynamic** **addressing** **are** **normal** | **Admin** **paths** **favor** **outbound-initiated** **tunnels** **or** **cloud** **rendezvous** **you** **control** **—** **see** [`Network segmentation…` § VPN / overlay](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md#vpn-overlay-assumptions) **.** |
| **Weather** **/** **obstruction** **outages** | **Treat** **as** **security** **+** **ops** **event** **:** **sessions** **die** **;** **remote** **trust** **drops** **to** **zero** **for** **real-time** **welfare** **—** [`Manual fallback and degraded modes`](manual-fallback-degraded-modes-critical-operations.md) **,** [`Automation degraded modes SOP`](automation-degraded-modes-manual-fallback-sop.md) **.** |
| **Second** **terminal** **/** **farm** **uplink** | **Increases** **physical** **and** **config** **surface** **—** **defer** **until** **Phase** **1** **proof** **per** [`Validation plan — Connectivity validation`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation) **.** |

---

## Actors and assets

| Actor | Typical need |
|-------|--------------|
| **Owner / admin** | Patch **broker**, **gateway**, **VPN**; **restore** from backup |
| **Family operator** | **Dashboards**, **acknowledge** alerts—not **root** on **everything** |
| **Vendor / MSP** (optional) | **Scoped** access **window** |
| **Attacker** (assumed) | **Scans** on **public** **IP**, **stolen** **credentials**, **local** **physical** access at **unattended** **120 ac** |

**Assets**: **Gateways**, **brokers**, **Home Assistant / Grafana**, **cameras**, **NVR**, **field** **LTE** **router**, **laptops** used for **admin**.

---

## Trust zones (conceptual)

| Zone | Location | Trust assumption |
|------|----------|------------------|
| **Z1** | **Home LAN** at `SITE_HOME_5AC` | **Higher** **control**; **still** not **trusted** for **flat** **admin** to **field** |
| **Z2** | **Field** **OT-ish** network at `SITE_FARM_120AC` | **Assume** **hostile** **Wi‑Fi** / **mesh**; **limit** **lateral** **movement** |
| **Z3** | **Internet** | **Hostile**; **no** **unauthenticated** **admin** |
| **Z3a** | **LEO satellite WAN** (e.g. **Starlink** path into **Z1** or **field CPE**) | **Same as Z3** for **admin**—**encrypted** **tunnels** **only**; **no** **trust** in **“private”** **because** **satellite** |

**Rule**: **Admin** paths should **not** require **exposing** **Z2** **directly** to **Z3** without **controls** (VPN, **reverse** **tunnel** with **keys**, **outbound-only** **where** **feasible**).

**Starlink-specific**: **Carrier-grade NAT / dynamic addressing** and **weather-linked** **outages** are **normal**—**do not** build **security** that **requires** **stable** **inbound** **to** **field** **without** **outbound-initiated** **tunnels** or **cloud** **rendezvous** you **control**.

---

## Remote access patterns (choose and document **one primary**)

| Pattern | Favors | Risks |
|---------|--------|-------|
| **VPN** to home, then **internal** **hop** to field | **Central** **policy** | **VPN** **SPOF**; **key** **management** |
| **Outbound** **tunnel** from field (**SSH** **reverse**, **WireGuard** **initiated** **from** **field**) | **No** **inbound** **ports** on **field** **LTE** | **Tunnel** **service** **availability** |
| **Cloud** **broker** + **TLS** | **Less** **port** **forwarding** at home | **Vendor** **dependency**, **data** **residency** |
| **RDP/SSH** **exposed** **on** **public** **IP** | **Never** **default** | **Brute** **force**, **credential** **stuffing** |

**Placeholder**: `PRIMARY_REMOTE_ADMIN_PATTERN = ___` (document **in** **private** **runbook** if sensitive).

---

## Authentication and segmentation (controls)

| Control | Note |
|---------|------|
| **No shared** **root** **password** | **Per-user** **accounts**; **break-glass** **in** **vault** |
| **2FA** where **exposed** **to** **internet** | **Email/SMS** **weak**—prefer **TOTP** **or** **WebAuthn** |
| **Separate** **VLAN** or **SSID** for **cameras** / **IoT** | **Limit** **east-west** |
| **Field gateway** **admin** **only** **from** **Z1** **or** **tunnel**—not **wide** **open** |

**Full** **segmentation** **matrix** **(cameras,** **gateways,** **telemetry,** **admin,** **user** **devices** **)** **and** **internet** **exposure** **policy** **:** [`Network segmentation, site-to-site connectivity, and internet exposure`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md) **.**

---

## Patching and maintenance burden (explicit)

| Item | Owner | Cadence placeholder |
|------|-------|---------------------|
| **Broker** | | **Monthly** minimum |
| **Gateways** | | **Quarterly** or **on** **CVE** |
| **HA / Grafana** | | Same |
| **LTE** **router** firmware | | **Check** **quarterly** |
| **TLS** **certs** | | **Automation** **or** **calendar** |

**Rule**: If **patch** **cadence** **cannot** be **met**, **reduce** **attack** **surface** (**fewer** **services**, **more** **managed**)—[`Automation principles`](automation-principles-two-site-smart-farm.md).

---

## Physical and two-site context

| Risk | Mitigation (architecture-level) |
|------|----------------------------------|
| **Theft** of **gateway** / **camera** **NVR** at **120 ac** | **Encrypt** **drives**; **no** **secrets** **only** **on** **device**; **revoke** **keys** **procedure** |
| **Slow** **response** when **alert** **fires** | **Design** **systems** **so** **wrong** **state** **is** **safe** **long** **enough** for **`COMMUTE_ONE_WAY`** |
| **Insider** **misclick** | **RBAC**; **separate** **“view”** vs **“actuate”** |

---

## Logging and accountability

| Event | Log **where** |
|-------|----------------|
| **Admin** **login** **success/fail** | Central **if** possible |
| **Config** **change** **(automation** **rule)** | **Version** **control** **or** **export** **after** **change** |
| **Remote** **gate** **command** | **Correlate** **with** **user** **+** **time** |

---

## Ingested references (patterns, not endorsements)

- CISA primers on **remote** **access** and **OT** **inventory** (see `wiki/source-notes/` **cisa-*** files).
- [`Field telemetry reference architecture`](field-telemetry-reference-architecture-homestead-120ac.md) — **admin** **access** **question** **Q5**.

---

<h2 id="execution-and-validation-hooks">Execution and validation hooks</h2>

| Hook | How this page ties in |
|------|------------------------|
| **MV-6** **(cyber:** **remote** **surface** **)** | **Inventory** **must** **match** **documented** **admin** **pattern** **and** [`Internet exposure policy`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md#internet-exposure-policy) **—** [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) **.** |
| **MV-7** **(WAN** **fade** **drill** **)** | **Proves** **no** **welfare** **/** **trip** **reliance** **on** **live** **cloud** **when** **Z3** **is** **impaired** **.** |
| **CS-3** | **Freeze** **if** **remote** **access** **inventory** **incomplete** **before** **fleet** **expansion** **.** |
| **Connectivity** **validation** **—** **remote** **access** **hardening** | [`Validation plan — Connectivity validation`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation) **—** **before** **production** **reliance** **on** **dashboards** **/** **telemetry** **egress** **.** |
| **Business** **plan** **execution** | [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) **—** **Phase** **0–1** **discipline** **;** **named** **owners** **for** **homelab** **/** **prod** **boundary** **.** |

---

## Open items

- [ ] **Network** **diagram** with **trust** **zones** **and** **admin** **paths** **(even** **hand-drawn** **photo** **in** **private** **store** **)** **—** **align** **with** [`Execution topology package`](execution-topology-package-two-site-smart-farm.md) **.** 
- [ ] **Key** **rotation** **drill** **annually** **.** 
- [ ] **Decide** **camera** **retention** **and** **who** **can** **view** **live** **(see** **segmentation** **table** **)** **.** 

---

## Links

- [`Network segmentation, site-to-site connectivity, and internet exposure`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md)
- [`Connectivity strategy — Claxton & Demory`](connectivity-strategy-for-claxton-and-demory.md)
- [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md)
- [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md)
- [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md)
- [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md)
- [`Implementation backlog`](implementation-backlog-strategic-audit.md) — OT security depth **P2**
