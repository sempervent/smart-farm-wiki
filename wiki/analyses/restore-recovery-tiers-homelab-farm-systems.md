---
title: Restore and recovery tiers — homelab farm systems
page_type: analysis
page_subtype: operational_guide
operational_maturity: pilot_ready
status: active
created: 2026-04-18
updated: 2026-04-24
tags:
  - backup
  - disaster-recovery
  - farmos
  - homelab
review_status: reviewed
confidence: high
---

# Restore and recovery tiers — homelab farm systems

## Purpose

Define **tiered recovery** expectations for **farm records** (farmOS / DB), **container hosts**, and **cluster storage**—using **labels** (Tier 0–3). **RPO/RTO** are **operator-defined** targets filled after **restore drills**, not invented by the wiki.

**Doctrine role**: Canonical **tier vocabulary** for the package—pair with [`Disaster recovery decision rules`](disaster-recovery-decision-rules-farm-edge-stack.md) for **when** to invoke each tier.

**Sources**: [`homelab backup stack — official captures`](../source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md).

**Canonical package**: [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md).

---

## RPO and RTO expectations (worksheet)

**Recovery Point Objective (RPO)**: maximum **acceptable age** of data you are willing to **lose** (e.g. “last successful nightly dump” vs “15-minute WAL shipping”—only the former is assumed here unless you document otherwise).

**Recovery Time Objective (RTO)**: maximum acceptable downtime to bring minimum usable farm records or telemetry back online (typically hours to days by tier below).

| Workload | Tier target (below) | RPO (you fill) | RTO (you fill) | Last drill date |
|----------|---------------------|----------------|----------------|-----------------|
| farmOS / PostgreSQL logical | 2 | e.g. 24 h | e.g. 8 h | |
| Longhorn volume(s) for app PVC | 1–2 | | | |
| k3s etcd / control plane | 3 | | | |
| Rancher (if deployed) | 3 | | | |
| Edge gateway config (non-Git) | 1 | | | |

**Rule**: Targets without a dated restore drill per [`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md) are aspirational only.

---

## Tier definitions (operational)

| Tier | Scope | Restore speed (typical) | Complexity | Retention behavior (typical) | Encryption |
|------|--------|-------------------------|------------|------------------------------|------------|
| **0 — Working state** | Live service; **no** restore | N/A | N/A | N/A | TLS in transit as deployed |
| **1 — File / volume rollback** | **One** PVC, bind mount, or VM disk from **restic** or Longhorn snapshot | **Hours** (operator available) | **Low–medium**—mount + verify | **Snapshot** count + **forget** policy ([`restic` remove docs](../../raw/processed/2026/restic-removing-backup-snapshots-documentation-0-18-1-capture-inbox-2026-04-17.md)) | restic **repo** encryption; Longhorn **backup target** TLS |
| **2 — Database logical restore** | **`pg_dump` / vendor dump** into clean DB | **Hours** | **Medium**—schema/version match | **Daily**/**weekly** dumps per policy | Same as backup medium |
| **3 — Platform DR** | **Longhorn system backup/restore** + **rebuild** cluster | **Days** | **High**—ordering, CRDs, targets | **Infrequent** **full** platform bundles | Cluster **secrets** + backup store **ACLs** |

**Rule**: **Tier 3** without **Tier 2** for the **same** app data can produce **empty** “healthy” clusters—always keep a **logical** farm data path for farmOS-class systems unless you have proven **consistent** volume-level procedures.

---

## What to drill (minimum)

1. **Restore one restic snapshot** to scratch storage (verify files, not just `restic check`).
2. **Restore DB** from latest **logical** dump to a **staging** DB and run farmOS **update**/**migrate** per project docs.
3. **Longhorn** (if used): walkthrough **backup target** failure and **re-auth** procedure from [`longhorn backup` capture](../../raw/processed/2026/longhorn-backup-system-capture-inbox-2026-04-17.md).

---

## Related

- [`Disaster recovery decision rules — farm edge stack`](disaster-recovery-decision-rules-farm-edge-stack.md)
- [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md)
- [`Central vs local backup scope — farm edge stack`](central-vs-local-backup-scope-farm-edge-stack.md)
- [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md)
- [`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md)
- [`Automation degraded modes SOP`](automation-degraded-modes-manual-fallback-sop.md) — when “cloud is wrong” overlaps with “restore in progress.”
- [`Off-grid implications — backup and networking choices`](off-grid-implications-backup-and-networking-choices.md)
