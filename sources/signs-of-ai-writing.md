---
id: sources.signs-of-ai-writing
layer: sources
version: 1.5.0
status: active
budget: none
evidence_kind: community
checked_on: 2026-09-08
verification_status: historical
source_version: "Dossier's recorded Wikipedia page pass of 2026-08-23, following retrieval on 2026-08-09; no immutable revision ID was retained"
source_urls:
  - https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
verification_note: "This refresh reassesses the inherited community observations and their limits; it does not certify the live page, every linked study, historical counts or detector performance. Model-era labels are unpinned historical reports. Editorial diagnostics are not authorship tests or independently validated prompt interventions."
source:
  title: "Wikipedia:Signs of AI writing"
  url: "https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing"
  publisher: "Wikimedia Foundation / Wikipedia contributors"
  year: 2026
  extent: "1,665 lines of wikitext at retrieval, August 9, 2026; ~60 named tells"
  license: "CC BY-SA 4.0"
  license_url: "https://creativecommons.org/licenses/by-sa/4.0/"
  modified: "Restated and reorganized. Term lists are adapted from the source's
    selection; this note is Adapted Material under CC BY-SA 4.0 and is offered
    under the same license."
consumers:
  - core/accuracy.md
  - core/anti-slop.md
  - core/formatting.md
  - core/restraint.md
  - core/rhythm.md
  - core/voice.md
  - domain/non-fiction.md
---

# Source: Wikipedia — Signs of AI Writing

Evidence base for `core/anti-slop.md` and, secondarily, for every other module in `core/`. Unbudgeted by design: nothing here is loaded into a prompt alongside a draft. This is what you read when you author or revise a core module, so the module itself can stay short and still be defensible.

This dossier uses original restatements and selected phrase examples, not source-text transcription. The examples illustrate the community taxonomy rather than measured prohibitions. Wikipedia's internal shortcuts (`WP:AIVOCAB`, `WP:SUPERFICIAL`, `WP:AICONNECT`) appear as-is because they are identifiers.

The previous dossier recorded a page check on August 23, 2026. Its revision ID was not preserved. That date describes the historical reading, not current coverage; this September refresh corrects the interpretation without claiming a new live-page audit.

## Why This Source

This is a community-maintained catalog of observations, examples, linked research and cautions from Wikipedia editing. It is useful for generating review questions, especially where unsupported claims or assistant artifacts enter encyclopedia prose. A community example or repeated practitioner observation is not itself an independently verified experiment.

Its false-positive cautions matter as much as its pattern inventory. Judge an edit by the reader-facing problem it fixes; agreement with another anti-slop checklist does not establish empirical authority.

### The repurposing caveat

The page concerns suspected AI writing in Wikipedia's editing context. `emerson-press` takes candidate editorial checks, not an authorship classifier or a specification to avoid every listed form.

- A detection tell is not automatically a writing rule. Some tells are about provenance artifacts (`utm_source=chatgpt.com`, unfilled placeholder dates) and belong to `core/accuracy.md` as hygiene, not to voice.
- Wikipedia's house register is encyclopedic and deliberately flat. Some of what it flags as promotional would be fine in an essay. Read the mechanism, not the verdict, and let the `domain/` module decide register.
- The page and the models change. The former revision-count extrapolation was not a version pin and is retired. A future update needs an identifiable page revision and separately checked primary support for empirical claims.

## The Governing Caveat

Take this before anything else, because it constrains how every tell below may be used.

Detection performance depends on the model, population, task, class balance and decision threshold. The studies linked by the historical page were not independently re-audited here, so no detector or human-accuracy benchmark is carried as currently verified.

The former inference from **90% overall accuracy to a 10% false-accusation rate was invalid**. Overall accuracy combines correct decisions across classes. A false-positive rate needs the number of human texts wrongly flagged divided by all human texts; the fraction of accusations that are false has yet another denominator. Neither follows from overall accuracy without the confusion matrix and relevant population.

