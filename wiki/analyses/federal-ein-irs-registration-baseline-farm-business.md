---
title: Federal EIN and IRS registration baseline — farm business
page_type: analysis
page_subtype: operational_guide
status: active
operational_maturity: draft
created: 2026-04-22
updated: 2026-04-22
review_status: unreviewed
confidence: high
tags:
  - irs
  - ein
  - farm-business
source_ids:
  - raw/processed/2026/irs-ein-online-application-overview-capture-2026-04-22.md
  - raw/processed/2026/irs-responsible-parties-and-nominees-capture-2026-04-22.md
---

# Federal EIN and IRS registration baseline — farm business

## Official requirements (IRS — verify on IRS.gov)

| Topic | Requirement / mechanic | Source |
|-------|-------------------------|--------|
| **Online session** | One sitting; **15-minute** inactivity timeout | [`irs-ein-online-application-overview-capture-2026-04-22.md`](../../raw/processed/2026/irs-ein-online-application-overview-capture-2026-04-22.md) |
| **Responsible party** | Must be a **person** with **SSN or ITIN** (exceptions for government entities) | [`irs-responsible-parties-and-nominees-capture-2026-04-22.md`](../../raw/processed/2026/irs-responsible-parties-and-nominees-capture-2026-04-22.md) |
| **Nominees** | **Cannot** apply; should not be on **Form SS-4** | same |
| **Daily cap** | **1** online EIN per **responsible party** per day | [`irs-ein-online-application-overview-capture-2026-04-22.md`](../../raw/processed/2026/irs-ein-online-application-overview-capture-2026-04-22.md) |
| **State-first** | For LLC/corp/partnership, IRS advises forming **state entity** before EIN to reduce delay | same |
| **Ongoing filing** | After EIN, file required **tax** and **information** returns | same |
| **Responsible party changes** | **Form 8822-B**; IRS discusses **60-day** reporting window | [`irs-responsible-parties-and-nominees-capture-2026-04-22.md`](../../raw/processed/2026/irs-responsible-parties-and-nominees-capture-2026-04-22.md) |

## Operational recommendations

- Store **EIN confirmation letter** with **formation docs** and **TNTAP** registration screenshots in **private** evidence store (not wiki).
- Align **farm legal name** on insurance, bank, and **TNTAP** to reduce mismatch friction.

## Professional gates

- **CPA** for whether you need EIN **before** employees (often yes) and for **payroll** / **1099** flows.
- **Attorney** if **ownership** changes should trigger **new EIN** vs updates—see IRS “when to get a new EIN” pages.

## BOI cross-link

- IRS EIN page reminds some entities of **FinCEN beneficial ownership** reporting—treat as **separate** obligation with **fast-changing** enforcement: [`Beneficial ownership information reporting — FinCEN / CTA status`](beneficial-ownership-information-reporting-fincen-status.md)

## See also

- [`Tennessee LLC formation and annual report checklist`](tennessee-llc-formation-annual-report-checklist.md)
- [`Tennessee farm business compliance package`](../topics/tennessee-farm-business-compliance-package.md)
