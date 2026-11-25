#!/usr/bin/env python3
"""Show Your Working — entry program.

writes one line, a dog's excuse after being caught eating the homework,
to /output/entry.txt. Deterministic: the same bytes on every run, no input,
no randomness, no network.

The excuse: the homework said "show your working", so the dog showed it —
literally. The laugh is dog logic at its purest: a teacher's phrase taken
at face value, then the digestion punchline lands it. The dog believes it has done
nothing wrong; it followed instructions. No cat, no taste of paper, no
"good boy" — the fresh angle is the dog as a diligent pupil.
"""

from pathlib import Path

ENTRY = (
    "It said 'show your working', so I did — it's inside me now. Ask again in an hour.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
