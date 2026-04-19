---
title: American ginseng — woodlot maintenance, pathology, and remote security
page_type: analysis
page_subtype: operational_guide
status: active
created: 2026-04-20
updated: 2026-04-20
review_status: unreviewed
confidence: medium
operational_maturity: draft
tags:
  - american-ginseng
  - security
  - trail-camera
  - observability
source_ids:
  - raw/processed/2026/ginseng-pest-management-presentation-capture-inbox-2026-04-20.pdf
  - raw/processed/2026/ginseng-fungicide-tables-organic-conventional-capture-inbox-2026-04-20.pdf
  - raw/processed/2026/ut-soil-plant-pest-center-ginseng-fungal-pathogens-capture-inbox-2026-04-20.md
  - raw/processed/2026/ginseng-site-selection-capture-inbox-2026-04-20.pdf
---

# American ginseng — woodlot maintenance, pathology, and remote security

**Routing**: **Field maintenance** (disease awareness, scouting, sanitation) plus a **phased security stack** that starts with **trail cameras** and can later align with the **homelab / farm edge** video posture—without pretending cameras replace **legal**, **physical**, or **biosecurity** controls.

**Suite**: [`ASAP start plan`](american-ginseng-from-seed-asap-start-plan.md) · [`Site evaluation + materials`](american-ginseng-site-evaluation-and-materials-checklist.md) · [`Planting + cultivation`](american-ginseng-planting-and-cultivation-guide.md) · **this page**

**Provenance**: [`American ginseng — PDF-heavy inbox batch … 2026-04-20`](../source-notes/american-ginseng-pdf-heavy-inbox-batch-2026-04-20.md) · UT Soil, Plant and Pest Center capture · [`Local video / NVR — role and deferral boundaries (farm stack)`](local-video-nvr-role-and-deferral-boundaries-farm-stack.md)

**Mandatory vs optional**

| Tier | Scope |
|------|--------|
| **Mandatory** | **Identify** diseases before buying fungicides; follow **label** law and applicator licensing; **never** apply from wiki tables alone. |
| **Mandatory for security** | **Landowner permission**, **no trespass** signage where appropriate, **insurance** review for theft. |
| **Optional Phase 0** | **Cellular or SD-card trail cameras** on plot approaches (cheap signal of intrusion). |
| **Optional Phase 1+** | **On-LAN IP cameras + Frigate-class NVR** only after power, storage, and WAN doctrine gates—see deferral page. |

---

## 1. Maintenance rhythm (annual)

| Season | Tasks |
|--------|--------|
| **Early spring** | Scout emergence; check for **damping-off**; verify mulch did not smother crowns; slug / rodent sign |
| **Late spring / summer** | Thin competing brush; maintain **airflow**; photograph canopy gaps; remove diseased leaf litter where feasible (Alternaria management pattern in extension literature) |
| **Fall** | Verify seed drop / replanting if harvesting any plants under **TDEC** rules; prep winter mulch if used in your system |

---

## 2. Pathology mindset (disease triangle)

The **2021** workshop deck [`ginseng-pest-management-presentation-capture-inbox-2026-04-20.pdf`](../../raw/processed/2026/ginseng-pest-management-presentation-capture-inbox-2026-04-20.pdf) frames **host + pathogen + environment + time**. Practical meaning:

- **Host**: juvenile tissue is most vulnerable to **damping-off**; mature stands still get **Alternaria** leaf blight and **Phytophthora**-class root rots when drainage fails.
- **Environment**: humid, stagnant air + dense planting = higher **Alternaria** pressure—often addressed by **spacing**, **pruning competing vegetation**, and **sanitation**.
- **Time**: scout **after** rain events and **before** long trips away from the woodlot.

---

## 3. University + state lab resources (Tennessee)

