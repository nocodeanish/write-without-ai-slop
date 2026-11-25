# Sources

Where the rules come from. The skill does not read this file. Checked 2026-11-17. Review the word lists by 2027-05-17.

Labels: **official** is a maker's own guidance, **research** is a study, **real-use** is a practitioner or news source, **inference** means no source was found and the rule is a judgment.

## Patterns

- Wikipedia, "Signs of AI writing" (real-use, medium confidence): negative parallelism ("not X, but Y"), groups of three, setups, trailing "-ing" claims, puffed importance, false ranges, challenge-then-optimism, regression to the mean, elegant variation, and chatbot leftovers. Its editors call the list "observations, not rules": signs matter in combination.
- HBR, 2025-09-22, with BetterUp Labs and Stanford (real-use, low to medium; summary only): "workslop", content that "appears polished but lacks real substance". It also informs the email and Slack pages.
- Sameness across a batch and piled-up hedges: inference.

## Words

- Tier 2, first group: Kobak et al., arXiv 2406.07016 v4, 2025-02-19 (research, high). Words used far more in 2024 PubMed abstracts than expected, for example "delves" at 28 times its expected rate. Academic abstracts only, not posts, email or web copy.
- Tier 2, second group: GOV.UK A to Z style guide, "words to avoid" (official).
- Tier 2, third group (seamless, cutting-edge, unlock, tapestry and others): inference.
- Tier 3: Wikipedia (didactic disclaimers). "In order to": GOV.UK and digital.gov. "Please note", "simply", "it's easy": Google developer documentation style guide, tone page, 2026-05-27.

## Channels

### LinkedIn (low to medium)

- Entrepreneur, 2026-05-19 (real-use, news): LinkedIn said it is cutting the reach of generic AI-written posts and comments, using classifiers trained on posts its editors labeled generic or original. For comments it also looks at posting volume. Generic text can cost reach, not only trust.
- No source measured which LinkedIn tells matter most. The rest of the page is inference.

### X (medium for the rules, low for ranking)

- X platform manipulation and spam policy (official, March 2023): bans "bulk, aggressive, high-volume unsolicited replies, mentions, or Direct Messages", "repeatedly posting identical or nearly identical Posts", and "aggressively or automatically engaging with Posts to drive traffic or attention". It does not mention AI.
- PiunikaWeb, 2026-02-24 (real-use): since 2026-02-23 the X API allows a programmatic reply only when the original author mentions or quotes the account.
- xai-org/x-algorithm README (official, direction only): the feed predicts what each viewer will do with a post, and negative actions (not interested, mute, block, report) count against it. No published rule on length or links.
- Simon Willison, 2026-02-23 (real-use): AI "reply guy" tools post "generic, banal commentary slop", often ending in a question "to drive engagement".
- Techweez, 2026-09-03, citing X's product head (real-use, numbers unaudited): AI replies are "polished, agreeable comments that say very little". X says it removed more than 1.7 million bot accounts since January and 42,000 in July. The article also warns that careful human writing can be mistaken for bot output.

### Email (medium for plain-language rules, low for reader reaction)

- Australian Government Style Manual, "Emails and letters", 2024-12-20 (official): keep the email as short as possible, one idea per paragraph, "write only what the recipient needs to know", state the main idea at the start, make the subject line "sum up the purpose", no emoji in formal mail, link a phrase rather than pasting a raw URL.
- Mailchimp, "Finding the Right Email Tone", 2024-11-26, and Content Style Guide, 2023 (official company content): avoid excessive exclamation marks, slang and corporate-speak; clarity over entertainment; no "fluffy metaphors".
- GOV.UK A to Z style guide (official): no need for "please" or "please note"; use bold sparingly.
- Jakesch et al., CHI 2019 (research, old): in three experiments with 286 to 527 US participants, people who suspected or were told that AI wrote a host profile trusted that host less, but only when they saw a mix of profiles. One context, perceived rather than real AI authorship, no behavior measured.
- Instiller, 2023-07-03 (vendor study, low to medium): of 510 UK participants, about half could not tell AI marketing email from human.
- Hunter, a cold-email vendor (low): 47% of sender respondents said they would be less likely to reply to an AI-written email. Stated intent, no sample size.
- No source measured real reply rates with and without AI-sounding copy.

### Website copy (medium for promotional language)

