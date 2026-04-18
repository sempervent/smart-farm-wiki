---
title: Capital phasing table — years 0 to 10 (two-site smart farm)
page_type: analysis
status: draft
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - finance
  - capex
  - two-site
  - template
confidence: medium
---

# Capital phasing table — years 0 to 10 (two-site smart farm)

## Purpose

Lay out **infrastructure and equipment spend** on a **0–10 year** horizon for the **two-site** **grazing-led** strategy family, with **placeholders** for **amounts** and **financing**. Complements [`East Tennessee two-site farm business plan — capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md) and [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md).

## Key decisions supported

| Decision | Table use |
|----------|-----------|
| **When** to spend on **fence vs telemetry** | Row timing + **gate** column |
| **Home vs farm** CAPEX | **Site** column |
| **Debt vs cash** | **Source** column—**no** silent credit card leverage |
| **Stop** if gate fails | Link **Gate ID** to [`Validation backlog — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md) |

## Phasing map (business plan Phases 0–4)

| Yr (approx) | Business plan phase | Capital theme |
|-------------|---------------------|---------------|
| **0–1** | 0–1 | **No-regret**, **intel**, **pilot** |
| **2–4** | 2 | **MVP** **production** **infra** + **herd** **or** **contracts** |
| **5–7** | 3 | **Scale** **or** **second** stream |
| **8–10** | 4 | **Salary** **architecture**, **hardening** |

## Capital table — years 0–10 (fill)

**Legend**: **Site** = `HOME` | `FARM` | `BOTH` · **Src** = `CASH` | `FIN` | `GRANT` | `LEASE` (equipment) · **Gate** = prerequisite ID

| Yr | Quarter (opt) | Category | Item | Site | Est $ | Src | Gate / trigger | Irreversible? |
|----|-----------------|----------|------|------|-------|-----|----------------|---------------|
| 0 | | Legal / maps | Surveys, boundary, access clarity | BOTH | `$_` | CASH | G0 | Partially |
| 0 | | Comms | Homelab baseline / backup | HOME | | | | |
| 1 | | Land intel | Soil, water tests, fence audit | FARM | | | V-land | |
| 1 | | Telemetry pilot | **One** I/O path (see [`Instrumentation priority matrix`](instrumentation-priority-matrix-two-site-smart-farm.md)) | FARM | | CASH | I-manual | |
| 2 | | Water | Develop / extend distribution | FARM | | FIN? | G1 | **Yes** |
| 2 | | Fence | Perimeter / interior MVP | FARM | | FIN? | G1 | **Yes** |
| 2 | | Livestock | Herd or contract buy-in | FARM | | | margin | |
| 3–4 | | Handling | Corral / load-out MVP | FARM | | | | |
| 3–4 | | Transport | Truck/trailer class upgrade | BOTH | | | | |
| 5–7 | | Scale | Add paddocks, water, herd | FARM | | | G2 | |
| 5–7 | | Telemetry | Expand sensors **within** OPEX cap | FARM | | | | |
| 8–10 | | Optimization | Cold chain, direct marketing assets | BOTH | | | G3 | |

Add rows; **do not** pre-fill **$_** without **quotes**.

## Financing caution (checklist)

- [ ] **Debt service** ≤ **`MAX_DS_PCT`** % of trailing **gross** farm revenue
- [ ] **Operating line** not used for **depreciable** **without** **amortization** plan
- [ ] **Personal guarantee** **documented** **worst-case**
- [ ] **Equipment**: **custom hire** quote **before** **purchase** **for** **first** **season**

## Known / assumed / open

| Class | Content |
|-------|---------|
| **Known** | **Phased** investment + **selective** financing **stated** in plan |
| **Assumed** | **Off-farm** income **subsidizes** **early** years |
| **Open** | **FSA** / **lender** **terms**; **exact** **EQIP** **eligibility** |

## Links

- [`East Tennessee two-site farm business plan — revenue and milestones`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md)
- [`Business risk register`](business-risk-register-two-site-smart-farm.md)
