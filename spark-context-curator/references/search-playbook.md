# Search Playbook

Use local-only search. Do not browse the web for codebase facts.

## 1) Fast Skeleton

```bash
rg --files
rg --files | rg "src|app|api|service|handler|model|test"
find . -maxdepth 3 -type d | head -n 200
```

## 2) Lexical Probes (`rg`)

```bash
# Entry points and handlers
rg -n "main\\(|if __name__ ==|router|route|endpoint|handler|command"

# Data and domain concepts
rg -n "class .*Service|Repository|Model|Schema|DTO|Entity"

# Configuration and wiring
rg -n "ENV|config|settings|dependency|inject|container"

# Narrow by type and path
rg -n --glob "*.py" "async def|def .*\\("
rg -n --glob "*.{ts,tsx,js}" "export function|class |router|controller"
```

## 3) Semantic Probes (`colgrep`)

Use semantic search for intent-level discovery.

```bash
# Generic semantic search
colgrep -k 10 "where request validation happens" .

# Hybrid mode: lexical pre-filter + semantic ranking
colgrep -e "handler|controller|endpoint" -k 10 "authentication flow" .

# File-level shortlist only
colgrep -l -k 15 "business rules for billing" .

# Check index status
colgrep status
```

Notes:
- First semantic search may build/update an index.
- If `colgrep` fails due to permissions/indexing, fall back to `rg` immediately.

## 4) History and Ownership

```bash
git log --oneline -- path/to/file
git blame -L 1,120 path/to/file
git show <commit> -- path/to/file
```

## 5) Context Curation Heuristics

- Prefer 8-15 high-signal files over broad dumps.
- Link every claim to file evidence.
- Keep uncertain areas explicit under "Unknowns".
- End with next read-only probes, not code edits.
