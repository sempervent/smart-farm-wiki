---
title: Automation degraded modes and manual fallback SOP
page_type: analysis
status: draft
created: 2026-04-21
updated: 2026-04-24
tags:
  - sop
  - automation
  - safety
  - mqtt
review_status: unreviewed
confidence: low
---

# Automation degraded modes and manual fallback SOP

## Purpose

**First-draft standard operating procedure** for when **automation is wrong, offline, or untrusted**—irrigation, pumps, gates, feeders, alerts tied to **`BROKER_LABEL`**, Home Assistant, or cloud rules. Goal: **animals, people, and structures** stay safe **without** assuming MQTT, internet, or logic is correct.

## Scope

- **In scope**: **Recognize failure class** → **safe state** → **manual steps** → **when to restore automation**.
- **Out of scope**: Specific **electrical lockout/tagout** (get training); **vendor** runbooks—cite in appendix when you add them.

## Assumptions

| Assumption | Implication |
|------------|-------------|
| **Fail-safe** is not automatic—your install may **fail open** or **closed**; **you must know which** per system. |
| Someone can reach **`SITE_FARM`** within **`MANUAL_INTERVENTION_TIME`** when Tier 1 risk exists—if not, **downscope automation** until coverage improves (see [`Weekly coverage matrix — two-site farm operations`](weekly-coverage-matrix-two-site-farm-operations.md)). |
| **Placeholders** `SYSTEM_IRRIGATION`, `SYSTEM_PUMP`, `SYSTEM_GATE`, `SYSTEM_FEEDER` stand in for **your** actual systems—duplicate section per system when you customize. |

## Failure classes (use as checklist)

| Class | Signs | Immediate mindset |
|-------|-------|-------------------|
| **A — Internet / broker down** | No MQTT messages; HA **unknown** state | **Do not** assume last command ran; **verify physical** |
| **A2 — LEO satellite WAN impaired** (e.g. **Starlink** fade) | **Same** **symptoms** **as** **A** **if** **uplink** **is** **satellite**; **may** **recover** **without** **your** **action** | **Do not** **chase** **MQTT** **during** **storm**—**execute** **manual** **rounds** **per** [`Manual fallback`](manual-fallback-degraded-modes-critical-operations.md) |
| **B — Sensor lying** | Tank reads empty but is full, or vice versa | **Disable auto** that acts on that sensor until recalibrated |
| **C — Actuator stuck / partial** | Valve half, gate motor humming, pump cavitating | **Manual disconnect** per equipment **label**—**if not labeled, stop and label** |
| **D — Logic bug / bad rule** | Water runs at wrong time; gate opens on schedule error | **Disable rule** at controller; not just “fix tomorrow” |
| **E — Power loss** | Field battery dead; **generator** not started | Follow **cold start** steps for **`SITE_FARM`** (document in asset registry) |

## Decision criteria: when to disable automation

| Condition | Action |
|-----------|--------|
| **Animal welfare** could depend on a **single** sensor | **Manual schedule** or **redundant** sensor—until then, **no closed-loop** |
| **Runoff / erosion** if water runs uncontrolled | **Shut source** first (well breaker, valve **upstream**) |
| **Cannot see** actual water level | **Do not** trust **remote** “off” command—**verify** |

## Manual fallback — template sections (customize per `SYSTEM_*`)

### `SYSTEM_IRRIGATION` (placeholder)

1. **Locate** manual valves: `VALVE_MAP_REF` (photo or registry ID).
2. **Desired safe state** when unsure: **`IRRIGATION_SAFE_STATE`** = typically **closed** upstream—**confirm** with your plumbing.
3. **Verify** wetness at **outlet** or **field** before leaving.
4. **Restore automation** only after: sensor **recalibrated** or **replaced**, rule **reviewed**, **dry run** in daylight.

### `SYSTEM_PUMP` (placeholder)

1. **Electrical**: note **`PUMP_BREAKER_ID`**; **lockout** if service—trained persons only.
2. **Prime / pressure**: follow **`PUMP_MANUAL_REF`** (manual PDF or plate).
3. **If run dry risk**: **disable auto start** until **float / pressure** sensor fixed.

### `SYSTEM_GATE` (placeholder)

1. **If motorized**: **disconnect motor** per manufacturer; **chain/latch** in **`GATE_SAFE_POSITION`** (closed/open per animal risk).
2. **Never** rely on **MQTT** for **escape prevention**—physical **latch** wins.

### `SYSTEM_FEEDER` (placeholder)

1. **Jam / runaway**: **power off** at **`FEEDER_BREAKER_ID`**.
2. **Overfeed risk**: measure **manual ration** until **scale** verified.

## Telemetry and alerts during degraded mode

- **Mute noisy alerts** only **after** physical safe state—silencing **without** verification repeats audit **false positive** failure.
- **Log** incidents in **`DEGRADED_MODE_LOG_REF`** (notebook, ticket, or wiki log entry)—**pattern** detection matters.

## Specialized runbooks (same degraded-mode family)

- [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md)
- [`Runbook — power loss at remote site`](runbook-power-loss-remote-site.md)
- [`Runbook — sensor false positive and alert triage`](runbook-sensor-false-positive-alert-triage.md)
- [`Runbook — manual fallback for irrigation, gates, and pumps`](runbook-manual-fallback-irrigation-gates-pumps.md)

## Links to related future or existing pages

- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md) — where **broker** and **gateways** sit.
- [`Data storage (farm and edge stacks)`](../concepts/data-storage.md) — **truth** in DB vs broker.
- [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md) — protocol context.
- [`Weekly coverage matrix — two-site farm operations`](weekly-coverage-matrix-two-site-farm-operations.md) — **who** can execute manual steps.
- [`Dual-site operations model — non-agritourism farm business`](dual-site-operations-model-non-agritourism.md) — **time tax** to reach `SITE_FARM`.
- *Observability and alerts — broker down, false positives, on-call* — see **[P2 #19](implementation-backlog-strategic-audit.md)** when a standalone page exists.

## Open items

- [ ] Per **`SYSTEM_*`**: breaker IDs, valve photos, **manufacturer** emergency section bookmarked.
- [ ] **Dry run** this SOP once **on purpose** in safe conditions (tabletop + short field exercise).
- [ ] Post **one-page** “kill order” in **`FIELD_SHED_LOCATION`** and **`HOME_OFFICE_LOCATION`**.

---

*First draft: replace every placeholder with real IDs; have a qualified person review electrical and water steps.*
