---
title: Longhorn vs central storage architecture — homelab / farm platform
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-18
tags:
  - longhorn
  - storage
  - kubernetes
  - nas
review_status: unreviewed
confidence: medium
---

# Longhorn vs central storage architecture — homelab / farm platform

## Purpose

**Choose** between **Longhorn** (distributed **Kubernetes** block storage) and **central** storage (NAS/NFS/object **outside** the cluster) for **farmOS**, **telemetry stacks**, and **media**—without prescribing a vendor SKU.

**Sources**: [`Longhorn CSI on K3s`](../../raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md), [`homelab Pi + Longhorn capture`](../../raw/processed/2026/raspberry-pi-k3s-longhorn-rancher-homelab-capture-inbox-2026-04-18.md), [`Longhorn system backup`](../../raw/processed/2026/longhorn-backup-system-capture-inbox-2026-04-17.md). **Compare** also [`Backup strategy comparison`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md).

---

## When Longhorn fits

- You want **PVCs** **portable** across **k3s** nodes with **replication** and **snapshots** in the **Kubernetes** control path.
- Nodes have **dedicated disk** for Longhorn (Pi narrative: **SSD** per node).
- You accept **iSCSI** + **Longhorn** **operator** **burden** ([`CSI on K3s`](../../raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md)).

## When central storage fits

- **Large** **sequential** **files** (video, bulk imagery) where **NFS/SMB** **or** **object** **is** **simpler** than block PVCs.
- **Single** **strong** **NAS** with **UPS** **and** **backup**—good for **read-mostly** **archives**.
- You want **fewer** **moving** **parts** **inside** **Kubernetes** **for** **a** **specific** **dataset**.

## Hybrid (common)

- **Longhorn** for **stateful** **workloads** **(farmOS DB PVC,** **broker** **PVC** **)**.
- **Central** **NFS** **or** **S3-compatible** **target** for **backup** **repositories** **(restic)** **and** **media**—see [`Kubernetes platform backup / DR`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md).

---

## “HA storage” in this wiki

- **Longhorn replication** ≠ **geographic** **HA**—it is **survive** **a** **node** **disk** **/ host** **loss** **within** **a** **LAN**.
- **Central** **NAS** **HA** **(dual-controller,** **etc.** **)** **is** **a** **different** **product** **class**—**not** **assumed** **here**.

---

## Related

- [`Raspberry Pi k3s fleet — central and HA storage options`](raspberry-pi-k3s-fleet-central-and-ha-storage-options.md) (operational decision path for this wiki’s Pi stack)
- [`Homelab / edge Kubernetes platform strategy`](homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md)
- [`Rancher role and timing`](rancher-role-and-timing-k3s-homelab-farm-platform.md)
