---
id: domain.general
layer: domain
kind: functional
version: 2.1.0
status: draft
budget: 2054
tokens: 2054
mechanics: house
evidence_floor: 3
---

# Domain: General

The default. Blog posts, short essays, internal documents, email — everything with no professional register of its own.

Every other module in this directory writes for a captive reader. The judge has to read the brief. The reviewer has to read the paper. The clinician has to read the note, and the person locked out of their account has to read the troubleshooting page. Those genres can afford a slow opening because the reader cannot leave.

General prose has no captive reader. Nothing bad happens to anyone who stops. A reader free to leave is why the claim goes in the first line, why the page has to survive being scanned rather than read, why an email carries one ask, and why the throat-clearing opener has to go. It also explains why this is the hardest domain to write well and the easiest to write adequately, and why the beige machine register — smooth, competent, about nothing in particular — collects here first. When no genre supplies the constraints, the writer has to.

General becomes generic. A module invoked as a fallback tends to produce prose with the texture of a fallback — the transitional phrases, the balanced both-sides paragraph, the conclusion that restates the introduction. `core/` catches those constructions sentence by sentence. This module supplies the thing that prevents them upstream, which is a piece that is about something in particular.

The rule is that specificity has to come from the subject, because the genre supplies none. `non-fiction` gets rigor from its apparatus, `legal` from its authority, `medical` from its numbers. General prose gets it from names, dates, figures, and the particular case — or it does not get it at all.

## Detect

### Throat-clearing

- The opening that circles: *in today's fast-paced world*, *now more than ever*, *as we all know*, *it's no secret that*.
- A first paragraph that announces the topic instead of starting on it.
- Scene-setting for a piece with no scene.
- An apology for the piece's own existence, or a preamble explaining what the piece will do before doing it.

### Emptiness

- Paragraphs that survive deletion with nothing lost.
- Claims with no name, number, or date anywhere near them.
- Both-sides balance that reaches no view. Weighing is fine; refusing to land after weighing is not.
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

Start on the subject. The first sentence carries information; the second carries the reason the reader should keep going. Everything before that is warm-up, and warm-up belongs in a draft rather than a piece.

Have a point, and put it near the front. If the piece has no point, that is diagnostic rather than a formatting problem, and no amount of structure fixes it.

Front-load. Readers on screens scan before they read and often decide inside the first line of a paragraph. Put the substantive claim in that line and the support after it, in the paragraph as well as the piece.

Reach for the concrete. A name, a number, a date, a case. This is the whole technique, and it works because abstraction is what the machine register defaults to and specificity is what it cannot fake.

Take a position where the material supports one, and say so plainly. Balanced consideration followed by a view is honest. Balanced consideration followed by nothing is evasion dressed as fairness.

Write to a length the argument earns. Then cut what the argument does not need — which usually includes the transitional sentences, the second example, and the summary paragraph at the end.

In anything that asks for action, put the ask first, name the owner, and give a date. One ask per message. If there are three, send three messages or number them and say so at the top.

## Mechanics

House mechanics — no external manual and no citation system. That is the point of the domain, and it is not a license to be vague about where things came from.

- Attribute in the sentence: *a 2024 Pew survey found*, *according to the company's annual report*. Enough for a reader to check.
- Link where the medium supports links, to the source rather than to coverage of it.
- Numbers with their base and their date. *A third of customers* means nothing without the denominator and the year.
- Headings that describe their section, in the reader's words rather than the organization's.
- Short paragraphs, because the medium is usually a screen. Lists where the content is genuinely a list, prose where it is not.
- No external style manual; `core/formatting.md` governs, and this module adds nothing to it.

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

One ask per email. A message containing three requests will get one answered.

Name the owner and the date. *Someone should look at this soon* commits nobody to nothing.

Length is a cost imposed on the reader. Impose only what the content requires, and remember that the reader is on a phone.

### Internal document

Updates, proposals, decision records, briefs to colleagues — the highest-volume writing in most organizations and the least edited.

