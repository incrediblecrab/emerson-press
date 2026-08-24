---
id: sources.signs-of-ai-writing
layer: sources
version: 1.4.0
status: active
budget: none
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

This dossier restates every rule and observation in original wording. The bracketed term lists appear as lists, because a list of flagged words is a finding rather than prose. Wikipedia's internal shortcuts (`WP:AIVOCAB`, `WP:SUPERFICIAL`, `WP:AICONNECT`) appear as-is because they are identifiers.

Checked against the live page on August 23, 2026, and brought current: one tell moved to `## Historical Tells`, one restored there that had been carried as live, seven sections added, three headings re-titled.

## Why This Source

Almost everything written about "AI writing style" is either marketing or vibes. This page is neither. It is a maintained, adversarial, heavily cited field record kept by people who read suspected machine text all day and who are accountable to each other for false positives. It names roughly sixty distinct tells, dates them by model era, links each to the study or the diff that established it, and — crucially — keeps a list of the tells that turned out not to work.

That last part is what makes it usable. A source that only tells you what AI writing looks like will push you into overcorrection. This one tells you where the evidence is thin, which is what lets `core/restraint.md` exist at all.

### The repurposing caveat

The page exists to help Wikipedia editors *detect* machine text so they can remove it. `emerson-press` uses it backwards: as a specification of what to not-write. Two consequences follow.

- A detection tell is not automatically a writing rule. Some tells are about provenance artifacts (`utm_source=chatgpt.com`, unfilled placeholder dates) and belong to `core/accuracy.md` as hygiene, not to voice.
- Wikipedia's house register is encyclopedic and deliberately flat. Some of what it flags as promotional would be fine in an essay. Read the mechanism, not the verdict, and let the `domain/` module decide register.
- The page moves faster than a dossier does. It took 78 revisions in the fourteen days to August 23, 2026 — about six a day, so roughly 170 between monthly passes. Two of the tells below have already changed tense once. Re-read the live section index before trusting any tense in this file, and treat a month-old pass as stale rather than merely dated.

## The Governing Caveat

Take this before anything else, because it constrains how every tell below may be used.

Detection does not work well. Automated detectors beat chance but carry error rates too high to act on, and they are defeated by paraphrase, by markup changes, and by models they were not trained against. Humans are worse: a 2025 study put untrained human discrimination at roughly chance. Heavy LLM users reach about ninety percent, which still means one false accusation in ten.

Two further complications. Human prose is drifting toward machine prose through ordinary exposure, measurably so since 2024, including in speech. And writers now actively edit around these tells to avoid suspicion, which corrupts the signal further.

The operational conclusion for `emerson-press`: **the tells are a guide to what to avoid writing, never a test to apply to finished text.** A module may say "do not write X." No module may say "text containing X was machine-made." This is the whole justification for `core/restraint.md`.

## The Root Mechanism

Everything downstream follows from one property. A language model predicts the likeliest continuation, so it regresses to the mean of its training data. Specific, rare, load-bearing facts are statistically uncommon; generic approving description is statistically everywhere. So the specific gets swapped for the general, and — because the training corpus describes notable subjects in flattering terms — the general arrives pre-inflated.

Wikipedia's formulation of the net effect is the single most useful idea in the document: the subject becomes **less specific and more exaggerated at the same time**. Volume rises as resolution drops. An inventor of one particular coupling mechanism becomes a titan of industry.

This is why anti-slop cannot be a banned-word list. The words are symptoms. The disease is the trade of detail for approval, and it will simply route around any list of forbidden vocabulary. Every rule in `core/anti-slop.md` should be traceable to this mechanism.

## Content Tells

### Inflated significance, legacy, and broader trends

The most reliable content tell. The model attaches claims about importance to material that does not carry any, situating an ordinary fact inside a sweeping arc.

Flagged constructions: `stands as`, `serves as`, `is a testament to`, `is a reminder of`, `played a crucial/pivotal/vital/significant/key role`, `a key moment`, `underscores its importance`, `highlights its significance`, `reflects broader`, `symbolizing its ongoing/enduring/lasting`, `contributing to the`, `setting the stage for`, `marking a shift`, `represents a shift`, `key turning point`, `evolving landscape`, `focal point`, `indelible mark`, `deeply rooted`.

Characteristic behaviors worth knowing beyond the word list:

