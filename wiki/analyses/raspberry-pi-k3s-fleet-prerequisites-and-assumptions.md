---
title: Raspberry Pi k3s fleet — prerequisites and assumptions
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - k3s
  - raspberry-pi
  - operations
review_status: unreviewed
confidence: medium
---

# Raspberry Pi k3s fleet — prerequisites and assumptions

**Parent runbook**: [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md).

---

## Mandatory

1. **64-bit Linux** on every node, **kernel** and **userspace** aligned with **k3s** [installation requirements](https://docs.k3s.io/installation/requirements) (verify current doc at deploy time).
2. **Unique hostname** per node (or explicit `K3S_NODE_NAME` at join)—duplicate names break joins; see [`Raspberry Pi fleet provisioning standard`](raspberry-pi-fleet-provisioning-standard-smart-farm-homelab.md).
3. **Synchronized time** (systemd-timesyncd, chrony, or NTP on the LAN)—required for TLS, logs, and etcd coherence.
4. **Outbound path to pull images** during install (or a **private registry** plan documented in advance)—air-gapped installs are **Later** and out of scope for this outline.
5. **Operator skill**: `ssh`, `sudo`, basic `kubectl`, willingness to read upstream **k3s** / **Longhorn** / **Rancher** docs for **version-pinned** commands.

---

## Assumptions (explicit)

| Assumption | If false |
|------------|----------|
| **Small fleet** (typically **1** server + **1–4** agents, not a hyperscale datacenter) | Revisit **etcd** sizing, **network** policy, and **monitoring**—still not “infinite Pi.” |
| **Ethernet backhaul** for cluster nodes during bootstrap | Wi‑Fi-only **may** work but is **not** assumed stable for **Longhorn** **replication** **or** **etcd** **latency**. |
| **You can tolerate maintenance windows** on **P0/P1** | **HA** control plane is **Optional**; see [`Central and HA storage options`](raspberry-pi-k3s-fleet-central-and-ha-storage-options.md). |
| **Workloads are modest** (a few stateful services, not hundreds of pods per node) | Set **resource requests/limits** and **avoid** **Rancher** **+** **heavy** **observability** **on** **the** **same** **tiny** **nodes**. |

---

## Phase scope

| Phase | What this package assumes you want |
|-------|-----------------------------------|
| **P0** | Learn k3s + **maybe** Longhorn; **data disposable**; **single** k3s server OK. |
| **P1** | **Pilot** workloads (e.g. **farmOS** trial); **backups** **mandatory**; still **one** server acceptable if **RTO** is honest. |
| **Later** | **HA** k3s servers, **tested** failover, **Rancher** as a **managed** **component**, **off-site** backup targets. |

---

## Optional (HA / scale)

- **HA control plane** (multiple k3s servers + embedded etcd or external datastore)—see [k3s HA docs](https://docs.k3s.io/datastore/ha-embedded) **externally**.
- **Dedicated** **monitoring** stack (Prometheus/Grafana) on **separate** **hardware**—not on **2× Pi 4** **by** **default**.

---

## Related

- [`Hardware BOM and node roles`](raspberry-pi-k3s-fleet-hardware-bom-and-node-roles.md)
- [`Network and power prerequisites`](raspberry-pi-k3s-fleet-network-and-power-prerequisites.md)
