# Backup / DR — official documentation link batch (curated)

**Purpose**: Stable **pointers** to **operator-authoritative** backup and restore documentation for the stacks used in this wiki’s **homelab / farm edge** synthesis. **Not** a substitute for reading current upstream docs at deploy time (versions move).

**Created**: 2026-04-17 (agent-curated index; no full doc paste).

---

## Kubernetes / k3s (control plane, etcd)

| Topic | URL | Notes |
|-------|-----|--------|
| Backup and restore (embedded etcd) | https://docs.k3s.io/datastore/backup-restore | Restore ordering, token file, disaster recovery context |
| etcd snapshot CLI | https://docs.k3s.io/cli/etcd-snapshot | `save`, `ls`, S3-compatible upload flags |
| Datastore (HA, external DB) | https://docs.k3s.io/datastore | Choose snapshot story vs external DBA backup |

---

## Longhorn

Vault **captures** (excerpts): [`longhorn-backup-system-capture-inbox-2026-04-17.md`](longhorn-backup-system-capture-inbox-2026-04-17.md), [`longhorn-restore-system-capture-inbox-2026-04-17.md`](longhorn-restore-system-capture-inbox-2026-04-17.md). **Live** hub: https://longhorn.io/docs/ (verify version path).

---

## Rancher (management cluster)

| Topic | URL | Notes |
|-------|-----|--------|
| Back up Rancher | https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/backup-restore-and-disaster-recovery/back-up-rancher | Rancher Backups chart; **verify** version path (`v2.x`) at read time |
| Backup / restore usage | https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/backup-restore-and-disaster-recovery/back-up-restore-usage-guide | Resource order, encryption config **not** auto-backed up |

---

## PostgreSQL

| Topic | URL | Notes |
|-------|-----|--------|
| Backup and restore (manual) | https://www.postgresql.org/docs/current/backup.html | Logical vs file-system-level; **`pg_dump`** family |

---

## restic

Vault **captures**: [`restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md`](restic-backing-up-documentation-0-18-1-capture-inbox-2026-04-17.md). **Live**: https://restic.readthedocs.io/

---

## farmOS

| Topic | URL | Notes |
|-------|-----|--------|
| Hosting | https://farmos.org/hosting/ | **farmOS 2.x** and PostgreSQL—confirm before backup design |
| Historical Docker dev capture (vault) | [`farmos-docker-developing-hosting-capture-inbox-2026-04-17.md`](farmos-docker-developing-hosting-capture-inbox-2026-04-17.md) | Older compose/MariaDB pattern—**epistemic** only |

---

## Kubernetes secrets / config (patterns)

| Topic | URL | Notes |
|-------|-----|--------|
| Secrets | https://kubernetes.io/docs/concepts/configuration/secret/ | **Backups** **of** **etcd** **may** **contain** **secret** **material**—**govern** **access** **to** **snapshots** |

No single “backup secrets” page replaces **your** **Sealed Secrets / SOPS / external vault** policy.
