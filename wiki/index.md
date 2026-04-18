# Wiki index

First-stop navigation for humans and agents. Every **intentional** wiki page should appear here unless it is intentionally transient (rare); orphans are reported by `scripts/validate_wiki.py`.

## Overview

- [Wiki overview](overview.md) — North-star summary of this vault’s purpose and rules.
- [Repository analysis](analyses/repository-analysis.md) — This repo’s layout, tooling, CI, corpus scale, and design tradeoffs (meta; complements `docs/`).
- [Domain content overview](analyses/domain-content-overview.md) — What this wiki is *about*: land, connectivity, power, data, business, and time/PNT strands.
- [Structural audit — repository shape and canonical routing](analyses/structural-audit-repository-and-canonical-routing.md) — IA strengths, overlap risks, hub/entity gaps, merge policy; complements `AGENTS.md`.
- [Structural audit — page ownership, entity gaps, and hub routing](analyses/structural-audit-page-ownership-entity-gaps-and-hub-routing.md) — Canonical clusters vs supporting analyses, entity backlog, hub routing; **anti–analysis-swamp** companion to `AGENTS.md`.
- [Structural debt audit — wiki IA and operational maturity](analyses/structural-debt-audit-wiki-ia-and-operational-maturity.md) — Analysis sprawl, guide/standard metadata, `operational_maturity`, flat-index pain; links implemented fixes.
- [Wiki navigation and structural hubs](topics/wiki-navigation-and-structural-hubs.md) — Themed router: meta audits, ET two-site spine, homelab/k3s package, runbooks (complements the flat analyses list).
- [Execution readiness gap audit — East Tennessee operational knowledge](analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md) — Missing execution-grade data, mixed-authority clusters, glossary/timeline/onboarding gaps, **recommended canonical updates** (no invented parcel facts).
- [Evidence grade and canonical authority](concepts/evidence-grade-and-canonical-authority.md) — Vocabulary: **canonical** vs **supporting** vs **exploratory**; raw vs public intelligibility.
- [Authoritative execution evidence cluster — East Tennessee (source index)](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) — Hub for **agency/extension** ingests (soils, NASS, DOR, FSA, septic, farmOS docs, CISA, DC/Starlink batch).
- [Electrical, networking, and Starlink — inbox batch (2026-04-23)](source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md) — Victron / NREL / Morse Micro / Starlink / UT PDFs + wiring & WAN captures.
- [Off-grid power, field RF, and optional WAN — source index (Demory planning)](source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) — **Provenance** **hub** **for** **off-grid-first** **`SITE_FARM`** **:** NREL, Victron, Meshtastic, HaLow, Starlink **captures** **.**

## Business plan (East Tennessee two-site)

**First-class package** (~5 ac home base + ~120 ac production + phased strategy). Start at the **package hub**; the **planning framework** holds full rubrics, knowns/unknowns, and embedded tables.

- [East Tennessee two-site farm business plan (package)](business-plan/east-tennessee-two-site-farm-business-plan.md) — **Navigation spine**: reading order, execution pilots, artifacts, finance layer, critique, Git/PR wiring.
- **Site intelligence (Claxton + Demory anchors)**: [Claxton home base — Anderson County](analyses/claxton-home-base-site-intelligence.md), [Demory farm — Campbell County](analyses/demory-farm-site-intelligence.md) (**off-grid-first** **hub** **:** [off-grid power — Demory](analyses/off-grid-power-strategy-demory-farm-site.md), [mesh/field RF — Demory](analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md), [off-grid topology (Mermaid)](analyses/off-grid-farm-execution-topology-demory-mermaid.md)), [Anderson vs Campbell — operating implications](comparisons/anderson-county-vs-campbell-county-operating-implications.md).
- [Local site and county intelligence](topics/local-site-and-county-intelligence.md) — **Router** beside the package: Anderson/Campbell, Claxton/Demory entities, comparison, validation, missing-data register (ties **agency** evidence to **named places**).
- [Authoritative execution evidence cluster — East Tennessee (source index)](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) — **Agency/extension catalog** (NASS, NRCS, FSA, septic, farmOS, CISA, …) grounded in `raw/processed/` via source-notes.
- [Ingest visibility gap — authoritative evidence vs published wiki (East Tennessee)](analyses/ingest-visibility-gap-authoritative-evidence-east-tennessee.md) — **IA diagnosis**: why authoritative ingests felt quiet; remediation checklist.
- [Parcel intelligence package — East Tennessee two-site](topics/parcel-intelligence-package-east-tennessee-two-site.md) — **Hub**: Claxton + Demory parcel worksheets, blank template, WSS ingest pointers.
- [Parcel intelligence worksheet (blank template)](topics/parcel-intelligence-worksheet-template.md) — Reusable section order (soils, slope, hydrology, access, utilities, telemetry candidates, validation tasks).
- [Parcel intelligence — Claxton home base](analyses/parcel-intelligence-claxton-home-base-east-tennessee-two-site.md) — `SITE_HOME` worksheet (placeholders; WSS process ref ingested).
- [Parcel intelligence — Demory farm site](analyses/parcel-intelligence-demory-farm-site-east-tennessee-two-site.md) — `SITE_FARM` worksheet (Campbell WSS table from vault; AOI clip pending).
- [Claxton and Demory — missing data register](analyses/claxton-and-demory-missing-data-register.md) — **Parcel gaps** still not knowable from vault sources; how to resolve; what **V\*/G\*** rows they affect.
- [East Tennessee two-site farm business plan — planning framework](analyses/east-tennessee-two-site-farm-business-plan-framework.md) — Detailed hub and document tree.
- [East Tennessee two-site farm business plan — executive summary](analyses/east-tennessee-two-site-farm-business-plan-executive-summary.md) — One-page map.
- [East Tennessee two-site farm business plan — vision, objectives, and constraints](analyses/east-tennessee-two-site-farm-business-plan-vision-and-constraints.md)
- [East Tennessee two-site farm business plan — two-site operating model](analyses/east-tennessee-two-site-farm-business-plan-two-site-operating-context.md) — 5 ac control center; **35-min distance tax** (structural).
- [Trip batching and site visit policy — two-site smart farm](analyses/trip-batching-and-site-visit-policy-two-site-smart-farm.md) — **Justified trips**, batching, remote observability, **failure patterns**.
- [Two-site structure disqualifiers — East Tennessee package](analyses/two-site-structure-disqualifiers-east-tennessee.md) — **Poor-fit** enterprises and **self-disqualifying** ops.
- [Enterprise options analysis — 120-acre East Tennessee two-site smart farm](analyses/east-tennessee-two-site-farm-business-plan-enterprise-options-analysis.md) — Scenario matrix.
- [Recommended enterprise strategy — phased East Tennessee path](analyses/east-tennessee-two-site-farm-business-plan-recommended-enterprise-strategy.md) — Phase 1–2 **default** (stocker-led beef) vs **fallback** (lease/custom), deferred paths, decision boundaries.
- [Smart technology and telemetry strategy — control center on 5 acres](analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) — **AA/AF/PA/SO** decision controls; links **stop rules**.
- [Connectivity strategy — Claxton home base and Demory farm site](analyses/connectivity-strategy-for-claxton-and-demory.md) — **Canonical two-site WAN**: Starlink, LTE, terrestrial assumptions; pilot vs scale; power, cost, security, degraded modes; **named** Anderson/Campbell anchors.
- [Execution topology package — two-site smart farm (Mermaid)](analyses/execution-topology-package-two-site-smart-farm.md) — **Reference / pilot / degraded** diagrams; **Z1/Z2/Z3**, WAN vs **local-only survivable**; links runbooks.
- [Automation stop rules — two-site smart farm](analyses/automation-stop-rules-two-site-smart-farm.md) — **NS/MV** gates; **CS-*** WAN cost/fragility + **CS-5** off-grid energy budget; **MV-7** WAN fade drill; **MV-8** off-grid local-only/SOC drill; **Phase 1** observational-only defaults.
- [Labor model and weekly operating rhythm](analyses/east-tennessee-two-site-farm-business-plan-labor-and-family-model.md)
- [Capital plan and infrastructure sequencing](analyses/east-tennessee-two-site-farm-business-plan-capital-and-financing.md)
- [Revenue model and milestones](analyses/east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md)
- [Risk register and mitigation strategy](analyses/east-tennessee-two-site-farm-business-plan-risk-register.md)
- [East Tennessee two-site farm business plan — 10-year roadmap](analyses/east-tennessee-two-site-farm-business-plan-10-year-roadmap.md) — Phases 0–4.
- [Validation backlog and decision gates](analyses/east-tennessee-two-site-farm-business-plan-validation-backlog.md)
- [Execution dossier — Phase 0–1 (hub)](analyses/execution-dossier-hub-phase-0-1-east-tennessee.md) — **Start here**: memo → 90d → checklist → 12m → 24m.
- [First 90 days — Phase 0–1 execution](analyses/execution-first-90-days-phase-0-1-east-tennessee.md)
- [First 12 months — Phase 0–1 execution](analyses/execution-first-12-months-phase-0-1-east-tennessee.md)
- [First 24 months — Phase 0–1 execution](analyses/execution-first-24-months-phase-0-1-east-tennessee.md)
- [Master checklist — Phase 0–1 execution](analyses/execution-dossier-master-checklist-phase-0-1-east-tennessee.md)
- [Decision memo — Phase 0–1 execution](analyses/execution-dossier-decision-memo-phase-0-1-east-tennessee.md)
- [Validation and pilot plan — first 24 months (East Tennessee two-site)](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) — matrix + T0 calendar windows; **[Connectivity validation](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation)** (survey, power, WAN testing, remote access, Starlink may/must-not, **CS-*** cost stops)
- [Pilot and recon checklists — first 24 months (two-site smart farm)](analyses/pilot-and-recon-checklists-first-24-months-two-site-smart-farm.md)

**Operational artifacts** (tables / matrices):

