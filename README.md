# Skills

Some skills I use with Claude Code and Codex.

Install with [skills](https://skills.sh/) by Vercel using `bunx` (or `npx`).

<!-- SKILLS_TABLE_START -->
| Skill | Description | Install Command |
|-------|-------------|-----------------|
| [build-python-dockerfiles](build-python-dockerfiles) | Build production-ready Dockerfiles for Python projects that use uv. Use when creating or refactoring Dockerfiles for reproducible installs, cache-efficient builds, bytecode compilation, small runtime images, and non-root execution. Follows the production patterns from Hynek Schlawack's article "Production-ready Python Docker Containers with uv" while staying flexible about base images and app type. Supports packaged and unpackaged applications, including web apps, workers, and CLI services. Triggers on requests like "write a Dockerfile for this Python project", "optimize this uv Dockerfile", "containerize this FastAPI/Django/Flask app", "containerize this worker", or "split this into build and runtime stages". | `bunx skills add baggiponte/skills --skill "build-python-dockerfiles"` |
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
