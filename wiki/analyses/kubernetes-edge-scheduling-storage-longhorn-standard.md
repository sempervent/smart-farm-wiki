---
title: Kubernetes edge — scheduling, storage class, and Longhorn roles standard
page_type: analysis
page_subtype: standard
operational_maturity: pilot_ready
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - kubernetes
  - longhorn
  - storage
  - standards
review_status: reviewed
confidence: high
---

# Kubernetes edge — scheduling, storage class, and Longhorn roles standard

## Purpose

**Norms** for **node labels**, **taints/tolerations**, and **Longhorn** **disk** **roles** on **Pi / k3s** **edge** clusters—so workloads land predictably and **storage** **defaults** are explicit.

**Guides**: [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) · [`Longhorn role in the homelab / farm platform`](longhorn-role-in-homelab-farm-platform.md).

---

## Standard

| Topic | Rule |
|-------|------|
| **Control-plane nodes** | **Document** whether Longhorn **replicas** are **allowed** on **server** nodes; if **no**, use **labels/taints** so storage-heavy workloads do not starve **etcd** (align with [`Pi fleet provisioning standard`](raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md) narrative). |
| **Storage-heavy agents** | Prefer **dedicated** **agent** nodes with **USB3 SSD** for **Longhorn** disks; **label** `longhorn-storage=true` (or project convention) **consistently**. |
| **Default StorageClass** | **Exactly one** **default** **SC** for **general** workloads; **document** **reclaim** **policy** (Retain vs Delete) **per** environment—**no** silent **default** changes mid-season. |
| **farmOS / DB PVCs** | **Name** **namespaces** and **PVC** **prefixes** **predictably** (e.g. `farmos-*`) so **backup** jobs and **DR** **tracks** stay filterable ([`Kubernetes platform backup / DR`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md)). |
| **Taints** | Use **taints** for **specialist** nodes (e.g. **GPU**, **dedicated** **ingress**); **every** taint has a **documented** **toleration** in the workload that needs it. |

**Anti-pattern**: **Mixing** **SD-card-only** **nodes** into **Longhorn** **replica** **counts** for **production** **farm** **data**.

---

## Related

- [`Longhorn vs central storage architecture — homelab / farm platform`](longhorn-vs-central-storage-architecture-homelab-farm-platform.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)