- It fires on genuinely mundane subjects — etymology sections, population figures, a bus route.
- It sometimes hedges first and then does it anyway, conceding that a subject is minor before explaining its broader significance.
- It invents participation in discourse, dropping a subject into "debates" or crediting it with joining a public discussion.
- In biology writing it inflates ecosystem connection and dwells on conservation status and preservation efforts even when the status is unknown and no efforts exist.

### Promotional and advertisement-like language

Register drifts toward travel brochure or press release even when the prompt asked for neutral prose, and even when the writer had no promotional intent. It can happen while purportedly removing promotional tone.

Flagged: `boasts a`, `vibrant`, `rich`, `profound`, `enhancing`, `showcasing`, `exemplifies`, `commitment to`, `natural beauty`, `nestled`, `in the heart of`, `groundbreaking`, `renowned`, `featuring`, `diverse array`.

Two era notes: older models were flatly superlative, newer ones are subtly positive and avoid obvious words like `best`, which makes the tell harder but not absent. And anything the model can construe as cultural heritage triggers repeated reminders of its importance.

### Superficial analysis

A structural tell rather than a lexical one, and the one most worth teaching. The model appends an interpretive flourish to a factual sentence, usually as a trailing present participle, so a fact looks analyzed when the sentence has only complimented it.

Flagged endings: `highlighting ...`, `underscoring ...`, `emphasizing ...`, `ensuring ...`, `reflecting ...`, `symbolizing ...`, `contributing to ...`, `cultivating ...`, `fostering ...`, `encompassing ...`, `enhancing ...`, `valuable insights`, `align with`, `resonate with`.

Retrieval-capable models make this worse by pinning the invented analysis to a real named person, who did not say it.

The test that generalizes: delete the trailing participial clause. If nothing was lost, it was ornament. This belongs in `core/anti-slop.md` as a procedure, not as a word list, because the procedure survives vocabulary drift.

### Vague attribution and overgeneralized opinion

The model hangs a claim on an unnamed authority and inflates the number of people who hold it.

Flagged: `industry reports`, `observers have cited`, `experts argue`, `some critics argue`, `several sources`, `several publications`, and `such as` placed before a list that is in fact exhaustive.

The distinct failures: presenting one source's view as consensus; referring to `reviewers` or `scholars` in the plural while citing one; implying a list is open-ended when the source gives no reason to think so. That last one is subtle and worth carrying into `core/accuracy.md`.

### Canned emphasis on notability, attribution, and media coverage

The model argues for the subject's importance by cataloging where it was covered and what tier those outlets occupy. Common in models from 2025 on.

Flagged: `independent coverage`, `local/regional/national media outlets`, `trade publications`, `music/business/tech outlets`, `profiled in`, `written by a leading expert`, `active social media presence`.

The `maintains an active social media presence` formula is idiosyncratic enough to be near-diagnostic. Note also that models asked for encyclopedia prose will echo the platform's own policy vocabulary back at it — a general lesson: machine text tends to recite the criteria it is being judged against.

### Outline-like conclusions about challenges and prospects

A rigid closing formula: a `Challenges` section opening with a concession built on praise, then either a vague reassurance or speculation about what future initiatives might accomplish. Often paired with a `Future Prospects` or `Future Outlook` section.

Flagged: `Despite its ..., X faces several challenges`, `Despite these challenges`, `Challenges and Legacy`, `Future Outlook`.

The tell is the formula, not the topic. Writing about real difficulties is fine. Reaching for this shape to manufacture a conclusion is not.

### Leads that treat a descriptive title as a proper noun

When the title is a description rather than a name, the opening sentence defines the title as though it were a thing in the world — `refers to`, `is the chronological list of`, `is a curated compilation of`. The underlying error is writing about the label instead of the subject.

### Section headings of the form "X and Y"

Upstream's example is `Awards and recognition`, described as nearly ubiquitous in machine-written articles, with bare `Recognition` close behind. The paired-noun heading is the general shape and the source says it is common but not exclusive to machine text.

The diagnosis links it to two tells already above: the pull toward legacy and broader trends, and the vague gesture at a subject's coverage or recognition. A paired heading is easy to fill without knowing anything, because whatever the section contains can be filed under one noun or the other.

For `core/formatting.md`: a heading should name what is under it. If a section needs two nouns joined by `and` to describe itself, either it holds two sections or it holds nothing definite.

## Language and Grammar Tells

### High density of AI vocabulary

The strongest single lexical signal, with two critical qualifications: the words co-occur, so density matters far more than any individual hit; and the set drifts by model generation.