Human imitation, editing practices and model changes can further shift the comparison. **Use these observations to inspect meaning and usefulness, never to accuse an author.** Even a cluster of stylistic cues does not justify deleting sound prose. A useful module says what to check and when to retain a construction, not merely what words to ban.

## A Useful Diagnosis, Not a Single Proven Cause

Language-model generation depends on training, post-training, prompts, retrieved context and decoding choices; it is not invariably greedy selection of the likeliest continuation. This community page does not establish that one mechanism explains all the patterns below. See `ai-slop-research.md` for scoped lexical research, including the mixed causal evidence about RLHF.

The transferable editorial diagnosis is that a revision can become **less specific and more exaggerated at the same time**. For example, replacing a verifiable description of an invention with general praise loses information while overstating importance. That failure can occur in human or generated prose.

Test for lost information and unsupported evaluation. Do not turn that test into a theory of all models, a guarantee that specificity defeats detection, or an inventory of forbidden vocabulary.

## Content Tells

### Inflated significance, legacy, and broader trends

A useful content check: does the draft attach importance to an ordinary fact without evidence? No comparative reliability ranking was verified for this refresh.

Flagged constructions: `stands as`, `serves as`, `is a testament to`, `is a reminder of`, `played a crucial/pivotal/vital/significant/key role`, `a key moment`, `underscores its importance`, `highlights its significance`, `reflects broader`, `symbolizing its ongoing/enduring/lasting`, `contributing to the`, `setting the stage for`, `marking a shift`, `represents a shift`, `key turning point`, `evolving landscape`, `focal point`, `indelible mark`, `deeply rooted`.

Behaviors described in the historical page account, not universal model properties:

- It fires on genuinely mundane subjects — etymology sections, population figures, a bus route.
- It sometimes hedges first and then does it anyway, conceding that a subject is minor before explaining its broader significance.
- It invents participation in discourse, dropping a subject into "debates" or crediting it with joining a public discussion.
- In biology writing it inflates ecosystem connection and dwells on conservation status and preservation efforts even when the status is unknown and no efforts exist.

### Promotional and advertisement-like language

Register drifts toward travel brochure or press release even when the prompt asked for neutral prose, and even when the writer had no promotional intent. It can happen while purportedly removing promotional tone.

Flagged: `boasts a`, `vibrant`, `rich`, `profound`, `enhancing`, `showcasing`, `exemplifies`, `commitment to`, `natural beauty`, `nestled`, `in the heart of`, `groundbreaking`, `renowned`, `featuring`, `diverse array`.

The inherited page account distinguished conspicuous superlatives in some older output from subtler positivity in some later output, including heritage topics. These are model-era observations, not a verified description of every newer system.

### Superficial analysis

A structural check rather than a lexical one: an appended interpretive flourish, including a trailing participial clause, can make a factual sentence appear analyzed without adding an explanation.

Flagged endings: `highlighting ...`, `underscoring ...`, `emphasizing ...`, `ensuring ...`, `reflecting ...`, `symbolizing ...`, `contributing to ...`, `cultivating ...`, `fostering ...`, `encompassing ...`, `enhancing ...`, `valuable insights`, `align with`, `resonate with`.

A retrieved source can be wrongly credited with an interpretation it does not support. Verify that the cited source actually makes the attributed point; retrieval alone does not guarantee entailment.

The test that generalizes: delete the trailing participial clause. If nothing was lost, it was ornament. This belongs in `core/anti-slop.md` as a procedure, not as a word list, because the procedure survives vocabulary drift.

### Vague attribution and overgeneralized opinion

Check for a claim attached to an unnamed authority or attributed to more people than the sourcing establishes.

Flagged: `industry reports`, `observers have cited`, `experts argue`, `some critics argue`, `several sources`, `several publications`, and `such as` placed before a list that is in fact exhaustive.

The distinct failures: presenting one source's view as consensus; referring to `reviewers` or `scholars` in the plural while citing one; implying a list is open-ended when the source gives no reason to think so. That last one is subtle and worth carrying into `core/accuracy.md`.

### Canned emphasis on notability, attribution, and media coverage

