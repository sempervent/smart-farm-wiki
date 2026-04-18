---
title: Runbook — backup validation and recovery drill
page_type: analysis
page_subtype: operational_guide
operational_maturity: pilot_ready
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - backup
  - disaster-recovery
  - runbook
  - homelab
review_status: unreviewed
confidence: medium
---

# Runbook — backup validation and recovery drill

**Parent package**: [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md).

**Principle**: A backup that has never been restored is a hypothesis. Prefer **restore-tested** evidence over job-success notifications alone.

---

## Preconditions

- Documented backup landing zones (**central** vs **local**) per [`Central vs local backup scope — farm edge stack`](central-vs-local-backup-scope-farm-edge-stack.md).
- Break-glass access to decrypt restic / Longhorn targets **outside** the only copy of the failed cluster.

---

## Drill A — restic repository health (no full restore)

Mandatory for any restic-based path.

1. Run `restic check` (or documented maintenance) against the repository used for DB dumps or file backups—see [`restic backing up` capture](../../raw/processed/2026/restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md).
2. Confirm the latest snapshot has non-zero content for at least one critical path (`restic ls` spot-check).
3. Document who may run `forget` / `prune` and when (avoid locking the repo during peak farm loads on constrained power).

**Pass**: Check completes; snapshot list matches policy.

---

## Drill B — logical database restore (farmOS / PostgreSQL)

Mandatory when farm records are the system of record.

1. Provision a throwaway database (new instance or new database name).
2. Restore the latest `pg_dump` (or supported export) into that DB—match PostgreSQL and farmOS version expectations per [PostgreSQL backup docs](https://www.postgresql.org/docs/current/backup.html) and [farmOS hosting](https://farmos.org/hosting/).
3. Point a **staging** farmOS install at the restored DB and verify known records (assets, geometry spot-checks)—not production DNS until cutover is deliberate.

**Pass**: App boots; data age matches your stated RPO from [`Restore and recovery tiers`](restore-recovery-tiers-homelab-farm-systems.md).

---

## Drill C — Longhorn volume restore (subset)

When Longhorn backs up PVCs you rely on.

1. Pick one non-production namespace or test PVC.
2. Execute restore per [`Longhorn restore` capture](../../raw/processed/2026/longhorn-restore-system-capture-inbox-2026-04-17.md) and current Longhorn docs.
3. Verify mount and filesystem integrity (checksum or workload smoke test).

**Pass**: Volume is attachable and consistent for that workload class.

---

## Drill D — k3s etcd snapshot restore (staging only)

Dangerous on production without a maintenance window—use a lab cluster first.

1. Follow [k3s backup and restore](https://docs.k3s.io/datastore/backup-restore) and [etcd-snapshot CLI](https://docs.k3s.io/cli/etcd-snapshot) for your install mode.
2. Prove you can list and restore from your real snapshot store (local path and S3-compatible if configured).

**Pass**: Documented steps work end-to-end in staging once.

---

## Drill E — Rancher (if installed)

1. Per [Rancher backup/restore usage](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/backup-restore-and-disaster-recovery/back-up-restore-usage-guide), confirm backup artifacts exist and you retain the encryption configuration if used (the operator does not back that file up for you).
2. Tabletop or staging restore per docs—avoid version skew between backup source and restore target.

---

## Drill F — secrets and configuration

1. List what is **not** in plain Git: Sealed Secrets, SOPS, cloud KMS, manual kubeconfig distribution.
2. Verify one rotation or recovery path (dry-run acceptable) and where encrypted break-glass copies live.

---

## Reporting

After drills, update [`Restore and recovery tiers — homelab farm systems`](restore-recovery-tiers-homelab-farm-systems.md) with measured elapsed times (RPO/RTO worksheet) and append `wiki/log.md` if policy changed.

---

## Related

- [`Restore and recovery tiers — homelab farm systems`](restore-recovery-tiers-homelab-farm-systems.md)
- [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md)
