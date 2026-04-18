---
title: Central vs local backup scope — farm edge stack
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - backup
  - edge
  - two-site
  - homelab
review_status: unreviewed
confidence: medium
---

# Central vs local backup scope — farm edge stack

**Parent package**: [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md).

---

## Definitions

| Term | Meaning here |
|------|----------------|
| **Central** | **Primary** backup **landing zone** you treat as **authoritative** for **recovery** (home-base NAS, object store, cloud bucket)—often **`SITE_HOME`** in the two-site model. |
| **Local** | **On-gateway** or **on-field** storage used for **queueing**, **short** retention, or **survival** when **WAN** is **down**—**not** a substitute for **off-device** **central** **copies** **unless** **policy** **explicitly** **accepts** **single-site** **risk**. |

---

## What should be backed up **centrally** (typical)

| Asset class | Why central |
|-------------|-------------|
| **farmOS / PostgreSQL logical dumps** | **Farm records** **SoR**—**survive** **gateway** **swap** **or** **DB** **host** **loss** |
| **restic** **repository** **or** **object-store** **target** **for** **logical** **exports** | **Versioned** **recovery**; **encryption** **at** **rest** **per** **tool** |
| **Longhorn** **backup** **target** **(S3/NFS)** **when** **used** | **Off-node** **PVC** **history**; **pairs** **with** **k3s** **story** |
| **k3s** **etcd** **snapshots** **(embedded** **etcd** **)** | **Control** **plane** **DR**—**store** **off** **the** **server** **disk** **(S3-compatible** **per** **k3s** **docs** **)** |
| **Rancher** **backup** **artifacts** **(if** **Rancher** **installed** **)** | **Management** **UI** **+** **CR** **bundle** **per** **Rancher** **Backups** **docs** |
| **Helm** **values** **/** **GitOps** **repo** **(non-secret)** | **Reproducible** **redeploy** |

---

## What can stay **local** (with eyes open)

| Asset class | Local role | Risk if local-only |
|-------------|------------|---------------------|
| **Edge** **gateway** **SQLite** **/** **buffer** **DBs** | **Survive** **brief** **outages** | **Field** **device** **loss** **=** **buffer** **loss** **if** **never** **replicated** **central** |
| **MQTT** **broker** **spool** **(if** **any** **)** | **Transient** **ingress** | **Usually** **not** **SoR**—confirm **against** **SoR** **page** |
| **restic** **repo** **on** **USB** **disk** **at** **farm** | **When** **WAN** **unreliable** | **Site** **fire** **/** **theft**—still need **off-site** **policy** **for** **true** **DR** |
| **Mesh** **/** **LoRa** **configs** | **Fast** **field** **recovery** | **Document** **export** **to** **central** **Git** **or** **encrypted** **archive** |

---

## Two-site pattern (East Tennessee scenario)

- **Bias** **farm** **record** **exports** **and** **credential** **rotation** **artifacts** **toward** **`SITE_HOME`** **(control** **center** **)** **when** **Starlink** **/** **WAN** **allows**—see [`Connectivity strategy — Claxton and Demory`](connectivity-strategy-for-claxton-and-demory.md).
- **If** **WAN** **is** **down** **for** **days**: **local** **queue** **on** **gateway** **+** **manual** **removable** **media** **export** **beats** **silent** **failure** **of** **cloud-only** **pipelines**—[`Off-grid implications — backup and networking choices`](off-grid-implications-backup-and-networking-choices.md).

---

## Related

- [`Restore and recovery tiers — homelab farm systems`](restore-recovery-tiers-homelab-farm-systems.md)
- [`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md)
