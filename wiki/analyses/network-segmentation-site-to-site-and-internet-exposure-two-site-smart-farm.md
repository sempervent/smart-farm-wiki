---
title: Network segmentation, site-to-site connectivity, and internet exposure — two-site smart farm
page_type: analysis
status: active
created: 2026-04-24
updated: 2026-04-24
review_status: unreviewed
tags:
  - security
  - networking
  - segmentation
  - two-site
  - vpn
confidence: medium
aliases:
  - Segmentation and exposure policy two-site
---

# Network segmentation, site-to-site connectivity, and internet exposure — two-site smart farm

## Purpose

Define **architecture-level** **policy** for **how traffic classes are separated**, **how** **`SITE_HOME`** **and** **`SITE_FARM`** **reunify** **without** **flat L2**, and **what** **may** **face** **the** **Internet** **vs** **what** **must** **never** **be** **directly** **exposed**—**vendor-neutral** (Starlink, LTE, fiber are **transport** **choices**, not **trust** **anchors**).

**Paired canonical pages**: [`Remote access and operational security model`](remote-access-operational-security-model-two-site-smart-farm.md) (**admin** **paths**, **identity**, **patching**); [`Connectivity strategy — Claxton & Demory`](connectivity-strategy-for-claxton-and-demory.md) (**WAN** **roles** **per** **named** **site**).

**Non-goals**: Product **hardening** **guides**; **per-device** **CVE** **tracking** **here**.

---

## Site-to-site connectivity — assumptions (policy)

| Assumption | Rationale |
|------------|-----------|
| **No** **Ethernet** **“** **one** **LAN** **”** **across** **`COMMUTE_ONE_WAY`** | **Distance** **tax** **and** **theft** **risk** **favor** **logical** **reunion** **(VPN** **/** **overlay** **/** **cloud** **rendezvous** **)** **over** **stretched** **L2**. |
| **Encrypted** **overlay** **for** **admin** **and** **telemetry** **egress** **as** **designed** | **WAN** **(including** **LEO** **satellite** **)** **is** **Z3** **—** **same** **hostile** **model** **as** **any** **ISP** **path**. |
| **Outbound-first** **where** **possible** **for** **field** **initiated** **tunnels** | **CGNAT** **and** **dynamic** **IPs** **are** **normal** **on** **Starlink** **/** **LTE** **—** **do** **not** **depend** **on** **stable** **inbound** **to** **`SITE_FARM`**. |
| **Documented** **split** **DNS** **or** **name** **targets** **per** **zone** **(optional** **)** | **Reduces** **accidental** **hairpin** **and** **leakage** **of** **internal** **names** **to** **public** **resolvers**. |

**Diagrams**: [`Execution topology package — two-site smart farm (Mermaid)`](execution-topology-package-two-site-smart-farm.md) (Z1/Z2/Z3, WAN-dependent vs local survivable).

---

## Segmentation — device and service classes

**Goal**: **Limit** **east-west** **movement** **if** **one** **class** **is** **compromised** **(stolen** **gateway,** **camera** **botnet,** **phished** **laptop** **)**.

| Class | Typical location | Segment posture (policy) | Notes |
|-------|------------------|----------------------------|--------|
| **User** **/** **family** **devices** **(phones,** **laptops** **)** | **Z1** **primarily** **;** **sometimes** **Z2** **visitor** | **Standard** **LAN** **or** **trusted** **Wi‑Fi** **;** **not** **flat** **admin** **to** **field** **OT** | **Separate** **from** **IoT** **SSID** **/** **VLAN** **where** **feasible** |
| **Admin** **stations** **(jump** **host,** **shelf** **laptop** **)** | **Z1** **or** **VPN** **into** **Z1** | **Dedicated** **account** **;** **no** **shared** **root** **;** **2FA** **for** **paths** **that** **touch** **Z2** **or** **cloud** **control** **planes** | **MV-*** **gates** **on** [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) |
| **Edge** **/** **WAN** **router** **/** **firewall** | **WAN** **demarc** **at** **each** **site** | **Policy** **zone** **between** **Z3** **and** **Z1** **/** **Z2** **;** **deny** **by** **default** **inbound** **from** **Z3** | **Starlink** **terminal** **—** **untrusted** **cable** **from** **ISP** **perspective** |
| **Field** **gateway(s)** **(MQTT,** **edge** **compute** **)** | **Z2** | **One** **/** **few** **ingress** **points** **to** **sensors** **;** **admin** **UI** **not** **Internet-routable** | **Patch** **cadence** **owner** **named** |
| **Telemetry** **devices** **(sensors,** **LoRa** **nodes** **)** | **Z2** **edge** **or** **RF** **only** | **No** **direct** **routable** **IPs** **;** **gateway** **aggregates** | **Local** **path** **can** **survive** **WAN** **loss** |
| **Cameras** **/** **NVR** | **Dedicated** **IoT** **/** **cam** **VLAN** **/** **SSID** **in** **Z1** **/** **Z2** | **No** **routing** **to** **admin** **VLAN** **without** **rules** **;** **NVR** **not** **exposed** **WAN** **:80** **/** **554** **raw** | **Viewing** **via** **VPN** **or** **TLS** **app** **only** |

**Rule**: **Cameras** **and** **gateways** **are** **not** **in** **the** **same** **trust** **bucket** **as** **family** **laptops** **—** **even** **if** **same** **physical** **building**.

---

<h2 id="vpn-overlay-assumptions">VPN / overlay network — assumptions</h2>