The current pooled list: `additionally` (especially sentence-initial), `align with`, `boasts` (meaning has), `bolstered`, `crucial`, `deep dive`, `delve`, `emphasizing`, `enduring`, `enhance`, `fostering`, `garner`, `highlight` (verb), `interplay`, `intricate`, `intricacies`, `key` (adjective), `landscape` (abstract), `meticulous`, `meticulously`, `pivotal`, `robust`, `showcase`, `tapestry` (abstract), `testament`, `underscore` (verb), `valuable`, `vibrant`.

By era, which is useful for knowing what still matters:

- **2023 to mid-2024** — `additionally`, `boasts`, `bolstered`, `crucial`, `delve`, `emphasizing`, `enduring`, `garner`, `intricate`, `interplay`, `key`, `landscape`, `meticulous`, `pivotal`, `underscore`, `tapestry`, `testament`, `valuable`, `vibrant`.
- **Mid-2024 to mid-2025** — `align with`, `bolstered`, `crucial`, `emphasizing`, `enhance`, `enduring`, `fostering`, `highlighting`, `pivotal`, `showcasing`, `underscore`, `vibrant`.
- **Mid-2025 on** — `emphasizing`, `enhance`, `highlighting`, `showcasing`, plus the notability-and-coverage vocabulary above.

Model-specific: Grok favors pseudo-scientific diction — `causal`, `empirical`, `correlate` — and still overuses `underscore`.

Two constraints the source states explicitly and that a module must honor. Read the list literally: a word being overused does not implicate its synonyms. And context governs — `underscore` as a typographic mark or as film music is not the tell.

### Avoidance of basic copulatives

The model replaces `is` and `are` with weightier substitutes. Measured as an over-ten-percent drop in `is`/`are` across academic writing in 2023, with no prior trend, and reproduced experimentally: ask a model to revise a sentence and the copula count falls.

Flagged substitutes: `serves as`, `stands as`, `marks`, `functions as`, `operates as`, `represents`, `boasts`, `features`, `maintains`, `offers`, `refers to`.

Two refinements. Several of these are marketing verbs standing in for `has`. And newer output builds longer detours — `ventured into politics as a candidate` for `was a candidate`, `began his career as` for `was`. The tell shows up most clearly in machine copyedits, which "improve" plain sentences into padded ones.

For `core/voice.md` this inverts cleanly into a positive rule: let the verb be `is` when the relation is `is`.

### Vague expression of connection or association

Shortcuts `WP:AICONNECT` and `WP:AIASSOCIATION`. Words to watch: `in connection with`, `in connection to`, `connected with`, `connected to`, `in association with`, `associated with`.

Newer models reach for an indirect construction when they need to assert that two things are related, abstracting the relation away instead of naming it. The plain alternatives are the small prepositions — `of`, `for`, `by` — or a verb that says what the relation actually is: `working with`, `used for`, `caused by`, `funded by`. The source notes it often arrives compounded with promotional vocabulary, as in `widely associated`, and that indirection alone convicts nobody; density and company are what matter.

For `core/anti-slop.md` the rule states cleanly and needs no detection framing: when two things are related, name the relation. Ownership, employment, funding, authorship, membership, cause — each of those has a word, and once you have picked one, `of`, `for` or `by` will usually carry it.

The exception is not decoration, and any module taking this rule must carry it. Sometimes an unexplained association is exactly the finding. An epidemiologist writing that a diet is `associated with` an outcome has chosen the precise phrase, because the direction of causation is unknown and asserting one would be false. There the vague-looking construction is the accurate one and `core/accuracy.md` requires it. The fault is the phrase standing where a nameable relation belongs, not the phrase itself. Banned outright, the rule would trade a vague sentence for a false one, which is the failure `core/restraint.md` exists to prevent.

Note what this one is not. Unlike most of the page it is attributed to *newer* models, which makes it the live counterpart to the elegant-variation tell that moved into `## Historical Tells` in the same fortnight. See the note at the head of that section: this pair is the evidence for it.

### Negative parallelism

Three shapes, all common, all stereotyped:

- `not just X, but Y` / `not only X but also Y` / `it's not just X, it's Y`
- `not X, but Y` / `it's not X, it's Y` / `no X, no Y, just Z`
- `X rather than Y` — the reversal. Unlike the two above it, this one negates nothing and asserts nothing false, so it is a frequency finding and not a fault: Grok output carries it at a notably high rate. Watch the rate, never the presence. `core/anti-slop.md` exempts the construction outright and `core/voice.md` builds on that exemption, and both are right to. Read this bullet as a reason to count occurrences in a draft that seems to lean on it, not as a reason to ban it.

