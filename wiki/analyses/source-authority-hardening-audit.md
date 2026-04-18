---
title: Source authority hardening audit
page_type: analysis
page_subtype: meta_audit
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - meta
  - epistemics
  - source-notes
  - provenance
review_status: unreviewed
confidence: high
---

# Source authority hardening audit

## Purpose

Track **where** the vault still leans on **low-authority** material (forums, Reddit, listicles, vendor marketing, informal blogs) for claims that normally require **extension**, **agency**, **standards**, **vendor primary documentation**, or **peer-reviewed** sources—and record **remediation**: authoritative clusters, reclassified support notes, and canonical page updates.

**Vocabulary**: [`Evidence grade and canonical authority`](../concepts/evidence-grade-and-canonical-authority.md) · [`Evidence grade` (glossary)](../glossary/evidence-grade.md).

**Rule**: **Exploratory** sources remain valuable for **ideas, ergonomics, and failure-mode color**; they must not **silently** anchor **financial, regulatory, safety, electrical, or backup** claims in canonical analyses.

---

## 1. Weak areas by domain

| Domain | Typical weak sources | Risk | Authoritative categories to prefer | Remediation (this pass) |
|--------|---------------------|------|-----------------------------------|---------------------------|
| **Unpaved roads / drainage** | Reddit (steep road, homestead), vendor blogs, retailer articles | Design and maintenance claims sound “peer-reviewed” when they are anecdotal | **FHWA**, state DOT gravel-road guidance, **NRCS** access-road PDFs, **academic/extension** bulletins (e.g. Penn State CDGRS), USFS low-volume manuals | [`Authoritative roads and driveways — source cluster`](../source-notes/authoritative-roads-and-driveways-source-cluster.md); [`FHWA — Gravel Roads…` (official reference)](../source-notes/fhwa-gravel-roads-maintenance-guide-official-reference.md); **topic** [`Rural road and driveway erosion sources`](../topics/rural-road-and-driveway-erosion-sources.md) reframed |
| **Field RF / MQTT bridges** | Reddit, Instructables | Misconfiguration and security assumptions | **Meshtastic** / **LoRaWAN** project docs, **MQTT** spec / broker docs | Topic points to [`Off-grid power, field RF, and WAN — source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md); Reddit/Instructables marked **low confidence** |
| **Homelab motivation** | Reddit threads | Low risk to ops if not used in DR/architecture | **Official** k3s/Longhorn/Rancher docs ([`Backup/DR cluster`](../source-notes/backup-dr-official-documentation-cluster.md)) | Topic disclaimer; existing **official** captures unchanged |
| **PostgreSQL / PostGIS “explainers”** | Medium, interview blogs | Internals explainers can drift from release behavior | **postgresql.org** / **postgis.net** reference manuals | New [`PostgreSQL and PostGIS — official documentation primary cluster`](../source-notes/postgresql-and-postgis-official-documentation-primary-cluster.md) |
| **NTP / PTP on Raspberry Pi** | Forum threads | Clock discipline claims for telemetry | **RFCs**, **IEEE 1588**, vendor HAT datasheets, **kernel/docs** | Forums remain **supporting**; canonical timing topics should cite standards when making precision claims |
| **Business formation (TN)** | Shopify/Zarla-style articles | Checklist drift vs current statute | **TN Secretary of State**, **TN Dept of Revenue**, **IRS** publications | Existing ingests include **TN Smart Start** PDF—prefer over blog checklists for **filing** facts |
| **Livestock / on-farm practice** | Permies, Reddit | Welfare and processing claims | **Extension**, **NRCS**, species **Code of Federal Regulations** where applicable | No purge—**classify**; enterprise economics already tied to **UT PDFs** where present |

---

## 2. Source-note classification (representative)

Low-authority notes used for **color** have been tagged with **`confidence: low`** and **`exploratory-social`** (or **`listicle-blog`**) where updated—see individual notes’ **Authority** lines.

**Not downgraded** (already strong or mixed official + secondary): [`Off-grid power, field RF, and optional WAN — source index`](../source-notes/off-grid-power-rf-wan-source-index-demory-planning-2026-04.md) (NREL, Victron, Meshtastic captures, Starlink specs), [`Backup / DR — official documentation cluster`](../source-notes/backup-dr-official-documentation-cluster.md), [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md).

---

## 3. Canonical pages touched

| Page | Change |
|------|--------|
| [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md) | **Evidence stance** paragraph: operational claims defer to official doc cluster + restore drills |
| [`Evidence grade and canonical authority`](../concepts/evidence-grade-and-canonical-authority.md) | Link to this audit |
| [`Rural road and driveway erosion sources`](../topics/rural-road-and-driveway-erosion-sources.md) | **Agency / standards first** narrative; exploratory list preserved but labeled |

---

## 4. Backlog (not closed)

| Item | Next ingest / action |
|------|---------------------|
| **FHWA gravel roads PDF** | Add `raw/processed` PDF + extract when corpus policy allows; until then use [`FHWA — official reference`](../source-notes/fhwa-gravel-roads-maintenance-guide-official-reference.md) URL |
| **Forum-heavy timing threads** | Replace precision claims with **RFC / IEEE** citations in any future **canonical** timing analysis |
| **Medium PostGIS/PostgreSQL primers** | Prefer **official** cluster for **release-specific** behavior; keep Medium as **pedagogy only** |

---

## Related

- [`Structural audit — page ownership, entity gaps, and hub routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md)
- [`Ingest visibility gap — authoritative evidence vs published wiki`](ingest-visibility-gap-authoritative-evidence-east-tennessee.md)
- [`Execution readiness gap audit — East Tennessee`](execution-readiness-gap-audit-east-tennessee-operational-knowledge.md)
