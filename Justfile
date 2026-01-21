set shell := ["/bin/sh", "-eu", "-c"]

skill_dirs := "architecture-design-critique codebase-librarian gh-fix-ci"

link:
	mkdir -p ~/.claude/skills ~/.codex/skills
	for d in {{skill_dirs}}; do \
		ln -sfn "$PWD/$d" ~/.claude/skills/$d; \
		ln -sfn "$PWD/$d" ~/.codex/skills/$d; \
	done

link-local:
	mkdir -p .claude/skills .codex/skills
	for d in {{skill_dirs}}; do \
		ln -sfn "$PWD/$d" .claude/skills/$d; \
		ln -sfn "$PWD/$d" .codex/skills/$d; \
	done
