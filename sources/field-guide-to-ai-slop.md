---
id: sources.field-guide-to-ai-slop
layer: sources
version: 1.1.0
status: active
budget: none
source:
  title: "The Field Guide to AI Slop"
  subtitle: "And what it's doing to human writing."
  author: "Charlie Guo"
  publisher: "Artificial Ignorance"
  year: 2025
  extent: "~2,600 words"
consumers:
  - core/anti-slop.md
  - core/formatting.md
  - core/restraint.md
  - core/rhythm.md
  - core/voice.md
  - domain/non-fiction.md
  - user-interface/website.md
---

# Source: The Field Guide to AI Slop

Companion evidence to `sources/signs-of-ai-writing.md`. Unbudgeted by design. Where the Wikipedia page is a committee's adversarial checklist, this is one practicing long-form writer's account of what slop feels like from the inside — including what it is doing to his own prose. It supplies three things the Wikipedia page does not: a causal story for why models overproduce lists, the best available treatment of monotony, and the positive prescription that `core/voice.md` is built on.

This dossier restates the piece in original wording throughout. Short flagged phrases appear as flagged phrases, because the phrase is the finding.

## Why This Source

The Wikipedia page tells you what machine text looks like to a reviewer hunting it. This tells you what it feels like to a reader who was not hunting anything — the moment halfway through a paragraph when you realize nothing has been said. That reader's experience is what `core/` is actually trying to prevent, and it is not reducible to a list of tells.

It is also honest about the cost of the whole enterprise in a way the detection literature is not. The author uses these tools himself, is self-conscious about his own em dashes, and argues that the tells are degrading as fast as they are documented.

### Scale

Context for why this matters, as reported in the piece: an SEO firm's data suggested AI-written articles overtook human-written ones during 2024, with the rate later settling near even; a separate ongoing study put roughly seventeen percent of top-20 Google results as machine-generated; workplace surveys put regular AI use at forty percent or more of workers, concentrated in search, ideation, and email.

## The Red Herrings

The author opens with what *not* to treat as evidence. Called yellow flags — worth noticing, never damning alone. This section is the reason `core/restraint.md` cites this source.

- **Elevated vocabulary.** `delve`, `unpack`, `ascertain`, `multifaceted`. Plenty of professionals write this way. A consultant writing `ascertain the root cause` is a consultant.
- **Absence of typos.** Spell-check and Grammarly are ubiquitous. Clean copy stopped being a signal.
- **Absence of contractions.** Often just light editing, or a habit of someone who learned English as a second language.

Note the direct conflict with a naive reading of the Wikipedia vocabulary list. Both sources actually agree: density and co-occurrence are the signal, never a single elevated word. A module must not turn this into a banned-word list.

## Stylistic Tics

### Em dashes

The most belabored tell, and the author treats it with appropriate hedging. His argument for it: outside professional columnists, few people reach for an em dash in daily writing. His evidence is a Reddit analysis of the top thousand posts across several technology and startup subreddits, showing the share of comments containing an em dash roughly tripling over a year — a hard thing to explain by any other cause, though correlation is not causation.

He also predicts vendors will train the habit out, which has since happened. Treat frequency, not presence, and never treat it alone.

### Rhetorical reflexes

Parallelism is a legitimate device. The problem is reflexive deployment where it adds nothing. He groups it with a family of moves that make writing sound profound without saying anything:

- **`It's not X, it's Y`** — the parallelism proper.
- **Snappy triads** — three examples, or three imperative beats in a row, used for cadence rather than because there are three of something.
- **Unearned profundity** — a grave narrative pivot arriving from nowhere. `Something shifted.` `Everything changed.` `But here's the thing.`
- **Mid-sentence questions** — a question mark used as a drum hit. `The solution? It's simpler than you think.` `But now?`
- **Vapid openers and transitions** — `As technology continues to evolve`, `In today's fast-paced world`, `At the end of the day`.

The threshold he states is the useful part: any one instance is forgivable in the right context; repetition is what breaks authenticity.

### Arbitrary formatting

Bold that does not mark emphasis — words are heavy for no recoverable reason. And, more distinctively, Unicode used to fake formatting: mathematical alphanumeric characters standing in for bold or italic, plus decorative Unicode arrows and multiplication signs dropped into running text. He rates the Unicode habit as close to exclusively machine-made.

## Structural Patterns

### Lists and emoji

The causal claim here is this source's most valuable contribution, and it does not appear in the Wikipedia page. Models overproduce bulleted lists because of how their tuning ran: human raters reward answers that look organized, bullets look organized, so raters scored bullet-heavy answers higher and training drove the habit in. The list habit is not a quirk of style. It is a trained preference for the appearance of structure.

That matters for `core/formatting.md`, because it means the pull toward bullets will be strongest exactly when the material is thin — when there is an appearance of organization to manufacture.

