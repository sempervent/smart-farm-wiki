---
title: Off-grid farm execution topology — Demory (Mermaid)
page_type: analysis
status: active
created: 2026-04-24
updated: 2026-04-17
tags:
  - mermaid
  - off-grid
  - demory
  - topology
confidence: medium
---

# Off-grid farm execution topology — Demory (Mermaid)

## Purpose

**Three** **Mermaid** **views** **for** **`SITE_FARM`** **(Demory)** **:** **reference** **(intended** **off-grid** **+** **field** **network** **) **,** **pilot** **(Phase** **0/1** **) **,** **degraded** **(low** **SOC** **/** **WAN** **loss** **/** **local-only** **)** **—** **with** **power** **domains** **and** **trust** **zones** **.**

**Doctrine** **package** **:** [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md) **.**

**Policy** **pages** **:** [`Off-grid power doctrine — Demory farm site`](off-grid-power-strategy-demory-farm-site.md) **,** [`Mesh and field networking strategy — off-grid Demory farm`](mesh-and-field-networking-strategy-off-grid-demory-farm.md) **,** [`Off-grid degraded modes — power and connectivity`](off-grid-degraded-modes-power-and-connectivity-demory-farm.md) **.**

**Two-site** **WAN** **context** **(**Claxton** **vs** **Demory** **)** **:** [`Execution topology package — two-site smart farm (Mermaid)`](execution-topology-package-two-site-smart-farm.md) **.**

**Mermaid** **:** [`mkdocs.yml`](../../mkdocs.yml) **(**`mermaid2` **plugin** **).**

---

## Legend

| Mark | Meaning |
|------|---------|
| **Pcrit** | **Battery-backed** **“** **keep** **alive** **”** **loads** **(**policy** **—** **placeholder** **list** **)** **.** |
| **Popt** | **Sheddable** **optional** **loads** **(**cameras** **dense** **,** **Starlink** **CPE** **,** **extra** **RF** **)** **.** |
| **Z2** | **Field** **OT** **/** **LAN** **—** **hostile** **lateral** **assumption** **(**[`Remote access`](../analyses/remote-access-operational-security-model-two-site-smart-farm.md)**)** **.** |
| **Z3** | **WAN** **/** **Internet** **—** **untrusted** **.** |
| **Solid** | **Intended** **normal** **path** **.** |
| **Dashed** | **Optional** **/** **sheddable** **.** |

---

## 1. Reference topology — off-grid Demory farm (intended)

```mermaid
flowchart TB
  subgraph PD["Power domain — DC / AC plant (placeholder sizing)"]
    pv["PV array"]
    batt["Battery + BMS\n(Pcrit reserve policy)"]
    inv["Inverter / charger\nAC distribution"]
    pv --> batt
    batt --> inv
  end

  subgraph Pcrit["Pcrit — continuous policy loads"]
    pump["Water / interlock logic\n(local safe defaults)"]
    gw["Field gateway\n(edge buffer)"]
    inv --> pump
    inv --> gw
  end

  subgraph Popt["Popt — optional / sheddable"]
    cpe["Starlink / LTE CPE\n(WAN uplink)"]
    cam["Cameras / NVR\n(policy)"]
    inv -.-> cpe
    inv -.-> cam
  end

  subgraph Z2["Z2 — field LAN / OT"]
    eth["Ethernet / Wi‑Fi AP\n(barn zone)"]
    mesh["Meshtastic / LoRa mesh\n→ gateway"]
    halow["Wi‑Fi HaLow segment\n(optional IP links)"]
    gw --> eth
    gw --> mesh
    eth -.-> halow
  end

  subgraph Z3["Z3 — WAN (optional)"]
    cloud["Cloud / MQTT egress\n(convenience)"]
  end

  cpe -.-> Z3
  gw -.->|"TLS / MQTT"| cloud
```

**Interpretation**: **Networking** **loads** **sit** **inside** **the** **same** **energy** **budget** **as** **pumps** **—** **Starlink** **and** **dense** **video** **are** **Popt** **unless** **you** **promote** **them** **in** **writing** **.** **Mesh** **/** **HaLow** **stay** **below** **WAN** **for** **local** **survivability** **.**

---

## 2. Pilot topology — Phase 0/1 minimum viable

```mermaid
flowchart LR
  subgraph PDp["Power — pilot"]
    pvp["Small PV + battery\n(measure first)"]
    invp["Single inverter / bus"]
    pvp --> invp
  end

  subgraph Z2p["Z2 — field"]
    g1["One gateway"]
    m1["Few mesh nodes\n(tank / gate class)"]
    g1 --> m1
  end

  subgraph WANp["WAN — optional"]
    sp["Starlink or LTE\n(one uplink)"]
  end

  cloudp["Cloud / phone\n(convenience)"]

  invp --> g1
  invp -.-> sp
  sp -.->|"egress when up"| cloudp
```

**Interpretation**: **Prove** **Wh/day** **before** **adding** **HaLow** **infrastructure** **or** **a** **second** **WAN** **path** **(**[`Decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md)**)** **.**

---

## 3. Degraded topology — low SOC and/or WAN loss

```mermaid
flowchart TB
  subgraph stress["Stress — low SOC or charge fault"]
    note["Load shed: Popt first"]
  end

  subgraph Pcritd["Pcrit — may still run if policy allows"]
    pumpd["Interlocks / critical logic"]
    gwd["Gateway (if not shed)"]
  end

  subgraph meshonly["Local-only survivable"]
    meshd["Mesh / LoRa local path\n(no cloud required)"]
    sens["Sensors / actuators\nfail-safe"]
    gwd --> meshd
    meshd --> sens
  end

  subgraph dead["WAN — down or intentionally off"]
    z3d["No cloud trust"]
  end

  stress -.-> Pcritd
  gwd -.->|"blocked"| z3d
```

**Interpretation**: **When** **SOC** **is** **deep** **,** **shed** **Popt** **before** **you** **lose** **pump** **logic** **.** **When** **WAN** **is** **gone** **,** **mesh** **may** **still** **carry** **local** **telemetry** **to** **a** **live** **gateway** **;** **if** **gateway** **is** **shed** **,** **revert** **to** **manual** **rounds** **(**[`Off-grid degraded modes`](off-grid-degraded-modes-power-and-connectivity-demory-farm.md)**)** **.**

---

## Related

- [`Demory farm — site intelligence`](demory-farm-site-intelligence.md)
- [`Two-site smart farm — network topology and WAN/edge reference (Mermaid)`](two-site-smart-farm-network-topology-and-wan-edge-reference.md)