The historical page account describes encyclopedia-style drafts cataloging coverage and outlet prestige instead of explaining the subject. Its attribution to some 2025-era output is not a current cross-model prevalence finding.

Flagged: `independent coverage`, `local/regional/national media outlets`, `trade publications`, `music/business/tech outlets`, `profiled in`, `written by a leading expert`, `active social media presence`.

The `maintains an active social media presence` formula may be empty when no relevant activity is described. It is not near-proof of authorship. Likewise, reciting a platform's notability criteria is no substitute for supplying relevant sourced facts.

### Outline-like conclusions about challenges and prospects

A rigid closing formula: a `Challenges` section opening with a concession built on praise, then either a vague reassurance or speculation about what future initiatives might accomplish. Often paired with a `Future Prospects` or `Future Outlook` section.

Flagged: `Despite its ..., X faces several challenges`, `Despite these challenges`, `Challenges and Legacy`, `Future Outlook`.

The tell is the formula, not the topic. Writing about real difficulties is fine. Reaching for this shape to manufacture a conclusion is not.

### Leads that treat a descriptive title as a proper noun

When the title is a description rather than a name, the opening sentence defines the title as though it were a thing in the world — `refers to`, `is the chronological list of`, `is a curated compilation of`. The underlying error is writing about the label instead of the subject.

### Section headings of the form "X and Y"

The historical account flags headings such as `Awards and recognition`. No prevalence estimate or authorship accuracy was verified here; this is an ordinary heading form.

The useful question is whether the section contains substantive information or only gestures at prestige and coverage.

For `core/formatting.md`: a heading should name what is under it. Two related nouns can accurately label a useful section; split or rename it only if its contents warrant that change.

## Language and Grammar Tells

### High density of AI vocabulary

The historical page cataloged recurring vocabulary. Co-occurrence may warrant closer reading, but this dossier establishes neither a validated density threshold nor a strongest lexical signal.

The historical pooled inventory included `delve`, abstract uses of `landscape` and `tapestry`, and evaluative uses of `pivotal`, `robust` and `vibrant`. These are examples, not a word-ban list; many uses are ordinary and precise.

The earlier dossier assigned examples to 2023-24, 2024-25 and 2025-26 periods and included Grok-specific scientific diction. Without model snapshots, prompts and comparison corpora, these remain historical observations, not a current vocabulary classifier. Scientific terms can be exactly right in scientific prose.

Two constraints the source states explicitly and that a module must honor. Read the list literally: a word being overused does not implicate its synonyms. And context governs — `underscore` as a typographic mark or as film music is not the tell.

### Avoidance of basic copulatives

The page describes copyedits that replace `is` and `are` with weightier substitutes. The earlier precise claim about an academic-writing decline was not independently verified in this refresh and is retired as quantitative support.

Flagged substitutes: `serves as`, `stands as`, `marks`, `functions as`, `operates as`, `represents`, `boasts`, `features`, `maintains`, `offers`, `refers to`.

Some substitutions may pad a relation that `is` or `has` expresses adequately. Others add real meaning: beginning a career is not identical to holding a role. Compare the actual claim before simplifying, and do not treat the historical copyediting examples as a statement about all newer output.

For `core/voice.md` this inverts cleanly into a positive rule: let the verb be `is` when the relation is `is`.

### Vague expression of connection or association

Shortcuts `WP:AICONNECT` and `WP:AIASSOCIATION`. Words to watch: `in connection with`, `in connection to`, `connected with`, `connected to`, `in association with`, `associated with`.

An indirect construction can obscure a known relationship. Where the evidence permits, name the relation with a precise verb or preposition, such as `working with`, `used for` or `funded by`. Neither indirection alone nor its co-occurrence with promotional language proves authorship.

For `core/anti-slop.md` the rule states cleanly and needs no detection framing: when two things are related, name the relation. Ownership, employment, funding, authorship, membership, cause — each of those has a word, and once you have picked one, `of`, `for` or `by` will usually carry it.

