# Before and after

The inputs are invented. The "after" text is what a model returned when it followed this skill. It shows the shape of the output, not a promise of the same result every time.

## LinkedIn post (rewrite)

Before:

```
Here's the thing: shipping fast isn't just about speed, it's about trust.

Last month our team cut the checkout bug backlog from 42 to 9 in two weeks. Not just a win for engineering, but a win for customers, for the business, and for the future.

At the end of the day, the journey of building great products is a tapestry of small, consistent steps.

Agree? What's your biggest lesson?

#Leadership #Growth #Engineering #Mindset #Innovation
```

After:

```
Shipping fast builds trust.

Last month our team cut the checkout bug backlog from 42 to 9 in two weeks.

Good products get built in small, consistent steps.

#Engineering

Changed:
- Cut "Here's the thing:" and the "isn't just about speed" contrast.
- Cut the "win for customers, for the business, and for the future" group of three.
- Replaced the tapestry line with the plain lesson.
- Removed the comment-bait question.
- Cut five hashtags to one.
```

## Cold email (rewrite)

The writer said: Dev builds invoice-matching automation. Priya runs finance operations at Northwind.

Before:

```
Hi Priya,

I hope this email finds you well! I wanted to reach out because I was really impressed by your company's incredible growth. I help teams like yours leverage AI to unlock efficiency. Let me know your thoughts, and I'd love to jump on a quick call whenever works!

Best regards,
Dev
```

After:

```
Hi Priya,

I build invoice-matching automation, and I'm writing because you run finance operations at Northwind.

Does your team match invoices by hand today? If it does, I'd like to show you how mine works on a short call.

Best regards,
Dev

Changed:
- Cut the "hope this finds you well" opener.
- Cut the praise for "incredible growth". Nothing supports it.
- Replaced "leverage AI to unlock efficiency" with what Dev builds.
- Replaced "let me know your thoughts" with one clear question.
```

## Website hero (rewrite)

Before:

```
Make every workday effortless.

Planboard helps your team stay ahead with one clear workspace.

Create tasks, assign an owner, and set a due date in one place.
```

After:

```
Planboard keeps tasks, owners, and due dates in one place.

Create a task, assign an owner, and set a due date.
```

Changed:
- Removed the unsupported promise in "Make every workday effortless."
- Replaced the vague "stay ahead" claim with the product's stated function.
- Kept all three features: tasks, owners and due dates.

## Check only

Request: "Check this draft for AI patterns. Do not rewrite it."

Draft: "In today's fast-paced world, communication is more crucial than ever. Our platform seamlessly empowers teams to collaborate, innovate, and thrive. Whether you're a startup or an enterprise, we've got you covered. Experts agree that better tools lead to better results. Ready to unlock your team's potential?"

Result:

```
- "Experts agree that better tools lead to better results." Vague source. Name the expert and date, or cut the line.
- "Whether you're a startup or an enterprise, we've got you covered." False range plus a generic promise. Name who uses it, or cut.
- "Our platform seamlessly empowers teams to collaborate, innovate, and thrive." Two list words and a group of three. Say what the platform does.
- "In today's fast-paced world, communication is more crucial than ever." Stock opener plus puffed importance. Open with the product.
- "Ready to unlock your team's potential?" List word in a closer with no next step. Replace with a concrete action.

Clear problem: every sentence is general, and the patterns stack with no specific fact anywhere in the draft.
```
