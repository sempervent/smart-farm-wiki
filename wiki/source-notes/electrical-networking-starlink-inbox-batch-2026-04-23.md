---
title: Electrical, networking, and Starlink — inbox batch (2026-04-23)
page_type: source_note
status: active
created: 2026-04-23
updated: 2026-04-23
source_ids:
  - raw/processed/2026/victron-wiring-unlimited-43562-en.pdf
  - raw/processed/2026/nrel-off-grid-solar-module-5-design-modeling-89248.pdf
  - raw/processed/2026/nrel-off-grid-solar-module-6-installation-operations-maintenance-89249.pdf
  - raw/processed/2026/morse-micro-mm6108-mf08651-us-datasheet.pdf
  - raw/processed/2026/morse-micro-mm8108-mf15457-datasheet-v4.pdf
  - raw/processed/2026/ut-extension-pb1752.pdf
  - raw/processed/2026/ut-extension-sp434a-small-grains-ryegrass-clovers-forage.pdf
  - raw/processed/2026/starlink-specifications-sheet-mini.pdf
  - raw/processed/2026/starlink-standard-4x-kit-specifications.pdf
  - raw/processed/2026/technical-information-achieving-the-impossible-en.pdf
  - raw/processed/2026/1-introduction-inbox-2026-04-23.md
tags:
  - ingest
  - networking
  - power
  - starlink
  - victron
  - morse-micro
review_status: unreviewed
confidence: medium
---

# Electrical, networking, and Starlink — inbox batch (2026-04-23)

**Purpose**: Single **grounding note** for the **2026-04-23** ingest: **PDFs** (machine extracts beside each) plus **web/article captures** moved from `raw/inbox/` to `raw/processed/2026/`. Use for **provenance** on the **network topology analysis**—not a claim that every source is authoritative for **your** deployment.

**Synthesis**: [`Two-site smart farm — network topology and WAN/edge reference (Mermaid)`](../analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md). **Off-grid Demory** (solar+battery default, mesh-first, WAN optional): [`Off-grid power, field RF, and optional WAN — source index (Demory planning)`](off-grid-power-rf-wan-source-index-demory-planning-2026-04.md).

## Evidence summary

| Field | Content |
|-------|---------|
| **Abstract** | Large **2026-04-23** batch: Victron/NREL **PDFs** + extracts, Morse Micro **HaLow** datasheets, Starlink **spec** PDFs, UT Extension PDFs, and **web** captures (wiring series, Starlink farm articles, Meshtastic, HaLow explainers, OpenWrt notes). |
| **Authority mix** | **Agency** (NREL) + **vendor** (Victron, Morse Micro, Starlink) + **extension** (UT) + **community** articles (**supporting** only). |
| **Decision relevance** | DC **safety**, off-grid **solar** modules, **HaLow** chipset facts, **WAN** kit **electrical**—supports topology Mermaid and Demory **power/RF** index; **does not** size **your** array or **tower** without local engineering. |
| **Canonical wiki links** | [`Two-site smart farm — network topology and WAN/edge reference (Mermaid)`](../analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md) · [`Off-grid power, field RF, and optional WAN — source index (Demory planning)`](off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) · [`Connectivity strategy — Claxton and Demory`](../analyses/connectivity-strategy-for-claxton-and-demory.md) |

**Key claims** (public-safe):

- NREL off-grid **modules 5–6** are **curriculum-style** PDFs, not a site-specific design stamp.
- Starlink **spec** sheets describe **CPE-class** **power** / **interface**—not **coverage at your coordinates**.

**Open questions / follow-ups**

- Align **OpenWrt**/driver captures with **chosen** HaLow **hardware** generation.

---

## PDFs + extracts

