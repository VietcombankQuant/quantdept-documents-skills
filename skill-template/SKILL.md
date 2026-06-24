---
name: skill-name-here
description: >-
  One or two sentences, written in the third person, that state WHAT this skill
  does and WHEN an agent should use it. Pack in concrete trigger words and
  synonyms the user is likely to say — this text is the only thing the agent
  sees when deciding whether to load the skill. Max 1024 characters.
# Optional fields below — delete any you don't need.
# license: MIT
# allowed-tools: Read, Grep, Glob, Bash
# metadata:
#   version: 0.1.0
#   author: your-name
---

# Skill Name Here

> Replace this whole file with your skill's real instructions. The guidance
> below is a checklist; keep the parts that apply and delete the rest.

## Overview

Briefly describe the capability in 1–3 sentences. What problem does it solve?
What is the end state after the skill runs successfully?

## When to use this skill

- Trigger condition 1 (e.g. "the user asks to convert a spreadsheet to ...").
- Trigger condition 2.
- When NOT to use it — point to the alternative skill or approach instead.

## Instructions

Write the steps the agent should follow. Be explicit and ordered. Prefer
imperative voice ("Read the file", "Run the script") over description.

1. **Step one.** What to do and how to verify it worked.
2. **Step two.** Reference a helper script with a relative path, e.g. run
   `scripts/example.py` rather than pasting a long program inline.
3. **Step three.** Note edge cases and how to handle failures.

## Resources

Use progressive disclosure — keep this file short and link out to detail that
is only needed sometimes. The agent loads these on demand.

- `references/reference.md` — deeper background, schemas, or API details.
- `scripts/example.py` — runnable helper; describe its inputs and outputs.
- `assets/` — templates, boilerplate, or output stubs the skill copies from.

## Examples

Show one concrete input → output. Examples teach the model the expected shape
of a good result far better than prose does.