The exception is not decoration, and any module taking this rule must carry it. Sometimes an unexplained association is exactly the finding. An epidemiologist writing that a diet is `associated with` an outcome has chosen the precise phrase, because the direction of causation is unknown and asserting one would be false. There the vague-looking construction is the accurate one and `core/accuracy.md` requires it. The fault is the phrase standing where a nameable relation belongs, not the phrase itself. Banned outright, the rule would trade a vague sentence for a false one, which is the failure `core/restraint.md` exists to prevent.

The earlier dossier recorded this as a newer-model observation while elegant variation was reclassified as historical. Without pinned comparisons, that page change establishes neither a causal explanation nor a universal change in model behavior.

### Negative parallelism

Three shapes, all common, all stereotyped:

- `not just X, but Y` / `not only X but also Y` / `it's not just X, it's Y`
- `not X, but Y` / `it's not X, it's Y` / `no X, no Y, just Z`
- `X rather than Y` — a contrast that may be precise or misleading depending on the facts. The historical Grok frequency observation does not make the form a fault.

These forms can stage an unnecessary correction and manufacture the appearance of insight. They can also express a real correction, contrast or addition. Inspect the claim, including across sentence boundaries, rather than rejecting its grammatical shape.

Human writers use these forms, including in myth-busting and technical contrasts. Review repetitive use for its effect on meaning, not as an authorship signal.

### Rule of three

A reflexive triad can make a thin account sound complete, from stacked adjectives to parallel phrases. Check whether each item contributes. A set with three real members is not a defect, and reducing it to two can change the facts.

## Style and Markup Tells

These are historical review prompts for `core/formatting.md`, not universal defects. Wikipedia's page conventions do not automatically govern Markdown, a slide deck or an accessible application.

- **Title Case In Headings.** Capitalizing every significant word in section headings.
- **Boldface as emphasis spray.** Check whether highlighted terms actually help a reader find important information.
- **Inline-header vertical lists.** The signature shape: bullet, bold label, colon, explanatory sentence. Often with a non-standard bullet character (`•`, `-`, `–`, `#`, an emoji) or hand-numbered items.
- **Em dashes.** Check whether the pause or interruption serves the sentence. The prior model-ranking and vendor-suppression claims were not independently verified here. Presence, spacing or a cluster of dashes is not an authorship test.
- **Emoji as structure.** Emoji prefixed to headings or bullets.
- **Needless small tables** for material that should be prose.
- **Curly quotes and apostrophes**, sometimes mixed inconsistently with straight ones in a single passage. Weak on its own — Chicago style, Word, and macOS all produce them.
- **Skipped heading levels**, typically starting at level three.
- **Heading hierarchy.** Follow the destination's structure; level 1 is not universally forbidden in a document body.
- **A duplicate title heading.** Remove it if the publishing system already supplies the title; a standalone document may need one.
- **Headings that contain only other headings.** Check for missing explanation, but do not add filler to a useful hierarchical outline.
- **Thematic breaks between sections**, a Markdown habit.

## Chat-Register Leakage

Assistant-to-user speech can be the wrong register for a finished article. It is not unambiguous authorship evidence: it can be quoted, copied, templated or deliberately addressed to a reader.

- **Collaborative filler** — `I hope this helps`, `Of course!`, `Certainly!`, `You're absolutely right!`, `Would you like ...`, `is there anything else`, `let me know`, `more detailed breakdown`, `here is a ...`.
- **Meta-narration of structure** — announcing what a section will do before doing it.
- **Placeholder text** left unfilled: bracketed slots, `2025-xx-xx` dates.
- **Over-itemized change descriptions.** In an ordinary summary, explain what changed and why instead of inventorying every field visited. Retain exact parameters or markup when a changelog, audit or technical handoff needs them; granularity does not identify an author.

## Knowledge-Gap Speculation

Important enough to separate, and easy to underweight. When a model cannot find something, it frequently says so *and then speculates anyway*.

Flagged: `as of my last knowledge update`, `up to my last training update`, `while specific details are limited`, `not widely documented`, `not extensively documented in readily available sources`, `in the provided search results`, `based on available information`.

