---
title: Backup and restore tier labels — farm stack
page_type: entity
status: active
created: 2026-04-23
updated: 2026-04-24
tags:
  - backup
  - disaster-recovery
  - farmos
  - operational-model
aliases:
  - Tier 0 1 2 3 restore labels
confidence: medium
review_status: unreviewed
---

# Backup and restore tier labels — farm stack

## Purpose

Durable **labels** for **Tier 0–3** recovery expectations used across **farm records**, **volumes**, and **platform** rebuilds—so pages can say “Tier 2 path” without pasting the tier table.

## Scope

- **In scope**: What each **tier** means **operationally**; pointers to **RPO/RTO** as **operator-filled** worksheets.
- **Out of scope**: Numeric SLAs invented by the wiki; **your** drill dates (those belong in runbooks / evidence).

## Knowns

- **Tier 0** is **live** state (no restore).
- **Tier 1** is typically **file/volume** rollback (restic/Longhorn-class).
- **Tier 2** is **logical DB / app** restore (e.g. `pg_dump` class).
- **Tier 3** is **platform DR** (cluster/storage rebuild ordering).

## Assumptions

- **Tier 3** without a **Tier 2**-class path for the **same** app data can yield an “empty healthy” system—see canonical warning in restore tiers analysis.

## Related analyses

- [`Disaster recovery decision rules — farm edge stack`](../analyses/disaster-recovery-decision-rules-farm-edge-stack.md) — **when** to apply each tier in an incident
- [`Restore and recovery tiers — homelab farm systems`](../analyses/restore-recovery-tiers-homelab-farm-systems.md)
- [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md)
- [`Runbook — backup validation and recovery drill`](../analyses/runbook-backup-validation-and-recovery-drill.md)
- [`Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn`](../analyses/kubernetes-platform-backup-dr-pi-k3s-longhorn.md)

## Related source notes

- [`Backup / DR — official documentation cluster`](../source-notes/backup-dr-official-documentation-cluster.md)

## Outstanding unknowns

- **Dated** restore drill outcomes per tier (evidence gap until runbooks are exercised).
