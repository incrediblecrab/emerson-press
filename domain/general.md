---
id: domain.general
layer: domain
kind: functional
version: 2.2.0
status: draft
budget: 1780
tokens: 1780
mechanics: house
evidence_floor: 3
---

# Domain: General

The default. Blog posts, short essays, internal documents, email — everything with no professional register of its own.

Write for the reader's actual purpose and attention. An internal decision, an email request and a reflective post need different structures; other professional genres also benefit from clear openings.

For a functional document, make the point or request easy to find. For a narrative or exploratory piece, an opening can build deliberately. No universal claim about captive readers or which genre is hardest is needed to make either choice.

General becomes generic. A module invoked as a fallback tends to produce prose with the texture of a fallback — the transitional phrases, the balanced both-sides paragraph, the conclusion that restates the introduction. `core/` catches those constructions sentence by sentence. This module supplies the thing that prevents them upstream, which is a piece that is about something in particular.

Specificity must come from the available subject matter, not a quota for names, dates or figures. A useful general explanation can be rigorous without invented statistics or a named anecdote.

## Detect

### Throat-clearing

- The opening that circles: *in today's fast-paced world*, *now more than ever*, *as we all know*, *it's no secret that*.
- A first paragraph that announces the topic instead of starting on it.
- Scene-setting for a piece with no scene.
- An apology for the piece's own existence, or a preamble explaining what the piece will do before doing it.

### Emptiness

- Paragraphs that survive deletion with nothing lost.
- Claims too vague for their purpose, not merely claims lacking a name or number.
- A comparison that evades a requested recommendation. A neutral overview or honestly inconclusive result is legitimate.
- Advice at a level of abstraction that fits any situation and helps in none.
- A conclusion that restates the introduction in different words.
- Section headings that could sit above any content — *Key Takeaways*, *Final Thoughts*, *Understanding the Basics*.

### Reader cost

- The ask buried in paragraph four of an email.
- A subject line that names a topic rather than a request.
- Multiple unrelated asks in one message, so that acting on one loses the rest.
- Deadlines with no date, actions with no owner.
- Long undifferentiated blocks in a medium where readers scan.
- A word count set before the argument, which produces padding as reliably as a quota produces anything.
- Clickbait: a headline that withholds the thing the piece exists to say.

## Write

Start with material that serves the purpose. Remove ceremonial warm-up, but keep context, courtesy or a deliberate scene when it helps the reader.

Have a point, and put it near the front. If the piece has no point, that is diagnostic rather than a formatting problem, and no amount of structure fixes it.

Front-load. Readers on screens scan before they read and often decide inside the first line of a paragraph. Put the substantive claim in that line and the support after it, in the paragraph as well as the piece.

Use relevant, supported details where they clarify. Do not create a name, figure, date, experience or mechanism because concrete prose sounds more credible. Explain an unknown or write without the missing detail.

Give a supported position when the task asks for one. Preserve a neutral explanation, a real trade-off or an inconclusive result when that is the honest answer.

Write to the length the purpose earns. Cut repetition, but retain a transition, second example or summary when it helps the reader understand or act.

Make action requests visible, with known owners and deadlines. Do not invent either. Group related requests when that reduces coordination cost; separate or clearly number unrelated ones.

## Mechanics

House mechanics unless the task names a venue or manual. Use a citation adapter when formal references are requested; otherwise provide appropriate prose attribution and links.

- Attribute in the sentence: *a 2024 Pew survey found*, *according to the company's annual report*. Enough for a reader to check.
- Link where the medium supports links, to the source rather than to coverage of it.
- Numbers with the denominator, period and comparison needed for their meaning. Request missing context rather than supplying it speculatively.
- Headings that describe their section, in the reader's words rather than the organization's.
- Short paragraphs, because the medium is usually a screen. Lists where the content is genuinely a list, prose where it is not.
- `core/formatting.md` supplies defaults; explicit venue requirements control within their scope.

## Formats

### Blog post and short essay

Public, optional, competing with everything else on the device. It exists because there is something to say, and the writer's obligation is to make the first two sentences worth the click without lying about what follows.

Give the piece one idea. Announce it early. Support it with specific material. Land it.

The genre's characteristic failure is the piece assembled to occupy a slot — written to a keyword, padded to a length, structured into interchangeable sections with a numbered heading over each. It reads exactly like what it is.

Headlines say what the piece contains. A headline that withholds the answer to manufacture a click spends trust the piece then has to earn back.

### Email

The most-written genre in professional life and the least taught. Most of it is worse than it needs to be for reasons that are entirely fixable.

Subject line states the request and any deadline. *Approve Q3 budget by Friday* does more work than *Q3 budget*, and it survives being skimmed in a list of forty.

First line contains the ask. Context after. Recipients who need only the ask can act; recipients who need the reasoning can read on.

