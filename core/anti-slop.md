---
id: core.anti-slop
layer: core
version: 1.3.0
status: draft
budget: 2161
tokens: 2161
evidence:
  - sources/signs-of-ai-writing.md
  - sources/field-guide-to-ai-slop.md
  - sources/ap-stylebook.md
  - sources/stop-slop.md
  - sources/ai-slop-research.md
  - sources/antislop-banlists.md
---

# Anti-Slop

One mechanism produces nearly all of this. A model predicts likely words, and specific facts are rare while approving generalities are everywhere. So the model trades detail for praise, and the prose comes out less specific and more emphatic at once. Volume rises as resolution drops.

The trade leaves a countable trace. Profiling work that compares model output against a human baseline finds some phrasings running more than a thousand times more often on the machine side. That ratio is the thing a reader notices — not any single word, which is why no list of forbidden words survives contact with the next model.

Read what follows as symptoms. The disease is that trade, and it routes around any vocabulary you forbid.

## Detect

### Inflation

- **Significance attached to ordinary facts.** `a pivotal moment in`, `stands as a testament to`, `underscores the importance of`, `marked a turning point`, `reflects a broader shift`, `left an indelible mark`, `setting the stage for`. Fires hardest on mundane material — a founding date, a population count, a bus route.
- **Hedge, then inflate.** Conceding a subject is minor and explaining its broader significance anyway.
- **Manufactured discourse.** A subject placed amid `ongoing debates` or said to have `participated in public discussions`, with no debate named.
- **Brochure register.** `nestled in the heart of`, `boasts a`, `rich cultural heritage`, `renowned for`, `a diverse array of`, `natural beauty`, `groundbreaking`. Arrives uninvited, sometimes while claiming to strip promotional tone out.
- **Credential recital.** Importance argued by cataloging coverage: `featured in national outlets`, `profiled in trade publications`, `maintains an active social media presence`.

### Evasion

- **Unnamed authorities.** `experts argue`, `observers have noted`, `industry reports suggest`, `critics contend`, `it is widely regarded`.
- **Inflated consensus.** `scholars` or `reviewers` in the plural over one cited source. One view reported as settled.
- **False open sets.** `such as` or `among others` in front of a list that is actually the whole list.
- **Speculation after a disclaimer.** Announcing something is `not widely documented`, then guessing at it with `likely`. For people this collapses into formula: the subject `keeps personal details private`, or `maintains a low profile`.
- **Vague connection.** `in connection with`, `in connection to`, `connected with`, `connected to`, `in association with`, `associated with` standing where a nameable relation belongs. Ask what the relation is: if it is ownership, employment, funding, authorship, membership, or cause, name it and let `of`, `for`, or `by` carry it. Where the relation genuinely is an unexplained correlation, the phrase is exact and `accuracy` requires it.

### Reflex

- **Throat-clearing openers.** `Here's what`, `Here's the thing`, `The truth is`, `It turns out`, `Let me be clear`, `The uncomfortable truth is`. An announcement standing where the point should be.
- **Vague declaratives.** `The implications are significant.` `The stakes are high.` `The reasons are structural.` `The consequences are real.` A sentence asserting that something is important, deep, or structural without naming the thing. Delete it, or replace it with the thing.
- **Emphasis crutches.** `Full stop.` `Period.` `Let that sink in.` `Make no mistake.` `Here's why that matters.` Punctuation of tone substituting for a reason.
- **Meta-commentary.** `In this section, we'll`, `Let me walk you through`, `As we'll see`, `The rest of this piece explains`. A section announcing itself instead of starting.
- **Negative parallelism.** `not just X, but Y`, `it isn't X — it's Y`, `no X, no Y, just Z`. Stages the correction of a misconception the reader never held. Runs across sentence boundaries too, so a one-sentence check misses it. The plain comparative `X rather than Y` is not this: it negates nothing and states a preference, and `voice` depends on it. Some models do overuse the comparative, so watch its rate and never its presence.
- **Negative listing.** `Not a study. Not a survey. A guess.` The same move spread across three fragments.
- **Triads.** Three stacked adjectives, or three parallel clauses, used to make a thin observation look surveyed. A list that genuinely has three members is not this.
- **Tacked-on participles.** A fact with an interpretive tail: `..., highlighting its role in`, `..., ensuring continued growth`, `..., reflecting the region's character`, `..., contributing to`, `..., fostering`, `..., underscoring`.
- **Formula edges.** `In today's fast-paced world`, `As technology continues to evolve`, `At the end of the day`, `Despite these challenges`, `In conclusion`. Also the closing shape itself: a `Challenges` section built on a concession, then a `Future Outlook` of speculative optimism.
- **Unearned profundity.** `Something shifted.` `Everything changed.` `But here's the thing.` A grave pivot arriving from nowhere.
- **Permission-granting closers.** `And that's okay.` `And that's the point.` Reassurance nobody asked for.
- **Questions as drum hits.** `The solution? Simpler than you think.`
- **Copula avoidance.** `serves as`, `stands as`, `functions as`, `represents`, `boasts`, `features`, `offers`, `maintains`, `refers to` where `is` or `has` is honest. Also the detour: `ventured into politics as a candidate` for `was a candidate`.

### Churn

