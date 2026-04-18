Hey everyone 👋

If you have been following my posts, you might have noticed that I have been pretty quiet lately 😅  
There is a good reason for that

I have been spending a lot of time building my own homelab a place where I can safely test, break, and rebuild complex infrastructures without worrying about cloud costs or production risks 🧑💻

My goal is simple  
Create a production grade Kubernetes environment at home using Proxmox for virtualization and Kubespray for cluster provisioning 💡  
This environment allows me to test real world scenarios and also experiment with features for my Kubermates project 🚀

Let me walk you through the why and the how

---

⚙️ The Motivation

As a DevOps and SRE engineer, Kubernetes is part of my daily life.  
But testing new tools, scaling strategies, GitOps workflows, or security rules often requires:

✅ complete freedom  
✅ zero fear of downtime  
✅ repeatability  
✅ controlled costs

A homelab gives me full control of the stack including: network, storage, virtualization, routing, DNS, automation and resilience strategies 💪

It rapidly became much more than a hobby. It is now my mini data center

---

🧩 Proxmox as the Foundation

To host everything, I chose Proxmox VE

Reasons behind this choice:  
🖥️ clean and powerful web UI and CLI  
⚙️ excellent virtualization and storage integration  
🌐 flexible networking and clustering  
🔁 snapshots and backup system made for tests and disasters

Each hypervisor node runs multiple virtual machines that will become control planes, workers or utility nodes like DNS and monitoring services

Proxmox gives me the freedom to rebuild everything as many times as needed

---

☁️ Kubernetes Deployment With Kubespray

Once the virtual machines were ready, I needed a repeatable approach to deploy Kubernetes.  
I selected Kubespray because:

🔥 it is production proven  
🧩 uses Ansible which makes automation easy  
🔧 allows deep customization  
🔄 supports highly available clusters

This lets me rebuild the entire cluster in minutes while keeping the configuration under version control

Perfect for experimentation

---

💪 Homelab Specs

Right now, my homelab is running with:

🧠 96 GB of RAM  
⚡ 36 vCPUs

This gives enough headroom to simulate:

Autoscaling and performance constraints

Monitoring with Prometheus, Loki, Thanos etc

GitOps flows with Argo CD and Helmfile

Network isolation and multi tenancy

Production security patterns

Computing constraints actually make the optimization challenges even more interesting

---

🔬 A Playground for Kubermates

If you know me, you know I am working on Kubermates  
This homelab is now my real life testing ground for the platform

Here I can:  
✅ test onboarding flows and automation patterns  
✅ simulate multi tenant setups  
✅ validate best practices for deploy and operate  
✅ try both cluster and application level policies

Everything is reproducible and controlled  
Exactly what I need to test responsibly

---

🌐 Secure Remote Access With WireGuard VPN

Although everything runs at home, I still want to access the environment securely when I travel or work away from my desk

For this, I use WireGuard VPN running on a small gateway VM

Why WireGuard

🔒 strong encryption

⚡ ultra fast performance

🧩 minimal configuration

📱 clients for Linux, Mac, Windows, iOS and Android

My access architecture:

Only VPN traffic can reach the Proxmox cluster and Kubernetes nodes

No ports are exposed directly to the internet

Internal DNS and Ingress work exactly as inside the local network

So I get full access to Grafana, Argo CD, dashboards, kubectl and SSH  
as if I was physically at home 🏠

This keeps everything private and secure  
Perfect for a personal lab

---

🧠 Key Lessons Learned So Far

Building Kubernetes at home gives you a deeper understanding of what is behind the cloud curtain

Main takeaways

Networking is always trickier than expected 😅

Local DNS matters more than anyone admits

Good VM templates save hours of setup time

Resource constraints teach real FinOps awareness

Breaking things makes you learn faster

And the best part  
It is incredibly fun

---

🚀 What Comes Next

This is just the beginning

Upcoming articles in the series  
1️⃣ Proxmox hardware and virtualization best practices  
2️⃣ Kubespray automation and cluster bootstrapping  
3️⃣ DNS and networking architecture for homelabs  
4️⃣ GitOps, certificates and observability stack deployment  
5️⃣ How to simulate production workloads at home

The goal  
Help anyone build a professional grade Kubernetes experience locally  
without cloud billing surprises

Thanks for reading and stay tuned for more 🔥

[![Google article image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FziGriZ9.png)](https://dev.to/googleai/how-to-prompt-gemini-31s-new-text-to-speech-model-24bb?bb=263070)

## How to prompt Gemini 3.1's new text to speech model

Gemini 3.1 Flash text to speech (TTS) is a new model that you can direct to get the precise audio performance you want. In this blog post I'll share some tips on how to guide the model with prompts, and share some examples of its strengths.