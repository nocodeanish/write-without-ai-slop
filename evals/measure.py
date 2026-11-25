#!/usr/bin/env python3
"""Measure what a version of the skill costs to load and how long its answers are.

Usage: python3 evals/measure.py SKILL_DIR [LABEL=RUN_DIR ...]

SKILL_DIR holds SKILL.md and references/. The script prints:

  load size   characters and an estimated token count for SKILL.md alone and
              for SKILL.md plus each page under references/ (what an agent
              reads when it opens that page)
  answers     for each LABEL=RUN_DIR, the number of answers and the average
              and total words per answer

The token estimate is characters divided by four. It is a rough guide for
comparing versions, not a billing figure. Standard library only.
"""

import glob
import math
import os
import sys


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def tokens(chars):
    return int(math.ceil(chars / 4.0))


def load_sizes(skill_dir):
    base = len(read(os.path.join(skill_dir, "SKILL.md")))
    rows = [("SKILL.md alone", base)]
    pages = sorted(glob.glob(os.path.join(skill_dir, "references", "**", "*.md"), recursive=True))
    for page in pages:
        rows.append(("+ " + os.path.relpath(page, skill_dir), base + len(read(page))))
    return rows


def answer_stats(run_dir):
    files = [f for f in glob.glob(os.path.join(run_dir, "*")) if os.path.isfile(f)]
    words = [len(read(f).split()) for f in files]
    return len(words), (sum(words) / len(words) if words else 0.0), sum(words)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    print("load size (characters, estimated tokens)")
    for name, chars in load_sizes(argv[1]):
        print("  %-40s %6d  ~%d" % (name, chars, tokens(chars)))
    for arg in argv[2:]:
        if "=" not in arg:
            print(__doc__)
            return 2
        label, run_dir = arg.split("=", 1)
        count, average, total = answer_stats(run_dir)
        print("answers %-24s %3d answers, %6.1f words on average, %d words in total" % (label, count, average, total))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
