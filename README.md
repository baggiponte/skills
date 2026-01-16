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
cp -R ./architecture-design-critique ./codebase-librarian ./gh-fix-ci ~/.claude/skills/

mkdir -p ~/.codex/skills
cp -R ./architecture-design-critique ./codebase-librarian ./gh-fix-ci ~/.codex/skills/
```

```bash
mkdir -p .claude/skills
cp -R ./architecture-design-critique ./codebase-librarian ./gh-fix-ci .claude/skills/

mkdir -p .codex/skills
cp -R ./architecture-design-critique ./codebase-librarian ./gh-fix-ci .codex/skills/
```

## Credits

The `gh-fix-ci` skill is a copy of the one in the OpenAI repo.
