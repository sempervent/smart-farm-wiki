---
title: Runbook — power loss at remote site
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
tags:
  - sop
  - runbook
  - power
review_status: unreviewed
confidence: low
---

# Runbook — power loss at remote site

**Prerequisites**: [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md); power assumptions in that doc (**solar/battery/grid**). Link [`Off-grid solar power and storage (special topic)`](../topics/off-grid-solar-power-and-storage.md) for **design** context.

## Purpose

When **`SITE_FARM`** (or a **field hub**) loses **mains** or **battery** hits **low-voltage cutoff**, **field telemetry and actuators** may fail **opposite** to “safe”—know **fail-open vs fail-closed** per install.

## Detection

- **Monitoring**: **UPS**, **battery SOC**, **last-seen** on gateway—if architecture documents them.
- **On-site**: **no** pump, **dark** barn, **silent** inverter.

## Immediate actions

1. **Safety**: **livestock** water—**manual** fill or **generator** per **pre-placed** SOP (placeholders: `GEN_START_STEPS_REF`).
2. **Do not trust remote commands** until **power** and **time sync** are healthy.
3. **Spoilage / cold chain**: if relevant—**inventory** decision tree (business).

## Recovery

- **Restore** loads in order: **gateway** before **non-critical** displays (define order).
- **Verify** **NTP** after long outage—[`Time synchronization — NTP and PTP sources`](../topics/time-synchronization-ntp-and-ptp.md).

## Related

- [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md) — overlapping symptoms.

---

*Label **breakers** and **generator** cords before you need them in the dark.*
