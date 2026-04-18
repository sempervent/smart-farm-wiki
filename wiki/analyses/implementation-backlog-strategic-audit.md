---
title: Implementation backlog — strategic audit (P0–P3)
page_type: analysis
status: active
created: 2026-04-20
updated: 2026-04-21
review_status: unreviewed
tags:
  - meta
  - roadmap
  - operations
  - backlog
confidence: medium
---

# Implementation backlog — strategic audit (P0–P3)

**Source of truth**: [`Strategic audit — decision-safe operations for a two-site smart farm`](strategic-audit-decision-safe-operations.md).

**Target IA**: [`Information architecture — decision-safe operational brain (target design)`](information-architecture-decision-safe-operations.md) — how backlog items **fit the navigation model** (hubs, cross-links, migration).

**Purpose**: Prioritized **implementation backlog** to convert the wiki from a **knowledge vault** into an **operational brain** for a **~5-acre homestead**, a **~120-acre farm business ~35 minutes away**, and a **heavy smart-tech / telemetry / automation** environment.

**Legend**

- **Effort**: **S** = small (roughly &lt;1 session), **M** = medium (multi-section page / light research), **L** = large (deep synthesis, diagrams, or wide ingest).
- **Orientation**: **Foundational** = naming, schemas, and primitives everything else hangs on. **Integrative** = connects land + tech + business + labor. **Optimization-oriented** = improves margin, resilience tuning, or efficiency after core exists.

---

## Missing knowledge vs missing synthesis vs missing operational structure

| Category | Meaning here | Examples from audit |
|----------|----------------|---------------------|
| **Missing knowledge** | **Raw or primary-citable** material not yet in `raw/` / **source-notes**—extension bulletins, enterprise budgets, grazing math, TN regulatory primary sources, forage carrying-capacity methods | Ingest campaigns for **grazing/forage**; **university enterprise budgets**; **NRCS/soil** references |
| **Missing synthesis** | Topics exist as fragments; need **decision-grade** analysis tying hubs together | **Dual-site non-agritourism** model; **telemetry system of record**; **CAPEX/OPEX phasing**; **instrumentation priority** |
| **Missing operational structure** | **Templates, SOPs, registries, diagrams** that operators run during incidents, outages, or weekly rhythm | **Asset registry**; **coverage matrix**; **degraded-mode SOP**; **reference network diagram** |

---

## P0 — Essential skeleton (decision-safe minimum)

*Goal: Own a **spatial/asset identity layer**, a **single integrative hub**, and a **credible telemetry + comms picture** with **failure awareness**. Without P0, the wiki remains inspiration-grade.*

| # | Title | Artifact type | Why it matters | Dependencies | Effort | Orientation |
|---|--------|---------------|----------------|--------------|--------|-------------|
| 1 | **Parcel, paddock, and asset naming conventions** | template | Every sensor, gate, tank, and vehicle must **resolve to a stable ID** on a map; without naming, telemetry is noise and farmOS/records cannot anchor to real earth. | None | S | Foundational |
| 2 | **Farm asset registry — minimum fields** | template | **Decision-safe ops** requires knowing **what exists**, **where**, **serial/spares**, **owner**—prerequisite for maintenance routing and insurance documentation. | #1 (naming) | S | Foundational |
| 3 | **Two-site smart farm operations** (hub) | topic | Single **entry point** linking **5 ac / 120 ac / ~35 min**, on-call, routing, and links to SOPs—stops the story living only inside one agritourism analysis. | Optional: link to [`Agritourism business plan…`](agritourism-dual-site-business-plan-five-and-120-acres.md) | M | Integrative |
| 4 | **Dual-site operations model — non-agritourism farm business** | analysis | Audit **critical gap**: production logistics (equipment, fuel, harvest, batch work) **without** lodging-led revenue—otherwise all “two-site” thinking is skewed. | [`Farm stocking…`](farm-stocking-120-acres-vs-5-acres-research-prompt.md), [`Agritourism business plan…`](agritourism-dual-site-business-plan-five-and-120-acres.md) (contrast) | L | Integrative |
| 5 | **Field telemetry and backhaul — reference architecture (120 ac + homestead)** | topic + architecture doc | **Critical gap**: end-to-end **power, radio, uplink, broker, on-call**—must exist as **one** maintained picture + **SPOF** list. | #1–2 (IDs), [`Field network IoT comparisons…`](../topics/field-network-iot-comparisons.md), [`LoRa, MQTT…`](../topics/lora-mqtt-and-gateway-bridges.md) | L | Foundational + integrative |
| 6 | **Telemetry system of record — options and boundaries** | analysis | Resolves **which system wins** when farmOS, HA, and a time-series DB **disagree**—audit **top unsupported decision**. | [`Farm data, farmOS…`](../topics/farm-data-farmos-and-ag-lab-builds.md), [`Timing on the farm…`](timing-on-the-farm-synthesis.md) | M | Integrative |
| 7 | **Weekly coverage and on-call matrix — two sites** | template | **35-minute** distance makes **livestock welfare** and **equipment** response a **scheduling** problem; generalizes beyond guest coverage. | #3 hub | S | Operational structure |

