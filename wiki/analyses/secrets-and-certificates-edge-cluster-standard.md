---
title: Secrets and certificates — edge cluster standard
page_type: analysis
page_subtype: standard
operational_maturity: pilot_ready
status: active
created: 2026-04-24
updated: 2026-04-25
tags:
  - secrets
  - tls
  - kubernetes
  - standards
review_status: reviewed
confidence: high
---

# Secrets and certificates — edge cluster standard

## Purpose

**Minimum** **security** **norms** for **kubeconfig**, **join tokens**, **TLS**, and **application** **secrets** on **farm edge** clusters—aligned with [`Remote access and operational security model — two-site smart farm`](remote-access-operational-security-model-two-site-smart-farm.md).

**Drill**: [`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md) **Drill F**.

---

## Standard

| # | Rule |
|---|------|
| 1 | **No** **plaintext** **secrets** or **kubeconfig** in **public** **Git**—use **Sealed Secrets**, **SOPS**, **external** **secret** **store**, or **private** **vault** per team policy. |
| 2 | **Join** **tokens** and **API** **credentials** are **rotated** on **compromise** or **personnel** **change**—document **who** may **re-issue**. |
| 3 | **TLS** for **ingress** and **backup** **targets**: **document** **issuer** (Let's Encrypt, internal CA) and **renewal** **owner**; **alert** on **expiry** where possible. |
| 4 | **Rancher** (if used): **retain** **encryption** **config** for backups **outside** operator artifacts ([`Kubernetes platform backup / DR`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md)). |
| 5 | **Break-glass**: **one** **offline** **copy** **path** for **cluster** **recovery** **secrets** (encrypted)—**tested** annually or when **DR** **policy** **changes**. |

---

## Related

- [`Observability, secrets, and trust bar — homelab / farm edge`](observability-secrets-and-trust-bar-homelab-farm-edge.md) — **SOPS/Flux** placement and **repo-safe** norms (complements this standard).
- [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md) — Flux “manage secrets with SOPS” + **getsops/sops** readme captures (`raw/processed/2026/`).
- [`Remote access and operational security model — two-site smart farm`](remote-access-operational-security-model-two-site-smart-farm.md)
- [`Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md)
- [`Disaster recovery decision rules — farm edge stack`](disaster-recovery-decision-rules-farm-edge-stack.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)
