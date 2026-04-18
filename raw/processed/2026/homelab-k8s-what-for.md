I often read that people set up some form of k8s cluster at home, like on a bunch of Raspberry PIs or older hardware.

I just wonder what do you use these clusters for? Is it purely educational? Which k8s distribution do you use? Do you run some actual workloads? Do you expose some of them to the internet? And if yes, how do keep them secure?

Personally, I only have a NAS for files - that's it. Can't think of what people do in their home labs ☺️

---

## Comments

> **lidstah** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8n12fk/) · 109 points
> 
> I'm a freelance sysadmin (and part-time teacher two days a week in a local engineering school, where I'm teaching Linux, networking, virtualization and Kubernetes (yay!)), I use it for:
> 
> - home-cinema purpose (jellyfin, koel (music) and such) which is good for the WAF (Wife Approval Factor)
> - game servers (EQemu (everquest, pex like it's 1999!), Luanti (formerly Minetest, voxel engine), Veloren (voxel ARPG), and so on, which is good for the CAF (Children Approval Factor)
> - My freelance business tools (ERP/accounting (dolibarr), note-taking (Outline), Gitea (personnal git repos), Bookstack (documentation), Semaphore (ansible, opentofu, terraform, pulumi), webmail (snappymail, as I've my own mail server hosted in a colocation, opensmtpd+dovecot+rspamd), kanboard (simple kanban), harbor (container registry), argoCD (gitops)).
> - home tools: nextcloud, immich, mealie, and such (good for both the WAF and CAF)
> - IdP: Authentik and OpenLDAP as a fallback when OIDC is not an option.
> - DNS: powerdns (postgre backend), dnsdist, pdns-recursor
> - Web: WikiJS (where all my engineering school courses reside), my blog, file/picture sharing (picoshare), privatebin, etc
> - I use it to validate setups, make proof of concepts and demos for my clients and prospects.
> - as my homelab setup is using the same technologies that I propose to my clients (ProxmoxVE, Proxmox Backup Server, Talos Linux, PostgreSQL, Debian, IDP, etc), it's great to failproof upgrades.
> - It's great for staying up-to-date, testing, learning stuff…
> 
> All in one, I'm quite happy with this setup: it's highly available, quite easy to maintain and upgrade, I've enough resources available to learn, test and play with some quite demanding software, while not costing too much on the electricity bill.
> 
> > **Reptile212** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8oxjhx/) · 7 points
> > 
> > Quick question, I am attempting to run something similar on my home lab but I am curious about how you've done your IdP deployment with a CI workflow. If your IdP is on k8s and you authenticate with your CI platform with the IdP do you suffer from the chicken and egg problem? I am currently spinning up GitLab to set up runners that will do my terraform, ansible, and k8s deployments.
> > 
> > > **lidstah** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8psn6z/) · 6 points
> > > 
> > > > how you've done your IdP deployment with a CI workflow. If your IdP is on k8s and you authenticate with your CI platform with the IdP do you suffer from the chicken and egg problem?
> > > 
> > > Indeed, to avoid the chicken and egg problem, I manually installed it using the authentik helm chart, it's decoupled from the CI/CD stuff. So I still upgrade it manually. It's polite enough to send me a mail when a new version is available, though :).
> 
> > **Big\_Excuse3398** · [2025-08-15](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8vx561/) · 4 points
> > 
> > Please tell me you have a blog.
> > 
> > **slykethephoxenix** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8prrua/) · 2 points
> > 
> > Fuel fin powder phone journey chance chick band flock arch host loaf cushion bloom. Actor fish harp otter draft fork rock giraffe oven green round room.
> > 
> > A|1NgCURGBT8hmyhltLC0tlDgHZArvfVi7KPICVf4k5jP7zxZY2SQhc/Gd6vtpyjMMjQYKyd7uyy8oNpxjzyoLIXaCqq03OBIpfNZYNMJI5EoDI6DhlxjTGLWzG0JD4TJbBK80JR6PG7FHz+velPsJRkmMLlSbVLJV/6xL14sVblo5jmvaCSLQEn8aH+AEYFd1Z3Es0hB1DkuiKNDbc67ghs1Fxk9H/HsbFCCNuyxyivAqNbtIQpmXQGJC+Zho7GQKQBpY5s7aOK0siXASh2PxvPLqJUDV4zoTGzegW5FVSG0wD+9IIpM6ePQ6ar0O5VQl5DEgfvF0lvSp21S9C9DIo48DstkYvbk=
> > 
> > AES-PSK:/BffvoqOVL56FcC4yi2F94ft0Kqrj2OGdJxb9ASDPqY=
> > 
> > Remove 'A|' and Decrypt with: [https://unbound-sigbreak.github.io/message-deencrypter/aes.html](https://unbound-sigbreak.github.io/message-deencrypter/aes.html)
> > 
> > > **lidstah** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8q0mtc/) · 3 points
> > > 
> > > For storage I use:
> > > 
> > > - two nfs-subdir-external-provisioner instances for stateless data (e.g. nextcloud users' storage, eqemu/spire files, videos, music, git repos). I have two NAS, one "big but slow boy" with good old spinners, 16TB total (RAID-5), mainly for videos/music/documents/etc, and one 4TB NVMe with 2TB allocated to proxmox VMs who need to be able to migrate quickly from one host to another and for disposable VMs (tests, PoCs and so on) , and 2TB for kube (new machine, using zVault, quite happy with it right now), so each nfs-subdir storage class maps to one NAS.
> > > - openEBS (replicated mode) for anything stateful (postgre, mariadb, sqlite…). It's not the fastest storage class available but it's been solid for my use case. It's also open source and free as in free beer.
> > > - On my clients' sites, we use Netapp appliances and the Netapp Trident storage class, which has been rock solid. But that have a… non-negligible cost :)
> > > 
> > > All my Proxmox nodes have 1TB NVMe internal storage (RAID-1), and all my kubernetes nodes' virtual disks (including openEBS virtual disks) are provisioned on each nodes local LVM storages for best performance. Proxmox cluster and NVMe NAS are on a 2.5Gbps switch with dedicated interfaces for storage (MTU 9000 bytes). Home backbone, big-boy NAS and backup NAS are still 1Gbps though. The plan for next year is to switch the proxmox cluster on a 10Gbps switch (and buy 10Gbps network interfaces for the proxmox nodes), and move the home backbone on the actual 2.5Gbps switch.
> > > 
> > > Backup is done by Proxmox Backup Server (it's an amazing piece of software) on an old NAS with 2x12TB spinners (RAID-1). External backup is done on another VM at previously mentionned colocation, only important data (documents, photos, ERP data, git repos…) is synchronized there on an encrypted volume, so it amounts to roughly 100GB of data. Never forget to regularly test your backups!

> **Nothos927** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8motmu/) · 36 points
> 
> I run Jellyfin and the \*arr suite as well as local dev tools like a Postgres instance

> **Attunga** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8mpt70/) · 22 points
> 
> I use OpenShift purely for learning both administration, various apps and operators as well development of apps that I deploy into OpenShift. The learning you can do at home is invaluable, it is nice to be able to do something on a business site in minutes that you have spent days working out how to do at home. You can also experiment and waste time at home, you just can't do that at a business site.
> 
> Hardware wise it is kind of demanding for a home lab but I can shut it down when I am not using it to save power.
> 
> With OpenShift there is a 60 day trial but it seems to just keep on updating even after the trial runs out. I rebuild it every few months though.
> 
> > **just-porno-only** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8nbssc/) · 6 points
> > 
> > > OpenShift
> > 
> > How did you install it? Did you have a fresh cluster then use helm to install OpenShift? For me that's how I installed Rancher on my cluster. But I think OpenShift > Rancher so I wanna go with that.
> > 
> > > **quentiin123** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8ntl5p/) · 8 points
> > > 
> > > Openshift is not something you install on top of a kubernetes cluster. It's a separate installation. For a lab you can go with a SNO cluster (single node)
> 
> > **Attunga** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8ptx26/) · 2 points
> > 
> > For those asking how I personally install it .... the first thing I do is plan my deployment. Work out hardware (vms or bare metal). This involves planning hosts, ingress address and API addresses then setting these up in DNS. Mostly you should have addresses for your hosts, an address for your api.\[cluster.\]\[domain\] and then a wildcard pointing to apps.\[cluster\].\[domain\].
> > 
> > Next you most likely need to set up a DHCP Server that will then assign IP Addresses and Hostnames to the MAC addresses I want to deploy it to.
> > 
> > You will also need a bunch of cheap USB Drives if installing on bare metal hardware, not needed for virtual.
> > 
> > You then need a free Red Hat developer account. You then go to [console.redhat.com](http://console.redhat.com/) (logging in with Developer account) --> Red Hat OpenShift --> Red Hat OpenShift Container Platform --> Create Cluster --> Datacenter (Tab) --> Platform Agnostic (Link)
> > 
> > You can then make your choice of the type you want, for ease of use I mostly choose Interactive. You then go through filling out the Wizard with the options you want.
> > 
> > Click past the Operators page (just do them later) and eventually you get to the Host Discovery page, you enter in all the details for the Host mac's somewhere there but the core is to click on the Add Hosts button at the top. A dialog comes up to offer to download an ISO, I usually change this to Full Image File and then add in my local SSH Public key to be deployed to the hosts. You can then click on Generate Discovery ISO, it will then give some links to download.
> > 
> > You can then click on the Download Button or what I do is grab the command and adjust it for Curl which seems to work best for some reason.
> > 
> > From there you boot up your hosts with the ISO, as they come up you will then see them in the console. You then assign the different hosts to different functions and continue on through the rest to networking where you set your network details.
> > 
> > You then click through to deploy .. and it mostly just works, the new cluster should be all ready to go in a couple of hours.
> > 
> > While it is going, download your cert and record the temporary kubeadmin password.
> > 
> > You should then have a working cluster with a 60 day expiry that just keeps on working ... and it is just the way I do it, plenty of other ways work as well

> **dopey\_se** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8mq3i4/) · 15 points
> 
> I run on r740 servers, before that mini PCs.
> 
> I learn by doing. I wanted to learn how to run Kubernetes, not simply how to use it. Also not just k8s but the complete gitops approach.
> 
> I run harvester+rancher and provision a rke2 guest cluster into harvester. Which to be fair still simplifies allot of the stack but it was a nice balance for me.
> 
> I run upwards of 20+ services with gitops principles/tools with majority accessible via internet (behind/integration with authentik).
> 
> I've seen the skills learn here translate to work. Became way way more comfortable with K8 s triage whether onprem or cloud due to this.
> 
> (I wrote a thing to monitor and notify me of new versions (semantic comparison), and can push the updated version to my git repo to trigger gitops :x)

