---
title: Farm accounting baseline — chart of accounts and enterprise P&L structure
page_type: analysis
status: draft
created: 2026-04-18
updated: 2026-04-22
review_status: unreviewed
tags:
  - accounting
  - two-site
  - chart-of-accounts
  - enterprise
confidence: low
---

# Farm accounting baseline — chart of accounts and enterprise P&L structure

## Purpose

Define a **wiki-native accounting skeleton** so that **books**, **enterprise unit worksheets**, and **milestones** speak the same language. This page is **not tax advice**; it is a **structuring template** for records and internal P&L views. Align with your CPA on **tax** vs **management** accounts.

**Pairs with**: [`Enterprise unit economics — worksheet methodology`](enterprise-unit-economics-worksheet-methodology-two-site-smart-farm.md), [`Revenue milestone model`](revenue-milestone-model-supplemental-to-salary-replacement.md), [`East Tennessee two-site farm business plan — capital and financing`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md), [`Tennessee farm business compliance package`](../topics/tennessee-farm-business-compliance-package.md) (entity + tax **registration** before books go live).

---

## Required inputs

| Input | Description |
|-------|-------------|
| **Legal entities** | One schedule F vs LLC vs multiple—**decision with advisor** |
| **Enterprise list** | Same IDs as unit economics worksheets (`E1`, `E2`…) |
| **Site tags** | Which costs are **`SITE_HOMESTEAD`**, **`SITE_FARM`**, **shared** |
| **Allocation rules** | How hay, fuel, utilities, equipment hours split **between enterprises** |
| **Inventory method** | Feed, livestock, crop—**cash vs accrual** management view |
| **Family compensation policy** | Draw vs W-2 vs none—**placeholder** until professional advice |

---

## Outputs supported

| Output | Use |
|--------|-----|
| **Consistent account labels** | Import into QuickBooks / FarmBooks / spreadsheet |
| **Enterprise P&L rollup** | See each **E** as a column quarterly |
| **Split-site reporting** | Filter by site tag for CAPEX/OPEX sequencing |
| **Milestone evidence** | **M0–M4** tie to **documented** revenue and expense classes |
| **Working capital visibility** | Prepaid / AP / inventory rows visible **monthly** |

---

## Assumptions

| Assumption | Note |
|------------|------|
| **Management P&L ≠ tax return** | You may mirror Schedule F categories for sanity but add **management** dimensions (enterprise, site). |
| **Inter-site transfers** | Moves of equipment or hay between sites need **internal memo** pricing or **transfer at cost** rule—pick one and document. |
| **Automation** | Software, sensors, cloud, and **cell** bills are **real OPEX**—tag by **system** (telemetry vs office). |

---

## Placeholders until real numbers exist

| Placeholder | Meaning |
|-------------|---------|
| Account **numbers** | Your numbering scheme—fill when software chosen |
| **Allocation %** | Replace `___%` with agreed rules per quarter |
| **Opening balances** | Year-start inventory and cash—**per books** |

---

## Chart of accounts — template (expand / renumber)

**Assets** (balance sheet — summary)

| Range / ID | Account name | Site tag | Notes |
|------------|--------------|----------|-------|
| 1xxx | Cash — operating | shared | |
| 1xxx | Cash — tax escrow | shared | optional |
| 1xxx | Accounts receivable | | |
| 1xxx | Inventory — feed | farm | |
| 1xxx | Inventory — crop / product | farm | |
| 1xxx | Inventory — livestock | farm | method TBD |
| 1xxx | Prepaid expenses | | split by schedule |
| 1xxx | Fixed assets — equipment | tag by primary location | depreciation schedule |
| 1xxx | Fixed assets — buildings / improvements | homestead vs farm | |

**Liabilities & equity** — template only; **structure with accountant**.

---

## Income accounts (by enterprise and channel)

| Income account | Enterprise tag | Channel (auction, direct, wholesale) | Notes |
|----------------|----------------|--------------------------------------|-------|
| Product sales — E1 | E1 | | |
| Product sales — E2 | E2 | | |
| Agritourism / services — E_ | | | if applicable |
| Government / insurance indemnity | | | separate—non-operating flag optional |
| Interest / other | | | keep **non-operating** visible |

---

## Expense accounts — operating (map to Schedule F–like buckets where helpful)

| Expense group | Examples | Enterprise allocation method |
|---------------|----------|-------------------------------|
| **Crop / feed / inputs** | Seed, fertilizer, feed | By **enterprise** job or **%** |
| **Livestock purchases** | Feeder cattle, breeding stock | Direct to **E** |
| **Vet / medicine** | | Direct + **head-day** allocation |
| **Fuel & oil** | Field + transport | **Mile log** + **equipment hour** meter |
| **Repairs — equipment** | | By **hour** or **site** |
| **Repairs — structures** | | By **site tag** |
| **Custom hire** | Hay, trucking | Direct to **E** |
| **Labor — hired** | W-2 / 1099 | Time cards → **E** |
| **Family labor imputation** | **Not** in tax books usually—**management column only** | See milestone model shadow rate |
| **Insurance** | Crop, liability, vehicle | **%** revenue or **asset** split—document |
| **Utilities** | Electric (shop, cold, pump) | **Meter** ID → **site** → **E** if allocatable |
| **Software / IT / telemetry** | farmOS, cloud, LTE | Tag **automation stack**; split homestead NOC vs field gateways |
| **Professional fees** | CPA, legal | Often overhead—**not** buried in crop COGS without rule |
| **Interest** | Equipment / land | Tie to **which asset** financed |
| **Rent / lease — land** | | Often **overhead** then allocate |

---

## Enterprise P&L — rollup template (quarterly)

| Line | E1 | E2 | E3 | Farm total |
|------|----|----|-----|------------|
| Revenue | | | | |
| − Variable COGS (your definition) | | | | |
| **= Contribution margin** | | | | |
| − Allocated overhead (rule: `___`) | | | | |
| **= Operating margin (management)** | | | | |

**Overhead allocation rule (placeholder)**: e.g. **by labor hours**, **by gross revenue %**, **by machine hours**—state **one primary** and **one sensitivity** method.

---

## Split-site columns (optional management view)

| Line | SITE_HOMESTEAD | SITE_FARM | Unallocated |
|------|----------------|------------|---------------|
| Revenue | | | |
| Site-specific OPEX | | | |
| Shared OPEX allocation | | | |

Use this for [`CAPEX/OPEX sequencing`](capex-opex-enterprise-sequencing-two-site-constraint.md) and **duplicate vs consolidate** decisions.

---

## Phased capital vs expense (reminder)

| Spend type | Typical treatment | Wiki tracking |
|------------|-------------------|---------------|
| **Sensor kit under capitalization threshold** | Expense | Telemetry OPEX account |
| **Major equipment** | Capitalize + depreciate | Fixed asset + depreciation |
| **Soil / pasture improvement** | Varies—**advisor** | Separate project tag |

---

## Disclaimer

This page supports **internal planning and wiki discipline**. **Tax, entity choice, and depreciation** require a qualified professional. Do not use wiki tables as filing documents.

---

## Links

- [`East Tennessee two-site farm business plan — revenue model and milestones`](east-tennessee-two-site-farm-business-plan-revenue-and-phased-income.md)
- [`Instrumentation ROI model`](instrumentation-roi-model-two-site-smart-farm.md) — OPEX and labor lines for automation
- [`UT Extension — Farm Management Boot 2017 budgets`](../source-notes/ut-extension-fm-boot-2017-budgets-velandia-pdf.md) — example **line-item** patterns (not current dollars)
