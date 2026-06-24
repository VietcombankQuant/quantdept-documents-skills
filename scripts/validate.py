#!/usr/bin/env python3
"""Validate a SKILL.md file against the basic Agent Skills conventions.

Checks:
  - SKILL.md exists and has a YAML frontmatter block.
  - `name` is present, lowercase-hyphen, <= 64 chars, and matches the folder.
  - `description` is present and <= 1024 chars.

Usage:
    python scripts/validate.py [path/to/skill-dir]   # defaults to parent dir
"""

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        raise ValueError("SKILL.md must start with a '---' frontmatter block.")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Frontmatter block is not closed with '---'.")
    fields: dict[str, str] = {}
    key = None
    buf: list[str] = []
    for line in parts[1].splitlines():
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if m and not line.startswith(" "):
            if key:
                fields[key] = " ".join(buf).strip()
            key, val = m.group(1), m.group(2).strip()
            buf = [val.lstrip(">|").strip()] if val else []
        elif key:
            buf.append(line.strip())
    if key:
        fields[key] = " ".join(buf).strip()
    return fields


def main() -> int:
    skill_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    skill_md = skill_dir / "SKILL.md"

    errors: list[str] = []
    if not skill_md.exists():
        print(f"FAIL: no SKILL.md in {skill_dir}")
        return 1

    try:
        fields = parse_frontmatter(skill_md.read_text())
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    name = fields.get("name", "")
    desc = fields.get("description", "")

    if not name:
        errors.append("missing `name`")
    else:
        if not NAME_RE.match(name):
            errors.append("`name` must be lowercase letters/digits/hyphens")
        if len(name) > 64:
            errors.append("`name` exceeds 64 characters")
        if name != skill_dir.name and skill_dir.name != "skill-template":
            errors.append(f"`name` ({name}) should match folder ({skill_dir.name})")

    if not desc:
        errors.append("missing `description`")
    elif len(desc) > 1024:
        errors.append("`description` exceeds 1024 characters")

    if errors:
        print("FAIL:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {name} — {len(desc)} char description")
    return 0


if __name__ == "__main__":
    sys.exit(main())
