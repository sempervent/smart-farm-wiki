---
title: Site-to-site network role boundaries standard
page_type: analysis
page_subtype: standard
operational_maturity: pilot_ready
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - networking
  - two-site
  - security
  - standards
review_status: reviewed
confidence: high
---

# Site-to-site network role boundaries standard

## Purpose

**Norms** for **trust** **zones**, **SITE_HOME** vs **SITE_FARM** **roles**, and **what** **crosses** **the** **WAN** **vs** **stays** **local**—aligned with [`Network segmentation, site-to-site, and internet exposure — two-site smart farm`](network-segmentation-site-to-site-and-internet-exposure-two-site-smart-farm.md) (exposure table) and [`Execution topology package — two-site smart farm (Mermaid)`](execution-topology-package-two-site-smart-farm.md).

---

## Standard

| # | Rule |
|---|------|
| 1 | **Document** **Z1/Z2/Z3** (or **equivalent**) **per** **site**—**admin**, **telemetry**, **guest/user** **traffic** **do** **not** **share** **implicit** **trust**. |
| 2 | **SITE_HOME** **may** **host** **control** **plane** **/** **central** **backup** **landing**; **SITE_FARM** **edge** **assumes** **constrained** **power** **and** **WAN** ([`Central vs local backup scope`](central-vs-local-backup-scope-farm-edge-stack.md)). |
| 3 | **Field** **telemetry** **must** **operate** **local-first** **for** **welfare-critical** **signals** **per** **off-grid** **doctrine** **where** **applicable**—**WAN** **is** **not** **the** **sole** **proof** **path**. |
| 4 | **Site-to-site** **link** **(VPN** **/** **tailnet** **/** **SSH** **bastion** **)** **terminates** **in** **a** **known** **segment**—**no** **flat** **LAN** **across** **counties** **without** **documented** **exception**. |
| 5 | **Internet** **exposure** **table** **(cameras** **,** **broker** **,** **farmOS** **)** **stays** **current** **when** **services** **move**—see **segmentation** **analysis** **for** **fill-in** **template**. |

---

## Related

- [`Two-site operations model — 5-acre home base and 120-acre farm`](two-site-operations-model-5ac-homebase-120ac-production.md)
- [`Local site and county intelligence`](../topics/local-site-and-county-intelligence.md)
- [`Operational standards — farm and homelab platform`](../topics/operational-standards-farm-homelab-platform.md)