| Topic | Raw PDF | Extract |
|-------|---------|---------|
| Victron — *Wiring Unlimited* | [`victron-wiring-unlimited-43562-en.pdf`](../../raw/processed/2026/victron-wiring-unlimited-43562-en.pdf) | [`*-extracted.md`](../../raw/processed/2026/victron-wiring-unlimited-43562-en-extracted.md) |
| NREL — off-grid solar (module 5) | [`nrel-off-grid-solar-module-5-design-modeling-89248.pdf`](../../raw/processed/2026/nrel-off-grid-solar-module-5-design-modeling-89248.pdf) | [`*-extracted.md`](../../raw/processed/2026/nrel-off-grid-solar-module-5-design-modeling-89248-extracted.md) |
| NREL — off-grid solar (module 6) | [`nrel-off-grid-solar-module-6-installation-operations-maintenance-89249.pdf`](../../raw/processed/2026/nrel-off-grid-solar-module-6-installation-operations-maintenance-89249.pdf) | [`*-extracted.md`](../../raw/processed/2026/nrel-off-grid-solar-module-6-installation-operations-maintenance-89249-extracted.md) |
| Morse Micro MM6108 | [`morse-micro-mm6108-mf08651-us-datasheet.pdf`](../../raw/processed/2026/morse-micro-mm6108-mf08651-us-datasheet.pdf) | [`*-extracted.md`](../../raw/processed/2026/morse-micro-mm6108-mf08651-us-datasheet-extracted.md) |
| Morse Micro MM8108 | [`morse-micro-mm8108-mf15457-datasheet-v4.pdf`](../../raw/processed/2026/morse-micro-mm8108-mf15457-datasheet-v4.pdf) | [`*-extracted.md`](../../raw/processed/2026/morse-micro-mm8108-mf15457-datasheet-v4-extracted.md) |
| UT Extension — PB1752 | [`ut-extension-pb1752.pdf`](../../raw/processed/2026/ut-extension-pb1752.pdf) | [`*-extracted.md`](../../raw/processed/2026/ut-extension-pb1752-extracted.md) |
| UT Extension — SP434A forage | [`ut-extension-sp434a-small-grains-ryegrass-clovers-forage.pdf`](../../raw/processed/2026/ut-extension-sp434a-small-grains-ryegrass-clovers-forage.pdf) | [`*-extracted.md`](../../raw/processed/2026/ut-extension-sp434a-small-grains-ryegrass-clovers-forage-extracted.md) |
| Starlink — Mini spec sheet | [`starlink-specifications-sheet-mini.pdf`](../../raw/processed/2026/starlink-specifications-sheet-mini.pdf) | [`*-extracted.md`](../../raw/processed/2026/starlink-specifications-sheet-mini-extracted.md) |
| Starlink — Standard 4x kit | [`starlink-standard-4x-kit-specifications.pdf`](../../raw/processed/2026/starlink-standard-4x-kit-specifications.pdf) | [`*-extracted.md`](../../raw/processed/2026/starlink-standard-4x-kit-specifications-extracted.md) |
| Technical information (EN) | [`technical-information-achieving-the-impossible-en.pdf`](../../raw/processed/2026/technical-information-achieving-the-impossible-en.pdf) | [`*-extracted.md`](../../raw/processed/2026/technical-information-achieving-the-impossible-en-extracted.md) |

---

## Web captures (markdown), same batch

**Victron / DC wiring (numbered series)**

- [`1-introduction-inbox-2026-04-23.md`](../../raw/processed/2026/1-introduction-inbox-2026-04-23.md) … [`9-credits-inbox-2026-04-23.md`](../../raw/processed/2026/9-credits-inbox-2026-04-23.md)

**Starlink / farm WAN context**

- [`how-to-share-starlink-internet-across-your-farm-inbox-2026-04-23.md`](../../raw/processed/2026/how-to-share-starlink-internet-across-your-farm-inbox-2026-04-23.md)
- [`starlink-mini-cultivating-a-connected-future-in-agriculture-and-farming-inbox-2026-04-23.md`](../../raw/processed/2026/starlink-mini-cultivating-a-connected-future-in-agriculture-and-farming-inbox-2026-04-23.md)
- [`enterprise-faqs-technical-functionality-starlinks-hjelpesenter-inbox-2026-04-23.md`](../../raw/processed/2026/enterprise-faqs-technical-functionality-starlinks-hjelpesenter-inbox-2026-04-23.md)
- (additional Starlink-themed captures in `raw/processed/2026/*starlink*inbox-2026-04-23.md`)

**Meshtastic / field RF**

- [`getting-started-meshtastic-inbox-2026-04-23.md`](../../raw/processed/2026/getting-started-meshtastic-inbox-2026-04-23.md)
- [`power-configuration-meshtastic-inbox-2026-04-23.md`](../../raw/processed/2026/power-configuration-meshtastic-inbox-2026-04-23.md)

