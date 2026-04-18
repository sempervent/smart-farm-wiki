---
title: Raspberry Pi fleet provisioning standard — smart farm / homelab
page_type: analysis
page_subtype: standard
operational_maturity: pilot_ready
status: active
created: 2026-04-18
updated: 2026-04-18
tags:
  - raspberry-pi
  - k3s
  - provisioning
  - homelab
review_status: unreviewed
confidence: medium
---

# Raspberry Pi fleet provisioning standard — smart farm / homelab

## Purpose

**Minimum** **operator** **standard** for **Pi-class** nodes joining a **k3s** fleet that may run **farmOS**, **telemetry**, and **Longhorn**—aligned with **official k3s** install notes and **Longhorn on K3s** prerequisites.

**Sources**: [`k3s quick-start`](../../raw/processed/2026/k3s-quick-start-guide-docs-capture-inbox-2026-04-18.md), [`Longhorn CSI on K3s`](../../raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md), [`Pi + k3s + Longhorn homelab narrative`](../../raw/processed/2026/raspberry-pi-k3s-longhorn-rancher-homelab-capture-inbox-2026-04-18.md) (secondary). **External**: [K3s requirements](https://docs.k3s.io/installation/requirements).

---

## Checklist (every node)

| Item | Why |
|------|-----|
| **Unique hostname** | k3s quick-start: duplicate hostnames break joins—use `K3S_NODE_NAME` if needed ([`quick-start`](../../raw/processed/2026/k3s-quick-start-guide-docs-capture-inbox-2026-04-18.md)) |
| **64-bit OS** | Match k3s + container images for your stack; verify against [requirements](https://docs.k3s.io/installation/requirements) |
| **Quality storage for etcd / Longhorn** | **SD-only** control plane is a **fragility** pattern; **USB3 SSD** or better for **server** nodes and **Longhorn** disks per homelab narrative |
| **`open-iscsi` / `iscsiadm`** | Longhorn on K3s prerequisite ([`CSI capture`](../../raw/processed/2026/longhorn-csi-on-k3s-docs-capture-inbox-2026-04-18.md)) |
| **Time sync** | NTP/chrony—cluster security and logs correlate to [`time / PNT` topics](../topics/time-synchronization-ntp-and-ptp.md) |
| **Network policy known** | Static DHCP or reserved IPs; **document** **server URL** and **token** handling per quick-start |

---

## Roles (k3s)

- **Server**: runs datastore + control plane (embedded or HA topology per [`architecture`](../../raw/processed/2026/k3s-architecture-docs-capture-inbox-2026-04-18.md)).
- **Agent**: workload + kubelet; join with `K3S_URL` + `K3S_TOKEN` ([`quick-start`](../../raw/processed/2026/k3s-quick-start-guide-docs-capture-inbox-2026-04-18.md)).

**Longhorn scheduling**: narrative suggests **disabling** Longhorn replicas on **server** nodes if you want control-plane separation—validate against your **HA** and **disk** layout ([`homelab capture`](../../raw/processed/2026/raspberry-pi-k3s-longhorn-rancher-homelab-capture-inbox-2026-04-18.md), Longhorn docs on node/disk eviction).

---

## Pilot vs production-ready

| Aspect | Pilot (acceptable) | Production-ready (raise bar) |
|--------|-------------------|------------------------------|
| **Control plane** | **One** k3s server | HA servers per k3s docs + **tested** restore |
| **Storage** | Single replica / small PVCs | Longhorn **replica** count + **backup target** + **monitored** disk health |
| **Secrets** | Manual token files | Sealed Secrets / external secret store (policy choice—not prescribed here) |

---

## Related

- [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) (full runbook: bootstrap → Longhorn → optional Rancher → backup)
- [`Homelab / edge Kubernetes platform strategy`](homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md)
- [`Platform decision memo`](platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md)