---

## P1 — Operational design and risk containment

*Goal: **Labor, legal hooks, biological grounding**, and **manual fallback** so automation failures do not become animal or safety failures.*

| # | Title | Artifact type | Why it matters | Dependencies | Effort | Orientation |
|---|--------|---------------|----------------|--------------|--------|-------------|
| 8 | **Incident response — livestock emergency (owner remote)** | SOP | **Highest-risk** gap when nobody is on the 120 for **35+ minutes**; names **order of calls**, **on-site contact**, **vet**, **water shutoffs**. | #3, #7 | M | Operational structure |
| 9 | **Degraded modes — automation off (irrigation, gates, pumps, alerts)** | SOP | Audit: no **MQTT/internet down** runbook; **manual** procedures must exist **before** scaling sensors. | #5–6 | M | Operational structure |
| 10 | **Insurance, liability, and two parcels — question checklist** | template | Two parcels multiply **zoning, liability, vehicle, agritourism vs production**; not legal advice—**structured questions for counsel**. | #4 | S | Operational structure |
| 11 | **Homestead civil systems — water, waste, power, network** | topic | **Ops base** at 5 ac: **domestic water, septic, backup power, LAN**—fragmented today; needed so **home** stays command-capable during farm crises. | [`Off-grid solar…`](../topics/off-grid-solar-power-and-storage.md), [`Smart home…`](../topics/smart-home-matter-thread-and-home-assistant-ai.md) | M | Integrative |
| 12 | **Stocking and forage — methods (extension-first synthesis)** | analysis | **Missing knowledge + synthesis**: carrying capacity is **not** answered by [`Farm stocking…`](farm-stocking-120-acres-vs-5-acres-research-prompt.md) alone—needs **ingested** extension + **methods** page. | Ingest campaign (knowledge); **partial raw**: [`ut-forage-menu-beef-forage-center`](../source-notes/ut-forage-menu-beef-forage-center.md), [`guide-livestock-forage-feeding-grit`](../source-notes/guide-livestock-forage-feeding-grit.md) | L | Foundational (biology) |
| 13 | **CAPEX, OPEX, and enterprise sequencing — two-site constraint** | analysis | Phasing **capital** under **distance** and **commute batch work**—supports **enterprise selection** and audit gap on **unit economics**. | [`Tennessee hobby farm…`](../topics/tennessee-hobby-farm-and-small-farm-business-sources.md), [`East Tennessee — profitable crops matrix`](east-tennessee-profitable-crops-matrix.md) | L | Integrative |
| 14 | **Spatial data and farm map hygiene** | topic | **GIS layers**, paddock IDs, sensor IDs—bridges **technology ↔ land units** (audit §4). | #1–2, #5 | M | Foundational |

---

## P2 — Security, comparisons, and instrumentation discipline

*Goal: **Decision-grade tradeoffs**, **security posture**, and **observability** so the stack is maintainable and defensible.*

| # | Title | Artifact type | Why it matters | Dependencies | Effort | Orientation |
|---|--------|---------------|----------------|--------------|--------|-------------|
| 15 | **Operational technology (OT) security — remote farm and homelab** | concept + topic | Consolidates **VPN, segmentation, camera exposure, MQTT auth**—audit **no dedicated cybersecurity topic**. | #5 | M | Foundational |
| 16 | **Farm cybersecurity and remote access** (hub) | topic | Single place for **secrets policy**, **update cadence**, **bastion vs mesh admin**—links **homelab** to **field**. | #15, [`Homelab…`](../topics/homelab-self-hosting-and-edge-narratives.md) | M | Integrative |
| 17 | **Gateway architecture — fixed tower vs vehicle vs mesh** | comparison | **Split sites** need explicit **backhaul SPOF** and **uplink diversity** tradeoffs. | [`Field network IoT comparisons…`](../topics/field-network-iot-comparisons.md) | M | Integrative |
| 18 | **farmOS vs lightweight record stack** | comparison | **Team size** and **developer capacity** drive whether Drupal/farmOS is viable vs CSV/HA/custom. | [`Farm data, farmOS…`](../topics/farm-data-farmos-and-ag-lab-builds.md) | M | Integrative |
| 19 | **Observability and alerts — broker down, false positives, on-call** | SOP / analysis | Closes **failure design** gap: **what happens** when the **alert pipeline** lies. | #5–6 | M | Optimization-oriented |
| 20 | **Firmware and device lifecycle — field nodes** | analysis | Meshtastic/ESP32/gateways **rot** without an **owned** update/replace policy. | #5 | M | Optimization-oriented |
| 21 | **Two-site logistics** (feed, fuel, harvest, tools, people) | concept | Abstract **movement** between parcels—feeds **routing** and **equipment** placement decisions. | #4 | S | Integrative |

