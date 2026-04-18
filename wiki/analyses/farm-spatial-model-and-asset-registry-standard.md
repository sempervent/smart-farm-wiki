---
title: Farm spatial model and asset registry standard
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-22
aliases:
  - Spatial data and farm asset registry standard
tags:
  - gis
  - assets
  - registry
  - postgis
review_status: unreviewed
confidence: medium
---

# Farm spatial model and asset registry standard

## Purpose

Define a **minimal, practical standard** so **parcels, paddocks, infrastructure, equipment, and telemetry endpoints** share stable **IDs** and can sit on a **map** (GIS layer or simple sketch) without requiring a survey-grade cadastre on day one. This is **glue** between **land** and **digital** systems—[`Strategic audit`](strategic-audit-decision-safe-operations.md) calls this a **critical gap** when farmOS or sensors float without **earth-anchored** names.

**farmOS alignment**: The **Asset** and **Log** abstractions in farmOS ([`Assets`](../source-notes/farmos-model-assets-documentation.md), [`Logs`](../source-notes/farmos-model-logs-documentation.md)) should **inform** how you name **equipment** and **sensor** assets in this registry—not mandatory software choice.

## Scope

- **In scope**: Naming pattern, **minimum fields** for registry rows, **layer** ideas, and **coordinate assumptions**.
- **Out of scope**: Legal boundary disputes; **subdivision**; professional surveying unless you later engage one.

## Assumptions

| Assumption | Notes |
|------------|--------|
| You may use **PostGIS**, **farmOS geometries**, **KML**, or **even a paper map photo** initially—**discipline of IDs** matters more than software brand. |
| **One “operating map”** should be agreed: *where is the current truth for boundaries?* **`MAP_AUTHORITY_LABEL`** = TBD (file name, farmOS layer, or GIS project). |
| **CRS**: If you mix WGS84 and a projected CRS, **document** the rule (e.g. “store WGS84 lon/lat for points; use **EPSG:XXXX** for distance math in GIS”). Replace **`EPSG_PLACEHOLDER`**. |
| **Campbell / Demory WSS** | Vault capture shows **558.6 ac** AOI **≠** **~120 ac** planning label—**operating** map must **clip** to **management** boundary ([`Demory site intelligence`](demory-farm-site-intelligence.md)). |

**What changed**: Named **county** evidence **forces** explicit **AOI vs deed vs operating acres**—no silent conflation in IDs.

## Identity pattern (draft)

**Sites** (top level):

- `SITE_A` = homestead placeholder code (e.g. `HMS`)
- `SITE_B` = farm placeholder code (e.g. `F120`)

**Land units** (examples—adjust vocabulary to your operation):

| Unit type | Example ID | Notes |
|-----------|------------|--------|
| Parcel / property block | `SITE_B-PARCEL-01` | **Not** legal description—operating label only. |
| Paddock / field | `SITE_B-F05` | Short, stable; no renaming seasonally unless you accept **broken history**. |
| Structure | `SITE_B-BARN-01`, `SITE_A-SHED-01` | Point or footprint polygon when known. |
| Linear | `SITE_B-LANE-N` | Roads, lanes—useful for **access** during mud/ice. |

**Assets** (equipment and fixed infrastructure):

| Field | Required? | Example |
|-------|-----------|---------|
| `asset_id` | Yes | `SITE_B-TR-001` |
| `site` | Yes | `SITE_B` |
| `category` | Yes | tractor, ATV, generator, pump, tank, gateway |
| `make_model` | If known | free text |
| `serial` | If known | **Redact** in shared copies if sensitive |
| `primary_location` | Yes | paddock ID, barn bay, or “stored @ `SITE_A`” |
| `power_source` | For field gear | solar/battery/grid/none |
| `telemetry_device_id` | If any | must match **broker/GPS** naming—see telemetry architecture |

**Telemetry endpoints** (must link to land or asset):

| Field | Required? |
|-------|-----------|
| `device_id` | Yes (global uniqueness) |
| `mounted_at` | `asset_id` **or** `lat/lon` **or** `paddock_id` |
| `measurement` | e.g. tank depth, gate open, soil VWC |

## Key questions

1. **Who owns the polygon** for each paddock—same person who maintains **fence**?
2. **When a sensor moves**, is it a **new** `device_id` or a **migration** event in a log?
3. **farmOS / PostgreSQL / spreadsheet**: which is **canonical** for **asset list** vs **geometry**? (See future **telemetry system of record** analysis.)
4. **Public sharing**: which layers are **never** exported (gates, cameras)?

## Decision criteria

| Situation | Recommendation |
|-----------|----------------|
| **Fewer than ~20** land units | Spreadsheet + map screenshot may suffice **if** IDs are stable. |
| **Overlapping uses** (graze + hay + crop) | Prefer **seasonal management zones** as attributes, **not** new polygons every year—**or** accept versioning. |
| **Telemetry scaling** | **Enforce** `device_id` ↔ `paddock_id` linkage **before** adding sensors—see audit **technology ↔ land** gap. |

---

## Architecture package — minimum standard (two-site smart farm)

**Hub**: [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md). **Authority** for **map vs books vs telemetry**: [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md).

| Minimum rule | Rationale |
|----------------|-----------|
| **Stable `site` + land-unit IDs** before **device** sprawl | **History** and **runbooks** reference **place** |
| **`device_id` ↔ `paddock_id` or `asset_id`** for every field endpoint | **Otherwise** dashboards are **unmoored** |
| **One `MAP_AUTHORITY_LABEL`** | **Single** **operating** map—paper or GIS |
| **Migration log** when **sensors** **move** | **Avoid** **silent** **history** **break** |

---

## Authoritative land-intelligence references (external)

Use **official** soil and elevation products to **inform** map layers and **labels**—not as a substitute for **field verification** or **local permits**.

| Source | Role in this wiki |
|--------|-------------------|
| **Web Soil Survey / SSURGO** | Map-unit capability, limiting factors; see [`Web Soil Survey & 3D Elevation — captures`](../source-notes/web-soil-survey-and-elevation-captures-inbox-2026-04-18.md) |
| **3DEP / lidar-backed elevation** | Drainage / cut-fill context; same capture note |
| **County septic / SSDS** | Buildability near structures; [`Tennessee onsite sewage / septic captures`](../source-notes/tn-onsite-sewage-septic-captures-inbox-2026-04-18.md) |

**Index**: [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md). **Gap audit**: [`Execution readiness gap audit`](../analyses/execution-readiness-gap-audit-east-tennessee-operational-knowledge.md).

---

## Links to related future or existing pages

- [`PostGIS — complete workflow (capture)`](../source-notes/postgis-complete-workflow.md) — workflow narrative.
- [`Data storage (farm and edge stacks)`](../concepts/data-storage.md) — PostgreSQL/PostGIS docs.
- [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md) — farmOS as possible **geometry + records** home.
- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md) — where **devices** sit in the stack.
- [`Weekly coverage matrix — two-site farm operations`](weekly-coverage-matrix-two-site-farm-operations.md) — who is **on site** to verify map vs reality.
- Future **entity pages** under `entities/` for **`SITE_A` / `SITE_B`** when real (see [`Implementation backlog`](implementation-backlog-strategic-audit.md)).

## Open items

- [ ] Choose **`MAP_AUTHORITY_LABEL`** and record path or URL (internal).
- [ ] Create **empty** registry table (sheet or DB) with column headers above.
- [ ] Walk fence lines once with **GPS track** or **marked waypoints**—even coarse—**before** trusting irrigation or animal partitions.

---

*First draft: naming convention is the product; software is secondary.*
