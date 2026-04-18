---
title: Homelab, edge, and networking — inbox batch (2026-04-18)
page_type: source_note
status: active
created: 2026-04-18
updated: 2026-04-18
source_ids:
  - raw/processed/2026/openwrt.pdf
  - raw/processed/2026/openwrt-extracted.md
tags:
  - homelab
  - k3s
  - longhorn
  - restic
  - wireguard
  - openwrt
  - esphome
  - farmos
review_status: unreviewed
---

# Homelab, edge, and networking — inbox batch (2026-04-18)

**Purpose**: **Provenance** for a **single** **inbox** **wave** moved from `raw/inbox/` to `raw/processed/2026/` (2026-04-18) with **kebab-case** basenames. **Epistemic**: Many pages **overlap** **prior** **captures** (e.g. k3s quick-start, restic 0.18.1, Longhorn)—treat as **alternate** **imports** **or** **supplementary** **reading**, not a second authority.

**PDF + extract (verify tables against PDF)**

| Raw | Role |
|-----|------|
| [`openwrt.pdf`](../../raw/processed/2026/openwrt.pdf) | OpenWrt documentation PDF (42 pp.) |
| [`openwrt-extracted.md`](../../raw/processed/2026/openwrt-extracted.md) | Machine text extract (`pdf_to_markdown.py`) |

---

## Kubernetes / homelab / backup (markdown)

| Raw path | Topic |
|----------|--------|
| [`architecture-k3s.md`](../../raw/processed/2026/architecture-k3s.md) | k3s architecture |
| [`configuration-options-k3s.md`](../../raw/processed/2026/configuration-options-k3s.md) | k3s configuration |
| [`installation-k3s.md`](../../raw/processed/2026/installation-k3s.md) | k3s installation index |
| [`quick-start-guide-k3s.md`](../../raw/processed/2026/quick-start-guide-k3s.md) | k3s quick start |
| [`k3s-lightweight-kubernetes-for-edge-iot-arm.md`](../../raw/processed/2026/k3s-lightweight-kubernetes-for-edge-iot-arm.md) | k3s product positioning |
| [`longhorn-csi-on-k3s.md`](../../raw/processed/2026/longhorn-csi-on-k3s.md) | Longhorn on k3s |
| [`introducing-longhorn-to-the-homelab.md`](../../raw/processed/2026/introducing-longhorn-to-the-homelab.md) | Longhorn narrative |
| [`backup-longhorn-system.md`](../../raw/processed/2026/backup-longhorn-system.md), [`backup-longhorn-system-1.md`](../../raw/processed/2026/backup-longhorn-system-1.md), [`restore-longhorn-system.md`](../../raw/processed/2026/restore-longhorn-system.md), [`the-longhorn-documentation.md`](../../raw/processed/2026/the-longhorn-documentation.md) | Longhorn backup/docs |
| [`backing-up-restic-0-18-1-documentation.md`](../../raw/processed/2026/backing-up-restic-0-18-1-documentation.md), [`removing-backup-snapshots-restic-0-18-1-documentation.md`](../../raw/processed/2026/removing-backup-snapshots-restic-0-18-1-documentation.md) | restic 0.18.1 |
| [`build-a-rke2-kubernetes-cluster-with-longhorn-and-rancher.md`](../../raw/processed/2026/build-a-rke2-kubernetes-cluster-with-longhorn-and-rancher.md), [`simple-rke2-longhorn-and-rancher-install.md`](../../raw/processed/2026/simple-rke2-longhorn-and-rancher-install.md) | RKE2 + Longhorn + Rancher narratives |
| [`part-4-automating-homelab-kubernetes-setup-deploying-longhorn-and-minio.md`](../../raw/processed/2026/part-4-automating-homelab-kubernetes-setup-deploying-longhorn-and-minio.md) | Longhorn + MinIO automation |
| [`raspberry-pi-k3s-homelabrancher-longhorn-storage-md-at-main.md`](../../raw/processed/2026/raspberry-pi-k3s-homelabrancher-longhorn-storage-md-at-main.md) | Pi + k3s + Longhorn repo narrative |
| [`quick-installation.md`](../../raw/processed/2026/quick-installation.md) | Longhorn quick install (title in source) |
| [`argo-cd-declarative-gitops-cd-for-kubernetes.md`](../../raw/processed/2026/argo-cd-declarative-gitops-cd-for-kubernetes.md) | Argo CD |
| [`basic-understanding-of-how-to-navigate-the-k8s-official-documentation.md`](../../raw/processed/2026/basic-understanding-of-how-to-navigate-the-k8s-official-documentation.md) | K8s docs navigation |
| [`kuberneteswebsite-kubernetes-website-and-documentation-repo.md`](../../raw/processed/2026/kuberneteswebsite-kubernetes-website-and-documentation-repo.md) | kubernetes.io repo readme |

