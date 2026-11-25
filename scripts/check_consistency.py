#!/usr/bin/env python3
"""Repository consistency checks for write-without-ai-slop.

Usage:
    python3 scripts/check_consistency.py [REPO_ROOT]

Checks that the numbers and names stated in more than one file agree, so a
reader never finds two different versions or counts. Standard library only.
It never changes a file and makes no network calls.

Checks:
  1. Version: SKILL.md, the newest CHANGELOG entry and the evals README.
  2. Skill format: name, description length, SKILL.md length.
  3. Links: every relative Markdown link points to a file that exists, and
     every page in references/ is linked from SKILL.md.
  4. Test counts: the numbers in evals/README.md match the case files and
     the results table.
  5. README art: every image in README.md has alt text and exists, no art
     file is unused, the art stays small, and the install command in the demo
     matches the one in the README.

Exit code 0 when all checks pass, 1 when any fails, 2 on a usage error.
"""

import json
import re
import sys
from pathlib import Path

NAME = "write-without-ai-slop"
MAX_SKILL_LINES = 150  # CONTRIBUTING.md: SKILL.md stays under 150 lines
MAX_DESCRIPTION = 1024  # agentskills.io specification
MAX_NAME = 64
EVAL_SETS = ("evals", "evals/v2", "evals/v3", "evals/v4", "evals/v5", "evals/v6", "evals/v7")
TABLE_SETS = 4  # the results table covers the first four sets only
ART_DIR = ".github/readme"
MAX_ART_BYTES = 250_000  # the art is part of every clone and every install
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)|(?:src|href)=\"([^\"]+)\"")
IMG = re.compile(r"<img\b[^>]*>")
INSTALL = re.compile(r"npx skills add [\w./-]+")
SEMVER = r"\d+\.\d+\.\d+"


def read(root, relative):
    return (root / relative).read_text(encoding="utf-8")


def skill_fields(skill_text):
    """Return (name, description, version) from the SKILL.md front matter."""
    match = re.match(r"---\n(.*?)\n---\n", skill_text, re.S)
    if not match:
        return None, None, None
    front = match.group(1)
    name = re.search(r"^name:\s*(\S+)\s*$", front, re.M)
    description = re.search(r"^description:\s*(.+)$", front, re.M)
    version = re.search(r'^\s+version:\s*"?(' + SEMVER + r')"?\s*$', front, re.M)
    return (
        name.group(1) if name else None,
        description.group(1).strip() if description else None,
        version.group(1) if version else None,
    )


def check_versions(root):
    problems = []
    _, _, skill_version = skill_fields(read(root, "SKILL.md"))
    if not skill_version:
        return ["SKILL.md: no metadata version found"]
    heads = re.findall(r"^## (" + SEMVER + r")\b", read(root, "CHANGELOG.md"), re.M)
    if not heads:
        problems.append("CHANGELOG.md: no version heading found")
    elif heads[0] != skill_version:
        problems.append(
            f"CHANGELOG.md: newest entry is {heads[0]}, SKILL.md says {skill_version}"
        )
    results = re.search(r"^## Results on (\S+)", read(root, "evals/README.md"), re.M)
    if not results:
        problems.append("evals/README.md: no 'Results on VERSION' heading found")
    elif results.group(1) != skill_version:
        problems.append(
            f"evals/README.md: results are for {results.group(1)}, SKILL.md says {skill_version}"
        )
    return problems


def check_skill_format(root):
    problems = []
    text = read(root, "SKILL.md")
    name, description, _ = skill_fields(text)
    if name != NAME:
        problems.append(f"SKILL.md: name is {name!r}, expected {NAME!r}")
    if name and (len(name) > MAX_NAME or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name)):
        problems.append(f"SKILL.md: name {name!r} breaks the naming rules")
    if not description:
        problems.append("SKILL.md: description is missing")
    elif len(description) > MAX_DESCRIPTION:
        problems.append(
            f"SKILL.md: description is {len(description)} characters, limit {MAX_DESCRIPTION}"
        )
    lines = len(text.splitlines())
    if lines >= MAX_SKILL_LINES:
        problems.append(f"SKILL.md: {lines} lines, CONTRIBUTING.md says under {MAX_SKILL_LINES}")
    market = json.loads(read(root, ".claude-plugin/marketplace.json"))
    plugin_names = [p.get("name") for p in market.get("plugins", [])]
    if NAME not in plugin_names:
        problems.append(f".claude-plugin/marketplace.json: no plugin named {NAME}")
    return problems


