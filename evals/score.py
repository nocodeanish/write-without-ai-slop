#!/usr/bin/env python3
"""Score a judge's verdicts against the hidden map from judge_pack.py.

Usage: python3 evals/score.py JUDGE_MAP VERDICTS [VERDICTS ...]

VERDICTS files hold one line per answer: case id, letter, PASS or FAIL, and
the reason for a FAIL. Give several files (one per judge) to get each judge's
totals and how often the judges agree. An answer counts as agreed when every
judge gave it the same verdict. Standard library only.
"""

import json
import sys
from collections import defaultdict


def parse(path):
    """Return {(case id, letter): (verdict, reason)}."""
    verdicts = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(None, 3)
            if len(parts) < 3:
                continue
            case_id, letter, verdict = parts[0], parts[1], parts[2].rstrip(":").upper()
            if verdict in ("PASS", "FAIL") and len(letter) == 1:
                verdicts[(case_id, letter)] = (verdict, parts[3] if len(parts) > 3 else "")
    return verdicts


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        mapping = json.load(f)
    judges = [parse(p) for p in argv[2:]]
    totals = [defaultdict(lambda: [0, 0]) for _ in judges]  # label -> [passes, answers]
    for n, verdicts in enumerate(judges):
        for (case_id, letter), (verdict, _) in verdicts.items():
            label = mapping.get(case_id, {}).get(letter)
            if label is None:
                continue
            totals[n][label][1] += 1
            totals[n][label][0] += verdict == "PASS"
    for n, path in enumerate(argv[2:]):
        print("judge %d (%s)" % (n + 1, path))
        for label, (passes, count) in sorted(totals[n].items()):
            print("  %-24s %d of %d" % (label, passes, count))
    if len(judges) > 1:
        keys = set.intersection(*(set(j) for j in judges))
        agreed = sum(len({j[k][0] for j in judges}) == 1 for k in keys)
        print("agreement: %d of %d answers judged by all" % (agreed, len(keys)))
        for k in sorted(keys):
            if len({j[k][0] for j in judges}) > 1:
                print("  disagree: %s %s (%s)" % (k[0], k[1], mapping[k[0]][k[1]]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
