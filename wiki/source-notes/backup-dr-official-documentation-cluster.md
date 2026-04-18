---
title: Backup / DR — official documentation cluster (k3s, Longhorn, Rancher, PostgreSQL, farmOS)
page_type: source_note
status: active
created: 2026-04-17
updated: 2026-04-18
source_ids:
  - raw/processed/2026/backup-dr-official-documentation-links-batch-2026-04-17.md
review_status: unreviewed
tags:
  - backup
  - disaster-recovery
  - k3s
  - longhorn
  - rancher
  - postgresql
  - farmos
---

# Backup / DR — official documentation cluster (k3s, Longhorn, Rancher, PostgreSQL, farmOS)

## Evidence summary

| Field | Content |
|-------|---------|
| **Abstract** | Curated **official-doc** link batch plus **vault captures** (restic, Longhorn, farmOS Docker era) that anchor the **backup/restore** narrative for the **homelab / farm** stack. |
| **Authority mix** | **Vendor primary** (k3s, Longhorn, Rancher, PostgreSQL, farmOS upstream) + **project docs**; captures are **time-stamped**. |
| **Decision relevance** | Informs **parallel restore tracks** (app vs etcd vs volumes), **restic** vs **volume** scope, and **DR drill** expectations—see DR package. |
| **Canonical wiki links** | [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) · [`Backup and disaster recovery — doctrine hub`](../topics/backup-disaster-recovery-doctrine-hub.md) · [`Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn`](../analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md) |

**Key claims** (public-safe):

- **etcd** and **control-plane** backup semantics are **distinct** from **Longhorn volume** replication; the DR package states **restore order** and **failure classes**.
- **farmOS** backup posture depends on **DB + files**; captures may reflect an older **Docker** dev pattern—treat as **provenance**, not current deployment truth alone.

**Open questions / follow-ups**

- Re-validate **farmOS** backup against **your** deployment (version, storage, compose vs k8s) before production reliance.

**Purpose**: **Provenance hub** for **official** backup and restore documentation **pointers** plus vault **captures** used by the **canonical DR package** in `wiki/analyses/`.

---

## Curated link batch (processed)

- [`backup-dr-official-documentation-links-batch-2026-04-17.md`](../../raw/processed/2026/backup-dr-official-documentation-links-batch-2026-04-17.md) — k3s etcd backup/restore, Rancher manager docs, PostgreSQL manual, cross-links to Longhorn/restic/farmOS.

---

## Captures already in the vault (excerpts)

- [`Homelab backup stack — official captures (restic, Longhorn, farmOS Docker)`](homelab-backup-stack-official-captures-inbox-2026-04-18.md) — restic 0.18.1, Longhorn system backup/restore, farmOS Docker **historical** dev pattern.

---

## Synthesis (canonical)

- [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) — **Start here** for navigation.
- [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](../analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md)
- [`Restore and recovery tiers — homelab farm systems`](../analyses/restore-recovery-tiers-homelab-farm-systems.md)
- [`Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn`](../analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md)
- [`Central vs local backup scope — farm edge stack`](../analyses/central-vs-local-backup-scope-farm-edge-stack.md)
- [`Runbook — backup validation and recovery drill`](../analyses/runbook-backup-validation-and-recovery-drill.md)
