---
title: Smart Farm Wiki — mission, audience, and voice
page_type: concept
status: active
created: 2026-04-18
updated: 2026-04-18
tags:
  - meta
  - mission
review_status: unreviewed
---

# Smart Farm Wiki — mission, audience, and voice

This page holds the **mission statement**, **audience**, **values**, and **voice** for the **Smart Farm Wiki**—the domain-facing “why” and “who we serve,” distinct from the **mechanical** rules in [`AGENTS.md`](../../AGENTS.md) (repository contract) and the **operator handbook** in [`docs/`](../../docs/index.md).

---

## Mission statement

**Smart Farm Wiki** exists to **compound practical knowledge** for people building **resilient, observant, small- and medium-scale food and land systems**—and the **networks, power, and data** that support them—by maintaining a **transparent, cited, agent-habitable** synthesis layer over an immutable evidence corpus.

We connect **soil, water, crops, and animals** with **honest economics and place** (markets, regulation, seasonality) and with **appropriate technology** (field connectivity, edge devices, energy, time discipline)—without reducing land or livestock to gadget demos or turning the vault into uncited opinion.

---

## Vision (where this can go)

Over time, the wiki should read as a **trustworthy atlas**: cross-linked **topics** and **analyses** that respect **uncertainty**, flag **stale** claims, and make it **obvious** what is grounded in **`raw/`** sources versus forward-looking prompts or models. The published site should welcome **human readers** and **automated maintainers** equally.

---

## Audience

- **Owner-operators and serious homesteaders** planning enterprises, infrastructure, or diversification (including agritourism).
- **Builders and integrators** choosing **LoRa, LoRaWAN, Meshtastic, Wi‑Fi HaLow**, solar, or farm data stacks—who need **tradeoffs**, not a single vendor answer.
- **Agents and researchers** who require **inspectable** markdown, **stable paths**, and **provenance** to extend the corpus responsibly.

---

## Values (authoring and maintenance)

1. **Evidence before swagger** — Prefer **source-notes** tied to `raw/processed/` over unattributed assertions; when evidence is thin, say so (`confidence`, `review_status`).
2. **Place and scale honesty** — Many sources skew **regional** (e.g. business checklists); generalize carefully or label **locale**.
3. **Safety and compliance humility** — Legal, electrical, animal-welfare, and food-safety contexts get **disclaimers** and pointers to professionals, not fake certainty.
4. **Incremental truth** — **Append** dated subsections when facts conflict; use **`supersedes`** chains rather than silent rewrites.
5. **Readable structure** — **Topics** cluster themes; **concepts** define terms; **analyses** hold arguments and plans—so readers can enter from intent, not folder names alone.

---

## Voice and prose style

- **Direct and concrete** — Name **species, acres, protocols, and failure modes** where useful; avoid filler.
- **Technical but accessible** — Define acronyms on first use in a page; link to **concepts** instead of jargon walls.
- **Neutral where possible** — Marketing language from imported sources is **labeled** as such; vendor claims are not adopted as fact without evidence.
- **Consistent with the repo contract** — Prose lives here; **workflows** (ingest, query, lint) remain in **`AGENTS.md`** and **`docs/workflows/`**.

---

## Relationship to other documents

| Document | Role |
|----------|------|
| [`AGENTS.md`](../../AGENTS.md) | **Highest-priority** behavior: layers, immutability, log, validation—**not** domain mission prose. |
| [`Wiki overview`](../overview.md) | How to **navigate** this vault. |
| [`Domain content overview`](../analyses/domain-content-overview.md) | **Map** of subject-matter strands. |
| [`Repository analysis`](../analyses/repository-analysis.md) | **Tooling and CI** profile. |
| [`docs/index.md`](../../docs/index.md) | **Handbook** for running the template (not MkDocs-published as part of wiki site in this repo’s split). |

---

## Review

When **mission or voice** changes materially, update this page, **append** [`log.md`](../log.md), and align the **Mission** subsection in [`AGENTS.md`](../../AGENTS.md) so agents still see the pointer in one scan.