Layered on top: emoji-led bullets in professional contexts, which almost no one does unprompted. He observes this more in GPT-4o than in later or earlier models, and rarely in Claude.

### Monotony

The best treatment of rhythm in either source, and the backbone of `core/rhythm.md`.

Machine prose is metrically flat. Sentences run to similar lengths. Paragraphs repeat a shape. The cadence never varies, so there is no emphasis — when every sentence is weighted equally, nothing is weighted. The piece invokes the well-known Gary Provost passage on sentence variety to make the point. That passage is quoted material, so this dossier leaves it where it is; the underlying principle stands on its own and several traditions reach it separately: vary length deliberately, because contrast is what creates stress.

A second observation, rarer and worth keeping: machines hold tense and person fixed with unnatural consistency. Human writers drift between second and third person, slip into first for an aside, shift tense to mark a change in footing. Models settle into one and hold it. This is a rhythm tell that operates above the sentence, and no word list will catch it.

## Uncanny Content

### Generic analogies

Machine metaphors land in the right conceptual neighborhood without being thought through. His generated examples for a ukulele post — fingers taught to dance again, chords as puzzle pieces clicking into place, first strums as a toddler's babble, an instrument as a mirror for learning — are all serviceable and all inert.

The diagnosis is precise and worth carrying into `core/voice.md` intact as a rule: human figures of speech are either **highly specific**, drawn from something the writer actually experienced, or **culturally resonant**, drawn from a shared reference. Machine figures are merely *plausible*. They gesture at meaning without arriving.

This gives an actionable test. For any comparison, ask which of the two sources it draws on. If neither, cut it.

### Filler

He names filler the worst of the tells, and the one least open to measurement. Two experiences:

- Reaching the middle of a piece and being unable to say what the author is claiming. Individual sentences parse; there is no throughline.
- Noticing that four sentences delivered what one sentence held. The other three did not merely add nothing — they diluted the one that mattered.

His summary formulation is the sharpest line in either source and the thing `core/anti-slop.md` should be organized around: **surface polish with nothing underneath is the signature.** A human can write with good grammar and communicate badly, but a human is unlikely to sustain prose that looks and sounds correct right up until it is examined. That specific pairing is the tell.

## Pattern Matching Has Limits

The section that makes this source honest, and that `core/restraint.md` draws on directly.

Good human writers use every device listed above. Prestige long-form journalism was in the training data; the models learned this style *from* that writing. Em dashes, parallelism, rhetorical flourish — none are inherently bad.

The stated difference is intention and rate. A good writer deploys an em dash when that particular pause is wanted. A model scatters them. The device is not the problem; indiscriminate use is.

On detectors, he is blunter than the Wikipedia page: they do not work, they misfire far too often in the false-positive direction, they have flagged students' original work, they have put writers under accusations they did not earn, and on his reckoning they cause more harm than they prevent. He adds that a few minutes of deliberate prompting defeats any of them.

And he notes the recursive problem: documenting these tells feeds them back into the next generation of training, which trains the tells away.

## The Feedback Loop

The framing idea, by way of Churchill on architecture — we shape our buildings, and then they shape us. We built the models on human writing; they learned our rhythms and devices; and now, trying to distinguish ourselves, we are giving up constructions we once used freely, because association with the machines has tainted them.

He gives the concrete cost from his own practice: he now avoids constructions he used freely before, is self-conscious about clunky metaphors, and worries that the tools he uses for ideation and editing leave fingerprints anyway. One commenter reports the same — reaching for commas where an em dash would be better, purely to avoid suspicion.

The conclusion, and the reason `core/restraint.md` is a module rather than a footnote: each turn of this loop narrows the space of writing that reads as authentically human. **Avoidance is itself a style, and it is converging.** A style system that only subtracts makes this worse.

## The Prescription

His stated defense is not stylistic at all, and it is the positive claim that `core/voice.md` is built on.

Do not primarily manage style and structure. **Cultivate specificity.** Write from particular knowledge and tangible experience. Develop a point of view and hold to it. These are what models still fail to imitate convincingly.

This closes the loop with the Wikipedia page's root mechanism. If machine prose fails by trading specific detail for generic approval, then specificity is not one defense among several. It is the only one that cannot be trained around, because it requires having been somewhere.

He closes with the caution that belongs on every module in `core/`: having all the tells does not mean a human did not write it.

## What This Source Adds Beyond Wikipedia

1. **A causal account of the list habit** — preference tuning rewarded the appearance of structure. Predicts bullets will spike where content is thinnest.
2. **Monotony as a first-class failure**, including fixed tense and person, which no lexical check detects.
3. **The specific-or-resonant test for figurative language**, which turns a vague instinct about bad metaphors into something checkable.
4. **"Surface polish with nothing underneath"** as the unifying definition of slop.
5. **The convergence argument** — avoidance is a style, and mere subtraction accelerates the problem it is trying to escape.
6. **A stronger red-herring list** than the detection literature, from someone who bears the cost of false positives.