- [Execution topology package — two-site smart farm (Mermaid)](analyses/execution-topology-package-two-site-smart-farm.md) — Reference / pilot / degraded **Mermaid**; trust boundaries, WAN vs local survivable.
- [Two-site operating model — 5-acre home base and 120-acre farm](analyses/two-site-operations-model-5ac-homebase-120ac-production.md) — **Authoritative distance-tax**; see also [`trip policy`](analyses/trip-batching-and-site-visit-policy-two-site-smart-farm.md) and [`disqualifiers`](analyses/two-site-structure-disqualifiers-east-tennessee.md).
- [Family labor model and coverage matrix — two-site smart farm](analyses/family-labor-model-and-coverage-matrix-two-site-smart-farm.md)
- [Instrumentation priority matrix — two-site smart farm](analyses/instrumentation-priority-matrix-two-site-smart-farm.md)
- [Capital phasing table — years 0 to 10](analyses/capital-phasing-table-years-0-10-two-site-smart-farm.md)
- [Business risk register — two-site smart farm](analyses/business-risk-register-two-site-smart-farm.md)
- [Manual fallback and degraded modes — critical operations](analyses/manual-fallback-degraded-modes-critical-operations.md)
- [Validation backlog — assumptions before major spend](analyses/validation-backlog-before-major-spend-two-site-smart-farm.md)

**Financial planning layer** (methodology; evidence fills placeholders):

- [Enterprise unit economics — worksheet methodology (two-site smart farm)](analyses/enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md)
- [CAPEX, OPEX, and enterprise sequencing — two-site constraint](analyses/capex-opex-enterprise-sequencing-two-site-constraint.md)
- [Farm accounting baseline — chart of accounts and enterprise P&L structure](analyses/farm-accounting-baseline-chart-of-accounts-enterprise-pl-two-site-smart-farm.md)
- [Revenue milestone model — supplemental to salary replacement](analyses/revenue-milestone-model-supplemental-to-salary-replacement.md)
- [Execution gates — financial thresholds (Phase 0→4)](analyses/execution-gates-financial-thresholds.md)
- [Instrumentation ROI model — two-site smart farm](analyses/instrumentation-roi-model-two-site-smart-farm.md) — Triage, **FP** cost, upkeep, **DC-*** decommission.

**Critique, remediation, source campaign:**

- [East Tennessee two-site farm business plan — hostile internal review](analyses/east-tennessee-two-site-farm-business-plan-hostile-internal-review.md)
- [Business plan remediation backlog](analyses/east-tennessee-two-site-farm-business-plan-remediation-backlog.md)
- [Business plan source-ingest campaign — East Tennessee two-site](analyses/business-plan-source-ingest-campaign-east-tennessee-two-site.md)

**Wiki / repository wiring** (merge order for markdown work, not farm operations):

- [Smart Farm Wiki — repository implementation plan (business plan integration)](analyses/smart-farm-wiki-repository-implementation-plan.md)
- [Business plan wiki — Git-friendly execution sequence](analyses/business-plan-wiki-git-execution-sequence.md)

## Entities

Stable **named** subjects—products, **modeled sites**, **infrastructure systems**—distinct from **concepts** (generic ideas like “LoRaWAN”). See **`AGENTS.md`** (entity-first, page ownership).

- [Example Organization](entities/example-org.md) — Fictional org used to demonstrate entity pages.
- [farmOS](entities/farmos.md) — Open-source Drupal-based farm management / records (canonical product page).
- [Home Assistant](entities/home-assistant.md) — Open-source home automation platform; telemetry consumer / UI in two-site stack discussions.
- [Five-acre home base (SITE_HOME) — ET two-site](entities/five-acre-home-base-site-home-et-two-site.md) — Homestead / control-center **role** (planning labels, not a deed).
- [120-acre production farm (SITE_FARM) — ET two-site](entities/120-acre-production-farm-site-farm-et-two-site.md) — Production parcel **role** for the ET scenario.
- [Claxton home base (place, Anderson County)](entities/claxton-home-base.md) — Named **geographic anchor** for `SITE_HOME` (not a deed).
- [Demory farm site (place, Campbell County)](entities/demory-farm-site.md) — Named **geographic anchor** for `SITE_FARM` (not a deed).
- [Anderson County, Tennessee (two-site context)](entities/anderson-county-tennessee.md) — County-level **operating object** (NASS + qualitative context for Claxton).
- [Campbell County, Tennessee (two-site context)](entities/campbell-county-tennessee.md) — County-level **operating object** (NASS + WSS session discipline for Demory).
- [Farm parcels and land units](entities/farm-parcels-and-land-units.md) — Parcels, paddocks, zones; ties to spatial registry + farmOS geometry.
- [Farm water infrastructure system](entities/farm-water-infrastructure-system.md) — Water movement, storage, irrigation, livestock water as one system.
- [Farm on-site power system](entities/farm-on-site-power-system.md) — Grid/solar/gen/loads at farm scale; links runbooks and power topics.
- [Field telemetry network — two-site](entities/field-telemetry-network-two-site.md) — End-to-end field telemetry stack (radios → broker → consumers → SoR).

## Concepts

- [Smart Farm Wiki — mission, audience, and voice](concepts/smart-farm-wiki-mission-and-values.md) — Mission statement, vision, values, and prose style; domain “why” (complements `AGENTS.md`).
- [LLM Wiki pattern](concepts/llm-wiki-pattern.md) — Core ideas: raw vs wiki, synthesis, maintenance.
- [Composting](concepts/composting.md) — Aerobic decomposition of organics into soil amendment; homestead synthesis cluster.
- [Data storage (farm and edge stacks)](concepts/data-storage.md) — MQTT handoff vs PostgreSQL/PostGIS durable data; links to official docs.
- [Decentralized physical infrastructure networks (DePIN)](concepts/depin.md) — Token-incentivized physical/digital infrastructure framing (see sources).
- [ESP32](concepts/esp32.md) — Espressif SoC family common in IoT, sensors, and displays.
- [LoRa (radio)](concepts/lora-radio.md) — LoRa PHY vs LoRaWAN and mesh stacks.
- [LoRaWAN](concepts/lorawan.md) — LPWAN stack for long-range sensors; common in farm IoT backhaul framing.
- [Meshtastic](concepts/meshtastic.md) — LoRa mesh firmware for off-grid comms and field nodes.
- [Network Time Protocol (NTP)](concepts/network-time-protocol.md) — Clock sync over IP; typical ms-scale for general hosts.
- [Precision agriculture](concepts/precision-agriculture.md) — Data-driven field management concept (Wikipedia-sourced note).
- [Precision Time Protocol (PTP)](concepts/precision-time-protocol.md) — IEEE 1588 clock sync; hardware timestamping for tight discipline.
- [Wi-Fi HaLow](concepts/wi-fi-halow.md) — IEEE 802.11ah sub-GHz Wi‑Fi for IoT range/power tradeoffs.
- [Evidence grade and canonical authority](concepts/evidence-grade-and-canonical-authority.md) — How to read **canonical** pages vs **supporting** analyses vs **low-authority** sources.

## Topics

- [Knowledge synthesis](topics/knowledge-synthesis.md) — Cross-cutting theme for how conclusions are built here.
- [Two-site smart farm operations](topics/two-site-smart-farm-operations.md) — **Hub**: East TN 5 ac + 120 ac business plan, operational artifacts, telemetry, runbooks, comparisons.
- [Wiki navigation and structural hubs](topics/wiki-navigation-and-structural-hubs.md) — **Meta router**: IA audits, canonical clusters, homelab guide entry, runbooks; escape hatch from flat `index.md` analyses list.
- [Local site and county intelligence](topics/local-site-and-county-intelligence.md) — **Router**: Anderson/Campbell context, Claxton/Demory site intel, comparison, missing-data register, validation plan.
- [Parcel intelligence package — East Tennessee two-site](topics/parcel-intelligence-package-east-tennessee-two-site.md) — Parcel worksheets (Claxton/Demory), blank template, WSS pointers.
- [Agritourism, tiny housing, and natural building sources](topics/agritourism-tiny-housing-and-natural-building.md) — Farm stays, natural building, agritourism listicles, news excerpts.
- [Tennessee hobby farm and small-farm business sources](topics/tennessee-hobby-farm-and-small-farm-business-sources.md) — Hobby-farm primers, TN business guides, USDA BFR, revenue/licensing excerpts, startup PDFs.
- [Backyard livestock and homestead animal sources](topics/backyard-livestock-and-homestead-animals.md) — Poultry/cattle guides, AI husbandry marketing, PDF papers.
- [ESP32, ESPHome, and smart-farming builds](topics/esp32-iot-smart-farming-and-tooling.md) — MCU guides, smart-farming firmware README, ESPHome CYD.
- [Docker, Kubernetes, Compose, and Bake (edge and homelab)](topics/docker-kubernetes-compose-and-bake.md) — Compose, Bake, k3s/RKE2, distro comparisons for self-hosted stacks.
- [Farm data, farmOS, and agriculture lab builds](topics/farm-data-farmos-and-ag-lab-builds.md) — farmOS (Drupal), ag-lab automation thread, sensor integration hints.
- [Field network IoT comparisons (HaLow, LoRa, NB-IoT)](topics/field-network-iot-comparisons.md) — Comparative articles on LPWAN / HaLow / cellular IoT.
- [LoRa, MQTT, and gateway bridges](topics/lora-mqtt-and-gateway-bridges.md) — LoRaWAN app MQTT, OpenMQTTGateway, DIY gateways, Meshtastic MQTT thread, HA LoRa exploration.
- [Homestead and regional gardening sources](topics/homestead-and-regional-gardening-sources.md) — Small-farm book import and Tennessee gardening guide.
- [Homestead composting and soil sources](topics/homestead-composting-and-soil-sources.md) — EPA, NRDC, Wikipedia, extension, Earth Easy captures; practical composting guide.
- [Irrigation and water-wise farming sources](topics/irrigation-and-water-wise-farming-sources.md) — Solar pumping, drip/sprinkler tradeoffs, DIY homestead irrigation, sensor zones; ingested batch.
- [Homelab, self-hosting, and edge narratives](topics/homelab-self-hosting-and-edge-narratives.md) — Homelab guides, Reddit threads, AI architecture, partial solar rack.
- [Home workshop, 3D printing, basement, off-grid smart home sources](topics/home-workshop-3d-printing-basement-offgrid-smart-home-sources.md) — Shop/basement maker ingests; off-grid smart-home automation themes.
- [Off-grid solar power and storage (special topic)](topics/off-grid-solar-power-and-storage.md) — PV, charge control, battery sizing: homestead, off-grid homes, field power.
- [Ponds, water features, and homestead hydrology](topics/ponds-water-features-and-homestead-hydrology.md) — DIY ponds, biofilters, farm ponds, fountains, pumping.
- [Rural road and driveway erosion sources](topics/rural-road-and-driveway-erosion-sources.md) — Unpaved road drainage, water bars, hillside sediment; ingested batch.
- [Position, navigation, and timing alternatives](topics/position-navigation-and-timing-alternatives.md) — BPS, LORAN, resilient trackers beyond GPS.
- [Smart agriculture, Meshtastic, and LoRaWAN](topics/smart-agriculture-meshtastic-and-lorawan.md) — Field networks: precision-ag LoRaWAN vs Meshtastic mesh deployments.
- [Sustainable cropping, soil, and farm entry sources](topics/sustainable-cropping-soil-and-farm-entry-sources.md) — Rotations, cover crops, SARE, TN beginning-farmer links.
- [Smart home — Matter, Thread, and Home Assistant AI (special topic)](topics/smart-home-matter-thread-and-home-assistant-ai.md) — Matter/Thread interoperability and HA AI tooling.
- [Smart mirror and e-paper display builds](topics/smart-mirror-and-e-paper-displays.md) — MagicMirror² ecosystem + E Ink survey.
- [Time synchronization — NTP and PTP sources](topics/time-synchronization-ntp-and-ptp.md) — NTP/PTP references, GNSS-disciplined Pi clocks, Time Pi Ansible, forums.

