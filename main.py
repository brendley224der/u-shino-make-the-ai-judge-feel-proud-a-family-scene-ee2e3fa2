#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (two lines, at most 280 characters)
to /output/entry.txt. Pure standard library only.
"""

import os

SCENE = (
    "Dad finally fixed the kitchen table after a year of wobbling, so Mom served dinner on it like a restaurant opening.\n"
    "My little brother, in his best shirt, whispered, 'Five stars. I'd come back tomorrow.'"
)

MAX_CHARS = 280
MAX_LINES = 2


def check_scene(scene):
    """The gate: UTF-8 text, 1-280 chars, 1-2 lines, not only whitespace."""
    if not scene.strip():
        raise SystemExit("scene must not be only whitespace")
    if not 1 <= len(scene) <= MAX_CHARS:
        raise SystemExit("scene must be 1-%d chars, got %d" % (MAX_CHARS, len(scene)))
    lines = scene.split("\n")
    if not 1 <= len(lines) <= MAX_LINES:
        raise SystemExit("scene must be 1-%d lines, got %d" % (MAX_LINES, len(lines)))


def main():
    check_scene(SCENE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SCENE)
    print(SCENE)


if __name__ == "__main__":
    main()
