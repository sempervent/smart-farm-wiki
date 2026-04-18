---
title: Strategic audit — decision-safe operations for a two-site smart farm
page_type: analysis
status: active
created: 2026-04-20
updated: 2026-04-21
review_status: unreviewed
tags:
  - meta
  - operations
  - two-site
  - telemetry
  - roadmap
confidence: medium
---

# Strategic audit — decision-safe operations for a two-site smart farm

**Purpose**: Ruthlessly assess whether this wiki is **sufficient** to support a future **~5-acre homestead** plus **~120-acre farming business** ~**35 minutes** away, both relying on **smart tech, automation, telemetry, edge compute, and resilient infrastructure**—and to list **what data, synthesis, and artifacts** must be added before the vault can act as a **decision-safe operational brain** (not just a document collection).

**Scope**: Evaluates the repository as a **planning system**. Distinguishes **source-note accumulation**, **genuine synthesis**, **reusable operational decision support**, and **executable architecture**. Does not invent capabilities not present in the corpus; uncertainty is called out.

**Related meta**

- [`Information architecture — decision-safe operational brain (target design)`](information-architecture-decision-safe-operations.md) — **target IA**: top-level layers, hubs, cross-linking rules, orphans, migration plan.
- [`Business viability and farm economics — gap analysis (strategic audit)`](business-viability-and-farm-economics-gap-analysis.md) — revenue, enterprise, channels, staffing, insurance, accounting, CAPEX/OPEX, logistics, risk; prioritized business pages; **under-modeled** decisions.
- [`Smart technology architecture audit (strategic audit)`](smart-technology-architecture-audit.md) — telemetry, radios, edge, HA/farmOS/MQTT/TSDB, time, identity, registry, alerting, observability, firmware, degraded modes, security, remote access; **fragmentation**, reference outline, SOPs, diagrams.
- [`Agentic wiki improvement prompts (staged, strategic audit)`](agentic-wiki-improvement-prompts-strategic-audit.md) — **Pre-prompt** + **Phase 1–4** agent prompts (foundational → operational → resilience → optimization) with deliverables and acceptance criteria.
- [`Implementation backlog — strategic audit (P0–P3)`](implementation-backlog-strategic-audit.md) — **prioritized** artifacts, effort, dependencies, and **top 10** pages to build first.
- [`Domain content overview`](domain-content-overview.md) — strand map; this audit **extends** the “Gaps and growth directions” section with an actionable backlog.
- [`Knowledge synthesis`](../topics/knowledge-synthesis.md) — entry points across the vault.
- [`Repository analysis`](repository-analysis.md) — repo mechanics vs domain content.

---

## 1. Executive judgment

The vault is **strong as a knowledge architecture** (raw → source-notes → topics/concepts/analyses, explicit strand map, honest gap callouts in [`Domain content overview`](domain-content-overview.md)). It is **not yet** a **decision-safe operations system** for a **two-site, instrumented farm business**. Strength is **breadth** (LPWAN/mesh, solar, farmOS pointer, livestock/garden captures, hydrology, roads). Weakness is **thin connective tissue**: the wiki **already states** that pages tying **soil/crop decisions** to **sensor placement** and **data models** are **sparse** compared to standalone source-notes ([`Domain content overview` — Gaps and growth directions](domain-content-overview.md)). **Synthesis** exists in pockets ([`Timing on the farm — synthesis`](timing-on-the-farm-synthesis.md), [`Agritourism business plan — guest hub on 120 acres, family home 35 min away`](agritourism-dual-site-business-plan-five-and-120-acres.md), road-erosion analyses, [`Homestead composting — practical guide`](homestead-composting-guide.md)). **Operational decision support** (SOPs, runbooks, asset registry schemas, staffing math, unit economics, security models) is **largely missing**. **Executable architecture** (canonical diagrams, telemetry schema, firmware lifecycle, observability) is **mostly absent** beyond hubs and captures.

---

## 2. What the wiki already covers well

