---
title: Instrumentation priority matrix — two-site smart farm
page_type: analysis
status: draft
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - telemetry
  - automation
  - two-site
  - template
confidence: medium
---

# Instrumentation priority matrix — two-site smart farm

## Purpose

Rank **where automation earns its keep first** for a **35-minute** separated operation: **trip reduction**, **risk reduction**, and **labor relief**—with **explicit** cost of **false positives** and **maintenance**.

Aligns with [`East Tennessee two-site farm business plan — smart-tech strategy`](east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) and [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md).

## Key decisions supported

| Decision | Use matrix for |
|----------|----------------|
| **Phase 1 pilot sensor** | Only **rows** scoring **high** on **trip ROI** + **feasible** install |
| **OPEX cap** | Sum **annual** **subscription + spares** for enabled rows |
| **What NOT to buy** | Low **trip ROI** + high **alert fatigue** |
| **Manual proof first** | Rows with **“manual first”** gate **unchecked** → **no** remote control |

## Scoring columns (1–5 each; total **/25** optional)

| Criterion | Meaning |
|-----------|---------|
| **Trip ROI** | Reduces **unnecessary** `SITE_FARM` visits |
| **Risk** | Prevents **catastrophic** loss (stock, crop, equipment) |
| **Labor** | Reduces **hours** (not just **miles**) |
| **Capital** | Reasonable **CAPEX** for phase (**5** = cheap pilot) |
| **Ops burden** | Low **false positives**, **spares** available, **simple** triage |

## Priority matrix (fill)

| ID | Instrument / signal | Trip ROI | Risk | Labor | Capital | Ops burden | Manual proof first? | Phase target | Notes |
|----|---------------------|----------|------|-------|---------|------------|----------------------|--------------|-------|
| I1 | **Tank / trough level** | | | | | | **Y**—stick log **30d** | 0–1 | |
| I2 | **Pump run / fault / pressure** | | | | | | **Y** | 1 | |
| I3 | **Gate position (if motorized)** | | | | | | **Y**—safe default | 2 | |
| I4 | **Power / generator / UPS** at critical loads | | | | | | **partial** | 0–1 | home + farm |
| I5 | **Soil moisture (point)** | | | | | | **Y**—calibrate to **crop** | 3+ | defer if grazing-only |
| I6 | **Weather station** | | | | | | optional | 1 | |
| I7 | **Cameras** | | | | | | **policy** first | 2+ | privacy, **triage** load |
| I8 | **GPS collars / tags** | | | | | | market **proof** | 3+ | **OPEX** heavy |
| I9 | **Irrigation valve control** | | | | | | **walk** **lines** first | 3+ | |

## Automate early (typical winners)

- **Water** visibility + **pump** fault: **highest** trip ROI for **remote** pasture.
- **Power** awareness at **remote** **pump** or **gateway**: explains **silent** failures.

## Automate late or never (until gates pass)

| Item | Why wait |
|------|----------|
| **Camera everywhere** | Bandwidth, storage, **alert** noise |
| **Remote** **chute** / **feed** **actuation** | **Safety** + **liability** |
| **Full** **irrigation** automation | **Crop** commitment + **skill** |

## Manual-before-automation checklist

- [ ] **Asset IDs** in [`Farm spatial model / registry`](farm-spatial-model-and-asset-registry-standard.md)
- [ ] **One** season **paper** or **simple** **digital** **log** for **the** **signal** you think you need
- [ ] **Runbook** row: [`Sensor false positive / alert triage`](runbook-sensor-false-positive-alert-triage.md)

## Known / assumed / open

| Class | Content |
|-------|---------|
| **Known** | Business plan **prioritizes** **telemetry** **with** **degraded** **modes** |
| **Assumed** | **LTE** or **fallback** at **`SITE_HOME`** acceptable for **non-life** alerts |
| **Open** | **Radio** **technology** choice ([`LoRaWAN vs Meshtastic`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md)); **exact** **tank** count |

## Links

- [`Capital phasing table`](capital-phasing-table-years-0-10-two-site-smart-farm.md)
- [`Validation backlog — before major spend`](validation-backlog-before-major-spend-two-site-smart-farm.md)
