---
title: farmOS vs lightweight record stack for a two-site farm
page_type: comparison
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - farmos
  - records
  - two-site
review_status: unreviewed
confidence: medium
---

# farmOS vs lightweight record stack for a two-site farm

## Question

Given **two physical sites** (homestead + distant parcel), is **farmOS** (Drupal-backed) worth the **ops weight**, or does a **lightweight** stack (spreadsheets + HA helpers + minimal DB) fit **team size** and **integration** capacity?

## Criteria

| Criterion | farmOS | Lightweight (e.g. sheets + HA + PostGIS optional) |
|-----------|--------|-----------------------------------------------------|
| **Data model** | Rich **asset/log** model; modules | You design **discipline**; faster to drift |
| **Ops burden** | PHP/Drupal **hosting**, updates, backups | Smaller surface; **more** glue scripts |
| **Multi-site / org** | One instance can map **assets** to **geometry** | You merge **two** worlds manually |
| **Integrations** | API, community modules | MQTT → **your** DB rules |
| **Best when** | You want **auditable** agronomic records + maps | You have **minimal** IT time and **narrow** scope |

## Tradeoff summary

- **farmOS** when **records** and **geometry** are central and someone owns **hosting hygiene**.
- **Lightweight** when **telemetry → action** in Home Assistant is 90% of value and **records** are **secondary**.

## Links

- [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md)
- [`farmOS model — Assets (documentation capture)`](../source-notes/farmos-model-assets-documentation.md), [`farmOS model — Logs (documentation capture)`](../source-notes/farmos-model-logs-documentation.md)
- [`Telemetry system of record — boundaries and authority`](../analyses/telemetry-system-of-record-boundaries-and-authority.md) — authority matrix for records vs telemetry vs dashboards
- [`Dual-site operations model — non-agritourism farm business`](../analyses/dual-site-operations-model-non-agritourism.md)

---

*Team size and security patching cadence should dominate this choice as much as features.*