Two failures compound here. The claim that something is undocumented is itself unverified — often the model simply did not find it. And the speculation that follows, hedged with `likely`, is presented as informative content. For people this collapses into a stock formula: the subject `maintains a low profile` or `keeps personal details private`.

For `core/accuracy.md`: report absence of evidence as a failed search, say where you looked, and do not follow it with a guess dressed as a finding.

## Citation Tells

For `core/accuracy.md`.

- **Dead links on arrival.** Investigate broken URLs and missing archive records; a moved page, access barrier or incomplete archive can explain a failed lookup. Absence from an archive does not prove fabrication.
- **Invalid ISBN checksums and unresolvable DOIs.**
- **Valid DOIs pointing at unrelated papers.** Resolution can conceal an identity or relevance error; inspect the actual paper instead of stopping at a successful lookup.
- **Missing or inaccurate locators.** Check the cited passage in the cited edition. Whole-work references can legitimately lack a page, and unpaginated works may have other locators. Neither a missing page nor a missing URL makes a reference inherently unfalsifiable. See `citation-authority.md` for mechanics and unresolved style-specific rules.
- **Provenance parameters in URLs** — `utm_source=chatgpt.com`, `utm_source=openai`, `utm_source=copilot.com`, `referrer=grok.com`.
- **Reference-syntax errors** — named references defined but never cited, reused references with broken syntax, the `↩` character around footnotes.
- **Unrendered tool markers.** Fragments such as `contentReference`, `oaicite` or `turn0search0` may need conversion into usable references. Product syntax changes, and a person can copy it; repair the artifact without inferring authorship of the whole document.

Verify both bibliographic identity and support for the claim. A resolving DOI can identify the wrong paper; a valid citation may require a library or a different edition to check. Report the verification limit instead of either certifying or accusing from appearance.

## Historical Tells

Patterns recorded as historical by the earlier page pass, not certified absent from current models.

**Model-era observations need version pins.** Training, instructions, task and decoding can all change output. A page's decision to reclassify an indicator is not an experiment isolating which cause changed, and structural patterns are not immune to model or genre differences.

- **Didactic disclaimers** — `it's important to note`, `it's crucial to note`, `worth noting`, `may vary`. Advice to an imagined reader about safety or jurisdiction.
- **Section summaries** — `In summary`, `In conclusion`, `Overall`, plus restating the paragraph's point at its end.
- **Procedural self-narration in a change note** — announcing that information was `preserved`, `retained`, or that mistakes were `avoided`, and similar statements about the process rather than the result.
- **Abrupt truncation** at a token limit.
- **Stale default access dates** in citations.
- **Prompt refusals** — formulaic statements about being an AI or offering a nearby alternative. Their prevalence depends on the product and task; no current rate was verified here.
- **Elegant variation.** The previous dossier recorded upstream reclassification on August 19, 2026; the exact page revision remains unpinned. Repeatedly renaming one referent can confuse a reader, but it also has a long human history, including learned writing practices. No universal current-model prevalence or false-positive rate is established here.

**Decoding is a possible contributor, not the only mechanism.** Some repetition penalties can discourage reuse of tokens and encourage alternatives. This does not show that every older model used such a penalty, that all current models omit it, or that prompts and learned style cannot produce synonym variation without it. The earlier categorical causal story is withdrawn.

For module authors, keep the two judgments separate: preserve stable terms where reference would otherwise become unclear, and do not use synonym variation to determine authorship.

A conclusion or summary can help readers. Revise it when it merely repeats material without a useful synthesis, not because a particular transition appears.

## Bias in Generated Content

The historical dossier repeated August 2026 press coverage about political bias, including Stu Woo in the *Wall Street Journal* and a *Fortune* report. The underlying experiments, specific language comparisons and proposed causes were not independently verified here; they are not carried as established model-wide findings.

The house application is narrower: check whether political claims are supported and fairly contextualized, including in translation. A citation's existence does not establish the interpretation attached to it. The community account is not authority for a predetermined conclusion about a government or a model.

