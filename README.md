# Skills

Some skills I use with Claude Code and Codex.

Install with [skills](https://skills.sh/) by Vercel using `bunx` (or `npx`).

<!-- SKILLS_TABLE_START -->
| Skill | Description | Install Command |
|-------|-------------|-----------------|
| [architecture-design-critique](architecture-design-critique) | Perform a codebase-wide architectural review through a Ports & Adapters (hexagonal architecture) lens. Assess boundary violations, coupling issues, and dependency direction. Produces a prioritized improvement roadmap. | `bunx skills add baggiponte/skills --skill "architecture-design-critique"` |
| [code-refactor](code-refactor) | Systematic refactoring of codebase components through a structured 3-phase process. Use when asked to refactor, restructure, or improve specific components, modules, or areas of code. Produces research documentation, change proposals with code samples, and test plans. Triggers on requests like "refactor the authentication module", "restructure the data layer", "improve the API handlers", or "clean up the payment service". | `bunx skills add baggiponte/skills --skill "code-refactor"` |
| [codebase-librarian](codebase-librarian) | Create a comprehensive inventory of a codebase. Map structure, entry points, services, infrastructure, domain models, and data flows. Pure documentation—no opinions or recommendations. | `bunx skills add baggiponte/skills --skill "codebase-librarian"` |
<!-- SKILLS_TABLE_END -->

## Installation

Here are the skills I pre-installed with [skills](https://skills.sh/):

```sh
bunx skills add anthropics/skills --skill="doc-coauthoring" --global --agent=claude-code --agent=codex
bunx skills add vercel-labs/agent-browser --skill="agent-browser" --global --agent=claude-code --agent=codex
bunx skills add https://github.com/intellectronica/agent-skills --skill="context7" --global --agent=claude-code --agent=codex

bunx skills add anthropics/skills --skill="skill-creator" --global --agent=claude-code
bunx skills add openai/skills --skill="skill-creator,create-plan" --global --agent=codex
```
