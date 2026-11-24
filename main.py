"""The Dog Ate My Homework: Funniest Excuse: writes the entry text to /output/entry.txt.

Why this entry: Dog logic twist (name on it = mine), dog's voice with no embarrassment, no stock lines (no cat, no taste of paper, no good boy).
"""

import os

ENTRY = 'It had your name on it, and I have never seen you eat anything with your name on it, so I assumed it was mine.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
