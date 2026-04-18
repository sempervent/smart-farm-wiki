---
title: Structural audit — repository shape and canonical routing
page_type: analysis
status: active
created: 2026-04-21
updated: 2026-04-21
review_status: unreviewed
tags:
  - meta
  - information-architecture
  - maintenance
confidence: medium
---

# Structural audit — repository shape and canonical routing

**Purpose**: Periodic **structural** review of `smart-farm-wiki`: what works, what risks duplication or drift, and where to invest next—without replacing [`Domain content overview`](domain-content-overview.md) (domain steering) or [`Repository analysis`](repository-analysis.md) (tooling/CI scale).

---

## Strengths

| Area | Why it helps |
|------|----------------|
| **Layer split** | `raw/` provenance vs `wiki/` synthesis vs `docs/` handbook matches the LLM-wiki pattern; validation scripts enforce kebab-case, frontmatter, index coverage, and log format. |
| **East Tennessee two-site spine** | [`East Tennessee two-site farm business plan (package)`](../business-plan/east-tennessee-two-site-farm-business-plan.md) + [`Planning framework`](east-tennessee-two-site-farm-business-plan-framework.md) + [`topics/two-site-smart-farm-operations`](../topics/two-site-smart-farm-operations.md) bundle business plan, telemetry, finance, and runbooks into **discoverable tables**. |
| **Reference architecture package** | [`Reference architecture — 5-acre home base + 120-acre farm`](reference-architecture-5ac-homebase-120ac-smart-farm.md) + [`Field telemetry reference architecture — homestead + 120-acre farm`](field-telemetry-reference-architecture-homestead-120ac.md) + [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md) give **consistent vocabulary** (SoR, broker, backhaul). |
| **Strategic audit trilogy** | [`Strategic audit — decision-safe operations`](strategic-audit-decision-safe-operations.md), [`Information architecture — decision-safe operational brain`](information-architecture-decision-safe-operations.md), [`Implementation backlog — strategic audit`](implementation-backlog-strategic-audit.md) align **gap analysis** with **target IA**. |
| **Comparisons and runbooks** | LPWAN, records stack, equipment vs hire, gateway topology—paired with **degraded modes** and **runbooks**—reduce “one-off blog” sprawl if extended rather than duplicated. |
| **Mission and voice** | [`Smart Farm Wiki — mission, audience, and voice`](../concepts/smart-farm-wiki-mission-and-values.md) keeps prose norms out of `AGENTS.md`. |

---

## Structural risks

| Risk | Manifestation | Mitigation (wiki practice) |
|------|----------------|----------------------------|
| **Overlapping analyses** | **Generic** two-site logistics [`Dual-site operations model — non-agritourism`](dual-site-operations-model-non-agritourism.md) vs **scenario-specific** [`Two-site operating model — 5-acre home base and 120-acre farm`](two-site-operations-model-5ac-homebase-120ac-production.md); multiple **meta** “audit / backlog / implementation plan” pages. | Treat **ET scenario** pages as **canonical** for the business plan; use **dual-site** as **pattern** when enterprise is not lodging-led. Add **routing** sections (not merges) until content truly converges. Prefer **one** backlog: [`Implementation backlog — strategic audit`](implementation-backlog-strategic-audit.md) for P0–P3; link others as **historical** or **narrow** scopes. |
| **Weak entity layer** | **Demo** [`Example Organization`](../entities/example-org.md) coexisted with many pages naming **farmOS** and **Home Assistant** without **entity** anchors; regional programs (USDA, Extension) still often appear only via source-notes. | Add **`entities/`** for **named products** and orgs referenced repeatedly (**farmOS**, **Home Assistant** added with this audit); keep **concepts** for technology categories. |
| **Hub staleness** | Topic hubs can lag if new analyses are indexed but **not** linked from [`two-site-smart-farm-operations`](../topics/two-site-smart-farm-operations.md) or [`domain-content-overview`](domain-content-overview.md). | **Hub maintenance** rule in `AGENTS.md`: update hub tables when adding siblings. |
| **Placeholder honesty vs navigation** | Many pages use **`TBD`** tables correctly; risk is **orphan** analyses that repeat placeholders without linking **SoR** or **capital** gates. | Cross-link to [`Telemetry system of record`](telemetry-system-of-record-boundaries-and-authority.md), [`Validation backlog`](east-tennessee-two-site-farm-business-plan-validation-backlog.md), and [`Capital plan`](east-tennessee-two-site-farm-business-plan-capital-and-financing.md). |
| **Raw corpus and public build** | `raw/` links are **neutralized** in MkDocs HTML; **Obsidian** authors still need **local** files for deep reading. | Follow `docs/operations/raw-corpus-and-publishing.md`; run `--raw-pdf-links` locally when validating a full corpus. |

**Orphans / index**: Validation (`scripts/validate_wiki.py`) reports pages **missing from index** with no inbound links; current policy is **index everything intentional**. Not all warnings indicate “bad”—defer only with a **log** entry.

---

## Highest-value next canonical pages or merges

**Canonical pages to extend first (before new parallel essays)**

1. [`topics/two-site-smart-farm-operations`](../topics/two-site-smart-farm-operations.md) — add rows for any new runbook, comparison, or ET chapter; keep the **single** hub table current.
2. [`reference-architecture-5ac-homebase-120ac-smart-farm.md`](reference-architecture-5ac-homebase-120ac-smart-farm.md) — **package hub** for control-center vs production; link new telemetry or security work here.
3. [`telemetry-system-of-record-boundaries-and-authority.md`](telemetry-system-of-record-boundaries-and-authority.md) — **authority** questions should consolidate here rather than new “data governance” essays.
4. [`east-tennessee-two-site-farm-business-plan-framework.md`](east-tennessee-two-site-farm-business-plan-framework.md) — **index** for decision-grade business plan pages.

**Entity pages (fill as subjects stabilize)**

- [`farmOS`](../entities/farmos.md) — software product used across records and spatial discussions.
- [`Home Assistant`](../entities/home-assistant.md) — automation stack referenced in telemetry, LoRa bridges, and homelab topics.

**Merge / deprecation policy (not immediate merges)**

- **Do not merge** [`dual-site-operations-model-non-agritourism`](dual-site-operations-model-non-agritourism.md) into the ET **two-site** page: different **generality** and **assumptions**. **Routing** headers tie them instead.
- **Repository implementation plan** vs **business plan wiki git sequence**: keep both; first is **file/PR** mechanics, second is **merge order** for humans—cross-link in “Related” only if drift appears.

**Low-churn fixes applied with this audit**

- Broken comparison link → [`Telemetry system of record — boundaries and authority`](telemetry-system-of-record-boundaries-and-authority.md) in [`farmOS vs lightweight stack`](../comparisons/farmos-vs-lightweight-stack-two-site-farm.md).
- **Routing** paragraphs on dual-site and two-site operating models.
- **`AGENTS.md`** — governance rules: public vs private, canonicalization, entity-first, hubs, claim strength.

---

## Related

- [`Domain content overview`](domain-content-overview.md) — strand maturity and backlog.
- [`Structural audit — page ownership, entity gaps, and hub routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md) — canonical clusters, entity backlog, anti–analysis-sprawl routing.
- [`Information architecture — decision-safe operational brain`](information-architecture-decision-safe-operations.md) — target tree.
- [`AGENTS.md`](../../AGENTS.md) — operating contract (updated with governance sections).
