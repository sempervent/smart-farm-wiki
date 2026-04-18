---
title: Domain content overview (Smart Farm Wiki)
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-21
review_status: unreviewed
tags:
  - domain
  - meta-synthesis
confidence: medium
---

# Domain content overview (Smart Farm Wiki)

This page is the **steering document** for the vault’s **domain** (not CI or MkDocs mechanics—see [`Repository analysis`](repository-analysis.md)). It keeps the **strand map**, states the **target future**, judges **maturity**, names **gaps**, separates **supportable vs unsupported** decisions, and ends with a **short prioritized backlog**. Agents and humans should read it before large ingests or architecture work.

**Epistemic stance**: Claims about *your* operation require *your* data; the wiki holds **placeholders**, **source-notes**, and **synthesis**. This overview **does not** replace professionals (legal, tax, electrical, vet).

**Canonical ownership & anti-sprawl**: Which **cluster** owns durable meaning (business plan, two-site ops, telemetry/SoR, validation, economics) and how **entities** and **hubs** should route readers—see [`Structural audit — page ownership, entity gaps, and hub routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md). Prefer **extending** a canonical page over a parallel analysis; follow **`AGENTS.md`** (page ownership, canonicalization, entity-first).

---

## Target future-state

The vault should become a **decision-safe operational brain** for a **two-site** pattern (homestead-scale + farm-parcel-scale, separated by meaningful drive time): **land and biology**, **energy and water**, **digital telemetry and records**, **business and risk**—with **explicit** identity (parcel/paddock/device), **reference architecture** for field tech, **runbooks** for failure, and **economics** that justify capital. See [`Strategic audit — decision-safe operations for a two-site smart farm`](strategic-audit-decision-safe-operations.md) and [`Information architecture — decision-safe operational brain (target design)`](information-architecture-decision-safe-operations.md).

**Concrete end-state signals**

- **Foundation pages** (spinal cord) are **active** and cross-linked: dual-site ops model, field telemetry reference architecture, farm spatial + asset registry standard, CAPEX/OPEX sequencing—see [Foundation artifacts](#foundation-artifacts-spinal-cord) below.
- **Comparisons** force **tradeoffs** (radios, records stack, equipment vs hire, gateway topology)—not vendor enthusiasm.
- **Runbooks** assume **architecture first** (broker down, remote power loss, alert triage, manual irrigation/gates)—see [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md) as parent SOP.

---

## North star (three rings)

The corpus mixes **small-scale agriculture and homestead practice** with **instrumentation, networks, and automation**. Mental model:

1. **Land and living systems** — soil, water, crops, livestock, ponds, regional gardening.
2. **Energy and infrastructure** — off-grid solar, storage, pumps and hydrology, **time** as infrastructure.
3. **Digital layer** — LPWAN/mesh, MQTT, MCUs, **farmOS** / records, homelab patterns, **cybersecurity**.

Not every page sits in all three rings; many **source-notes** are single-import anchors pending synthesis.

---

## Strand map (A–G)

### Strand A — Land, water, and biological production

**Themes**: Rotations, cover crops, compost, forage, precision soil sensing, livestock, ponds, irrigation, horses.

**Hubs**: [`Sustainable cropping, soil, and farm entry sources`](../topics/sustainable-cropping-soil-and-farm-entry-sources.md), [`Homestead composting and soil sources`](../topics/homestead-composting-and-soil-sources.md), [`Homestead and regional gardening sources`](../topics/homestead-and-regional-gardening-sources.md), [`Backyard livestock and homestead animal sources`](../topics/backyard-livestock-and-homestead-animals.md), [`Ponds, water features, and homestead hydrology`](../topics/ponds-water-features-and-homestead-hydrology.md).

**Concepts**: [`Precision agriculture`](../concepts/precision-agriculture.md), [`Composting`](../concepts/composting.md).

### Strand B — Regional business, diversification, shelter

**Themes**: TN-leaning business excerpts, agritourism, tiny housing / natural building where it intersects farm stays.

**Hubs**: [`Tennessee hobby farm and small-farm business sources`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md), [`Agritourism, tiny housing, and natural building sources`](../topics/agritourism-tiny-housing-and-natural-building.md).

### Strand C — Field connectivity (LPWAN, mesh, Wi‑Fi HaLow)

**Themes**: LoRa vs LoRaWAN vs Meshtastic; MQTT bridges; solar repeaters; cellular IoT.

**Hubs**: [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md), [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md), [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md).

**Concepts**: [`LoRa (radio)`](../concepts/lora-radio.md), [`LoRaWAN`](../concepts/lorawan.md), [`Meshtastic`](../concepts/meshtastic.md), [`Wi-Fi HaLow`](../concepts/wi-fi-halow.md), [`DePIN`](../concepts/depin.md).

### Strand D — Edge devices and farm-adjacent compute

**Themes**: ESP32, ESPHome, farmOS, ag-lab / homelab, containers.

**Hubs**: [`ESP32, ESPHome, and smart-farming builds`](../topics/esp32-iot-smart-farming-and-tooling.md), [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md), [`Homelab, self-hosting, and edge narratives`](../topics/homelab-self-hosting-and-edge-narratives.md), [`Docker, Kubernetes, Compose, and Bake (edge and homelab)`](../topics/docker-kubernetes-compose-and-bake.md).

**Concepts**: [`ESP32`](../concepts/esp32.md), [`Data storage (farm and edge stacks)`](../concepts/data-storage.md).

### Strand E — Power and site energy

**Hub**: [`Off-grid solar power and storage (special topic)`](../topics/off-grid-solar-power-and-storage.md).

### Strand F — Building automation and consumer IoT

**Hubs**: [`Smart home — Matter, Thread, and Home Assistant AI (special topic)`](../topics/smart-home-matter-thread-and-home-assistant-ai.md), [`Smart mirror and e-paper display builds`](../topics/smart-mirror-and-e-paper-displays.md).

### Strand G — Time, position, resilient references

**Hubs**: [`Time synchronization — NTP and PTP sources`](../topics/time-synchronization-ntp-and-ptp.md), [`Position, navigation, and timing alternatives`](../topics/position-navigation-and-timing-alternatives.md).

**Concepts**: [`NTP`](../concepts/network-time-protocol.md), [`PTP`](../concepts/precision-time-protocol.md). **Synthesis**: [`Timing on the farm — synthesis`](timing-on-the-farm-synthesis.md).

---

## Maturity matrix by strand

| Strand | What the wiki does well | Maturity | What is still thin |
|--------|-------------------------|----------|---------------------|
| **A** | Broad source capture; some **synthesis** (compost, ponds); **forage PDFs** ingested | **Medium** | Carrying capacity **conclusions**; sensor ↔ rotation **loops** per field |
| **B** | TN / hobby-farm **pointers**; agritourism analyses | **Low–Medium** | **Integrated** economics and labor routing |
| **C** | Strong **literacy** and MQTT/LoRa **clusters** | **Medium** | **Chosen** stack per site; **comparison** to decision-grade |
| **D** | farmOS + lab + homelab **threads** | **Medium–Low** | **System of record**; farmOS **model** tied to **map** |
| **E** | Solar / storage narratives | **Medium** | **One** diagram with **field gateway power** |
| **F** | HA / Matter **survey** | **Medium–Low** | HA as **farm alert** consumer + **on-call** |
| **G** | NTP/PTP **primers** | **Medium** | **Subsystem clock requirements** in architecture |

---

## Foundation artifacts (spinal cord)

These **four** analyses connect strands that the map above used to only **gesture** at:

| Page | Role |
|------|------|
| [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md) | Production-led **logistics** vs agritourism bias; batching and equipment **home**. |
| [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md) | **Broker, radios, uplink, HA/farmOS/TSDB** placeholders and SPOFs. |
| [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md) | **IDs** for land, assets, devices; map **authority**. |
| [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md) | **Capital phasing** under distance; ties **enterprise** to **infrastructure**. |

---

## Expanded gaps

- **Vertical slice**: Sensor → **identity** → **storage** → **alert** → **human** → **manual fallback** is **not** fully documented except in patches; [`Smart technology architecture audit`](smart-technology-architecture-audit.md) lists fragmentation.
- **farmOS ↔ telemetry**: Adjacent topics; **event → asset → geometry** pattern still **implicit** (see farmOS **Assets/Logs** source-notes under [`source-notes/farmos-model-assets-documentation.md`](../source-notes/farmos-model-assets-documentation.md)).
- **Business ↔ tech**: [`Business viability and farm economics — gap analysis`](business-viability-and-farm-economics-gap-analysis.md) — ROI and **instrumentation priority** still **methodology**-level.
- **Security**: OT / remote-access **ingests** landed (CISA PDFs/excerpts); **farm cybersecurity hub** still to formalize as a **topic** page.
- **NRCS**: Large **FY25 scenarios** PDF is **planning context**, not a substitute for site engineering—see [`source-notes/nrcs-fy25-conservation-scenarios-pdf.md`](../source-notes/nrcs-fy25-conservation-scenarios-pdf.md).

---

## Supported vs unsupported decisions (from this repository alone)

### Generally **supported** (with sources + synthesis)

| Decision type | Why |
|---------------|-----|
| **Radio stack literacy** (LoRa vs LoRaWAN vs mesh) | Topic hubs + concepts + comparisons |
| **farmOS data model** (assets, logs) | Documentation captures + [`Farm data…`](../topics/farm-data-farmos-and-ag-lab-builds.md) |
| **Enterprise budget orientation** (UT publications, scenarios) | Source-notes + [`East Tennessee — profitable crops matrix`](east-tennessee-profitable-crops-matrix.md) |
| **OT security framing** (inventory, remote access mitigations) | CISA ingests + [`cisa-primary-mitigations-ot-cyber-threats-excerpt`](../source-notes/cisa-primary-mitigations-ot-cyber-threats-excerpt.md) |
| **Degraded automation** (manual safe states) | [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md) + runbooks below |

### **Unsupported** or **high risk** without external data / professionals

| Decision type | Why |
|---------------|-----|
| **Exact enterprise profitability** | Needs **your** yields, prices, costs |
| **Insurance / entity / liability** | Questions only—see future insurance checklist |
| **Whether to deploy LoRaWAN vs Meshtastic** on **your** terrain | Site survey + comparison page is input, not answer |
| **Legal market channels** (meat, on-farm sales) | Counsel + current **TN** rules |
| **“Hands-off” remote farm** via automation alone | Conflicts with welfare and **coverage** reality |

---

## Runbooks (after architecture)

Written to depend on **foundation** pages and **reference architecture**, not to replace them:

- [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md)
- [`Runbook — power loss at remote site`](runbook-power-loss-remote-site.md)
- [`Runbook — sensor false positive and alert triage`](runbook-sensor-false-positive-alert-triage.md)
- [`Runbook — manual fallback for irrigation, gates, and pumps`](runbook-manual-fallback-irrigation-gates-pumps.md)

Parent: [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md).

---

## Comparisons (tradeoffs)

- [`LoRaWAN vs Meshtastic for fixed farm telemetry`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md)
- [`farmOS vs lightweight record stack for a two-site farm`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md)
- [`Own equipment vs custom hire under two-site logistics`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md)
- [`Fixed gateway tower vs mobile or vehicle gateway`](../comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md)

---

## Prioritized backlog (short)

1. **Telemetry system of record** — extend [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md) with **conflict playbooks** (farmOS vs HA vs TSDB) as operators deploy; backlog P0 #6 tracked in [`Implementation backlog`](implementation-backlog-strategic-audit.md).  
2. **Parcel/paddock naming** + **asset registry minimum fields** as first-class templates (if not yet split from spatial standard).  
3. **Two-site operations topic hub** — [`topics/two-site-smart-farm-operations`](../topics/two-site-smart-farm-operations.md) is live; **ongoing**: keep tables **current** when adding sibling pages.  
4. **Farm cybersecurity and remote access** topic hub (CISA ingests → policy).  
5. **Homestead civil systems** topic (command post during crises).  
6. **Stocking and forage — methods** (extension synthesis).  
7. **Insurance checklist** (two parcels).  
8. **Resilience graph** analysis (roads × water × power × comms).  
9. **Instrumentation priority matrix** — [`Instrumentation priority matrix — two-site smart farm`](instrumentation-priority-matrix-two-site-smart-farm.md) exists; **fill** with site evidence over time.  
10. **Named entities** — [`farmOS`](../entities/farmos.md), [`Home Assistant`](../entities/home-assistant.md); **sites & systems** — [`Five-acre home base (SITE_HOME)`](../entities/five-acre-home-base-site-home-et-two-site.md), [`120-acre production farm (SITE_FARM)`](../entities/120-acre-production-farm-site-farm-et-two-site.md), [`Farm parcels and land units`](../entities/farm-parcels-and-land-units.md), [`Farm water infrastructure system`](../entities/farm-water-infrastructure-system.md), [`Farm on-site power system`](../entities/farm-on-site-power-system.md), [`Field telemetry network — two-site`](../entities/field-telemetry-network-two-site.md); **equipment instances** when stable names exist.

Detailed tracking: [`Implementation backlog — strategic audit (P0–P3)`](implementation-backlog-strategic-audit.md).

---

## Meta and navigation

- **Structural audit (repo shape)**: [`Structural audit — repository shape and canonical routing`](structural-audit-repository-and-canonical-routing.md)  
- **Strategic audit**: [`Strategic audit — decision-safe operations for a two-site smart farm`](strategic-audit-decision-safe-operations.md)  
- **IA & prompts**: [`Information architecture — decision-safe operational brain (target design)`](information-architecture-decision-safe-operations.md), [`Agentic wiki improvement prompts (staged, strategic audit)`](agentic-wiki-improvement-prompts-strategic-audit.md)  
- **Economics**: [`Business viability and farm economics — gap analysis`](business-viability-and-farm-economics-gap-analysis.md)  
- **Tech architecture audit**: [`Smart technology architecture audit`](smart-technology-architecture-audit.md)  
- **Broad entry**: [`Knowledge synthesis`](../topics/knowledge-synthesis.md)  
- **Catalog**: [`index.md`](../index.md)  
- **Vault mechanics**: [`Repository analysis`](repository-analysis.md)

---

*Steering document: update when foundation pages, comparisons, or runbooks materially change.*
