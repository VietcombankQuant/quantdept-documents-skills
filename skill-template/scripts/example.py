#!/usr/bin/env python3
"""Example helper script for a skill.

Keep real logic in scripts like this and have SKILL.md instruct the agent to
run them, rather than pasting large code blocks into the skill instructions.

Usage:
    python scripts/example.py INPUT [--option VALUE]
"""

import argparse
import sys


def run(text: str) -> str:
    """Replace with the skill's actual work."""
    return text.strip().upper()


def main() -> int:
    parser = argparse.ArgumentParser(description="Example skill helper.")
    parser.add_argument("input", help="Input to process.")
    args = parser.parse_args()

    print(run(args.input))
    return 0


if __name__ == "__main__":
    sys.exit(main())
