---
title: Observability, secrets, and trust bar — homelab / farm edge
page_type: analysis
status: active
created: 2026-04-25
updated: 2026-04-29
tags:
  - observability
  - prometheus
  - alertmanager
  - sops
  - grafana
  - kubernetes
  - two-site
review_status: unreviewed
confidence: high
---

# Observability, secrets, and trust bar — homelab / farm edge

## Purpose

**Canonical synthesis** for **how** the **homelab / farm edge** stack should treat **metrics**, **alerts**, **logs**, **secrets**, and **remote trust**—aligned with **operator-grade** upstream docs and **without** mandating a single vendor bundle. **Complements** [`Monitoring and logging expectations — edge cluster standard`](monitoring-and-logging-expectations-edge-cluster-standard.md) and [`Secrets and certificates — edge cluster standard`](secrets-and-certificates-edge-cluster-standard.md).

**Non-goals**: Full Prometheus **HA** design; **product** selection where [`Platform decision memo — phase, HA scope, deferrals`](platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md) already defers scope.

---

## Source grounding (vault + primary web)

| Topic | Vault / primary |
|-------|-----------------|
| **Prometheus Alertmanager** — routing, inhibition, silences | Captures: [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md) (`prometheus-alertmanager-*-docs-capture-inbox-2026-04-18.md`); upstream [prometheus.io/docs/alerting](https://prometheus.io/docs/alerting/latest/alertmanager/). |
| **Flux + SOPS** (GitOps secrets) | Capture: `fluxcd-manage-kubernetes-secrets-with-sops-capture-inbox-2026-04-18.md` in same batch; upstream [fluxcd.io/flux/guides/mozilla-sops](https://fluxcd.io/flux/guides/mozilla-sops/). |
| **SOPS** (encrypt YAML/JSON in repo) | Capture: `sops-project-readme-docs-capture-inbox-2026-04-18.md`; project [github.com/getsops/sops](https://github.com/getsops/sops). |
| **Grafana Alloy** (collector / pipeline option) | Primary reference note: [`Grafana Alloy — official documentation`](../source-notes/grafana-alloy-official-documentation-primary-reference.md). |

---

## Alert routing philosophy (farm-relevant)

1. **Reduce noise before adding channels**: Use **Alertmanager**-style **grouping** and **inhibition** so **one** physical failure does not **page** as dozens of tickets ([`Automation stop rules — two-site smart farm`](automation-stop-rules-two-site-smart-farm.md) **NS-*** family).
2. **Separate “welfare / safety” from “convenience”**: Livestock **water**, **extreme temperature**, or **gate** anomalies deserve **different** routing than **disk** or **certificate** warnings—document **receiver** mapping in the same place as [`Instrumentation priority matrix — two-site smart farm`](instrumentation-priority-matrix-two-site-smart-farm.md).
3. **WAN-aware stops**: If alerts drive **“should I drive?”**, they must pass **degraded** drills in [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) (**CS-4**) and [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md)—**dashboards are not ground truth** when the broker is **stale**.
4. **Off-grid / `SITE_FARM`**: Pair **cluster** metrics with **power** state (**SOC**, **generator**) per [`Monitoring and logging expectations — edge cluster standard`](monitoring-and-logging-expectations-edge-cluster-standard.md)—**Kubernetes green** can coexist with **ranch brown**.

---

## Secrets and repo-safe handling (normative summary)

| Rule | Rationale |
|------|-----------|
| **No plaintext secrets in public Git** | [`Secrets and certificates — edge cluster standard`](secrets-and-certificates-edge-cluster-standard.md) row 1; implement with **SOPS**, **Sealed Secrets**, or **external KMS** per policy. |
| **Flux + SOPS** for GitOps clusters | Encrypted **Secret** manifests in repo; **decrypt** only on cluster—see Flux guide capture in inbox batch. |
| **Rotate on personnel or compromise** | Same standard rows 2–4; **break-glass** path documented and **tested**. |

---

## What must be observable before remote operations are “trusted”

**Minimum trust bar** (additive to the **monitoring standard**):

| Signal | Why it matters |
|--------|----------------|
| **End-to-end app health** (HTTP/probe **beyond** pod Running) | Prevents **false confidence** when **PVC** or **DB** is broken. |
| **Backup job success** (or explicit “no backup configured”) | [`Backup validation cadence — farm stack standard`](backup-validation-cadence-standard-farm-stack.md). |
| **Certificate / ingress expiry** (if TLS ingress used) | Avoid **silent** **HTTPS** failure on **remote** admin. |
| **One** **documented** **on-call** path for **farm-critical** alerts | Ties to **CS-*** and [`Remote access and operational security model — two-site smart farm`](remote-access-operational-security-model-two-site-smart-farm.md). |

**Not sufficient alone**: **Video** / **NVR** feeds (see [`Local video / NVR — role and deferral boundaries`](local-video-nvr-role-and-deferral-boundaries-farm-stack.md)).

### Operator burden (hostile default)

**Trust bar ≠ free time.** Routing, inhibition, silences, and on-call paths are **recurring labor**—often **invisible** until they **collide** with **field surge** and **two-site** travel. Budget **triage hours** explicitly; otherwise **NS-2** triage stops are **theoretical** ([`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md)). Skeptical stack view: [`Phase 0–1 operator burden review — East Tennessee two-site (hostile)`](phase-0-1-operator-burden-review-east-tennessee-two-site.md).

---

## Grafana Alloy (optional component)

**Alloy** may **centralize** **otel** **pipelines** (logs + metrics + traces) **if** the team accepts **another** **daemon** on the edge—see [`Grafana Alloy — official documentation`](../source-notes/grafana-alloy-official-documentation-primary-reference.md). **Default** remains: satisfy the **monitoring standard** with **any** **supported** **stack**; **upgrade** to Alloy when **log** volume or **multi-signal** **routing** justifies **ops** cost.

---

## Related

- [`Phase 0–1 operator burden review — East Tennessee two-site (hostile)`](phase-0-1-operator-burden-review-east-tennessee-two-site.md)
- [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md)
- [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md)
- [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md)