> **ThePapanoob** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8mrma6/) · 12 points
> 
> It might sound weird but ease of use & reliability. Kubernetes is incredibly complex and nuanced wich makes it easy to fuck up. But im working with it all day anyway so i know pretty much all of its quirks good enough that its no longer hindering me. And quite the opposite it actually makes it easier now because i can use my whole gitops setup the same way i do it at work

> **UnfairerThree2** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8mwv5e/) · 8 points
> 
> 1. Learn by doing
> 2. kubesearch.dev / Home Operations
> 3. Some actual internet facing projects / volunteering work
> 4. Copy [github.com/onedr0p](https://github.com/onedr0p) wherever possible lol
> 
> > **onedr0p** · [2025-08-15](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8t3di5/) · 5 points
> > 
> > Hey I know that guy
> > 
> > > **UnfairerThree2** · [2025-08-15](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8t3k8z/) · 3 points
> > > 
> > > no way

> **boneheadcycler** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8ms4bm/) · 6 points
> 
> Definitely educational for me. I absolutely don’t need k8s at home. Portainer using docker compose would be plenty. However, I wanted to learn more about k8s and microservices, so I figured hands on experience would help me learn it the best.
> 
> I have 3 mini pcs running the cluster using k3s. Control plane (beelink s12pro, intel n100), 2 workers (beelink eqr5, amd 5825u).

