# Skill Template

A scaffold for building a new Agent Skill for Claude (and other agents that
support the Skills format). Copy this folder, rename it, and fill in the files.

## Quick start

1. Copy the template into your skills directory and rename it:
   ```bash
   cp -r skill-template ../my-skill-name
   ```
2. Edit `SKILL.md`:
   - Set `name` to match the folder name (lowercase, hyphens, ≤ 64 chars).
   - Write a `description` that says **what** the skill does and **when** to use
     it, in the third person. This is the only text the agent reads when
     deciding to invoke the skill, so make the triggers explicit.
3. Replace the body of `SKILL.md` with your real instructions.
4. Add any helper code to `scripts/`, deep docs to `references/`, and templates
   or boilerplate to `assets/`. Delete folders you don't use.
5. Validate with `scripts/validate.py` (or your own check).

## Folder layout

```
skill-template/
├── SKILL.md            # Required. Frontmatter (name + description) + instructions.
├── README.md           # This file — notes for the skill author, not the agent.
├── scripts/            # Executable helpers the skill calls (keep code out of SKILL.md).
│   └── example.py
├── references/         # Detailed docs loaded on demand (progressive disclosure).
│   └── reference.md
└── assets/             # Templates, boilerplate, fonts, output stubs.
    └── .gitkeep
```

## Design principles

- **Progressive disclosure.** `SKILL.md` should stay short. Push detail into
  `references/` and link to it; the agent only reads what it needs.
- **Code lives in files, not prose.** Put scripts in `scripts/` and have the
  skill run them, instead of pasting large code blocks into `SKILL.md`.
- **The description does the routing.** A skill is only as useful as its
  `description` — load it with the words a user would actually say.
- **One skill, one job.** If a skill grows multiple unrelated jobs, split it.

## Naming rules (enforced by most loaders)

| Field         | Rule                                                        |
|---------------|-------------------------------------------------------------|
| Folder name   | lowercase letters, digits, hyphens                          |
| `name`        | matches folder name, ≤ 64 chars                             |
| `description` | ≤ 1024 chars, third person, includes when-to-use triggers   |
