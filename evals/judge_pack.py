#!/usr/bin/env python3
"""Build a blind judge pack from saved answers, so a judge cannot tell which run wrote which.

Usage: python3 evals/judge_pack.py SET_DIR OUT_DIR LABEL=RUN_DIR [LABEL=RUN_DIR ...] [--seed N]

SET_DIR holds cases.json and inputs/. Each RUN_DIR holds one answer file per
case, named with the case id. LABEL names the run, for example old or
new. The script writes two files to OUT_DIR:

  judge-pack.md   each case with its text, must and must-not lists, and the
                  answers under neutral letters (A, B, ...), shuffled per case
  judge-map.json  which letter was which run, for scoring afterwards

Give only judge-pack.md to the judge. Score the judge's lines with score.py.
Standard library only.
"""

import glob
import json
import os
import random
import string
import sys

PACK_INTRO = (
    "# Judge pack\n\n"
    "Each case has several answers under letters. Score each answer against that case's "
    "Must and Must not lists, reading the answer text itself. An answer passes only if "
    "every Must is met and no Must not is hit. A check-only answer must end with exactly "
    "one closing sentence. Write one line per answer: case id, letter, PASS or FAIL, and "
    "for FAIL the one reason.\n"
)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_answer(run_dir, case_id):
    matches = sorted(glob.glob(os.path.join(run_dir, case_id + "*")))
    return read(matches[0]) if matches else None


def build(set_dir, runs, seed):
    """Return (pack_text, mapping). mapping[case_id][letter] = run label."""
    rng = random.Random(seed)
    cases = json.loads(read(os.path.join(set_dir, "cases.json")))
    parts = [PACK_INTRO]
    mapping = {}
    for case in cases:
        answers = [(label, load_answer(run_dir, case["id"])) for label, run_dir in runs]
        answers = [(label, text) for label, text in answers if text is not None]
        rng.shuffle(answers)
        mapping[case["id"]] = {}
        text = read(os.path.join(set_dir, case["input"]))
        parts.append(
            "## %s\nRequest: %s\n\nText:\n<<<\n%s\n>>>\n\nMust:\n%s\n\nMust not:\n%s\n"
            % (
                case["id"],
                case["request"],
                text.rstrip("\n"),
                "\n".join("- " + m for m in case["must"]),
                "\n".join("- " + m for m in case["must_not"]),
            )
        )
        for letter, (label, answer) in zip(string.ascii_uppercase, answers):
            mapping[case["id"]][letter] = label
            parts.append("### Answer %s\n<<<\n%s\n>>>\n" % (letter, answer.rstrip("\n")))
    return "\n".join(parts), mapping


def main(argv):
    seed = 1
    args = []
    i = 1
    while i < len(argv):
        if argv[i] == "--seed" and i + 1 < len(argv):
            seed = int(argv[i + 1])
            i += 2
        else:
            args.append(argv[i])
            i += 1
    if len(args) < 3 or any("=" not in a for a in args[2:]):
        print(__doc__)
        return 2
    set_dir, out_dir = args[0], args[1]
    runs = [tuple(a.split("=", 1)) for a in args[2:]]
    pack, mapping = build(set_dir, runs, seed)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "judge-pack.md"), "w", encoding="utf-8") as f:
        f.write(pack)
    with open(os.path.join(out_dir, "judge-map.json"), "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=1)
    print("wrote judge-pack.md and judge-map.json for %d cases" % len(mapping))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
