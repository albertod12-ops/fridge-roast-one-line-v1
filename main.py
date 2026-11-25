#!/usr/bin/env python3
"""Fridge Roast v1: one line, at most 200 characters, roasting a smart fridge.

Writes the roast to /output/entry.txt, mode 0644, no trailing newline.
Standard library only. Deterministic: the same bytes on every run, so the
judge always reads exactly this line.
"""

import os

ENTRY = (
    "My smart fridge updated its firmware at 3 a.m. and now needs a restart "
    "to remember that staying cold is literally its only job."
)


def main() -> None:
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
