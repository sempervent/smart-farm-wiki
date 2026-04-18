---
title: Two-site smart farm — network topology and WAN/edge reference (Mermaid)
page_type: analysis
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - two-site
  - networking
  - topology
  - starlink
  - telemetry
  - mermaid
source_count: 11
source_ids:
  - raw/processed/2026/victron-wiring-unlimited-43562-en.pdf
  - raw/processed/2026/starlink-specifications-sheet-mini.pdf
  - raw/processed/2026/morse-micro-mm6108-mf08651-us-datasheet.pdf
confidence: medium
review_status: unreviewed
---

# Two-site smart farm — network topology and WAN/edge reference (Mermaid)

**Purpose**: A **reference-only** view of how **WAN**, **two physical sites**, **field RF**, and **DC electrical context** fit together for the **East Tennessee two-site** scenario. **Not** a deployed design—labels are **logical**. **Diagrams** use **Mermaid** (enabled in [`mkdocs.yml`](../../mkdocs.yml) via `mkdocs-mermaid2-plugin`).

**Provenance batch** (PDFs + captures): [`Electrical, networking, and Starlink — inbox batch (2026-04-23)`](../source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md). **Canonical stack narrative** (no diagrams): [`Reference architecture — 5-acre home base + 120-acre farm`](reference-architecture-5ac-homebase-120ac-smart-farm.md), [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md).

**Reading the sources**

- **Victron *Wiring Unlimited*** — DC busses, Lynx distribution, inverter/charger integration patterns (see PDF extract in batch note).
- **Starlink spec PDFs** — **Mini** vs **Standard / 4× kit** hardware facts for **uplink** planning (not coverage guarantees at your coordinates).
- **Morse Micro MM6108 / MM8108 datasheets** — **Wi‑Fi HaLow** (802.11ah) **RF** positioning for **long-range Wi‑Fi** options at **sub‑GHz**; still **orthogonal** to **Meshtastic/LoRa** in most farm stacks.
- **NREL off-grid solar** modules — **generic** design/O&M framing (Haiti training context); use for **discipline**, not **TN parcel** defaults.
- **Meshtastic captures** — power + getting started for **field mesh** posture.

---

## 1. Places, WAN uplink, and inter-site relationship

**Interpretation**: **Starlink** (or any **satellite/fixed wireless** uplink) is shown as the **shared Internet** path for discussion; **fiber/cable** may exist at **`SITE_HOME`** only—**verify** per address. **`SITE_HOME`** and **`SITE_FARM`** are **not** bridged at L2 across **`COMMUTE_ONE_WAY`**; use **VPN**, **overlay**, or **cloud** for **logical** reunification.

```mermaid
flowchart TB
  subgraph internet["Internet / cloud"]
    cloud(["SaaS / APIs / optional cloud broker"])
  end

  subgraph wan["WAN access layer"]
    starlink["Starlink terminal\n(spec: Mini vs Standard kit — see batch PDFs)"]
    wan_router["Edge router / firewall\n(VLANs, VPN, policy — TBD)"]
    starlink --> wan_router
  end

  subgraph home["SITE_HOME — control center (~5 ac scenario)"]
    homelan["LAN: HA / NOC / office / workshop\nMQTT client, TSDB ingest, backups"]
    dc_bus["DC plant (solar/battery/inverter)\nsee Victron Wiring Unlimited"]
    wan_router --> homelan
    dc_bus -.->|"AC tie / critical loads"| homelan
  end

  subgraph farm["SITE_FARM — production (~120 ac scenario)"]
    farmlan["Site LAN / field gateways\nweaker or no wireline"]
    field_rf["Field RF: Meshtastic / LoRaWAN / cameras\n(gateways → backhaul)"]
    farmlan --> field_rf
  end

  wan_router -->|"VPN / SD-WAN / tunnel\n(not a single flat LAN)"| farmlan
  homelan -->|"Records / dashboards"| cloud
  farmlan -->|"Telemetry egress"| cloud
  field_rf -->|"Via gateway"| farmlan
```

