---
title: Raspberry Pi k3s fleet — validation checklist
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - k3s
  - longhorn
  - operations
review_status: unreviewed
confidence: medium
---

# Raspberry Pi k3s fleet — validation checklist

**Parent runbook**: [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md).

---

## Cluster — mandatory

- [ ] `kubectl get nodes`: all nodes `Ready` without repeated `NotReady` flapping.
- [ ] `kubectl get pods -A`: core add-ons healthy (resolve `CrashLoopBackOff` before sign-off).
- [ ] Time sync verified on each node (logs or `timedatectl`).
- [ ] Disk headroom on the etcd server node and on every Longhorn disk.

---

## Longhorn — mandatory when Longhorn is in scope

- [ ] Disks schedulable on expected nodes (Longhorn UI or `kubectl`).
- [ ] Test PVC: bind, write, read, delete cycle succeeds.
- [ ] Replica policy documented per StorageClass or volume; observe CPU during rebuild (simulate with cordon/drain in lab).

---

## Rancher — only if installed

- [ ] HTTPS endpoint loads with trusted certs (or documented lab exception).
- [ ] Admin bootstrap password rotated; break-glass access documented.
- [ ] Helm chart/value version pinned; upgrade path noted.

---

## Backup — P1+ mandatory

- [ ] Application logical backup (e.g. `pg_dump` path) ran successfully at least once; artifact exists off-node.
- [ ] Longhorn backup job succeeded, or deferral is explicitly logged with risk acceptance.
- [ ] Tabletop restore completed against a non-production namespace or lab cluster.

---

## Performance sanity (Pi — mandatory honesty)

- [ ] Idle and loaded power measured for server + one agent (watts at wall where possible).
- [ ] During Longhorn rebuild, no sustained 100% CPU on all cores for routine work (`kubectl top nodes` if metrics exist, or `htop` on node).

---

## Related

- [`Troubleshooting and degraded modes`](raspberry-pi-k3s-fleet-troubleshooting-and-degraded-modes.md)
- [`Backup and restore sequence`](raspberry-pi-k3s-fleet-backup-and-restore-sequence.md)