- **Synonym rotation.** One referent renamed at each mention — `the company`, `the firm`, `the organization`, `the enterprise` — until a reader cannot tell whether a second organization has entered the paragraph. Older than the models and no longer particular to them, so it stays here on reader grounds alone; `restraint` carries it among the non-tells.
- **Dilution.** Four sentences carrying one sentence of content. The other three do not merely add nothing; they weaken the one that mattered.
- **No throughline.** Every sentence parses and you cannot say what is being claimed.
- **Generic figures of speech.** Comparisons landing near the idea without being thought through — a skill as a muscle, a process as a journey, parts clicking into place like puzzle pieces.

### Cliche and jargon

- **Borrowed shorthand.** `paradigm shift`, `perfect storm`, `holy grail`, `game changing`, `smoking gun`, `sea change`, `cutting edge`, `wake-up call`, `silver bullet`, `low-hanging fruit`, `tip of the iceberg`. A cliche signals that nothing specific is being said, and attention slides off the page.
- **Jargon as camouflage.** Specialist vocabulary standing in for a fact the writer has not established, or softening one they would rather not state plainly.
- **Redundancy.** A word restating what the sentence already carries: `past history`, `new record`, `totally destroyed`, `future planning`, `convicted felon`, `ATM machine`, `HIV virus`, `civil lawsuit`. Degree words on absolutes belong here too — `very unique`.

### Vocabulary

Density convicts, never a single word. These co-occur, so several in one paragraph is the signal: `delve`, `crucial`, `pivotal`, `robust`, `tapestry`, `landscape`, `showcase`, `intricate`, `interplay`, `meticulous`, `underscore`, `testament`, `garner`, `bolster`, `foster`, `enhance`, `align with`, `vibrant`, `enduring`, `deep dive`, and `additionally` opening a sentence.

Read this literally. A synonym of a flagged word is not flagged, and context governs — an underscore can be a typographic mark.

## Write

**Substitution test.** If a clause stays true with a different company, town, or person dropped into it, it says nothing about this one. Cut it.

**Deletion test.** Remove every trailing participle. If nothing was lost, it was ornament. This single procedure catches significance inflation, superficial analysis, and puffery at once, and it keeps working after the vocabulary shifts.

Name a thing once and keep that name. Repetition is not a fault. It is how a reader tracks a referent across a paragraph.

Let `is` be `is`. Reach for a heavier verb only when the relation is heavier than identity.

State the fact and stop. Significance is the reader's to draw, and a fact strong enough to matter does not need to be told that it matters.

Attribute to someone nameable or not at all. Count sources before characterizing them: if one person said it, write that one person said it. When you did not find something, say where you looked and stop — do not follow a disclaimer with a guess.

Test every comparison for where it draws from. Figures of speech that work are either specific — rooted in something the writer actually observed — or culturally resonant, drawn from a shared reference. A comparison that is neither is merely plausible. Cut it.

Prefer the number, the proper noun, the date, the quoted phrase — each drawn from a source, never minted to fill a slot. A model can imitate the look of a specific. What it cannot manufacture is one that survives being checked. That is the defense that lasts, which is why specificity and verification are one instruction. `accuracy` owns the check.

Remember who pays. Slop is cheap to write and expensive to read, and the bill goes to someone downstream who never agreed to it — the reviewer, the maintainer, the next person who needs the answer. That is the reason to cut a hollow paragraph, and it holds whether or not anyone suspects a machine wrote it.

## Examples

The specifics below stand in for facts you must actually hold. The lesson is the move from vague to concrete, not these particular numbers. Supply your own, and source them.

**Significance inflation**

> Founded in 1974, the bureau represented a pivotal step in the modernization of municipal recordkeeping, reflecting a broader shift toward local autonomy.

> The bureau opened in 1974. Three neighboring counties copied its filing system within five years.

**Brochure register and copula avoidance**

> Nestled in the heart of the valley, the gallery serves as the association's exhibition arm and boasts four separate spaces.

> The gallery is the association's exhibition space. It has four rooms.

**Tacked-on participle**

> The population reached 56,998 in the 2008 census, creating a lively community and further enhancing its significance as a cultural hub.

> The 2008 census counted 56,998 residents.

**Negative parallelism with a formula closer**

> In the end, learning an instrument isn't really about the notes — it's about rediscovering the courage to be a beginner.

> I still can't play barre chords.

**Vague attribution**

> Experts argue the policy has been widely interpreted as a signal to markets.

> The one economist who testified, named in the hearing record, called it a signal to markets. No one else on the panel addressed it.

**Speculation after a disclaimer**

> While specific details about her early career are not widely documented, she likely developed her interest in ceramics during this period, which would prove formative.

> Her work before 1979 does not appear in the museum's archive or in either published interview.

**Credential recital**

> The firm has been profiled in leading trade publications and maintains an active presence across major social platforms, reflecting its standing in the industry.

> Ceramics Monthly ran a profile in March. The firm has 1,900 followers on Instagram.

**Dilution**

> The committee met on Tuesday to discuss the proposal. During this meeting, members had the opportunity to review the various elements of the plan and share their perspectives. A range of viewpoints was expressed throughout the course of the discussion. Ultimately, no formal decision was reached at this time.

> The committee discussed the proposal Tuesday and did not vote.

**Generic figure of speech**

> Building a research practice is like tending a garden: it requires patience, consistent care, and a willingness to let things grow at their own pace.

> Building a research practice is mostly waiting on other people's email.
