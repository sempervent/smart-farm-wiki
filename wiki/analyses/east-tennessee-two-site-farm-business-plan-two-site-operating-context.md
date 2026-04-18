---
title: East Tennessee two-site farm business plan — two-site operating model
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - business-plan
  - two-site
---

# Two-site operating model

**Hub**: [`Planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)  
**Canonical ops reference**: [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md)

## Site roles

| Site | Acres (planning) | Role | Production? |
|------|------------------|------|-------------|
| **A** Homestead | ~5 | Residence; **future** smart house, workshop/basement lab, 3D print, **telemetry broker / NOC**, spares, dev | **No**—not primary commercial production |
| **B** Farm | ~120 | **Primary** land-based revenue; livestock, forage, **leased** acres if any | **Yes** |

## Why the 5-acre site is the control center

| Reason | Implication |
|--------|-------------|
| **Uptime** | Grid power, climate-stable **indoor** gear, **fast** internet for **VPN**, backups, **firmware** work |
| **Security** | **Credentials** and **VPN** termination live where **physical** access is **daily** |
| **Economics** | One **homelab / broker** stack amortized across **whole** operation—not duplicated at **120** |
| **Work pattern** | **Design / CAD / print** for **jigs and repairs** happens **at home**; **field** execution at **120** |
| **Risk** | **120** has **theft / storm / critter** exposure—**avoid** sole copy of **critical** data there |

**Should not** live **only** at 120: **secrets**, **only** copy of **records**, **only** MQTT broker **if** farm must run **safe** when **home** link is down—design **degraded** autonomy (see [`Field telemetry reference architecture`](field-telemetry-reference-architecture-homestead-120ac.md)).

## Distance economics

| Line | Formula / note |
|------|----------------|
| Round-trip time | ~**70 min** + **task** time at **120** |
| **Batch rule** | If round-trip **> ~1.5 h**, **batch** tasks to **≥ 2–3 h** **productive** work **or** **don’t** go |
| **Opportunity cost** | Optional: **replacement wage × hours** in truck (sanity check only) |

## Travel-time-aware labor design

| Principle | Implementation |
|-----------|----------------|
| **Telemetry first** where it **stops** trips | Water level, pump fault, gate position, **power** at pump |
| **Weekly rhythm** | **Fixed** **dow** for **120** (see [`Labor model and weekly rhythm`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md)) |
| **Surge weeks** | **Pre-blocked** on calendar (calving, hay, shipping)—**reduce** other commitments |
| **No “daily crop”** default | **Incompatible** with **35 min** **unless** hired labor or **resident**—**not** baseline |

## Infrastructure split (typical)

| Asset class | Preferred location |
|-------------|---------------------|
| **Broker, dashboards, backups, dev** | **Homestead** |
| **Field gateways, tank sensors, pump controls** | **120** (edge) |
| **Heavy tools, livestock handling** | **120** |
| **Spare LoRa/gateway**, **laptop** for **field** | **Both**—**spares** policy |

## Phased two-site behavior

| Phase | Two-site focus |
|-------|----------------|
| **0** | **Comms** pattern: phone, **maps**, **boundaries** documented |
| **1** | **Pilot** **one** **remote** signal (e.g. **tank** or **gate**) **home-visible** |
| **2** | **Production** visits **batched**; **records** **authoritative** in chosen **system of record** |
| **3** | **Scale** **telemetry** only with **OPEX** cap and **triage** SOP |
| **4** | **Salary** model: **fewer** **off-farm** days → **more** **batch** **flex** at **120** |

---

## Known facts

| ID | Fact |
|----|------|
| K1 | **5 ac** not primary production |
| K2 | **~35 min** separation (planning) |

## Assumptions

| ID | Assumption |
|----|------------|
| A1 | **Home** internet suitable for **VPN** **or** **cell fallback** acceptable for **non-life-critical** alerts |
| A2 | **120** has **legal** **physical** access **road** maintainable year-round |

## Open questions

| ID | Question |
|----|----------|
| Q1 | **Second** operator path when **primary** is **sick** (same household vs local hire)? |
| Q2 | **Overnight** stay acceptable at **120** (trailer, camper) for **hay** or **calving**? |
| Q3 | **Cell** coverage map at **tanks** and **gates**? |

## Operational artifact

- [`Two-site operations model — 5 ac home base, 120 ac production`](two-site-operations-model-5ac-homebase-120ac-production.md) — fillable **SITE_HOME** / **SITE_FARM** split, batch rules, infrastructure table.

## Links

- [`Smart-tech strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)
- [`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md)
- [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md)
