---
title: Structural audit — page ownership, entity gaps, and hub routing
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-17
review_status: unreviewed
tags:
  - meta
  - information-architecture
  - ownership
confidence: medium
---

# Structural audit — page ownership, entity gaps, and hub routing

**Purpose**: Keep the wiki from becoming an **analysis swamp** by naming **who owns durable meaning** (canonical pages), which **analyses** support them, where **entities** should anchor repeated real-world subjects, and how **hubs** route readers. Complements [`Structural audit — repository shape and canonical routing`](structural-audit-repository-and-canonical-routing.md) (merge policy, index structure) and implements **`AGENTS.md`** governance (canonicalization, entity-first, hubs).

**Epistemic rule**: This audit **does not** invent site facts. It **routes** and **prioritizes**; placeholders stay on deployment pages until evidence lands in `raw/` + source-notes.

---

## 1. Canonical ownership by cluster

| Cluster | **Canonical owner(s)** (durable scope) | **Supporting / extending** (do not duplicate TOC) | **Ownership notes** |
|---------|----------------------------------------|-----------------------------------------------------|------------------------|
| **Business plan / strategy (ET two-site)** | [`business-plan/east-tennessee-two-site-farm-business-plan`](../business-plan/east-tennessee-two-site-farm-business-plan.md), [`east-tennessee-two-site-farm-business-plan-framework`](east-tennessee-two-site-farm-business-plan-framework.md) | Chapters in `analyses/east-tennessee-two-site-farm-business-plan-*.md`; critique/remediation/source-campaign | **Package hub** = navigation; **framework** = rubric + full tree. New “strategy essays” should extend framework or a single chapter, not parallel packages. |
| **Two-site operating model** | [`two-site-operations-model-5ac-homebase-120ac-production`](two-site-operations-model-5ac-homebase-120ac-production.md) (ET scenario) | [`dual-site-operations-model-non-agritourism`](dual-site-operations-model-non-agritourism.md) | **Generic** vs **ET-named** sites—**no merge**; routing headers on both. Weekly/family matrices **extend** ops model. |
| **Telemetry / architecture / SoR** | [`reference-architecture-5ac-homebase-120ac-smart-farm`](reference-architecture-5ac-homebase-120ac-smart-farm.md) (package hub), [`telemetry-system-of-record-boundaries-and-authority`](telemetry-system-of-record-boundaries-and-authority.md), [`field-telemetry-reference-architecture-homestead-120ac`](field-telemetry-reference-architecture-homestead-120ac.md) | [`automation-principles-two-site-smart-farm`](automation-principles-two-site-smart-farm.md), [`remote-access-operational-security-model-two-site-smart-farm`](remote-access-operational-security-model-two-site-smart-farm.md), smart-tech **business-plan** chapter | **Reference arch** = boundaries + package map; **field telemetry** = MQTT/stack detail; **SoR** = authority matrix—avoid a fourth “data governance” analysis until one of these is full. |
| **Spatial / identity** | [`farm-spatial-model-and-asset-registry-standard`](farm-spatial-model-and-asset-registry-standard.md) | Instrumentation matrix (IDs), farmOS model source-notes | **Parcels/paddocks/devices** minimum fields live here; entity [`Farm parcels and land units`](../entities/farm-parcels-and-land-units.md) summarizes for cross-linking. |
| **Validation / pilot planning** | [`east-tennessee-two-site-farm-business-plan-validation-backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md), [`validation-backlog-before-major-spend-two-site-smart-farm`](validation-backlog-before-major-spend-two-site-smart-farm.md) | [`validation-and-pilot-plan-first-24-months-east-tennessee-two-site`](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md), [`pilot-and-recon-checklists-first-24-months-two-site-smart-farm`](pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md) | **First 24 months** = time-boxed matrix; **major-spend** = $ gates—if a new “validation” analysis appears, it must **link** these two or justify a new scope in `wiki/log.md`. |
| **Labor / coverage / risk** | [`east-tennessee-two-site-farm-business-plan-labor-and-family-model`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md), [`east-tennessee-two-site-farm-business-plan-risk-register`](east-tennessee-two-site-farm-business-plan-risk-register.md) | [`weekly-coverage-matrix-two-site-farm-operations`](weekly-coverage-matrix-two-site-farm-operations.md), [`family-labor-model-and-coverage-matrix-two-site-smart-farm`](family-labor-model-and-coverage-matrix-two-site-smart-farm.md), [`business-risk-register-two-site-smart-farm`](business-risk-register-two-site-smart-farm.md) | Matrices are **artifacts**, not alternate labor theories. |
| **Capital / revenue / economics** | [`east-tennessee-two-site-farm-business-plan-capital-and-financing`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md), [`east-tennessee-two-site-farm-business-plan-revenue-and-phased-income`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md) | [`capex-opex-enterprise-sequencing-two-site-constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md), [`enterprise-unit-economics-worksheet-methodology-two-site-smart-farm`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md), [`farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm`](farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md), milestone/ROI models | **Worksheets** hold methodology shells—**no competing** “capital theory” pages without `supersedes`. |
| **Water / roads / power / infra** | Topic hubs ([`Ponds, water features…`](../topics/ponds-water-features-and-homestead-hydrology.md), [`Off-grid solar…`](../topics/off-grid-solar-power-and-storage.md), [`Rural road and driveway erosion…`](../topics/rural-road-and-driveway-erosion-sources.md)); two-site **reference** + **runbooks** for failures | Standalone syntheses (e.g. dirt road erosion analyses) | **Synthesis analyses** should end with **hub links** and **entity** anchors ([`Farm water infrastructure system`](../entities/farm-water-infrastructure-system.md), [`Farm on-site power system`](../entities/farm-on-site-power-system.md)) rather than fork new “infrastructure overview” pages. |
| **Agritourism vs non-agritourism** | [`agritourism-dual-site-business-plan-five-and-120-acres`](agritourism-dual-site-business-plan-five-and-120-acres.md) (lodging-led alternate scenario) | ET **business plan** package (production-led) | **Different intent**—cross-link as **alternate scenario**, not merge. |

