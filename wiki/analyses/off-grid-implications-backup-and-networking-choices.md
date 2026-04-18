---
title: Off-grid implications — backup and networking choices
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-18
tags:
  - off-grid
  - backup
  - networking
review_status: unreviewed
confidence: medium
---

# Off-grid implications — backup and networking choices

## Purpose

Connect **solar + battery** field reality to **(1)** where backups can run reliably and **(2)** how **HaLow / mesh / WAN** choices affect **whether** backups complete—without duplicating full power pages.

**Canonical power**: [`Off-grid power strategy — Demory farm site`](off-grid-power-strategy-demory-farm-site.md). **Decision rules**: [`Off-grid operational decision rules`](off-grid-operational-decision-rules-power-and-networking-demory-farm.md).

---

## Backup scheduling vs energy

| Topic | On-grid homelab | Off-grid farm |
|-------|-----------------|---------------|
| **Large restic jobs** | Run nightly | Prefer **high solar surplus** window or **genset** policy—**avoid** deep **SOC** discharge for hours-long jobs unless budgeted |
| **Longhorn backup to cloud** | Depends on **WAN** | **Same**, plus **WAN** may be **Starlink**—**degraded** when weather hits—**local** target may be safer ([`restore tiers`](restore-recovery-tiers-homelab-farm-systems.md)) |
| **Edge gateway** | Stable | **Size** **battery** for **always-on** **backup** **agent** **or** **accept** **manual** **trigger** |

---

## Networking vs backup path

- **HaLow / mesh** **local-only**: backups **can** **queue** **at** **gateway** **until** **WAN** **returns**—design **queue** **disk** **and** **retention** **explicitly**.
- **No WAN**: **Tier 2** **logical** **dumps** **to** **removable** **media** **still** **work**—**tier** **3** **cloud** **restore** **does** **not**.

---

## Related

- [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md)
- [`Sub-GHz Wi‑Fi (HaLow) — farm sensors deployment guide`](subghz-wi-fi-halow-farm-sensors-deployment-guide.md)
