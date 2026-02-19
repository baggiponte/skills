---
name: spark-context-curator
description: "Ultra-fast, read-only codebase exploration and context curation for GPT-5.3 Codex Spark. Use when you need deep repository understanding without modifying anything: architecture mapping, flow tracing, ownership discovery, incident/code-review prep, or implementation planning. Triggers on requests like \"explore this codebase\", \"curate context\", \"map where X happens\", \"investigate before editing\", or \"read-only deep dive\"."
---

# Spark Context Curator

Delegate exploration to an isolated Codex subprocess instead of doing a long in-session analysis. This keeps the caller's context window clean.

## Primary Command

Run the wrapper script:

```bash
scripts/run-spark-curator.sh "Map authentication flow and key files" -C .
```

Other forms:

```bash
# Read objective from file
scripts/run-spark-curator.sh -f /tmp/objective.md -C /path/to/repo

# Write the final assistant message to a file
scripts/run-spark-curator.sh "Trace billing data flow" -C . -o /tmp/curation.md
```

## What The Wrapper Enforces

The wrapper launches:

- `codex exec`
- `--model gpt-5.3-codex-spark`
- `--sandbox read-only`
- `--ephemeral`
- `--cd <target directory>`

It injects the dedicated prompt in `references/system-prompt.md` plus your objective.

Note: Codex CLI does not expose a separate `--system-prompt` flag in current `codex exec --help`; this skill uses a clear prompt envelope from file to simulate a stable system layer.

## Read-Only Scope

The delegated run is context curation only:

- No file edits
- No git mutations
- Local repository search only (`rg`, `git grep`, `git log/show/blame`, `colgrep`)
- Explicit uncertainty and next probes

## Fallback

If `codex` is unavailable, run manual read-only exploration using `references/search-playbook.md`.
