---
title: Two-site smart farm operations
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-21
tags:
  - two-site
  - operations
  - business-plan
  - east-tennessee
review_status: unreviewed
---

# Two-site smart farm operations

**Navigation hub** for the **~5-acre home base** + **~120-acre production** + **~35-minute** separation scenario (East Tennessee business plan). **Does not** duplicate long analyses—use the links below.

**Business plan (first-class package)**: [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md)

**Meta plan**: [`Smart Farm Wiki — repository implementation plan (business plan integration)`](../analyses/smart-farm-wiki-repository-implementation-plan.md)

**Structure / governance** (overlaps, hubs, entities): [`Structural audit — repository shape and canonical routing`](../analyses/structural-audit-repository-and-canonical-routing.md), [`Structural audit — page ownership, entity gaps, and hub routing`](../analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md), and [`AGENTS.md`](../../AGENTS.md).

## Canonical ownership (durable scope)

| Cluster | Canonical entry | Notes |
|---------|-----------------|--------|
| **Business plan (ET)** | [`Package hub`](../business-plan/east-tennessee-two-site-farm-business-plan.md) + [`Planning framework`](../analyses/east-tennessee-two-site-farm-business-plan-framework.md) | Chapters are supporting; **not** parallel “strategy blogs.” |
| **Two-site ops (named sites)** | [`Two-site operating model — 5 ac / 120 ac`](../analyses/two-site-operations-model-5ac-homebase-120ac-production.md) + [`Trip policy`](../analyses/trip-batching-and-site-visit-policy-two-site-smart-farm.md) + [`Disqualifiers`](../analyses/two-site-structure-disqualifiers-east-tennessee.md) | **35-min distance tax** is structural. Generic pattern: [`Dual-site — non-agritourism`](../analyses/dual-site-operations-model-non-agritourism.md). **Entities**: [`SITE_HOME`](../entities/five-acre-home-base-site-home-et-two-site.md), [`SITE_FARM`](../entities/120-acre-production-farm-site-farm-et-two-site.md). |
| **Telemetry + SoR** | [`Reference architecture`](../analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`SoR boundaries`](../analyses/telemetry-system-of-record-boundaries-and-authority.md), [`Field telemetry ref arch`](../analyses/field-telemetry-reference-architecture-homestead-120ac.md) | **Entity**: [`Field telemetry network — two-site`](../entities/field-telemetry-network-two-site.md). |
| **Land IDs** | [`Farm spatial model / asset registry`](../analyses/farm-spatial-model-and-asset-registry-standard.md) | **Entity**: [`Farm parcels and land units`](../entities/farm-parcels-and-land-units.md). |
| **Water / power infra** | Topic hubs + runbooks (see tables below) | **Entities**: [`Farm water infrastructure system`](../entities/farm-water-infrastructure-system.md), [`Farm on-site power system`](../entities/farm-on-site-power-system.md). |

## Business plan (decision-grade)

| Page | Role |
|------|------|
| [`Planning framework`](../analyses/east-tennessee-two-site-farm-business-plan-framework.md) | Hub, rubric, package index |
| [`Executive summary`](../analyses/east-tennessee-two-site-farm-business-plan-executive-summary.md) | Distilled map |
| [`Enterprise options analysis`](../analyses/east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md) | Scenario matrix |
| [`Recommended enterprise strategy — phased East Tennessee path`](../analyses/east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md) | Grazing-led phased mixed |
| [`Hostile internal review`](../analyses/east-tennessee-two-site-farm-business-plan-hostile-internal-review.md) | Skeptical critique |
| [`Business plan remediation backlog`](../analyses/east-tennessee-two-site-farm-business-plan-remediation-backlog.md) | Fixes, **do not finance**, validation checklist |
| [`Business plan source-ingest campaign`](../analyses/business-plan-source-ingest-campaign-east-tennessee-two-site.md) | Extension/NRCS/market priorities, backlog titles |

## Operations & logistics

| Page | Role |
|------|------|
| [`Dual-site operations model — non-agritourism`](../analyses/dual-site-operations-model-non-agritourism.md) | Generic two-site production logistics |
| [`Two-site operating model — 5-acre home base and 120-acre farm`](../analyses/two-site-operations-model-5ac-homebase-120ac-production.md) | **Distance-tax** (`DT-*`), **`R_SPLIT`**; fillable SITE_HOME / SITE_FARM |
| [`Trip batching and site visit policy`](../analyses/trip-batching-and-site-visit-policy-two-site-smart-farm.md) | **Justified** trips, **batching**, **remote** observability, **failure** patterns |
| [`Two-site structure disqualifiers`](../analyses/two-site-structure-disqualifiers-east-tennessee.md) | **Poor-fit** enterprises + **operating** anti-patterns |
| [`Labor model and weekly operating rhythm`](../analyses/east-tennessee-two-site-farm-business-plan-labor-and-family-model.md) | Family capacity + DOW template |
| [`Weekly coverage matrix`](../analyses/weekly-coverage-matrix-two-site-farm-operations.md) | Template grid |
| [`Family labor and coverage matrix`](../analyses/family-labor-model-and-coverage-matrix-two-site-smart-farm.md) | Family + tiers |

