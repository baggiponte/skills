#!/usr/bin/env -S uv run
# /// script
# dependencies = []
# ///
from __future__ import annotations

from pathlib import Path


def list_skill_dirs(root: Path) -> list[str]:
    return sorted(
        [
            p.name
            for p in root.iterdir()
            if p.is_dir() and not p.name.startswith(".")
        ]
    )


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
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


def build_skill_descriptions(root: Path, skill_names: list[str]) -> list[str]:
    items: list[tuple[str, str]] = []
    for name in skill_names:
        frontmatter = parse_frontmatter(root / name / "SKILL.md")
        item_name = frontmatter.get("name", name)
        description = frontmatter.get("description", "").strip()
        if description:
            items.append((item_name, description))
        else:
            items.append((item_name, ""))

    return [
        f"- `{item_name}`: {description}".rstrip()
        for item_name, description in items
    ]


def update_readme(
    readme_path: Path,
    skill_names: list[str],
    skill_bullets: list[str],
) -> None:
    lines = readme_path.read_text().splitlines()

    try:
        list_idx = lines.index("## List")
    except ValueError as exc:
        raise RuntimeError("Could not find '## List' heading in README.md") from exc

    fence_start = None
    for i in range(list_idx + 1, len(lines)):
        if lines[i].strip().startswith("```"):
            fence_start = i
            break

    if fence_start is None:
        raise RuntimeError("Could not find opening code fence after '## List'")

    fence_end = None
    for i in range(fence_start + 1, len(lines)):
        if lines[i].strip().startswith("```"):
            fence_end = i
            break

    if fence_end is None:
        raise RuntimeError("Could not find closing code fence after '## List'")

    after_fence = fence_end + 1
    next_heading = None
    for i in range(after_fence, len(lines)):
        if lines[i].startswith("## "):
            next_heading = i
            break

    tail = lines[after_fence:] if next_heading is None else lines[next_heading:]
    updated = (
        lines[: fence_start + 1]
        + skill_names
        + lines[fence_end:fence_end + 1]
        + [""]
        + skill_bullets
        + tail
    )
    readme_path.write_text("\n".join(updated) + "\n")


def main() -> None:
    root = Path.cwd()
    readme_path = root / "README.md"
    skill_names = list_skill_dirs(root)
    skill_bullets = build_skill_descriptions(root, skill_names)
    update_readme(readme_path, skill_names, skill_bullets)


if __name__ == "__main__":
    main()
