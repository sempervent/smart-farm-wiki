---
title: Package artifact backlog — canonical East Tennessee packages
page_type: analysis
page_subtype: meta_audit
status: active
created: 2026-04-25
updated: 2026-04-25
tags:
  - backlog
  - meta
  - two-site
  - packages
review_status: unreviewed
confidence: medium
---

# Package artifact backlog — canonical East Tennessee packages

## Purpose

**Ranked, durable backlog** of **structured artifacts** (matrices, standards, runbooks, checklists) that would **complete** major **canonical packages** without duplicating [`Implementation backlog — strategic audit`](implementation-backlog-strategic-audit.md) (P0–P3 product work). **Second table**: **Evidence summary** adoption queue for **cluster** source-notes that still lack the block per [`Source-note abstract and evidence pattern`](../concepts/source-note-abstract-and-evidence-pattern.md).

**Policy**: [`AGENTS.md`](../../AGENTS.md) — ingest **activation**, Evidence summaries, **structural vs integration** validation.

**Related**: [`Evidence hardening audit (2026-04)`](evidence-hardening-audit-east-tennessee-two-site-2026-04.md) · [`Domain content overview`](domain-content-overview.md) (strand backlog) · [`Execution readiness gap audit — East Tennessee`](execution-readiness-gap-audit-east-tennessee-operational-knowledge.md).

---

## Ranked backlog — missing structured artifacts

| Priority | Artifact | Package / owner | Gap | Suggested canonical home |
|----------|----------|-----------------|-----|----------------------------|
| **P0** | **Parcel / WSS AOI** row in worksheets when **Claxton** homestead AOI is filed | Local evidence / parcel | **Homestead** soils still **unknown** in vault vs **Demory** WSS session | Extend [`Parcel intelligence — Claxton`](../analyses/parcel-intelligence-claxton-home-base-east-tennessee-two-site.md); cite new `raw/` + source-note |
| **P0** | **WAN seasonal reliability** log template (outages, handoff) | Connectivity / validation | [`Validation plan`](../analyses/validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md) references **CS-2** evidence | Add **subsection or appendix** table on [`Connectivity strategy`](../analyses/connectivity-strategy-for-claxton-and-demory.md) or validation plan—**not** a third essay |
| **P1** | **Off-grid energy budget** worksheet (P_crit, radio tiers) filled | Off-grid Demory | [`Off-grid operational decision rules`](../analyses/off-grid-operational-decision-rules-power-and-networking-demory-farm.md) **DR-1** needs **numbers** | Single **template** section in [`Off-grid power domains and battery tiers`](../analyses/off-grid-power-domains-and-battery-tiers-demory-farm.md) or loads bridge |
| **P1** | **Restore drill record** (date, tier, pass/fail) | Backup / DR | Runbook exists; **proof** cadence is standard-level | [`Backup validation cadence — farm stack standard`](../analyses/backup-validation-cadence-standard-farm-stack.md) — add **one** example table row pattern |
| **P1** | **Sensor pilot subset** selection record (which rows of matrix are Phase 0–1) | Sensors / Demory | Matrix is wide; **pilot** scope needs explicit **subset** | [`Farm sensor architecture — Demory`](../analyses/farm-sensor-architecture-demory-farm-site.md) **Pilot** section or [`Sensor checklist matrix`](../analyses/sensor-checklist-matrix-for-demory-farm.md) **Recommended phase** column already present—add **“pilot default”** note when field picks rows |
| **P2** | **Starlink / LTE cost ledger** (quarterly) | Business / connectivity | **CS-1** stop rule needs **ledger** habit | [`Enterprise unit economics`](../analyses/enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md) or validation plan **Connectivity** subsection |
| **P2** | **Farm cybersecurity** topic hub (CISA ingests → policy) | Security / remote access | [`Domain content overview`](domain-content-overview.md) backlog item | **New topic hub** only when ready—until then, extend [`Remote access and operational security model`](../analyses/remote-access-operational-security-model-two-site-smart-farm.md) **Links** |

---

## Standards / runbooks / checklists — status (spot check)

| Kind | Example | Status |
|------|---------|--------|
| **Standard** | [`Secrets and certificates — edge cluster`](../analyses/secrets-and-certificates-edge-cluster-standard.md), [`Monitoring and logging expectations`](../analyses/monitoring-and-logging-expectations-edge-cluster-standard.md) | **Exist** — extend with version pins when stack chosen |
| **Runbook** | [`Runbook — broker or backhaul down`](../analyses/runbook-broker-or-backhaul-down.md), [`Runbook — power loss at remote site`](../analyses/runbook-power-loss-remote-site.md) | **Exist** — tie to **pilot** drills |
| **Checklist** | [`Field observation template package`](../topics/field-observation-template-package-east-tennessee-two-site.md) | **Exists** — activate rows as **measured** facts land |
| **Matrix** | [`Sensor checklist matrix — Demory`](../analyses/sensor-checklist-matrix-for-demory-farm.md), [`Instrumentation priority matrix`](../analyses/instrumentation-priority-matrix-two-site-smart-farm.md) | **Exist** — **narrow** pilot via architecture page |

**Gap summary**: Few **net-new** large artifacts required; **highest leverage** is **filling** worksheets, **energy** numbers, and **WAN**/**drill** **evidence** rows—not new essay pages.

---

## Evidence summary adoption queue (source-note clusters)

**Already have** Evidence summary blocks (skip): [`authoritative-execution-evidence-cluster-east-tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md), [`backup-dr-official-documentation-cluster`](../source-notes/backup-dr-official-documentation-cluster.md), [`off-grid-power-rf-wan-source-index-demory-planning-2026-04`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md), [`authoritative-roads-and-driveways-source-cluster`](../source-notes/authoritative-roads-and-driveways-source-cluster.md), [`inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md), plus sensor / portal / electrical / LoRaWAN batch / k3s / Grafana notes (2026-04 policy pass).

| Rank | Source-note (add Evidence summary next) | Why |
|------|----------------------------------------|-----|
| **1** | [`homelab-backup-stack-official-captures-inbox-2026-04-18`](../source-notes/homelab-backup-stack-official-captures-inbox-2026-04-18.md) | Pairs **DR doctrine**; large capture batch |
| **2** | [`farmos-documentation-captures-inbox-2026-04-18`](../source-notes/farmos-documentation-captures-inbox-2026-04-18.md) | **Records** / asset model—execution-critical |
| **3** | [`web-soil-survey-home-page-inbox-2026-04-18`](../source-notes/web-soil-survey-home-page-inbox-2026-04-18.md) + [`Campbell County — WSS AOI soil map tab`](../source-notes/campbell-county-wss-aoi-soil-map-tab-capture-2026-04-18.md) | **Parcel** / soils **process**—scanning surface |
| **4** | [`cisa-guide-securing-remote-access-software-508-pdf`](../source-notes/cisa-guide-securing-remote-access-software-508-pdf.md) (or **joint OT cluster** if merged later) | **Remote access** doctrine |
| **5** | [`nrcs-fy25-conservation-scenarios-pdf`](../source-notes/nrcs-fy25-conservation-scenarios-pdf.md) | Large **planning** PDF—abstract helps **scope** |

**Defer**: Single-file **bill** or **one-off** captures unless promoted to a **cluster** index.

---

## Related

- [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md)
- [`Procedural guides package strategy`](../topics/procedural-guides-package-strategy-smart-farm-wiki.md)
