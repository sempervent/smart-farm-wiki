---
title: Information architecture — decision-safe operational brain (target design)
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
review_status: unreviewed
tags:
  - meta
  - information-architecture
  - two-site
  - telemetry
  - operations
confidence: medium
---

# Information architecture — decision-safe operational brain (target design)

**Purpose**: Define a **target information architecture (IA)** for this wiki so it can function as a **decision-safe operational brain**: not only curated sources and concepts, but **owned identity layers** (spatial, asset, data authority), **executable architecture**, and **runnable operations** (SOPs, templates, failure modes).

**Grounding**: Extends [`Strategic audit — decision-safe operations for a two-site smart farm`](strategic-audit-decision-safe-operations.md) and [`Implementation backlog — strategic audit (P0–P3)`](implementation-backlog-strategic-audit.md). This page is **design intent**; the backlog remains the **prioritized build list**.

**Staged agent prompts**: [`Agentic wiki improvement prompts (staged, strategic audit)`](agentic-wiki-improvement-prompts-strategic-audit.md) — pre-prompt + Phase 1–4 to build out the IA in order.

**Foundation spine (2026)** — [`Dual-site operations model — non-agritourism`](dual-site-operations-model-non-agritourism.md), [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md), [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md), [`CAPEX, OPEX, and enterprise sequencing — two-site constraint`](capex-opex-enterprise-sequencing-two-site-constraint.md), [`Weekly coverage matrix — two-site`](weekly-coverage-matrix-two-site-farm-operations.md), [`Automation degraded modes and manual fallback SOP`](automation-degraded-modes-manual-fallback-sop.md). **Runbooks**: [`broker/backhaul down`](runbook-broker-or-backhaul-down.md), [`power loss — remote site`](runbook-power-loss-remote-site.md), [`sensor false positive / alert triage`](runbook-sensor-false-positive-alert-triage.md), [`manual fallback — irrigation, gates, pumps`](runbook-manual-fallback-irrigation-gates-pumps.md). **Tradeoff comparisons**: [`LoRaWAN vs Meshtastic — fixed farm telemetry`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md), [`farmOS vs lightweight stack — two-site farm`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md), [`own equipment vs custom hire — two-site logistics`](../comparisons/own-equipment-vs-custom-hire-two-site-logistics.md), [`fixed gateway tower vs mobile/vehicle gateway`](../comparisons/fixed-gateway-tower-vs-mobile-vehicle-gateway.md).

**Audience**: Human operators and agents maintaining `wiki/`; scope is **~5-acre homestead**, **~120-acre farm business**, **~35-minute** separation, **instrumented** stack (telemetry, edge, automation).

---

## 1. Design principles

| Principle | Meaning for IA |
|-----------|----------------|
| **Single spine** | Every operational page should reach **two-site operations**, **telemetry**, or **enterprise/finance** within **two hops** (hub → specialist page). |
| **Identity before instrumentation** | **Parcel / paddock / asset IDs** and **map hygiene** precede sensor density; otherwise events cannot attach to land or liability. |
| **Authority is explicit** | One **system of record** decision per data class (telemetry vs records vs alerts)—see target analyses below. |
| **Degraded modes first** | Automation SOPs assume **offline / wrong / malicious** states; happy-path-only docs are insufficient. |
| **Cross-domain edges are first-class** | Road ↔ vet access ↔ feed movement ↔ comms ↔ water is one **resilience** object—not isolated topic silos. |

---

## 2. Proposed top-level structure (logical layers)

Folders stay within the existing taxonomy (`concepts/`, `topics/`, `analyses/`, `comparisons/`, `entities/`, `timelines/`, `glossary/`, `source-notes/`). The **target IA** adds **named layers** inside `wiki/index.md` and **consistent prefixes** so navigation matches mental model.

```text
wiki/
├── overview.md                    # North star + link to "operations spine"
├── concepts/                      # Stable definitions (incl. OT security, two-site logistics)
├── topics/                        # Hubs: source clusters + integrative hubs (NEW hubs below)
├── analyses/                      # Decision-grade synthesis, SOPs, architecture narratives, fillable templates
├── comparisons/                   # Decision-grade A/B (stacks, gateways, record systems)
├── entities/                      # Parcels, LLCs, major equipment (placeholders → real)
├── timelines/                     # Phased build, seasons, capital sequencing
├── glossary/                      # Terms of art for ops + tech
└── source-notes/                  # Provenance anchors (unchanged role)
```