**Homelab culture / setup essays**

| Raw path | Topic |
|----------|--------|
| [`why-i-built-my-own-homelab-to-run-kubernetes.md`](../../raw/processed/2026/why-i-built-my-own-homelab-to-run-kubernetes.md) | Motivation essay |
| [`7-essential-apps-for-your-homelab-kubernetes-cluster.md`](../../raw/processed/2026/7-essential-apps-for-your-homelab-kubernetes-cluster.md) | App list |
| [`an-over-engineered-home-lab-with-docker-and-kubernetes.md`](../../raw/processed/2026/an-over-engineered-home-lab-with-docker-and-kubernetes.md) | Over-engineered lab |
| [`homelab-kubernetes-cluster-setup-of-course-it-s-free.md`](../../raw/processed/2026/homelab-kubernetes-cluster-setup-of-course-it-s-free.md) | Cluster setup |
| [`homelab-k8s-what-for.md`](../../raw/processed/2026/homelab-k8s-what-for.md) | Why k8s in homelab |

**farmOS**

| Raw path | Topic |
|----------|--------|
| [`docker-farmos-org.md`](../../raw/processed/2026/docker-farmos-org.md) | farmOS Docker / dev hosting (verify version vs [farmOS hosting](https://farmos.org/hosting/)) |

**Edge / IoT docs**

| Raw path | Topic |
|----------|--------|
| [`esp32-platform.md`](../../raw/processed/2026/esp32-platform.md) | ESP32 (Espressif) |
| [`esphome-core-configuration.md`](../../raw/processed/2026/esphome-core-configuration.md), [`esphome-docs.md`](../../raw/processed/2026/esphome-docs.md) | ESPHome |
| [`eclipse-mosquittomosquitto-eclipse-mosquitto-an-open-source-mqtt-broker.md`](../../raw/processed/2026/eclipse-mosquittomosquitto-eclipse-mosquitto-an-open-source-mqtt-broker.md), [`mosquitto-conf-man-page.md`](../../raw/processed/2026/mosquitto-conf-man-page.md) | Mosquitto MQTT |

**Networking / VPN**

| Raw path | Topic |
|----------|--------|
| [`wireguard-archwiki.md`](../../raw/processed/2026/wireguard-archwiki.md), [`quick-start-wireguard.md`](../../raw/processed/2026/quick-start-wireguard.md), [`piratewireguard-docs-unofficial-wireguard-documentation-setup-usage-configuration-and-full-example-setups-for-vpns-supporting-both-servers-roaming-clients.md`](../../raw/processed/2026/piratewireguard-docs-unofficial-wireguard-documentation-setup-usage-configuration-and-full-example-setups-for-vpns-supporting-both-servers-roaming-clients.md) | WireGuard |

**Longhorn doc hub (short)**

| Raw path | Topic |
|----------|--------|
| [`documentation.md`](../../raw/processed/2026/documentation.md) | Longhorn docs landing / index (confirm against upstream) |
| [`quick-installation.md`](../../raw/processed/2026/quick-installation.md) | Longhorn quick installation (1.11.1 path in page) |

---

## Synthesis links

- **DR / backup**: [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md), [`K3s / Longhorn / Pi captures`](k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md), [`Backup / DR — official documentation cluster`](backup-dr-official-documentation-cluster.md)
- **Homelab / k8s topics**: [`Homelab, self-hosting, and edge narratives`](../topics/homelab-self-hosting-and-edge-narratives.md), [`Docker, Kubernetes, Compose, and Bake`](../topics/docker-kubernetes-compose-and-bake.md)
- **Field / MQTT**: [`LoRa, MQTT, and gateway bridges`](../topics/lora-mqtt-and-gateway-bridges.md), [`Field network IoT comparisons`](../topics/field-network-iot-comparisons.md)
- **Remote access**: [`Remote access and operational security model — two-site smart farm`](../analyses/remote-access-operational-security-model-two-site-smart-farm.md) (WireGuard/OpenWrt as **optional** **farm** **edge** **context**)
