---
title: Time synchronization — NTP and PTP sources
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-18
tags:
  - ntp
  - ptp
  - raspberry-pi
review_status: unreviewed
---

# Time synchronization — NTP and PTP sources

Reference and project material on **NTP** vs **PTP**, **IEEE 1588** profiles, hardware timestamping expectations, **GNSS-disciplined** lab/edge clocks, a **DIY Raspberry Pi grandmaster** (**Time Pi**) repo, **Raspberry Shake**-style NTP operational notes, and forum threads on **GNSS HATs** and stratum-1 builds.

This hub focuses on **distributing** and disciplining time over IP/Ethernet. For **where** time and positioning come from when **GNSS is contested or complemented** (e.g. broadcast timing, LORAN history, non-GPS trackers), see [`Position, navigation, and timing alternatives`](position-navigation-and-timing-alternatives.md)—linked below.

**Concepts**

- [`Network Time Protocol (NTP)`](../concepts/network-time-protocol.md)
- [`Precision Time Protocol (PTP)`](../concepts/precision-time-protocol.md)

**Source notes**

- [`source-notes/network-time-protocol-wikipedia.md`](../source-notes/network-time-protocol-wikipedia.md)
- [`source-notes/precision-time-protocol-wikipedia.md`](../source-notes/precision-time-protocol-wikipedia.md)
- [`source-notes/precision-time-protocol-explained-networklessons.md`](../source-notes/precision-time-protocol-explained-networklessons.md)
- [`source-notes/diy-ptp-grandmaster-pi-geerling.md`](../source-notes/diy-ptp-grandmaster-pi-geerling.md)
- [`source-notes/raspberry-pi-5-ptp-timestamping-forums.md`](../source-notes/raspberry-pi-5-ptp-timestamping-forums.md)
- [`source-notes/geerlingguy-time-pi-ansible-configuration.md`](../source-notes/geerlingguy-time-pi-ansible-configuration.md)
- [`source-notes/ntp-and-gps-timing-raspberry-shake.md`](../source-notes/ntp-and-gps-timing-raspberry-shake.md)
- [`source-notes/gps-controlled-clock-raspberry-pi-engineering-radio.md`](../source-notes/gps-controlled-clock-raspberry-pi-engineering-radio.md)
- [`source-notes/gnss-hat-setting-time-raspberry-pi-forums.md`](../source-notes/gnss-hat-setting-time-raspberry-pi-forums.md)
- [`source-notes/timeserver-with-gnss-receiver-raspberry-pi-forums.md`](../source-notes/timeserver-with-gnss-receiver-raspberry-pi-forums.md)
- [`source-notes/nist-internet-time-service-servers.md`](../source-notes/nist-internet-time-service-servers.md)

**Related topics**

- [`Position, navigation, and timing alternatives`](position-navigation-and-timing-alternatives.md) — BPS/LORAN/non-GPS tracker framing
- [`Timing on the farm — synthesis`](../analyses/timing-on-the-farm-synthesis.md) — How clock sync fits alongside seasonal and labor timing on-farm
