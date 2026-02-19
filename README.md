# Skills

Some skills I use with Claude Code and Codex.

Install with [skills](https://skills.sh/) by Vercel using `bunx` (or `npx`).

<!-- SKILLS_TABLE_START -->
| Skill | Description | Install Command |
|-------|-------------|-----------------|
| [codebase-librarian](codebase-librarian) | Create a comprehensive inventory of a codebase. Map structure, entry points, services, infrastructure, domain models, and data flows. Pure documentation—no opinions or recommendations. | `bunx skills add baggiponte/skills --skill "codebase-librarian"` |
<!-- SKILLS_TABLE_END -->

## Installation

Here are the skills I pre-installed with [skills](https://skills.sh/):

Global skills:

```sh
bunx skills add vercel-labs/agent-browser --skill="agent-browser" --global --agent=claude-code --agent=codex
bunx skills add https://github.com/intellectronica/agent-skills --skill="context7" --global --agent=claude-code --agent=codex
bunx skills add https://github.com/softaworks/agent-toolkit --skill="commit-work" --global --agent=claude-code --agent=codex
```

Local skills:

```sh
bunx skills add anthropics/skills --skill="skill-creator" --agent=claude-code
bunx skills add openai/skills --skill="skill-creator" --agent=codex
```

Note: skills are installed under `~/.agents/skills`. Currently, `skills` symlinks to the various agent global/project folders. In other words, for claude code they end up in `~/.claude/skills`, while for codex they end up in `~/.codex/skills`.