**Wi‑Fi HaLow / sub‑GHz / Morse Micro context**

- [`how-to-10x-the-reach-of-wi-fi-devices-with-wi-fi-halow-802-11ah-inbox-2026-04-23.md`](../../raw/processed/2026/how-to-10x-the-reach-of-wi-fi-devices-with-wi-fi-halow-802-11ah-inbox-2026-04-23.md)
- [`morse-micro-introduces-the-smallest-fastest-lowest-power-and-farthest-reaching-wi-fi-chip-in-the-world-inbox-2026-04-23.md`](../../raw/processed/2026/morse-micro-introduces-the-smallest-fastest-lowest-power-and-farthest-reaching-wi-fi-chip-in-the-world-inbox-2026-04-23.md)
- [`sub-ghz-an-emerging-wlan-alternative-for-iot-applications-inbox-2026-04-23.md`](../../raw/processed/2026/sub-ghz-an-emerging-wlan-alternative-for-iot-applications-inbox-2026-04-23.md)
- [`testing-sub-ghz-wi-fi-mesh-802-11ah-802-11s-in-my-homelab-inbox-2026-04-23.md`](../../raw/processed/2026/testing-sub-ghz-wi-fi-mesh-802-11ah-802-11s-in-my-homelab-inbox-2026-04-23.md)
- [`openwrt-wiki-tohasiarfasiarf-awmhu5-001-inbox-2026-04-23.md`](../../raw/processed/2026/openwrt-wiki-tohasiarfasiarf-awmhu5-001-inbox-2026-04-23.md)
- [`openwrt-wiki-tohasiarfasiarf-mm610x-001-inbox-2026-04-23.md`](../../raw/processed/2026/openwrt-wiki-tohasiarfasiarf-mm610x-001-inbox-2026-04-23.md)

**Other (same drop)**

- [`open-source-victron-energy-inbox-2026-04-23.md`](../../raw/processed/2026/open-source-victron-energy-inbox-2026-04-23.md)
- [`forage-forage-species-ut-beef-forage-center-inbox-2026-04-23.md`](../../raw/processed/2026/forage-forage-species-ut-beef-forage-center-inbox-2026-04-23.md)
- [`greensight-inbox-2026-04-23.md`](../../raw/processed/2026/greensight-inbox-2026-04-23.md)
- [`specifications-inbox-2026-04-23.md`](../../raw/processed/2026/specifications-inbox-2026-04-23.md)
- [`technology-inbox-2026-04-23.md`](../../raw/processed/2026/technology-inbox-2026-04-23.md)
- [`list-of-wlan-channels-wikipedia-inbox-2026-04-23.md`](../../raw/processed/2026/list-of-wlan-channels-wikipedia-inbox-2026-04-23.md)

## Per-source descriptions for previously unsummarized files

The files below were present in `raw/processed/2026/` but had no explicit wiki summary text before this cleanup pass. They remain **supporting** material inside this batch rather than standalone canonical notes.

