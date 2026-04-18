---
title: Tennessee two-site — evidence hardening audit (2026-04)
page_type: analysis
status: active
created: 2026-04-25
updated: 2026-04-25
tags:
  - audit
  - evidence
  - two-site
  - execution
review_status: unreviewed
confidence: high
---

# Tennessee two-site — evidence hardening audit (2026-04)

## Purpose

**Durable record** of a **2026-04** pass to move the vault from **strong execution theory** toward a **more evidence-rich** **operational** knowledge base: **what** was **added**, **what** **gaps** **remain**, and **which** **canonical** **pages** **changed**. **Does not** claim parcel-specific facts—those still require **deed**, **field**, and **county** **work**.

**Spine**: [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) · [`Local site and county intelligence`](../topics/local-site-and-county-intelligence.md) · [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md).

---

## What was added (this pass)

### A. Local parcel, GIS, flood, climate — desk portals

- **New source-note**: [`Tennessee two-site — official parcel, GIS, flood, and climate portals`](../source-notes/tennessee-two-site-official-parcel-gis-flood-climate-portals.md) — **primary URLs** for **TN Property Viewer**, **Anderson** / **Campbell** **assessor** entry points, **WSS**, **USGS** elevation, **FEMA** MSC, **NOAA** climate normals.
- **Canonical updates**: [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md), [`Parcel intelligence package — East Tennessee two-site`](../topics/parcel-intelligence-package-east-tennessee-two-site.md), [`Parcel evidence intake and validation workflow — two-site`](parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md), [`Claxton home base — site intelligence`](claxton-home-base-site-intelligence.md), [`Demory farm — site intelligence`](demory-farm-site-intelligence.md) — **routing** and **desk** **checklists** (no **new** **acre** or **map-unit** claims).

### B. Physical infrastructure — locate, fence, water, irrigation

- **Grounding** (already ingested **`raw/`** batch): TN **811** captures, **UT Extension** **PB1541** / **PB1641** PDFs + extracts, **NRCS** **CPS 614** hub + **NEH Part 652** irrigation guide — indexed in [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md).
- **Canonical updates**: [`Infrastructure inventory baseline — both sites`](infrastructure-inventory-baseline-two-sites-east-tennessee.md), [`Field observation template package — two-site`](../topics/field-observation-template-package-east-tennessee-two-site.md) — **workflow** links and **non-parcel** **validation** **prompts**.

### C. Observability and secrets — doctrine layer

- **New source-note**: [`Grafana Alloy — official documentation (primary reference)`](../source-notes/grafana-alloy-official-documentation-primary-reference.md).
- **New synthesis**: [`Observability, secrets, and trust bar — homelab / farm edge`](observability-secrets-and-trust-bar-homelab-farm-edge.md) — Alertmanager **philosophy**, **SOPS/Flux**, **Alloy** as **optional**, **trust** **bar** for **remote** **ops**.
- **Canonical updates**: [`Monitoring and logging expectations — edge cluster standard`](monitoring-and-logging-expectations-edge-cluster-standard.md), [`Secrets and certificates — edge cluster standard`](secrets-and-certificates-edge-cluster-standard.md), [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md), [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md), [`Remote access and operational security model — two-site smart farm`](remote-access-operational-security-model-two-site-smart-farm.md).

### D. Video / NVR (Frigate)

- **New synthesis**: [`Local video / NVR — role and deferral boundaries (farm stack)`](local-video-nvr-role-and-deferral-boundaries-farm-stack.md) — **explicit** **deferral** + **boundaries**; **Frigate** docs remain in the **2026-04-18** inbox batch.
- **Canonical update**: [`Reference architecture — 5-acre home base + 120-acre farm`](reference-architecture-5ac-homebase-120ac-smart-farm.md) — **video** called out as **non-authoritative** for **welfare** / **production** **proof**.

### E. Hubs and index

- [`wiki/index.md`](../index.md) — audit + new analyses + portal source-note.
- [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md) — portal **row** (if not already present from parallel edit).
- [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md) — **audit** pointer under meta / steering.

---

## Execution gaps (still open)

| Gap | Why it remains | Next step (non-wiki) |
|-----|----------------|----------------------|
| **Deed-aligned AOI** for **~5 ac** and **~120 ac** **operating** polygons | Wiki **cannot** infer **legal** **boundaries** | Survey / deed / county **GIS** **tie** with **field** stakes |
| **Claxton WSS** AOI **capture** in `raw/` | Not yet filed for **homestead** footprint | Run WSS; file `raw/` + source-note per workflow |
| **FEMA** **FIRMette** or **LOMR** context for **structures** | **Desk** **screening** ≠ **permit** **determination** | **County** floodplain admin + **insurance** agent |
| **NOAA normals** → **microclimate** at **paddock** | Normals are **station** **statistics** | On-site **weather** **telemetry** + **seasonal** **log** |
| **811** **ticket** **history** for **planned** **trenches** | **Process** captured; **not** **project** **records** | Operator **tickets** + **Positive** **Response** **logs** |
| **Production** **observability** **stack** **choice** (Alloy vs **Prom**/**Loki** split) | **Team** and **hardware** **dependent** | [`Platform decision memo`](platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md) **pilot** **gate** |

---

## Canonical pages changed (checklist)

- [`Local evidence package — East Tennessee two-site`](../topics/local-evidence-package-east-tennessee-two-site.md)
- [`Parcel intelligence package — East Tennessee two-site`](../topics/parcel-intelligence-package-east-tennessee-two-site.md)
- [`Parcel evidence intake and validation workflow — two-site`](parcel-evidence-intake-and-validation-workflow-east-tennessee-two-site.md)
- [`Infrastructure inventory baseline — both sites`](infrastructure-inventory-baseline-two-sites-east-tennessee.md)
- [`Claxton home base — site intelligence`](claxton-home-base-site-intelligence.md)
- [`Demory farm — site intelligence`](demory-farm-site-intelligence.md)
- [`Field observation template package — two-site`](../topics/field-observation-template-package-east-tennessee-two-site.md)
- [`Monitoring and logging expectations — edge cluster standard`](monitoring-and-logging-expectations-edge-cluster-standard.md)
- [`Secrets and certificates — edge cluster standard`](secrets-and-certificates-edge-cluster-standard.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)
- [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md)
- [`Remote access and operational security model — two-site smart farm`](remote-access-operational-security-model-two-site-smart-farm.md)
- [`Reference architecture — 5-acre home base + 120-acre farm`](reference-architecture-5ac-homebase-120ac-smart-farm.md)
- [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md)
- [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md)
- [`wiki/index.md`](../index.md)
- [`wiki/log.md`](../log.md)

---

## Related

- [`Execution readiness gap audit — East Tennessee operational knowledge`](execution-readiness-gap-audit-east-tennessee-operational-knowledge.md) — **broader** **execution** **debt** (pre-dates this pass)
- [`Claxton and Demory — missing data register`](claxton-and-demory-missing-data-register.md) — **parcel** **unknowns**
