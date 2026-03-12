---
name: context7
description: Retrieve up-to-date documentation for software libraries, frameworks, and components via the Context7 CLI using `bunx ctx7`. Use this whenever you need current docs, API references, code examples, migration details, or verification for a library or framework instead of relying on training data. Triggers on requests like "look up the docs for X", "find the latest API for Y", "show me examples from the docs", "check the current React/Next.js/FastAPI docs", or "verify this library usage against current documentation".
---

# Context7

Use this skill to fetch current documentation through the Context7 CLI.

## Workflow

1. Resolve the library name to a Context7 library ID with `bunx ctx7 library`.
2. Pick the best match:
   - Prefer official docs and higher benchmark scores.
   - If the top result looks wrong, inspect the next few entries before choosing.
   - Use `--json` when you want to filter results with `jq`.
3. Fetch focused documentation with `bunx ctx7 docs <query>`.
4. Answer from the retrieved docs, not from stale memory.

## Commands

### Search for a library

Use readable output when browsing candidates:

```bash
bunx ctx7 library react hooks
```

Use JSON output when you want to inspect fields or filter with `jq`:

```bash
bunx ctx7 library react hooks --json
```

The JSON array includes fields such as:

- `id`: Context7 library ID to use with `bunx ctx7 docs`
- `title`: Human-readable library name
- `description`: Summary of the library or docs source
- `benchmarkScore`: Relevance/quality score
- `versions`: Available versions, when present

### Fetch documentation

Use the chosen library ID and a task-focused query:

```bash
bunx ctx7 docs /facebook/react "useEffect examples"
```

Use JSON output when you need structured snippets:

```bash
bunx ctx7 docs /facebook/react "useEffect examples" --json
```

The JSON response includes:

- `codeSnippets`: Code examples with titles, descriptions, languages, and code blocks
- `infoSnippets`: Explanatory text snippets for the topic

## Examples

### React hooks documentation

```bash
# Find likely React library IDs
bunx ctx7 library react hooks

# Fetch current docs and examples
bunx ctx7 docs /facebook/react "useEffect examples"
```

### Next.js routing documentation

```bash
# Search for the right Next.js docs source
bunx ctx7 library nextjs routing

# Fetch app router documentation
bunx ctx7 docs /vercel/next.js "app router"
```

### FastAPI dependency injection

```bash
# Search for FastAPI docs
bunx ctx7 library fastapi dependencies

# Fetch dependency injection guidance
bunx ctx7 docs /fastapi/fastapi "dependency injection"
```

## Tips

- Prefer `bunx ctx7 docs` default output when you want readable text in the terminal.
- Prefer `--json` when you need to pipe into `jq` or inspect fields precisely.
- Use specific queries such as `"server actions"`, `"dependency injection"`, or `"useEffect cleanup"` to improve relevance.
- If a library has multiple plausible entries, prefer official docs over mirrors or secondary sources.
- If the user cares about a specific version, check whether `versions` are listed in the search results and choose the matching library entry.
