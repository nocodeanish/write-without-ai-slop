#!/usr/bin/env python3
"""Deterministic checks for write-without-ai-slop.

Usage:
    python3 check_text.py ORIGINAL OUTPUT [--allow-dashes]

Compares an original text with a rewritten one. Standard library only.
The model still judges voice and new claims. This script only checks what a
machine can check exactly:

  numbers   every number in OUTPUT is also in ORIGINAL
  urls      every URL in OUTPUT is also in ORIGINAL
  code      every fenced code block in ORIGINAL appears unchanged in OUTPUT
  quotes    every double-quoted passage of 3+ words in ORIGINAL appears in OUTPUT
  ids       every ticket ID (ABC-123), @mention and branch name (fix/name) in ORIGINAL appears in OUTPUT
  dashes    no paragraph in OUTPUT has more than one em or en dash
  leftovers no chatbot leftover phrase appears in OUTPUT
  residue   no tool residue such as utm_source=chatgpt.com in OUTPUT

Exit code 0 means no findings. 1 means findings. 2 means bad usage.
The em and en dash characters are built from code points so this file stays
free of the characters it checks for.
"""

import re
import sys

EM_DASH = chr(0x2014)
EN_DASH = chr(0x2013)

NUMBER = re.compile(r"\d[\d,.]*%?")
URL = re.compile(r"https?://[^\s)\]>\"']+")
FENCE = re.compile(r"```.*?```", re.DOTALL)
QUOTE = re.compile(r"[\"“]([^\"”]{12,}?)[\"”]")
TICKET_ID = re.compile(r"\b[A-Z][A-Z0-9]+-\d+\b")
MENTION = re.compile(r"(?<![\w.])@[A-Za-z][\w-]*")
BRANCH = re.compile(r"\b(?:fix|feature|feat|chore|hotfix|bugfix|release)/[\w./-]+")

LEFTOVERS = [
    "certainly!",
    "great question",
    "i hope this helps",
    "hope this helps",
    "as an ai language model",
    "as an ai,",
    "as of my last update",
    "as of my knowledge cutoff",
]
RESIDUE = ["utm_source=chatgpt.com", "utm_source=openai", "turn0search", "contentreference", "oaicite"]


def norm_url(url):
    """Drop utm_ tracking parameters, so removing them is not a new URL."""
    url = re.sub(r"[?&]utm_[^&\s]*", "", url)
    return url.rstrip(".,;")


def norm_numbers(text):
    """Return the set of numbers with trailing punctuation removed."""
    return {n.rstrip(".,") for n in NUMBER.findall(text)}


def check(original, output, allow_dashes=False, quote_source=None):
    """quote_source: text whose quotes must survive. Defaults to original.
    Use it when original also holds request text that need not be repeated.
    Plain markers such as "[your name]" are allowed: the skill asks for them."""
    findings = []

    new_numbers = norm_numbers(output) - norm_numbers(original)
    if new_numbers:
        findings.append("numbers: not in original: " + ", ".join(sorted(new_numbers)))

    new_urls = {norm_url(u) for u in URL.findall(output)} - {norm_url(u) for u in URL.findall(original)}
    if new_urls:
        findings.append("urls: not in original: " + ", ".join(sorted(new_urls)))

    for block in FENCE.findall(original):
        if block not in output:
            findings.append("code: a fenced block from the original changed or is missing")

    for quote in QUOTE.findall(original if quote_source is None else quote_source):
        if len(quote.split()) >= 3 and quote not in output:
            findings.append("quotes: changed or missing: " + quote[:60])

    # A ticket ID inside a branch name does not count as a standalone ID.
    plain_original = BRANCH.sub(" ", original)
    plain_output = BRANCH.sub(" ", output)
    for pattern, src, out in (
        (TICKET_ID, plain_original, plain_output),
        (MENTION, original, output),
        (BRANCH, original, output),
    ):
        lost = set(pattern.findall(src)) - set(pattern.findall(out))
        if lost:
            findings.append("ids: changed or missing: " + ", ".join(sorted(lost)))

    if not allow_dashes:
        for i, paragraph in enumerate(re.split(r"\n\s*\n", output), start=1):
            count = paragraph.count(EM_DASH) + paragraph.count(EN_DASH)
            if count > 1:
                findings.append("dashes: paragraph %d has %d long dashes" % (i, count))

    lower = output.lower()
    for phrase in LEFTOVERS:
        if phrase in lower and phrase not in original.lower():
            findings.append("leftovers: " + phrase)
    for marker in RESIDUE:
        if marker in lower:
            findings.append("residue: " + marker)

    return findings


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    allow_dashes = "--allow-dashes" in argv
    if len(args) != 2:
        print(__doc__)
        return 2
    try:
        with open(args[0], encoding="utf-8") as f:
            original = f.read()
        with open(args[1], encoding="utf-8") as f:
            output = f.read()
    except OSError as err:
        print("error: " + str(err))
        return 2
    findings = check(original, output, allow_dashes)
    for line in findings:
        print(line)
    if not findings:
        print("ok")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