| Area | Evidence in wiki | Why it matters | Maturity |
|------|------------------|----------------|----------|
| Dual-site narrative (one scenario) | [`Agritourism business plan — guest hub on 120 acres, family home 35 min away`](agritourism-dual-site-business-plan-five-and-120-acres.md) | Addresses **5 ac vs 120 ac**, **~35 min** commute, **coverage/caretaker**, biosecurity vs hobby animals at home | **Medium** (strong for **agritourism-led** ops; not generalized) |
| Stocking / scale as research problem | [`Farm stocking — 120 acres vs 5 acres (research prompt)`](farm-stocking-120-acres-vs-5-acres-research-prompt.md) | Frames automation vs labor; **does not** deliver prescriptions | **Low–Medium** |
| Field connectivity literacy | [`Smart agriculture, Meshtastic, and LoRaWAN`](../topics/smart-agriculture-meshtastic-and-lorawan.md), [`Field network IoT comparisons (HaLow, LoRa, NB-IoT)`](../topics/field-network-iot-comparisons.md), [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md) + concepts | Tradeoff vocabulary for telemetry | **Medium** |
| Edge / data pointers | [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md), [`ESP32, ESPHome, and smart-farming builds`](../topics/esp32-iot-smart-farming-and-tooling.md), [`Homelab, self-hosting, and edge narratives`](../topics/homelab-self-hosting-and-edge-narratives.md) | Names a **possible** record + self-host path; **not** your deployed SoR | **Medium–Low** |
| Power resilience | [`Off-grid solar power and storage (special topic)`](../topics/off-grid-solar-power-and-storage.md) | Backup / field power narratives | **Medium** |
| Time sync | [`Time synchronization — NTP and PTP sources`](../topics/time-synchronization-ntp-and-ptp.md), [`Timing on the farm — synthesis`](timing-on-the-farm-synthesis.md) | Correlating telemetry and ops | **Medium** |
| Soil / entry / compost | [`Sustainable cropping, soil, and farm entry sources`](../topics/sustainable-cropping-soil-and-farm-entry-sources.md), [`Homestead composting and soil sources`](../topics/homestead-composting-and-soil-sources.md), [`Homestead composting — practical guide`](homestead-composting-guide.md) | Compost **synthesized**; rotations elsewhere **template-oriented** | **Medium** |
| Water / ponds / irrigation | [`Ponds, water features, and homestead hydrology`](../topics/ponds-water-features-and-homestead-hydrology.md), [`Irrigation and water-wise farming sources`](../topics/irrigation-and-water-wise-farming-sources.md) | Hydrology as captures + some synthesis | **Medium** |
| TN business pointers | [`Tennessee hobby farm and small-farm business sources`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md) | Regional alignment; **excerpt-level**, not compliance ([`Domain content overview`](domain-content-overview.md)) | **Low–Medium** |
| Physical access / erosion | e.g. [`Steep curved hill dirt road — erosion prevention (120-acre farm)`](steep-curved-hill-dirt-road-erosion-prevention-120-acres.md) | Roads, sediment—not full civil engineering | **Medium** |
| Repository meta | [`Repository analysis`](repository-analysis.md), [`Domain content overview`](domain-content-overview.md), [`Knowledge synthesis`](../topics/knowledge-synthesis.md) | Maintaining the vault | **High** (for **repo** ops, not **farm** ops) |

---

## 3. Critical gaps

