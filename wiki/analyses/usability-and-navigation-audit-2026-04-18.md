---
title: Usability and navigation audit — 2026-04-18
page_type: analysis
page_subtype: meta_audit
status: active
created: 2026-04-18
updated: 2026-04-18
tags:
  - meta
  - navigation
  - information-architecture
  - usability
review_status: unreviewed
confidence: high
---

# Usability and navigation audit — 2026-04-18

**Purpose**: Document **reader-facing** friction in a large markdown wiki: **flat catalogs**, **weak visual hierarchy**, **canonical vs supporting** confusion, and **source-note** usability. This audit **complements** [`Structural debt audit — wiki IA and operational maturity`](structural-debt-audit-wiki-ia-and-operational-maturity.md) (tooling/metadata) and [`Structural audit — page ownership, entity gaps, and hub routing`](structural-audit-page-ownership-entity-gaps-and-hub-routing.md) (ownership). **Companion pattern**: [`Source-note abstract and evidence pattern`](../concepts/source-note-abstract-and-evidence-pattern.md).

---

## Executive summary

| Finding | Severity | Mitigation (this pass) |
|---------|----------|-------------------------|
| [`index.md`](../index.md) **Overview** mixes onboarding, audits, package hubs, standards, procedural strategy, and **many** source-note previews—**similar visual weight** for different jobs | High | **Tighten** Overview: **three reader lanes** + pointer to hubs; **move** long source-note batch lines out of Overview where possible; **link** this audit + pattern page |
| **Business plan** section in `index.md` is a **full TOC**—correct for completeness, easy to mistake for “read all of this in order” | Medium | **Emphasize** [`Start here`](../topics/start-here-smart-farm-wiki.md) and **package hub** first; hubs already state **canonical first**; [`overview.md`](../overview.md) shortened to **lane-based** entry |
| **Analyses** section at bottom of `index.md` duplicates **many** links already reachable via hubs—**escape hatch** exists ([`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md)) but is **not** always obvious from the homepage | Medium | **Surface** themed entry in Overview + **start-here** table row; hub page **unchanged** in scope, **clearer** cross-links |
| **Source-notes** vary: some have **purpose + synthesis hooks**; others are **path lists** only—hard to scan in MkDocs or Obsidian | Medium | **Standardized** [`Evidence summary`](../concepts/source-note-abstract-and-evidence-pattern.md) block on **high-value** cluster notes |
| **Callouts and maturity**: standards use `page_subtype: standard`; guides use `operational_maturity`—**not all** reader landing pages restate **draft vs field_tested** | Low | Audit only; **defer** bulk frontmatter edits unless a page is already being touched |
| **Known / assumptions / unknowns**: strongest on **business plan** and **site intelligence** pages; **weaker** on some **topic** hubs that are mostly link lists | Medium | Hubs **retain** tables; **add** one-line **routing** intent at top (targeted edits, not new pages) |

---

## A. Navigation audit

### Flat or noisy index sections

- **`index.md` — Overview** (~lines 4–51): Combines **start pages**, **multiple structural audits**, **package hubs**, **operational standards** (long bullet list), **procedural guides**, then **additional** links (structural debt, execution evidence cluster, inbox batches). Readers see **ten-plus** peer bullets before the **Business plan** heading.
- **`index.md` — Source notes** (~lines 224–463): A **single flat list** of **hundreds** of entries—necessary for **validator/orphan** hygiene, but **not** a reading order. Discovery relies on **cluster indexes** and **topic hubs**.

### Hubs that are strong vs weak

- **Strong**: [`Wiki navigation and structural hubs`](../topics/wiki-navigation-and-structural-hubs.md) (tables by job), [`Two-site smart farm operations`](../topics/two-site-smart-farm-operations.md) (canonical ownership table), [`Start here — Smart Farm Wiki`](../topics/start-here-smart-farm-wiki.md) (fast-path table).
- **Weaker by nature (index-style)**: [`Authoritative execution evidence cluster — East Tennessee`](../source-notes/authoritative-execution-evidence-cluster-east-tennessee.md)—valuable **content**, but **table-of-tables** without a **short abstract** at the top was harder to scan; **addressed** with an **Evidence summary** block.

### Hard to find from homepage / overview

- **Themed analyses entry**: buried at **bottom** of `index.md` (`## Analyses`)—easy to miss when Overview is already long.
- **Evidence / provenance vocabulary**: [`Evidence grade and canonical authority`](../concepts/evidence-grade-and-canonical-authority.md) is linked from **Start here** but not from **every** hub; **acceptable** if **Start here** + **overview** stay prominent.

### Where readers cannot tell where to start

- **New reader**: should use [`Start here`](../topics/start-here-smart-farm-wiki.md) → [`overview.md`](../overview.md)—**not** the full `index.md` **Analyses** list.
- **Agent / maintainer**: [`index.md`](../index.md) + [`log.md`](../log.md) + [`AGENTS.md`](../../AGENTS.md).
- **East Tennessee package**: [`business-plan/east-tennessee-two-site-farm-business-plan.md`](../business-plan/east-tennessee-two-site-farm-business-plan.md) spine, not the **entire** business-plan block in `index.md` in sequence.

### Similarly weighted links (friction)

- Multiple **structural audits** in Overview (**repository**, **ownership**, **entity gaps**, **source authority**, **structural debt**)—all **legitimate** but **overwhelming** for a first visit. **Mitigation**: [`overview.md`](../overview.md) **lanes** + **one** link to this audit instead of repeating the full audit menu.

---

## B. Style and structure audit

### Weak summaries

- Some **topic** pages are **link-only** after one paragraph; acceptable for **hubs** if the **first screen** states **who should open this** and **what not to duplicate**.

### Long walls of links

- **`index.md`** Business plan and Analyses sections: **by design** comprehensive; **risk** is **accidental linear reading**. **Mitigation**: **canonical-first** language in **package hub** + **execution dossier** pointers.

### Inconsistent callouts

- Mix of **`**bold**` purpose lines**, tables, and **horizontal rules**—acceptable; **avoid** adding new ad-hoc emoji or HTML in markdown.

### Tables and checklists

- **Hubs** increasingly use tables (good). **Standards** use checklist-shaped prose—**consistent** with `page_subtype: standard`.

### Status / maturity indicators

- **Operational** pages: prefer **`operational_maturity`** where procedures exist ([`Procedural guides package strategy`](../topics/procedural-guides-package-strategy-smart-farm-wiki.md)). **Gap**: not every **hub** repeats **pilot vs production**; **low priority** unless editing those pages for other reasons.

### Known / assumptions / unknowns structure

- **Strong** on parcel and execution pages; **source-notes** historically emphasized **raw paths** over **decision relevance**. **Mitigation**: [`Source-note abstract and evidence pattern`](../concepts/source-note-abstract-and-evidence-pattern.md).

---

## C. Source-note improvement strategy (reference)

Implemented as a **reusable** block documented on [`Source-note abstract and evidence pattern`](../concepts/source-note-abstract-and-evidence-pattern.md). **Principles**:

- **Public-safe**: **Abstract** and **key claims** must read clearly when **`raw/`** links are **neutralized** in MkDocs (claims cite **authority type**, not only file paths).
- **Lightweight**: **one** summary table or short sections—**not** a second full essay.
- **Canonical-first**: every **cluster** note should link **synthesis** pages **above** the raw inventory.

---

## D. Implemented routing updates (this session)

- [`overview.md`](../overview.md): **three-lane** entry for humans.
- [`index.md`](../index.md): **Overview** section: **reader lanes**, **link** to this audit and **source-note pattern**; trim redundant bullets where superseded by lanes.
- [`topics/start-here-smart-farm-wiki.md`](../topics/start-here-smart-farm-wiki.md): **navigation / evidence** row.
- [`topics/wiki-navigation-and-structural-hubs.md`](../topics/wiki-navigation-and-structural-hubs.md): **Meta** table row for this audit + pattern.
- **High-value source-notes**: **Evidence summary** blocks on cluster indexes (see pattern page for list).

---

## E. Deferred / next passes

- **Optional**: split `index.md` **Source notes** into **cluster indexes only** in the Overview (would require **policy** change and **validator** alignment)—**not** done here.
- **Bulk** `operational_maturity` on all runbooks—**defer** to procedural package owner.
- **MkDocs** theme tweaks (fonts, sidebar)—out of scope for markdown-only pass.

---

## See also

- [`How to read this wiki`](../topics/how-to-read-this-wiki.md)
- [`Evidence grade and canonical authority`](../concepts/evidence-grade-and-canonical-authority.md)
- [`Ingest visibility gap — authoritative evidence vs published wiki (East Tennessee)`](ingest-visibility-gap-authoritative-evidence-east-tennessee.md)
