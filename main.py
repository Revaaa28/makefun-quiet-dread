#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment (a single line of at most 140 characters
that approves a pull request while carrying quiet existential dread)
to /output/entry.txt.

The entry is a fixed, deterministic string: no input, no network, no
randomness, so every run produces byte-identical output. The gate the
bounty checks (UTF-8, 1-140 chars, single line, not whitespace-only)
is re-checked here before writing, so a bad entry fails loudly instead
of shipping silently.
"""

from pathlib import Path

ENTRY = (
    "Approved. Whoever wrote this is gone, whatever it does is load-bearing, "
    "and my approval changes nothing either way."
)  # 115 characters, 1 line, no trailing newline

OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the bounty gate before anything is written."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 140:
        raise ValueError(f"entry is {len(text)} chars, over the 140-char limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # newline="" + no trailing "\n": exactly the chosen text, nothing else.
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
