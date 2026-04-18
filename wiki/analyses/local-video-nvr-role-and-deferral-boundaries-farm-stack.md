---
title: Local video / NVR — role and deferral boundaries (farm stack)
page_type: analysis
status: active
created: 2026-04-25
updated: 2026-04-25
tags:
  - video
  - nvr
  - frigate
  - observability
  - two-site
review_status: unreviewed
confidence: high
---

# Local video / NVR — role and deferral boundaries (farm stack)

## Purpose

**Explicit** stance on **IP camera** + **NVR** software (e.g. **Frigate**) in the **two-site smart farm** architecture: **what** it is **good for**, **what** it must **not** replace, and **why** full deployment is **deferred** until **Phase 1** **field** and **power** **baselines** exist.

**Source grounding**: Frigate **intro + configuration** captures in [`Inbox batch — Frigate, SOPS, Prometheus, TN811, NRCS/UT (2026-04-18)`](../source-notes/inbox-batch-2026-04-18-frigate-sops-prometheus-alertmanager-tenn811-nrcs-ut-extension.md); upstream [docs.frigate.video](https://docs.frigate.video/).

---

## What video is good for (when justified)

| Use | Notes |
|-----|--------|
| **Perimeter / gate** **awareness** | Reduces **nuisance** trips for **ambiguous** events—**not** a substitute for **physical** **locks** and **livestock** **checks**. |
| **Workshop / equipment** **yards** | **Theft** and **misuse** **deterrence** **supporting** evidence—**policy** and **insurance** still **primary**. |
| **Calving / handling** **areas** (where installed) | **Observation** aid—**does not** replace **hands-on** **welfare** **protocols**. |

Frigate’s design (**motion → detect**, **MQTT**, **Home Assistant** integration) fits **homelab** **integration** patterns described in the capture—**if** **LAN** and **storage** **budget** exist.

---

## What video must not be used for (operationally)

| Anti-pattern | Why |
|--------------|-----|
| **Sole** proof of **animal welfare** | Cameras **miss** **blind** **spots**, **night** **conditions**, and **non-visual** **distress**. |
| **Replacement** for **water** / **weather** **telemetry** | **Sensors** and **manual** **rounds** remain **authoritative** for **drought** and **freeze** risk ([`Farm sensor architecture — Demory farm site`](farm-sensor-architecture-demory-farm-site.md)). |
| **WAN-dependent** **“peace of mind”** | Violates **local survivability** doctrine when **Starlink** / **LTE** **fade**—align with [`Automation stop rules — two-site smart farm`](automation-stop-rules-two-site-smart-farm.md) **CS-***. |

---

## Power, storage, and network implications

- **Continuous** **encode** + **retention** **consume** **disk** and **CPU**/**GPU** **budget**—compete with **k3s**, **DB**, and **backup** **windows** ([`Platform decision memo`](platform-decision-memo-phase-homelab-k3s-pi-fleet-2026-04-18.md)).
- **Remote** **viewing** **increases** **egress** and **attack** **surface**—route through [`Network segmentation, site-to-site connectivity, and internet exposure`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md) and [`Remote access and operational security model — two-site smart farm`](remote-access-operational-security-model-two-site-smart-farm.md).

---

## Deferral decision (canonical)

**Phase 0–1 default**: **Defer** **Frigate** (or any **NVR**) **production** **scope** until:

1. [`Secrets and certificates — edge cluster standard`](secrets-and-certificates-edge-cluster-standard.md) and [`Monitoring and logging expectations — edge cluster standard`](monitoring-and-logging-expectations-edge-cluster-standard.md) are **met** for the **edge** **cluster** (or consciously **scoped-down** **non-k8s** **stack** with **equivalent** **controls**).
2. **Demory** **power** and **network** **degraded** **modes** are **documented** per [`Off-grid systems doctrine package — Demory`](../topics/off-grid-systems-doctrine-package-demory-farm-site.md)—**video** must not **expand** **fragility** **before** **water** / **fence** **MVP**.

**Pilot exception**: **Single** **camera** + **short** **retention** on **`SITE_HOME`** **only** for **learning** **MQTT** / **storage** **load**—**not** **farm** **production** **dependence**.

---

## Related

- [`Observability, secrets, and trust bar — homelab / farm edge`](observability-secrets-and-trust-bar-homelab-farm-edge.md)
- [`Reference architecture — 5-acre home base + 120-acre farm`](reference-architecture-5ac-homebase-120ac-smart-farm.md) (video called out in **layered** view **notes**)