| Topic | Policy |
|-------|--------|
| **What** **the** **overlay** **protects** | **Confidentiality** **and** **integrity** **of** **admin** **/** **telemetry** **sessions** **across** **Z3** **—** **not** **“** **trust** **everyone** **on** **the** **VPN** **”** **(identity** **and** **RBAC** **still** **required** **)**. |
| **Mutual** **authentication** | **Keys** **or** **certs** **rotatable** **;** **no** **long-lived** **shared** **PSKs** **across** **unrelated** **devices** **without** **rotation** **plan**. |
| **Split** **tunneling** | **Conscious** **choice** **:** **what** **exits** **via** **overlay** **vs** **direct** **Internet** **—** **document** **to** **avoid** **accidental** **data** **paths**. |
| **Starlink** **as** **underlay** | **Same** **overlay** **crypto** **whether** **underlay** **is** **fiber,** **LTE,** **or** **LEO** **—** **do** **not** **skip** **TLS** **/** **WireGuard** **/** **TLS** **to** **cloud** **because** **“** **it’s** **our** **dish** **”** **.** |

---

<h2 id="internet-exposure-policy">Internet exposure — allowed vs forbidden (direct)</h2>

| May be **internet-reachable** **(only** **with** **controls** **)** | **Must** **never** **be** **directly** **exposed** **(no** **port** **forward** **/** **public** **listener** **without** **TLS** **+** **auth** **+** **rate** **limits** **)** |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TLS-terminated** **public** **services** **you** **operate** **(e.g.** **HTTPS** **dashboard** **behind** **reverse** **proxy,** **OIDC** **)** **with** **patch** **owner** | **Raw** **admin** **:** **SSH** **/** **WinRM** **/** **router** **GUI** **/** **gateway** **config** **UI** **on** **public** **IP** |
| **Cloud** **broker** **/** **API** **endpoints** **(vendor** **)** **—** **policy** **choice** | **MQTT** **/** **broker** **without** **TLS** **+** **strong** **auth** **on** **any** **routable** **interface** |
| **Outbound-only** **field** **agents** **(no** **inbound** **listen** **)** | **RTSP** **/** **ONVIF** **camera** **streams** **to** **the** **open** **Internet** |
| **Optional** **STUN/TURN** **for** **webrtc** **—** **if** **used,** **scoped** | **Flat** **RDP** **to** **internal** **desktop** **at** **farm** **or** **home** |

**Default**: **Deny** **all** **inbound** **from** **Z3** **to** **Z1** **/** **Z2** **;** **open** **only** **what** **is** **listed** **in** **a** **private** **runbook** **with** **owner** **and** **review** **date**.

---

## Security implications — Starlink (or any LEO WAN) at **home** vs **farm**

| Topic | **`SITE_HOME`** **(e.g.** **Claxton** **)** | **`SITE_FARM`** **(e.g.** **Demory** **)** |
|-------|----------------|---------------|
| **Threat** **model** | **More** **valuable** **data** **(records,** **keys** **to** **other** **sites** **)** **if** **homelab** **over-trusted** | **Physical** **access** **to** **gear** **;** **fewer** **eyes** **on** **blinkenlights** |
| **NAT** **/** **addressing** | **CGNAT** **common** **—** **design** **admin** **around** **outbound** **/** **controlled** **rendezvous** | **Same** **;** **second** **terminal** **increases** **attack** **/** **cost** **surface** **without** **discipline** |
| **Outage** **=** **security** **event** | **Sessions** **drop** **;** **no** **silent** **“** **we’re** **fine** **”** **from** **cloud** **without** **local** **checks** | **Remote** **trust** **zero** **—** **see** **degraded** **modes** |
| **Terminal** **physical** **security** | **Theft** **/** **tamper** **—** **key** **revocation** **path** | **Higher** **theft** **risk** **—** **encrypt** **storage** **;** **no** **sole** **copy** **of** **secrets** **on** **field** **box** |

**Policy**: **LEO** **WAN** **does** **not** **change** **Z3** **/** **Z3a** **—** **it** **only** **changes** **latency** **and** **availability** **statistics**.

---

## Ties — runbooks, degraded modes, execution

| Artifact | Link |
|----------|------|
| **Degraded** **/** **WAN** **impaired** | [`Manual fallback and degraded modes — critical operations`](manual-fallback-degraded-modes-critical-operations.md), [`Automation degraded modes SOP`](automation-degraded-modes-manual-fallback-sop.md) |
| **Backhaul** **/** **broker** **down** | [`Runbook — broker or backhaul down`](runbook-broker-or-backhaul-down.md) |
| **Power** **at** **remote** **site** | [`Runbook — power loss at remote site`](runbook-power-loss-remote-site.md) |
| **Automation** **/** **connectivity** **stops** **(MV** **/** **CS** **)** | [`Automation stop rules`](automation-stop-rules-two-site-smart-farm.md) |
| **First** **24** **months** **connectivity** **validation** | [`Validation and pilot plan` § Connectivity validation](validation-and-pilot-plan-first-24-months-east-tennessee-two-site.md#connectivity-validation) |
| **Business** **plan** **package** | [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) |

---

## Related

- [`Reference architecture — 5 ac + 120 ac`](reference-architecture-5ac-homebase-120ac-smart-farm.md)
- [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md)
- [`CISA — Guide to securing remote access software`](../source-notes/cisa-guide-securing-remote-access-software-508-pdf.md) (ingested patterns)
