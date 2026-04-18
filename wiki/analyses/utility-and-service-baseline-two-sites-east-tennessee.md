---
title: Utility and service baseline — both sites
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - two-site
  - utilities
  - electric
  - water
  - execution
review_status: unreviewed
confidence: medium
---

# Utility and service baseline — both sites

**Scope**: **Accounts**, **providers**, **rate classes**, **metering**, **billing** touchpoints, **communications**—per **`SITE_HOME`** and **`SITE_FARM`**. **Not** physical pipe/fence inventory (see [`Infrastructure inventory baseline`](infrastructure-inventory-baseline-two-sites-east-tennessee.md)).

**Package**: [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md).

**Rule**: **Account numbers** and **exact rates** belong in **`raw/`** redacted exports or secure notes—**here**: **provider**, **service type**, **fact class**, **what’s unknown**.

---

## Epistemic classes

| Class | Use |
|-------|-----|
| **Measured** | Bill kWh, demand charges, your meter photo |
| **Reported** | Tariff sheet, provider quote |
| **Assumption** | Placeholder for planning |
| **Unknown** | Confirm with bill or call |

---

## Electric (grid)

| Site | Fact class | Provider / co-op | Service identifier | Voltage / phase | Meter type | Net metering / standby | Last bill review | Blocks |
|------|------------|-------------------|---------------------|-------------------|------------|-------------------------|------------------|--------|
| SITE_HOME | Unknown | TBD | TBD | Unknown | Unknown | Unknown | — | Backup interconnection rules, demand |
| SITE_FARM | Unknown | TBD | TBD | Unknown | Unknown | Unknown | — | Pump motor sizing, TOU if any |

---

## Electric (on-site generation / backup)

| Site | Fact class | Asset | kW / kWh nameplate | Interconnection / transfer | Fuel / maintenance | Blocks |
|------|------------|-------|---------------------|----------------------------|---------------------|--------|
| SITE_HOME | Unknown | Generator / solar / inverter TBD | TBD | Unknown | Unknown | Code compliance, [`loads`](loads-register-known-estimated-unknown-two-sites-east-tennessee.md) |
| SITE_FARM | Unknown | TBD | TBD | Unknown | Unknown | Irrigation overlap |

---

## Water (utility vs well)

| Site | Fact class | Source type | Provider / permit # | Meter / allocation | Quality test date | Blocks |
|------|------------|-------------|---------------------|---------------------|-------------------|--------|
| SITE_HOME | Unknown | Utility vs well TBD | TBD | Unknown | Unknown | Domestic + irrigation design |
| SITE_FARM | Unknown | Well(s) TBD | Well permit / log in `raw/` when filed | Unknown | Unknown | Livestock health, treatment |

---

## Wastewater / septic

| Site | Fact class | System type | Last inspection | Capacity vs occupancy / visitors | Blocks |
|------|------------|-------------|-----------------|----------------------------------|--------|
| SITE_HOME | Unknown | TBD | Unknown | Unknown | Event hosting, guest housing |
| SITE_FARM | Unknown | TBD (if any) | Unknown | Worker facilities | Compliance |

---

## Solid waste / recycling

| Site | Fact class | Hauler / county | Cart size | Special waste (tires, oil) | Blocks |
|------|------------|-----------------|-----------|----------------------------|--------|
| SITE_HOME | Unknown | TBD | Unknown | Unknown | On-farm disposal vs haul |
| SITE_FARM | Unknown | TBD | Unknown | Carcass / large metal TBD | Biosecurity |

---

## Communications (operations)

| Site | Fact class | ISP / cellular | Backup path | Farm data (sensors) | Blocks |
|------|------------|----------------|-------------|---------------------|--------|
| SITE_HOME | Unknown | TBD | TBD | Unknown | Remote monitoring design |
| SITE_FARM | Unknown | TBD | Mesh / LoRa TBD | Unknown | [`Mesh and field networking — off-grid Demory`](mesh-and-field-networking-strategy-off-grid-demory-farm.md); [`Field network IoT comparisons`](../topics/field-network-iot-comparisons.md) |

---

## Fuel and bulk deliveries

| Site | Fact class | Fuel type | Tank / storage | Delivery access | Blocks |
|------|------------|-----------|------------------|-----------------|--------|
| SITE_HOME | Unknown | Propane / diesel TBD | Unknown | Unknown | Generator runtime |
| SITE_FARM | Unknown | Diesel / off-road TBD | Unknown | Unknown | Tractor hours plan |

---

## Insurance / liability (utility-related)

| Item | Fact class | Carrier / policy area | Flood / fence / livestock | Notes |
|------|------------|----------------------|----------------------------|-------|
| SITE_HOME | Unknown | TBD | Unknown | — |
| SITE_FARM | Unknown | TBD | Unknown | — |

---

## Decision gates

| Decision | Blocked until |
|----------|----------------|
| Grid-tie solar size / export | **Measured** usage + **provider** rules + panel capacity |
| Well vs utility expansion | **Reported** permit + **measured** seasonal gpm |
| Comms architecture | **Measured** signal maps + bill for bandwidth |

---

## Related

- [`Loads register`](loads-register-known-estimated-unknown-two-sites-east-tennessee.md) · [`Execution dossier hub`](../analyses/execution-dossier-hub-phase-0-1-east-tennessee.md) · [`Missing data register`](claxton-and-demory-missing-data-register.md)
