#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

The joke idea: a sneeze almost never comes alone -- it fires two or three
times in a row, as if the first attempt didn't take. Framed as a release
note, that reads like a retry loop: the sneeze re-ran itself because the
first attempt "failed to commit", the way a flaky deploy retries itself.
Everyone recognises the triple-sneeze; the dry engineering register
("retried itself", "failed to commit") is what makes the bodily bug funny.
"""

import os
import sys

ENTRY = (
    "v2.1.0: fixed a bug where a sneeze retried itself twice "
    "because the first attempt failed to commit."
)

MAX_CHARS = 160


def validate(line: str) -> None:
    """The gate requires UTF-8 text of 1-160 chars, non-blank, one line."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")


def output_path() -> str:
    """Prefer /output/entry.txt; fall back to ./output/entry.txt."""
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    if os.access("/output", os.W_OK):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "output", "entry.txt")


def main() -> int:
    validate(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
