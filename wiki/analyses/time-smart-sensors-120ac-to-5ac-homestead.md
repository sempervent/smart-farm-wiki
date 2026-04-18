---
title: Time and smart sensors — 120-acre field to 5-acre homestead
page_type: analysis
status: active
created: 2026-04-17
updated: 2026-04-17
review_status: unreviewed
tags:
  - time
  - sensors
  - two-site
  - telemetry
confidence: medium
---

# Time and smart sensors — 120-acre field to 5-acre homestead

**Scope**: How **time** shows up when **smart sensors** span a **remote production site** (~120 acres) and a **local homestead hub** (~5 acres), in the vault’s two-site framing. This is a **synthesis** of existing analyses—not new site measurements or invented latencies.

“Time” here is **not** one problem; it is several layers that interact.

---

## 1. Human and operational time (often the binding constraint)

The **5-acre homestead** is where planning, dashboards, and often the **stable internet path** live; the **120-acre** site is where **physical reality** and **field hardware** live. Between them, **`COMMUTE_ONE_WAY`** (planning default ~35 minutes in the operations model) is not a network metric—it is **batching and emergency math**: how often you can afford to drive, how you stack chores, and what “fast enough” means when something fails in the field. See [`Two-site operating model — 5-acre home base and 120-acre farm`](two-site-operations-model-5ac-homebase-120ac-production.md).

**Implication for sensors**: Telemetry can **shorten information delay** (you see a dry tank sooner than the next visit), but it cannot create **new hours** or shrink **drive time**. If the control loop you care about is “owner on scene,” the relevant timescale is still **commute + on-site work**, not MQTT latency alone.

---

## 2. End-to-end latency (remote sensing → homestead awareness)

For **smart sensors at the 120**, “time” includes the full chain:

**Field device → radio (LoRa / LTE / Wi‑Fi / mesh) → edge gateway → backhaul → broker / DB → UI or alert at the 5-acre hub.**

Each hop adds **delay and jitter**. Backhaul is a **variable** (cell, fiber, PtP, mesh), and the **homestead** may see data only as fast as the **slowest** segment. See [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md) and tradeoff tables in that doc.

**Implication**: “Real time” on the dashboard is **bounded** by that chain. For **welfare-critical** signals (water, power at pump), the design question is whether **end-to-end time + your reaction time** is less than **time-to-harm**, not whether one link is fast.

---

## 3. Clock time — correlation and trust (not just speed)

A separate layer is **synchronized clocks**: NTP / PTP / GNSS at edges so that tank level, pump run, soil moisture, and weather **share a coherent timeline** when you debug or correlate events. See [`Timing on the farm — synthesis`](timing-on-the-farm-synthesis.md), [`Time synchronization — NTP and PTP sources`](../topics/time-synchronization-ntp-and-ptp.md), and strand **G** (time / correlated logs) in the field telemetry architecture page.

**Implication**: **Homestead** consoles can show charts, but if **field** nodes drift or logs are merged without UTC discipline, “smart” becomes misleading. The field telemetry page lists **time sync** among broker/gateway-class failure concerns.

---

## 4. Stale time and authority (when “now” is not the field)

At the **5-acre** side, **dashboards are not truth**—they are **views** with a **freshness** problem. If **120-acre backhaul** drops, the **homestead** UI can show **last known** state while the real field is already in a different state. Treat **stale** data as a first-class failure mode; see [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md) and [`Reference architecture — 5-acre home base + 120-acre farm`](reference-architecture-5ac-homebase-120ac-smart-farm.md).

**Implication**: “Time” here is **age of last good sample** and **policy** (when to assume worst-case and send a body to the field), not refresh rate alone.

---

## 5. Control-loop vs sampling time

**Fast sampling** (e.g. soil moisture every few minutes) is only useful if **actuation** or **human response** can keep up. **Slow hazards** (tank draining over hours) match **lower** telemetry rates; **fast hazards** need **redundant** sensing, **local** alarms, or **someone** within **response time**. Instrumentation pages frame **trip ROI** and **triage burden**—i.e. **operator time** on alerts—alongside capital: [`Instrumentation priority matrix — two-site smart farm`](instrumentation-priority-matrix-two-site-smart-farm.md), [`Instrumentation ROI model — two-site smart farm`](instrumentation-roi-model-two-site-smart-farm.md).

**Implication**: The right question is often **minutes-to-intervene** from **first trustworthy alert**, including **commute**, not **milliseconds** from sensor to MQTT.

---

## 6. Summary table

| Time concept | Main locus | Role for 120 → 5 ac sensors |
|--------------|------------|------------------------------|
| **Commute / batch** | Human | Caps how often “remote” can become “on site” |
| **E2E telemetry delay** | Network stack | Bounds how fresh “remote awareness” is |
| **UTC / NTP discipline** | Field + hub | Makes multi-sensor and multi-site logs comparable |
| **Staleness / outage** | Hub UI vs field | Defines when automation and dashboards must defer to manual rules |
| **Alert / triage time** | Family OPEX | Automation can **increase** wall-clock load if false positives dominate |

---

## Related entry points

- [`Timing on the farm — synthesis`](timing-on-the-farm-synthesis.md) — broader layers of “timing” on the farm.
- [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md) — topic hub for 5 ac + 120 ac operations and telemetry.