The rhetorical move in the first two shapes is to stage a correction of a misconception the reader never held, which manufactures the feel of insight without adding a fact. It also appears across sentence boundaries, which makes a single-sentence check insufficient.

Humans use it too, especially in myth-busting registers, so it is a tell of frequency and reflex, not of presence.

### Rule of three

Overuse of triads, from three stacked adjectives to three parallel phrases. The source's diagnosis is the important part: the model reaches for a triad to make a superficial analysis look comprehensive. Three items feel like a survey. This belongs to `core/rhythm.md` as much as to anti-slop, because it is a cadence problem.

## Style and Markup Tells

These belong mostly to `core/formatting.md`.

- **Title Case In Headings.** Capitalizing every significant word in section headings.
- **Boldface as emphasis spray.** Bolding every instance of a chosen term, or bolding key-takeaway phrases mid-paragraph. Inherited from readmes, decks, listicles, and sales copy.
- **Inline-header vertical lists.** The signature shape: bullet, bold label, colon, explanatory sentence. Often with a non-standard bullet character (`•`, `-`, `–`, `#`, an emoji) or hand-numbered items.
- **Em dashes.** Used more than in comparable non-professional human text, in slots where a comma, colon, or parentheses would serve, and typically spaced. The formulaic use is to punch up a clause or stage a parallelism. Weak alone; meaningful in combination. Also unstable as a signal: vendors have suppressed it, and a July 2026 study found only Claude exceeding professional human rates while ChatGPT fell below them.
- **Emoji as structure.** Emoji prefixed to headings or bullets.
- **Needless small tables** for material that should be prose.
- **Curly quotes and apostrophes**, sometimes mixed inconsistently with straight ones in a single passage. Weak on its own — Chicago style, Word, and macOS all produce them.
- **Skipped heading levels**, typically starting at level three.
- **Overuse of level 1 headings.** The top level is effectively reserved for the title, so a document whose body sections start at level 1 is usually a Markdown structure converted without adjustment.
- **A title heading repeating the document's own title**, placed above everything else. The model does not assume the title already exists, so it writes one.
- **Headings that contain only other headings**, with no text of their own between them. An outline promoted to a document without being written.
- **Thematic breaks between sections**, a Markdown habit.

## Chat-Register Leakage

Assistant-to-user speech that survives into the document. Distinct from the other tells because it is unambiguous when present.

- **Collaborative filler** — `I hope this helps`, `Of course!`, `Certainly!`, `You're absolutely right!`, `Would you like ...`, `is there anything else`, `let me know`, `more detailed breakdown`, `here is a ...`.
- **Meta-narration of structure** — announcing what a section will do before doing it.
- **Placeholder text** left unfilled: bracketed slots, `2025-xx-xx` dates.
- **Over-itemized change descriptions.** A summary of one's own edit that names the exact parameters, fields and templates touched, reproduces their markup, and calls out having added `inline citations` or `internal links`. The granularity is the tell: a person describes what changed, and a model inventories it. Where the analogue is a commit message, a changelog entry, or a cover note, `core/voice.md` gets the rule — say what changed and why, not which fields you visited.

## Knowledge-Gap Speculation

Important enough to separate, and easy to underweight. When a model cannot find something, it frequently says so *and then speculates anyway*.

Flagged: `as of my last knowledge update`, `up to my last training update`, `while specific details are limited`, `not widely documented`, `not extensively documented in readily available sources`, `in the provided search results`, `based on available information`.

Two failures compound here. The claim that something is undocumented is itself unverified — often the model simply did not find it. And the speculation that follows, hedged with `likely`, is presented as informative content. For people this collapses into a stock formula: the subject `maintains a low profile` or `keeps personal details private`.

For `core/accuracy.md`: report absence of evidence as a failed search, say where you looked, and do not follow it with a guess dressed as a finding.

## Citation Tells

For `core/accuracy.md`.

