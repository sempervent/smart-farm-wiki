---
title: Edge cluster storage roles — homelab / farm stack
page_type: entity
status: active
created: 2026-04-23
updated: 2026-04-23
tags:
  - storage
  - longhorn
  - k3s
  - backup
  - edge
aliases:
  - Central storage vs distributed storage farm edge
confidence: medium
review_status: unreviewed
---

# Edge cluster storage roles — homelab / farm stack

## Purpose

Stable reference for **where bytes live** in the **farm edge / homelab** stack: **central bulk store** (e.g. NAS), **distributed cluster volumes** (e.g. Longhorn on k3s), **object/backup repositories** (e.g. restic targets), and **ephemeral** local caches on gateways—so analyses can say “PVC tier” or “central store” without re-explaining the whole platform.

## Scope

- **In scope**: Role definitions, backup/DR **implications** at a high level, pointers to doctrine.
- **Out of scope**: Your **hostname**, disk SKU, capacity, or network path—those are deployment tables.

## Knowns

- The wiki treats **logical** DB exports (e.g. PostgreSQL / farmOS) as a distinct concern from **volume** snapshots—see backup package.
- **Hybrid** central + Longhorn patterns are analyzed in the platform cluster.

## Assumptions

- At least one **versioned** recovery path exists for **farm records** (not sync-only mirroring).

## Related analyses

- [`Longhorn vs central storage architecture — homelab / farm platform`](../analyses/longhorn-vs-central-storage-architecture-homelab-farm-platform.md)
- [`Longhorn role in the homelab / farm platform`](../analyses/longhorn-role-in-homelab-farm-platform.md)
- [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md)
- [`Central vs local backup scope — farm edge stack`](../analyses/central-vs-local-backup-scope-farm-edge-stack.md)
- [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md)

## Related source notes

- [`k3s / Longhorn / Rancher / Pi platform — official captures`](../source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md)
- [`homelab backup stack — official captures`](../source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md)

## Outstanding unknowns

- Final **ratio** of central bulk to cluster-backed PVCs for your fleet size and power budget.
- Whether **single-site** loss requires a documented **restore ordering** beyond the generic DR package (operator worksheet).
