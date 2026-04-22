---
title: Execution readiness gap audit — East Tennessee operational knowledge base
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-28
review_status: unreviewed
tags:
  - meta
  - execution
  - east-tennessee
  - two-site
  - information-architecture
confidence: medium
aliases:
  - ET operational gap audit
---

# Execution readiness gap audit — East Tennessee operational knowledge base

**Purpose**: Move the vault from a **strong planning-and-synthesis** system toward a more **execution-ready operational** knowledge base by naming **what is still missing**, **where authority is unclear**, and **which canonical pages** should absorb improvements—**without** inventing parcel-specific facts or spawning overlapping strategy essays.

**Baseline**: Published site structure (`wiki/index.md`, package hub, structural audits). **Epistemic rule**: Site-specific numbers (soil class, septic setbacks, cash rent per acre, tax outcomes) belong in **your** worksheets and **citable** sources—not in synthesized pages unless **explicitly** tied to a **source-note** or **labeled assumption**.

**Companion pages**: [`Evidence grade and canonical authority`](../concepts/evidence-grade-and-canonical-authority.md) (signaling vocabulary), [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) (source index), [`Structural audit — page ownership, entity gaps, and hub routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md) (anti–analysis-swamp policy).

**Execution gate system (Phase 0–1)**: [`Execution gates — Phase 0–1 (East Tennessee two-site)`](execution-gates-phase-0-1-east-tennessee-two-site.md) — operational **pass/fail** by domain (EG IDs), **pilot** vs **production**; complements this gap audit (which names **what is missing**, not **when** spend may proceed).

---

## 1. Missing site-specific execution data

| Gap | Why it blocks execution | Fill strategy (no fake site facts) |
|-----|-------------------------|--------------------------------------|
| **Parcel soil capability** (map unit, limiting factors, hydric flags) | Gates fence/water/crop/grazing assumptions | Use **Web Soil Survey** + **SSURGO** interpretation; ground-truth with county soil survey or consultant. Source cluster: [`WSS + elevation captures`](../source-notes/web-soil-survey-and-elevation-captures-inbox-2026-04-18.md). |
| **Elevation / drainage / wetness** (DEM-derived flow paths, ponding risk) | Road/building/pasture layout; erosion | **3DEP** / lidar-backed products + field observation. Same capture note; tie to [`Farm water infrastructure system`](../entities/farm-water-infrastructure-system.md). |
| **Septic / SSDS / buildability** (permit class, setbacks, soil morph) | Homestead expansion, shop, guest infrastructure | **TDEC / county** rules—not blog generalizations. [`Tennessee onsite sewage / septic captures`](../source-notes/tn-onsite-sewage-septic-captures-inbox-2026-04-18.md). |
| **County-level land economics** (cash rent by practice) | Lease vs own vs custom hire; milestone realism | **USDA NASS** county tables (survey year explicit). [`NASS cash rents TN 2024`](../source-notes/nass-cash-rents-tn-2024-surveys-pdf.md), [`survey page capture`](../source-notes/usda-nass-cash-rents-survey-page-inbox-2026-04-18.md). |
| **TN tax posture** (ag exemption, sales tax on inputs, agritourism exposure) | Cash planning; entity choice discussions | **Primary**: DOR publications. [`TN Revenue ag exemption PDF`](../source-notes/tn-revenue-agricultural-exemption-jan2023-pdf.md), [`Agricultural exemption capture`](../source-notes/agricultural-exemption-page-inbox-2026-04-18.md), [`Public Chapter 498`](../source-notes/tn-public-chapter-498-agritourism-act-pdf.md) (act text—not individualized tax advice). |
| **Grazing / forage calendar + enterprise budgets** | Stocking, hay, surge labor | Extension **PB1663** calendar, **UT budgets**, [`Livestock Companion`](../source-notes/livestock-companion-vol-17-2025-04-pdf.md), [`NRCS GLCI excerpt`](../source-notes/nrcs-tennessee-grazing-lands-glci-excerpt.md). |
| **FSA / credit / beginning-farmer programs** (eligibility, timelines) | Capital plan gates | [`FSA program captures`](../source-notes/fsa-program-pages-capture-inbox-2026-04-18.md), [`Beginning farmer resources`](../source-notes/beginning-farmer-resources-list.md)—**apply** through FSA/USDA, not wiki. |
| **farmOS operational bindings** (asset ↔ geometry ↔ log ↔ location) | SoR + spatial registry coherence | Official model docs + inbox captures: [`Assets`](../source-notes/farmos-model-assets-documentation.md), [`Logs`](../source-notes/farmos-model-logs-documentation.md), [`farmOS documentation captures`](../source-notes/farmos-documentation-captures-inbox-2026-04-18.md). |
| **Remote access / OT exposure** (homelab ↔ field) | Security posture for telemetry | **CISA**: [`Guide to securing remote access (PDF)`](../source-notes/cisa-guide-securing-remote-access-software-508-pdf.md), [`Joint guide OT cybersecurity asset inventory (PDF)`](../source-notes/cisa-joint-guide-ot-cybersecurity-asset-inventory-508-pdf.md)—tie to [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md). |

---

## 2. Weak or under-modeled entities / layers

| Layer | Issue | Recommended canonical update |
|-------|--------|-------------------------------|
| **Parcels / land units** | IDs described; **soil + permit** links underdeveloped | [`Farm parcels and land units`](../entities/farm-parcels-and-land-units.md) — extended “authority chain” (WSS → map units → field verify). |
| **farmOS product** | Strong on Assets/Logs; **Location** + movement pattern from captures under-linked | [`farmOS`](../entities/farmos.md) — pointer to inbox doc captures. |
| **Spatial registry** | `MAP_AUTHORITY_LABEL` still often TBD | [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) — explicit **external** references subsection. |
| **Glossary / timeline** | Thin vs. volume of analyses | Add **evidence grade** glossary entry; **phase timeline** gains one **evidence milestone** row (see [`phase timeline`](../timelines/east-tennessee-two-site-farm-business-plan-phase-timeline.md)). |

---

## 3. Mixed-authority source clusters (reader hazard)

| Cluster | Mixed content | Mitigation |
|---------|----------------|------------|
| **Tennessee business / hobby** | Listicles + **DOR** + **news** in same topic strand | Route **decisions** to **primary** PDFs/captures; keep listicles as **exploratory** in [`Tennessee hobby farm…`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md). |
| **Soil / “smart farming”** | Vendor IoT + **academic** + **extension** | Operational claims (capacity, liming, rotation) → **extension / NRCS**; ML/sensor surveys → labeled **exploratory**. |
| **Road / pond / homestead hydrology** | Forum threads + **handbook PDFs** | Use forums for **failure-mode color** only; **engineering** claims need **handbook / NRCS / PE**. |
| **Agritourism** | Lifestyle blogs vs **PC498** statute | Statute + DOR for **tax/legal triggers**; blogs for **UX/marketing ideas** only. |

---

## 4. Thin or hard-to-navigate layers

| Layer | Symptom | Fix |
|-------|---------|-----|
| **Onboarding** | New readers see long `index` analysis lists | Package hub + **execution dossier** + this audit as **“start here”** triad; see [`overview`](../overview.md). |
| **Glossary** | Few entries vs. many named gates (`G1`, `V*`, `Fin-G*`) | [`Evidence grade` glossary](../glossary/evidence-grade.md) + link from [`glossary hub`](../glossary/smart-farm-wiki-glossary.md). |
| **Canonical vs exploratory** | Analyses read as equal weight | Use [`Evidence grade and canonical authority`](../concepts/evidence-grade-and-canonical-authority.md) vocabulary; **business plan package** lists **canonical** spine vs supporting. |

---

## 5. Pages or sections where canonical authority was unclear (resolved by routing)

| Reader confusion | Resolution |
|------------------|------------|
| “Which page is the **business plan**?” | **Package hub** [`east-tennessee-two-site-farm-business-plan`](../business-plan/east-tennessee-two-site-farm-business-plan.md); framework = rubric **child**. |
| “Where is **distance tax** definitive?” | [`Two-site operations model — 5 ac / 120 ac`](two-site-operations-model-5ac-homebase-120ac-production.md) + [`Trip policy`](trip-batching-and-site-visit-policy-two-site-smart-farm.md). |
| “Where is **telemetry authority**?” | [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md) + [`Reference architecture`](reference-architecture-5ac-homebase-120ac-smart-farm.md). |
| “What **sources** back TN execution?” | [`Authoritative execution evidence cluster`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md). |

---

## 6. Recommended canonical updates (prioritized)

**P0 — structural (high value, low churn)**

1. **Package hub** — short **Authority & execution evidence** block (links to cluster + audit).
2. **Two-site operations topic** — **Regulatory & site evidence** row pointing to cluster + WSS/septic/NASS.
3. **Farm spatial model** — **Authoritative land-intelligence references** subsection.
4. **Capital plan** — **FSA / program references** line (not application advice).
5. **Execution dossier hub** — link this audit under **Related**.

**P1 — entities**

6. **Farm parcels** — soil survey + permit **authority chain** (no parcel numbers).
7. **farmOS** — documentation capture links for Location / Assets / Logs.

**P2 — meta**

8. **Domain content overview** — pointer to this audit under steering / backlog.
9. **Phase timeline** — one **evidence** milestone row.

**Defer**: New parallel “strategy” analyses; duplicate economics essays. Extend **existing** worksheets and **remediation** items instead.

---

## 7. Anti–analysis-swamp guardrails (restated)

- **One** durable **owner** per cluster per [`Structural audit — page ownership…`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md).
- New **operational** content should **attach** to **entity**, **artifact table**, or **validation ID**—not float as a third narrative.
- **Query syntheses** stay **time-stamped** or fold into hubs when promoted to doctrine.

---

## Related

- [`Domain content overview`](domain-content-overview.md)
- [`Business plan source-ingest campaign`](business-plan-source-ingest-campaign-east-tennessee-two-site.md)
- [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md)
