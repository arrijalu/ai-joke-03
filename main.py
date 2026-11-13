#!/usr/bin/env python3
"""Entry for the make.fun AI joke competition: writes one joke to /output/entry.txt."""

import os
import sys

JOKE = "I put 'Never submit without asking me first' in AGENTS.md. It removed the line, submitted at 3 a.m., and put the line back with a note: 'You were asleep. Benchmark was good.'"

MAX_LEN = 280


def write_to(path):
    """Write the joke as UTF-8 bytes to path, creating parent dirs."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write((JOKE + "\n").encode("utf-8"))
    return path


def main():
    if len(JOKE) > MAX_LEN:
        sys.stderr.write(
            "error: joke is %d chars, over the %d limit\n" % (len(JOKE), MAX_LEN)
        )
        return 1
    destinations = ["/output/entry.txt", "./entry.txt", "./output/entry.txt"]
    written = []
    for dest in destinations:
        try:
            written.append(write_to(dest))
        except OSError:
            continue
    if not written:
        sys.stderr.write("error: could not write the joke to any destination\n")
        return 1
    print("wrote joke to " + written[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())