[`ut-soil-plant-pest-center-ginseng-fungal-pathogens-capture-inbox-2026-04-20.md`](../../raw/processed/2026/ut-soil-plant-pest-center-ginseng-fungal-pathogens-capture-inbox-2026-04-20.md) documents the **UT Soil, Plant and Pest Center** collaboration with **MTSU International Ginseng Institute**, including **sample submission** pathways and **tabular** active ingredients keyed to pathogens (**Alternaria**, **Phytophthora**, etc.). **Fungicide tables** PDF [`ginseng-fungicide-tables-organic-conventional-capture-inbox-2026-04-20.pdf`](../../raw/processed/2026/ginseng-fungicide-tables-organic-conventional-capture-inbox-2026-04-20.pdf) complements the page capture.

**Wiki policy**: Do **not** copy **rates**, **REI**, or **trade-name stacks** into this page—those belong on the **label** you hold in hand after a **diagnosis**.

---

## 4. Remote security — Phase 0 trail cameras

Why start here:

- The Cornell **site selection** sheet in [`ginseng-site-selection-capture-inbox-2026-04-20.pdf`](../../raw/processed/2026/ginseng-site-selection-capture-inbox-2026-04-20.pdf) literally scores **“Surveillance camera installed”** as a partial mitigation for **exposure** risk—useful when plots are not beside the farmhouse.
- **Cellular** cameras can alert without **LAN** infrastructure; **SD-card** cameras are cheaper but require **physical** retrieval (fits **off-grid** visits to `SITE_FARM`).

**Operational checklist**

| Item | Guidance |
|------|----------|
| **Placement** | Aim along **trails / logging roads / property lines** approaching beds—not at public roads where privacy law gets messy |
| **Height & angle** | Chest–head height, slight downward tilt; **test** daylight + night IR glare from understory |
| **Power** | Lithium packs vs solar—match to **seasonal** visit schedule |
| **Storage policy** | Download/delete clips on a schedule; **encrypt** SD cards if supported |
| **Comms** | Cellular units need **carrier** reality check at ridge vs hollow (same as WAN planning elsewhere in the wiki) |
| **Law & ethics** | Post **private property** signage; know **TN** recording/peeping statutes for **areas filmed**; do **not** stream **public** URLs of ginseng locations |

Trail cameras are **evidence/deterrence aids**, not proof of compliance with **animal welfare**, **food safety**, or **insurance** clauses.

---

## 5. Remote security — Phase 1+ IP video (smart farm stack)

When **LAN**, **PoE switches**, **disk**, and **operator time** exist, align with:

- [`Local video / NVR — role and deferral boundaries (farm stack)`](local-video-nvr-role-and-deferral-boundaries-farm-stack.md) — **Frigate-class** scope, **MQTT** / **Home Assistant** integration, **WAN dependency** cautions.
- [`Monitoring and logging expectations — edge cluster standard`](monitoring-and-logging-expectations-edge-cluster-standard.md) — observability **minimums** for the **homelab / farm edge** (metrics/logs), complementary to video.

**Do not** hang multi-camera **4K** retention on **Starlink-only** backhaul without walking the **CS-*** stop rules in [`Automation stop rules — two-site smart farm`](automation-stop-rules-two-site-smart-farm.md).

---

## 6. Poaching and operational security (non-video)

- **Human theft** of ginseng is a **documented** risk in Hankins and popular sources—vary visit times, remove **geo-tagged** social posts, and consider **GPS-private** plot maps.
- **Deer / rodents**: fence sections, **harvest** pressure, or **exclusion cages** on high-value test plots—tie back to **site evaluation** scores.

---

## Sources

- [`American ginseng — PDF-heavy inbox batch (2026-04-20)`](../source-notes/american-ginseng-pdf-heavy-inbox-batch-2026-04-20.md)
- [`ut-soil-plant-pest-center-ginseng-fungal-pathogens-capture-inbox-2026-04-20.md`](../../raw/processed/2026/ut-soil-plant-pest-center-ginseng-fungal-pathogens-capture-inbox-2026-04-20.md)
- [`Local video / NVR — role and deferral boundaries (farm stack)`](local-video-nvr-role-and-deferral-boundaries-farm-stack.md)
