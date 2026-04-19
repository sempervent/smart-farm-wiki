---
title: PostgreSQL and PostGIS — official documentation primary cluster
page_type: source_note
status: active
created: 2026-04-24
updated: 2026-04-17
tags:
  - postgresql
  - postgis
  - farmos
  - documentation
review_status: unreviewed
confidence: high
---

# PostgreSQL and PostGIS — official documentation primary cluster

## Evidence summary

| Field | Content |
|-------|---------|
| **Abstract** | **Primary URLs** (PostgreSQL manual, backup chapter, PostGIS reference) for **release-accurate** behavior—**cluster** note so blog/Medium explainers in the vault stay **secondary**. |
| **Authority mix** | **Project official** documentation (web); vault **captures** elsewhere for farmOS/Docker/DR context. |
| **Decision relevance** | **Backup/restore** semantics, **spatial** indexes, and **SQL** behavior for **farmOS** and **PostGIS** geometry—feeds [`Backup strategy comparison — farmOS, homelab, PostgreSQL, containers`](../analyses/backup-strategy-comparison-farmos-homelab-postgresql-containers.md). |
| **Canonical wiki links** | [`Farm data, farmOS, and agriculture lab builds`](../topics/farm-data-farmos-and-ag-lab-builds.md) · [`Backup and disaster recovery package — smart farm stack`](../analyses/backup-and-disaster-recovery-package-smart-farm-stack.md) · [`farmOS documentation captures`](farmos-documentation-captures-inbox-2026-04-18.md) |

**Key claims** (public-safe):

- **postgresql.org/docs/current** and **postgis.net/docs** are the **authority** for **versioned** behavior; Medium articles are **pedagogy only**.

**Open questions / follow-ups**

- Pin **Postgres major** and **PostGIS** versions in runbooks when production stack is fixed.

**Purpose**: **Operator-grade** entry points for **behavior and semantics** of **PostgreSQL** and **PostGIS** as used by **farmOS** and homelab stacks—so **Medium** / blog **explainers** ([`postgresql-deep-dive-query-flow-medium-part-1`](postgresql-deep-dive-query-flow-medium-part-1.md), [`postgis-gist-spatial-index-medium`](postgis-gist-spatial-index-medium.md)) stay clearly **pedagogical**, not **release truth**.

---

## Primary (project / standards)

| Topic | Canonical URL |
|--------|----------------|
| **PostgreSQL** manual (current) | https://www.postgresql.org/docs/current/ |
| **SQL commands** | https://www.postgresql.org/docs/current/sql.html |
| **Backup / dump** | https://www.postgresql.org/docs/current/backup.html |
| **PostGIS** manual | https://postgis.net/docs/ |
| **PostGIS** reference (functions) | https://postgis.net/docs/reference.html |

---

## Vault captures (when present)

- farmOS + Docker / deployment captures: [`farmOS documentation captures`](../source-notes/farmos-documentation-captures-inbox-2026-04-18.md), [`homelab backup stack — official captures`](homelab-backup-stack-official-captures-inbox-2026-04-18.md)
- DR doctrine: [`Backup / DR — official documentation cluster`](backup-dr-official-documentation-cluster.md)

---

## Exploratory (low authority for behavior claims)

- [`postgresql-deep-dive-query-flow-medium-part-1.md`](postgresql-deep-dive-query-flow-medium-part-1.md) — **`confidence: low`**
- [`postgis-gist-spatial-index-medium.md`](postgis-gist-spatial-index-medium.md) — **`confidence: low`**

---

## Meta

- [`Source authority hardening audit`](../analyses/source-authority-hardening-audit.md)
