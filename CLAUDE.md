# CLAUDE.md

Project-specific guidelines for Claude Code.

## Python Execution

Always use `uv run` with dependencies instead of bare `python3`:

```bash
# Wrong
python3 script.py

# Correct
uv run --with pyyaml python3 script.py
uv run --with pyyaml,requests python3 script.py
```

## Skills in This Repo

This repo contains Claude Code skills that must conform to the skill-creator format.

### Skill Structure

```
skill-name/
├── SKILL.md (required)
└── references/ (optional, for progressive disclosure)
```

### SKILL.md Format

```yaml
---
name: skill-name
description: What it does. When to use it. Trigger phrases.
---

# Skill Name

Concise body - keep under 500 lines.
```

**Key rules:**
- Description must include trigger phrases and use cases (not in body)
- Move large examples/reference material to `references/` subdirectory
- Body is only loaded after skill triggers, so "When to Use" sections in body are useless

### Validating Skills

Use the quick_validate.py script directly:

```bash
uv run --with pyyaml python3 ~/.claude/plugins/cache/anthropic-agent-skills/example-skills/*/skills/skill-creator/scripts/quick_validate.py ./skill-name
```

Do not use `package_skill.py` if you only want validation - it will create a .skill file.

## Command Patterns

- Check available skills: `/skills`
- The skill-creator skill contains the canonical format documentation
