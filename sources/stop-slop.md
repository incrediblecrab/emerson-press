---
id: sources.stop-slop
layer: sources
version: 1.3.0
status: active
budget: none
evidence_kind: practitioner
checked_on: 2026-09-08
verification_status: historical
source_version: "SKILL.md, phrases.md, structures.md and examples.md as described in the 2026-08-09 dossier; repository commit not recorded"
source_urls:
  - https://github.com/hardikpandya/stop-slop
verification_note: "This refresh qualifies the retained prompt-file account, not a newly pinned upstream checkout or an efficacy study. Popularity claims, comparative rankings and detection implications are not verified. MIT attribution and historical retrieval metadata are retained."
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

A prompt, not a study. Unbudgeted by design. Its phrase families and review questions are practitioner proposals, much as the community and essay dossiers offer diagnostic ideas rather than empirical authority. The earlier popularity, installation and star-count claims were not version-pinned and are retired; popularity would not establish writing efficacy anyway.

This dossier restates every rule in original wording. Flagged phrases appear as flagged phrases, because a list of banned phrases is a finding rather than prose.

## Why This Source

Two uses, neither of which requires treating it as authoritative.

First, its functional grouping of phrases — throat-clearing, emphasis, meta-commentary and vague declaratives — can reduce repeated rules about the same underlying failure. A statement that something matters needs to explain what matters and why.

Second, it offers a concrete prompt design to compare with reader-oriented editing. Such a comparison still requires an evaluation; this dossier does not report one.

### The repurposing caveat

The retained account describes prescriptive rules, including categorical bans, without a calibrated evaluation or error analysis. It is not a fresh audit of the upstream files. Three consequences follow.

- **A prompt rule is not an empirical result.** Agreement with Wikipedia or another practitioner does not validate it, and disagreement cannot be settled just by counting sources.
- **The bans are unconditional and the tells are not.** `core/restraint.md` exists to prevent exactly the overcorrection this file instructs.
- **Its examples chiefly fit a personal-essay-adjacent tech register.** Transfer to lab reports, briefs and interface labels is not established. A rule that removes necessary precision or structure is inappropriate regardless of genre.

## What It Contains

### The four phrase families

The taxonomy, restated:

- **Throat-clearing openers.** Announcements such as `here's the thing` can delay the point. Start directly when no useful orientation is lost; retain framing that helps the reader follow a task.
- **Emphasis crutches.** `Full stop.` `Period.` `Let that sink in.` `Make no mistake.` `This matters because.` `Here's why that matters.`
- **Meta-commentary.** `The rest of this essay explains`, `Let me walk you through`, `In this section, we'll`, `As we'll see`, `Plot twist:`, `Spoiler:`, `X is a feature, not a bug`.
- **Vague declaratives.** `The reasons are structural.` `The implications are significant.` `The stakes are high.` `The consequences are real.` `This is the deepest problem.`

The last family supplies a useful test: if a sentence announces importance without explaining it, supply the supported consequence or omit the empty assertion. Metacommentary and explicit emphasis can still be useful in teaching, navigation or a sustained argument.

### The business-jargon table

A plain-language substitution table: `navigate` to handle; `unpack` to explain; `lean into` to accept; `landscape` to situation; `game-changer` to significant; `double down` to commit; `deep dive` to analysis; `take a step back` to reconsider; `moving forward` to next; `circle back` to return to; `on the same page` to agreed.

Treat these as candidate explanations, not interchangeable meanings. A word such as `navigate` may be literal in an interface. AP supplies publisher guidance in its own context; it is not an experimental tie-breaker for every stylistic disagreement.

### False agency

An abstract subject can hide who made a decision or performed an action. Ask whether the draft can identify the actual actor and act more clearly. This is an editorial diagnosis, not evidence of why a model chose the construction.

Do not force every inanimate subject into a human-agent sentence. A process can change without a single decision-maker, data can support an inference, and the actor may be unknown. Name an actor when the evidence supports one; never invent one for grammatical neatness.

### Structural patterns

Binary contrast in eleven surface forms (`not X, it's Y`; `the question isn't X, it's Y`; `stops being X and starts being Y`; `not just X but also Y`), negative listing (`Not a X. Not a Y. A Z.`), dramatic fragmentation (`Noun. That's it. That's the thing.`), and rhetorical setups (`What if`, `Think about it:`, `And that's okay.`).

These are review prompts for `core/anti-slop.md`, not additions to a banlist. Retain real contrasts and appropriate reassurance; revise staged profundity or a permission-granting closer only when it contributes nothing useful.

### The scoring rubric

The historical account records five dimensions rated 1-10 — directness, rhythm, trust, authenticity and density — with revision below 35 of 50. Calibration and inter-rater evidence are not documented in this record, so the threshold is not validated here. The dimensions may supply review questions; their scores are not measured writing outcomes.

## Overcorrection Risks in the Recorded Prompt

This section is why the file sits in `sources/` instead of being adopted.

**The em-dash ban.** A categorical ban removes a legitimate punctuation choice. The field-guide essay offers a related caution, not independent experimental validation. Choose punctuation for the intended relationship or pause.

**Kill all adverbs.** No qualification, no exception. `Fell sharply` and `declined slightly` are different facts. A rule that cannot tell an intensifier from a measurement is a word filter, not a style.

**Ban Wh- sentence openers.** The recorded rule rejects openings with `What`, `When`, `Where`, `Which`, `Who`, `Why` or `How`. That excludes many ordinary direct questions and useful introductory clauses, imposing a needless constraint on sentence openings.

**Two items beat three.** A reflexive triad can be empty; a set with three real members should keep all three. Rewriting it to two can change the content to avoid a suspicion.

**Lazy extremes.** `every`, `always`, `never`, `everyone`, `nobody` flagged as false authority. Sometimes the claim is universal and the word is exact. `core/accuracy.md` handles this properly by flagging the *unverified* superlative rather than the superlative.

**No calibrated error account in this record.** This dossier cannot establish the upstream prompt's false-positive rate or prove that it improves writing. Downstream instructions need explicit exceptions for meaningful uses rather than assuming every match warrants a change.

## What `emerson-press` Takes

1. The four-family sort of the phrase inventory, especially **vague declaratives** as a named failure with a usable test.
2. **Agency checks** where an abstract subject conceals a known actor, without inventing an actor.
3. **Structural review questions** about staged contrast and empty reassurance, not new forbidden forms.
4. The **density** question as a review prompt.
5. A reminder that introductory filler can crowd out the action or explanation in a short label or empty state. The overlap with `kill-ai-slop` is a shared practitioner idea, not a second efficacy study.

## What `emerson-press` Refuses

Unconditional bans on ordinary punctuation, adverbs, question openers, three-item lists and supported absolutes. These features are not validated density signals by default. The house rule is to identify what an edit improves and what it might damage; this source establishes neither a detector-evasion benefit nor a prompt-efficacy number.