def relative_links(text):
    """Yield link targets that point to files in the repository."""
    for markdown, attribute in LINK.findall(text):
        target = markdown or attribute
        if re.match(r"[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue  # web link, mailto or in-page anchor
        yield target.split("#", 1)[0]


def check_links(root):
    problems = []
    pages = ["README.md", "SKILL.md", "CONTRIBUTING.md", "CHANGELOG.md", "evals/README.md"]
    pages += [str(p.relative_to(root)) for p in (root / "docs").glob("*.md")]
    pages += [str(p.relative_to(root)) for p in (root / "examples").glob("*.md")]
    for page in pages:
        base = (root / page).parent
        for target in relative_links(read(root, page)):
            if target and not (base / target).exists():
                problems.append(f"{page}: link to {target} does not exist")
    skill_text = read(root, "SKILL.md")
    linked = {
        (root / t).resolve() for t in relative_links(skill_text) if (root / t).exists()
    }
    for page in sorted((root / "references").rglob("*.md")):
        if page.resolve() not in linked:
            problems.append(f"SKILL.md: does not link {page.relative_to(root)}")
    return problems


def check_eval_counts(root):
    problems = []
    readme = read(root, "evals/README.md")
    counts = []
    for folder in EVAL_SETS:
        cases = json.loads(read(root, f"{folder}/cases.json"))
        counts.append(len(cases))
        for case in cases:
            path = case.get("input")
            if path and not (root / folder / path).exists():
                problems.append(f"{folder}/cases.json: case {case['id']} input {path} is missing")
    total = sum(counts)
    table_total = sum(counts[:TABLE_SETS])
    stated = re.search(r"(\d+) invented test cases in (\w+) sets", readme)
    if not stated:
        problems.append("evals/README.md: no '<N> invented test cases in <N> sets' sentence")
    else:
        if int(stated.group(1)) != total:
            problems.append(f"evals/README.md: says {stated.group(1)} cases, files hold {total}")
    original = re.search(r"\((\d+) cases\)", readme)
    if original and int(original.group(1)) != counts[0]:
        problems.append(f"evals/README.md: says {original.group(1)} original cases, files hold {counts[0]}")
    each = re.search(r"\((\d+) each\)", readme)
    if each and any(int(each.group(1)) != n for n in counts[1:TABLE_SETS]):
        problems.append(f"evals/README.md: says {each.group(1)} each for later sets, files hold {counts[1:TABLE_SETS]}")
    header = re.search(r"Total of (\d+)", readme)
    if header and int(header.group(1)) != table_total:
        problems.append(f"evals/README.md: table header says {header.group(1)}, files hold {table_total}")
    rows = re.findall(r"^\| (?!Model|---)([^|]+)\|((?:\s*\d+\s*\|){5})\s*$", readme, re.M)
    for model, cells in rows:
        numbers = [int(n) for n in re.findall(r"\d+", cells)]
        if sum(numbers[:-1]) != numbers[-1]:
            problems.append(f"evals/README.md: {model.strip()} row does not add up")
    answers = re.search(r"all (\d+) answers", readme)
    if answers and rows and int(answers.group(1)) != table_total * len(rows):
        problems.append(
            f"evals/README.md: says {answers.group(1)} answers, {len(rows)} models x {table_total} cases = {table_total * len(rows)}"
        )
    return problems


def check_art(root):
    problems = []
    folder = root / ART_DIR
    files = sorted(folder.glob("*.svg")) if folder.is_dir() else []
    readme = read(root, "README.md")
    total = sum(f.stat().st_size for f in files)
    if total > MAX_ART_BYTES:
        problems.append(f"{ART_DIR}: art is {total} bytes, limit {MAX_ART_BYTES}")
    for tag in IMG.findall(readme):
        if not re.search(r'alt="[^"]+"', tag):
            problems.append(f"README.md: image without alt text: {tag[:70]}")
    for f in files:
        if f"{ART_DIR}/{f.name}" not in readme:
            problems.append(f"{ART_DIR}/{f.name}: not used in README.md")
        if "<title>" not in f.read_text(encoding="utf-8"):
            problems.append(f"{ART_DIR}/{f.name}: no <title> element")
    command = INSTALL.search(readme)
    demo = folder / "demo.svg"
    if command and demo.exists() and command.group(0) not in demo.read_text(encoding="utf-8"):
        problems.append(f"{ART_DIR}/demo.svg: install command differs from README ({command.group(0)})")
    return problems


CHECKS = (
    ("version", check_versions),
    ("skill format", check_skill_format),
    ("links", check_links),
    ("test counts", check_eval_counts),
    ("art", check_art),
)


def run(root):
    """Return a list of (check name, problem) pairs."""
    found = []
    for label, check in CHECKS:
        try:
            found.extend((label, p) for p in check(root))
        except (OSError, ValueError, KeyError) as error:
            found.append((label, f"could not run: {error}"))
    return found


def main(argv):
    if len(argv) > 2:
        print(__doc__)
        return 2
    root = Path(argv[1]) if len(argv) == 2 else Path(__file__).resolve().parent.parent
    if not (root / "SKILL.md").exists():
        print(f"No SKILL.md in {root}")
        return 2
    problems = run(root)
    for label, problem in problems:
        print(f"[{label}] {problem}")
    if problems:
        print(f"\n{len(problems)} problem(s).")
        return 1
    print(f"All {len(CHECKS)} checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
