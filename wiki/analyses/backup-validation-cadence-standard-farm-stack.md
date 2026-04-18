---
title: Backup validation cadence — farm stack standard
page_type: analysis
page_subtype: standard
operational_maturity: pilot_ready
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - backup
  - standards
  - runbook
review_status: reviewed
confidence: high
---

# Backup validation cadence — farm stack standard

## Purpose

**How often** to **prove** backups via **restore** **drills**—complements [`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md) (the **how**) and [`Restore and recovery tiers`](restore-recovery-tiers-homelab-farm-systems.md) (the **targets**).

---

## Standard (minimum cadence)

| Maturity | restic / repo check | Logical DB restore (staging) | Longhorn subset restore | etcd / k3s snapshot drill |
|----------|----------------------|-------------------------------|-------------------------|----------------------------|
| **Pilot** | **Monthly** `restic check` (or equivalent) | **Before** calling farm data **production** | **Once** before relying on PVC backup | **Document** path; **lab** only |
| **Production** | **Monthly** + after **major** **upgrade** | **Quarterly** full **Drill B** | **Semi-annual** | **Annual** or when **topology** **changes** |

**Rule**: **RPO/RTO** cells in the tier worksheet stay **blank** or **“aspirational”** until a **dated** drill completes ([`Runbook`](runbook-backup-validation-and-recovery-drill.md) **Reporting**).

**Execution tie**: **Major** **capital** **gates** (**G\***) should **not** assume **HA** **or** **cloud** **egress** **without** **matching** **backup** **evidence** ([`Business plan execution and pilot operations hub`](../topics/business-plan-execution-and-pilot-operations-hub.md)).

---

## Related

- [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)
