---
title: Backup strategy comparison — farmOS, homelab, PostgreSQL, containers
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-17
tags:
  - backup
  - farmos
  - postgresql
  - homelab
review_status: unreviewed
confidence: medium
---

# Backup strategy comparison — farmOS, homelab, PostgreSQL, containers

## Purpose

**Decision-safe** comparison of **backup granularities** for **farmOS-class** stacks (Drupal + DB), **PostgreSQL** services, **containers**, and **Kubernetes volumes**—grounded in **ingested operator docs**, not a single vendor recipe.

**Sources**: [`homelab backup stack — official captures`](../source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md) · [`Backup / DR — official documentation cluster`](../source-notes/backup-dr-official-documentation-cluster.md). **Gap context**: [`source gap audit`](source-gap-audit-backup-dr-and-subghz-wifi-2026-04-18.md).

**Canonical package**: [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md) — navigation spine, backup vs sync, volume vs app-aware restore.

**Epistemic**: **farmOS 2.x** uses **PostgreSQL** per current project hosting materials; the processed **Docker** capture in this wave documents an older **7.x / MariaDB** dev pattern—treat it as evidence of **compose + DB sidecar + volumes**, then **verify** your installed major version before choosing `mysqldump` vs `pg_dump`.

---

## Backup vs synchronization (do not conflate)

| Backup | Synchronization / mirroring |
|--------|-----------------------------|
| Point-in-time copies for rollback and disaster recovery (snapshots, restic generations, logical dumps) | Continuous or near-real-time replication for availability or convenience |
| Versioned retention (`forget` policies, snapshot schedules) | Often last-writer-wins or bidirectional conflict rules—poor substitute for “undo last Tuesday” unless you also have versioned backups |
| Validated by restore drills ([`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md)) | Validated by replication lag—not the same as application-consistent recovery |

**Rule**: Treat Syncthing / rsync / mirror jobs as sync, not backup, unless you add immutable history (snapshots, versioned object store) and test restores.

---

## Volume / filesystem backup vs application-consistent restore

| Approach | Captures | Restore risk |
|----------|----------|----------------|
| Logical dump (`pg_dump`, vendor export) | Coherent transactions for one database | Lower risk for farm-record portability |
| Volume snapshot (Longhorn, LVM, SAN) | Fast whole-PVC or whole-disk rollback | PostgreSQL + Drupal need crash recovery or quiesce—dirty snapshots can mean long replay or failure |
| File-level copy of `/var/lib/postgresql` | Physical data directory | High risk unless cold or PostgreSQL base-backup procedure per manual |

**Rule**: For **farmOS**, keep a **logical** path (Tier 2 in [`Restore and recovery tiers`](restore-recovery-tiers-homelab-farm-systems.md)) even if you also use Longhorn volume backups.

---

## Comparison table (granularity vs mechanism)

| Strategy | What is captured | Typical restore complexity | Encryption / security (typical) | Infra assumptions | farmOS fit | Edge / gateway fit | Off-grid farm fit |
|----------|------------------|----------------------------|-----------------------------------|-------------------|------------|--------------------|---------------------|
| **A. Logical DB dump** (`pg_dump` / `mysqldump` stream) | **Coherent SQL** or custom format for **one** DB | **Medium**—restore DB, then app version compatibility | **At rest**: repo encryption if tool supports (e.g. restic); **in flight**: trust pipe/host | Scheduled job, credentials to DB | **Strong** when farmOS is the main state | **OK** if DB reachable from backup host | **Good**—small objects, can run **during** generator hours |
| **B. restic file backup of `/var/lib/postgresql`** | **Data directory** (physical) | **High**—version match, must be **cold** or **PG-aware** | restic **repo** encryption common | Filesystem access; **risk** if DB running—prefer A or vendor procedure | **Discouraged** unless you follow **PostgreSQL** cold/consistent rules | Same | **Risky** on flaky power—corruption risk if not quiesced |
| **C. restic `backup --stdin-from-command`** | **Stdout of dump command** | **Medium**—same as A; **avoids** masking dump errors if used as documented | Same as A | restic + dump binary in same execution context | **Recommended pattern** to study—restic documents **`mysqldump`**; **analogue** to `pg_dump` for PG | **Works** at hub | **Works** if scheduler + power stable |
| **D. Docker volume / bind-mount copy** | **Files** under `www`, `db` dirs | **Medium–high**—consistent with compose stop/start | Filesystem + optional restic | Compose layout known | Matches **dev** capture pattern | Common on single-node edge | **OK** with explicit **stop** windows |
| **E. Longhorn volume backup** (K8s) | **CSI** volume snapshots to **backup target** | **Medium–high**—cluster restore story | Backup target **TLS** + credentials; **not** a substitute for **secrets** rotation | **Kubernetes** + Longhorn + remote target | farmOS **as workload on PVC**—**app-level** backup still often needed for **portable** restore | **Gateway** workloads on cluster | **Power + WAN** to object store—see [`off-grid implications`](off-grid-implications-backup-and-networking-choices.md) |
| **F. Longhorn system backup** | **CRDs + PV/PVC metadata** bundle (not full cluster) | **High**—disaster **platform** story | Remote backup store | Longhorn configured; see capture **limitations** (e.g. nodes) | **Complements** E for **platform** DR | Same | Same |

**restic warning (verbatim pattern)**: Piping a dump into restic with plain `--stdin` **without** `--stdin-from-command` can **hide dump failures** and produce **empty** snapshots—see [`restic backing up` capture](../../raw/processed/2026/restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md) (section on `--stdin` vs `--stdin-from-command`).

---

## farmOS-specific notes

- **Authoritative product** hosting and upgrade path: confirm on [farmOS.org](https://farmOS.org/) (external)—wiki does not mirror full hosting guide.
- **System of record**: align backup scope with [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md)—**MQTT** is usually **not** the canonical farm record store unless you explicitly chose that.

---

## Related

- [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md)
- [`Central vs local backup scope — farm edge stack`](central-vs-local-backup-scope-farm-edge-stack.md)
- [`Restore and recovery tiers — homelab farm systems`](restore-recovery-tiers-homelab-farm-systems.md)
- [`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md)
- [`Kubernetes platform backup / DR — Pi, k3s, Longhorn`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md) (CSI + etcd context)
- [`Raspberry Pi k3s fleet — backup and restore sequence`](raspberry-pi-k3s-fleet-backup-and-restore-sequence.md) (stepwise sequence aligned to this comparison)
- [`farmOS` entity](../entities/farmos.md)
- [`farmOS vs lightweight stack`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md)
