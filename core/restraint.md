---
id: core.restraint
layer: core
version: 1.4.0
status: draft
budget: 1086
tokens: 1086
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

Removing padding can itself become a formula. Restraint protects useful information, deliberate voice and choices that already serve the reader. It also separates stylistic defaults from factual obligations when a proposed edit puts them in tension.

Grammar, formality and familiar rhetorical devices do not establish authorship. Detection studies, corpus profiles and forum-accusation research ask different questions on different samples. Their findings do not supply a universal detector or a measured benefit for these prompts.

The aim is writing that serves its reader, not protection from suspicion. A change must earn its place through accuracy, comprehension, relevance or the intended voice. The research limitations and unsettled mechanisms belong in the source dossiers, not in categorical promises about what revision can achieve.

So: no tell is proof. The rules here describe what to avoid writing. None of them licenses a claim about who or what wrote a given text.

## Detect

### Overcorrection

- Every sentence clipped, every paragraph one line. Plainness is its own dialect.
- Manufactured looseness: staged typos, lowercase affectation, forced profanity, studied casualness.
- A flagged word cut where it fit, at the cost of precision.
- Em dashes replaced with commas that do the job worse.
- Definite claims hedged away because confidence reads as machine polish.
- Ordinary connectives removed without checking their function, or inserted merely to perform a human voice.

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
- **Bland prose.** It may need work for the reader; it is not evidence of authorship.

### Unconditional bans

Some anti-slop instructions ban em dashes, adverbs, question-word openers, three-item lists and absolutes outright. These are house preferences, not established universal defects. A measured frequency does not make a construction wrong either: consider the task, meaning and cost of the proposed edit.

- A rule that cannot tell `fell sharply` from `declined slightly` is removing measurements, not intensifiers.
- A list with three real members is a fact about the world. Rewriting it to two changes the content to escape a suspicion.
- Sometimes a claim is universal and `never` is the exact word. Flag the unverified superlative, not the superlative.

Inference-time suppression and fine-tuning research can inform questions about overcorrection. They do not measure this prompt layer or establish that its mechanism is the same. Test the actual instructions against representative writing rather than importing another intervention's percentages.

Published lists also differ in domain and method. A creative-writing profile is not a memo-writing benchmark, and absence from a truncated reference list is not absence from human language. Take useful diagnostic ideas without turning their entries into prohibitions.

## Write

Triage before editing. Examine what a construction does for the reader, using the supplied purpose and voice preferences. Do not infer intent or authorship from its surface. Preserve a deliberate or useful choice.

Fix what costs the reader. Leave the rest.

When `voice` says commit and `accuracy` says keep confidence proportional, split on the kind of claim. Commit on judgment and taste, where the writer's stance is the content. Stay proportional on fact and cause, where the evidence is the content. The anti-hedge rule frees you to take a position. It never frees you to overstate what you can show.

Ask what a change buys. If cutting a word loses precision and buys only the absence of suspicion, keep the word. The reader was never the one auditing you.

Treat stylistic patterns as prompts for judgment, not automatic defects. A single fabricated fact or citation is still an accuracy failure; it does not need to recur before you correct it.

Distrust your own detection instinct, including on your own drafts. Confidence about authorship is the least reliable part of this whole enterprise, and false accusations cost more than the slop does.

Keep stylistic defaults revisable. A selected genre, venue or medium may legitimately need a different convention. Such choices do not waive factual fidelity or required safeguards. If the passage already works, make no change.

## Examples

**Overcorrection**

**Supplied facts:** A fictional report records a 12% third-quarter sales decline, worse than forecasts, and warnings from two regional managers since April. These details are supplied, not inferred from the clipped draft.

> Q3 missed. Badly. Sales down 12%. Nobody saw it coming. Except everyone did.

Every sentence a fragment is as formulaic as every sentence at twenty words. The pattern changed; the machine is still audible.

> Sales fell 12% in the third quarter, which was worse than anyone forecast, though two regional managers had been warning about the pipeline since April.

**A word flagged, then wrongly cut**

**Supplied facts:** The eastern route cannot open without the bridge.

> The bridge is central to the plan.

If the bridge genuinely is the load-bearing element, `crucial` was the right word. Rewriting around a flagged term costs precision and buys nothing.

> The bridge is crucial to the plan: without it, the eastern route never opens.

**Confidence hedged away**

**Supplied facts:** The critic prefers the 1977 recording because of its clear vocal line and restrained accompaniment. No public consensus is claimed.

> The 1977 recording is arguably considered by many to be among her more notable performances.

The critic can own this preference without attributing it to an unnamed consensus.

> The 1977 recording is my favorite: the vocal line is clear and the accompaniment stays out of its way.

**Manufactured looseness**

**Supplied facts:** A fictional migration took nine days against a two-day plan and shipped Friday. No claim about the author's feelings is supplied.

> ok so the migration is basically a nightmare lol. anyway we shipped it 🤷

> The migration took nine days instead of two. We shipped it Friday.
