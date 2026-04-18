---
title: Knowledge synthesis
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - theme
review_status: unreviewed
---

# Knowledge synthesis

This topic spans how conclusions are assembled from sources across the vault.

**Entry points**

- [`LLM Wiki pattern`](../concepts/llm-wiki-pattern.md)
- [`Why a synthesis layer`](../analyses/why-synthesis-layer.md)
- [`Concept relationships — summary objects`](../analyses/concept-relationships-overview.md) — How domain concepts link (table + YAML for agents)
- [`Domain content overview`](../analyses/domain-content-overview.md) — Map of subject-matter strands (land, networks, power, data, business, time/PNT)
- [`Two-site smart farm operations`](two-site-smart-farm-operations.md) — **Topic hub** (navigation): business plan package, artifacts, runbooks, comparisons
- [`East Tennessee two-site farm business plan — planning framework`](../analyses/east-tennessee-two-site-farm-business-plan-framework.md) — Decision-grade **business plan** (5 ac base + 120 ac ET; Phases **0–4**; [`executive summary`](../analyses/east-tennessee-two-site-farm-business-plan-executive-summary.md)); **operational artifacts**: [`two-site ops 5/120`](../analyses/two-site-operations-model-5ac-homebase-120ac-production.md), [`instrumentation priority`](../analyses/instrumentation-priority-matrix-two-site-smart-farm.md), [`validation before major spend`](../analyses/validation-backlog-before-major-spend-two-site-smart-farm.md); **skeptical critique**: [`hostile internal review`](../analyses/east-tennessee-two-site-farm-business-plan-hostile-internal-review.md); **remediation / decision controls**: [`business plan remediation backlog`](../analyses/east-tennessee-two-site-farm-business-plan-remediation-backlog.md); **targeted ingest**: [`business plan source-ingest campaign`](../analyses/business-plan-source-ingest-campaign-east-tennessee-two-site.md)
- [`Information architecture — decision-safe operational brain (target design)`](../analyses/information-architecture-decision-safe-operations.md) — Target **wiki IA**: operations spine, telemetry/spatial hubs, SOPs/templates, cross-link rules, migration plan
- [`Strategic audit — decision-safe operations for a two-site smart farm`](../analyses/strategic-audit-decision-safe-operations.md) — Backlog of gaps and artifacts for **decision-safe** split-site farm ops
- [`Business viability and farm economics — gap analysis (strategic audit)`](../analyses/business-viability-and-farm-economics-gap-analysis.md) — **Economics & business** gaps only: revenue, enterprise, channels, staffing, insurance, accounting, CAPEX/OPEX, logistics, risk
- [`Smart technology architecture audit (strategic audit)`](../analyses/smart-technology-architecture-audit.md) — **Smart stack**: telemetry, radios, edge, HA/farmOS/MQTT/TSDB, time, registry, alerting, observability, firmware, degraded modes, cybersecurity
- [`Smart Farm Wiki — repository implementation plan (business plan integration)`](../analyses/smart-farm-wiki-repository-implementation-plan.md) — **Meta**: how to wire the ET two-site plan into topic hubs, overview, and backlog (**agent-executable**)
- [`Agentic wiki improvement prompts (staged, strategic audit)`](../analyses/agentic-wiki-improvement-prompts-strategic-audit.md) — **Pre-prompt** + phased **agent prompts** to build the wiki in order (P0→P3 alignment)
- [`Implementation backlog — strategic audit (P0–P3)`](../analyses/implementation-backlog-strategic-audit.md) — **Prioritized** implementation list (dependencies, effort, top 10 first pages)
- **Foundation analyses (two-site spine)**: [`Dual-site operations model — non-agritourism`](../analyses/dual-site-operations-model-non-agritourism.md), [`Field telemetry reference architecture — homestead + 120-acre farm`](../analyses/field-telemetry-reference-architecture-homestead-120ac.md), [`Farm spatial model and asset registry standard`](../analyses/farm-spatial-model-and-asset-registry-standard.md), [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](../analyses/capex-opex-enterprise-sequencing-two-site-constraint.md), [`Weekly coverage matrix — two-site`](../analyses/weekly-coverage-matrix-two-site-farm-operations.md), [`Automation degraded modes SOP`](../analyses/automation-degraded-modes-manual-fallback-sop.md)
- **Runbooks (after architecture)**: [`Broker or backhaul down`](../analyses/runbook-broker-or-backhaul-down.md), [`Power loss at remote site`](../analyses/runbook-power-loss-remote-site.md), [`Sensor false positive / alert triage`](../analyses/runbook-sensor-false-positive-alert-triage.md), [`Manual fallback — irrigation, gates, pumps`](../analyses/runbook-manual-fallback-irrigation-gates-pumps.md)
- [`Timing on the farm — synthesis`](../analyses/timing-on-the-farm-synthesis.md) — Seasonal, labor, water/energy, and clock-sync layers of “time”

