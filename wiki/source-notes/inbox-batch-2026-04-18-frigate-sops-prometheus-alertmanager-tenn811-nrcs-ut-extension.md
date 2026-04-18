---
title: Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)
page_type: source_note
status: active
created: 2026-04-18
updated: 2026-04-18
source_ids:
  - raw/processed/2026/frigate-introduction-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/frigate-configuration-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/fluxcd-manage-kubernetes-secrets-with-sops-capture-inbox-2026-04-18.md
  - raw/processed/2026/sops-project-readme-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/prometheus-alertmanager-overview-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/prometheus-alertmanager-configuration-docs-capture-inbox-2026-04-18.md
  - raw/processed/2026/tenn811-home-page-capture-inbox-2026-04-18.md
  - raw/processed/2026/tenn811-before-you-dig-steps-capture-inbox-2026-04-18.md
  - raw/processed/2026/nrcs-cps-614-watering-facility-standard-page-capture-inbox-2026-04-18.md
  - raw/processed/2026/nrcs-neh-part-652-irrigation-guide-1997-capture-inbox-2026-04-18.pdf
  - raw/processed/2026/nrcs-neh-part-652-irrigation-guide-1997-capture-inbox-2026-04-18-extracted.md
  - raw/processed/2026/ut-extension-pb1541-planning-building-fences-farm-capture-inbox-2026-04-18.pdf
  - raw/processed/2026/ut-extension-pb1541-planning-building-fences-farm-capture-inbox-2026-04-18-extracted.md
  - raw/processed/2026/ut-extension-pb1641-alternative-livestock-watering-systems-capture-inbox-2026-04-18.pdf
  - raw/processed/2026/ut-extension-pb1641-alternative-livestock-watering-systems-capture-inbox-2026-04-18-extracted.md
tags:
  - ingest
  - frigate
  - sops
  - prometheus
  - alertmanager
  - tennessee
  - nrcs
  - ut-extension
review_status: unreviewed
confidence: medium
---

# Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)

## Evidence summary

| Field | Content |
|-------|---------|
| **Abstract** | Single **batch** grounding **edge** observability/secrets (Frigate, Flux+SOPS, SOPS readme, Alertmanager) with **Tennessee 811** locate process captures and **NRCS/UT** agriculture PDFs (fence, watering, irrigation guide). |
| **Authority mix** | **Vendor primary docs** (captured) + **state agency** (811) + **federal NRCS** + **UT Extension** PDFs. |
| **Decision relevance** | **Homelab**: Frigate/Alertmanager/SOPS patterns for **platform** and **secrets** standards. **Field**: **811** safe-digging / ticket timing; **NRCS/UT** references for **fence** and **watering** planning—**not** substitute for **current** standard drawings or **site** engineering. |
| **Canonical wiki links** | [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md) · [`Secrets and certificates — edge cluster standard`](../analyses/secrets-and-certificates-edge-cluster-standard.md) · [`Monitoring and logging expectations — edge cluster standard`](../analyses/monitoring-and-logging-expectations-edge-cluster-standard.md) · [`Authoritative execution evidence cluster — East Tennessee`](authoritative-execution-evidence-cluster-east-tennessee.md) |

**Key claims** (public-safe):

- **TN811** captures describe **one-call** process and **three working days** notice framing at **ingest time**—verify **current** TCA and operator rules before digs.
- **UT Extension PB1541/PB1641** PDFs are **planning** references for **fences** and **alternative watering**; **NRCS NEH 652** is a **1997** irrigation guide PDF—use as **historical** reference unless superseded by current NRCS guidance.
- **Frigate / Alertmanager / SOPS** captures are **vendor** documentation snapshots for **operator** alignment—not a **security audit** of your cluster.

**Open questions / follow-ups**

- Re-validate **Flux+SOPS** flow against **your** GitOps toolchain and **key** management.

**Purpose**: Grounding note for material moved from `raw/inbox/` into `raw/processed/2026/` on **2026-04-18**: **homelab / edge** operator captures (Frigate NVR, Flux+SOPS secrets guide, upstream SOPS readme, Prometheus **Alertmanager** docs) plus **field-operations** references (**Tennessee 811** locate process, **NRCS** CPS 614 hub page, **NRCS NEH Part 652** Irrigation Guide PDF, **UT Extension** fence and livestock watering PDFs).

**Synthesis hooks**

- **Platform / observability / secrets**: [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md), [`Secrets and certificates — edge cluster standard`](../analyses/secrets-and-certificates-edge-cluster-standard.md), [`Monitoring and logging expectations — edge cluster standard`](../analyses/monitoring-and-logging-expectations-edge-cluster-standard.md); companion k3s stack captures: [`K3s, Longhorn, Rancher, Raspberry Pi — platform captures`](k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md).
- **Execution evidence / infrastructure**: [`Authoritative execution evidence cluster — East Tennessee`](authoritative-execution-evidence-cluster-east-tennessee.md) (tables updated for this batch).

**Provenance**: Web captures mirror **third-party sites** at ingest time; PDFs are **local copies** with machine `*-extracted.md` beside each. **Do not** treat captures as substitutes for current law, standards, or professional engineering.

---

## Frigate (NVR / Home Assistant)

