---
title: Homelab backup stack — official captures (restic, Longhorn, farmOS Docker)
page_type: source_note
status: active
created: 2026-04-18
updated: 2026-04-17
source_ids:
  - raw/processed/2026/restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md
  - raw/processed/2026/restic-removing-backup-snapshots-documentation-0-18-1-capture-inbox-2026-04-17.md
  - raw/processed/2026/longhorn-backup-system-capture-inbox-2026-04-17.md
  - raw/processed/2026/longhorn-restore-system-capture-inbox-2026-04-17.md
  - raw/processed/2026/longhorn-documentation-hub-capture-inbox-2026-04-17.md
  - raw/processed/2026/farmos-docker-developing-hosting-capture-inbox-2026-04-17.md
tags:
  - backup
  - restic
  - longhorn
  - farmos
  - kubernetes
review_status: unreviewed
---

# Homelab backup stack — official captures (restic, Longhorn, farmOS Docker)

**Ingest wave**: moved from `raw/inbox/` to stable `raw/processed/2026/*-inbox-2026-04-17.md` (2026-04-18).

## What each file is

| Raw path | Authority | Notes |
|----------|-----------|--------|
| [`restic-backing-up...`](../../raw/processed/2026/restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md) | **restic** user manual (0.18.1) | Backup semantics, `--stdin-from-command`, warning on naive ` \| restic --stdin` masking command failures |
| [`restic-removing...`](../../raw/processed/2026/restic-removing-backup-snapshots-documentation-0-18-1-capture-inbox-2026-04-17.md) | **restic** | Snapshot removal / forget policies |
| [`longhorn-backup-system...`](../../raw/processed/2026/longhorn-backup-system-capture-inbox-2026-04-17.md) | **Longhorn** docs (1.11.1 path in page) | System backup bundle, volume policies, backup target |
| [`longhorn-restore-system...`](../../raw/processed/2026/longhorn-restore-system-capture-inbox-2026-04-17.md) | **Longhorn** docs | System restore flow |
| [`longhorn-documentation-hub...`](../../raw/processed/2026/longhorn-documentation-hub-capture-inbox-2026-04-17.md) | **Longhorn** | Short hub / index capture |
| [`farmos-docker-developing...`](../../raw/processed/2026/farmos-docker-developing-hosting-capture-inbox-2026-04-17.md) | **farmOS.org** (capture) | **Historical v1.x** pattern: `docker-compose` + **MariaDB** sidecar—use for **compose/volume** thinking only; **confirm** current [farmOS hosting](https://farmos.org/hosting) for **farmOS 2.x** (PostgreSQL) before production backup design |

## Synthesis

- [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md)
- [`Backup / DR — official documentation cluster`](backup-dr-official-documentation-cluster.md)
- [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](../analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md)
- [`Restore and recovery tiers — homelab farm systems`](../analyses/restore-recovery-tiers-homelab-farm-systems.md)
- [`Runbook — backup validation and recovery drill`](../analyses/runbook-backup-validation-and-recovery-drill.md)
- [`Kubernetes platform backup / DR — Pi, k3s, Longhorn`](../analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md)
- [`Off-grid implications — backup and networking choices`](../analyses/off-grid-implications-backup-and-networking-choices.md)
- [`K3s / Longhorn / Pi platform captures`](../source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md) (cluster runtime context)