## Telemetry & automation

| Page | Role |
|------|------|
| [`Reference architecture — 5 ac + 120 ac`](../analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) | **Package hub** |
| [`Telemetry system of record — boundaries and authority`](../analyses/telemetry-system-of-record-boundaries-and-authority.md) | Authority matrix |
| [`Field telemetry reference architecture`](../analyses/field-telemetry-reference-architecture-homestead-120ac.md) | MQTT/broker/backhaul stack |
| [`Farm spatial model / asset registry`](../analyses/farm-spatial-model-and-asset-registry-standard.md) | IDs + map |
| [`Instrumentation priority matrix`](../analyses/instrumentation-priority-matrix-two-site-smart-farm.md) | First acres/risks/systems + ROI ranking |
| [`Automation principles`](../analyses/automation-principles-two-site-smart-farm.md) | Early / late / never |
| [`Remote access and operational security model`](../analyses/remote-access-operational-security-model-two-site-smart-farm.md) | Admin + zones |
| [`Smart technology and telemetry strategy — control center on 5 acres`](../analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) | **AA/AF/PA/SO** controls; execution-safe strategy |
| [`Automation stop rules`](../analyses/automation-stop-rules-two-site-smart-farm.md) | **NS/MV** no-scale gates; Phase 1 **observe-only** table |

## Resilience

| Page | Role |
|------|------|
| [`Automation degraded modes SOP`](../analyses/automation-degraded-modes-manual-fallback-sop.md) | Parent degraded-mode doc |
| [`Manual fallback — critical operations`](../analyses/manual-fallback-degraded-modes-critical-operations.md) | Scenario model + critical-ops matrix |
| Runbooks: [`broker`](../analyses/runbook-broker-or-backhaul-down.md), [`power`](../analyses/runbook-power-loss-remote-site.md), [`triage`](../analyses/runbook-sensor-false-positive-alert-triage.md), [`water/gates`](../analyses/runbook-manual-fallback-irrigation-gates-pumps.md) | |

## Finance & validation

| Page | Role |
|------|------|
| [`Capital plan and infrastructure sequencing`](../analyses/east-tennessee-two-site-farm-business-plan-capital-and-financing.md) | Sequencing + financing rules |
| [`Revenue model and milestones`](../analyses/east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md) | Streams + horizon |
| [`Risk register and mitigation strategy`](../analyses/east-tennessee-two-site-farm-business-plan-risk-register.md) | Register |
| [`Validation backlog and decision gates`](../analyses/east-tennessee-two-site-farm-business-plan-validation-backlog.md) | Tasks V* + gates G* |
| [`Execution dossier — Phase 0–1 (hub)`](../analyses/execution-dossier-hub-phase-0-1-east-tennessee.md) | **Start here**: memo, 90d/12m/24m, master checklist |
| [`Validation and pilot plan — first 24 months`](../analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) | Matrix + T0 calendar windows + gates |
| [`Pilot and recon checklists`](../analyses/pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md) | Fillable rows |
| [`Enterprise unit economics — worksheet methodology`](../analyses/enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md) | Units, scenarios, split-site costs |
| [`CAPEX/OPEX — two-site constraint`](../analyses/capex-opex-enterprise-sequencing-two-site-constraint.md) | Phasing by site + gates |
| [`Farm accounting baseline — COA + enterprise P&L`](../analyses/farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md) | Books structure; not tax advice |
| [`Capital phasing 0–10`](../analyses/capital-phasing-table-years-0-10-two-site-smart-farm.md) | Fillable year table |
| [`Revenue milestones`](../analyses/revenue-milestone-model-supplemental-to-salary-replacement.md) | Supplemental → salary ladder |
| [`Execution gates — financial thresholds`](../analyses/execution-gates-financial-thresholds.md) | Phase **0→4** pass/fail; ties **M*** to **Fin-G** |
| [`Instrumentation ROI model`](../analyses/instrumentation-roi-model-two-site-smart-farm.md) | Pilot vs fleet; triage + OPEX |
| [`Validation before major spend`](../analyses/validation-backlog-before-major-spend-two-site-smart-farm.md) | Major-$ gates |
| [`Business risk register`](../analyses/business-risk-register-two-site-smart-farm.md) | Review matrix |

## Comparisons (tradeoffs)

| Page |
|------|
| [`LoRaWAN vs Meshtastic`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md) |
| [`farmOS vs lightweight`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md) |
| [`Own equipment vs custom hire`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md) |
| [`Fixed vs mobile gateway`](../comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md) |

## Related topic sources

- [`Tennessee hobby farm and small-farm business sources`](tennessee-hobby-farm-and-small-farm-business-sources.md)
- [`Farm data, farmOS, and agriculture lab builds`](farm-data-farmos-and-ag-lab-builds.md)
- [`LoRa, MQTT, and gateway bridges`](lora-mqtt-and-gateway-bridges.md)
