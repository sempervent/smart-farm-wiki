---
title: Remote access and operational security model — two-site smart farm
page_type: analysis
status: draft
created: 2026-04-18
updated: 2026-04-18
review_status: unreviewed
tags:
  - security
  - operations
  - two-site
  - remote-access
confidence: low
---

# Remote access and operational security model — two-site smart farm

## Purpose

First-draft **operational security** model for **administering** field gateways, brokers, and **homelab** services across **`SITE_HOME_5AC`** (hub) and **`SITE_FARM_120AC`** (remote production)—**without** prescribing brands. Aligns with [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md) and **business plan** risks around **homelab-as-prod** and **two-site theft / slow response**.

**Non-goals**: Full OT/IT **compliance** program; **zero trust** vendor pitch.

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

**Rule**: **Admin** paths should **not** require **exposing** **Z2** **directly** to **Z3** without **controls** (VPN, **reverse** **tunnel** with **keys**, **outbound-only** **where** **feasible**).

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

## Authentication and segmentation

| Control | Note |
|---------|------|
| **No shared** **root** **password** | **Per-user** **accounts**; **break-glass** **in** **vault** |
| **2FA** where **exposed** **to** **internet** | **Email/SMS** **weak**—prefer **TOTP** **or** **WebAuthn** |
| **Separate** **VLAN** or **SSID** for **cameras** / **IoT** | **Limit** **east-west** |
| **Field gateway** **admin** **only** **from** **Z1** **or** **tunnel**—not **wide** **open** |

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

## Open items

- [ ] **Network** **diagram** with **trust** **zones** and **admin** **paths** (even **hand-drawn** **photo** **in** **private** **store**).
- [ ] **Key** **rotation** **drill** **annually**.
- [ ] **Decide** **camera** **retention** and **who** **can** **view** **live**.

---

## Links

- [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md)
- [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md)
- [`Implementation backlog`](implementation-backlog-strategic-audit.md) — OT security depth **P2**
