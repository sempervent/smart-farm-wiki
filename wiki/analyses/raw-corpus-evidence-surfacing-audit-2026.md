---
title: Raw corpus vs wiki synthesis — evidence surfacing audit (2026)
page_type: analysis
page_subtype: meta_audit
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - raw
  - provenance
  - source-notes
  - meta
  - audit
review_status: unreviewed
confidence: medium
---

# Raw corpus vs wiki synthesis — evidence surfacing audit (2026)

## Purpose

**Durable audit** comparing **`raw/processed/2026/`** (immutable captures) to **`wiki/source-notes/`** and **canonical** synthesis (hubs, standards, analyses). **Goal**: name where the **raw layer is deeper** than the **visible** routing layer, and prioritize **Evidence summaries**, **cluster notes**, and **activation**—not one summary per file.

**Companion policy**: [`AGENTS.md`](../../AGENTS.md) (ingest activation + summarization). **Pattern**: [`Source-note abstract and evidence pattern`](../concepts/source-note-abstract-and-evidence-pattern.md).

---

## Methodology

| Step | What we compared |
|------|-------------------|
| **Corpus size** | File count under `raw/processed/2026/` (all types, ~**449** files at audit time). |
| **Wiki coverage** | `wiki/source-notes/*.md` referencing `raw/processed/2026/` paths (not 1:1—many raw files share one batch note). |
| **Integration** | Whether material appears on **canonical** pages, **hubs**, **standards**, or **Evidence summary** blocks—not only in `raw/`. |

**Limits**: This audit does **not** enumerate every orphan raw file; it **themes** gaps. Re-run after large ingest waves.

---

## Findings — corpus vs synthesis depth

| Theme | Raw depth (2026 tree) | Wiki surfacing | Gap / action |
|-------|------------------------|----------------|--------------|
| **PostgreSQL / farmOS / backup / DR** | Many captures: farmOS Docker, Longhorn/restic, k3s variants | Strong **doctrine** pages + [`Backup / DR — official documentation cluster`](../source-notes/backup-dr-official-documentation-cluster.md); [`homelab backup stack captures`](../source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md) | **Evidence summaries** on backup + farmOS doc batches (done in this pass where missing); keep **farmOS 2.x / PostgreSQL** truth on [`PostgreSQL and PostGIS — official documentation primary cluster`](../source-notes/postgresql-and-postgis-official-documentation-primary-cluster.md). |
| **Observability / alerts / secrets** | Frigate, SOPS, Flux, Alertmanager, Prometheus captures | [`Inbox batch — Frigate, SOPS, Prometheus…`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md) has **Evidence summary**; [`Grafana Alloy`](../source-notes/grafana-alloy-official-documentation-primary-reference.md) | **Low gap**—route from [`Platform doctrine package`](../topics/platform-doctrine-package-homelab-farm-edge.md). Optional: pin **versions** in runbooks when stack chosen. |
| **Frigate / local NVR** | Frigate intro + config captures | Same **Frigate batch** + [`Local video / NVR — role and deferral boundaries`](../analyses/local-video-nvr-role-and-deferral-boundaries-farm-stack.md) | **Boundary** is explicit; **SITE_FARM** deferral**—do not** duplicate NVR essays. |
| **MQTT / broker / eventing** | Mosquitto docs, many MQTT-adjacent raw files | [`Homelab, edge, and networking — inbox batch`](../source-notes/homelab-edge-networking-inbox-batch-2026-04-18.md) tables + [`Field telemetry reference architecture`](../analyses/field-telemetry-reference-architecture-homestead-120ac.md) | **Evidence summary** added; **broker SoR** remains on telemetry / platform analyses—**not** every MQTT blog in `raw/` needs a note. |
| **WireGuard / segmentation / DNS / certs** | WireGuard captures, OpenWrt PDF, Arch wiki extracts | [`Network segmentation…`](../analyses/network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md), [`Remote access…`](../analyses/remote-access-operational-security-model-two-site-smart-farm.md), [`Secrets and certificates — edge cluster standard`](../analyses/secrets-and-certificates-edge-cluster-standard.md), homelab batch | **Medium gap**: many **secondary** homelab essays in `raw/` are **not** indexed—**intentional**; **official** and **batch** paths carry the burden. |
| **Soil / irrigation / weather / agronomic sensors** | NRCS NEH, UT PBs, Decentlab/ChirpStack/LoRaWAN vendor pages, WSS | [`Authoritative execution evidence cluster`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md), [`Demory farm sensor layer cluster`](../source-notes/demory-farm-sensor-layer-official-and-operator-source-cluster.md), parcel / WSS notes | **Strong** for **East TN** execution; **residual** = **Claxton WSS AOI** and **measured** field rows—see [`missing data register`](../analyses/claxton-and-demory-missing-data-register.md). |
| **Roads / drainage / access** | FHWA gravel roads, Reddit erosion, UT/NRCS PDFs in batches | [`Authoritative roads and driveways — source cluster`](../source-notes/authoritative-roads-and-driveways-source-cluster.md) | **Cluster exists**; activate into **parcel / site inventory** when **field** evidence lands. |
| **Tennessee parcel / tax / greenbelt / startup / legal ops** | Many PDFs and captures (Revenue, agritourism, hobby farm, Smart Start) | [`Authoritative execution evidence cluster`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) tables + per-PDF source-notes | **Strong index**; **weak** where a PDF has **no** dedicated note—**defer** unless it changes a **gate**; prefer **batch** + **cluster** over **100** single-file notes. |

---

## Categories where raw ≫ visible synthesis (summary)

1. **Duplicate homelab imports** — multiple k3s/Longhorn/restic markdown captures overlap **intentionally**; synthesis lives in **platform + DR packages**, not in per-file wiki pages.
2. **Tennessee policy listicles / blogs** — captured for **search**; only **high-authority** or **gate-affecting** pieces earn **standalone** notes or **Evidence summaries**.
3. **Vendor sensor catalog pages** — clustered under **Demory sensor layer** and RF batches; **matrix** pages carry **decision** relevance.

---

## Prioritized backlog (not automatic work)

| Priority | Action |
|----------|--------|
| **P1** | When a **new** official batch lands: add or refresh **Evidence summary** on the **batch** source-note first. |
| **P1** | Link new **execution-grade** sources from [`Authoritative execution evidence cluster`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) **same PR** as ingest. |
| **P2** | Standalone source-notes for **orphan** high-value PDFs **only** if they change **business-plan validation gates**, **DR**, or **parcel** workflow. |
| **P3** | Periodic re-run of this audit after **>50** new `raw/processed/2026/` files. |

---

## Related

- [`Evidence hardening audit — East Tennessee (2026-04)`](evidence-hardening-audit-east-tennessee-two-site-2026-04.md) — prior **site-specific** pass.
- [`Source authority hardening audit`](source-authority-hardening-audit.md) — provenance stance.
- [`Ingest visibility gap — authoritative evidence vs published wiki`](ingest-visibility-gap-authoritative-evidence-east-tennessee.md) — IA diagnosis.
- [`Package artifact backlog — canonical East Tennessee packages`](package-artifact-backlog-canonical-packages-east-tennessee.md) — artifact + Evidence queue.
