---
title: Smart technology and telemetry strategy — control center on 5 acres
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - business-plan
  - automation
  - telemetry
  - two-site
confidence: medium
aliases:
  - East Tennessee two-site farm business plan — smart technology, telemetry, and automation
---

# Smart technology and telemetry strategy — control center on 5 acres

## Purpose

Define how **telemetry and automation** support a **two-site** operation where the **~5-acre homestead** is the long-run **control center** (stable power, daily access, primary **broker**, backups, development) and the **~120-acre farm** holds **production risk** and **field edge**. The strategy treats automation as **capital + OPEX + maintenance + false positives + cyber exposure**—not as labor elimination by default.

This page remains **valid** while **radio technology**, **stack**, and **sensor count** are still open; it sets **rules** and **sequence**.

**Architecture reference**: [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md).  
**Registry / naming**: [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md).  
**Hub**: [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md).

## Decisions supported by this page

| Decision | This page provides |
|----------|-------------------|
| **What** to deploy **before** Phase 2 production | Pilot list + “do not automate yet” |
| **Where** the **broker** and **secrets** live | Homestead vs field split |
| **When** remote control is allowed | Manual proof gates |
| **OPEX cap** for subscriptions and on-call time | Alert budget + triage discipline |

## Why the control center is on the 5-acre parcel

| Reason | Implication |
|--------|-------------|
| **Uptime and access** | Grid power and daily presence beat remote rack in a barn for **patching**, **backups**, **credential** hygiene |
| **Security** | VPN and credentials terminate where **physical** access is **routine** |
| **Amortization** | One **homelab** stack serves the whole operation—**avoid** duplicating “brains” at `SITE_FARM` |
| **Separation of concerns** | **Mess, theft exposure, and weather** concentrate at **120**; **stable compute** stays **home** |

**Constraint**: If the **only** copy of **critical** logic lives at home, **design degraded behavior** at **120** when **backhaul fails** ([`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md)).

## Principles

1. **Telemetry must reduce trips or provable risk**—otherwise it is **cost**, not ROI.
2. **Manual process before automation**: named assets, defined good/bad, **one season** of logs before tuning alerts.
3. **Degraded modes first**: broker down, power down, alert flood ([`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md), runbooks below).
4. **One system of record** for operational events (e.g. farmOS-class)—MQTT is **transport** unless you **explicitly** choose otherwise.

## What to prioritize early (Phase 0–1)

| Item | Why | Caveat |
|------|-----|--------|
| Maps + parcel/paddock IDs | Every sensor binds to **land** | No geometry → orphan data |
| One **water or pump** monitor | Highest trip-avoidance per dollar at distance | Calibrate; plan for **freeze** |
| Power awareness at remote pump/gateway | Explains “silent” failures | Not a substitute for **genset** / transfer plan |
| Backup + tested restore at **home** | Brain survives disk | **Test** restore on a schedule |

## What not to automate early

| Item | Why wait |
|------|----------|
| Camera mesh everywhere | Bandwidth, storage, privacy, **triage** load |
| Herd-wide GPS collars | OPEX, vendor lock; often weak ROI at **small** herd |
| Full irrigation automation | Skill + crop commitment—off **default** grazing path until Phase 3+ if ever |
| “AI” on edge | After **SOPs** and **labels** exist |

## Manual proof gates (before remote actuation)

| Proof | Before… |
|-------|-----------|
| Water system behavior (stick, timer, visual) | Remote setpoints / auto pump logic |
| Gate **safe default** policy written | Remote gate control |
| Weekly animal check rhythm sustainable | Escalation rules on alerts |
| At least one **successful** sale channel touch | Scaling inventory |

## Stack posture by phase

| Phase | Posture |
|-------|---------|
| 0 | Spreadsheets + photos; avoid **cloud-only** for compliance-critical records |
| 1 | Pilot: MQTT → broker at **home**; 1–2 field nodes; **document** topics |
| 2 | System of record live; duplicate MQTT consumers only with a **written** reason |
| 3 | Observability: uptime, alert budget, **spares list** |
| 4 | Hardening: segmentation, patch cadence, key rotation |

## Failure modes (expect them)

| Mode | Expectation |
|------|-------------|
| Backhaul down | Field edge **fails safe**; **increase** physical check frequency per runbook |
| Power loss at 120 | Tanks drain; pumps don’t self-fix—[`Runbook — power loss at remote site`](runbook-power-loss-remote-site.md) |
| Alert flood | Corroborate before mute—[`Runbook — sensor false positive and alert triage`](runbook-sensor-false-positive-alert-triage.md) |
| Cyber | Remote access = exposure—inventory mindset (CISA-style); see source-notes under [`Planning framework`](east-tennessee-two-site-farm-business-plan-framework.md) links |

## Financing caution (automation)

- Cap **subscription + spare parts** OPEX annually; **reconcile** to **hours saved** and **incidents avoided**.
- Do not **finance** gadgets on consumer credit—tie to **phase gate** ([`Validation backlog`](validation-backlog-before-major-spend-two-site-smart-farm.md)).

## Known facts

| ID | Statement |
|----|-----------|
| K1 | The plan designates the **5-acre parcel** as the long-run **operations / telemetry control center**, not primary production. |
| K2 | The vault already contains **reference architecture** and **runbooks** for degraded modes. |

## Assumptions

| ID | Statement |
|----|-----------|
| A1 | Someone in the family can **maintain** one Linux/Docker-class stack **or** budget **paid** support. |
| A2 | Home internet is **good enough** for VPN + monitoring, with a **documented** fallback (LTE/Starlink-class) if required. |

## Open questions

| ID | Question |
|----|----------|
| Q1 | **farmOS vs lighter stack**? [`Comparison`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md) |
| Q2 | **LoRaWAN vs Meshtastic** for fixed telemetry? [`Comparison`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md) |
| Q3 | **Who is on-call** for alerts after normal hours? |
| Q4 | **Maximum** acceptable **alert hours per week** before you **de-scope** sensors? |

## Iterative updates

- Fill **Instrumentation priority matrix** [`instrumentation-priority-matrix-two-site-smart-farm.md`](instrumentation-priority-matrix-two-site-smart-farm.md) after pilot **ROI** numbers exist.
- Add **topic naming convention** table when MQTT topics are frozen.
- Date any **stack version** pin and **review quarterly**.

## Related pages

- [`East Tennessee two-site farm business plan — labor model and weekly operating rhythm`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md)
- [`East Tennessee two-site farm business plan — capital plan and phased infrastructure roadmap`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md)
- [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md)