---

## 2. Overlapping or sideways analyses (risk)

| Pattern | Examples | Mitigation |
|---------|----------|------------|
| **Meta-audits** | Strategic audit, IA target design, implementation backlog, repository structural audit, [`Structural debt audit — wiki IA and operational maturity`](structural-debt-audit-wiki-ia-and-operational-maturity.md), **this page** | Keep **one question per audit title**; cross-link; do not copy/paste backlog tables between them—**pointer** instead. |
| **Query syntheses** | `analyses/*query*` agritourism, stocking prompts, profitable crops matrix | Acceptable as **time-stamped answers**; if content becomes permanent doctrine, **fold** into topic hub or canonical analysis and add routing. |
| **Duplicate “overview”** | Domain content overview vs strategic audit vs business plan executive summary | **Domain overview** = strands; **executive summary** = business plan only; **strategic audit** = gap list—readers should not see three competing “north stars” without labels. |

---

## 3. Weak hubs (before this pass)

| Hub | Issue | Fix direction |
|-----|--------|----------------|
| **`index.md`** | Long flat analyses list elsewhere | Business plan **section** already elevates ET package; **entities** need expansion (below). |
| **`two-site-smart-farm-operations`** | Tables strong but no **ownership** row | **Addressed** (2026-04): **Canonical ownership** table + **Regulatory & site evidence** row → [`Authoritative execution evidence cluster`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md), [`Execution readiness gap audit`](../analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md). |
| **`domain-content-overview`** | Strand map strong; **ownership** implicit | Add **canonical routing** pointer to this audit **and** [`Execution readiness gap audit`](../analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md). |

---

## 4. Entity layer gaps (addressed incrementally)

**Previously**: Mostly **products** ([`farmOS`](../entities/farmos.md), [`Home Assistant`](../entities/home-assistant.md)) + demo org.

**Added (structural placeholders, no fake deeds)**:

- [`Five-acre home base (SITE_HOME) — ET two-site`](../entities/five-acre-home-base-site-home-et-two-site.md)
- [`120-acre production farm (SITE_FARM) — ET two-site`](../entities/120-acre-production-farm-site-farm-et-two-site.md)
- [`Farm parcels and land units`](../entities/farm-parcels-and-land-units.md)
- [`Farm water infrastructure system`](../entities/farm-water-infrastructure-system.md)
- [`Farm on-site power system`](../entities/farm-on-site-power-system.md)
- [`Field telemetry network — two-site`](../entities/field-telemetry-network-two-site.md)

**Still thin (future)**: Legal **operating entities** (LLC, etc.) until named; **specific** equipment instances; **named** market channels—use placeholders on economics pages until real.

---

## 5. Prompt residue / scaffolding risk

| Signal | Response |
|--------|----------|
| Analysis with **only** questions and no links to canonical pages | Add **Routing** paragraph or merge into hub. |
| **status: draft** everywhere | Acceptable for deployment placeholders; **business plan framework** should graduate to `active` when family review completes (human gate). |
| **“Hostile review”** standing alone | Keep as **critique artifact**; **remediation backlog** owns follow-up—already linked. |

---

## 6. Recommended habits (agents & humans)

1. Before **`analyses/new-*.md`**: search [`domain-content-overview`](domain-content-overview.md) + relevant hub + this section.  
2. Prefer **`entities/`** for sites and infrastructure **systems** that appear in ≥3 pages.  
3. Update **hub tables** the same commit as a new sibling page.  
4. Log **scope decisions** in [`wiki/log.md`](../log.md) when creating a page that could be read as canonical.

---

## Related

- [`AGENTS.md`](../../AGENTS.md) — Page ownership section; canonicalization; entity-first; `page_subtype` / `operational_maturity`.  
- [`Structural debt audit — wiki IA and operational maturity`](structural-debt-audit-wiki-ia-and-operational-maturity.md) — Sprawl metrics, guide taxonomy, flat-index mitigations.  
- [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md) — Themed router for canonical clusters.  
- [`Domain content overview`](domain-content-overview.md) — Strand maturity.  
- [`Knowledge synthesis`](../topics/knowledge-synthesis.md) — Entry points.
