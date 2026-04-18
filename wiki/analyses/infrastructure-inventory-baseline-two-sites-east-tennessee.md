---
title: Infrastructure inventory baseline — both sites
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-25
tags:
  - two-site
  - infrastructure
  - fences
  - water
  - execution
review_status: unreviewed
confidence: medium
---

# Infrastructure inventory baseline — both sites

**Scope**: **Physical** infrastructure shared or comparable across **`SITE_HOME`** (Claxton) and **`SITE_FARM`** (Demory): **fencing**, **lanes**, **water movement**, **gates**, **fixed crossings**—**not** utility **accounts** (see [`Utility and service baseline`](utility-and-service-baseline-two-sites-east-tennessee.md)).

**Package**: [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md).

**Entities**: [`Farm water infrastructure system`](../entities/farm-water-infrastructure-system.md) · [`Farm on-site power system`](../entities/farm-on-site-power-system.md) (generation/distribution, not **loads** table).

---

## Epistemic classes

| Class | Use |
|-------|-----|
| **Measured** | Length, diameter, pressure test, photo with date |
| **Reported** | Installer, prior owner, well log |
| **Assumption** | Engineering default—label and revisit |
| **Unknown** | Not yet inspected |

---

## Master matrix (repeat rows per segment)

| Site | Asset ID | Category | Fact class | Description / route | Material / age if known | Condition | Last verified | Blocks until known |
|------|----------|----------|------------|---------------------|---------------------------|-----------|---------------|-------------------|
| SITE_HOME | H-F-001 | Perimeter fence | Unknown | TBD | Unknown | Unknown | — | Animal plan, liability |
| SITE_HOME | H-G-001 | Gate | Unknown | TBD | Unknown | Unknown | — | Trailer access |
| SITE_FARM | F-F-001 | Perimeter fence | Unknown | TBD | Unknown | Unknown | — | Stocking boundaries |
| SITE_FARM | F-L-001 | Internal lane | Unknown | TBD | Unknown | Unknown | — | Winter feed route |

*Categories*: perimeter fence · cross fence · lane · gate · culvert · water line (buried) · riser · trough · pond dam / spillway · power run (pole to barn) — **add rows**; **do not** fill with guesses.

---

## Water movement (inventory layer)

| Site | Segment | Fact class | From → to | Pipe/size if known | Head / pressure notes | Blocks |
|------|---------|------------|-----------|---------------------|------------------------|--------|
| SITE_HOME | — | Unknown | TBD | Unknown | Unknown | Garden irrigation, frost |
| SITE_FARM | — | Unknown | Well → distribution TBD | Unknown | Unknown | Grazing layout, pump sizing |

**Deep dive**: well logs, pump curves → cite `raw/` + [`water entity`](../entities/farm-water-infrastructure-system.md).

---

## Power distribution (not end-use loads)

| Site | Segment | Fact class | Description | Panel / disconnect location | Blocks |
|------|---------|------------|-------------|----------------------------|--------|
| SITE_HOME | — | Unknown | Service → subpanels TBD | Unknown | Backup interlock, transfer switch |
| SITE_FARM | — | Unknown | Service → pump / barn TBD | Unknown | Solar tie-in point |

**End-use loads**: [`Loads register`](loads-register-known-estimated-unknown-two-sites-east-tennessee.md).

---

## Evidence, excavation, and water-development references (national / state)

**Use** for **design discipline** and **checklist** prompts—**not** a substitute for **site** engineering, **TDEC** / **local** **floodplain** **admin**, or **811** **locates** on **your** **routes**.

| Topic | Vault grounding |
|-------|-----------------|
| **Excavation / utility locate (TN)** | TN **811** captures: [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md) (`tenn811-*-capture-inbox-2026-04-18.md`). |
| **Fencing** | UT Extension **PB1541** PDF + extract in same batch. |
| **Livestock watering alternatives** | UT Extension **PB1641** PDF + extract in same batch. |
| **NRCS watering practice (CPS 614) + irrigation guide** | CPS **614** hub page + NEH **Part 652** PDF + extract in same batch. |
| **Flood hazard desk screening** | [`Tennessee two-site — official parcel, GIS, flood, and climate portals`](../source-notes/tennessee-two-site-official-parcel-gis-flood-climate-portals.md) (FEMA MSC link). |

**Field validation** (add rows to the master matrix as **measured**): white-lining dig lines per 811 guidance; **pressure**/**flow** at **troughs**; **evidence** of **unmarked** utilities → **second notice** per 811 process.

---

## Decision gates

| Decision | Blocked until |
|----------|----------------|
| Fence repair vs replace budget | Segment-level **condition** + priority animals |
| Water system upgrade (pipe, storage) | **Measured** flow/pressure at representative points + winter demand |
| Solar / generator siting | Shade study + **infrastructure** path to load centers |

---

## Site baselines

- [`Site inventory — Claxton`](site-inventory-baseline-claxton-home-base-east-tennessee.md) · [`Site inventory — Demory`](site-inventory-baseline-demory-farm-site-east-tennessee.md)