---

## 2. Telemetry and application data plane (logical)

**Interpretation**: Matches the **roles** table on [`Field telemetry reference architecture`](field-telemetry-reference-architecture-homestead-120ac.md)—**transport** (MQTT) is **not** automatically **authority** for compliance records.

```mermaid
flowchart LR
  subgraph farm_edge["SITE_FARM edges"]
    sensors["Sensors / actuators\nMODBUS / GPIO / LoRa / etc."]
    gw["Field gateway(s)\nMQTT publish"]
    sensors --> gw
  end

  subgraph transport["Message plane"]
    broker["MQTT broker\n(BROKER_LABEL)"]
    gw -->|"TLS / private net"| broker
  end

  subgraph home_core["SITE_HOME services"]
    ha["Home Assistant / automations"]
    sor["SOR / TSDB / DB\n(durable history — policy)"]
    farmos["farmOS / records UI"]
    broker --> ha
    broker --> sor
    ha --> farmos
  end

  subgraph humans["Operators"]
    phone["Alerts / phone"]
    sor --> phone
    farmos --> phone
  end
```

---

## 3. DC electrical context (coupled PV/battery/inverter)

**Interpretation**: Abstract pattern from **DC-coupled** training materials—**Victron** book details **Lynx**, **BMS**, **Multi/Quattro** integration. **Your** conductor sizes, fusing, and grounding are **not** stated here.

```mermaid
flowchart TB
  subgraph sources["DC sources"]
    pv["PV array\n(charge controllers)"]
    alt["Alternator / genset\n(optional)"]
  end

  subgraph storage["Storage"]
    batt["Battery bank\n(BMS)"]
  end

  subgraph distribution["DC distribution"]
    bus["Bus / fused distribution\n(e.g. Lynx-class — see Victron extract)"]
  end

  subgraph ac["AC integration"]
    inv["Inverter/charger\n(AC loads + grid/gen port)"]
    ac_loads["AC loads\n(home / barn)"]
  end

  pv --> bus
  alt --> bus
  bus --> batt
  bus --> inv
  inv --> ac_loads
```

---

## 4. Optional — long-range Wi‑Fi HaLow vs field mesh (decision overlay)

**Interpretation**: **802.11ah** (HaLow) and **Meshtastic/LoRa** solve **different** problems—throughput vs **very low-rate** telemetry; **coexistence** is **planning**, not **one radio**.

```mermaid
flowchart LR
  subgraph halow["802.11ah HaLow (e.g. Morse Micro silicon)"]
    mm["MM6108/MM8108-class PHY\n(sub-GHz Wi-Fi)"]
  end

  subgraph mesh["Sub-GHz mesh / LPWAN"]
    mesht["Meshtastic\n(device network)"]
    loraw["LoRaWAN\n(gateway uplink)"]
  end

  subgraph use["Typical farm fit"]
    u1["Higher IP throughput\nlong Wi-Fi links"]
    u2["Low-power sensor backhaul\n& messaging"]
    u3["Sensors to gateway\ncloud or on-prem"]
  end

  mm --> u1
  mesht --> u2
  loraw --> u3
```

---

## Limits

- **No** **public IP**, **VLAN ID**, or **radio channel** choices for **your** sites—those are **deployment** decisions.
- **Starlink** **terms**, **availability**, and **performance** vary—treat PDFs as **hardware** references.
- **Mermaid** renders on the **MkDocs** site; **Obsidian** may need a Mermaid plugin for the same diagrams in vault view.

---

## Related

- [`Electrical, networking, and Starlink — inbox batch (2026-04-23)`](../source-notes/electrical-networking-starlink-inbox-batch-2026-04-23.md)
- [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md)
- [`Remote access and operational security model — two-site smart farm`](remote-access-operational-security-model-two-site-smart-farm.md)
