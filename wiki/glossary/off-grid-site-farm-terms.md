---
title: Off-grid site farm terms (Pcrit, Popt, local-first)
page_type: glossary
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - glossary
  - off-grid
  - demory
review_status: unreviewed
confidence: high
---

# Off-grid site farm terms (Pcrit, Popt, local-first)

For **`SITE_FARM`** when modeled **off-grid-first** (solar + battery default; **WAN optional**):

| Term | Meaning |
|------|---------|
| **Pcrit** | **Battery-backed** loads and controls that should **stay up** through normal **WAN** outages and **short** SOC stress—**policy-defined** list (water head, gateway spine, etc.). |
| **Popt** | **Sheddable** loads: extra **RF**, dense **cameras**, **Starlink** CPE, **shop** gear—**cut** first when SOC is low. |
| **Local-first** | **Sensor → gateway → actuator** and **records** paths work **without internet**; cloud is **overlay**. |
| **DR-*** | **Stop rules** on the farm (e.g. **DR-1** metered network load vs battery)—see [`Off-grid infrastructure stop rules`](../analyses/off-grid-operational-decision-rules-power-and-networking-demory-farm.md). |

**See:** [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md).
