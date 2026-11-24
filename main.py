#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler arriving from 1800, to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

SENTENCE = (
    "Picture one road joining every post office, library, and market on "
    "earth, so a letter crosses the world in a blink and any question "
    "finds its answer among them at once."
)


def main() -> None:
    text = SENTENCE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
