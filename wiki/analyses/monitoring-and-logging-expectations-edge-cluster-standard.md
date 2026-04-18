---
title: Monitoring and logging expectations — edge cluster standard
page_type: analysis
page_subtype: standard
operational_maturity: pilot_ready
status: active
created: 2026-04-24
updated: 2026-04-25
tags:
  - observability
  - kubernetes
  - standards
review_status: reviewed
confidence: high
---

# Monitoring and logging expectations — edge cluster standard

## Purpose

**Minimum** **observability** bar for **farm edge** **k3s** clusters: enough **signal** to detect **disk**, **API**, and **workload** **failure** **without** mandating a specific vendor stack.

**Not in scope**: Full Prometheus architecture—pick components per [`Platform decision memo`](platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md).

---

## Standard

| Area | Expectation |
|------|-------------|
| **Cluster health** | **Someone** can answer: API up? **Nodes** **Ready**? **Longhorn** **volumes** **attached**?—via **kubectl**, **dashboard**, or **metrics**. |
| **Stateful workloads** | **farmOS** / **DB**: **HTTP** or **app** **probe** **outside** **“pod running”**—**verify** **read/write** **path** periodically. |
| **Logs** | **Retain** policy **documented** (days/weeks); **centralize** if **multi-node**—**avoid** **only** **ephemeral** **container** **logs** for **debugging** **tax** **events**. |
| **Alerts** | **At least one** **channel** (email, phone, **HA** **notify**) for **backup** **job** **failure** and **cert** **expiry** if **ingress** used. |
| **Pi / power** | On **off-grid** **sites**, pair with **SOC** / **generator** **awareness** ([`Off-grid implications — backup and networking choices`](off-grid-implications-backup-and-networking-choices.md))—**not** **only** **K8s** **metrics**. |

**Pilot vs production**: **Pilot** may be **manual** **kubectl** **only**; **production** implies **scheduled** **checks** or **metrics** **scraping**.

---

## Related

- [`Observability, secrets, and trust bar — homelab / farm edge`](observability-secrets-and-trust-bar-homelab-farm-edge.md) — **Doctrine**: alert routing philosophy, trust bar for **remote** ops, optional **Grafana Alloy**.
- [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md) — Prometheus **Alertmanager** overview + configuration doc captures (`raw/processed/2026/`).
- [`Instrumentation priority matrix — two-site smart farm`](instrumentation-priority-matrix-two-site-smart-farm.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)