- **Dead links on arrival** — several 404s or nonexistent domains in new text, with nothing in the Internet Archive, suggesting the URL never existed.
- **Invalid ISBN checksums and unresolvable DOIs.**
- **Valid DOIs pointing at unrelated papers** — the most dangerous variant, because the identifier resolves. The source's worked example includes a paper attributed to an author three decades dead at the purported date.
- **Book citations without page numbers**, which are unfalsifiable by construction; and citations with page numbers where the pages do not support the claim. Risk rises for general or frequently cited books, and when no URL is given.
- **Provenance parameters in URLs** — `utm_source=chatgpt.com`, `utm_source=openai`, `utm_source=copilot.com`, `referrer=grok.com`.
- **Reference-syntax errors** — named references defined but never cited, reused references with broken syntax, the `↩` character around footnotes.
- **Vendor leakage markers inside the markup**, each specific to a product: fragments such as `contentReference`, `oaicite`, `turn0search0` and `attributableIndex` from ChatGPT, bracketed `cite:` spans from Gemini, card and citation-render fragments from Grok, lenticular brackets from DeepSeek, upload paths from Perplexity. The page keeps a per-vendor inventory of these, and gives one of them a second life: `turn0search0` is used as an HTML anchor on the section that documents it. The joke is also the evidence, and it is worth noticing that the most mechanical class of tell is the one nobody has to argue about.

The generalizable rule: a citation that cannot be checked is not a citation. Page numbers and resolvable identifiers are what make a claim falsifiable.

## Historical Tells

Largely gone from current models, retained because they still surface in older text and because they show where the failure modes were.

**Read this section as the dossier's own expiry notice.** Most of what this page calls a tell is a fact about decoding, not about machines as such: a sampling penalty, a token limit, a refusal layer, a training-time habit. Change how the text is generated and the tell goes with it, which is why a list of tells is a dated artifact rather than a taxonomy. August 2026 supplied both halves of the demonstration inside two weeks — elegant variation retired because decoders stopped penalizing repetition, and vague connection added because newer models had started abstracting relations away. Neither move was about writing getting better or worse. So distrust the tense of every entry here before you distrust its content, and distrust the lexical entries above before the structural ones, because a word list tracks a model generation and a structural failure tracks the absence of something to say.

- **Didactic disclaimers** — `it's important to note`, `it's crucial to note`, `worth noting`, `may vary`. Advice to an imagined reader about safety or jurisdiction.
- **Section summaries** — `In summary`, `In conclusion`, `Overall`, plus restating the paragraph's point at its end.
- **Procedural self-narration in a change note** — announcing that information was `preserved`, `retained`, or that mistakes were `avoided`, and similar statements about the process rather than the result.
- **Abrupt truncation** at a token limit.
- **Stale default access dates** in citations.
- **Prompt refusals** — `as an AI language model`, `as a large language model`, `I cannot offer medical advice, but I can ...`. The model declined the request as written, apologized, and offered a nearby request instead. Outright refusals of this shape have become rare.
- **Elegant variation**, retired upstream on August 19, 2026 and re-tensed there to the past. Take the source's caveat first, because with the tell retired it is the load-bearing half of the entry: several educational traditions teach students never to repeat a word, so this heuristic fired hardest on writers who had been taught to write that way, and on non-native English writers in particular. It was weak evidence against them while it was evidence at all, and it is none now. The pattern it named — one referent accumulating synonyms down a paragraph until the prose reads as thesaurus churn — was measured against pre-2023 Wikipedia and against generated imitations of it, and is no longer characteristic of current output.

**Why it expired, stated so it cannot be re-read as taste.** Older decoders applied a repetition penalty at sampling time: a token's probability was reduced arithmetically because that token had already appeared. The operand was a count of tokens. No judgment about style entered anywhere, and the model held no view that repetition was a fault — the penalty would have fired identically on a text where repeating the word was the right call. Its effect on prose was secondhand: a name already used was cheaper to avoid than to repeat, so the referent picked up synonyms. Current models sample without that penalty, so there is no longer a mechanism to produce the pattern, and the pattern no longer indicates machine authorship. Kept here because it explains why text of that era reads as it does.

**Where it went in `core/`, and why it went to two places.** The fault is retained in `core/anti-slop.md` on reader grounds alone — a single referent renamed at each mention until a reader cannot tell whether a second organization has entered the paragraph — and it is listed among the non-tells in `core/restraint.md`, beside missing citations, as a fault with a long pre-model history that convicts nobody. Both are correct and they are not in tension: the same pattern can be worth fixing and worthless as evidence, and keeping those two judgments in separate modules is what stops a style rule from hardening into an accusation. What must not survive anywhere is the inference from thesaurus churn to machine authorship.

The source dates `In conclusion` as a machine tell, but it remains a real writing weakness, so `core/rhythm.md` should keep it on craft grounds rather than detection grounds.

