---
title: Off-grid power, field RF, and optional WAN — source index (Demory planning)
page_type: source_note
status: active
created: 2026-04-24
updated: 2026-04-24
source_ids:
  - raw/processed/2026/nrel-off-grid-solar-module-5-design-modeling-89248.pdf
  - raw/processed/2026/nrel-off-grid-solar-module-6-installation-operations-maintenance-89249.pdf
  - raw/processed/2026/victron-wiring-unlimited-43562-en.pdf
tags:
  - off-grid
  - solar
  - mesh
  - meshtastic
  - halow
  - starlink
  - demory
review_status: unreviewed
confidence: medium
---

# Off-grid power, field RF, and optional WAN — source index (Demory planning)

**Purpose**: Durable **provenance index** for **`SITE_FARM`** **(Demory, Campbell County)** when the **business plan** treats the **production parcel** as **off-grid-first** (solar + battery default; WAN secondary). **Does not** assert **kW**, **Ah**, or **wire sizes** **—** those are **local** **engineering** **after** **loads** **are** **metered** **.**

**Batch hub** (PDFs + same-era captures): [`Electrical, networking, and Starlink — inbox batch (2026-04-23)`](electrical-networking-starlink-inbox-batch-2026-04-23.md).

**Canonical synthesis** (operational guidance, not duplicate extracts):

- [`Off-grid power strategy — Demory farm site`](../analyses/off-grid-power-strategy-demory-farm-site.md)
- [`Mesh and field networking strategy — off-grid Demory farm`](../analyses/mesh-and-field-networking-strategy-off-grid-demory-farm.md)
- [`Off-grid degraded modes — power and connectivity (Demory)`](../analyses/off-grid-degraded-modes-power-and-connectivity-demory-farm.md)
- [`Off-grid operational decision rules — power and networking (Demory)`](../analyses/off-grid-operational-decision-rules-power-and-networking-demory-farm.md)
- [`Off-grid farm execution topology — Demory (Mermaid)`](../analyses/off-grid-farm-execution-topology-demory-mermaid.md)
- [`Meshtastic vs Wi‑Fi HaLow vs conventional Wi‑Fi — off-grid farm operations`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md)

---

## By theme (raw paths)

### Off-grid solar, batteries, O&M (authoritative framing)

| Source | Raw |
|--------|-----|
| NREL — off-grid solar module 5 (design / modeling) | [`nrel-off-grid-solar-module-5-design-modeling-89248.pdf`](../../raw/processed/2026/nrel-off-grid-solar-module-5-design-modeling-89248.pdf) · [`*-extracted.md`](../../raw/processed/2026/nrel-off-grid-solar-module-5-design-modeling-89248-extracted.md) |
| NREL — off-grid solar module 6 (installation, O&M) | [`nrel-off-grid-solar-module-6-installation-operations-maintenance-89249.pdf`](../../raw/processed/2026/nrel-off-grid-solar-module-6-installation-operations-maintenance-89249.pdf) · [`*-extracted.md`](../../raw/processed/2026/nrel-off-grid-solar-module-6-installation-operations-maintenance-89249-extracted.md) |
| Victron — *Wiring Unlimited* (DC bus, distribution discipline) | [`victron-wiring-unlimited-43562-en.pdf`](../../raw/processed/2026/victron-wiring-unlimited-43562-en.pdf) · [`*-extracted.md`](../../raw/processed/2026/victron-wiring-unlimited-43562-en-extracted.md) |
| Victron wiring article series (web captures) | [`1-introduction-inbox-2026-04-23.md`](../../raw/processed/2026/1-introduction-inbox-2026-04-23.md) … [`9-credits-inbox-2026-04-23.md`](../../raw/processed/2026/9-credits-inbox-2026-04-23.md) (see batch note) |

### Meshtastic — power and getting started (operator docs, captured)

