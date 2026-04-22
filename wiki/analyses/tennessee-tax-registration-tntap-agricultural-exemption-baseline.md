---
title: Tennessee tax registration, TNTAP, and agricultural exemption baseline
page_type: analysis
page_subtype: operational_guide
status: active
operational_maturity: draft
created: 2026-04-22
updated: 2026-04-22
review_status: unreviewed
confidence: high
tags:
  - tennessee
  - tax
  - tntap
source_ids:
  - raw/processed/2026/tennessee-business-tax-registration-licensing-tntap.md
  - raw/processed/2026/agricultural-exemption.md
---

# Tennessee tax registration, TNTAP, and agricultural exemption baseline

## A — Business tax / TNTAP (Department of Revenue)

**Official snippet** in vault: [`tennessee-business-tax-registration-licensing-tntap.md`](../../raw/processed/2026/tennessee-business-tax-registration-licensing-tntap.md) + source-note [`tennessee-business-tax-registration-licensing-tntap.md`](../source-notes/tennessee-business-tax-registration-licensing-tntap.md).

| Element | Official content (high level) | Operator action |
|---------|------------------------------|-----------------|
| Registration channel | **TNTAP** | Create login; store credentials securely |
| Tax base | **Business tax** on **gross receipts** (annual) | **CPA** maps revenue streams |
| County license fee | **$15** registration fee note (excerpt) | Pay county/municipal clerk per excerpt |
| License bands | **Minimal** vs **standard** tied to receipts; **PC 377 (2023)** updates **$100k** thresholds for TY ending **≥ 12/31/2023** | Re-verify on **Revenue** site before relying |

## B — Agricultural sales tax exemption (Department of Revenue)

| Element | Source | Gate |
|---------|--------|------|
| Program summary + **>50%** use framing (extension-oriented capture) | [`agricultural-exemption.md`](../../raw/processed/2026/agricultural-exemption.md) + UT orientation [`building-a-farm-business-ut-center-of-farm-management.md`](../../raw/processed/2026/building-a-farm-business-ut-center-of-farm-management.md) | **CPA** validates **purchases** vs **qualified agricultural** use |
| Official PDF publication | [`tn-revenue-agricultural-exemption-jan2023-pdf.md`](../source-notes/tn-revenue-agricultural-exemption-jan2023-pdf.md) | Read tables for **eligible items** |

## C — Recommendations

- Run **TNTAP** and **county clerk** steps in the **same season** as entity formation to avoid operating **unlicensed** per Revenue excerpt’s “not allowed to operate until license obtained” language for in-state businesses over **$3,000** receipts.

## D — Two-site nuance

- **Receipts** may originate primarily at **`SITE_FARM`** while **admin** sits at **`SITE_HOME`**—mapping must be **CPA-grade**, not wiki-speculated.

## See also

- [`Tennessee farm business compliance package`](../topics/tennessee-farm-business-compliance-package.md)
- [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md)
