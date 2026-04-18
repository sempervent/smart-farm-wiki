---
title: East Tennessee two-site farm business plan — two-site operating model
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-21
review_status: unreviewed
tags:
  - business-plan
  - two-site
---

# Two-site operating model

**Hub**: [`Planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)  
**Canonical ops reference (distance-tax, batching, tables)**: [`Two-site operations model — 5 ac home base, 120 ac production`](two-site-operations-model-5ac-homebase-120ac-production.md)  
**Generic pattern (no ET names)**: [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md)

**First-class filters** (same brief as the **35-minute** split): [`Trip batching and site visit policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md), [`Two-site structure disqualifiers`](two-site-structure-disqualifiers-east-tennessee.md).

## Site roles

| Site | Acres (planning) | Role | Production? |
|------|------------------|------|-------------|
| **A** Homestead (`SITE_HOME`) | ~5 | Residence; **future** smart house, workshop/basement lab, 3D print, **telemetry broker / NOC**, spares, dev | **No**—not primary commercial production |
| **B** Farm (`SITE_FARM`) | ~120 | **Primary** land-based revenue; livestock, forage, **leased** acres if any | **Yes** |

## Why the 5-acre site is the control center

| Reason | Implication |
|--------|-------------|
| **Uptime** | Grid power, climate-stable **indoor** gear, **fast** internet for **VPN**, backups, **firmware** work |
| **Security** | **Credentials** and **VPN** termination live where **physical** access is **daily** |
| **Economics** | One **homelab / broker** stack amortized across **whole** operation—not duplicated at **120** |
| **Work pattern** | **Design / CAD / print** for **jigs and repairs** happens **at home**; **field** execution at **120** |
| **Risk** | **120** has **theft / storm / critter** exposure—**avoid** sole copy of **critical** data there |

**Should not** live **only** at 120: **secrets**, **only** copy of **records**, **only** MQTT broker **if** farm must run **safe** when **home** link is down—design **degraded** autonomy (see [`Field telemetry reference architecture`](field-telemetry-reference-architecture-homestead-120ac.md)).

## The 35-minute split (structural, not a small detail)

**`COMMUTE_ONE_WAY` ≈ 35 min** means **~70 min** round-trip **in the cab** before **`τ_ctx`** and before **any** **productive** work at **`SITE_FARM`**. That is a **distance tax** on **every** round trip: **vehicle OPEX**, **loaded labor**, **attention**, and—when trips are **junk**—**morale**.

**Non-negotiables for this package**

- **Routine unnecessary trips** **destroy** **margin** and **morale**; treat them as **operating failures**, not quirks.
- **Batching** and **low daily physical touch** are **design requirements**, not optimizations after the fact.
- **Remote observability** is **mandatory** for **P1** loads (water/power/gate class) before **sensor sprawl** elsewhere—see [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md) and [`trip policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md).

**Authoritative rules + formulas**: [`Distance-tax rules`](two-site-operations-model-5ac-homebase-120ac-production.md#distance-tax-rules-explicit) on the **5 ac / 120 ac** page (**DT-0–DT-6**, **`R_SPLIT`** linkage).

## Travel-time-aware labor design

| Principle | Implementation |
|-----------|----------------|
| **Telemetry first** where it **stops** trips | Water level, pump fault, gate position, **power** at pump |
| **Weekly rhythm** | **Fixed** **dow** for **120** (see [`Labor model and weekly rhythm`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md)) |
| **Surge weeks** | **Pre-blocked** on calendar (calving, hay, shipping)—**reduce** other commitments |
| **No “daily crop” default** | **Incompatible** with **35 min** **unless** hired labor or **resident**—**not** baseline |
| **Enterprise filter** | [`Enterprise options analysis`](east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md) **Split tax** column + [`disqualifiers`](two-site-structure-disqualifiers-east-tennessee.md) |

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
| **0** | **Comms** pattern: phone, **maps**, **boundaries** documented; **no** **myth** that “**we’ll** **pop** **out** **daily**” |
| **1** | **Pilot** **one** **remote** signal (e.g. **tank** or **gate**) **home-visible**; **trip** **justification** **discipline** **starts** |
| **2** | **Production** visits **batched**; **records** **authoritative** in chosen **system of record**; **`R_SPLIT`** **visible** |
| **3** | **Scale** **telemetry** only with **OPEX** cap and **triage** SOP (**`H_TRIAGE`** ceiling) |
| **4** | **Salary** model: **fewer** **off-farm** days → **more** **batch** **flex** at **120**—**not** **more** **junk** **trips** |

---

## Known facts

| ID | Fact |
|----|------|
| K1 | **5 ac** not primary production |
| K2 | **~35 min** separation (planning)—**measure** |

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

- [`Two-site operations model — 5 ac home base, 120 ac production`](two-site-operations-model-5ac-homebase-120ac-production.md) — **distance-tax**, **SITE_HOME** / **SITE_FARM** split, infrastructure table.

## Links

- [`Smart-tech strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)
- [`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md)
- [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md)