> **MarxN** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8mphsg/) · 4 points
> 
> I run everything I can. Immich, pinchflat, home assistant to name a few. I have 4 minipc with maxed out memory and I can run a lot on quite cheap hardware $100 each. It's not only educational, but also my home prod . And a lot of fun.

> **failcookie** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8nz9sq/) · 4 points
> 
> I run k8s on my homelab. I’m a senior web dev, but I don’t actively do DevOps at my work. I just like to tinker, practice, and expand my knowledge of the process. I also host a lot of my own software. I used Docker for a while, but I wasn’t a fan of the gitops experience with it and I wanted more control in certain areas. It’s also been a fun experience to see how I can get HA going and trying to maintain max uptime for myself/family. Absolutely 100% overkill, but it’s been fairly easy to maintain once I got over the k8s learning curve.

> **rvm1975** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8mqsmb/) · 3 points
> 
> Smart house, solar generator, humility sensors and plants watering, nas for cctv, metrics storage, backup and torrents.
> 
> Using rancher desktop from opensuse.
> 
> No exposing but I can reach home network using OpenVPN. For security and protection from Chinese bulbs I am using linkerd and TLS authentication.
> 
> > **itsjakerobb** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8mziaa/) · 18 points
> > 
> > > humility sensors
> > 
> > That might be the funniest typo/autocorrect I’ve ever seen. 🤣

