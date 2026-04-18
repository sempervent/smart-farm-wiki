---
title: Precision Time Protocol (PTP)
page_type: concept
status: active
created: 2026-04-17
updated: 2026-04-17
tags:
  - ptp
  - ieee-1588
  - time-sync
related_concepts:
  - concepts/network-time-protocol.md
review_status: unreviewed
confidence: medium
---

# Precision Time Protocol (PTP)

**PTP** (**IEEE 1588**) synchronizes clocks across Ethernet/IP networks to sub-microsecond/nanosecond regimes in well-instrumented deployments, often relying on **hardware timestamping** in NICs for best results—useful in power, industrial, A/V, and scientific timing, and adjacent to lab/edge **grandmaster** builds.

**Grounded sources**

- [`source-notes/precision-time-protocol-wikipedia.md`](../source-notes/precision-time-protocol-wikipedia.md)
- [`source-notes/precision-time-protocol-explained-networklessons.md`](../source-notes/precision-time-protocol-explained-networklessons.md)

**Related**

- [`Network Time Protocol (NTP)`](network-time-protocol.md)
- [`Time synchronization — NTP and PTP sources`](../topics/time-synchronization-ntp-and-ptp.md)