---

## P3 — Scale, resilience tuning, and economics depth

*Goal: **Margin**, **catastrophe tying**, **data governance**, and **long-horizon phasing** after the core runs.*

| # | Title | Artifact type | Why it matters | Dependencies | Effort | Orientation |
|---|--------|---------------|----------------|--------------|--------|-------------|
| 22 | **Enterprise unit economics — worksheet (methodology)** | analysis | Supports **which enterprises justify fixed infrastructure** on 120 ac—audit **top decision gap**. | #13, ingest **budgets** (knowledge) | L | Optimization-oriented |
| 23 | **Phased build — years 0–5 (two sites)** | timeline | **Capital + complexity** sequencing; pairs with **instrumentation priority**. | #13, #5 | M | Integrative |
| 24 | **Instrumentation priority matrix — acres, risks, ROI** | analysis | Answers **which acres get sensors first**—audit gap #8 in top-10 list. | #5, #4 | M | Optimization-oriented |
| 25 | **Resilience graph — roads, water, power, comms** | analysis | **Single narrative**: if **road** fails, **feed/vet** fail; ties erosion/pond/solar topics. | [`Steep curved hill…`](steep-curved-hill-dirt-road-erosion-prevention-120-acres.md), irrigation/pond hubs | L | Integrative |
| 26 | **Drought / flood / wildfire contingencies — water and access** | analysis | Regional **catastrophe** tied to **operational** assets (audit phase 4). | #25 | M | Optimization-oriented |
| 27 | **Data retention, ownership, and compliance — telemetry** | analysis | **Who owns** sensor data, **how long** retained—future **customer/employee** exposure. | #6 | M | Optimization-oriented |
| 28 | **Farm entities — parcels, LLCs, equipment** (placeholder entity pages) | entity page(s) | **Legal vs operating identity** and **major equipment IDs**—makes the registry **real** in the wiki taxonomy. | #2 | M | Foundational |

---

## Top 10 highest-leverage pages to create first

Ranked for **leverage** = unblocks the most downstream decisions with the least duplicate work. Aligned to P0/P1.

| Rank | Page title | Artifact type | Rationale |
|------|------------|---------------|-----------|
| 1 | **Parcel, paddock, and asset naming conventions** | template | **Foundational**: without IDs, no serious telemetry, registry, or map hygiene. |
| 2 | **Farm asset registry — minimum fields** | template | Makes **maintenance, insurance, and SOPs** attach to **real objects**. |
| 3 | **Field telemetry and backhaul — reference architecture (120 ac + homestead)** | topic + architecture doc | **Largest** single gap between “smart farm reading” and **executable** stack picture. |
| 4 | **Two-site smart farm operations** (hub) | topic | **Navigation spine** for the dual-site story; links homestead + farm + tech. |
| 5 | **Dual-site operations model — non-agritourism farm business** | analysis | Stops **single-scenario** bias; required if the business is **not** lodging-led. |
| 6 | **Telemetry system of record — options and boundaries** | analysis | Resolves **conflicting truth** between apps—**top unsupported decision**. |
| 7 | **Weekly coverage and on-call matrix — two sites** | template | **35-minute** reality for **livestock** and **equipment**—operational, not abstract. |
| 8 | **Degraded modes — automation off** | SOP | **Safety / continuity** before adding more sensors. |
| 9 | **Incident response — livestock emergency (owner remote)** | SOP | **Highest consequence** failure mode for remote owner. |
| 10 | **Insurance, liability, and two parcels — question checklist** | template | Cheap to write; **de-risks** structure before **major CAPEX**. |

---

## Maintenance

- When an item ships, add a **link** from this page to the new artifact and optionally **tick** it in [`Strategic audit`](strategic-audit-decision-safe-operations.md).
- Revisit **P2/P3** after **P0** naming + telemetry architecture exist—priority may shift.