> **corgtastic** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8ms8a6/) · 3 points
> 
> I'm running the Ubuntu Kubernetes ([https://documentation.ubuntu.com/canonical-kubernetes/latest/snap/howto/](https://documentation.ubuntu.com/canonical-kubernetes/latest/snap/howto/)) that I picked out to try. I mostly use Rancher k3s and RKE2 at work.
> 
> I've got mine setup with ArgoCD and Renovate, so updating the various things I run is as simple as checking for new merge requests in the morning. I just look over the release notes in the merge request and merge it, then a few minutes later ArgoCD has it updated. Works great!

> **patrolsnlandrcuisers** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8mu3s8/) · 3 points
> 
> I ran multiple proxmox VMS before and got frustrated with the lack of control, I would get out of memory on one node while lots available on the other, I had to manually manage mounts and user IDs and lxc vs VMS...eventually I got Talos installed and now run a 12 node cluster lol, I LOVE that I can unplug a server and about 70% of services seamlessly fail and the others spin up and self repear over about 10 mins....if you become obsessed with high availability like I did k8s becomes the only option quickly

> **Horvaticus** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8odaip/) · 3 points
> 
> Because my garage has better uptime than our AWS environment at work! I built my k8s homelab out in 2019 to learn Kubernetes, and I maintain that learning bare-metal k8s is the best way for a newbie to learn about the core networking, storage, linux, and other k8s fundamentals.
> 
> All the solutions I've developed for work started right there in my garage, keeping up to date on that stuff is the best way to keep yourself ahead of the pack. Took those baseline configs into an on-prem k8s deployment at work in vsphere clusters, translated pretty well honestly. Now that I'm entirely AWS based at my current role it's nice to be able to keep up to date on the networking/hardware side of the equation as well.
> 
> I've got about 122TiB of "Linux ISOs" that are backed by the \*arr suite + usenet downloaders, indexers, and other various media tools. Then I run my personal webapps, home automation, various self-hosted-cloud components, etc. I just slotted a spare 3090 into that box so I've been wanting to experiment with LLM stuff too.

> **AnomalyNexus** · [2025-08-14](https://reddit.com/r/kubernetes/comments/1mpxa9l/comment/n8p2h4j/) · 3 points
> 
> A lot of the [r/selfhosted](https://www.reddit.com/r/selfhosted/) stuff ends up being docker based so with a bit of poking and prodding you can make it k8s.
> 
> A huge amount of homelab stuff is also on proxmox, so for experimentation spinning up a couple nodes is really easy. e.g. I'm currently figuring out Talos that way. Everything is cached & scripted so I can just rebuild the cluster over and over with zero cost/friction to try things. Think terraform except not.
> 
> > And if yes, how do keep them secure?
> 
> Most homelabs are behind a NAT/CG-NAT which cuts out 99% of the security problems you get with public clusters. That means people need to actively think about the expose part and even nooblets think about security at that point
> 
> > Do you expose some of them to the internet?
> 
> Opinions on that vary & all camps gets really frothy about it in homelab crowd. One side says VPN only, one side says cloudflare/tailscale tunnels, one side says proxy on public with authentik/similar and perhaps some crowdsec sprinkled on top