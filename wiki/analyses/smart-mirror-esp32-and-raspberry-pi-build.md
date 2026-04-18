---
title: Smart mirror with ESP32 and Raspberry Pi — build analysis
page_type: analysis
status: active
created: 2026-04-18
updated: 2026-04-18
review_status: unreviewed
tags:
  - magic-mirror
  - esp32
  - raspberry-pi
confidence: medium
---

# Smart mirror with ESP32 and Raspberry Pi — build analysis

**Question**: How do you **build a smart mirror** using both an **ESP32** and a **Raspberry Pi**, and where do parts typically come from?

**Epistemic note**: This page mixes **upstream MagicMirror² documentation**, **community build write-ups**, and **ESP32 display/integration practice** from the open web with **existing vault** source-notes. It is **not** a guaranteed shopping list—verify **electrical**, **mechanical**, and **RF** compatibility before ordering.

---

## 1. Reality check: what each chip is for

**MagicMirror²** (the common open-source smart-mirror application) is a **Node.js** stack wrapped in **Electron** and is **developed and tested on Raspberry Pi** with a full **desktop** Raspberry Pi OS—not on ESP32. Official requirements state Pi-class hardware, current Raspberry Pi OS with a desktop, and a supported **Node.js** line; **Pi Zero / 1** are not supported for the standard GUI path ([MagicMirror² requirements](https://docs.magicmirror.builders/getting-started/requirements.html), [installation](https://docs.magicmirror.builders/getting-started/installation.html)).

**ESP32** cannot practically **host MagicMirror²** itself (RAM, no standard Electron target, no full desktop browser stack). Community discussion aligns: for ultra-compact builds, a **Pi Zero 2 W** or similar is often suggested over expecting ESP32 to run the mirror UI ([MagicMirror forum — ESP32 display thread](https://forum.magicmirror.builders/topic/19115/dell-lcd-display-with-esp32)).

**Practical combined design**: Use the **Raspberry Pi** behind the **two-way mirror** as the **primary display computer** running MagicMirror² on **HDMI**. Use the **ESP32** for **peripheral intelligence** (sensors, secondary small display, LED accent, or MQTT touch panel)—**co-located** in the same project, not as a second MagicMirror host.

---

## 2. Recommended high-level architecture

| Role | Device | Function |
|------|--------|----------|
| **Main UI** | **Raspberry Pi 4/5** (2 GB+ RAM common; 4 GB comfortable) | Raspberry Pi **OS Desktop**, **MagicMirror²**, HDMI to monitor behind glass |
| **Peripheral / HMI** | **ESP32** (often **-S3** if using a modern touch LCD + **LVGL**) | PIR/motion, ambient light, **ESPHome** or custom firmware, **MQTT** to Home Assistant or directly to services on the Pi |
| **Optional second screen** | Same Pi via second HDMI, or a **second Pi**, or ESP32 + TFT | Multi-monitor MagicMirror setups are documented ([two-display write-up](https://florianmuller.com/build-a-smart-magicmirror-with-two-displays-running-on-raspberry-pi)); ESP32 + TFT is a **parallel dashboard**, not a second Electron instance |

Upstream project: [MagicMirror² on GitHub](https://github.com/MichMich/MagicMirror).

---

## 3. Raspberry Pi path (main mirror)

1. **SBC**: **Raspberry Pi 4B** or **Pi 5** with adequate RAM; official **USB-C power** (5 V, adequate amps per Pi 5 guidance on [raspberrypi.com](https://www.raspberrypi.com/)).
2. **Storage**: **microSD** (quality card) or **SSD** via USB on Pi 4/5 for longevity.
3. **Display**: **IPS monitor** sized to your mirror opening; strip bezel to fit **two-way mirror acrylic or glass** (transmission vs reflection tradeoff—sample small pieces before large orders).
4. **OS**: **Raspberry Pi OS (64-bit) Desktop** per MagicMirror docs (not “Lite” for standard install).
5. **Install**: Follow [MagicMirror² installation](https://docs.magicmirror.builders/getting-started/installation.html); use **PM2** or **systemd** for auto-start after boot (common in hobby guides such as [step-by-step Pi mirror builds](https://pidiylab.com/raspberry-pi-magic-mirror-guide/)).

**Vault grounding**: [`source-notes/how-to-build-smart-magic-mirror.md`](../source-notes/how-to-build-smart-magic-mirror.md), [`source-notes/magicmirror2-open-source-smart-mirror-platform.md`](../source-notes/magicmirror2-open-source-smart-mirror-platform.md).

---

## 4. ESP32 path (companion roles)

Pick **one** primary role to avoid scope creep:

- **Sensors only**: **ESP32** + PIR, **BH1750** / ADC light sensing, **I²C** gesture chip—publish **MQTT**; MagicMirror or **Home Assistant** on the Pi subscribes and drives modules or automations.
- **Small touch panel** (wall or frame-mounted): **ESP32-S3** dev board with integrated **SPI/I²C touch LCD**, **ESPHome** + **LVGL** patterns ([ESPHome + LVGL home dashboard example](https://vahac.com/building-a-touch-controlled-home-assistant-dashboard-on-an-esp32-s3-with-lvgl-esphome/))—shows **complementary** info (climate, quick toggles), while the mirror remains the “glanceable” primary UI.
- **LED accent / bias lighting**: **ESP32** drives **WS2812B** strips; sync color to time-of-day or MQTT events (Pi or HA sends topics).

Avoid expecting the ESP32’s browser to render full MagicMirror web UI; treat it as **IoT** and **HMI**, not a second Electron machine.

---

## 5. Parts and where to source them (indicative)

Use this as a **checklist category** list; **SKUs change**—search the vendor site for current stock.

| Category | Examples | Typical sources (not exclusive) |
|----------|----------|----------------------------------|
| **Raspberry Pi + PSU** | Pi 4B/5, official USB-C supply | [Raspberry Pi approved resellers](https://www.raspberrypi.com/resellers/), [Adafruit](https://www.adafruit.com/), [Pimoroni](https://shop.pimoroni.com/), [DigiKey](https://www.digikey.com/), [Mouser](https://www.mouser.com/) |
| **microSD / SSD** | Name-brand SD A2/U3; USB SSD enclosure | Same as above; avoid no-name cards for 24/7 mirror |
| **Monitor** | Thin IPS HDMI panel, 24" common in DIY guides | Retail electronics; some builders use **used** office monitors ([multi-display mirror project](https://florianmuller.com/build-a-smart-magicmirror-with-two-displays-running-on-raspberry-pi)) |
| **Two-way mirror** | Acrylic or glass **dielectric** two-way | Local glass shops; online “two way mirror” suppliers; **sample first** for tint and transmission |
| **Frame / enclosure** | Wood or aluminum extrusion, VESA | Hardware stores; 8020-style extrusion vendors |
| **ESP32 module** | ESP32-S3 N16R8 class dev boards, or integrated **touch LCD** boards (Waveshare / Elecrow / “CrowPanel” class devices) | [Waveshare](https://www.waveshare.com/), [Adafruit](https://www.adafruit.com/), [SparkFun](https://www.sparkfun.com/), AliExpress (longer lead times) |
| **Sensors** | PIR, BH1750, I²C gesture | Adafruit, SparkFun, DigiKey |
| **Cabling** | Short HDMI, USB-C, 5 V for LED strips | Same distributors |

**Electrical**: Mirror installs are **continuous power**; use **fused** LED supplies and **gauge-appropriate** wire for **5 V** strips; follow your jurisdiction’s electrical rules for **permanent** mains wiring.

---

## 6. Software glue

- **Home Assistant** on the Pi or another host: **ESPHome** integration for ESP32; MagicMirror **MMM-HomeAssistant**-style modules exist in the community ecosystem (search [MagicMirror third-party modules](https://github.com/MichMich/MagicMirror/wiki/3rd-party-modules)).
- **MQTT**: **Mosquitto** on Pi is a common broker for ESP32 → automation → mirror-adjacent logic.
- **Time sync**: If the mirror shows wall-clock modules, ensure **NTP** is healthy on the Pi ([`Time synchronization — NTP and PTP sources`](../topics/time-synchronization-ntp-and-ptp.md)).

---

## 7. Related wiki pages

- [`Smart mirror and e-paper display builds`](../topics/smart-mirror-and-e-paper-displays.md)
- [`ESP32`](../concepts/esp32.md)
- [`ESP32, ESPHome, and smart-farming builds`](../topics/esp32-iot-smart-farming-and-tooling.md)

---

## 8. External references (web)

- [MagicMirror² — GitHub](https://github.com/MichMich/MagicMirror)
- [MagicMirror² — Documentation](https://docs.magicmirror.builders/)
- [Requirements (Pi, OS, Node)](https://docs.magicmirror.builders/getting-started/requirements.html)
- [Installation](https://docs.magicmirror.builders/getting-started/installation.html)
- [Raspberry Pi OS / configuration notes](https://docs.magicmirror.builders/configuration/raspberry.html)
- [Two-display MagicMirror build (Florian Müller)](https://florianmuller.com/build-a-smart-magicmirror-with-two-displays-running-on-raspberry-pi)
- [Pi Magic Mirror guide (Pidiylab)](https://pidiylab.com/raspberry-pi-magic-mirror-guide/)
- [MagicMirror forum — ESP32 display discussion](https://forum.magicmirror.builders/topic/19115/dell-lcd-display-with-esp32)
- [ESPHome + LVGL on ESP32-S3 (example project write-up)](https://vahac.com/building-a-touch-controlled-home-assistant-dashboard-on-an-esp32-s3-with-lvgl-esphome/)

---

*Prefer **one** clear architecture (Pi = mirror, ESP32 = sensors or side panel) before ordering; revise this page when new ingested raw sources land.*