## Bias in Generated Content

Added upstream in August 2026 and new territory for this dossier, which had carried no account of slanted content as distinct from slanted style.

The finding is that large American frontier models carry a pro-authoritarian slant on some prompts. The page gives two causes: training on the whole internet without excluding state propaganda on political subjects, and vendors citing the safety of users who live under authoritarian governments. Three specifics follow. Responses in Chinese run more authoritarian than responses in English. Models criticize governments in freer countries more readily than repressive ones, sometimes on stated safety grounds. Both are reported as measured, not inferred. Sourced to Stu Woo in the *Wall Street Journal*, August 14, 2026, and to *Fortune*, August 13, 2026.

For `core/accuracy.md` this is a verification obligation rather than a style rule, and it is sharper than the general one. The failure is not a fabricated citation, which a checker can catch, but a defensible-looking claim tilted by the corpus underneath it. Political and governmental subject matter therefore needs its sourcing checked against the claim's direction, not only against its existence. It also bears on translated or multilingual work, where the same question can return differently shaded answers in two languages.

`core/` should not restate this as a writing rule. Nothing here tells a writer what to do with a sentence.

## Signs of Human Writing

The inverse list, and the most directly useful section for `core/voice.md`. These are constructions that machine text avoids because it is reaching for a formal register, and that human writers use freely.

- **Plain copulatives** — `there is a`, `it has a`.
- **Short plain verbs over stiff or euphemistic ones** — `wrote` over `authored`, `moved` over `relocated`, `used` over `utilized`, `tried` over `attempted`, `died` over `passed away`.
- **Definite and superlative statements** where they are true — `one of the best`, `is the only`, `was the first`. Machine text hedges these away.
- **Hedges and intensifiers used naturally** — `very`, `perhaps`, `tends to`.
- **Ordinary wordy connectives in isolation** — `as a result of`, `in order to`, `all of the`, `a part of`, `the fact that`.

The last two points matter more than they look. A model trained to sound polished strips exactly these, so systematically removing every `very` and every `in order to` moves prose toward machine register, not away from it.

## Non-Tells

The overcorrection list. The source documents each of these as ineffective, and treating them as tells produces false positives.

- **Perfect grammar.** Many humans write cleanly.
- **Mixed casual and formal register.** Indicates a technical writer, a young writer, playfulness, neurodivergence, or several hands on one document.
- **Bland or robotic prose.** Machine output has specific traits, and generic dullness is not one of them; the output skews verbose and positive rather than flat.
- **Fancy, academic, or formal prose.** The correlation is with *specific overused words*, and does not generalize to elevated diction.
- **Transition words in isolation.** Only a few are actually overused. Many style guides accept sentence-initial connectives, and essayistic human writing uses them constantly.
- **Unsourced content.** Predates the models by decades, and modern models cite constantly — badly, but constantly.

The source also warns explicitly that false accusations drive people away and poison a community, and it names Dunning-Kruger and confirmation bias as the failure modes of the accuser. `core/restraint.md` inherits this whole section.

## What This Means for `core/`

1. **Anti-slop is a mechanism rule, not a word list.** Ban the trade of specificity for approval. Word lists date within eighteen months; the mechanism has not changed.
2. **The strongest single procedure is deletion-testing trailing clauses.** It catches superficial analysis, undue significance, and puffery at once, and needs no vocabulary.
3. **Restraint is load-bearing and evidence-backed.** The non-tells and the human-writing list mean that overcorrection is a real, documented failure mode, not a hypothetical one.
4. **Formatting tells are cheap to fix and cheap to state.** Heading case, bold spray, bullet-bold-colon lists, emoji, curly quotes.
5. **Accuracy owns the citation and knowledge-gap material.** Unverifiable citations and speculation-after-disclaimer are accuracy failures.
6. **Never let a module claim detection.** Every tell is written as "do not write this," never as "this proves a machine wrote it."

## Chunk Map

Working extraction lives outside the repository, in the session workspace, split by section.

The line ranges below index that extraction and not the wikitext. They were labeled "source lines" and are not: the page ran 1,665 lines of wikitext on the retrieval date against the extraction's 1,179, and the ranges do not scale onto the wikitext by any constant, so the extraction was evidently taken from a rendered or converted form. The ranges remain internally consistent and locate a section within the extraction. They cannot be used to cite the page, and no claim in this dossier rests on them. Re-deriving them against wikitext is not possible from inside the repository, because the extraction lives outside it.

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