**Index organization (target)**: Group intentional pages under **seven bands** (reorder `wiki/index.md` over migration):

1. **Meta & repository** — overview, repository analysis, domain content overview, this IA note, strategic audit, implementation backlog, log.
2. **Operations spine (dual-site)** — dedicated topic hub + linked SOPs/templates (below).
3. **Enterprise & finance** — TN business topic, unit economics analyses, crop/enterprise matrices (cross-linked to spine).
4. **Land & biology** — cropping, livestock, forage, stocking, compost, ponds (existing topics; tied to **spatial hub**).
5. **Physical infrastructure** — solar, water, irrigation, roads, erosion (existing topics; tied to **resilience** analysis).
6. **Digital & telemetry** — field networks, MQTT, data storage concept, farm data, **reference architecture** analyses, security hub.
7. **Capture** — source-notes (volume may stay alphabetical; **see migration**).

`docs/` continues **operator handbook** (how the repo works); **farm system architecture** lives in **`wiki/analyses/`** (or future `wiki/architecture/` only if the taxonomy is formally extended).

---

## 3. New topic hubs (required)

These are **integrative** hubs called out in the strategic audit; they should appear in **`wiki/index.md`** under Topics and **interlink heavily**.

| Hub (target path) | Role | Primary links |
|-------------------|------|----------------|
| **`topics/two-site-smart-farm-operations.md`** | **Spine**: 5 ac / 120 ac / ~35 min; coverage; routing; on-call; entry to SOPs | Agritourism dual-site analysis (contrast), stocking prompt, weekly coverage template, incident SOP |
| **`topics/field-telemetry-and-backhaul.md`** | End-to-end **field + homestead** comms: power, radio, uplink, broker, observability | LoRa/MQTT topic, field IoT comparisons, data storage concept, reference architecture analysis |
| **`topics/spatial-data-and-farm-map-hygiene.md`** | **GIS layers**, paddock IDs, sensor binding, PostGIS/farmOS positioning | Farm data topic, PostGIS source-notes, naming template |
| **`topics/farm-cybersecurity-and-remote-access.md`** | VPN, segmentation, MQTT auth, camera exposure, update cadence | Homelab topic, OT security concept, telemetry hub |
| **`topics/homestead-civil-systems.md`** | **Ops base**: domestic water, septic, backup power, LAN—command post during crises | Smart home topic, off-grid solar topic, degraded-mode SOPs |

