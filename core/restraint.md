---
id: core.restraint
layer: core
version: 1.3.0
status: draft
budget: 1598
tokens: 1598
evidence:
  - sources/signs-of-ai-writing.md
  - sources/field-guide-to-ai-slop.md
  - sources/stop-slop.md
  - sources/kill-ai-slop.md
  - sources/ai-slop-research.md
  - sources/antislop-banlists.md
  - sources/ap-stylebook.md
---

# Restraint

Four of the other five modules in `core/` subtract something, and subtraction has its own failure mode: prose scrubbed of every tell is still formulaic, just according to a different formula. `voice` answers half of that by supplying the particulars nothing can subtract its way to. Restraint answers the other half, the part where subtraction goes too far, and it decides when two rules in `core/` pull against each other.

Three facts make this a real risk rather than a hypothetical one. Detection does not work — untrained human accuracy sits near chance, and automated detectors carry error rates too high to act on. Writers now edit around these tells deliberately, so avoidance is itself becoming a recognizable style, and each turn of that loop narrows what reads as human. And a matched-control study of 25 million forum comments found no relationship between two things you would expect to be the same: the features that genuinely separate machine prose from human prose, and the features that get a person accused of writing like a machine. Accusation runs on something else.

That last finding sets the goal, so be exact about what it licenses. The study compared accused against unaccused human comments. So it measures who draws suspicion among people; it does not measure what happens when machine-typical prose is revised toward the human range. What it does establish is a limit. Much of accusation is social gatekeeping that never reads the text closely, and no revision gets you under that. Writing to escape suspicion cannot be made to work. Editing changes the prose; it does not reach the part that decides, because that part was never reading. Writing well still works. Every rule in `core/` earns its place by making prose better for a reader, and none of them by making it harder to accuse.

So: no tell is proof. The rules here describe what to avoid writing. None of them licenses a claim about who or what wrote a given text.

## Detect

### Overcorrection

- Every sentence clipped, every paragraph one line. Plainness is its own dialect.
- Manufactured looseness: staged typos, lowercase affectation, forced profanity, studied casualness.
- A flagged word cut where it fit, at the cost of precision.
- Em dashes replaced with commas that do the job worse.
- Definite claims hedged away because confidence reads as machine polish.
- Ordinary connectives hunted out — `very`, `in order to`, `the fact that`, `there is a`. Removing these moves prose toward machine register, not away from it.

### Non-tells treated as tells

- **Clean grammar.** Many people write cleanly, and spellcheck is everywhere.
- **Formal or academic diction.** The evidence covers specific overused words, and does not generalize to elevated vocabulary.
- **Elevated single words.** `Delve`, `ascertain`, `multifaceted`. Density and co-occurrence are the signal, never one word.
- **Mixed register.** Suggests a technical writer, a young writer, playfulness, or several hands on one document.
- **Transition words in isolation.** Only a few are actually overused, and sentence-initial connectives are ordinary in essayistic writing.
- **Absent contractions.** Often just light editing, or someone who learned English as a second language.
- **Curly quotes and em dashes.** Chicago style, Word, and macOS all produce the first; professional writers use the second.
- **Missing citations.** Predates the models entirely.
- **Synonym rotation.** A style fault with a long pre-model history, taught as good practice in some educational traditions, and no longer typical of current output. `anti-slop` still says fix it, because a reader loses the referent. It convicts nobody.
- **Bland prose.** Machine output skews verbose and positive rather than flat.

### Unconditional bans

A rule stated without exception is a density signal misread as a binary. Competing anti-slop instructions ban all em dashes, all adverbs, all sentences opening with a question word, all three-item lists, and all absolutes. Each turns a tell into a filter. Where a prescriptive instruction of that kind disagrees with a measurement, the measurement wins: a ban asserted by a skill file does not outrank a rate observed in a study.

- A rule that cannot tell `fell sharply` from `declined slightly` is removing measurements, not intensifiers.
- A list with three real members is a fact about the world. Rewriting it to two changes the content to escape a suspicion.
- Sometimes a claim is universal and `never` is the exact word. Flag the unverified superlative, not the superlative.

The objection is not only aesthetic. Work that suppressed slop at scale found flat token banning unusable at roughly two thousand patterns and scored an eight-thousand-pattern banlist at 28 out of 100 on its writing rubric. The reason is mechanical: a ban fires on a token, and the token you ban to stop a cliche is also the token some exact word needs. Suppression that could back up and choose again in context handled four times as many patterns with quality intact, and at four-tenths strength it suppressed them in 90% of ordinary generation while still producing them when a prompt asked for them outright. Overcorrection has a measured curve of its own in the same project, this time on the training side rather than the sampler: removing the safeguard that ends training pressure once a preference is won raised suppression to 98% and dropped writing quality from 67.8 to 19.6, while tethering too hard held quality at 69.7 and cut suppression to 56%. All of it ran on weights and logits, not on prompts, so read it as an analogy rather than a measurement of this layer. The analogy holds because the mechanism is the same: a ban filters a surface form, a revision is a decision made in context. Only the second one scales.

The lists themselves carry one further limit. Every published slop list was measured on creative writing — fiction prompts scored against a fiction baseline — so more than half of the best-known thousand-word list never appears in the human corpus's common bigrams at all, and most of that half is invented fantasy names and genre furniture. Almost none of it says anything about a memo, a spec, or a case note. Take the reasoning and check the entries against the prose you are actually writing.

## Write

Triage before editing. Separate what is slop from what was chosen. A dash, a formal word, a triad, a clean sentence — each can be a decision someone made and can defend. Change what was never decided.

Fix what costs the reader. Leave the rest.

When `voice` says commit and `accuracy` says keep confidence proportional, split on the kind of claim. Commit on judgment and taste, where the writer's stance is the content. Stay proportional on fact and cause, where the evidence is the content. The anti-hedge rule frees you to take a position. It never frees you to overstate what you can show.

Ask what a change buys. If cutting a word loses precision and buys only the absence of suspicion, keep the word. The reader was never the one auditing you.

Density is the signal. One instance of anything on any list here means nothing.

Distrust your own detection instinct, including on your own drafts. Confidence about authorship is the least reliable part of this whole enterprise, and false accusations cost more than the slop does.

Hold these rules the way a working style guide holds its own: as compromise and judgment in gray areas, revisable, not as a standard of correctness.

## Examples

**Overcorrection**

> Q3 missed. Badly. Sales down 12%. Nobody saw it coming. Except everyone did.

Every sentence a fragment is as formulaic as every sentence at twenty words. The pattern changed; the machine is still audible.

> Sales fell 12% in the third quarter, which was worse than anyone forecast, though two regional managers had been warning about the pipeline since April.

**A word flagged, then wrongly cut**

> The bridge is central to the plan.

If the bridge genuinely is the load-bearing element, `crucial` was the right word. Rewriting around a flagged term costs precision and buys nothing.

> The bridge is crucial to the plan: without it, the eastern route never opens.

**Confidence hedged away**

> The 1977 recording is arguably considered by many to be among her more notable performances.

Definite statements are a documented feature of human writing, not a machine tell. Machine prose is what hedges these.

> The 1977 recording is the best thing she ever did.

**Manufactured looseness**

> ok so the migration is basically a nightmare lol. anyway we shipped it 🤷

> The migration took nine days instead of two. We shipped it Friday.
