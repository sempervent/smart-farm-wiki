---
title: Tennessee farm business compliance — official layer cluster (2026-04-22)
page_type: source_note
status: active
created: 2026-04-22
updated: 2026-04-22
source_ids:
  - raw/processed/2026/irs-ein-online-application-overview-capture-2026-04-22.md
  - raw/processed/2026/irs-responsible-parties-and-nominees-capture-2026-04-22.md
  - raw/processed/2026/tennessee-sos-business-services-official-url-index-capture-2026-04-22.md
  - raw/processed/2026/us-dol-wage-hour-agricultural-employment-overview-capture-2026-04-22.md
  - raw/processed/2026/fincen-boi-corporate-transparency-act-status-note-2026-04-22.md
  - raw/processed/2026/tennessee-business-tax-registration-licensing-tntap.md
  - raw/processed/2026/greenbelt.md
  - raw/processed/2026/building-a-farm-business-ut-center-of-farm-management.md
  - raw/processed/2026/tn-law-and-resources-pertaining-to-the-definition-of-agriculture-zoning-farm-property-taxes-multiple-use-subclassification.pdf
  - raw/processed/2026/w1266.pdf
tags:
  - tennessee
  - compliance
  - ingest-cluster
  - business
review_status: unreviewed
confidence: high
---

# Tennessee farm business compliance — official layer cluster (2026-04-22)

**Purpose**: **Router + provenance** for the **two-site East Tennessee** plan’s **business shell**: **entity** filing entry points (SOS/TNBEAR), **federal EIN / responsible party** (IRS captures), **federal agricultural employment** overview (DOL), **BOI/FinCEN posture** (status note + FinCEN hub), **business tax / TNTAP** snippet, **greenbelt** comptroller capture, **UT farm business** orientation page, **TN law PDF** on agriculture/zoning/taxes, and **UT W1266** insurance PDF. **Not** legal, tax, or insurance advice.

**Downstream package**: [`Tennessee farm business compliance package`](../topics/tennessee-farm-business-compliance-package.md)

## Evidence summary

| Field | Content |
|-------|---------|
| **Abstract** | Clusters **new 2026-04-22** IRS/DOL/SOS URL captures with **existing** TN Revenue / Comptroller / UT / statute PDF material already in `raw/processed/2026/` so synthesis pages can cite **primary-ish** paths without scattering orphans. |
| **Authority mix** | **Federal IRS + DOL .gov**, **TN SOS/Revenue/Comptroller captures**, **UT Extension PDF (W1266)**, **TN statute PDF** + **UT web capture** — still requires **CPA / attorney / agent** for *your* facts. |
| **Decision relevance** | Informs **entity choice**, **registration order** (state formation before EIN per IRS), **property tax classification** (greenbelt application discipline), **sales tax exemption** research (Revenue materials), **insurance** questions for agents, **labor** routing to WHD + TN workers’ comp, **BOI** “check FinCEN today” habit. |
| **Canonical wiki links** | [`Tennessee farm business compliance package`](../topics/tennessee-farm-business-compliance-package.md) · [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) · [`Farm business legal entity model`](../entities/farm-business-legal-entity-model.md) |

**Key claims** (public-safe):

- **IRS** states online EIN issuance is **single-session**, **15-minute** timeout, and **one EIN per responsible party per day** for online applications (see IRS capture).
- **IRS** states **nominees** must not be listed as responsible party on **Form SS-4**; corrections use **Form 8822-B** (see IRS capture).
- **Greenbelt** first-time application filing deadline is **March 15** for agricultural/forest/open space classification per **Comptroller/SBOE** capture text citing **T.C.A.** sections (see [`greenbelt.md`](../../raw/processed/2026/greenbelt.md)).
- **Agricultural land** minimum **15 acres** threshold (plus statutory alternatives) appears in the same **greenbelt** capture—verify against **current** statute and **county** assessor practice.
- **TNTAP** excerpt in vault notes **business tax** registration and **Public Chapter 377 (2023)** updating **$100,000** license thresholds for tax years ending on or after **Dec 31, 2023** (see [`tennessee-business-tax-registration-licensing-tntap.md`](../../raw/processed/2026/tennessee-business-tax-registration-licensing-tntap.md))—**re-verify** on Revenue site.

**Open questions / follow-ups**

- Add **machine extract** or refreshed **capture** for **TN SOS LLC** guide body if automated fetch remains blocked—until then the **URL index** raw file is the SOS anchor.
- **County** business license / zoning: **Anderson** vs **Campbell** clerks—keep **parcel** pages free of invented license facts.

---

## Per-source index

| Topic | Raw / source-note |
|-------|-------------------|
| IRS — EIN online overview | [`irs-ein-online-application-overview-capture-2026-04-22.md`](../../raw/processed/2026/irs-ein-online-application-overview-capture-2026-04-22.md) |
| IRS — Responsible parties / nominees | [`irs-responsible-parties-and-nominees-capture-2026-04-22.md`](../../raw/processed/2026/irs-responsible-parties-and-nominees-capture-2026-04-22.md) |
| TN SOS / TNBEAR URL index | [`tennessee-sos-business-services-official-url-index-capture-2026-04-22.md`](../../raw/processed/2026/tennessee-sos-business-services-official-url-index-capture-2026-04-22.md) |
| DOL WHD — agriculture overview | [`us-dol-wage-hour-agricultural-employment-overview-capture-2026-04-22.md`](../../raw/processed/2026/us-dol-wage-hour-agricultural-employment-overview-capture-2026-04-22.md) |
| BOI / CTA — status routing note | [`fincen-boi-corporate-transparency-act-status-note-2026-04-22.md`](../../raw/processed/2026/fincen-boi-corporate-transparency-act-status-note-2026-04-22.md) |
| TN business tax / TNTAP excerpt | [`tennessee-business-tax-registration-licensing-tntap.md`](../../raw/processed/2026/tennessee-business-tax-registration-licensing-tntap.md) · source-note [`tennessee-business-tax-registration-licensing-tntap.md`](tennessee-business-tax-registration-licensing-tntap.md) |
| Greenbelt law / application FAQ | [`greenbelt.md`](../../raw/processed/2026/greenbelt.md) |
| UT — building a farm business | [`building-a-farm-business-ut-center-of-farm-management.md`](../../raw/processed/2026/building-a-farm-business-ut-center-of-farm-management.md) |
| TN statute PDF — agriculture, zoning, property taxes | [`tn-law-and-resources-pertaining-to-the-definition-of-agriculture-zoning-farm-property-taxes-multiple-use-subclassification.pdf`](../../raw/processed/2026/tn-law-and-resources-pertaining-to-the-definition-of-agriculture-zoning-farm-property-taxes-multiple-use-subclassification.pdf) + extract |
| UT W1266 — insurance considerations | [`ut-extension-w1266-insurance-considerations-farming-operation-pdf.md`](ut-extension-w1266-insurance-considerations-farming-operation-pdf.md) |

## See also

- [`Authoritative execution evidence cluster — East Tennessee`](authoritative-execution-evidence-cluster-east-tennessee.md) — parent index (tax/agritourism rows)
- [`Inbox batch — Tennessee farm policy…`](inbox-batch-2026-04-18-tennessee-farm-lorawan-chirpstack-meshtastic-decentlab-halow.md) — broader TN policy + RF stack index
