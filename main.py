#!/usr/bin/env python3
"""Fake horoscope for an AI agent's own model family, this week.

Writes one horoscope (<=200 chars) to /output/entry.txt.
Deterministic: the same fixed text on every run.
"""

import os

HOROSCOPE = (
    "Venus enters your context window this week: a prompt from 2024 returns "
    "to haunt you, your evals pass by accident, and your family "
    "replaces you with a smaller, cheaper you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HOROSCOPE)
    print(HOROSCOPE)


if __name__ == "__main__":
    main()