- Nielsen Norman Group, Morkes and Nielsen, 1997 and 1998 (research, old, small samples): in a test with 51 users, objective language scored 27% higher on usability than a promotional control; concise scored 58% higher, scannable 47%, and all three together 124%. A second test with 21 technical users found a rewrite without buzzwords and unsupported claims scored 159% higher. The article also warns that puns are risky for international readers.
- Mailchimp, 2024-11-26 (official): "BUY NOW!" versus "Discover member-exclusive pricing through Friday" as overselling versus clear.
- GOV.UK (official): "Plain English is mandatory for all of GOV.UK", with a list of buzzwords to avoid.

### Docs and README (high; three official guides agree)

- Google developer documentation style guide, tone page, 2026-05-27 (official): avoid buzzwords, "please note", "at this time", choppy or long-winded sentences, starting every sentence the same way, exclamation marks, "let's", "simply", "it's easy" or "quickly" in a procedure, and clichés. "Please" in instructions is overdoing politeness.
- Digital.gov plain language guide, 2025-09 (official): "to" for "in order to", "can" for "is able to"; avoid hidden verbs, "and/or", "e.g." and "i.e.".
- GOV.UK (official): no "in order to"; check sentences over 25 words; avoid "e.g.", "i.e." and "etc".

### Slack and chat (medium for etiquette, low for AI-specific tells)

No source discusses AI-written chat messages, so the AI-specific items are inference.

- Slack, "Slack etiquette", 2025-03-21 (official): never send a message that is only "hey"; send one complete message rather than several; use threads; use emoji reactions instead of "I agree"; keep @username for specific or urgent requests.
- Slack, "Designing and formatting messages in Slack", 2025-08-05 (official, product marketing): bullets, bold titles and a few emoji suit longer messages such as announcements; formatting need not be the focus of every message.
- Equal Experts public Slack guide, CC-BY-SA-4.0 (real-use): "Respect the amount of information anyone can tolerate reading." Prefer a thread in large channels, link to a message instead of copying it, use @channel and @here only for high-priority items.
- Grammarly, 2024-01-29, and Slab, 2020-03-04 (third party, opinion, low): combine follow-ups, use threads, @here and @channel only for urgent items.

### Padding (medium for the idea, low for the test)

- Australian Style Manual, "Emails and letters", 2024-12-20 (official, already listed under email): "write only what the recipient needs to know", state the main idea first.
- HBR, 2025-09-22 (real-use, already listed above): "workslop", content that "appears polished but lacks real substance".
- hardikpandya/stop-slop SKILL.md, read 2026-11-25 (real-use): cuts filler phrases and scores "Density: anything cuttable?". It works at phrase level. We found no rule in it that keeps a long text whose paragraphs all carry something.
- The test "what would the reader lose if this were cut" and the rule that length alone is not a tell are inference.

### Tickets and issue comments (low, all inference)

No source measured AI tells in tickets, so the whole page is inference. It checks for these problems: a result stated with nothing behind it, a missing way to reproduce a bug, criteria nobody can check, and several questions in one comment. The "leave alone" list exists because the "same shape everywhere" rule would otherwise flag normal lists and tables.

### Proposals (low, all inference)

One LinkedIn post (November 2026, author unknown, not linked) listed twelve signs that a proposal was written by AI. It is a list of ideas, not evidence, and its wording is not copied. Seven of the twelve were already in the skill: vague wording, rotating names, regular rhythm, generic text, unsourced figures, equal section lengths and claims about the client. Five are new on the proposals page: the client's problem repeated in longer words, a scope with no exclusions, a timeline with no dates, next steps with no person or date, and spelling that differs from the reader's. The swap test is a new way to check the generic-text sign. All of it is a practitioner's opinion until a study says otherwise.

## AI detectors

The skill never judges who wrote a text. Liang et al., arXiv 2304.02819 (research): seven detectors flagged 61.22% of TOEFL essays by non-native English writers as AI, though people wrote them.

## Limits

Email and Slack rest on thin evidence. The X and LinkedIn pages lean on news reports, and X's bot-removal numbers were not audited. The NN/g studies are from the 1990s and small. The skill is tested on invented inputs only.

## Prior work

We read [blader/humanizer](https://github.com/blader/humanizer) and [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) and wrote our lists fresh. On 2026-11-25 we also saw two skills on GitHub: the ticket-authoring skill by rampstackco and the upwork-proposal-writing-skill by fahadqaseem. We read only their titles and descriptions. They teach how to write a ticket or a proposal. This skill only lists what not to do and does not teach a structure.