## Ordinary Constructions Worth Preserving

The page's inverse list supplies useful reminders for `core/voice.md`, not a human-authorship test:

- **Plain copulatives** — `there is a`, `it has a`.
- **Short plain verbs over stiff or euphemistic ones** — `wrote` over `authored`, `moved` over `relocated`, `used` over `utilized`, `tried` over `attempted`, `died` over `passed away`.
- **Definite and superlative statements** when the evidence supports their scope. Neither unnecessary hedging nor unjustified certainty improves accuracy.
- **Hedges and intensifiers used naturally** — `very`, `perhaps`, `tends to`.
- **Ordinary wordy connectives in isolation** — `as a result of`, `in order to`, `all of the`, `a part of`, `the fact that`.

Keep a hedge when it states real uncertainty and a connective when it clarifies a relationship. Their presence or removal does not establish whether prose is human or generated.

## Non-Tells

These features have ordinary human uses and are not adequate grounds for an authorship conclusion:

- **Perfect grammar.** Many humans write cleanly.
- **Mixed casual and formal register.** Can reflect context, voice or collaborative editing; it does not establish a writer's identity or background.
- **Bland or robotic prose.** Dullness is a quality judgment, not evidence of a particular production method.
- **Fancy, academic, or formal prose.** A genre or learned register is not a machine fingerprint.
- **Transition words in isolation.** A connective can clarify an argument; its use is not an authorship test.
- **Unsourced content.** Has a long pre-model history. Generated writing can have references or lack them; check the actual sourcing.

The community account warns that false accusations can harm participation. Retain that caution without diagnosing an individual accuser or claiming a measured harm rate.

## What This Means for `core/`

1. **Check information, not just vocabulary.** Restore supported detail and remove unsupported evaluation.
2. **Try deletion-testing trailing clauses.** Keep them when they add a real consequence, qualification or explanation. This is an editorial procedure, not a measured best-performing prompt.
3. **Preserve legitimate variation.** Ordinary punctuation, formality, repetition and uncertainty can serve the reader.
4. **Choose formatting for the task and destination.** A checklist is not a reason to remove useful headings, emphasis, lists or accessible structure.
5. **Accuracy owns citation and knowledge-gap checks.** Distinguish a failed lookup from source absence, and an unchecked claim from a disproven one.
6. **Do not claim detection or prompt efficacy.** State the reader-facing reason for an edit and the conditions for retaining the original.

## Chunk Map

The earlier dossier records an external working extraction split by section. This map is historical provenance only; the extraction and its counts were not revalidated in this refresh.

These ranges index the historical extraction, not an immutable Wikipedia revision. Their former label as source lines was incorrect. They are not primary citation locators, and no current empirical claim rests on them.

| Chunk | Section | Extraction lines |
| --- | --- | --- |
| `00-lead` | Lead, scope | 1-86 |
| `01-caveats` | Detector and human reliability | 87-106 |
| `02-content` | Significance, puffery, superficial analysis, weasels | 107-253 |
| `03-language-and-grammar` | Vocabulary, copulatives, parallelism, triads | 254-370 |
| `04-style` | Title case, bold, lists, dashes, emoji, quotes | 371-522 |
| `05-communication-to-user` | Chat leakage, cutoff disclaimers, placeholders | 523-606 |
| `06-markup` | Markdown artifacts, citation markers | 607-782 |
| `07-citations` | Dead links, bad DOIs, missing pages, UTM params | 783-869 |
| `08-comment-specific` | Discussion-page tells | 870-897 |
| `09-edit-summaries` | Edit-summary tells | 898-958 |
| `10-miscellaneous` | Style shifts, canned pages, model differences | 959-1032 |
| `11-signs-of-human-writing` | Inverse list | 1033-1051 |
| `12-ineffective-indicators` | Non-tells | 1052-1062 |
| `13-historical-indicators` | Deprecated tells | 1063-1111 |
| `14-back-matter` | References | 1112-1179 |
