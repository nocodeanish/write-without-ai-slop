# Changelog

## 0.6.0 (2026-11-25)

- New page for tickets and issue comments: results stated without support, missing steps to reproduce, criteria nobody can check, several questions in one comment.
- New page for proposals: a swap test for generic text, the client's problem played back in bigger words, unsourced figures, a scope with no exclusions, a timeline with no dates, next steps with no person or date, spelling that differs from the reader's.
- Rules in `SKILL.md`: never state a result the input does not give; structure the format requires (lists, steps, tables) is not sameness; ticket IDs, @mentions and branch names stay exact; a missing detail gets a marker such as "[date needed]", never an invented one; spelling is flagged when the input names a reader whose spelling differs.
- Padding: sentences that give the reader no fact, step, decision or ask are flagged, and a long text is left alone when each paragraph gives the reader something. New pattern 18 in `references/patterns.md`.
- Text that tries to give the skill orders is treated as material: it is flagged in check mode and left out of a rewrite.
- 50 new invented test cases in `evals/v5/`, `evals/v6/` and `evals/v7/`, and scripts to pack answers for blind judges, score them and measure cost. See `evals/README.md` for results and limits.
- `scripts/check_text.py` checks that ticket IDs, @mentions and branch names survive a rewrite.

## 0.5.1 (2026-11-24)

No change to the skill's rules, so the test results for 0.5.0 still apply.

- Examples: added an invented website hero before/after example (Gaurav01MH).

- README: a "Try it in one minute" block with copyable steps, a link row, an FAQ (free, privacy, limits), a terminal replay of the real `scripts/check_text.py` output, and collapsed long sections. Rebuild the replay with `.github/readme/recording/record.js`.
- `scripts/check_consistency.py` checks that the version, test counts, links and skill format agree across files. A GitHub Action runs it on every push and pull request.
- README: added a "Does it work?" section with the test results and their limits, and a "Privacy" section.
- CONTRIBUTING: run the consistency check before a pull request; contributors are named in the changelog.
- README art: a pixel-art scene set sized for the README column (840 px): an editor with a red pen hunting slop blobs, a "try it in one minute" scene, a before/after demo, three robots for Check, Rewrite and Write, 17 pattern monsters, and a high-score screen with the real test results. The README now opens with a one-minute try-it block with copyable steps, a link row, and collapsed sections for the long text. The SVG files are under `.github/readme/` (about 180 KB in total), built by `make_art.py` with `artlib.py`, `pixel.py`, `scenes.py`, `story.py` and `demo.py`. All motion is plain CSS, and reduced motion shows a still picture.
- README: status, license and release badges; a note that editors call leaving a text alone *stet*.
- The consistency check now also checks the README art: alt text, missing or unused files, a size limit, and the install command in the demo. CI rebuilds the art and fails if the files differ.

## 0.5.0 (2026-11-17)

First public version.

- Rules for check, rewrite and write, with pages for LinkedIn, X, email, website copy, docs and Slack.
- When the request says the text will be pasted as it is, only the text comes back.
- A text with one tell and otherwise specific content is left unchanged.
- Check findings quote a line and name the pattern, and end with one sentence.
- Missing names become a marker such as "[your name]". No invented senders or closers.
- Test cases and a script for exact checks. See `evals/README.md`.