| Raw path | What it is / what it covers |
|----------|-----------------------------|
| [`2-theory-inbox-2026-04-23.md`](../../raw/processed/2026/2-theory-inbox-2026-04-23.md) | Victron *Wiring Unlimited* chapter on basic electrical theory: Ohm's law, power, conductivity, cable resistance, voltage drop, and why current calculations drive cable and fuse sizing. |
| [`3-battery-bank-wiring-inbox-2026-04-23.md`](../../raw/processed/2026/3-battery-bank-wiring-inbox-2026-04-23.md) | Victron battery-bank wiring chapter covering series/parallel layouts, balanced parallel takeoff, midpoint monitoring, battery balancers, and failure modes from uneven string wiring. |
| [`4-dc-wiring-inbox-2026-04-23.md`](../../raw/processed/2026/4-dc-wiring-inbox-2026-04-23.md) | Victron DC wiring chapter on cable selection, busbars, crimping, cable runs, DC fuses/breakers, isolation switches, shunts, and voltage-sensing practices for inverter and battery systems. |
| [`5-communication-wiring-inbox-2026-04-23.md`](../../raw/processed/2026/5-communication-wiring-inbox-2026-04-23.md) | Victron communication-wiring chapter describing signal types, interference sources, shielded/twisted-pair practices, RJ45/RJ12/VE.Direct cable roles, and protocol adapters for monitored power systems. |
| [`6-ac-wiring-inbox-2026-04-23.md`](../../raw/processed/2026/6-ac-wiring-inbox-2026-04-23.md) | Victron AC wiring chapter on 3-phase generation basics, TN/TT/IT network models, power factor, AC conductor sizing, breakers, and manual bypass patterns for inverter/charger systems. |
| [`7-ground-earth-and-electrical-safety-inbox-2026-04-23.md`](../../raw/processed/2026/7-ground-earth-and-electrical-safety-inbox-2026-04-23.md) | Victron safety chapter on earth/chassis/ground distinctions, shock paths, RCD logic, neutral-earth links, and grounding models for fixed and mobile installations. |
| [`8-galvanic-corrosion-inbox-2026-04-23.md`](../../raw/processed/2026/8-galvanic-corrosion-inbox-2026-04-23.md) | Victron marine-specific note explaining galvanic corrosion through shore earth, why hull metals corrode, and how galvanic isolators or isolation transformers interrupt the corrosion circuit without dropping protection. |
| [`bridging-the-digital-divide-how-starlink-is-transforming-farms-with-high-speed-internet-inbox-2026-04-23.md`](../../raw/processed/2026/bridging-the-digital-divide-how-starlink-is-transforming-farms-with-high-speed-internet-inbox-2026-04-23.md) | Marketing article from an HSG partner/reseller framing Starlink as rural connectivity for precision ag, equipment monitoring, market access, security cameras, and farm-family connectivity, with financing rhetoric rather than hard technical specs. |
| [`how-to-boost-starlink-internet-for-farms-with-many-devices-inbox-2026-04-23.md`](../../raw/processed/2026/how-to-boost-starlink-internet-for-farms-with-many-devices-inbox-2026-04-23.md) | Vendor sales article from GNS Wireless arguing that Starlink backhaul often needs point-to-point links, outdoor mesh, or long-range bridges to cover multiple barns, stores, cameras, and households on one farm. |
| [`remote-farm-with-starlink-are-my-product-selections-sensible-inbox-2026-04-23.md`](../../raw/processed/2026/remote-farm-with-starlink-are-my-product-selections-sensible-inbox-2026-04-23.md) | Ubiquiti forum thread about linking an off-grid Starlink shed, a second off-grid house, and remote camera points across roughly 100 acres using PtP/PTMP radios, with replies weighing AirMax, LTU, and direct-bury fiber. |
| [`starlink-anybody-inbox-2026-04-23.md`](../../raw/processed/2026/starlink-anybody-inbox-2026-04-23.md) | Farming forum thread with operator anecdotes comparing poor 4G against Starlink, discussing ease of self-install, home/farm mesh add-ons, monthly cost impressions, and general satisfaction in rural use. |
| [`starlink-business-agriculture-inbox-2026-04-23.md`](../../raw/processed/2026/starlink-business-agriculture-inbox-2026-04-23.md) | Starlink business case-study page centered on the John Deere JDLink Boost integration: in-field data, remote diagnostics, automation support, and the claim that inadequate connectivity constrains equipment productivity. |
| [`starlink-for-agriculture-inbox-2026-04-23.md`](../../raw/processed/2026/starlink-for-agriculture-inbox-2026-04-23.md) | Clarus Networks marketing overview of Starlink for agriculture covering precision farming, livestock tracking, remote operations, sustainability claims, and a reseller case-study narrative rather than engineering-grade deployment guidance. |
| [`starlink-installed-on-our-farm-inbox-2026-04-23.md`](../../raw/processed/2026/starlink-installed-on-our-farm-inbox-2026-04-23.md) | Reddit anecdote from a farm using Gen 3 Starlink in bypass mode for the whole property, with comments about robots, mesh/router chaining, payment terminals, and a suggestion to add lightning protection. |

---

## Related

- [`Off-grid power, field RF, and optional WAN — source index (Demory planning)`](off-grid-power-rf-wan-source-index-demory-planning-2026-04.md)
- [`Authoritative execution evidence cluster — East Tennessee`](authoritative-execution-evidence-cluster-east-tennessee.md)
