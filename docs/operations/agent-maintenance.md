# Agent maintenance

Automation (Codex, Claude Code, Cursor agents, etc.) should treat [`AGENTS.md`](https://github.com/sempervent/llm-wiki-template/blob/main/AGENTS.md) as the **highest-priority** contract.

## Priorities

1. `AGENTS.md` — mission, layers, workflows, log rules
2. `README.md` — human orientation
3. Task-specific user instructions

## Session pattern

1. Read `AGENTS.md` and `wiki/index.md`.
2. Perform ingest/query/lint in small, verifiable steps. On ingest: follow **capture + activation** (`AGENTS.md` — ingest steps, **Ingest activation rule**, Evidence summary guidance for high-value source-notes).
3. Run `scripts/validate_wiki.py` before commit. **Structural** pass ≠ **integration** complete—confirm hubs/canonical pages were updated when the batch affects execution (see `docs/operations/validation.md`).
4. Append `wiki/log.md` for substantive work.

## Pull requests

- Keep diffs scoped; prefer incremental updates over full rewrites.
- CI must pass: tests, validator, MkDocs strict build.
