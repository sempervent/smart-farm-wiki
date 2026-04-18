---
title: Docker, Kubernetes, Compose, and Bake (edge and homelab)
page_type: topic
status: active
created: 2026-04-17
updated: 2026-04-18
tags:
  - docker
  - kubernetes
  - compose
  - bake
review_status: unreviewed
---

# Docker, Kubernetes, Compose, and Bake (edge and homelab)

**Narrative**: These imports cluster **multi-container** workflows and **cluster** choices relevant to **self-hosted** and **edge** environments. **Docker Compose** material ranges from “in depth” explainers to long **multi-service** guides and a very deep single-topic compose dive. **Docker Bake** sources cover **buildx bake** patterns for bundling and shipping compose-oriented projects. **Kubernetes** coverage contrasts **kubeadm**, **k3s**, **MicroK8s**, **Minikube**, **Talos**, and **RKE2**, then narrows to **K3s vs RKE2** selection, **when to use** each, and short **either/or** framing—useful when a homelab or farm-edge gateway moves past single-host Compose.

**Source notes**

- [`source-notes/docker-compose-in-depth.md`](../source-notes/docker-compose-in-depth.md)
- [`source-notes/mastering-docker-compose-multi-container-applications.md`](../source-notes/mastering-docker-compose-multi-container-applications.md)
- [`source-notes/deep-dive-docker-compose.md`](../source-notes/deep-dive-docker-compose.md)
- [`source-notes/docker-bake-comprehensive-guide.md`](../source-notes/docker-bake-comprehensive-guide.md)
- [`source-notes/building-compose-projects-with-bake.md`](../source-notes/building-compose-projects-with-bake.md)
- [`source-notes/kubernetes-distributions-overview-kubeadm-k3s-microk8s-minikube-talos-rke2.md`](../source-notes/kubernetes-distributions-overview-kubeadm-k3s-microk8s-minikube-talos-rke2.md)
- [`source-notes/rke2-vs-k3s-choosing-right-distribution.md`](../source-notes/rke2-vs-k3s-choosing-right-distribution.md)
- [`source-notes/when-to-use-k3s-and-rke2.md`](../source-notes/when-to-use-k3s-and-rke2.md)
- [`source-notes/k3s-or-rke2.md`](../source-notes/k3s-or-rke2.md)

**Related**

- [`Homelab, self-hosting, and edge narratives`](homelab-self-hosting-and-edge-narratives.md) — where these tools usually run in practice
- [`Farm data, farmOS, and agriculture lab builds`](farm-data-farmos-and-ag-lab-builds.md) — Drupal/farmOS hosting sometimes sits beside containerized stacks
- **Pi fleet + k3s + Longhorn (canonical)**: [`Homelab / edge Kubernetes platform strategy`](../analyses/homelab-edge-kubernetes-platform-strategy-pi-k3s-longhorn-rancher.md) · [`How to provision k3s, Longhorn, and Rancher on a Raspberry Pi fleet`](../analyses/how-to-provision-k3s-longhorn-and-rancher-on-a-raspberry-pi-fleet.md) · [`K3s / Longhorn / Rancher captures`](../source-notes/k3s-longhorn-rancher-pi-platform-official-captures-inbox-2026-04-18.md)
