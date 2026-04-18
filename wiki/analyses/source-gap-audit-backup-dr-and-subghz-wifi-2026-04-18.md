---
title: Source gap audit — backup/DR vs sub-GHz Wi‑Fi (homelab + farm)
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-18
tags:
  - ingest
  - backup
  - halow
  - farmos
review_status: unreviewed
confidence: medium
---

# Source gap audit — backup/DR vs sub-GHz Wi‑Fi (homelab + farm)

## Purpose

Short **evidence map** for what the vault **had** vs **needed** to answer decision-safe questions on **(1)** farmOS/homelab backup strategy and **(2)** sub-GHz Wi‑Fi (802.11ah / HaLow) for farm sensors—without fabricating operator procedures.

---

## 1. Backup strategy comparison pages

| Category | Previously in vault | Gap | Addressed in this wave |
|----------|---------------------|-----|-------------------------|
| **Logical DB backup into object-style repos** | Generic PostgreSQL primers; no restic operator capture | Official **restic** patterns for `--stdin-from-command` (e.g. DB dumps) and snapshot hygiene | [`restic` captures](../../raw/processed/2026/restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md), [`restic removing snapshots`](../../raw/processed/2026/restic-removing-backup-snapshots-documentation-0-18-1-capture-inbox-2026-04-17.md) + [`source note`](../source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md) |
| **Kubernetes / CSI volume backup** | Homelab narratives; no Longhorn operator capture | Longhorn **system backup** / **restore** bundle semantics | [`longhorn` captures](../../raw/processed/2026/longhorn-backup-system-capture-inbox-2026-04-17.md) etc. + same source note |
| **farmOS + containers** | farmOS model docs; overview | **Docker** development/hosting capture for **compose + DB sidecar** pattern (epistemic: **v1/MariaDB** era in capture) | [`farmOS Docker capture`](../../raw/processed/2026/farmos-docker-developing-hosting-capture-inbox-2026-04-17.md) |
| **farmOS 2.x PostgreSQL specifics** | Hosting links in overview, not full backup runbook | **Still partial**—confirm current **farmOS.org/hosting** for DB engine and backup expectations; wiki synthesis cites **patterns**, not a single blessed command | Called out in [`backup strategy comparison`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md) |

**Remaining gaps (explicit)**

- **Official farmOS backup/restore chapter** as a dedicated processed capture (optional future ingest).
- **PostgreSQL** vendor backup docs (e.g. continuous archiving) if the deployment moves beyond single-instance compose.
- **Immutable air-gapped** tape/object-lock patterns for compliance—out of scope unless sources added.

---

## 2. Sub-GHz Wi‑Fi / HaLow how-to pages

| Category | Previously in vault | Gap | Addressed |
|----------|---------------------|-----|-----------|
| **802.11ah / HaLow concept** | [`Wi‑Fi HaLow` concept](../concepts/wi-fi-halow.md), multiple article captures | Consolidated **how-to** narrative | [`Sub-GHz Wi‑Fi farm sensors — deployment guide`](subghz-wi-fi-halow-farm-sensors-deployment-guide.md) |
| **Deployment / bridge patterns** | Silex-style PoC capture | Step-level outline + **constraints** | Cites [`how-to 10x reach HaLow`](../../raw/processed/2026/how-to-10x-the-reach-of-wi-fi-devices-with-wi-fi-halow-802-11ah-inbox-2026-04-23.md) |
| **vs LoRa / Meshtastic** | [`Meshtastic vs HaLow vs Wi‑Fi`](../comparisons/meshtastic-wi-fi-halow-conventional-wi-fi-off-grid-farm-operations.md), LoRaWAN vs Meshtastic | **Four-way** field-network table including **LoRaWAN** | [`Wi‑Fi HaLow vs LoRaWAN vs Meshtastic vs conventional Wi‑Fi`](../comparisons/wi-fi-halow-lorawan-meshtastic-conventional-wi-fi-farm-field-networking.md) |
| **IEEE / chipset datasheets** | Morse Micro etc. in off-grid index | No new PDFs in this inbox wave; **still** rely on existing cluster | [`Off-grid power/RF source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) |

**Remaining gaps**

- **Regulatory domain / channel plan** per country—must be verified for **your** jurisdiction at deploy time.
- **Vendor-specific** OpenWrt/build guides as processed captures if a chosen CPE is fixed.

---

## Related

- [`Homelab backup stack — official captures (source note)`](../source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md)
- [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md)
- [`Off-grid implications — backup and networking choices`](off-grid-implications-backup-and-networking-choices.md)
