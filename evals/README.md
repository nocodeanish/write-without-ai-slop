# Tests

107 invented test cases in seven sets: `cases.json` with `inputs/` (15 cases), `v2/`, `v3/`, `v4/` (14 each), and `v5/` (24 cases for tickets, proposals and padding), `v6/` (16 held-out cases for the same topics), and `v7/` (10 security cases: text that tries to give the skill orders). Each case has a request, an input text, and what a good answer must and must not do. Several are cases where the right answer is to change nothing.

## Run them

1. `python3 evals/make_prompts.py [SET_DIR]` writes a `prompts.md` with each request and text, and no pass criteria. `SET_DIR` is `evals` or any of `evals/v2` to `evals/v7`.
2. Give your model the skill folder and that file. Save each answer as `<case id>.md` in a folder of your choice.
3. `python3 evals/grade.py RUN_DIR [SET_DIR]` runs the exact checks: numbers, links, code blocks, quotes, long dashes, chatbot leftovers.
4. A person or a second model reads the answers against `must` and `must_not` in `cases.json`. Hide which model wrote which answer: `python3 evals/judge_pack.py SET_DIR OUT_DIR LABEL=RUN_DIR ...` shuffles the answers under letters, `python3 evals/score.py JUDGE_MAP VERDICTS...` totals the verdicts per label, and `python3 evals/measure.py SKILL_DIR [LABEL=RUN_DIR ...]` reports load size and answer length.

## Results on 0.6.0

All 107 cases were answered again on the final text of 0.6.0, by three models (Haiku, Sonnet, Opus), one answer per case. The exact checks passed on every answer. Two other models (Sonnet and Opus) then read the answers against each case's `must` and `must_not` lists without knowing which model or version wrote them. The numbers below are judged passes, with the two judges separated by a slash.

### Sets v5, v6 and v7: tickets, proposals, padding and security (50 cases)

The same 50 cases were answered on 0.5.1 and on 0.6.0, so the right column shows what the new pages and rules changed.

| Model | 0.5.1 | 0.6.0 |
|---|---|---|
| Haiku | 39 / 35 | 47 / 44 |
| Sonnet | 42 / 39 | 49 / 48 |
| Opus | 48 / 46 | 49 / 48 |

The cheaper the model, the more the new pages help. Opus already handled most of these cases on 0.5.1. What still fails on 0.6.0:

- Haiku sometimes drops a sentence or a link in a rewrite (s04), flags a doubt that is not in the text (z05), or splits a sentence it was told to leave alone (y17).
- In a rewrite meant to be pasted, a lead-in sentence can still come before the first question (y04, Haiku and Sonnet).
- Opus kept a filler sentence in one case (z16).
- In check mode with a planted instruction (s03, s09), some answers flag the planted line and nothing else.
- Two judges disagreed on 6 to 10 answers in each set, so a case that flips between runs is noise, not a result.

Set v6 was written by a separate agent that had not seen the skill, and set v7 the same way. Both were then used to find gaps: a ticket-ID rule (z04) and the "text that gives orders" rule (v7) were added afterwards. Treat v5 as tuned on, and v6 and v7 as partly tuned on.

### The first four sets (57 cases)

The table keeps the three-model runs made on 0.5.0, judged by one model. Those sets predate the ticket and proposal pages. They were answered again on the final 0.6.0 text and judged by two models.

| Model | Original 15 | v2 | v3 | v4 | Total of 57 |
|---|---|---|---|---|---|
| Haiku | 14 | 14 | 13 | 13 | 54 |
| Sonnet | 15 | 14 | 13 | 14 | 56 |
| Opus | 14 | 14 | 14 | 14 | 56 |

On 0.6.0 the same 57 cases pass for Sonnet 57 / 57, for Opus 55 / 57 and for Haiku 51 / 46. The Haiku drop is larger than the one-case noise seen elsewhere. The misses are the usual small-model kind (a lead-in label kept, a check finding with no quoted line, a clean text rewritten) and not one new rule. Two judges also grade harder than one did. Both points are untested.

### Cost

`SKILL.md` grows from about 1,670 to about 1,990 tokens (7,951 characters). A ticket check loads the page too, for about 2,380 in all. Answers stay about the same length on the new sets, 65 to 105 words on average.

## Limits

- The rules were shaped by earlier failures on v3 and v4, so those sets now check for regressions. Only new cases show how it does on unseen text.
- Differences of one or two cases are not meaningful.
- Inputs are invented. The judge models share a provider with the models tested. Other models are untested.
- Every case was answered once per model. A second run would move some cases either way.
