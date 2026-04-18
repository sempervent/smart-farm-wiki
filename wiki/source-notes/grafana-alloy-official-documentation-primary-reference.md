---
title: Grafana Alloy — official documentation (primary reference)
page_type: source_note
status: active
created: 2026-04-25
updated: 2026-04-25
source_ids: []
tags:
  - grafana
  - alloy
  - observability
  - kubernetes
review_status: unreviewed
confidence: high
---

# Grafana Alloy — official documentation (primary reference)

**Purpose**: **Single** **primary** pointer for **Grafana Alloy**—the vendor’s **OpenTelemetry**-centric **collector** and **pipeline** component that can **replace** or **complement** **node_exporter** + **Promtail**-style splits in some architectures.

**Official documentation (web)**

- **Documentation home**: [grafana.com/docs/alloy](https://grafana.com/docs/alloy/latest/)
- **Release / product context**: [grafana.com/oss/alloy](https://grafana.com/oss/alloy/)

**What this is not**: A mandate to adopt Alloy on the farm edge; [`Platform decision memo`](../analyses/platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md) remains the **scope** gate. **Synthesis** for alert routing and trust bars: [`Observability, secrets, and trust bar — homelab / farm edge`](../analyses/observability-secrets-and-trust-bar-homelab-farm-edge.md).

**Raw capture**: None in vault as of this note—operators should cite **versioned** docs URLs in runbooks when Alloy is adopted.

## Evidence summary

| Field | Content |
|-------|---------|
| **Abstract** | **Primary web** pointer for **Grafana Alloy** OTel collector docs—optional alternative to split Prometheus/Loki agents on the edge. |
| **Authority mix** | **Vendor** (Grafana Labs) official documentation only. |
| **Decision relevance** | Observability **pipeline** shape—supports [`Observability, secrets, and trust bar — homelab / farm edge`](../analyses/observability-secrets-and-trust-bar-homelab-farm-edge.md); **does not** override [`Platform decision memo`](../analyses/platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md) scope. |
| **Canonical wiki links** | [`Observability, secrets, and trust bar — homelab / farm edge`](../analyses/observability-secrets-and-trust-bar-homelab-farm-edge.md) · [`Monitoring and logging expectations — edge cluster standard`](../analyses/monitoring-and-logging-expectations-edge-cluster-standard.md) |

**Key claims** (public-safe):

- Alloy is **one** supported way to run **OpenTelemetry**-style **pipelines**—not mandatory for a valid farm edge cluster.

**Open questions / follow-ups**

- Pin **docs URL** + **version** in runbooks when Alloy is deployed.

