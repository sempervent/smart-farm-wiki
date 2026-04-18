# Publishing (MkDocs + GitHub Pages)

## What gets published

- The **wiki** in `wiki/` is the MkDocs site (`mkdocs.yml` sets `docs_dir: wiki`). Navigation is generated from the wiki tree; start from `wiki/index.md` in the built site.
- The **operator handbook** in `docs/` is **not** included in the MkDocs build; it remains in-repo documentation for humans and agents (read in GitHub or your editor).

## GitHub Actions

- **`.github/workflows/ci.yml`** — pull requests and pushes: `uv sync --frozen`, validate, pytest, MkDocs strict build (wiki only).
- **`.github/workflows/docs.yml`** — pushes to `main` and manual dispatch: same steps plus upload to GitHub Pages (`actions/deploy-pages`).
- Uses concurrency to cancel superseded runs.

## Repository settings

Enable **GitHub Pages** with the **GitHub Actions** source. The first successful deploy creates the environment; no legacy `gh-pages` branch is required.

## Local build

```bash
uv sync
uv run mkdocs build --strict
```

Artifacts land in `site/` (gitignored).

**Diagrams (Mermaid):** `mkdocs.yml` enables the **`mermaid2`** plugin (`mkdocs-mermaid2-plugin`). Pages can use fenced `mermaid` code blocks; the build loads Mermaid from CDN. Example: [`wiki/analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md`](../../wiki/analyses/two-site-smart-farm-network-topology-and-wan-edge-reference.md).

**Raw links:** Markdown links into `raw/` are rewritten at build time by `scripts/mkdocs_neutralize_raw_links.py` (see [`raw-corpus-and-publishing.md`](raw-corpus-and-publishing.md)) so the public site does not expose broken URLs to omitted evidence files. Obsidian-authored sources stay unchanged.