Prefer a clear primary ask. Related requests can share an email; make each required response easy to identify rather than predicting that readers will answer only one.

Name the owner and the date. *Someone should look at this soon* commits nobody to nothing.

Length is a cost imposed on the reader. Impose only what the content requires, and remember that the reader is on a phone.

### Internal document

Updates, proposals, decision records, briefs to colleagues — the highest-volume writing in most organizations and the least edited.

Lead with the decision, the status, or the recommendation. Readers here are scanning for whether the document affects them, and they will stop as soon as they establish it does not.

State what changed, what it means, and what happens next. Where a decision has been made, record what was decided, who decided, when, and what alternatives were rejected and why — the last one is what makes the document worth anything in a year.

Say what is uncertain rather than smoothing it, because the reader is a colleague who will find out anyway and the cost of the discovery is trust.

## Evidence

The legacy `evidence_floor: 3` emphasizes checkable support appropriate to the claim. An opinion, a supplied workplace fact and a research claim need different handling. General writing does not automatically require peer review or a formal reference list, and it does not get to invent.

The floor is lower than the regulated domains and it is not zero, because the failure this repository exists to prevent shows up here as confidently delivered specifics that are not true. The move that makes general prose good — reach for the concrete number — is the same move that produces a fabricated statistic when the number is not to hand. The discipline is that the concrete detail must be real. Where it is not available, write the sentence without it.

An optional classroom preset does not lower accuracy or require new research merely because of the reader's credentials.

## Boundaries

Against the specialized domains. This module applies when no other does. If the piece is a health explainer, `medical` governs the numbers; if it documents software, `technical` governs; if it reports the news, `press` governs attribution and structure; if it sells something, `marketing` and its substantiation rules apply. General is the residue, not an override, and a writer who invokes it to escape a stricter domain's obligations has chosen the wrong module.

Against `non-fiction`. Choose by purpose and reading experience rather than length alone. A developed narrative or critical essay may fit that module; a practical update or explanation often fits this one.

With `core/`. Core provides accuracy, restraint and style defaults, not a universal banlist. This module adds task structure. Neither justifies changing facts or deleting a construction that earns its place.

With `domain/education-level/`. Describe the reader's familiarity and support needs directly. Use a preset for an appropriate classroom task, not as a generic cure for weak prose or an assumed measure of the reader.

## Examples

These independent synthetic briefs supply the facts and the requested editing operation.

**Circling before starting**

**Supplied facts:** The requested post recommends putting a memo's decision first and its explanation afterward. No reading-time measurement or estimate of how long a rewrite takes has been supplied.

> In today's rapidly evolving digital landscape, organizations of all sizes are increasingly recognizing the importance of effective communication. This post will explore some key considerations.

> Put the decision in the first line of the memo, then explain the reason.

**A paragraph that survives its own deletion**

**Supplied facts:** The surrounding document already introduces the analysis. The quoted paragraph adds no specific condition or qualification. The task asks for a review recommendation.

> It's important to note that there are many factors to consider when approaching this topic, and different organizations may find that different approaches work better for them depending on their specific circumstances and needs.

> Cut it. If the piece needs to say that context matters, it should say which context and what it changes.

**Balance with nothing at the end of it**

**Supplied facts:** The fictional team's members report quieter conditions for focused work at home and missing informal handoffs. The author is asked to recommend how to retain remote work while addressing those handoffs. No comparative productivity study or pattern across other teams is supplied.

> There are advantages and disadvantages to remote work. Some studies show increased productivity while others show decreased collaboration. Ultimately, each organization must decide what works best for them.

> This team reports quieter conditions for focused work at home, but informal handoffs are being missed. I recommend keeping remote work while adding scheduled handoffs and written decision records.

**An email with the ask underneath the context**

**Supplied facts:** The team must choose a vendor by Thursday, October 8, 2026. Vendor A costs $40,000 and takes eight weeks; Vendor B costs $65,000, takes three weeks and includes migration support. The requested reply is A or B. No attachment or linked comparison document is supplied.

> Subject: Following up
>
> Hi team, hope you're all doing well. I wanted to circle back on the conversation we had last month regarding the vendor situation. As you know, we've been evaluating several options and there have been a number of developments since then. Anyway, it would be great to get your thoughts at some point.

> Subject: Vendor decision — choose A or B by October 8
>
> Choose Vendor A or Vendor B by Thursday, October 8, 2026. Reply A or B.
>
> A costs $40,000 and takes eight weeks. B costs $65,000, takes three weeks and includes migration support.

**A conclusion doing nothing**

**Supplied facts:** The previous paragraph already states the supported conclusion. The task asks whether this additional generic summary contributes anything; no reader-support need for it is identified.

> In conclusion, as we have seen, there are many important considerations when it comes to writing well. By keeping these principles in mind, writers can improve their craft and better serve their readers.

> End on the last real thing you had to say. If that was the paragraph above, the piece is already over.
