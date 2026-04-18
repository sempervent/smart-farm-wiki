---
title: Backup and disaster recovery — doctrine hub
page_type: topic
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - backup
  - disaster-recovery
  - navigation
  - farmos
  - k3s
review_status: unreviewed
confidence: high
---

# Backup and disaster recovery — doctrine hub

**Purpose**: **Router** for **backup / restore / DR** across **farm records** (farmOS / PostgreSQL), **Kubernetes** (k3s, etcd), **cluster storage** (Longhorn), **Rancher**, **secrets**, and **edge** scope—so readers land on the **canonical spine** first instead of skimming dozens of analyses.

**What this hub owns**: **Navigation** (labels, read order, “which page is authoritative for X?”). It does **not** duplicate the DR package prose or invent RPO/RTO numbers.

**What it does not own**: Per-site **cron schedules**, **bucket names**, or **restore drill dates**—those stay in operator runbooks and evidence.

---

## Start here

| Reader goal | Open |
|-------------|------|
| **Full doctrine** (backup vs sync, tiers, parallel tracks, read order) | [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) — **canonical spine** (`page_subtype: operational_guide`) |
| **Incident: what to restore first** | [`Disaster recovery decision rules — farm edge stack`](../analyses/disaster-recovery-decision-rules-farm-edge-stack.md) |
| **Prove backups work** | [`Runbook — backup validation and recovery drill`](../analyses/runbook-backup-validation-and-recovery-drill.md) |
| **Official doc pointers + vault captures** | [`Backup / DR — official documentation cluster`](../source-notes/backup-dr-official-documentation-cluster.md) |

---

## Canonical (durable scope)

| Page | Role |
|------|------|
| [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) | **Navigation spine**, package map, non-negotiable distinctions, **read order** |
| [`Restore and recovery tiers — homelab farm systems`](../analyses/restore-recovery-tiers-homelab-farm-systems.md) | Tier 0–3 **labels**; RPO/RTO worksheet |
| [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](../analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md) | Logical vs volume vs container patterns |
| [`Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn`](../analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md) | **Integration**: parallel tracks (app / Longhorn / etcd / Rancher / secrets) |
| [`Disaster recovery decision rules — farm edge stack`](../analyses/disaster-recovery-decision-rules-farm-edge-stack.md) | Failure classes, restore **order**, execution alignment |

**Entities (vocabulary)**: [`Backup and restore tier labels — farm stack`](../entities/backup-restore-tier-labels-farm-stack.md), [`Edge cluster storage roles — homelab / farm stack`](../entities/edge-cluster-storage-roles-homelab-farm.md).

---

## Supporting analyses and sequences

| Page | Role |
|------|------|
| [`Central vs local backup scope — farm edge stack`](../analyses/central-vs-local-backup-scope-farm-edge-stack.md) | What must be **central** vs **queued at edge** |
| [`Raspberry Pi k3s fleet — backup and restore sequence`](../analyses/raspberry-pi-k3s-fleet-backup-and-restore-sequence.md) | Ordered steps with platform guide |
| [`Off-grid implications — backup and networking choices`](../analyses/off-grid-implications-backup-and-networking-choices.md) | Power/WAN vs backup windows |
| [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](../analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) | Provisioning context (backup chapter inline) |

---

## Related hubs

- [`Platform doctrine package — homelab / farm edge`](platform-doctrine-package-homelab-farm-edge.md) — where **state** lives before you back it up
- [`Off-grid power and field networking hub`](off-grid-power-and-field-networking-hub.md) — when **WAN/power** affects backup scheduling
- [`Two-site smart farm operations`](two-site-smart-farm-operations.md) — cross-links to DR in **Telemetry** / **Resilience** rows
- [`Wiki navigation and structural hubs`](wiki-navigation-and-structural-hubs.md) — meta router