| Raw path | Notes |
|----------|--------|
| [`frigate-introduction-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/frigate-introduction-docs-capture-inbox-2026-04-18.md) | Product overview: detectors, MQTT, motion → detect, HA integration pointers ([docs.frigate.video](https://docs.frigate.video/)). |
| [`frigate-configuration-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/frigate-configuration-docs-capture-inbox-2026-04-18.md) | Configuration: `config.yml` paths (incl. HA App addon dirs), minimal starter YAML, env substitution (`FRIGATE_*`), schema URL for VS Code. |

---

## SOPS (secrets in Git, Flux)

| Raw path | Notes |
|----------|--------|
| [`fluxcd-manage-kubernetes-secrets-with-sops-capture-inbox-2026-04-18.md`](../../raw/processed/2026/fluxcd-manage-kubernetes-secrets-with-sops-capture-inbox-2026-04-18.md) | **Flux** documentation: encrypt Kubernetes Secrets with SOPS + GPG/KMS; GitOps-oriented workflow ([fluxcd.io](https://fluxcd.io/flux/guides/mozilla-sops/)). |
| [`sops-project-readme-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/sops-project-readme-docs-capture-inbox-2026-04-18.md) | **getsops/sops** project readme: formats, KMS backends, CLI usage ([GitHub](https://github.com/getsops/sops)). |

---

## Prometheus — Alertmanager

| Raw path | Notes |
|----------|--------|
| [`prometheus-alertmanager-overview-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/prometheus-alertmanager-overview-docs-capture-inbox-2026-04-18.md) | Concepts: grouping, inhibition, silences, HA flags ([prometheus.io/docs/alerting](https://prometheus.io/docs/alerting/latest/alertmanager/)). |
| [`prometheus-alertmanager-configuration-docs-capture-inbox-2026-04-18.md`](../../raw/processed/2026/prometheus-alertmanager-configuration-docs-capture-inbox-2026-04-18.md) | Full configuration reference (long capture; file was saved under a “Configuration / Prometheus” filename but content is **Alertmanager** config). |

---

## Tennessee 811 (utility locate)

| Raw path | Notes |
|----------|--------|
| [`tenn811-home-page-capture-inbox-2026-04-18.md`](../../raw/processed/2026/tenn811-home-page-capture-inbox-2026-04-18.md) | Home / FAQ: one-call role, **three working days** notice (TCA 65-31-101), Positive Response, online tickets ([tenn811.com](https://www.tenn811.com/)). |
| [`tenn811-before-you-dig-steps-capture-inbox-2026-04-18.md`](../../raw/processed/2026/tenn811-before-you-dig-steps-capture-inbox-2026-04-18.md) | Safe digging steps, tolerance zone framing, ticket validity (**15 calendar days** after legal start), uniform color code. |

---

## NRCS — CPS 614 hub; NEH Part 652 (Irrigation Guide)

| Raw path | Notes |
|----------|--------|
| [`nrcs-cps-614-watering-facility-standard-page-capture-inbox-2026-04-18.md`](../../raw/processed/2026/nrcs-cps-614-watering-facility-standard-page-capture-inbox-2026-04-18.md) | **National** CPS **614** — Watering Facility: links to NHCP/NED/PO PDFs (2023), [FOTG](https://efotg.sc.egov.usda.gov/) reminder, and supporting USDA fact sheets (see raw outbound links). |
| [`nrcs-neh-part-652-irrigation-guide-1997-capture-inbox-2026-04-18.pdf`](../../raw/processed/2026/nrcs-neh-part-652-irrigation-guide-1997-capture-inbox-2026-04-18.pdf) | **National Engineering Handbook** Part 652 — *Irrigation Guide* (Sept 1997); policy/engineering context. |
| [`nrcs-neh-part-652-irrigation-guide-1997-capture-inbox-2026-04-18-extracted.md`](../../raw/processed/2026/nrcs-neh-part-652-irrigation-guide-1997-capture-inbox-2026-04-18-extracted.md) | Machine extract (searchable text). |

---

## UT Extension — fencing and livestock watering

| Raw path | Notes |
|----------|--------|
| [`ut-extension-pb1541-planning-building-fences-farm-capture-inbox-2026-04-18.pdf`](../../raw/processed/2026/ut-extension-pb1541-planning-building-fences-farm-capture-inbox-2026-04-18.pdf) | **PB1541** — *Planning and Building Fences on the Farm*. |
| [`ut-extension-pb1541-planning-building-fences-farm-capture-inbox-2026-04-18-extracted.md`](../../raw/processed/2026/ut-extension-pb1541-planning-building-fences-farm-capture-inbox-2026-04-18-extracted.md) | Machine extract. |
| [`ut-extension-pb1641-alternative-livestock-watering-systems-capture-inbox-2026-04-18.pdf`](../../raw/processed/2026/ut-extension-pb1641-alternative-livestock-watering-systems-capture-inbox-2026-04-18.pdf) | **PB1641** — *Selection of Alternative Livestock Watering Systems*. |
| [`ut-extension-pb1641-alternative-livestock-watering-systems-capture-inbox-2026-04-18-extracted.md`](../../raw/processed/2026/ut-extension-pb1641-alternative-livestock-watering-systems-capture-inbox-2026-04-18-extracted.md) | Machine extract. |

---

## Related

- [`Electrical, networking, and Starlink — inbox batch (2026-04-23)`](electrical-networking-starlink-inbox-batch-2026-04-23.md) — adjacent **power / WAN / RF** ingest (different drop date).