**Domain entry points**

- [`Smart agriculture, Meshtastic, and LoRaWAN`](smart-agriculture-meshtastic-and-lorawan.md)
- [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](field-network-iot-comparisons.md)
- [`Off-grid solar power and storage (special topic)`](off-grid-solar-power-and-storage.md)
- [`Smart home — Matter, Thread, and Home Assistant AI (special topic)`](smart-home-matter-thread-and-home-assistant-ai.md)
- [`Time synchronization — NTP and PTP sources`](time-synchronization-ntp-and-ptp.md)
- [`Position, navigation, and timing alternatives`](position-navigation-and-timing-alternatives.md)
- [`ESP32, ESPHome, and smart-farming builds`](esp32-iot-smart-farming-and-tooling.md)
- [`Homestead and regional gardening sources`](homestead-and-regional-gardening-sources.md) and [`Backyard livestock and homestead animal sources`](backyard-livestock-and-homestead-animals.md) — see [`Ducks vs chickens — meat raising`](../comparisons/ducks-vs-chickens-meat-raising.md)
- [`Smart mirror and e-paper display builds`](smart-mirror-and-e-paper-displays.md)
- [`Agritourism, tiny housing, and natural building sources`](agritourism-tiny-housing-and-natural-building.md) — see also [`Agritourism smart hobby farm — tiny-house rentals and guest farm work (query synthesis)`](../analyses/agritourism-smart-hobby-farm-tiny-houses-guest-work-stays.md)
- [`Farm data, farmOS, and agriculture lab builds`](farm-data-farmos-and-ag-lab-builds.md)
- [`Data storage (farm and edge stacks)`](../concepts/data-storage.md) — MQTT and PostgreSQL/PostGIS documentation entry points
- [`Homelab, self-hosting, and edge narratives`](homelab-self-hosting-and-edge-narratives.md)
- [`Home workshop, 3D printing, basement, off-grid smart home sources`](home-workshop-3d-printing-basement-offgrid-smart-home-sources.md) — maker space + off-grid HA ingests ([`3D printing in a workshop — summary`](../analyses/3d-printing-in-a-workshop-summary.md), [`basement workshop design`](../analyses/basement-workshop-design-summary.md), [`off-grid smart home setups`](../analyses/off-grid-smart-home-setups-summary.md))
- [`Docker, Kubernetes, Compose, and Bake (edge and homelab)`](docker-kubernetes-compose-and-bake.md)
- [`LoRa, MQTT, and gateway bridges`](lora-mqtt-and-gateway-bridges.md)
- [`Tennessee hobby farm and small-farm business sources`](tennessee-hobby-farm-and-small-farm-business-sources.md)
- [`Ponds, water features, and homestead hydrology`](ponds-water-features-and-homestead-hydrology.md)
- [`Sustainable cropping, soil, and farm entry sources`](sustainable-cropping-soil-and-farm-entry-sources.md) — forage (**UT Beef & Forage**, Grit), **soil mapping** (MSU), **soil sensing** (CropWatch) ingests toward **stocking/forage** backlog items
