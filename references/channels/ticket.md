# Tickets and issue comments

Issue trackers and project boards. Applies to a ticket description and to a comment on it.

## Watch for

- A result stated as fact that the input does not give (fixed, working, deployed, verified).
- A bug report with no way to reproduce it. Flag a missing steps list, expected result or actual result. Never invent the steps. In a rewrite, leave a marker such as "[steps needed]".
- An acceptance criterion nobody can check ("works well", "is fast", "feels smooth"). Flag it. Never invent the threshold.
- Several unrelated questions in one comment, or the ask buried under background.
- A recap of the title or of earlier comments before the point.
- One feature or screen called by several names in the same ticket.
- A status comment with no fact in it ("Working on it, will update soon").
- Chatbot openers and closers in a comment ("Great catch!", "Let me know if you need anything else").
- A guess about the cause, written as if it were known.

In a rewrite of a comment, the first sentence is the first question or ask, then the context if it is needed. Drop an opener or closer that only thanks or offers more help. Keep the @mention and every ticket ID the text names, even when the sentence around it is cut.

## Leave alone

- Lists, steps, tables and other structure the format needs. Equal-looking items in a list of requirements are not sameness.
- Ticket IDs, @mentions, links, branch names, labels, status names, code terms, error text and file paths. Keep them exactly.
- A short, plain comment. A one-line answer is fine.