## Source notes

- [Authoritative execution evidence cluster — East Tennessee (index)](source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) — **Hub**: soils, elevation, septic, NASS rents, TN tax/ag exemption, FSA, farmOS, CISA—links to ingested source-notes.
- [Campbell County — Web Soil Survey AOI soil map tab (capture)](source-notes/campbell-county-wss-aoi-soil-map-tab-capture-2026-04-18.md) — Soil map units / AOI acres for Campbell WSS session (Demory farm intelligence).
- [CISA — Guide to securing remote access software (PDF)](source-notes/cisa-guide-securing-remote-access-software-508-pdf.md) — Remote access hardening; foundation ingest 2026-04.
- [CISA — Joint guide OT cybersecurity asset inventory (PDF)](source-notes/cisa-joint-guide-ot-cybersecurity-asset-inventory-508-pdf.md) — OT asset inventory process.
- [CISA — Foundations for OT asset inventory (excerpt)](source-notes/cisa-joint-foundations-ot-asset-inventory-guidance-excerpt.md) — Markdown excerpt companion.
- [CISA — Modern approaches to network access security (excerpt)](source-notes/cisa-modern-approaches-network-access-security-excerpt.md)
- [CISA — Primary mitigations for OT cyber threats (excerpt)](source-notes/cisa-primary-mitigations-ot-cyber-threats-excerpt.md)
- [farmOS model — Assets (documentation)](source-notes/farmos-model-assets-documentation.md) — Asset types, UUIDs; ties to spatial registry.
- [farmOS model — Logs (documentation)](source-notes/farmos-model-logs-documentation.md) — Log types; event→asset pattern.
- [NRCS — FY25 conservation scenarios (PDF, large)](source-notes/nrcs-fy25-conservation-scenarios-pdf.md) — Practice scenarios; planning context.
- [NRCS Tennessee — Grazing Lands GLCI (page excerpt)](source-notes/nrcs-tennessee-grazing-lands-glci-excerpt.md)
- [UT Extension — FM Boot 2017 budgets (Velandia) (PDF)](source-notes/ut-extension-fm-boot-2017-budgets-velandia-pdf.md)
- [UT — W1348 cut flower enterprise budgets (PDF)](source-notes/ut-publication-w1348-pdf.md)
- [UT — W1268 sheep enterprise budget template (PDF)](source-notes/ut-publication-w1268-pdf.md)
- [UT — D154 publication (PDF)](source-notes/ut-publication-d154-pdf.md)
- [UT — D31 publication (PDF)](source-notes/ut-publication-d31-pdf.md)
- [UT — D33 publication (PDF)](source-notes/ut-publication-d33-pdf.md)
- [UT — D252A publication (PDF)](source-notes/ut-publication-d252a-pdf.md)
- [UT — D252C publication (PDF)](source-notes/ut-publication-d252c-pdf.md)
- [UT — D252D publication (PDF)](source-notes/ut-publication-d252d-pdf.md)
- [UT — D32 publication (PDF)](source-notes/ut-publication-d32-pdf.md)
- [USDA NASS — Tennessee cash rent surveys 2024 (PDF)](source-notes/nass-cash-rents-tn-2024-surveys-pdf.md)
- [USDA NASS — Cash rents survey page (capture)](source-notes/usda-nass-cash-rents-survey-page-inbox-2026-04-18.md)
- [Tennessee Revenue — Agricultural exemption Jan 2023 (PDF)](source-notes/tn-revenue-agricultural-exemption-jan2023-pdf.md)
- [Agricultural exemption — page capture](source-notes/agricultural-exemption-page-inbox-2026-04-18.md)
- [NRCS — CEAP E472A / E528R FY2025 (PDF)](source-notes/nrcs-ceap-e472a-e528r-fy2025-pdf.md)
- [UT Beef & Forage Center — PB1663 resource calendar 2026 (PDF)](source-notes/ut-beef-forage-center-pb1663-resource-calendar-2026-pdf.md)
- [Tennessee — Public Chapter 498 agritourism act (PDF)](source-notes/tn-public-chapter-498-agritourism-act-pdf.md)
- [Livestock Companion — Vol. 17 Apr 2025 (PDF)](source-notes/livestock-companion-vol-17-2025-04-pdf.md)
- [USDA FSA — program pages (captures)](source-notes/fsa-program-pages-capture-inbox-2026-04-18.md)
- [farmOS — documentation captures (inbox)](source-notes/farmos-documentation-captures-inbox-2026-04-18.md)
- [Homelab backup stack — official captures (restic, Longhorn, farmOS Docker)](source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md) — **2026-04-18** ingest: restic 0.18.1, Longhorn system backup/restore, farmOS Docker dev capture (epistemic: v1/MariaDB era).
- [Backup / DR — official documentation cluster (k3s, Longhorn, Rancher, PostgreSQL, farmOS)](source-notes/backup-dr-official-documentation-cluster.md) — Provenance hub: link batch + captures for the DR package.
- [K3s, Longhorn, Rancher, Raspberry Pi — platform captures (inbox 2026-04)](source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md) — docs.k3s.io architecture/install/quick-start/config; Longhorn CSI on K3s; Pi homelab narrative; Rancher product page.
- [Homelab, edge, and networking — inbox batch (2026-04-18)](source-notes/homelab-edge-networking-inbox-batch-2026-04-18.md) — **Ingest wave**: k3s/Longhorn/restic/RKE2 essays, farmOS Docker, ESPHome/Mosquitto, WireGuard, **OpenWrt PDF** + extract; `raw/processed/2026/` kebab paths.
- [Tennessee — onsite sewage / septic (captures)](source-notes/tn-onsite-sewage-septic-captures-inbox-2026-04-18.md)
- [Web Soil Survey & 3D Elevation — captures](source-notes/web-soil-survey-and-elevation-captures-inbox-2026-04-18.md)
- [Web Soil Survey — product home page (capture)](source-notes/web-soil-survey-home-page-inbox-2026-04-18.md) — WSS app landing / how to run (process reference; not parcel soils).
- [Tennessee General Assembly — bill information (capture)](source-notes/tennessee-general-assembly-bill-info-capture-inbox-2026-04-18.md)
- [Erosion control on steep road — r/homestead](source-notes/erosion-control-steep-road-reddit-homestead.md) — Ditches, crown, water bars, outslope, rolling dips, handbook PDF link.
- [Example LLM Wiki note (raw)](source-notes/example-llm-wiki-note.md) — Grounding note for `raw/processed/2026/example-llm-wiki-note.md`.
- [3D printed workshop equipment — organizing (source)](source-notes/3d-printed-workshop-equipment-organizing.md) — Printed organizers; shop storage.
- [Basement dream workshop — r/DIY (source)](source-notes/basement-dream-workshop-reddit.md) — Build thread: access, noise, dust, power.
- [Beginner's guide — off-grid energy solutions (source)](source-notes/beginners-guide-off-grid-energy-solutions.md) — Energy tech overview.
- [Build off-grid smart home — step-by-step (source)](source-notes/build-off-grid-smart-home-step-by-step.md) — Planning / automation themes.
- [Choosing 3D printer types — deep dive (source)](source-notes/choosing-3d-printer-types-deep-dive.md) — FDM, SLA, SLS; materials.
- [Craft room or workshop — basement remodel (source)](source-notes/craft-room-or-workshop-basement-remodel-hobbyists.md) — Hobbyist basement design.
- [Do you have a 3D printer for your shop? — Garage Journal (source)](source-notes/do-you-have-3d-printer-for-your-shop.md) — Shop uses; jigs; molds.
- [Finally time — 3D printer in garage (source)](source-notes/finally-time-3d-printer-in-garage.md) — Garage install expectations.
- [Future of manufacturing — 3D printing deep dive (source)](source-notes/future-manufacturing-deep-dive-3d-printing.md) — Additive manufacturing survey.
- [Off grid smart home (source)](source-notes/off-grid-smart-home.md) — Short consumer listicle capture.
- [Off-grid tiny houses — complete guide (source)](source-notes/off-grid-tiny-houses-complete-guide.md) — Tiny off-grid systems.
- [Organize workshop with 3D printer — online tools (source)](source-notes/organize-workshop-3d-printer-free-online-tools.md) — Digital + printable workflow.
- [Smart home for off-grid — forum capture (source)](source-notes/smart-home-for-off-grid.md) — HA, battery SOC, load shedding.
- [Take your home off-grid the smart way (source)](source-notes/take-home-off-grid-smart-way.md) — Planning article.
- [12 shop layout tips (source)](source-notes/twelve-shop-layout-tips.md) — Layout listicle.
- [Turn basement into DIY utopia (source)](source-notes/turn-basement-into-diy-utopia.md) — Remodel narrative.
- [Turning basement into perfect workspace (source)](source-notes/turning-basement-into-perfect-workspace.md) — Workspace conversion.
- [Ultimate guide — off-grid homes (source)](source-notes/ultimate-guide-off-grid-homes.md) — Broad off-grid housing primer.
- [Ultimate woodworking workshop at home (source)](source-notes/ultimate-woodworking-workshop-at-home-step-by-step.md) — Home wood shop setup.
- [Weekend project — basement workshop (source)](source-notes/weekend-project-basement-workshop.md) — Short basement shop project.
- [Workshop layout options — pictures (source)](source-notes/workshop-layout-options-pictures-attached.md) — Layout photos / discussion.
- [Backyard ponds — farm waterfall forum (short)](source-notes/backyard-ponds-farm-waterfall-forum-short.md) — Liner/stone/waterfall tips fragment.
- [Beginning farmer resources (TN + USDA)](source-notes/beginning-farmer-resources-list.md) — Link hub for programs and manuals.
- [Cover crops — sustainable rotations (article)](source-notes/cover-crops-sustainable-crop-rotations.md) — SARE-style cover crop piece.
- [Cover crops — sustainable rotations (PDF)](source-notes/cover-crops-sustainable-crop-rotations-pdf.md) — Large PDF companion; confirm metadata inside.
- [Crop rotations overview](source-notes/crop-rotations-overview.md) — Rodale-style soil health explainer.
- [Cultivating the Future — sustainable farming](source-notes/cultivating-the-future-sustainable-farming-deep-dive.md) — Essay capture.
- [13 tips — starting a hobby farm (AgAmerica)](source-notes/agamerica-13-tips-starting-hobby-farm.md) — Zoning, plan, fencing, mindset checklist.
- [Beginning farmers and ranchers (USDA farmers.gov)](source-notes/beginning-farmers-and-ranchers-usda-farmers-gov.md) — BFR coordinators, programs entry.
- [How to start a hobby farm — beginner's guide (KW Land)](source-notes/kw-land-how-to-start-hobby-farm-beginners-guide.md) — Hobby vs commercial framing, pros/cons.
- [What's a hobby farm? (Land.com)](source-notes/land-com-whats-a-hobby-farm-guide.md) — Definition, USDA small-farm stats, time/cost reality.
- [newbusiness-checklist (PDF)](source-notes/newbusiness-checklist-pdf.md) — Checklist PDF import; confirm inside PDF.
- [Shopify — start a business in TN (10 steps, 2025)](source-notes/shopify-how-to-start-business-tennessee-10-steps-2025.md) — TN startup outline; not legal advice.
- [TN business tax / TNTAP licensing excerpt](source-notes/tennessee-business-tax-registration-licensing-tntap.md) — Gross receipts, county license fee notes.
- [TN Smart Startup Guide (PDF)](source-notes/tn-smart-startup-guide-pdf.md) — Large TN startup PDF; confirm edition inside file.
- [Zarla — how to start a business in Tennessee](source-notes/zarla-how-to-start-business-in-tennessee.md) — Stepwise TN formation article.
- [ezcGman LoRa-to-MQTT gateway (ESP32, EByte)](source-notes/ezcgman-lora-to-mqtt-gateway-esp32-ebyte.md) — DIY gateway PCB + broker integration.
- [Home Assistant — LoRa long-range sensors / MQTT exploration](source-notes/home-assistant-lora-long-range-sensors-mqtt-exploration.md) — ESP32 SX1276 P2P LoRa to extend HA reach.
- [How to make water go uphill without electricity](source-notes/how-to-make-water-go-uphill-without-electricity.md) — Ram pumps, siphons, low-input lifts.
- [How to start farming with no money](source-notes/how-to-start-farming-with-no-money.md) — Bootstrap listicle capture.
- [Keeping your horse at home](source-notes/keeping-your-horse-at-home.md) — Small-farm horse basics.
- [Kentucky EPSC — protecting slopes (PDF)](source-notes/kentucky-epsc-protect-slopes-guide-pdf.md) — Seed/mulch, blankets, contour rolls; construction slopes.
- [Layman's guide — private access road, Appalachians (PDF)](source-notes/laymans-guide-private-access-road-appalachian-nrcs-2005-pdf.md) — NRCS 2005; grades, curves, waterbars.
- [Low-volume roads BMPs — Chapter 7 roadway drainage (PDF)](source-notes/low-volume-roads-bmp-chapter7-roadway-drainage-pdf.md) — Surface drainage, rolling dips, cross-drains.
- [Management practices for dirt roads — Culebra / Ridge to Reefs (PDF)](source-notes/management-practices-dirt-roads-culebra-ridge-to-reefs-2015-pdf.md) — Sediment reduction practices; rolling dips.
- [Penn State TB — crown and cross-slope, dirt & gravel roads (PDF)](source-notes/penn-state-tb-crown-cross-slope-dirt-gravel-roads-pdf.md) — Crown vs in/out-slope; unpaved cross-slope %.
- [Plant a fountain, dig a pond (Acreage Life)](source-notes/plant-a-fountain-dig-a-pond-acreage-life.md) — Farm pond sizing, liners, stocking, fountains.
- [Pump pond water uphill — hose bib irrigation (Reddit)](source-notes/pond-pump-uphill-hose-bib-irrigation-reddit.md) — Forum advice thread.
- [Pump water uphill](source-notes/pump-water-uphill.md) — Head/flow/pump primer.
- [Designing a resilient smart irrigation system (solar, offline, modular)](source-notes/designing-resilient-smart-irrigation-solar-offline-modular.md) — r/solarpunk project; zones, soil moisture, offline.
- [Dirt road stabilization techniques — Desert Mountain Corp style](source-notes/dirt-road-stabilization-techniques-long-term-durability-desertmtncorp.md) — Grading, aggregates, geotextiles, chemical options; FHWA gravel guide link.
- [DIY garden irrigation](source-notes/diy-garden-irrigation.md) — Bottle drip, soaker hoses, small-plot ideas.
- [Garden irrigation solutions — DIY, efficient, toxin-free (Homestead and Chill)](source-notes/garden-irrigation-solutions-diy-efficient-toxin-free.md) — Soaker, drip, ollas, rainwater, irrigation map.
- [Solar-powered irrigation — sustainable solution for agriculture](source-notes/solar-powered-irrigation-sustainable-solution-agriculture.md) — PV pumps, surface vs submersible, irrigation types.
- [Six tips for road erosion control — SubStrata](source-notes/six-tips-road-erosion-control-substrata.md) — Seasonal erosion factors, construction/traffic, design checklist.
- [Soil stabilization, erosion and dust control — Corrosion Technologies](source-notes/soil-stabilization-erosion-dust-control-corrosion-technologies.md) — Vendor page; Ground Glue–class stabilizers (claims).
- [Sustainable farming — cultivating a water-wise future (CGIAR-style)](source-notes/sustainable-farming-cultivating-water-wise-future.md) — Global water stress, farmer-led irrigation themes.
- [Sustainable irrigation — definition, importance, methods, systems](source-notes/sustainable-irrigation-definition-importance-methods-systems.md) — Drip vs spray, flood tradeoffs, AI, Keyline mention.
- [Sustainable irrigation methods for farming](source-notes/sustainable-irrigation-methods-for-farming.md) — Irrigation types, pumping pipeline stages.
- [Water Power Technologies Office R&D Deep Dive webinars](source-notes/water-power-technologies-office-rd-deep-dive-webinar-series.md) — WPTO hydropower/marine energy webinars (short blurb).
- [Start farming — planning crop rotation (SARE)](source-notes/start-farming-planning-crop-rotation.md) — Rotation planning for new producers.
- [Sustainable food & agriculture investment (short)](source-notes/sustainable-food-agriculture-investment-deep-dive.md) — High-level investment excerpt.
- [Tyrant Farms — DIY pond + self-cleaning biofilter](source-notes/tyrant-farms-diy-backyard-pond-self-cleaning-biofilter.md) — Long build log, ecosystem + filtration.
- [Water features — origins and design (deep dive)](source-notes/water-features-origins-history-design.md) — History/design essay.
- [LoRaWAN + MQTT integration (HiveMQ article)](source-notes/lorawan-mqtt-integration-iot-application-design-hivemq.md) — App-server MQTT patterns, LPWAN constraints.
- [Meshtastic — LoRa ↔ MQTT (Reddit)](source-notes/meshtastic-lora-mqtt-bridge-reddit-thread.md) — Mesh/MQTT policy and 0-hop discussion.
- [MultiTech — MQTT messages / LoRa topics](source-notes/multitech-developer-resources-mqtt-messages-lora-topics.md) — `lora/<DEV-EUI>/...` broker topic reference.
- [MQTT Manager + LoRa poor-man gateway (Instructables)](source-notes/mqtt-manager-lora-poor-man-gateway-instructables.md) — Two ESP32 LoRa modules + MQTT Manager apps.
- [OpenMQTTGateway — Theengs LoRa gateway (v1.8.1)](source-notes/openmqttgateway-theengs-lora-gateway-v1-8-1.md) — Raw LoRa ↔ MQTT pub/sub, config via MQTT/WebUI.
- [7 homelab ideas — why you should have a homelab](source-notes/7-homelab-ideas-why-you-should-have-homelab.md) — Motivation and project ideas for a home lab.
- [Agriculture lab build (2023, r/homelab)](source-notes/agriculture-lab-build-2023-homelab-reddit.md) — Large automated ag lab; farmOS suggested in comments.
- [Build homelab if major is computing — Reddit](source-notes/build-homelab-if-major-computing-reddit.md) — Student-oriented motivation thread.
- [Building Compose projects with Bake](source-notes/building-compose-projects-with-bake.md) — Bake + Compose project wiring.
- [Deep dive — Docker Compose](source-notes/deep-dive-docker-compose.md) — Long single-topic Compose reference.
- [Deep dive — my home lab](source-notes/deep-dive-my-home-lab.md) — Personal inventory-style homelab tour.
- [Docker Bake — comprehensive guide](source-notes/docker-bake-comprehensive-guide.md) — buildx bake at scale.
- [Docker Compose in depth](source-notes/docker-compose-in-depth.md) — Mid-length Compose explainer.
- [farmOS overview (farmOS.org)](source-notes/farmos-overview-farmos-org.md) — Drupal-based farm management platform snapshot.
- [Home Assistant — 20 things wished I knew (installation)](source-notes/home-assistant-20-things-installation.md) — Installation pitfalls and tips listicle.
- [Homelab — AI life architecture deep dive](source-notes/homelab-runs-my-ai-life-architecture.md) — AI-centric homelab architecture article.
- [Homelab server — getting started (2026)](source-notes/homelab-server-getting-started-2026.md) — 2026-era homelab server guide.
- [Homelab underground culvert — Alaska off-grid](source-notes/homelab-underground-culvert-alaska-off-grid.md) — Extreme environment forum capture.
- [How to control erosion in your yard — Lowe's](source-notes/how-to-control-erosion-in-your-yard-lowes.md) — Riprap, wattles, terraces, groundcover; residential slopes.
- [How to improve a steep dirt road — r/OffGridCabins](source-notes/how-to-improve-steep-dirt-road-offgridcabins.md) — Angular gravel, crusher run, swales, rain walks.
- [How to landscape a hillside slope — Las Pilitas](source-notes/how-to-landscape-hillside-slope-stabilize-erosion-laspilitas.md) — Native mix planting; slope drainage checklist.
- [How to maintain a dirt road — Backwoods Home](source-notes/how-to-maintain-dirt-road-backwoodshome.md) — Outslope, grade dips, dragging, tractor blade.
- [K3s or RKE2?](source-notes/k3s-or-rke2.md) — Short distro comparison.
- [Kubernetes distributions overview](source-notes/kubernetes-distributions-overview-kubeadm-k3s-microk8s-minikube-talos-rke2.md) — kubeadm, k3s, MicroK8s, Minikube, Talos, RKE2.
- [Mastering Docker Compose — multi-container apps](source-notes/mastering-docker-compose-multi-container-applications.md) — Practical multi-service Compose guide.
- [Partial solar homelab — EcoFlow](source-notes/partial-solar-homelab-ecoflow.md) — Rack load, stringing, UPS, Home Assistant energy UI.
- [r/homelab wiki — building a homelab](source-notes/rhomelab-wiki-guide-building-homelab.md) — Subreddit wiki capture.
- [RKE2 vs K3s — choosing a distribution](source-notes/rke2-vs-k3s-choosing-right-distribution.md) — Selection criteria and positioning.
- [What led you to homelab — Reddit](source-notes/what-led-you-to-homelab-reddit.md) — Origin-story community thread.
- [When to use K3s and RKE2](source-notes/when-to-use-k3s-and-rke2.md) — Scenario-oriented guidance.
- [5 steps — calculate ideal solar battery storage](source-notes/5-steps-calculate-ideal-solar-battery-storage.md) — Load inventory, daily Wh, autonomy, panel + battery sizing.
- [5 steps — design off-grid solar energy storage](source-notes/5-steps-design-off-grid-solar-energy-storage.md) — Off-grid solar + storage design workflow.
- [Complete off-grid solar system guide (2025)](source-notes/complete-off-grid-solar-system-guide-2025.md) — End-to-end off-grid solar overview.
- [Deep dive — home solar systems](source-notes/deep-dive-home-solar-systems.md) — Residential solar components and framing.
- [DIY off-grid solar — homestead wiring](source-notes/diy-off-grid-solar-homestead-wiring.md) — Practical install and balance-of-system emphasis.
- [EcoFlow power kits — off-grid deep dive](source-notes/ecoflow-power-kits-off-grid-deep-dive.md) — Integrated portable power-station ecosystem.
- [Home Assistant AI deep dive (HASS Podcast)](source-notes/home-assistant-ai-deep-dive-hasspodcast.md) — LLM vision, HACS, Ollama/LiteLLM, MCP-style tooling.
- [Sizing solar — off-grid field studies (Eosense-style)](source-notes/sizing-solar-off-grid-field-studies-eosense.md) — Remote field station loads, autonomy, SLA/AGM constraints.
- [Smart home — Matter and Thread deep dive (Part 1)](source-notes/smart-home-matter-thread-deep-dive-part-1.md) — Matter interoperability and Thread mesh roles.
- [Solar battery bank sizing calculator — off-grid](source-notes/solar-battery-bank-sizing-calculator-off-grid.md) — Ah/Wh, DoD, bank voltage calculator framing.
- [Building solar-powered Meshtastic community network](source-notes/building-solar-powered-meshtastic-community-network.md) — Solar sizing, Heltec/ESP32 power notes, repeater + sensor pairing.
- [How to build a solar Meshtastic node the easy way](source-notes/how-to-build-solar-meshtastic-node-easy-way.md) — Integrated solar node (ThinkNode M6) deployment guide.
- [Meshtastic nodes basics and deployment (Seeed)](source-notes/meshtastic-nodes-basics-deployment-seeed.md) — Roles, maps, range, solar kits vs DIY.
- [LoRaWAN farmers money and yields (TEKTELIC)](source-notes/lorawan-farmers-money-yields-tektelic.md) — Vendor overview of LoRaWAN in agriculture and case studies.
- [Semtech LoRa smart agriculture applications](source-notes/semtech-lora-smart-agriculture-applications.md) — Semtech marketing summary of LoRa/LoRaWAN ag use cases.
- [Solar Meshtastic GPS ESP32 outdoor](source-notes/solar-meshtastic-gps-esp32-outdoor.md) — Power envelopes and informal multi-node GPS query behavior.
- [Deep look Wi‑Fi HaLow vs LoRaWAN (Newracom)](source-notes/deep-look-wi-fi-halow-lorawan-newracom.md) — Vendor LPWAN comparison and claims.
- [Experimental HaLow vs LoRa smart grid (Sensors 2023)](source-notes/experimental-halow-lora-smart-grid-sensors.md) — Peer-reviewed field performance study.
- [Compost — Earth Easy complete home gardeners guide](source-notes/eartheasy-how-to-compost-complete-home-gardeners-guide.md) — Long how-to: ratios, systems, troubleshooting.
- [Compost — EPA at home](source-notes/epa-composting-at-home.md) — Backyard composting, vermicomposting, rodent tips; appliance caveat.
- [Compost — extension home backyard introduction](source-notes/extension-home-backyard-composting-introduction.md) — Intro + benefit list; NCSU-style video links.
- [Compost — NRDC 101 guide](source-notes/nrdc-composting-101-guide.md) — Cold vs hot, C:N, landfill methane, community composting.
- [Compost — ultimate guide food waste reduction](source-notes/composting-ultimate-guide-food-waste-reduction.md) — Food-waste framing; compostables and cautions.
- [Compost — Wikipedia article](source-notes/compost-wikipedia-article.md) — Fundamentals, microbes, C:N, hot process.
- [Compare Wi‑Fi HaLow and LoRa (Morse Micro)](source-notes/compare-wi-fi-halow-lora-morse-micro.md) — Short vendor positioning piece.
- [DePIN Wikipedia excerpt](source-notes/depin-wikipedia.md) — Decentralized physical infrastructure snapshot.
- [Five Acres and Independence full text](source-notes/five-acres-and-independence-full-text.md) — Large historical small-farm guide import.
- [IEEE 802.11ah Wikipedia excerpt](source-notes/ieee-802-11ah-wikipedia.md) — Wi‑Fi HaLow standard overview tables.
- [Long-range internet over LoRa (Pi forums)](source-notes/long-range-internet-lora-raspberry-pi-forums.md) — Forum realism on LoRa throughput for “web” use.
- [LoRa Wikipedia excerpt](source-notes/lora-wikipedia.md) — LoRa PHY and LoRaWAN ecosystem overview.
- [Precision agriculture Wikipedia excerpt](source-notes/precision-agriculture-wikipedia.md) — PA definition and methods overview.
- [Wi‑Fi HaLow vs LoRaWAN (RAD)](source-notes/wifi-halow-vs-lorawan-rad.md) — Vendor comparison blog.
- [Wi‑Fi HaLow, LoRa, or NB‑IoT (WizzDev)](source-notes/wi-fi-halow-lora-nb-iot-wizzdev.md) — Three-way technology comparison.
- [Tennessee garden beginners (Willow Ridge)](source-notes/tennessee-garden-beginners-willow-ridge.md) — East TN seasonal planting guide.
- [AI animal husbandry (Ambiq)](source-notes/ai-animal-husbandry-ambiq.md) — Marketing survey of AI in livestock sectors.
- [AI-native operating model (Futurice)](source-notes/ai-native-operating-model-futurice.md) — Culture, value streams, product ops beyond Agile.
- [Dual operating system — Kotter excerpt](source-notes/dual-operating-system-kotter-excerpt.md) — Hierarchy vs network; strategic agility excerpt.
- [Farmers.gov — small-scale forage–animal balance (PDF, 2022)](source-notes/farmersgov-small-scale-forage-balance-factsheet-2022-pdf.md) — Pasture supply vs demand; NRCS grazing math.
- [Guide to livestock forage feeding — Grit](source-notes/guide-livestock-forage-feeding-grit.md) — Hay quality, grains vs forage primer.
- [PostGIS — complete workflow](source-notes/postgis-complete-workflow.md) — Spatial DB modeling; app-oriented GIS pipeline.
- [Geospatial PostgreSQL enterprise — PostGIS deep dive (Perry Robinson)](source-notes/geospatial-postgresql-enterprise-postgis-perry-robinson.md) — Enterprise PostGIS setup, fleet-style scenarios, tiles.
- [GiST spatial index in PostGIS (Medium)](source-notes/postgis-gist-spatial-index-medium.md) — Bounding boxes, spatial index pruning explainer.
- [MDPI Agriculture 2023 — soil ML smart farming (PDF)](source-notes/mdpi-agriculture-13091777-soil-ml-smart-farming-pdf.md) — Data-driven soil analysis; open-access article PDF + extract.
- [PostGIS Day 2019 — PostGIS 3.0 slides (PDF)](source-notes/postgis-day-2019-postgis-3-pdf.md) — Paul Ramsey deep dive deck; complements PostGIS docs.
- [PostgreSQL internals — query flow (Medium, part 1)](source-notes/postgresql-deep-dive-query-flow-medium-part-1.md) — DBMS layers; path of queries through PostgreSQL.
- [PostgreSQL — system design interviews (Algomaster)](source-notes/postgresql-system-design-interviews-algomaster.md) — Interview-oriented PostgreSQL architecture and patterns capture.
- [Precision agriculture — soil mapping (MSU)](source-notes/precision-agriculture-soil-mapping-msu.md) — Web Soil Survey, SSURGO, management zones.
- [Precision Agriculture journal — mobile sensors and yield maps (Springer PDF)](source-notes/precision-agriculture-s11119-025-10274-w-pdf.md) — 2025; HERMES crop model case study.
- [Remote sensing for crop mapping — RSE review](source-notes/remote-sensing-crop-mapping-rse-review.md) — Crop land-cover products; large academic review capture.
- [Soil and crop sensing — CropWatch (UNL)](source-notes/soil-crop-sensing-cropwatch-unl.md) — On-the-go sensors; map-based prescriptions.
- [Soil sensors — remote and ground-based mapping (ASA/CSSA P1792 PDF)](source-notes/asa-publication-p1792-remote-ground-sensors-soil-pdf.md) — Review; imagery vs on-the-go sensing.
- [UT forage menu — Beef & Forage Center](source-notes/ut-forage-menu-beef-forage-center.md) — Extension forage planning; diversification.
- [USDA — forage yield assessment (P2458 PDF)](source-notes/usda-p2458-forage-yield-assessment-pdf.md) — Pasture yield methods; clipping vs plate meter.
- [Animals journal PDF (animals-14-01645)](source-notes/animals-journal-14-01645-pdf.md) — Peer-reviewed PDF import; confirm metadata in file.
- [Cheap Yellow Display ESPHome beginners](source-notes/esphome-yellow-display-beginners.md) — ESP32-2432S028 + Home Assistant YAML.
- [DIY PTP grandmaster Pi (Geerling)](source-notes/diy-ptp-grandmaster-pi-geerling.md) — Time Pi / TimeHAT stratum-1 NTP+PTP build.
- [ESP32 deep dive Medium](source-notes/esp32-series-deep-dive-medium.md) — ESP8266/32 family overview (may be paywalled).
- [ESP32 for IoT Nabto guide](source-notes/esp32-for-iot-nabto-guide.md) — Long vendor feature overview.
- [IJRAW journal PDF (ijraw-4-5-50.1)](source-notes/ijraw-journal-pdf-4-5-50-1.md) — Large PDF import; confirm title inside document.
- [Lily OSP smart farming ESP32 README](source-notes/lily-osp-smart-farming-esp32-readme.md) — Irrigation automation project documentation.
- [NTP Wikipedia excerpt](source-notes/network-time-protocol-wikipedia.md) — Network Time Protocol baseline article.
- [PTP explained NetworkLessons](source-notes/precision-time-protocol-explained-networklessons.md) — IEEE 1588 tutorial and profiles.
- [PTP Wikipedia excerpt](source-notes/precision-time-protocol-wikipedia.md) — Precision Time Protocol baseline article.
- [Pi 5 Ethernet PTP timestamping forums](source-notes/raspberry-pi-5-ptp-timestamping-forums.md) — Community discussion of HW PTP support.
- [Raising backyard chickens (Wine & Country Life)](source-notes/raising-backyard-chickens.md) — Starting an egg flock (regional article).
- [Raising cattle beginning farmers (Hobby Farms)](source-notes/raising-cattle-beginning-farmers-guide.md) — Fencing and small-scale beef framing.
- [Raising chickens for meat](source-notes/raising-chickens-for-meat.md) — Broiler quick-facts and grow-out basics.
- [Ducks for meat (Reddit r/homestead)](source-notes/ducks-for-meat-reddit-homestead.md) — Pekin vs Cornish anecdote; water, plucking, weights.
- [Raising ducks for meat (Bramblewood Hill)](source-notes/raising-ducks-for-meat-bramblewood-hill.md) — Breeds, butcher timing, fat/dark meat.
- [How to butcher a chicken (Abundant Permaculture)](source-notes/how-to-butcher-a-chicken-abundant-permaculture.md) — Home processing walkthrough; tools/skills.
- [Butchering chickens first time — mental (Permies)](source-notes/butchering-chickens-first-time-mental-permies.md) — Forum on psychological barriers to slaughter.
- [How to butcher a chicken (Prairie Homestead)](source-notes/how-to-butcher-chicken-prairie-homestead.md) — Import capture parallel to other butchering guides.
- [Chicken tractor plans (Permies forum)](source-notes/chicken-tractor-plans-permies-forum.md) — Pasture tractor discussion.
- [Deep litter, chicken tractor, pasture systems](source-notes/deep-litter-chicken-tractor-pasture-systems.md) — Housing/pasture patterns for meat birds.
- [Sustainable egg & meat flock (forum)](source-notes/sustainable-egg-meat-flock.md) — Dual-purpose flock planning thread.
- [ESP32 deep dive request (ESP32.com)](source-notes/tutorial-deep-dive-esp32-forum.md) — Forum ask for advanced Espressif training.
- [Homestead chickens eggs or meat](source-notes/what-to-know-raising-homestead-chickens.md) — Layers vs broilers vs dual-purpose.
- [BPS GPS alternative (Geerling)](source-notes/bps-gps-alternative-geerling.md) — ATSC 3.0 broadcast timing vs GPS PPS demo notes.
- [E Ink world technology and uses](source-notes/e-ink-world-technology-and-uses.md) — E-paper tech and applications survey.
- [geerlingguy/time-pi Ansible configuration](source-notes/geerlingguy-time-pi-ansible-configuration.md) — Stratum-1 Pi NTP/PTP repo README.
- [GNSS HAT setting time (Pi forums)](source-notes/gnss-hat-setting-time-raspberry-pi-forums.md) — Receiver HAT time discipline thread.
- [GPS clock display Engineering Radio](source-notes/gps-controlled-clock-raspberry-pi-engineering-radio.md) — NTP Pi + HDMI/LAN clock adjunct.
- [How to build a smart Magic Mirror](source-notes/how-to-build-smart-magic-mirror.md) — Hardware build guide.
- [Trackers without GPS](source-notes/how-to-design-trackers-without-gps.md) — Resilient positioning design article.
- [LORAN definition (TME)](source-notes/loran-definition-tme.md) — Long-range navigation / eLORAN overview.
- [Magic Mirror Buddy](source-notes/magic-mirror-buddy.md) — Project article capture.
- [Magic Mirror reTerminal DM gestures](source-notes/magic-mirror-reterminal-dm-gestures.md) — Gesture + embedded display write-up.
- [MagicMirror² platform README](source-notes/magicmirror2-open-source-smart-mirror-platform.md) — Upstream project excerpt.
- [NTP and GPS timing Raspberry Shake](source-notes/ntp-and-gps-timing-raspberry-shake.md) — Seismic logger UTC/NTP operational notes.
- [Timeserver with GNSS (Pi forums)](source-notes/timeserver-with-gnss-receiver-raspberry-pi-forums.md) — Stratum-1 Pi discussion.
- [USFS — traveled way surface shape, 1997 (PDF)](source-notes/usfs-traveled-way-surface-shape-1997-pdf.md) — Low-volume road cross-section geometry.
- [360 publication PDF](source-notes/360-publication-pdf.md) — Large PDF import; confirm title inside file.
- [Deep dive natural building Natalie Bogwalker](source-notes/deep-dive-natural-building-natalie-bogwalker-podcast.md) — Podcast page on slip straw / hempcrete.
- [Deep dive tiny houses Medium](source-notes/deep-dive-tiny-houses-medium-casimir-curney.md) — Essay excerpt; Medium paywall.
- [Farmers agritourism tiny homes turtle bypass ABC](source-notes/farmers-agritourism-tiny-homes-turtle-bypass-abc.md) — Australia news excerpt.
- [Maximizing farm income agritourism](source-notes/maximizing-farm-income-agritourism.md) — Agritourism revenue ideas list.
- [NIST Internet Time Service servers](source-notes/nist-internet-time-service-servers.md) — ITS hostname/IP snapshot and usage notes.

## Analyses

**Themed entry point** (not a full catalog): [`Wiki navigation and structural hubs`](topics/wiki-navigation-and-structural-hubs.md).

- [Repository analysis](analyses/repository-analysis.md) — Structure, validation, publishing, and content profile of **smart-farm-wiki**.
- [Domain content overview](analyses/domain-content-overview.md) — **Steering doc**: strands, maturity matrix, gaps, supported vs unsupported decisions, backlog; target future-state.
- [Structural debt audit — wiki IA and operational maturity](analyses/structural-debt-audit-wiki-ia-and-operational-maturity.md) — Sprawl diagnosis, `page_subtype` / `operational_maturity` policy, navigation mitigations; complements structural audits.
- [Execution readiness gap audit — East Tennessee operational knowledge](analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md) — **Execution hardening**: missing site-evidence, weak entities, mixed-authority clusters, canonical routing recommendations.
- [Ingest visibility gap — authoritative evidence vs published wiki (East Tennessee)](analyses/ingest-visibility-gap-authoritative-evidence-east-tennessee.md) — **IA / ingest workflow**: why authoritative `raw/` + source-notes felt quiet in the published wiki; routing fixes.
- [Source gap audit — backup/DR vs sub-GHz Wi‑Fi (homelab + farm)](analyses/source-gap-audit-backup-dr-and-subghz-wifi-2026-04-18.md) — Evidence map for farmOS/homelab backup vs HaLow how-to; remaining gaps called out.
- [Backup and disaster recovery package — smart farm stack](analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) — **DR spine**: farmOS/PostgreSQL, k3s/etcd, Longhorn, Rancher, secrets, edge scope; backup vs sync; restore-tested emphasis.
- [Central vs local backup scope — farm edge stack](analyses/central-vs-local-backup-scope-farm-edge-stack.md) — What lands in central stores vs local queue; two-site notes.
- [Runbook — backup validation and recovery drill](analyses/runbook-backup-validation-and-recovery-drill.md) — restic check, DB restore, Longhorn/k3s/Rancher drills; prove restores.
- [Backup strategy comparison — farmOS, homelab, PostgreSQL, containers](analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md) — Granularity, restore complexity, encryption, infra assumptions; restic + Longhorn + compose patterns; backup vs sync.
- [Restore and recovery tiers — homelab farm systems](analyses/restore-recovery-tiers-homelab-farm-systems.md) — Tier 0–3 labels (no fabricated RTO/RPO); drill checklist.
- [Sub-GHz Wi‑Fi (HaLow) — farm sensors and IP backhaul (how-to outline)](analyses/subghz-wi-fi-halow-farm-sensors-deployment-guide.md) — Operator checklist; cites HaLow PoC capture + segmentation/power links.
- [Off-grid implications — backup and networking choices](analyses/off-grid-implications-backup-and-networking-choices.md) — Solar/battery vs backup jobs; WAN vs local queue.
- [Homelab / edge Kubernetes platform strategy — Pi fleet, k3s, Longhorn, Rancher](analyses/homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md) — Canonical stack narrative; farmOS/telemetry tie-in; anti-maximalism.
- [How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet](analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) — **Operator runbook hub**: mandatory vs optional HA, P0/P1 vs later, links to all sequence pages below.
- [Raspberry Pi k3s fleet — prerequisites and assumptions](analyses/raspberry-pi-k3s-fleet-prerequisites-and-assumptions.md) — OS, skills, fleet size, phase scope.
- [Raspberry Pi k3s fleet — hardware BOM and node roles](analyses/raspberry-pi-k3s-fleet-hardware-bom-and-node-roles.md) — Server/agent roles, disks, anti-patterns on Pi.
- [Raspberry Pi k3s fleet — network and power prerequisites](analyses/raspberry-pi-k3s-fleet-network-and-power-prerequisites.md) — LAN, firewall, time, UPS / off-grid coupling.
- [Raspberry Pi k3s fleet — central and HA storage options](analyses/raspberry-pi-k3s-fleet-central-and-ha-storage-options.md) — Longhorn vs NAS vs hybrid; etcd HA pointer.
- [Raspberry Pi k3s fleet — bootstrap sequence](analyses/raspberry-pi-k3s-fleet-bootstrap-sequence.md) — k3s server + agents + kubeconfig hygiene.
- [Raspberry Pi k3s fleet — Longhorn storage configuration sequence](analyses/raspberry-pi-k3s-fleet-longhorn-storage-configuration-sequence.md) — iSCSI, install, StorageClass, Pi limits.
- [Raspberry Pi k3s fleet — Rancher installation sequence](analyses/raspberry-pi-k3s-fleet-rancher-installation-sequence.md) — Defer P0; Helm when ingress/TLS ready.
- [Raspberry Pi k3s fleet — backup and restore sequence](analyses/raspberry-pi-k3s-fleet-backup-and-restore-sequence.md) — App dumps + Longhorn + etcd tracks.
- [Raspberry Pi k3s fleet — validation checklist](analyses/raspberry-pi-k3s-fleet-validation-checklist.md) — Cluster, Longhorn, backup, performance honesty.
- [Raspberry Pi k3s fleet — troubleshooting and degraded modes](analyses/raspberry-pi-k3s-fleet-troubleshooting-and-degraded-modes.md) — Symptom matrix, farm degraded modes, when to simplify.
- [Platform decision memo — phase, HA scope, deferrals (Pi / k3s / Longhorn / Rancher)](analyses/platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md) — Phase 0/1 vs deferred; what “HA” means here; overbuild warnings.
- [Raspberry Pi fleet provisioning standard — smart farm / homelab](analyses/raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md) — Hostnames, iSCSI, roles, pilot vs production bar.
- [Longhorn vs central storage architecture — homelab / farm platform](analyses/longhorn-vs-central-storage-architecture-homelab-farm-platform.md) — PVC replication vs NAS/object; hybrid patterns.
- [Rancher — role and timing (k3s homelab / farm platform)](analyses/rancher-role-and-timing-k3s-homelab-farm-platform.md) — Optional UI/CD; deferral guidance.
- [Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn](analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md) — App dumps + Longhorn + etcd tracks; links to generic backup comparison.
- [Claxton and Demory — missing data register](analyses/claxton-and-demory-missing-data-register.md) — **Parcel-level** unknowns vs desktop vs on-site; ties to **validation** tasks.
- [Claxton home base — site intelligence (Anderson County, Tennessee)](analyses/claxton-home-base-site-intelligence.md) — `SITE_HOME` anchor (NASS county rent + planning assumptions).
- [Demory farm — site intelligence (Campbell County, Tennessee)](analyses/demory-farm-site-intelligence.md) — `SITE_FARM` anchor (NASS + Campbell WSS AOI soils capture).
- [Parcel intelligence — Claxton home base (East Tennessee two-site)](analyses/parcel-intelligence-claxton-home-base-east-tennessee-two-site.md) — Parcel worksheet: placeholders; WSS process source-note ingested.
- [Parcel intelligence — Demory farm site (East Tennessee two-site)](analyses/parcel-intelligence-demory-farm-site-east-tennessee-two-site.md) — Parcel worksheet: WSS soil map table from vault capture (AOI clip pending).
- [Strategic audit — decision-safe operations for a two-site smart farm](analyses/strategic-audit-decision-safe-operations.md) — Gap analysis and backlog: what to add before the wiki is an operational brain (5 ac + 120 ac + telemetry).
- [Implementation backlog — strategic audit (P0–P3)](analyses/implementation-backlog-strategic-audit.md) — Prioritized build list: templates, topics, SOPs, analyses; top 10 pages first.
- [Information architecture — decision-safe operational brain (target design)](analyses/information-architecture-decision-safe-operations.md) — Target IA: hub layers, required pages, cross-links, orphan/integration gaps, migration phases.
- [Business viability and farm economics — gap analysis (strategic audit)](analyses/business-viability-and-farm-economics-gap-analysis.md) — Revenue, enterprise, channels, staffing, insurance, books, CAPEX/OPEX, logistics, risk; prioritized page list; decisions not yet supportable from the vault alone.
- [Smart technology architecture audit (strategic audit)](analyses/smart-technology-architecture-audit.md) — Field stack, identity, alerting, security, fragmentation; reference page outline; required SOPs and diagrams.
- [Agentic wiki improvement prompts (staged, strategic audit)](analyses/agentic-wiki-improvement-prompts-strategic-audit.md) — Pre-prompt + Phase 1–4 copy-paste prompts: deliverables, acceptance criteria, files to create/update.
- [Dual-site operations model — non-agritourism farm business](analyses/dual-site-operations-model-non-agritourism.md) — Production-led two-site logistics; batching, equipment home, coverage; connects strands.
- [Field telemetry reference architecture — homestead + 120-acre farm](analyses/field-telemetry-reference-architecture-homestead-120ac.md) — Logical stack, SPOFs, HA/farmOS/MQTT/TSDB roles; foundation for runbooks.
- [Connectivity strategy — Claxton home base and Demory farm site](analyses/connectivity-strategy-for-claxton-and-demory.md) — **Canonical** Internet posture for **two named sites** (WAN roles, LTE fallback, local vs cloud, pilot vs scale); complements topology diagram.
- [Execution topology package — two-site smart farm (Mermaid)](analyses/execution-topology-package-two-site-smart-farm.md) — **Ops-first** **three** diagrams: full reference, **Phase 0/1** pilot, **WAN-out** degraded; trust zones + runbook links.
- [Off-grid power strategy — Demory farm site (Campbell County)](analyses/off-grid-power-strategy-demory-farm-site.md) — **Solar+battery** **default** **;** **continuous** **vs** **duty-cycled** **loads** **;** **networking** **as** **electrical** **load** **.**
- [Mesh and field networking strategy — off-grid Demory farm](analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md) — **Mesh-first** **;** **Meshtastic** **/** **HaLow** **/** **Wi‑Fi** **roles** **;** **WAN** **secondary** **.**
- [Off-grid farm execution topology — Demory (Mermaid)](analyses/off-grid-farm-execution-topology-demory-mermaid.md) — **Reference** **/** **pilot** **/** **degraded** **;** **Pcrit** **/** **Popt** **power** **domains** **.**
- [Off-grid degraded modes — power and connectivity (Demory)](analyses/off-grid-degraded-modes-power-and-connectivity-demory-farm.md) — **SOC** **+** **WAN** **failure** **classes** **.**
- [Off-grid operational decision rules — power and networking (Demory)](analyses/off-grid-operational-decision-rules-power-and-networking-demory-farm.md) — **DR-*** gates; stacks with **CS-5** / **MV-8** on execution pages.
- [Two-site smart farm — network topology and WAN/edge reference (Mermaid)](analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md) — **Mermaid**: WAN, two sites, telemetry plane, DC context, HaLow vs mesh overlay. **Start with** [`Execution topology package`](analyses/execution-topology-package-two-site-smart-farm.md) for **trust/WAN/local** clarity. **Canonical integration** (Starlink/WAN **roles** per site): [`Connectivity strategy — Claxton & Demory`](analyses/connectivity-strategy-for-claxton-and-demory.md), [`Two-site operations model — 5 ac / 120 ac`](analyses/two-site-operations-model-5ac-homebase-120ac-production.md) § Starlink, [`Smart technology and telemetry strategy`](analyses/east-tennessee-two-site-farm-business-plan-smart-tech-strategy.md) § Starlink, [`Reference architecture`](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md), [`Remote access / operational security`](analyses/remote-access-operational-security-model-two-site-smart-farm.md), [`Manual fallback / degraded modes`](analyses/manual-fallback-degraded-modes-critical-operations.md), [`Validation plan — 24 mo`](analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md), [`Capital plan`](analyses/east-tennessee-two-site-farm-business-plan-capital-and-financing.md).
- [Reference architecture — 5-acre home base + 120-acre farm](analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md) — **Smart-farm architecture package** hub: control center vs production, scenario design, links to SoR/security/instrumentation/degraded modes.
- [Telemetry system of record — boundaries and authority](analyses/telemetry-system-of-record-boundaries-and-authority.md) — Records vs telemetry vs dashboards vs alerts vs manual verification.
- [Automation principles — two-site smart farm](analyses/automation-principles-two-site-smart-farm.md) — Automate early / late / never; distance and maintenance burden.
- [Remote access and operational security model — two-site smart farm](analyses/remote-access-operational-security-model-two-site-smart-farm.md) — **Canonical** admin paths, Z1–Z3a, Starlink as transport; **MV**/**CS** hooks; links segmentation policy.
- [Network segmentation, site-to-site connectivity, and internet exposure — two-site smart farm](analyses/network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md) — **Policy**: device classes, VPN/overlay, **may** vs **never** Internet-exposed; Starlink home vs farm implications; runbooks + validation.
- [Farm spatial model and asset registry standard](analyses/farm-spatial-model-and-asset-registry-standard.md) — Paddock/asset/device IDs; map authority; farmOS-aligned naming.
- [Weekly coverage matrix — two-site farm operations](analyses/weekly-coverage-matrix-two-site-farm-operations.md) — Fillable grid; Tier A/B/C checks.
- [Automation degraded modes and manual fallback SOP](analyses/automation-degraded-modes-manual-fallback-sop.md) — Failure classes, manual safe states, per-system placeholders.
- [Runbook — broker or backhaul down](analyses/runbook-broker-or-backhaul-down.md) — MQTT/uplink failure; verify physical; parent architecture required.
- [Runbook — power loss at remote site](analyses/runbook-power-loss-remote-site.md) — Field hub power loss; safe order of recovery.
- [Runbook — sensor false positive and alert triage](analyses/runbook-sensor-false-positive-alert-triage.md) — Corroborate before mute; observability discipline.
- [Runbook — manual fallback for irrigation, gates, and pumps](analyses/runbook-manual-fallback-irrigation-gates-pumps.md) — Water movement manual safe states; specialization of degraded SOP.
- [3D printing in a workshop — summary](analyses/3d-printing-in-a-workshop-summary.md) — FDM/shop uses, jigs, forum culture; ingested batch.
- [Basement workshop design — summary](analyses/basement-workshop-design-summary.md) — Layout, ingress, noise/dust, basement remodel sources.
- [Off-grid setups for the smart home — summary](analyses/off-grid-smart-home-setups-summary.md) — Energy + Home Assistant / SOC automations; ingested guides and forum.
- [Dirt road erosion — shade, hill, and curve (planning synthesis)](analyses/dirt-road-erosion-shade-hill-curve.md) — Stacked failure modes; drainage-first actions; handbook PDF + thread refs.
- [Steep curved hill dirt road — erosion prevention (120-acre farm)](analyses/steep-curved-hill-dirt-road-erosion-prevention-120-acres.md) — Drainage-first prevention, traffic/sediment context, checklist.
- [Timing on the farm — synthesis](analyses/timing-on-the-farm-synthesis.md) — Seasonal, rotation, labor, water/energy, and clock sync (NTP/PTP) as layers of “time.”
- [Time and smart sensors — 120-acre field to 5-acre homestead](analyses/time-smart-sensors-120ac-to-5ac-homestead.md) — Two-site synthesis: commute vs E2E latency, clock correlation, staleness, sampling vs control-loop time.
- [Smart mirror with ESP32 and Raspberry Pi — build analysis](analyses/smart-mirror-esp32-and-raspberry-pi-build.md) — Pi runs MagicMirror²; ESP32 for sensors/side HMI; parts sourcing and web references.
- [Long 360 tractor — no-start troubleshooting (synthesis)](analyses/long-360-tractor-no-start-synthesis.md) — Diesel electrical vs fuel vs preheat; forum + web references (not a service manual).
- [Why a synthesis layer](analyses/why-synthesis-layer.md) — Short analysis tying concepts to practice.
- [Concept relationships — summary objects](analyses/concept-relationships-overview.md) — Related concepts: narrative clusters, table, YAML graph.
- [Tracking chickens — motion sensors over LoRa and MQTT](analyses/tracking-chickens-motion-lora-mqtt.md) — Query synthesis: coop/run architecture, MQTT paths, limits vs per-bird tracking.
- [Agritourism, tiny houses, Tennessee hobby farms](analyses/agritourism-tiny-houses-tennessee-hobby-farm.md) — Query synthesis: diversification, TN business context, zoning caveat.
- [Agritourism smart hobby farm — tiny houses and guest work stays](analyses/agritourism-smart-hobby-farm-tiny-houses-guest-work-stays.md) — Query synthesis: lodging + farm work, smart-farm links, risk framing.
- [Starting and stocking a pond — beautiful water feature](analyses/starting-stocking-pond-beautiful-water-feature.md) — Query synthesis: build, stock legally, aesthetics, irrigation adjacency.
- [Farm stocking — 120 acres vs 5 acres (research prompt)](analyses/farm-stocking-120-acres-vs-5-acres-research-prompt.md) — Query brief: research prompt and methods for chickens, crops, animals; automation bias on larger holding.
- [Homestead composting — practical guide](analyses/homestead-composting-guide.md) — Greens/browns, hot vs cold, systems, hygiene; ingested compost batch.
- [East Tennessee — profitable crops matrix](analyses/east-tennessee-profitable-crops-matrix.md) — Query synthesis: commodity vs specialty profit signals, UT enterprise budgets, CPA specialty crops, NASS context.
- [Multi-field crop rotation plan (template)](analyses/multi-field-crop-rotation-plan.md) — Field roles, family-based rotations, coordinated A–D year tables, perennial block notes.
- [Agritourism business plan — guest hub on 120 acres, family home 35 min away](analyses/agritourism-dual-site-business-plan-five-and-120-acres.md) — Working farm + lodging on 120 ac; private 5 ac residence; coverage and animal placement.

## Comparisons

- [Raw vs wiki](comparisons/raw-vs-wiki.md) — Side-by-side responsibilities and failure modes.
- [LoRaWAN vs Meshtastic for fixed farm telemetry](comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md) — Star/gateway vs mesh; ops and SPOF tradeoffs.
- [Meshtastic vs Wi‑Fi HaLow vs conventional Wi‑Fi — off-grid farm operations](comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md) — **Demory** off-grid-first; observational vs throughput; local vs WAN.
- [Wi‑Fi HaLow vs LoRaWAN vs Meshtastic vs conventional Wi‑Fi — farm field networking](comparisons/wi-fi-halow-lorawan-meshtastic-conventional-wi-fi-farm-field-networking.md) — Four-way throughput/range/power/IP/mesh/backhaul matrix; field layer focus.
- [farmOS vs lightweight record stack for a two-site farm](comparisons/farmos-vs-lightweight-stack-two-site-farm.md) — Ops weight vs glue code; team-size framing.
- [Own equipment vs custom hire under two-site logistics](comparisons/own-equipment-vs-custom-hire-two-site-logistics.md) — Hauling time vs duplicate tools vs contractor scheduling.
- [Fixed gateway tower vs mobile or vehicle gateway](comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md) — Always-on RF vs intermittent mobile backhaul.
- [Anderson County vs Campbell County — two-site operating implications](comparisons/anderson-county-vs-campbell-county-operating-implications.md) — County NASS rents, home-base vs farm roles, over-generalization risks (Claxton / Demory anchors).
- [Ducks vs chickens — meat raising](comparisons/ducks-vs-chickens-meat-raising.md) — Housing, water, processing, grow-out (ingested sources + vault poultry notes).

## Timelines

- [East Tennessee two-site farm business plan — phase timeline](timelines/east-tennessee-two-site-farm-business-plan-phase-timeline.md) — Phases 0–4 bands and milestone anchors (gates in validation pages are authoritative).

## Glossary

- [Smart Farm Wiki glossary (hub)](glossary/smart-farm-wiki-glossary.md) — Index of definition-first entries for recurring operational terms.
- [Evidence grade](glossary/evidence-grade.md) — **Authority vocabulary** for decision-grade vs exploratory support.
- [Synthesis layer](glossary/synthesis-layer.md) — Raw vs wiki durable model (repository pattern).
- [Two-site sites (SITE_HOME / SITE_FARM)](glossary/two-site-sites.md)
- [System of record (farm data)](glossary/system-of-record-farm-data.md)
- [Validation gate](glossary/validation-gate.md)
- [Degraded mode (automation)](glossary/degraded-mode.md)

## Meta

- [Append-only log](log.md) — Chronological record of ingests, queries, and lint passes.
