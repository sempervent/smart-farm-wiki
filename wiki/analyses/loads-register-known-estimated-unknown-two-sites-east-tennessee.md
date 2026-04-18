---
title: Loads register — known, estimated, unknown (two sites)
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - two-site
  - loads
  - power
  - energy
  - execution
review_status: unreviewed
confidence: medium
---

# Loads register — known, estimated, unknown (two sites)

**Purpose**: Single **register** for **electrical** and **major duty-cycled** energy loads at **`SITE_HOME`** and **`SITE_FARM`** so [`Farm on-site power system`](../entities/farm-on-site-power-system.md), [`Utility baseline`](utility-and-service-baseline-two-sites-east-tennessee.md), and **business-plan** **execution** share one table—**without** mixing in **parcel** or **soil** facts.

**Package**: [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md).

**Business plan**: [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) — **energy** **targets** stay in package pages; **here**: **site-specific** **load lines**.

---

## Epistemic classes

| Class | Meaning |
|-------|---------|
| **Measured** | Clamp meter, utility interval data, inverter log |
| **Estimated** | Nameplate × duty cycle—**show math** in notes column |
| **Assumption** | Planning default from equipment plan—**replace** |
| **Unknown** | Not yet identified or metered |

---

## Electrical loads (master table)

| Site | Load ID | Description | Fact class | V / phase | A or W (steady) | Start / surge | Hours/day (season) | Priority (1=critical) | Blocks |
|------|---------|-------------|------------|-----------|-----------------|---------------|---------------------|----------------------|--------|
| SITE_HOME | H-L-001 | Example: well pump | Unknown | TBD | TBD | TBD | TBD | TBD | Inverter/charger sizing |
| SITE_HOME | H-L-002 | Example: HVAC | Unknown | TBD | TBD | TBD | TBD | TBD | Battery kWh |
| SITE_FARM | F-L-001 | Example: irrigation pump | Unknown | TBD | TBD | TBD | TBD | TBD | Solar pump controller |
| SITE_FARM | F-L-002 | Example: barn lights | Unknown | TBD | TBD | — | TBD | TBD | Circuit layout |

*Add rows; **do not** invent amperages—**Unknown** until measured.*

---

## Thermal / non-electric energy (where relevant)

| Site | Load ID | Description | Fact class | Fuel / source | Duty | Blocks |
|------|---------|-------------|------------|-----------------|------|--------|
| SITE_HOME | H-T-001 | Heat / DHW | Unknown | TBD | TBD | Electrification vs propane |
| SITE_FARM | F-T-001 | Water heating for parlor / wash | Unknown | TBD | TBD | Solar thermal vs electric |

---

## Simultaneity and diversity (planning)

| Scenario | Fact class | Assumed overlapping loads | Notes | Blocks |
|----------|------------|----------------------------|-------|--------|
| Winter evening peak (home) | Assumption | TBD | Replace with **measured** stack | Whole-home backup |
| Irrigation + barn (farm) | Unknown | TBD | Field verify | Generator vs grid upgrade |

---

## Decision gates

| Decision | Blocked until |
|----------|----------------|
| Inverter kW | **Surge** + **continuous** for **worst-case** overlapping **measured** loads |
| Battery kWh | **Measured** overnight + **irrigation** window overlap |
| Grid service upgrade | **Utility** **demand** history + **planned** new loads |

---

## Related

- [`Utility and service baseline`](utility-and-service-baseline-two-sites-east-tennessee.md) · [`Infrastructure inventory baseline`](infrastructure-inventory-baseline-two-sites-east-tennessee.md) · [`Site intelligence — Claxton`](claxton-home-base-site-intelligence.md) · [`Site intelligence — Demory`](demory-farm-site-intelligence.md)