**Optional consolidation later**: A single **“Resilience”** hub page that only **indexes** [`Resilience graph — roads, water, power, comms`](implementation-backlog-strategic-audit.md#p3--scale-resilience-tuning-and-economics-depth) (once written) and ties irrigation/ponds/roads—avoid duplicating body text.

---

## 4. Required analysis pages (minimum set)

Aligned to P0–P3 in the implementation backlog; titles match **artifact names** there for traceability.

### P0 — Skeleton (authority + architecture)

| Analysis | Intent |
|----------|--------|
| **Dual-site operations model — non-agritourism farm business** | Production logistics without lodging-led bias; equipment, fuel, harvest, batch work vs commute. |
| **Telemetry system of record — options and boundaries** | Who wins when farmOS, Home Assistant, and TSDB disagree; retention; manual override. |
| **Field telemetry and backhaul — reference architecture (120 ac + homestead)** | One maintained picture: radios, gateways, power, uplink, broker, alert path, **SPOF** list. |

### P1 — Risk, labor, finance shape

| Analysis | Intent |
|----------|--------|
| **CAPEX, OPEX, and enterprise sequencing — two-site constraint** | Phasing capital under distance; ties to profitable crops matrix and TN business pointers. |
| **Stocking and forage — methods (extension-first synthesis)** | Ground carrying-capacity work; bridges forage PDFs + research prompt. |
| **Resilience graph — roads, water, power, comms** | Single narrative for cascading failure (audit §4 integration gap). |

### P2–P3 — Depth

| Analysis | Intent |
|----------|--------|
| **Observability and alerts — broker down, false positives, on-call** | Failure of the **alert pipeline** as first-class. |
| **Firmware and device lifecycle — field nodes** | Replace/update policy for gateways and MCUs. |
| **Enterprise unit economics — worksheet (methodology)** | Which enterprises justify fixed infrastructure on 120 ac. |
| **Instrumentation priority matrix — acres, risks, ROI** | Ordered sensor plan. |
| **Data retention, ownership, and compliance — telemetry** | Legal/operational data policy. |
| **Drought / flood / wildfire contingencies — water and access** | Regional catastrophe tied to assets. |

**Fillable templates (as `analyses/` pages with `tags` including `template`)**

| Template | Intent |
|----------|--------|
| **Parcel, paddock, and asset naming conventions** | Stable IDs for map + telemetry. |
| **Farm asset registry — minimum fields** | What exists, where, serial, owner—insurance + maintenance. |
| **Weekly coverage and on-call matrix — two sites** | 35-minute reality for livestock + equipment. |
| **Insurance, liability, and two parcels — question checklist** | Structured questions for counsel (not legal advice). |

**SOPs (as `analyses/` pages with `tags` including `sop`)**

| SOP | Intent |
|-----|--------|
| **Incident response — livestock emergency (owner remote)** | Call order, on-site contact, vet, shutoffs. |
| **Degraded modes — automation off (irrigation, gates, pumps, alerts)** | Manual procedures when MQTT/internet/automation fails. |

---

## 5. Required comparison pages

| Comparison | Decision |
|------------|----------|
| **Gateway architecture — fixed tower vs vehicle vs mesh** | Backhaul SPOF and uplink diversity for split sites. |
| **farmOS vs lightweight record stack** | Operational weight vs team capacity (links farm data topic). |

**Existing comparisons** ([`Raw vs wiki`](../comparisons/raw-vs-wiki.md), [`Ducks vs chickens`](../comparisons/ducks-vs-chickens-meat-raising.md)) remain; add **cross-links from operations spine** only where they inform **livestock ops** or **knowledge governance**.

---

## 6. Required templates (repo + wiki)

**Repository templates** (under `templates/`—scaffold with `scripts/scaffold_page.py` when added):

| File | Use |
|------|-----|
| `sop-page.md` | Incident/degraded-mode SOP structure (steps, contacts, escalation, verification). |
| `architecture-doc.md` | Reference architecture: diagram slots, SPOF table, data flows, assumptions, revision date. |
| `registry-template.md` | Rows/columns for asset registry; link to naming conventions. |
| `weekly-coverage-matrix.md` | Rows = days/shifts; columns = sites + roles. |

**Wiki pages** using those shapes live in **`wiki/analyses/`** with stable titles; `templates/` provides **scaffold parity** with [`templates/analysis-page.md`](../../templates/analysis-page.md).

---

## 7. Required architecture documentation (where it lives)

| Doc | Location | Content |
|-----|----------|---------|
| **Reference network — homestead + 120 ac** | `wiki/analyses/architecture-reference-network-homestead-120ac.md` (name may vary) | VPN paths, MQTT, gateways, HA core, **single diagram** + SPOF table. |
| **Telemetry dataflow** | Section inside **field telemetry** topic + link from **system of record** analysis | Event → broker → storage → alert → human. |
| **Spatial model** | `topics/spatial-data-and-farm-map-hygiene.md` + naming template | Layers, CRS discipline, binding sensor ID ↔ geometry. |

**Not** in `docs/` unless the operator handbook needs a **pointer** (`docs/workflows/` already covers ingest; farm topology is **domain** wiki).

---

## 8. Required entity pages (minimum)

Placeholders can start as **`status: draft`** with `confidence: low` until populated.

| Entity pattern | Examples |
|----------------|----------|
| **Parcels / sites** | `entities/site-homestead-5ac.md`, `entities/site-farm-120ac.md` — addresses, access constraints, legal refs (by pointer, not advice). |
| **Operating / holding entities** | LLC or partnership placeholder—**names only** when approved; link to insurance checklist. |
| **Major equipment** | Tractor, truck, gateway tower, cold storage—**asset IDs** matching registry template. |

[`Example Organization`](../entities/example-org.md) remains the template pattern; real entities **supersede** demo content when introduced.

---

## 9. Cross-linking rules (how pages should connect)

**Hub-and-spoke**

- **`topics/two-site-smart-farm-operations.md`** links outward to: enterprise analyses, coverage template, incident SOP, degraded-mode SOP, logistics concept, agritourism analysis (contrast), stocking/forage analyses.
- **`topics/field-telemetry-and-backhaul.md`** links to: LoRa/MQTT topic, data storage concept, system-of-record analysis, reference architecture analysis, cybersecurity hub, time sync topic.

**Land ↔ digital binding**

- Every **sensor/gateway** narrative should eventually cite **`topics/spatial-data-and-farm-map-hygiene.md`** + **naming conventions** (once published).
- **farmOS / records** topic links to **system of record** analysis and **spatial** hub.

**Business ↔ ops**

- **Tennessee hobby farm** topic links to **enterprise sequencing** analysis, **unit economics** analysis, **two-site** hub.
- **Profitable crops matrix** links to **CAPEX/OPEX** and **instrumentation priority**.

**Resilience**

- Road erosion / pond / irrigation analyses link to **resilience graph** (when written) and **degraded-mode** SOP.

**Provenance**

- New synthesis pages add **`source_ids`** or “Grounded sources” only when claims need it; operational templates may be **methodology-only** with disclaimers.

---

## 10. Current areas: orphans and weak integration

These are **structural** observations (not necessarily `validate_wiki.py` orphans): integration **between strands** is thin, as the audit states.

| Area | Symptom | Target fix |
|------|---------|------------|
| **Dual-site narrative** | Strong in [`Agritourism business plan…`](agritourism-dual-site-business-plan-five-and-120-acres.md); **generic** production model missing | **Two-site operations hub** + **non-agritourism analysis** |
| **Telemetry** | Strong **topic literacy** (LoRa, MQTT, comparisons); **no** end-to-end architecture | **Field telemetry hub** + **reference architecture** + **system of record** |
| **Spatial / GIS** | PostGIS captures + farm data topic; **no** hygiene / registry standard | **Spatial hub** + **naming** + **registry templates** |
| **farmOS / HA / DB** | Adjacent topics; **no conflict-resolution** story | **Telemetry system of record** analysis |
| **Smart home / HA** | Consumer + Matter focus; **not** tied to **farm alerting** or **on-call** | Link from **two-site hub** + **civil systems** topic |
| **TN business / Shopify / tax excerpts** | Pointers; **no** labor routing or **enterprise phasing** | **CAPEX/OPEX** analysis + **two-site hub** |
| **Roads + water + power** | Good source clusters; **no** single **resilience** narrative | **Resilience graph** analysis |
| **Livestock / forage** | Many source-notes; **stocking** still prompt-forward | **Stocking and forage — methods** analysis |
| **Comparisons** | Only two; **stack decisions** underrepresented | **Gateway** + **farmOS vs lightweight** comparisons |

---

## 11. Migration plan (current wiki → target IA)

**Phase A — Navigation (low risk)**  
1. Add **`wiki/index.md`** subsection **“Operations spine (dual-site & telemetry)”** listing new hubs once created (even as stubs with `status: draft`).  
2. Update **`topics/knowledge-synthesis.md`** with the seven-band mental model and link to this page.  
3. Cross-link **`wiki/overview.md`** with one paragraph: “Operational brain” → strategic audit + IA + implementation backlog.

**Phase B — P0 artifacts (foundation)**  
1. Publish **naming conventions** + **asset registry** templates (`wiki/analyses/`).  
2. Create **stub** topic hubs: two-site operations, field telemetry, spatial hygiene, cybersecurity, civil systems—with **Related** sections pointing to existing topics.  
3. Draft **reference architecture** + **system of record** analyses (outline + open questions OK).  
4. Add **weekly coverage** template.

**Phase C — P1 SOPs and risk**  
1. **Incident** + **degraded-mode** SOPs.  
2. **Insurance checklist** template.  
3. **Dual-site non-agritourism** analysis (first full narrative).  
4. **Homestead civil systems** topic fleshed from existing solar + smart-home sources.

**Phase D — P2 comparisons and security depth**  
1. **Gateway** + **farmOS** comparisons.  
2. **OT security** concept finalized; link into cybersecurity hub.

**Phase E — P3 economics and resilience**  
1. **Unit economics**, **instrumentation priority**, **resilience graph**, **data retention** analyses.  
2. **Phased build timeline** populated.  
3. **Entity pages** for real parcels/equipment as decisions land.

**Ongoing**  
- After each new hub: **append `wiki/log.md`**, run `validate_wiki.py --strict`, refresh **implementation backlog** links.  
- Optionally run `scripts/rebuild_index.py` to audit coverage.

---

## 12. Related

- [`Strategic audit — decision-safe operations for a two-site smart farm`](strategic-audit-decision-safe-operations.md)  
- [`Implementation backlog — strategic audit (P0–P3)`](implementation-backlog-strategic-audit.md)  
- [`Domain content overview`](domain-content-overview.md)  
- [`Knowledge synthesis`](../topics/knowledge-synthesis.md)

---

*Revision policy: Update this IA when the backlog phases shift or when a new top-level band (e.g. dedicated `wiki/operations/`) is formally adopted in `AGENTS.md`.*
