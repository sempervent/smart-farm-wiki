---
title: Anderson County vs Campbell County — two-site operating implications
page_type: comparison
status: active
created: 2026-04-22
updated: 2026-04-23
tags:
  - two-site
  - tennessee
  - anderson-county
  - campbell-county
review_status: unreviewed
confidence: medium
aliases:
  - Anderson vs Campbell county operating implications
---

# Anderson County vs Campbell County — two-site operating implications

**Purpose**: Compare **county-context** factors that **shape** the **Claxton** (`SITE_HOME`) + **Demory** (`SITE_FARM`) two-site pattern—**without** treating **county averages** as **parcel truth**.

**Sites**: [`Claxton home base — site intelligence`](../analyses/claxton-home-base-site-intelligence.md), [`Demory farm — site intelligence`](../analyses/demory-farm-site-intelligence.md). **Package**: [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md).

---

## County-level data (2024 NASS cash rents)

**Source**: USDA NASS *Cash Rents County Estimates – 2024* (TN); [`nass-cash-rents-all-crops-tn-2024.pdf`](../../raw/processed/2026/nass-cash-rents-all-crops-tn-2024.pdf).

| County | Non-irrigated cropland ($/ac) | Irrigated cropland | Pastureland |
|--------|-------------------------------|--------------------|-------------|
| **Anderson** | **28.50** | `--` | `--` |
| **Campbell** | **27.50** | `--` | `--` |

`--` = not published at county level in this release (see footnotes in PDF).

**Reading**: **~$1/ac** difference in **non-irrigated cropland** rent **estimates** is **noise** vs real lease negotiation, **field quality**, and **term length**—use for **ballpark** only.

---

## Where Anderson County fits **home-base** functions better (planning bias)

| Factor | Anderson (Claxton anchor) | Why it matters |
|--------|---------------------------|----------------|
| **Service / retail / labor market depth** | **Generally** closer to **Knoxville MSA** services than **Campbell** hinterland (qualitative). | Easier **same-day** parts, **trades**, and **coverage** swaps for **homelab**, **records**, and **family** staging. |
| **Homestead “brain” role** | Matches **SITE_HOME** entity: **broker**, **backups**, **patch cadence**, **office** work. | Keeps **heavy** cognitive load off **field** time—see [`Reference architecture`](../analyses/reference-architecture-5ac-homebase-120ac-smart-farm.md). |

**Caveat**: **One address** in Anderson can still have **poor** broadband or **long** private drive service issues—**verify**.

---

## Where Campbell County conditions **shape farm** operations

| Factor | Campbell (Demory anchor) | Why it matters |
|--------|--------------------------|----------------|
| **Processed WSS AOI** (vault) | **Sloped**, **gravelly** map units dominate captured AOI (**FbF / FbD / TaF**); **558.6 ac** reported AOI. | **Earthwork**, **lanes**, **fence**, **stock water**, and **sediment** bind **operating cost** and **labor**—see [`Demory farm — site intelligence`](../analyses/demory-farm-site-intelligence.md). |
| **Lease economics (NASS)** | **Slightly lower** county **non-irrigated cropland** rent estimate than Anderson. | **Directional** only; **your** lease/custom-hire terms dominate. |
| **Distance from home base** | **~35 min** planning default (family)—not a county statistic. | Drives **trip batching**, **telemetry** value, and **enterprise** choice—[`Two-site operating model`](../analyses/two-site-operations-model-5ac-homebase-120ac-production.md). |

---

## Risks of over-generalizing county data to **your** parcels

| Risk | Mitigation |
|------|------------|
| **NASS rent** ≠ your **lease**, **cash rent**, or **share** terms | Use **contracts** and **comps** from **your** market radius, not county row alone. |
| **County soil survey** ≠ **AOI** polygon | **Re-run WSS** on **each** deed footprint; **clip** map units to **fields**. |
| **“Anderson has better utilities”** as blanket truth | **Test** bandwidth and **electrical** service at **each** site. |
| **Campbell = always steep** | **Micro-pockets** of better land exist; **walk** and **soil test**. |
| **Combining counties in one insurance / tax story** | **Two parcels** can imply **two** jurisdictions for **some** programs—**ask** agents and **DOR** (see [`Authoritative execution evidence cluster`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md)). |

---

## Related

- **County entities**: [`Anderson County, Tennessee (two-site context)`](../entities/anderson-county-tennessee.md), [`Campbell County, Tennessee (two-site context)`](../entities/campbell-county-tennessee.md)
- **Place entities**: [`Claxton home base (place)`](../entities/claxton-home-base.md), [`Demory farm site (place)`](../entities/demory-farm-site.md)
- [`Execution readiness gap audit`](../analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md)
- [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md)
