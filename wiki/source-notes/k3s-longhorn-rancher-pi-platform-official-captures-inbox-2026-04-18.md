---
title: K3s, Longhorn, Rancher, Raspberry Pi — platform captures (inbox 2026-04)
page_type: source_note
status: active
created: 2026-04-18
updated: 2026-04-18
source_ids:
  - raw/processed/2026/k3s-architecture-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/k3s-installation-index-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/k3s-quick-start-guide-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/k3s-configuration-options-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/rancher-k3s-product-page-capture-inbox-2026-04-18.md
  - raw/processed/2026/raspberry-pi-k3s-longhorn-rancher-homelab-capture-inbox-2026-04-18.md
tags:
  - k3s
  - longhorn
  - rancher
  - raspberry-pi
  - kubernetes
review_status: unreviewed
---

# K3s, Longhorn, Rancher, Raspberry Pi — platform captures (inbox 2026-04)

**Ingest**: Web captures from **docs.k3s.io**, **longhorn.io**, **rancher.com** product page, and one **homelab** narrative (GitHub-style article) for Pi + Longhorn + Rancher operational patterns.

## Official / primary operator docs (this batch)

| Raw path | Role |
|----------|------|
| [`k3s-architecture-docs-capture...`](../../raw/processed/2026/k3s-architecture-docs-capture-inbox-2026-04-18.md) | Server vs agent, single-server embedded DB, **HA** overview, agent LB / node-password behavior |
| [`k3s-installation-index-docs-capture...`](../../raw/processed/2026/k3s-installation-index-docs-capture-inbox-2026-04-18.md) | Installation hub; points to **Requirements**, air-gap, server roles, uninstall |
| [`k3s-quick-start-guide-docs-capture...`](../../raw/processed/2026/k3s-quick-start-guide-docs-capture-inbox-2026-04-18.md) | `get.k3s.io`, tokens, **unique hostname** / `K3S_NODE_NAME`, links to HA etcd pages |
| [`k3s-configuration-options-docs-capture...`](../../raw/processed/2026/k3s-configuration-options-docs-capture-inbox-2026-04-18.md) | `INSTALL_K3S_EXEC`, env vars, install script persistence |
| [`longhorn-csi-on-k3s-docs-capture...`](../../raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md) | `open-iscsi` / `iscsiadm`, **kubelet root dir** / `KUBELET_ROOT_DIR` for K3s |
| [`rancher-k3s-product-page-capture...`](../../raw/processed/2026/rancher-k3s-product-page-capture-inbox-2026-04-18.md) | Rancher + K3s positioning (marketing; not install requirements) |

**External (not duplicated in raw)**: [K3s installation requirements](https://docs.k3s.io/installation/requirements), [HA embedded etcd](https://docs.k3s.io/datastore/ha-embedded), [HA external datastore](https://docs.k3s.io/datastore/ha).

## Community / narrative (secondary)

| Raw path | Role |
|----------|------|
| [`raspberry-pi-k3s-longhorn-rancher-homelab-capture...`](../../raw/processed/2026/raspberry-pi-k3s-longhorn-rancher-homelab-capture-inbox-2026-04-18.md) | Pi cluster + SSD migration; Longhorn via Rancher Apps; **replica count**, **disable server node** for scheduling; **not** vendor canonical |

## Related batches (already in vault)

- Longhorn system backup/restore: [`homelab backup stack — official captures`](homelab-backup-stack-official-captures-inbox-2026-04-18.md)
- Distribution choice: [`k3s or RKE2`](k3s-or-rke2.md), [`when to use k3s and RKE2`](when-to-use-k3s-and-rke2.md), [`Kubernetes distributions overview`](kubernetes-distributions-overview-kubeadm-k3s-microk8s-minikube-talos-rke2.md)

## Synthesis

- [`Platform strategy for farm and homestead services`](../analyses/homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md) · [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md)
- [`Platform decision memo — phase, HA scope, deferrals (Pi / k3s / 2026)`](../analyses/platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md)
