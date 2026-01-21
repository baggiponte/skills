# Skills

Some skills I use with Claude Code and Codex.

Install with [skills](https://skills.sh/) by Vercel using `bunx` (or `npx`).

<!-- SKILLS_TABLE_START -->
| Skill | Description | Install Command |
|-------|-------------|-----------------|
| [architecture-design-critique](architecture-design-critique) | Perform a codebase-wide architectural review through a Ports & Adapters (hexagonal architecture) lens. Assess boundary violations, coupling issues, and dependency direction. Produces a prioritized improvement roadmap. | `bunx skills add baggiponte/skills --skill "architecture-design-critique"` |
| [code-refactor](code-refactor) | Systematic refactoring of codebase components through a structured 3-phase process. Use when asked to refactor, restructure, or improve specific components, modules, or areas of code. Produces research documentation, change proposals with code samples, and test plans. Triggers on requests like "refactor the authentication module", "restructure the data layer", "improve the API handlers", or "clean up the payment service". | `bunx skills add baggiponte/skills --skill "code-refactor"` |
| [codebase-librarian](codebase-librarian) | Create a comprehensive inventory of a codebase. Map structure, entry points, services, infrastructure, domain models, and data flows. Pure documentation—no opinions or recommendations. | `bunx skills add baggiponte/skills --skill "codebase-librarian"` |
| [gh-fix-ci](gh-fix-ci) | Inspect GitHub PR checks with gh, pull failing GitHub Actions logs, summarize failure context, then create a fix plan and implement after user approval. Use when a user asks to debug or fix failing PR CI/CD checks on GitHub Actions and wants a plan + code changes; for external checks (e.g., Buildkite), only report the details URL and mark them out of scope. | `bunx skills add baggiponte/skills --skill "gh-fix-ci"` |
<!-- SKILLS_TABLE_END -->

## Credits

The `gh-fix-ci` skill is a copy of the one in the OpenAI repo.
