---
id: sources.stop-slop
layer: sources
version: 1.2.0
status: active
budget: none
source:
  title: "stop-slop"
  subtitle: "A skill file for removing AI tells from prose."
  author: "Hardik Pandya"
  publisher: "GitHub"
  year: 2026
  extent: "SKILL.md plus phrases.md, structures.md, examples.md"
  license: "MIT"
  url: "https://github.com/hardikpandya/stop-slop"
  retrieved: 2026-08-09
consumers:
  - core/anti-slop.md
  - core/restraint.md
  - core/rhythm.md
  - core/voice.md
  - user-interface/applications.md
  - user-interface/website.md
---

# Source: stop-slop

A prompt, not a study. Unbudgeted by design, and read differently from the other sources in this directory: `signs-of-ai-writing.md` and `field-guide-to-ai-slop.md` are evidence, and this is a competitor. It is the most widely installed artifact of its kind — more than sixteen thousand stars since its release in January 2026 — which makes it, in practice, the default anti-slop instruction running inside a large number of other people's drafts.

This dossier restates every rule in original wording. Flagged phrases appear as flagged phrases, because a list of banned phrases is a finding rather than prose.

## Why This Source

Two reasons, and neither is that it is right.

First, coverage. Its phrase inventory is the best-organized public list of the 2025-26 chat-register tells, sorted by the job the phrase is doing — throat-clearing, emphasis crutch, meta-commentary, vague declarative — rather than alphabetically. That sorting is the useful part. `The implications are significant` and `The stakes are high` are one failure, not two, and the list says so.

Second, it is what `emerson-press` gets compared against. Anyone evaluating this repository has probably run that one. The differences need to be deliberate and defensible rather than accidental.

### The repurposing caveat

This is a prescriptive instruction file with no citations, no error analysis, and no false-positive discussion. Every rule is stated as absolute. Three consequences follow.

- **No rule here is evidence for anything.** It is one writer's taste, formalized. Where it agrees with `signs-of-ai-writing.md`, the citation goes to that page. Where it disagrees, it loses.
- **The bans are unconditional and the tells are not.** `core/restraint.md` exists to prevent exactly the overcorrection this file instructs.
- **It is tuned for one genre** — the personal-essay-adjacent tech blog post. Applied to a lab report, a brief, or a button label, several of its rules produce worse writing.

## What It Contains

### The four phrase families

The taxonomy, restated:

- **Throat-clearing openers.** Any `here's what / here's this / here's the thing` construction, plus `The uncomfortable truth is`, `It turns out`, `Let me be clear`, `The truth is`, `I'm going to be honest`, `Can we talk about`. The stated rule is the good one: any `here's what` construction is an announcement standing where the point should be.
- **Emphasis crutches.** `Full stop.` `Period.` `Let that sink in.` `Make no mistake.` `This matters because.` `Here's why that matters.`
- **Meta-commentary.** `The rest of this essay explains`, `Let me walk you through`, `In this section, we'll`, `As we'll see`, `Plot twist:`, `Spoiler:`, `X is a feature, not a bug`.
- **Vague declaratives.** `The reasons are structural.` `The implications are significant.` `The stakes are high.` `The consequences are real.` `This is the deepest problem.`

The last family is the sharpest contribution, and its test is worth keeping: if a sentence announces that something is important, deep, or structural without naming the specific thing, delete it or replace it with the specific thing.

### The business-jargon table

A plain-language substitution table: `navigate` to handle; `unpack` to explain; `lean into` to accept; `landscape` to situation; `game-changer` to significant; `double down` to commit; `deep dive` to analysis; `take a step back` to reconsider; `moving forward` to next; `circle back` to return to; `on the same page` to agreed.

This is the move AP's plain-language table already makes, and it duplicates it. Where the two disagree, AP is the citation.

### False agency

The best section, and the one with no equivalent in the other sources. The claim: models give inanimate things human verbs because it lets them avoid naming an actor. The worked list — a complaint becomes a fix, the decision emerges, the culture shifts, the conversation moves toward, the data tells us, the market rewards — is a genuine diagnostic. Somebody fixed it. Somebody decided. Somebody read the data.

`core/voice.md` already says *name the actor and the act*. This supplies the grammatical signature of failing to.

### Structural patterns

Binary contrast in eleven surface forms (`not X, it's Y`; `the question isn't X, it's Y`; `stops being X and starts being Y`; `not just X but also Y`), negative listing (`Not a X. Not a Y. A Z.`), dramatic fragmentation (`Noun. That's it. That's the thing.`), and rhetorical setups (`What if`, `Think about it:`, `And that's okay.`).

`core/anti-slop.md` already carries negative parallelism and triads. The additions worth taking are negative listing and the `And that's okay` permission-granting closer.

### The scoring rubric

Five dimensions rated 1-10 — directness, rhythm, trust, authenticity, density — with revision required below 35 of 50. There is no calibration behind the numbers and no inter-rater evidence, so the threshold is arbitrary. The dimensions are a reasonable review checklist, and `density` — is anything cuttable — is the one that does the most work.

## Where It Is Wrong

This section is why the file sits in `sources/` instead of being adopted.

**The em-dash ban.** Stated as `No em dashes at all.` This is the position `sources/field-guide-to-ai-slop.md` argues against with data — frequency is the signal, presence is not — and the position `core/restraint.md` exists to refuse. The author does not hold it either: his own fourth worked example offers `Speed, quality, cost—pick two` as the improved version. A rule the author cannot follow inside his own example is not a rule.

**Kill all adverbs.** No qualification, no exception. `Fell sharply` and `declined slightly` are different facts. A rule that cannot tell an intensifier from a measurement is a word filter, not a style.

**Ban Wh- sentence openers.** `What`, `When`, `Where`, `Which`, `Who`, `Why`, `How` — restructure any sentence starting with one. That removes every direct question and most fronted subordinate clauses from the language, which imposes uniformity in order to escape uniformity. `core/rhythm.md` asks for the opposite: vary the opening.

**Two items beat three.** A triad deployed reflexively is a tell. A list with three members in it is a fact about the world. Rewriting to two changes the content to avoid a suspicion.

**Lazy extremes.** `every`, `always`, `never`, `everyone`, `nobody` flagged as false authority. Sometimes the claim is universal and the word is exact. `core/accuracy.md` handles this properly by flagging the *unverified* superlative rather than the superlative.

**No false positives anywhere.** There is no equivalent of the Wikipedia page's ineffective-indicators list, and no account of what the rules cost when misapplied. That absence is what turns a style guide into a filter.

## What `emerson-press` Takes

1. The four-family sort of the phrase inventory, especially **vague declaratives** as a named failure with a usable test.
2. **False agency** as the grammatical signature of a missing actor. Sharpens `core/voice.md`.
3. **Negative listing** and the `And that's okay` closer, as additions to `core/anti-slop.md`.
4. The **density** question as a review prompt.
5. Its marketing-voice overlap with `kill-ai-slop`, which feeds `user-interface/website.md`. On a button or an empty state, a throat-clearing opener is not merely tiresome; it is most of the available space.

## What `emerson-press` Refuses

Every unconditional ban: em dashes, all adverbs, Wh- openers, three-item lists, absolutes. Each is a density signal misread as a binary. Adopting them produces the failure `core/restraint.md` describes — the pattern changes, the machine is still audible, and the prose is now worse in a second way.
