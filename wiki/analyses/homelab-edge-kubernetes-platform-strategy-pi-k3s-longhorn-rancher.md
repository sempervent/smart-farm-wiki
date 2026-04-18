---
title: Platform strategy for farm and homestead services
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-17
tags:
  - k3s
  - longhorn
  - rancher
  - raspberry-pi
  - homelab
  - farmos
review_status: unreviewed
confidence: medium
aliases:
  - Homelab edge Kubernetes platform strategy Pi fleet k3s Longhorn Rancher
---

# Platform strategy for farm and homestead services

## Purpose

**Canonical platform** story for this wiki: a **small** **homelab / farm edge** footprint using a **Raspberry Pi fleet** (or similar ARM SBCs), **k3s**, **Longhorn** for **distributed block storage**, optional **Rancher** for **multi-cluster UX**, and **central** or **co-located** storage servers where justified—**tied** to **farmOS**, **telemetry**, and **two-site** control-plane assumptions without **Kubernetes maximalism**.

**Doctrine package** (reading order, HA semantics, roles): [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md).

**Sources**: [`K3s / Longhorn / Rancher / Pi captures`](../source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md). **Backup/DR**: [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md), [`Kubernetes platform backup / DR — Pi, k3s, Longhorn`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md).

---

## Layered view

| Layer | Components | Role for farm / homelab |
|-------|------------|---------------------------|
| **Nodes** | Pi (or ARM/x86) **servers** + **agents** | Run k3s; **unique hostnames** per quick-start capture |
| **Cluster runtime** | **k3s** server/agent | Certified K8s API; single-server **SQLite** default vs **HA** servers + datastore ([`architecture capture`](../../raw/processed/2026/k3s-architecture-docs-capture-inbox-2026-04-18.md)) |
| **Block storage** | **Longhorn** CSI | PVCs for **farmOS**, **MQTT**, **TSDB**, **Rancher**; requires **iSCSI** client on node ([`Longhorn CSI on K3s`](../../raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md)) |
| **Control UX (optional)** | **Rancher** on cluster | Helm-installed management UI; **not** required for minimal k3s ([`Rancher role and timing`](rancher-role-and-timing-k3s-homelab-farm-platform.md)) |
| **Central storage (optional)** | NAS / NFS / object store | Large media, **off-cluster** backups, or **read-mostly** archives—[`Longhorn vs central storage`](longhorn-vs-central-storage-architecture-homelab-farm-platform.md) |
| **Workloads** | farmOS, brokers, **observability** | Prefer **few** **stateful** sets with **proven** backup paths ([`Telemetry SoR`](telemetry-system-of-record-boundaries-and-authority.md)) |

---

## Design principles (this repo)

1. **Pilot-ready ≠ production-ready**: single k3s server + agents can be enough for Phase 0/1; **HA** control plane is a **documented** upgrade path, not day-one default ([`platform decision memo`](platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md)).
2. **State is the product**: Longhorn protects **PVC** data; **logical** DB dumps still matter for farmOS/Postgres ([`backup strategy comparison`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md)).
3. **Rancher is optional glue**: adds **ops** **comfort** and **app catalog**; adds **attack surface** and **upgrade** coupling—defer until k3s + workloads are boring.
4. **Edge power**: Pi fleet at **remote farm** must align with [`off-grid power — Demory`](off-grid-power-strategy-demory-farm-site.md)—**k3s** **is** **not** **free** **Wh/day**.

---

## Related

- [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md) — **First-class** hub: k3s / Longhorn / Rancher **roles**, **HA** meaning, **approved vs deferred**
- [`k3s role in the homelab / farm platform`](k3s-role-in-homelab-farm-platform.md), [`Longhorn role in the homelab / farm platform`](longhorn-role-in-homelab-farm-platform.md), [`HA meaning and constraints`](ha-meaning-and-constraints-homelab-farm-platform.md)
- [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md) — DR spine (etcd, Longhorn, Rancher, farmOS/PostgreSQL, secrets, drills)
- [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) — **Stepwise operator runbook** (prerequisites → bootstrap → Longhorn → optional Rancher → backup → validation).
- [`Raspberry Pi fleet provisioning standard — smart farm / homelab`](raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md)
- [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md)
- [`Field telemetry reference architecture — homestead + 120 ac`](field-telemetry-reference-architecture-homestead-120ac.md)
- [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md)
