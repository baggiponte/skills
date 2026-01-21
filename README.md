# Skills

Some skills I use with Claude Code and Codex.

## List

```
architecture-design-critique
codebase-librarian
gh-fix-ci
```

- `architecture-design-critique`: Perform a codebase-wide architectural review through a Ports & Adapters (hexagonal architecture) lens. Assess boundary violations, coupling issues, and dependency direction. Produces a prioritized improvement roadmap.
- `codebase-librarian`: Create a comprehensive inventory of a codebase. Map structure, entry points, services, infrastructure, domain models, and data flows. Pure documentation—no opinions or recommendations.
- `gh-fix-ci`: Inspect GitHub PR checks with gh, pull failing GitHub Actions logs, summarize failure context, then create a fix plan and implement after user approval. Use when a user asks to debug or fix failing PR CI/CD checks on GitHub Actions and wants a plan + code changes; for external checks (e.g., Buildkite), only report the details URL and mark them out of scope.

## Installation

Install instructions (docs: [Claude Code Skills](https://code.claude.com/docs/en/skills), [OpenAI Codex Skills](https://developers.openai.com/codex/skills/)):

```bash
mkdir -p ~/.claude/skills
ln -sfn "$PWD/architecture-design-critique" ~/.claude/skills/architecture-design-critique
ln -sfn "$PWD/codebase-librarian" ~/.claude/skills/codebase-librarian
ln -sfn "$PWD/gh-fix-ci" ~/.claude/skills/gh-fix-ci

mkdir -p ~/.codex/skills
ln -sfn "$PWD/architecture-design-critique" ~/.codex/skills/architecture-design-critique
ln -sfn "$PWD/codebase-librarian" ~/.codex/skills/codebase-librarian
ln -sfn "$PWD/gh-fix-ci" ~/.codex/skills/gh-fix-ci
```

```bash
mkdir -p .claude/skills
ln -sfn "$PWD/architecture-design-critique" .claude/skills/architecture-design-critique
ln -sfn "$PWD/codebase-librarian" .claude/skills/codebase-librarian
ln -sfn "$PWD/gh-fix-ci" .claude/skills/gh-fix-ci

mkdir -p .codex/skills
ln -sfn "$PWD/architecture-design-critique" .codex/skills/architecture-design-critique
ln -sfn "$PWD/codebase-librarian" .codex/skills/codebase-librarian
ln -sfn "$PWD/gh-fix-ci" .codex/skills/gh-fix-ci
```

## Justfile

This repo includes a `Justfile` with recipes to create the symlinks above. `just` is a small command runner (docs: [just.systems](https://just.systems)). If you manage dependencies with uv, add it as a dev dependency and note that uv is required for the script:

```bash
uv add --dev -- just
```

```bash
just link
just link-local
```

## Credits

The `gh-fix-ci` skill is a copy of the one in the OpenAI repo.