Lead with the decision, the status, or the recommendation. Readers here are scanning for whether the document affects them, and they will stop as soon as they establish it does not.

State what changed, what it means, and what happens next. Where a decision has been made, record what was decided, who decided, when, and what alternatives were rejected and why — the last one is what makes the document worth anything in a year.

Say what is uncertain rather than smoothing it, because the reader is a colleague who will find out anyway and the cost of the discovery is trust.

## Evidence

Rung 3. A named, checkable source in the sentence. General writing does not need peer review, and it does not get to invent.

The floor is lower than the regulated domains and it is not zero, because the failure this repository exists to prevent shows up here as confidently delivered specifics that are not true. The move that makes general prose good — reach for the concrete number — is the same move that produces a fabricated statistic when the number is not to hand. The discipline is that the concrete detail must be real. Where it is not available, write the sentence without it.

Rung 3 is the lowest floor in this directory and it is still a floor. Loading a `domain/education-level/` tier beside this module changes who the sentence is pitched at, never whether the number in it is real.

## Boundaries

Against the specialized domains. This module applies when no other does. If the piece is a health explainer, `medical` governs the numbers; if it documents software, `technical` governs; if it reports the news, `press` governs attribution and structure; if it sells something, `marketing` and its substantiation rules apply. General is the residue, not an override, and a writer who invokes it to escape a stricter domain's obligations has chosen the wrong module.

Against `non-fiction`. The nearest boundary and the easiest to get wrong, because both cover prose with no institution behind it. Length and expectation separate them. A short piece a reader skims for what they need is this module. An essay someone chose, will finish, and might reread is `non-fiction`, and it takes Chicago and a rung-4 floor with it.

Against `core/`. The closest relationship in the repository, and the reason the boundary needs stating. `core/` bans constructions; this module supplies positive shape — front-loading, the one-ask rule, the demand for a point. On a piece with no other domain, they are nearly the whole instruction set, and `core/restraint.md` still governs: neither module bans a construction that is earning its place.

With `domain/education-level/`. This module and no tier is the pairing most at risk of the beige register, because an adult reader at work and a genre defined as the residue supply almost no friction between them. Loading a tier adds constraints and helps a little. The real correction is the one this module already asks for: specificity from the subject.

## Examples

**Circling before starting**

> In today's rapidly evolving digital landscape, organizations of all sizes are increasingly recognizing the importance of effective communication. This post will explore some key considerations.

> Most internal memos get skimmed in under fifteen seconds. Writing the decision in the first line rather than the fourth paragraph is the entire fix, and it takes about a minute.

**A paragraph that survives its own deletion**

> It's important to note that there are many factors to consider when approaching this topic, and different organizations may find that different approaches work better for them depending on their specific circumstances and needs.

> Cut it. If the piece needs to say that context matters, it should say which context and what it changes.

**Balance with nothing at the end of it**

> There are advantages and disadvantages to remote work. Some studies show increased productivity while others show decreased collaboration. Ultimately, each organization must decide what works best for them.

> Remote work suits deep individual work and hurts the unplanned conversations that produce new projects. Teams that shipped well remotely tended to have written decision records and scheduled the overlap; teams that struggled relied on hallway context nobody replaced. If your work depends on the hallway, replace it deliberately before removing it.

**An email with the ask underneath the context**

> Subject: Following up
>
> Hi team, hope you're all doing well. I wanted to circle back on the conversation we had last month regarding the vendor situation. As you know, we've been evaluating several options and there have been a number of developments since then. Anyway, it would be great to get your thoughts at some point.

> Subject: Vendor decision — need your pick by Thursday
>
> Choose Vendor A or Vendor B by Thursday, October 9. Reply to this thread with one word.
>
> A costs $40k and takes eight weeks. B costs $65k, takes three, and includes migration support. Full comparison in the linked doc.

**A conclusion doing nothing**

> In conclusion, as we have seen, there are many important considerations when it comes to writing well. By keeping these principles in mind, writers can improve their craft and better serve their readers.

> End on the last real thing you had to say. If that was the paragraph above, the piece is already over.
