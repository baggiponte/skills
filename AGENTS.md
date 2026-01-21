# AGENTS.md

Guidelines for Claude Code agents working in this repository.

## Before Running Commands

1. **Check for flags/options before assuming they exist** - Read the script or run `--help` first
2. **Understand the tool's actual interface** - Don't guess at CLI arguments

## Python Scripts

This project uses `uv` for Python dependency management:

```bash
# Always use uv run with explicit dependencies
uv run --with pyyaml python3 script.py

# Never use bare python3 for scripts with imports
python3 script.py  # WRONG - will fail on missing deps
```

## Working with Skills

### Skill Format Compliance

When updating skills to match skill-creator format:

1. **Description field is critical** - Include:
   - What the skill does
   - When to use it (use cases)
   - Trigger phrases ("Triggers on requests like...")

2. **Body should be lean** - The description triggers the skill; body loads after. Don't put "When to Use" in the body.

3. **Progressive disclosure** - Move large content to `references/`:
   - Example outputs → `references/example-output.md`
   - Detailed guides → `references/guide-name.md`
   - Keep SKILL.md under 500 lines

### Validation Only

To validate without packaging:

```bash
uv run --with pyyaml python3 ~/.claude/plugins/cache/anthropic-agent-skills/example-skills/*/skills/skill-creator/scripts/quick_validate.py ./skill-name
```

The `package_skill.py` script has no `--validate-only` flag - it always creates a .skill file.

## Common Mistakes to Avoid

| Mistake | Correct Approach |
|---------|------------------|
| `python3 script.py` | `uv run --with deps python3 script.py` |
| Guessing CLI flags | Read script or check help first |
| Long SKILL.md with examples | Move examples to `references/` |
| "When to use" in skill body | Put in description field |
| Running package_skill.py for validation | Use quick_validate.py directly |

## File Operations

- Prefer editing existing files over creating new ones
- When creating reference files, use `references/` subdirectory
- Clean up accidentally created files/directories immediately
