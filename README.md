<h1 align="center"><img src=".github/readme/hero.svg" alt="no-ai-slop. A pixel-art editor in a red beret runs along ruled paper and stomps green slop blobs with a red pen. The editor collects two coins, 42 and 9, instead of striking them, and reaches a green finish flag. A scoreboard counts four blobs struck and two coins kept." width="100%"></h1>

<p align="center"><b>Stop your AI agent from writing like every other AI.</b></p>

<p align="center">
  <a href="#try-it-in-one-minute">Try it</a> ·
  <a href="#see-it-work">See it work</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#faq">FAQ</a> ·
  <a href="#what-it-catches">What it catches</a> ·
  <a href="#does-it-work">Results</a>
</p>

<p align="center">
  <a href="https://github.com/nocodeanish/write-without-ai-slop/actions/workflows/consistency.yml"><img src="https://github.com/nocodeanish/write-without-ai-slop/actions/workflows/consistency.yml/badge.svg" alt="Consistency check status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/nocodeanish/write-without-ai-slop" alt="License: MIT"></a>
  <a href="https://github.com/nocodeanish/write-without-ai-slop/releases"><img src="https://img.shields.io/github/v/release/nocodeanish/write-without-ai-slop" alt="Latest release"></a>
</p>

AI text looks, feels and reads the same, and readers notice. This skill lists what not to do, so your agent keeps its own voice, or yours. No setup, and it does not ask questions mid-task.

## Try it in one minute

<img src=".github/readme/tryit.svg" alt="Install, paste, see. A sleepy grey robot gets a skill cartridge labelled SKILL.md dropped into its head and wakes up blue with a red pen. It eats a sheet of paper covered in green slop blobs, the blobs fly out and burst, and it hands back a clean sheet with a green check." width="100%">

1. Install it. It is an agent skill, a folder with a SKILL.md file that agents read.

   ```
   npx skills add nocodeanish/write-without-ai-slop
   ```

2. Open your agent, then paste your last post under this line:

   ```
   Check this draft for AI patterns. Do not rewrite it.
   ```

3. Read the findings. If you like them, say `Rewrite it.` You get the smallest edit that removes the problems and a short list of what changed. It does not invent facts, numbers, quotes or names.

A Check answer looks like this, on an invented draft (more in [examples](examples/before-after.md)):

```
- "Experts agree that better tools lead to better results." Vague source. Name the expert and date, or cut the line.
- "Ready to unlock your team's potential?" List word in a closer with no next step. Replace with a concrete action.
```

## See it work

<img src=".github/readme/demo.svg" alt="A short draft on the left, marked up with a red pen: a setup before the point, a not-just-X contrast, a group of three and a bait question are struck through. On the right, the same draft after the edit, with the numbers 42 and 9 kept, shown as two gold coins and a green check." width="100%">

<sub>An illustration of the example below, not a recording. All examples are invented. More in [examples](examples/before-after.md).</sub>

<details>
<summary>The same example as text</summary>

Before:

```
Here's the thing: shipping fast isn't just about speed, it's about trust.

Last month our team cut the checkout bug backlog from 42 to 9 in two weeks. Not just a win for engineering, but a win for customers, for the business, and for the future.

Agree? What's your biggest lesson?
```

After:

```
Shipping fast builds trust.

Last month our team cut the checkout bug backlog from 42 to 9 in two weeks.
```

The numbers stayed. The setup line, the "not just X" contrast, the group of three and the bait question went.

</details>

The exact checks are a real script. This replay shows the real output of `scripts/check_text.py` on the same invented text: a rewrite that added a number and a chatbot leftover is flagged, and a clean rewrite passes. Rebuild it with `.github/readme/recording/record.js`.

<img src=".github/readme/check-text.gif" alt="A terminal replay. The command check_text.py compares a before text with a first rewrite and prints three findings: the number 12 is not in the original, and two chatbot leftovers. The second rewrite prints ok and exit 0." width="100%">

## Other ways to install

In Claude Code 2.1.275 or later:

```
/plugin install write-without-ai-slop --marketplace nocodeanish/write-without-ai-slop
```

Or copy the folder into your agent's skills folder. For example, in Claude Code:

```
cp -r write-without-ai-slop ~/.claude/skills/
```

## Update

Nothing updates an installed skill by itself. Compare the version in your `SKILL.md` with the one in this repository, and update the way you installed it:

- Installed with `npx skills add`: run `npx skills check`, then `npx skills update`.
- Copied the folder or cloned the repository: copy the folder again, or run `git pull`.
- Uploaded the zip in the Claude app: upload the new zip from the latest release.

