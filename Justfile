link:
    #!/usr/bin/env bash
    mkdir -p ~/.claude/skills ~/.codex/skills
    skills=$(fd --type=directory --max-depth=1 --strip-cwd-prefix .)
    for d in $skills; do
      ln -sfn "$PWD/$d" "$HOME/.claude/skills/$d"
      ln -sfn "$PWD/$d" "$HOME/.codex/skills/$d"
    done
