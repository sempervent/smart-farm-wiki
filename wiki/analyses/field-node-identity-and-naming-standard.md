---
title: Field node identity and naming standard
page_type: analysis
page_subtype: standard
operational_maturity: pilot_ready
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - field-network
  - telemetry
  - standards
review_status: reviewed
confidence: high
---

# Field node identity and naming standard

## Purpose

**Stable** **identity** and **naming** for **field** **radios**, **sensors**, and **gateways** so **inventory**, **SoR**, and **runbooks** stay aligned—maps to **architecture** **classes** **G/R/S/H/W** ([`Field node classes (G/R/S/H/W)`](../entities/field-node-classes-off-grid-farm-roles.md)), not vendor SKUs.

**Spatial registry**: [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md).

---

## Standard

| # | Rule |
|---|------|
| 1 | **Every** **deployed** **field** **node** has a **unique** **wiki-stable** **ID** (matches **farmOS** / **telemetry** **registry** **when** **integrated**). |
| 2 | **Names** encode **site** **and** **role**: e.g. `{SITE}-{class}-{seq}` (`DEM-G-01`, `CLX-S-12`)—**document** **your** **separator** **rules** **once** **and** **reuse**. |
| 3 | **Refit** **/** **swap** **hardware** **without** **reusing** **IDs** **for** **a** **different** **physical** **device**—use **supersedes** **or** **retired** **flag** in **inventory**. |
| 4 | **G/R/S/H/W** **class** **letter** **appears** **in** **name** **or** **label** **table**—**never** **ambiguous** **“gateway”** **alone**. |

**Off-grid doctrine**: [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md).

---

## Related

- [`RF and telemetry gateway roles — field network`](../entities/rf-telemetry-gateway-roles-field-network.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)