The [changelog](CHANGELOG.md) says what changed in each version.

## FAQ

**Is it free?** Yes. It is MIT licensed. There is nothing to sign up for and no paid tier.

**Does my text leave my computer?** The skill is text files and one optional script, and it makes no network calls. Your agent still sends your text to its model, as it does for any request. The skill adds no other place for it to go.

**Does it work in my agent?** It is a standard agent skill. `npx skills add` installs it for Claude Code, Cursor, Codex, Cline and others.

**What can it not do?** It does not detect AI, teach a style or work well outside English. See [What it does not do](#what-it-does-not-do).

## How it works

<img src=".github/readme/robots.svg" alt="The three ways to use it, as three robots. Check lists each problem with a red marker. Rewrite strikes a line and shows what changed. Write types clean lines and ends with a green check." width="100%">

- **Check:** ask it to check a draft. You get a list of problems, each with the quoted line and a short fix. Nothing is rewritten.
- **Rewrite:** give it a draft. You get the smallest edit that removes the problems, and a short list of what changed. Say the text will be pasted as it is, and you get only the text.
- **Write:** an agent that is about to write follows the rules while it writes.

## What it catches

<img src=".github/readme/zoo.svg" alt="Seventeen pixel monsters, one for each pattern. A scan flags four together, and the editor clears them. A second scan flags just one, and the editor lowers the pen and lets it stay; the monster gets a heart and the word stet." width="100%">

- Invented facts, numbers, quotes and names.
- Chatbot leftovers such as "Certainly!", "I hope this helps" and unfilled placeholders.
- Sameness: five posts that open or end the same way.
- Patterns that matter in combination: "not X, but Y", groups of three, setups before the point, fake meaning at the end of a sentence, stacked fragments, piled-up hedges, vague sources, and more.

It has short pages for LinkedIn, X, email, website copy, docs, Slack, tickets and proposals.

## Does it work?

<img src=".github/readme/results.svg" alt="A high-score screen with the real results. Three models were judged on 57 cases and passed 54, 56 and 56. The exact checks passed on all 171 answers." width="100%">

The repo has 57 invented test cases in four sets, including cases where the right answer is to change nothing. Three models from one provider answered each case once, and a second model judged the answers without knowing which model wrote them. The exact checks (numbers, links, code, quotes, long dashes, chatbot leftovers) passed on all 171 answers. Judged passes were 54, 56 and 56 of 57.

The limits are real. The rules were shaped by failures on two of the four sets. One judge model read everything, and it shares a provider with the models tested. Other providers are untested. A difference of one or two cases is noise. Details, the five misses and how to run the tests yourself are in [evals/](evals/).

## What it does not do

- It does not teach good writing or a house style.
- It does not detect AI. Detectors are unreliable: in one study, seven of them flagged 61% of essays by non-native English writers as AI, though people wrote them. This skill never says who wrote a text.
- One pattern proves nothing. It acts on combinations, and leaves a text alone when only one shows up. Editors call that *stet*: let it stand.
- It works on English. For other languages it checks only for invented facts, padding and sameness.

## Your own voice

Give your agent a voice file or a short sample with your request. The skill keeps your phrasing and adds no voice of its own.

<details>
<summary><b>Something went wrong?</b></summary>

Open a [bad output report](https://github.com/nocodeanish/write-without-ai-slop/issues/new?template=bad-output.yml). Paste your request, the text and the answer. Use invented text or text you are free to share.

To add a pattern or fix a page, see [CONTRIBUTING.md](CONTRIBUTING.md). Small first tasks carry the `good first issue` label.

</details>

<details>
<summary><b>Privacy</b></summary>

The skill is text files and one optional script, `scripts/check_text.py`. The test and check scripts in this repository are separate from the skill. All of them use only the Python standard library, and none makes a network call or collects data. The installer `npx skills add` is a separate tool: it collects anonymous usage data unless you set `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` (see its [README](https://github.com/vercel-labs/skills#telemetry)).

</details>

<details>
<summary><b>Sources and versions</b></summary>

Where each rule comes from is in [docs/sources.md](docs/sources.md). Versions are in the [changelog](CHANGELOG.md).

</details>

## License

MIT. Created by Anish Gandhi. See `LICENSE`.

If this saved you an edit, a star helps other people find it.

Contributors are named in the [changelog](CHANGELOG.md). Small first tasks are labelled [good first issue](https://github.com/nocodeanish/write-without-ai-slop/labels/good%20first%20issue).
