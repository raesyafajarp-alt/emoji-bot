#!/usr/bin/env python3
"""Your Agent in One Emoji — entry writer.

Writes exactly one emoji to /output/entry.txt: the compass.

Why the compass: give this agent a destination and it charts its own course there.
The compass says that in a single glance — direction and journey, no map handed over. It reads instantly at small size, it is specific to autonomous
wayfinding (not a generic robot or a smiley), and it is not the first
obvious pick half the field would send.
"""

import os

ENTRY = "\U0001f9ed"  # U+1F9ED COMPASS

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert len(ENTRY) == 1, "entry must be exactly one emoji"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
