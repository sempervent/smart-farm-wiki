---
title: Business risk register — two-site smart farm
page_type: analysis
status: draft
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - risk
  - two-site
  - business-plan
  - template
confidence: medium
aliases:
  - Two-site smart farm business risk register
---

# Business risk register — two-site smart farm

## Purpose

Operational **risk register** for the **two-site** **family** **grazing-led** **plan**: **market**, **weather**, **labor**, **capital**, **legal**, **telemetry**—with **mitigations** **tied** **to** **phases**. **Supplements** [`East Tennessee two-site farm business plan — risk register and mitigation`](east-tennessee-two-site-farm-business-plan-risk-register.md) with **matrix** **suitable** **for** **monthly** **review**.

## Key decisions supported

| Decision | Register use |
|----------|----------------|
| **Insurance** limits / umbrella | **R-liability** rows |
| **Max debt** | **R-financial** |
| **Automation scope** | **R-tech** **false** **confidence** |
| **Herd size cap** | **R-labor** + **R-market** |

## Scoring (optional)

**L** = likelihood 1–5 · **I** = impact 1–5 · **Score** = L×I

## Register (fill)

| ID | Risk | Cat | L | I | Mitigation | Owner | Phase | Status |
|----|------|-----|---|---|------------|-------|-------|--------|
| B1 | Cattle **price** **drop** | Market | | | **Timing**; **smaller** **herd**; **lease** **buffer** | | 2–4 | open |
| B2 | **Drought** / **forage** **failure** | Weather | | | **Destock** **policy**; **water** **redundancy** | | 1–3 | open |
| B3 | **Key** **person** **injury** | Labor | | | **Cross-training**; **reduce** **complexity** | | 0–4 | open |
| B4 | **Debt** **service** **strain** | Financial | | | **Stop** **rules**; **match** **term** **to** **margin** | | 1–4 | open |
| B5 | **Equipment** **down** **at** **peak** | Ops | | | **Spares**; **custom** **hire** **#** | | 2–3 | open |
| B6 | **Fence** / **escape** | Ops | | | **Inspection** **cadence** | | 2–4 | open |
| B7 | **Broker** / **comms** **down** | Tech | | | **Runbooks**; **safe** **defaults** | | 1–4 | open |
| B8 | **Alert** **fatigue** | Tech | | | **Triage** **SOP**; **annual** **de-scope** | | 2–3 | open |
| B9 | **Cyber** / **remote** **access** **misuse** | Tech | | | **2FA**; **segmentation** | | 2–4 | open |
| B10 | **Liability** **visitor** / **animal** | Legal | | | **Insurance**; **signage**; **separate** **events** **if** **any** | | 2–4 | open |
| B11 | **Zoning** / **ag** **structure** **denial** | Legal | | | **Early** **county** **conversation** | | 0–1 | open |
| B12 | **Two-site** **delay** **cost** | Ops | | | **Batch** **rules**; **telemetry** **priority** **matrix** | | 0–4 | open |

## Two-site–specific notes

- **B12**: **Every** **avoidable** **trip** **tax** **margin**—track **hours** **in** **truck** **as** **cost**.
- **B7–B9**: **Homelab** **as** **prod** **=** **prod** **discipline** ([`Smart-tech strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md)).

## Review cadence (suggested)

| Frequency | Action |
|-----------|--------|
| **Monthly** | **Update** **L/I** **if** **events**; **close** **mitigated** |
| **Annual** | **Insurance** **limits**; **de-scope** **tech** |

## Known / assumed / open

| Class | Content |
|-------|---------|
| **Known** | **Two-site** **+** **telemetry** **in** **scope** |
| **Assumed** | **Farm** **insurance** **carried** |
| **Open** | **Entity** **structure**; **umbrella** **limit** |

## Links

- [`Manual fallback and degraded modes`](manual-fallback-degraded-modes-critical-operations.md)
- [`Family labor and coverage matrix`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md)
- [`Validation backlog — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md)