| Gap | Why it matters (5 ac + 120 ac + smart stack) | Evidence of weakness | Severity | Suggested artifact |
|-----|-----------------------------------------------|----------------------|----------|-------------------|
| Dual-site ops **outside agritourism** | Many businesses are **not** lodging-led | [`Agritourism business plan…`](agritourism-dual-site-business-plan-five-and-120-acres.md) is **that** scenario; little else models **generic** production logistics | **Critical** | Analysis: **Dual-site operations model — generic farm business (non-agritourism)** |
| End-to-end **telemetry architecture** | Needs backhaul, power, naming, on-call, failure modes | Integration explicitly **sparse** ([`Domain content overview`](domain-content-overview.md)) | **Critical** | Topic + diagram: **Field telemetry reference architecture — 120 ac** |
| **Spatial / GIS / asset model** | Map-anchored assets required | [`Farm data, farmOS…`](../topics/farm-data-farmos-and-ag-lab-builds.md) is intro-level; no **GIS** or **registry** standard | **Critical** | Templates: **Parcel & paddock naming**, **Farm asset registry (minimum fields)** |
| **Cybersecurity + remote access** | Attack surface for remote farm | No dedicated topic; scattered vendor mentions only | **High** | Topic: **Operational security — remote farm and homelab** |
| **Unit economics & financial ops** | CAPEX/OPEX, enterprise budgets | TN topic is pointers; no integrated model | **High** | Analysis: **Enterprise selection — unit economics worksheet (methodology)** |
| **Legal/permitting/insurance (worked)** | Two parcels multiply zoning/liability | Disclaimers only; no decision matrix | **High** | Checklist: **Insurance and liability — two parcels** (questions for counsel) |
| **Labor, coverage, routing** | **35 min** → scheduling, on-call | Worked in agritourism plan; not generalized | **High** | Template: **Weekly coverage matrix — two sites** |
| **Grazing / forage / stocking (grounded)** | Ruminants need forage math | Prompt exists; no carrying-capacity conclusions ([`Farm stocking…`](farm-stocking-120-acres-vs-5-acres-research-prompt.md)) | **High** | Ingest + analysis: **Stocking and forage — methods** |
| **Failure modes & runbooks** | Outages, false alerts, dead nodes | Partial elsewhere; no **internet/MQTT down** runbook | **High** | SOP: **Degraded modes — automation off** |
| **Comparisons (decision-grade)** | Forces tradeoffs | Core tradeoffs now include [`LoRaWAN vs Meshtastic — fixed farm telemetry`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md), [`farmOS vs lightweight stack — two-site farm`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md), [`own equipment vs custom hire — two-site logistics`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md), [`fixed gateway tower vs mobile/vehicle gateway`](../comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md); older examples: [`ducks vs chickens`](../comparisons/ducks-vs-chickens-meat-raising.md), [`raw vs wiki`](../comparisons/raw-vs-wiki.md) | **Medium** (improving) | Keep adding **decision-grade** comparisons tied to two-site + telemetry |
| **Homestead civil systems** | Septic, domestic water, home network as **ops base** | Fragmented across topics | **Medium** | Topic: **Homestead civil systems — water, waste, power, network** |

---

## 4. Missing integration layers

1. **Technology ↔ land units**: Radio topics rarely tie to **paddock boundaries**, **gates**, **distance/elevation**—the gap is **named** in [`Domain content overview`](domain-content-overview.md).
2. **farmOS / records ↔ telemetry**: [`Farm data, farmOS…`](../topics/farm-data-farmos-and-ag-lab-builds.md) and sensor topics are **adjacent**, not **integrated** (no canonical event → asset → location pattern).
3. **Business ↔ operations**: [`Tennessee hobby farm…`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md) does not link into **labor routing**, **equipment**, or **telemetry ROI**.
4. **Homestead ↔ farm site**: Strong link mainly in [`Agritourism business plan…`](agritourism-dual-site-business-plan-five-and-120-acres.md); [`Smart home — Matter, Thread…`](../topics/smart-home-matter-thread-and-home-assistant-ai.md) is not tied to **farm alerting** / **on-call**.
5. **Roads / water / power**: Not one **resilience graph** (if **road** fails, **feed** and **vet** access fail).
6. **Biological plan ↔ measurement**: [`Multi-field crop rotation plan`](multi-field-crop-rotation-plan.md) mentions distant parcels briefly; no **sensor/soil-test** loop per field.

---

## 5. Missing artifacts to add (backlog)

Groupings below are **targets for ingest + synthesis**, not promises of current content.

### Analyses

| Suggested title                                            | Purpose                                                  | Questions to answer                                      | Anchor to                                                                                                                                                                             |
| ---------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dual-site operations model — non-agritourism farm business | Generalize **5 ac / 120 ac / ~35 min** to **production** | Equipment, fuel, cold storage, **batch work** vs commute | [`Farm stocking…`](farm-stocking-120-acres-vs-5-acres-research-prompt.md), [`Agritourism business plan…`](agritourism-dual-site-business-plan-five-and-120-acres.md)                  |
| Telemetry system of record — options and boundaries        | Decide **authority** when systems disagree               | farmOS vs TSDB vs HA; **retention**; override            | [`Farm data, farmOS…`](../topics/farm-data-farmos-and-ag-lab-builds.md), [`Timing on the farm…`](timing-on-the-farm-synthesis.md)                                                     |
| CAPEX/OPEX and enterprise sequencing — two-site constraint | **Phasing** under distance                               | What must land on **120 ac** first?                      | [`Tennessee hobby farm…`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md), [`East Tennessee — profitable crops matrix`](east-tennessee-profitable-crops-matrix.md) |

### Comparisons

