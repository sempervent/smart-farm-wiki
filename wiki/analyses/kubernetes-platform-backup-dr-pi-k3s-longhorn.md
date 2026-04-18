---
title: Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn
page_type: analysis
page_subtype: operational_guide
operational_maturity: pilot_ready
status: active
created: 2026-04-18
updated: 2026-04-24
tags:
  - backup
  - k3s
  - longhorn
  - kubernetes
review_status: reviewed
confidence: high
---

# Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn

## Purpose

**Integration page**: maps **parallel backup tracks** (application logical, Longhorn volume/system, etcd, Rancher, secrets) to the **k3s + Longhorn** platform described in [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md). Sits **on top of** generic [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md) and [`Restore and recovery tiers`](restore-recovery-tiers-homelab-farm-systems.md).

**When things go wrong**: follow [`Disaster recovery decision rules — farm edge stack`](disaster-recovery-decision-rules-farm-edge-stack.md) for **restore order** and failure classification.

**Canonical package**: [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md).

**Longhorn operator docs (captures)**: [`Longhorn system backup`](../../raw/processed/2026/longhorn-backup-system-capture-inbox-2026-04-17.md), [`Longhorn system restore`](../../raw/processed/2026/longhorn-restore-system-capture-inbox-2026-04-17.md), [`homelab backup stack source note`](../source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md). **k3s / Rancher pointers**: [`backup-dr link batch`](../../raw/processed/2026/backup-dr-official-documentation-links-batch-2026-04-17.md).

---

## Parallel tracks (do not conflate)

| Track | Protects | Mechanism |
|-------|------------|----------------------------|
| **A. Application data** | farmOS DB, broker state | Logical dumps (`pg_dump` class) via restic `--stdin-from-command` ([`restic capture`](../../raw/processed/2026/restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md)); see **comparison** page |
| **B. Longhorn volumes** | PVC block data | Volume backups + CSI snapshots; **system backup** bundle for Longhorn metadata ([`backup system capture`](../../raw/processed/2026/longhorn-backup-system-capture-inbox-2026-04-17.md)) |
| **C. Cluster etcd / k3s state** | Control plane | Embedded etcd: [k3s backup and restore](https://docs.k3s.io/datastore/backup-restore), [etcd-snapshot](https://docs.k3s.io/cli/etcd-snapshot); external datastore: follow [k3s datastore](https://docs.k3s.io/datastore) docs |
| **D. Rancher** (if installed) | Rancher app state on cluster | [Rancher backup/restore usage](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/backup-restore-and-disaster-recovery/back-up-restore-usage-guide); encryption config must be **saved** outside the operator’s artifacts |
| **E. Configuration and secrets** | Helm values, GitOps, secrets | **Not** automatically solved by etcd snapshots for every policy—Sealed Secrets / SOPS / external KMS; **govern** access to snapshot stores that contain **Secret** objects ([Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)) |

**Rule**: **B** without **A** can still lose application consistency if database files were dirty at snapshot time—keep logical exports for farm records unless you accept crash recovery and have restore-tested that path.

**Rule**: **D** is **in addition to** **C** when Rancher manages clusters; version-match restore targets per Rancher docs.

---

## Optional HA patterns (storage)

- **Longhorn** **replicated** **volumes** **across** **nodes** **:** **survive** **single** **node** **loss** **on** **LAN**—not **off-site** **DR** **alone**.
- **Backup target** **to** **central** **NAS** **or** **object** **store** **:** **off-site** **copy** **still** **needed** **for** **site** **loss**.

---

## Related

- [`Disaster recovery decision rules — farm edge stack`](disaster-recovery-decision-rules-farm-edge-stack.md)
- [`Raspberry Pi k3s fleet — backup and restore sequence`](raspberry-pi-k3s-fleet-backup-and-restore-sequence.md) (operational ordering: app dumps → Longhorn → etcd)
- [`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md)
- [`Central vs local backup scope — farm edge stack`](central-vs-local-backup-scope-farm-edge-stack.md)
- [`Off-grid implications — backup and networking choices`](off-grid-implications-backup-and-networking-choices.md)
- [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md)
- [`Platform strategy for farm and homestead services`](homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md)