| Source | Raw |
|--------|-----|
| Getting started | [`getting-started-meshtastic-inbox-2026-04-23.md`](../../raw/processed/2026/getting-started-meshtastic-inbox-2026-04-23.md) |
| Power configuration | [`power-configuration-meshtastic-inbox-2026-04-23.md`](../../raw/processed/2026/power-configuration-meshtastic-inbox-2026-04-23.md) |

### Wi‑Fi HaLow / 802.11ah / sub‑GHz Wi‑Fi (datasheets + context)

| Source | Raw |
|--------|-----|
| Morse Micro MM6108 datasheet | [`morse-micro-mm6108-mf08651-us-datasheet.pdf`](../../raw/processed/2026/morse-micro-mm6108-mf08651-us-datasheet.pdf) · [`*-extracted.md`](../../raw/processed/2026/morse-micro-mm6108-mf08651-us-datasheet-extracted.md) |
| Morse Micro MM8108 datasheet | [`morse-micro-mm8108-mf15457-datasheet-v4.pdf`](../../raw/processed/2026/morse-micro-mm8108-mf15457-datasheet-v4.pdf) · [`*-extracted.md`](../../raw/processed/2026/morse-micro-mm8108-mf15457-datasheet-v4-extracted.md) |
| HaLow reach / 802.11ah (article capture) | [`how-to-10x-the-reach-of-wi-fi-devices-with-wi-fi-halow-802-11ah-inbox-2026-04-23.md`](../../raw/processed/2026/how-to-10x-the-reach-of-wi-fi-devices-with-wi-fi-halow-802-11ah-inbox-2026-04-23.md) |
| Sub‑GHz WLAN alternative (article capture) | [`sub-ghz-an-emerging-wlan-alternative-for-iot-applications-inbox-2026-04-23.md`](../../raw/processed/2026/sub-ghz-an-emerging-wlan-alternative-for-iot-applications-inbox-2026-04-23.md) |
| Homelab 802.11ah mesh test (article capture) | [`testing-sub-ghz-wi-fi-mesh-802-11ah-802-11s-in-my-homelab-inbox-2026-04-23.md`](../../raw/processed/2026/testing-sub-ghz-wi-fi-mesh-802-11ah-802-11s-in-my-homelab-inbox-2026-04-23.md) |
| OpenWrt + HaLow-class hardware notes (wiki captures) | [`openwrt-wiki-tohasiarfasiarf-awmhu5-001-inbox-2026-04-23.md`](../../raw/processed/2026/openwrt-wiki-tohasiarfasiarf-awmhu5-001-inbox-2026-04-23.md), [`openwrt-wiki-tohasiarfasiarf-mm610x-001-inbox-2026-04-23.md`](../../raw/processed/2026/openwrt-wiki-tohasiarfasiarf-mm610x-001-inbox-2026-04-23.md) |

### Starlink as optional WAN / backhaul (specs + context)

| Source | Raw |
|--------|-----|
| Starlink Mini spec sheet | [`starlink-specifications-sheet-mini.pdf`](../../raw/processed/2026/starlink-specifications-sheet-mini.pdf) · [`*-extracted.md`](../../raw/processed/2026/starlink-specifications-sheet-mini-extracted.md) |
| Starlink Standard kit | [`starlink-standard-4x-kit-specifications.pdf`](../../raw/processed/2026/starlink-standard-4x-kit-specifications.pdf) · [`*-extracted.md`](../../raw/processed/2026/starlink-standard-4x-kit-specifications-extracted.md) |
| Farm WAN article captures | listed under **Starlink / farm WAN** in [`Electrical batch`](electrical-networking-starlink-inbox-batch-2026-04-23.md) |

---

## Evidence cluster

[`Authoritative execution evidence cluster — East Tennessee`](authoritative-execution-evidence-cluster-east-tennessee.md) (agency / extension index; **not** a substitute for **NEC** / **licensed** **design** **.)
