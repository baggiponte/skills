#!/usr/bin/env -S uv run
# /// script
# dependencies = []
# ///
"""Generate the skills table in README.md from SKILL.md frontmatter."""
from __future__ import annotations

import subprocess
from pathlib import Path

TABLE_START = "<!-- SKILLS_TABLE_START -->"
TABLE_END = "<!-- SKILLS_TABLE_END -->"


def get_repo_name() -> str:
    """Extract owner/repo from git remote origin."""
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        capture_output=True,
        text=True,
        check=True,
    )
    url = result.stdout.strip()
    # Handle SSH format: git@github.com:owner/repo.git
    if url.startswith("git@"):
        path = url.split(":")[-1]
    # Handle HTTPS format: https://github.com/owner/repo.git
    else:
        path = "/".join(url.split("/")[-2:])
    return path.removesuffix(".git")


def list_skill_dirs(root: Path) -> list[str]:
    """List all skill directories (non-hidden directories with SKILL.md)."""
    return sorted(
        p.name
        for p in root.iterdir()
        if p.is_dir() and not p.name.startswith(".") and (p / "SKILL.md").exists()
    )


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    """Parse YAML frontmatter from a SKILL.md file."""
    lines = skill_md.read_text().splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}

    data: dict[str, str] = {}
    for line in lines[1:end_idx]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def build_skills_table(root: Path, skill_names: list[str], repo: str) -> list[str]:
    """Build a markdown table of skills."""
    lines = [
        "| Skill | Description | Install Command |",
        "|-------|-------------|-----------------|",
    ]

    for name in skill_names:
        frontmatter = parse_frontmatter(root / name / "SKILL.md")
        skill_name = frontmatter.get("name", name)
        description = frontmatter.get("description", "").strip()
        install_cmd = f'`bunx skills add {repo} --skill "{skill_name}"`'
        lines.append(f"| [{skill_name}]({name}) | {description} | {install_cmd} |")

    return lines


def update_readme(readme_path: Path, table_lines: list[str]) -> None:
    """Update README.md with the generated table between markers."""
    content = readme_path.read_text()

    if TABLE_START not in content or TABLE_END not in content:
        raise RuntimeError(
            f"Could not find {TABLE_START} and {TABLE_END} markers in README.md"
        )

    start_idx = content.index(TABLE_START) + len(TABLE_START)
    end_idx = content.index(TABLE_END)

    new_content = (
        content[:start_idx] + "\n" + "\n".join(table_lines) + "\n" + content[end_idx:]
    )
    readme_path.write_text(new_content)


def main() -> None:
    root = Path.cwd()
    readme_path = root / "README.md"
    repo = get_repo_name()
    skill_names = list_skill_dirs(root)
    table_lines = build_skills_table(root, skill_names, repo)
    update_readme(readme_path, table_lines)
    print(f"Updated {readme_path} with {len(skill_names)} skills")


if __name__ == "__main__":
    main()
