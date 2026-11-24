# Tests

58 invented test cases in five sets: `cases.json` with `inputs/` (15 cases), `v2/`, `v3/` and `v4/` (14 each), and `v6/` (1 case). Each case has a request, an input text, and what a good answer must and must not do. Several are cases where the right answer is to change nothing. The v6 case is new and is not included in the results below.

## Run them

1. `python3 evals/make_prompts.py [SET_DIR]` writes a `prompts.md` with each request and text, and no pass criteria. `SET_DIR` is `evals`, `evals/v2`, `evals/v3`, `evals/v4` or `evals/v6`.
2. Give your model the skill folder and that file. Save each answer as `<case id>.md` in a folder of your choice.
3. `python3 evals/grade.py RUN_DIR [SET_DIR]` runs the exact checks: numbers, links, code blocks, quotes, long dashes, chatbot leftovers.
4. A person or a second model reads the answers against `must` and `must_not` in `cases.json`. Hide which model wrote which answer.

## Results on 0.5.1

The runs were made on 0.5.0. The rules did not change in 0.5.1, so the results still apply. One model run per original set, three models from one provider, every original case answered once. The new v6 case is not included in these results. A second model judged the answers without knowing which model wrote them. Exact checks passed on all 171 answers.

| Model | Original 15 | v2 | v3 | v4 | Total of 57 |
|---|---|---|---|---|---|
| Haiku | 14 | 14 | 13 | 13 | 54 |
| Sonnet | 15 | 14 | 13 | 14 | 56 |
| Opus | 14 | 14 | 14 | 14 | 56 |

The five misses were small: two models kept one or two hashtags, one kept a lead-in label, one check finding quoted no line, and one kept a heading in a Slack message meant to be pasted as it is.

## Limits

- The rules were shaped by earlier failures on v3 and v4, so those sets now check for regressions. Only new cases show how it does on unseen text.
- Differences of one or two cases are not meaningful.
- Inputs are invented. One judge model read the answers, and it shares a provider with the models tested. Other models are untested.
