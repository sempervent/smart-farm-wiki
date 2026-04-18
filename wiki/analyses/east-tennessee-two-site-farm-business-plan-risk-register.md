---
title: Risk register and mitigation strategy
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-22
review_status: unreviewed
tags:
  - business-plan
  - risk
  - two-site
confidence: medium
aliases:
  - East Tennessee two-site farm business plan — risk register and mitigation strategy
---

# Risk register and mitigation strategy

## Purpose

Maintain a **working risk register** for the **two-site**, **telemetry-heavy**, **family-labor** farm business plan: **market**, **weather**, **labor**, **capital**, **operations**, **technology**, **legal/liability**. **Likelihood** and **impact** are **local judgments**—revise **quarterly** or after **incidents**.

**Operational matrix**: [`Business risk register — two-site smart farm`](business-risk-register-two-site-smart-farm.md) (monthly review option).  
**Hub**: [`East Tennessee two-site farm business plan — planning framework`](east-tennessee-two-site-farm-business-plan-framework.md).

## Decisions supported by this page

| Decision | This page provides |
|----------|-------------------|
| **Insurance** limits and umbrella | Liability rows |
| **Maximum debt** and **herd size** | Financial + operational rows |
| **Automation scope** | Tech false-confidence + alert fatigue |
| **When** to **downsize** enterprise | Mitigation tied to **measurable** triggers |

## Method

- Score **L** (likelihood) and **I** (impact) **1–5**; priority = **L × I** (optional).
- **Two-site** and **telemetry** risks are **first-class**, not footnotes.

## Register (living)

| ID | Risk | Category | L | I | Mitigation | Phase |
|----|------|----------|---|---|------------|-------|
| R1 | Cattle price crash | Market | 3 | 4 | Timing; smaller herd; lease buffer | 2–4 |
| R2 | Drought / forage gap | Weather | 3 | 4 | Destock policy; hay plan; water redundancy | 1–3 |
| R3 | Key person injury / absence | Labor | 2 | 4 | Cross-training; reduce complexity; insurance | 0–4 |
| R4 | Equipment failure at peak | Ops | 3 | 3 | Spares; custom hire number on fridge | 2–3 |
| R5 | Fence failure / escape | Ops | 2 | 4 | Inspection cadence; hot wire maintenance | 2–4 |
| R6 | Debt overhang | Financial | 2 | 5 | Hard stop rules; match term to margin | 1–4 |
| R7 | Broker / comms down | Tech | 3 | 2 | Runbooks; safe defaults at edge | 1–4 |
| R8 | False alert fatigue | Tech | 4 | 3 | Triage SOP; corroboration before mute | 2–3 |
| R9 | Cyber / remote access breach | Tech | 2 | 4 | Segmentation; 2FA; asset inventory mindset | 2–4 |
| R10 | Liability (visitor / animal / road) | Legal | 2 | 5 | Insurance; signage; separate agritourism if ever | 2–4 |
| R11 | Regulatory / zoning surprise | Legal | 2 | 3 | County conversation early | 0–1 |
| R12 | **Two-site delay cost** (slow response at 120) | Ops | 3 | 3 | Batch rules; water/gate telemetry priority | 0–4 |
| R13 | **Theft / vandalism** at remote parcel | Ops | 2 | 3 | Access control, neighbor awareness; **not** camera-only | 2–4 |
| R14 | **Terrain / road / sediment** (steep gravelly soils; lane erosion) | Ops | 3 | 4 | Earthwork + drainage **with** fence plan; **Campbell** evidence: [`Demory site intelligence`](demory-farm-site-intelligence.md) | 1–3 |
| R15 | **Map / AOI mismatch** (WSS session ≠ deed or ≠ ~120 ac operating area) | Ops | 2 | 3 | Redraw AOI; clip map units to **fields**; label `MAP_AUTHORITY` | 0–1 |

**What changed**: **R14**–**R15** added from **Campbell** WSS + **two-county** NASS context; **parcel** facts still **verify** locally.

## Mitigation themes

| Theme | Actions |
|-------|---------|
| Liquidity | Operating reserve months (**N**); lease income where ethical |
| Complexity | One major new system per year **after** Phase 2 |
| Telemetry | Alert budget (hours/week); annual **de-scope** review |
| Labor | Weekly rhythm + **documented** surge overrides |

## Known facts

| ID | Statement |
|----|-----------|
| K1 | Degraded-mode **runbooks** exist in the vault ([`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md)). |
| K2 | **Production risk** concentrates on the **120-acre** parcel; **control** functions concentrate **home** ([`Smart technology and telemetry strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)). |

## Assumptions

| ID | Statement |
|----|-----------|
| A1 | **Farm insurance** is carried at levels **lenders** and **comfort** require—**verify** with agent. |

## Open questions

| ID | Question |
|----|----------|
| Q1 | **Umbrella** limit and **exclusions**? |
| Q2 | **Entity structure** (LLC etc.) and liability isolation? |
| Q3 | **Right-to-farm** / neighbor conflict exposure? |

## Iterative updates

- Add **owner** name per row locally; **close** risks only when mitigation is **verified**.
- After **major** weather or market event, **re-score** R1–R2.

## Related pages

- [`East Tennessee two-site farm business plan — smart technology, telemetry, and automation`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)
- [`East Tennessee two-site farm business plan — validation backlog and decision gates`](east-tennessee-two-site-farm-business-plan-validation-backlog.md)
- [`East Tennessee two-site farm business plan — hostile internal review`](east-tennessee-two-site-farm-business-plan-hostile-internal-review.md)