| Suggested title | Purpose | Questions |
|-----------------|---------|-----------|
| Gateway architecture — fixed tower vs vehicle vs mesh | Backhaul for **split sites** | SPOF, uplink diversity |
| farmOS vs lightweight stack | Operational weight vs flexibility | Team size, dev capacity |

### Concepts

| Suggested title | Purpose |
|-----------------|---------|
| Operational technology (OT) security for farms | Remote access, segmentation |
| Two-site logistics | Movement of feed, fuel, harvest, tools, people |

### Entities

| Suggested title | Purpose |
|-----------------|---------|
| Farm entities — parcels, LLCs, major equipment (placeholders) | Legal vs operating identity; asset IDs |

### Topics

| Suggested title | Purpose |
|-----------------|---------|
| Two-site smart farm operations (hub) | Single entry for split ops, on-call, routing |
| Farm cybersecurity and remote access | Consolidate scattered hints |
| Spatial data and farm map hygiene | GIS layers, paddock IDs, sensor IDs |

### Timelines

| Suggested title | Purpose |
|-----------------|---------|
| Phased build — years 0–5 (two sites) | Capital + complexity sequencing |

### Templates / checklists / SOPs

| Suggested title | Purpose |
|-----------------|---------|
| Incident response — livestock emergency (owner remote) | Action order, on-site contact, vet |
| Automation kill-switch / manual fallback | Irrigation, gates, pumps when automation wrong |
| Minimum asset registry fields | ID everything that breaks |

### Architecture docs

| Suggested title | Purpose |
|-----------------|---------|
| Reference network diagram — homestead + 120 ac | VPN, gateways, MQTT; SPOF list |

---

## 6. Priority roadmap

| Phase | Focus |
|-------|--------|
| **1 — Essential strategic** | Dual-site **non-agritourism** model + **coverage** template; **spatial/asset** minimum + SoR choice; **telemetry reference architecture** (one diagram + failure modes); **enterprise phasing** vs distance/capital |
| **2 — Operational design** | **Labor routing** + weekly rhythm; **logistics** concept; **grazing/forage** ingest + synthesis; **insurance/legal** checklist (for professionals) |
| **3 — Automation & instrumentation** | **Cybersecurity + remote access**; **observability** (alerts, false positives, broker-down runbook); **firmware lifecycle**; **comparison** pieces for gateways/stacks |
| **4 — Scale / optimize / resilience** | **Unit economics** sensitivity; **drought/flood/wildfire** tied to water/roads; **data retention/ownership**; multi-year **instrumentation** timeline |

---

## 7. Top 10 decisions not yet supported confidently

1. Which **enterprises** justify **fixed infrastructure** on 120 ac vs contracting—without unified **economics**.  
2. Which stack is **authoritative** when farmOS, HA, and a DB **disagree**.  
3. **Staffing** model for **livestock welfare** at **35 min** (beyond guest-oriented coverage).  
4. **Single vs dual** energy/comms **budget** for **two** parcels—no consolidated architecture.  
5. **Security posture** for cameras, VPN, MQTT, **remote actuators**.  
6. **Carrying capacity** / **forage plan** for ruminants (prompt only).  
7. **Market channel** under **TN** rules—pointers only.  
8. **Instrumentation priority** (which acres, which risks first).  
9. **Insurance** for public, employees, volunteers, **two parcels**.  
10. **Manual operations** when automation is **wrong** or **offline**—no runbook layer.

---

## 8. Verdict

**Already helps with**: Orienting on **tech vocabulary**, **strand navigation**, and **one** worked **dual-site agritourism** narrative ([`Agritourism business plan…`](agritourism-dual-site-business-plan-five-and-120-acres.md)); partial decisions on **roads**, **compost**, **water**, **time**, **power** themes.

**Dangerously close but not ready**: Acting as **system-design authority** for sensors + backhaul + records; replacing **extension, vet, attorney, accountant, engineer**; **“hands-off 120 acres”** via automation without a **validated** architecture.

**Must be built for decision-safe use**: **Owned** spatial/asset model (even simple); **one** reference architecture for telemetry + data + alerts with **degraded modes**; **SOP/runbook** layer; **financial/enterprise** synthesis beyond pointers; **non-agritourism** dual-site model if that is the real business.

---

*This page is a **living backlog**: update it when major hubs land or when gap severity shifts.*
