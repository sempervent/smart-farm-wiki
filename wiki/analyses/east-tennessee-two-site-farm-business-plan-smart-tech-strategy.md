---
title: East Tennessee two-site farm business plan — smart technology, telemetry, and automation
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - business-plan
  - automation
  - telemetry
---

# Smart technology, telemetry, and automation strategy

**Hub**: [`Planning framework`](east-tennessee-two-site-farm-business-plan-framework.md)  
**Architecture**: [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md)  
**Registry**: [`Farm spatial model and asset registry standard`](farm-spatial-model-and-asset-registry-standard.md)

## Principles

1. **Telemetry reduces trips**—otherwise it is **cost**, not **ROI**.
2. **Manual process before automation**: **name assets**, **define** “good” / “bad”, **run** a season **without** optimizing alerts.
3. **Degraded modes** are **first-class**: **broker down**, **power down**, **false positive storm** ([`runbooks`](runbook-broker-or-backhaul-down.md)).
4. **One system of record** for **events** (e.g. farmOS-class + backups)—MQTT is **transport**, not **truth** unless **explicitly** chosen.

## What to automate early (Phase 0–1)

| Item | Why | Caveat |
|------|-----|--------|
| **Maps + parcel/paddock IDs** | **Every** sensor **binds** to **land** | No map → **orphan** data |
| **One** water or **pump** monitor | **Highest** trip-avoidance **per dollar** | **Calibration**; **freeze** protection |
| **Power awareness** at **remote** pump/gateway | Explains **silent** failures | **Not** a substitute for **genset** plan |
| **Backup + VPN** pattern at **homestead** | **Brain** survives **disk** | **Test** restore |

## What not to automate early

| Item | Why wait |
|------|----------|
| **Camera mesh** everywhere | **Bandwidth**, **storage**, **privacy**, **triage** load |
| **GPS collars** (herd-wide) | **OPEX**, **vendor** lock, **not** always **margin**-positive at **small** herd |
| **Full** **irrigation** automation | **High** **skill** + **crop** commitment—**off** **recommended** **path** **until** Phase 3+ **if** added |
| **“AI”** on **edge** | **After** **logging** and **SOPs** exist |

## What must be manually proven first

| Proof | Before automating… |
|-------|-------------------|
| **Water system** fills/drains as **expected** (manual **stick**, **timer**) | **Remote** **level** **setpoints** |
| **Gate** **default safe state** (open/closed policy) | **Remote** actuation |
| **Animal** **check** **rhythm** **works** **weekly** | **Alert** **escalation** rules |
| **Sale** **channel** **works** **once** (auction or direct) | **Scaling** **herd** |

## Stack posture (by phase)

| Phase | Stack |
|-------|--------|
| **0** | **Spreadsheets + photos**; **no** **cloud** **dependency** for **compliance** |
| **1** | **Pilot**: **MQTT** → **broker** at **homestead**; **1–2** **field** **nodes**; **document** **topics** |
| **2** | **farmOS** or **chosen** **SoR**; **duplicate** **MQTT** **consumers** **only** **with** **reason** |
| **3** | **Observability**: **uptime**, **alert** **budget**, **spares** **list** |
| **4** | **Hardening**: **segmentation**, **patch** **cadence**, **key** **rotation** |

## Failure and degraded-mode realities

| Mode | Expectation |
|------|-------------|
| **Backhaul down** | **Field** **edge** **queues** **or** **fails** **safe**; **human** **route** **check** |
| **Power loss at 120** | **Tanks** **drain**; **pumps** **don’t** **self-fix**—[`runbook`](runbook-power-loss-remote-site.md) |
| **Alert flood** | **Corroborate** **before** **mute**—[`triage runbook`](runbook-sensor-false-positive-alert-triage.md) |
| **Cyber** | **Remote access** = **attack** **surface**—CISA-style **inventory** **mindset** |

## Financing / CAPEX caution (automation)

| Caution | Mitigation |
|---------|------------|
| **Vendor** **subscriptions** **creep** | **Annual** **OPEX** **cap** **in** **budget** |
| **Financed** **gadgets** **on** **card** | **Match** **to** **phase** **gate** **only** |
| **Duplicate** **hubs** | **Homestead** **primary**; **120** **minimal** **autonomy** |

---

## Known facts

| ID | Fact |
|----|------|
| K1 | **Homestead** intended as **long-run** **control** **center** |
| K2 | Vault **already** **contains** **reference** **architecture** + **runbooks** |

## Assumptions

| ID | Assumption |
|----|------------|
| A1 | **Family** can **maintain** **one** **Linux**/Docker **stack** **or** **pay** **support** |
| A2 | **LTE** or **starlink-class** **fallback** **available** **if** **primary** **ISP** **fails** **at** **home** |

## Open questions

| ID | Question |
|----|----------|
| Q1 | **farmOS** **vs** **lighter** **stack**? ([`comparison`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md)) |
| Q2 | **LoRaWAN** **vs** **Meshtastic** **for** **fixed** **telemetry**? ([`comparison`](../comparisons/lorawan-vs-meshtastic-fixed-farm-telemetry.md)) |
| Q3 | **Who** **on-call** **for** **alerts** **after** **10pm**? |

## Links

- [`Labor model`](east-tennessee-two-site-farm-business-plan-labor-and-family-model.md)
- [`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md)
