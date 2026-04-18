---
title: Disaster recovery decision rules — farm edge stack
page_type: analysis
page_subtype: operational_guide
operational_maturity: pilot_ready
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - backup
  - disaster-recovery
  - decision-rules
  - farmos
  - k3s
review_status: reviewed
confidence: high
---

# Disaster recovery decision rules — farm edge stack

## Purpose

**When to restore what**, in **what order**, and **when to stop** and treat the event as a **rebuild** or **scope cut**—for **farmOS**, **PostgreSQL**, **k3s**, **Longhorn**, **Rancher**, **secrets/config**, and **edge** services. Complements tier labels ([`Restore and recovery tiers`](restore-recovery-tiers-homelab-farm-systems.md)) and the **runbook** ([`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md)) with **decision** logic, not step-by-step commands.

**Canonical package**: [`Backup and disaster recovery package — smart farm stack`](backup-and-disaster-recovery-package-smart-farm-stack.md).

**Platform context**: [`Platform doctrine package — homelab / farm edge`](../topics/platform-doctrine-package-homelab-farm-edge.md). **Execution / gates** (when DR proof matters for spend): [`Business plan execution and pilot operations hub`](../topics/business-plan-execution-and-pilot-operations-hub.md), [`Validation backlog and decision gates`](east-tennessee-two-site-farm-business-plan-validation-backlog.md).

---

## Non-negotiables (recap)

| Distinction | Rule |
|-------------|------|
| **Backup vs sync** | Sync/mirror jobs are **not** backup unless they produce **versioned**, **restore-tested** recovery points—see [`Backup strategy comparison`](backup-strategy-comparison-farmos-homelab-postgresql-containers.md). |
| **App-aware vs raw volume** | **farmOS / PostgreSQL**: keep a **logical** restore path (**Tier 2**); volume-only restore without a proven quiesce story is **high risk**—see main package. |
| **Restore-tested** | Targets in the RPO/RTO worksheet are **aspirational** until [`Runbook — backup validation and recovery drill`](runbook-backup-validation-and-recovery-drill.md) drills pass. |

---

## Classify the failure (pick a lane)

| Failure class | Typical signal | First recovery question |
|---------------|----------------|-------------------------|
| **F1 — App / DB only** | farmOS broken; cluster healthy; DB corrupt or bad migration | Can you restore **Tier 2** logical dump to **staging** first? |
| **F2 — PVC / volume** | Single workload data loss; etcd OK | Longhorn restore **Tier 1** for that volume—then **verify** app consistency (may still need **A** if DB was dirty). |
| **F3 — Control plane** | k3s API dead; nodes may be OK | **etcd** snapshot / k3s restore (**Tier 3** track)—**do not** assume app data returns without **A**. |
| **F4 — Site / rack loss** | Fire, theft, extended outage at **`SITE_HOME`** | **Off-site** copies per [`Central vs local backup scope`](central-vs-local-backup-scope-farm-edge-stack.md); **rebuild** cluster from docs + **Tier 2** before declaring success. |
| **F5 — Edge gateway** | Field MQTT/gateway lost; cluster OK | **Config** restore from Git/export (**Drill F**); **buffer** data may be gone—confirm against **SoR** ([`Telemetry system of record`](telemetry-system-of-record-boundaries-and-authority.md)). |

---

## Restore order (default)

1. **Stabilize** power and network enough to run restores safely (off-grid: see [`Off-grid implications — backup and networking choices`](off-grid-implications-backup-and-networking-choices.md)).
2. **Tier 2** (logical DB) for **farm records** when **F1** or when any doubt about DB consistency—**before** declaring a volume restore “done.”
3. **Tier 1** (volume) when **F2** and DB is known consistent or disposable (non-production test).
4. **Tier 3** (etcd / platform) when **F3**—expect **namespace/workload** recreation; **re-attach** PVC restores and **re-import** logical DB if needed.
5. **Rancher** only after **C** track is coherent—version-match per Rancher docs ([`Kubernetes platform backup / DR`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md) track **D**).

**Anti-pattern**: Restoring **Tier 3** alone and assuming **farmOS** data “came back” without a **Tier 2** check—produces **empty healthy clusters** (see tier page **Rule**).

---

## When to rebuild instead of deep restore

- **Lab / pilot** cluster with **no** production farm data: rebuild from [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) may be **faster** than etcd archaeology—**if** **Tier 2** exports exist and you accept **downtime**.
- **Secrets** lost with no break-glass copy: **rotate** and **redeploy**—restore from snapshot may **re-import** compromised material; follow your security policy.

---

## Business execution alignment (East Tennessee package)

| Idea | Where it lives |
|------|----------------|
| **Cheap proofs before major spend** | Validation backlog / **G\*** gates—**restore drills** are evidence that **backup jobs are real**, not theater. |
| **Phase 0–1** | Prefer **Track A** (logical dumps) **working** before **HA** or **Longhorn system** complexity—[`Raspberry Pi k3s fleet — backup and restore sequence`](raspberry-pi-k3s-fleet-backup-and-restore-sequence.md). |
| **Two-site ops** | **Central** backup bias toward **`SITE_HOME`** when WAN allows—[`Central vs local backup scope`](central-vs-local-backup-scope-farm-edge-stack.md). |

---

## Related

- [`Kubernetes platform backup / DR — Pi fleet, k3s, Longhorn`](kubernetes-platform-backup-dr-pi-k3s-longhorn.md) — parallel tracks **A–E**
- [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md) — ops while **restore in progress**
- [`Automation degraded modes SOP`](automation-degraded-modes-manual-fallback-sop.md)
- [`Backup and restore tier labels — farm stack`](../entities/backup-restore-tier-labels-farm-stack.md)
