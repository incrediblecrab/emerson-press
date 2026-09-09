---
id: sources.ap-stylebook
layer: sources
version: 1.3.0
status: active
budget: none
evidence_kind: publisher-guidance
checked_on: 2026-09-08
verification_status: partial
source_version: "56th edition (2022-2024) print basis, with selected public 58th-edition and newsroom updates through 2026-09-08; no full 57th/58th entry audit"
source_urls:
  - https://www.ap.org/media-center/press-releases/2026/new-ap-stylebook-features-expanded-artificial-intelligence-chapter/
  - https://www.ap.org/the-definitive-source/announcements/ap-updates-newsroom-standards-for-artificial-intelligence/
  - https://www.apstylebook.com/blog_posts/19
verification_note: "The public-update ledger uses primary AP announcements independently checked in the 2026-09-08 research artifact, including primary-page publication dates. Inherited 56th-edition page references were not re-audited in this refresh. The full paywalled 58th edition and operational policy details remain unverified; extraction omissions do not establish source silence."
source:
  title: "The Associated Press Stylebook and Briefing on Media Law"
  edition: "56th edition, 2022-2024"
  superseded_by: "57th edition, 2024-2026, and 58th edition, 2026-2028, released May 27, 2026; selected public updates recorded below, full entry audits outstanding"
  publisher: "The Associated Press"
  year: 2022
  extent: "1,224 pp."
consumers:
  - stop-the-slop/accuracy.md
  - stop-the-slop/anti-slop.md
  - stop-the-slop/formatting.md
  - stop-the-slop/restraint.md
  - stop-the-slop/rhythm.md
  - stop-the-slop/voice.md
  - domains/education-level/01-elementary-lower.md
  - domains/education-level/02-elementary-upper.md
  - domains/education-level/03-middle-school.md
  - domains/education-level/04-high-school.md
  - domains/education-level/05-undergraduate.md
  - domains/education-level/06-graduate.md
  - domains/education-level/07-post-graduate.md
  - domains/marketing.md
  - domains/medical.md
  - domains/press.md
---

# Source: AP Stylebook — 56th-Edition Basis and Public Updates

Evidence base for `stop-the-slop/`, and for the AP mechanics that `domains/` and the `domains/education-level/` ladder draw on. Unbudgeted by design: nothing here is loaded into a prompt alongside a draft. This is what you read when you author or revise a core module, so the module itself can stay short and still be defensible.

This dossier uses original restatements, not source-text transcription. Short usage examples illustrate the inherited notes; they are not a replacement for the manual. Page references are retained from the 56th-edition notes; their mapping to print pages was not rechecked here, and they do not locate entries in the current online edition.

The detailed basis remains the 56th edition. Neither the full 57th nor the full 58th edition has been audited against these notes. Public announcements establish the limited updates below; they do not verify every older entry by implication.

## Public-Update Ledger

| Primary publication | Publicly established update | Limit on reuse |
| --- | --- | --- |
| [58th-edition release, May 27, 2026](https://www.ap.org/media-center/press-releases/2026/new-ap-stylebook-features-expanded-artificial-intelligence-chapter/) | Confirms the 58th edition, an expanded AI chapter, entries for *AI agent*, *AI slop* and *vibe coding*, and *healthcare* as one word. AP copy avoids *vibe coding* outside quotations. | A release announcement is not the full chapter or a complete change list. Do not invent entry definitions or infer unread clauses. The full 58th-edition audit remains outstanding. |
| [Newsroom AI standards update, July 23, 2026](https://www.ap.org/the-definitive-source/announcements/ap-updates-newsroom-standards-for-artificial-intelligence/) | Permits specified assistive uses with journalist review before publication; retains human sourcing, verification and accountability. Adds coding-assistant guidance and standards for disclosure of material generative-AI contributions. | This is AP staff policy, not a universal condition of choosing AP spelling or punctuation. The public announcement does not expose every operational disclosure rule. |
| [AP guidance on reporting about AI](https://www.apstylebook.com/blog_posts/19), publication date not independently established; checked September 8, 2026 | Avoid anthropomorphizing systems or assigning them gendered pronouns; examine training-data bias and present-day effects; check developer claims rather than merely repeat them. | Public guidance summary, not verification of the complete paid AI chapter. Reporting *about* AI is distinct from permission to use AI in production. |

The session artifact `public-standards-research.json` records confirmation of the two announcements' publication dates from primary-page JSON-LD. July 26 is a republication date, not the date of AP's newsroom update.

Do not carry forward a blanket prohibition on AI-assisted publishable content from the older 2023 policy as AP's current position. Equally, the new announcement is not permission for unattended publication or unverified sourcing. A non-AP writer follows the applicable venue's AI policy; selecting AP mechanics alone does not adopt AP's organizational workflow.

Except where this ledger states a public update, treat the detailed notes below as historical 56th-edition guidance and recheck high-risk mechanics before claiming current wire-style compliance.

## Why This Source

AP supplies reader-oriented editorial guidance and treats many style decisions as working conventions. That is useful when explaining why a sentence should change, but it does not make AP the sole authority on clarity or independent experimental evidence for prompt efficacy.

Its usage material supplies concrete checks for redundancy, euphemism and precision. The relevant question is whether a formulation conceals or misstates a fact, not how this guide ranks against other manuals.

### The repurposing caveat

AP is a newsroom guide. Journalism mechanics — datelines, wire conventions, sports agate and media law — should not become general writing rules merely because they appear in it. Those require their own domain context.

What `stop-the-slop/` takes is the craft layer underneath: the reasoning about clarity, precision, plain language, and reader attention, which AP applies to news but which is not about news. This dossier marks a newsroom-specific rule where one appears and hands it to `domains/`.

## AP's Stated Philosophy

Three properties of how AP holds its own rules matter more to `emerson-press` than any individual rule.

**Rules are justified by reader effect.** The punctuation chapter states that punctuation exists only to make the intended thought clear, and that a mark which does not aid clarity should be removed. [[p. 565]] The health and science chapter frames the writer as a translator between specialists and readers who do not share the specialist vocabulary. [[p. 646]] The business chapter names the ordinary consumer, not the industry insider, as its audience. [[p. 585]] The accessibility section treats plain language as an access measure, listed alongside captioning and alt text. [[p. 613]]

**The guide is provisional.** The editors call the guidance a living compromise rather than a fixed code, and expect some calls to stay genuinely debatable rather than resolving into right and wrong. [[p. 17-19]] They weigh prescriptive convention against how people actually use a contested term, instead of leaning on either alone, and they write for a broad general audience while conceding that a narrower audience may be better served by a stricter or a looser convention. [[p. 17]] They also treat published guidance as revisable, and will amend or reverse a recommendation that draws substantive reader objection. [[p. 19]]

**Padding is an accuracy problem, not a taste problem.** The news values statement holds every format AP publishes in — text, audio, video, graphics, data — to one standard of accuracy, bars rumor and unverified material from a story outright, and forbids altering the substance of a quotation or manipulating an image. [[p. 848]] Imprecise or inflated language sits on the same continuum: it is a fidelity risk before it is a style problem. That inference is this dossier's, not AP's sentence, and it is the bridge to the anti-slop material, which treats vagueness as a failure of truthfulness rather than of taste.

## The Condensed Style Manifesto

The densest passage of general writing craft in the book, from the accessibility section of the inclusive storytelling chapter. [[p. 613]] Restated:

1. Use plain, jargon-free language.
2. Prefer the smaller word over the fancier one. The pairs below are supplied here rather than by AP: `use` for `utilize`, `try` for `attempt`.
3. Write short, direct sentences.
4. Use strong verbs.
5. One idea per sentence.
6. When a sentence accumulates punctuation, split it into two — or three.
7. Do not stack modifiers.

Point 6 suggests a useful check for `stop-the-slop/rhythm.md`: punctuation density can be a symptom of overload. These accessibility-oriented recommendations are not proof that every long sentence or sentence containing related ideas needs splitting.

## Sentence Construction

### The tangled sentence

Judge every mark by whether it helps a reader grasp the intended meaning. When nested clauses or punctuation obscure the thought, try rebuilding into shorter sentences rather than repeatedly patching the marks. A punctuation count alone does not establish that the construction is broken. [[p. 565]]

AP illustrates with two real unfixed sentences — nested clauses, appositives, stacked nationality and place detail — presented purely as cautionary specimens, with no corrected version offered. [[p. 565-566]]

### Parentheses as a symptom

In the inherited guidance, accumulating parenthetical material is a reason to consider rewriting. [[p. 579]] It is not proof that every parenthesis is a defect; technical notation, citation styles and genuinely incidental information can require or benefit from parentheses.

### Modifier stacking

Think hard before stacking more than three modifiers. A hyphen pileup defeats the writer assembling it and the reader parsing it; when the hyphen count becomes daunting, rephrase. AP demonstrates by nearly committing the error on purpose, setting a plainly worded description of its own hyphen guidance beside a hyphen-chained version of the same phrase. [[p. 577]]

### Dangling modifiers

A modifier must attach logically to a specific word in the sentence: the real subject has to match whatever the introductory phrase implies is acting. [[p. 142]] An invented case, since AP's own is not reproduced here — *rounding the last bend, the finish line came into view*. Lines do not round bends. The fix names the runner.

### Voice

The selected 56th-edition notes favor direct verbs in several contexts. The business material recommends *rose* and *fell* rather than *were up* or *were down*; those latter constructions are not grammatical passives. [[p. 586-587]] The stock-price and accessibility notes likewise favor active or strong verbs. [[p. 490, 613]] The historical `comprise` entry prescribes active use with a direct object. [[p. 115]] These examples support a house preference for naming the action when useful, not a claim that AP bans passive voice or that no other AP entry permits it.

The historical drowning entry distinguishes `drowned` from `was drowned` when another person caused the drowning. [[p. 174]] The useful test is factual: changing the construction can change the agency being asserted. Passive voice can also be appropriate when the recipient matters or the actor is unknown. Do not invent an actor merely to make a sentence active.

`stop-the-slop/voice.md` states the positive rule — name the actor and the act — and this is the evidence under it.

### Quotation as a construction decision

Quote only when quotation is genuinely the best carrier. Otherwise paraphrase. [[p. 430]] Avoid fragmentary partial quotes by default: if the speaker was clear and concise, use the whole thing; if the phrasing is cumbersome, paraphrase fairly and reserve quotation marks for material that is contested or sensitive enough to need pinning to exact words.

Quotations may not be altered, even to fix grammar. If a quote is so flawed or unclear that it would confuse a reader, paraphrase it faithfully instead. If its meaning is too murky to paraphrase with confidence, do not use it at all. [[p. 865]]

That last rule generalizes past journalism, and `stop-the-slop/rhythm.md` uses it: when a construction cannot be saved clearly and faithfully, the answer is non-use, not repair.

## Lists and Series

Historical AP list guidance relevant to `stop-the-slop/formatting.md`. It is a publishing convention, not evidence about the frequency or cause of lists in model output.

**Construction.** Mark each item with a dash by house default; a bullet character is an accepted alternative. Put one space between the mark and the item's first word. Capitalize the first word of every item. End each item with a period rather than a semicolon, whether the item runs as a full sentence or as a fragment. Lead into the list with a short introductory phrase or sentence instead of dropping items in unframed. [[p. 315]]

**Parallelism.** Hold comparable items to a consistent grammatical form. A list built entirely of short verbless phrases is also acceptable. [[p. 315]] Parallelism checks form, not substance: a perfectly parallel triad can still say little. Let the material determine the number of items; do not delete a real third item to avoid a stylistic pattern.

**The serial comma is conditional, and flattening it is the common error.** In a simple series, separate items with commas and skip the one before the final conjunction — unless dropping it leaves the grouping genuinely ambiguous, in which case keep it, or better, rewrite so the grouping does not depend on a comma at all. [[p. 570]] Add the comma before the final conjunction when a listed item already contains a conjunction of its own, or when the series is built from longer parallel clauses rather than single words. [[p. 571]] When items run long or already carry internal commas, switch the separators to semicolons, including before the final `and`. [[pp. 583-584]] "AP never uses the Oxford comma" overstates a rule AP states as a clarity call.

## Attribution

`domains/press.md` owns the wire mechanics — anonymity ground rules, manager sign-off, picking up another outlet's sourcing. Three rules underneath those are general, and `stop-the-slop/accuracy.md` needs them, because the AI-writing sources name unnamed authorities as a tell without supplying a standard to replace them with.

- **Attribute anything reasonably open to dispute**, and give enough detail about a named source — age, title, organization, hometown, as the case needs — to establish why that person is credible. [[p. 852]]
- **A bare `a source said` is not attribution.** Even an unnamed source needs a real descriptive attribution that establishes credibility. [[p. 850]]
- **Always try to identify where information came from** rather than leaving it unsourced. [[p. 848]]

The generalization: an assertion carries the standing of whoever is behind it, so a sentence that hides who that is has removed the reader's only way to weigh it. `experts argue` and `industry reports suggest` fail this rule on AP's terms, not only on the anti-slop literature's.

One related usage entry belongs here. `Claim` as a verb signals the writer's own doubt about a statement, so reserve it for a genuinely disputed assertion and default to `said`. [[p. 103]]

## Cliché

### The general argument

The selected cliché entry argues for wording specific to the situation rather than familiar language that adds little information. [[p. 103]] This is an editorial rationale, not a measured rule that every familiar phrase loses a reader.

The useful house application is constructive: supply the particular fact or relationship that a stock phrase leaves unstated. Do not infer the absence of other AP guidance from this selected entry.

### The health and science list

The inherited notes flag these clichés in science and medical writing. [[p. 646]] They are regrouped here by the kind of claim they can obscure; this is an illustrative review list, not a prohibition on discussing or quoting the terms:

- Overstated breakthrough: `holy grail`, `game changing`, `paradigm shift`, `sea change`, `cutting edge`
- False decisiveness: `silver bullet`, `smoking gun`, `wake-up call`
- Borrowed drama: `perfect storm`, `sci-fi`
- Managerial filler: `outside the box`, `low-hanging fruit`, `tip of the iceberg`

Avoid letting a quoted cliché stand in for a factual explanation. Do not silently remove words from a quotation and present the altered wording as verbatim: quotation integrity still governs. When appropriate, paraphrase faithfully or choose a different quotation.

### Sports

Paired contrasts of cliché against plain description. AP's instruction is to describe a scoring play, a lead, or a game's outcome in literal terms rather than reaching for a slang nickname or a dramatic set phrase, and to avoid exaggeration alongside it. [[p. 742]]

| Avoid | Write |
| --- | --- |
| `disaster` for a loss | what the score was |
| `dingers`, `jacks`, `bombs` | `homers` |
| `unanswered` points | `straight` points |
| `never looked back` | `never trailed` |

### Individual overused words

`controversial` — most things so labeled obviously are, making the word padding. [[p. 124]] `definitely` — a vague intensifier. [[p. 153]] `cyberattack` — routinely stretched past its actual meaning. [[p. 138]] And a family of pity-laden verbs applied to disabled people: `afflicted with`, `battling`, `suffers from`, and `overcame`, where `has` states the fact. [[p. 167]] `wheelchair-bound` and `Alzheimer's victim` fail the same way; a person uses a wheelchair, or has Alzheimer's disease. [[p. 167]] The framing version of the same fault is coverage that stages an ordinary disabled person's ordinary activity as a feel-good spectacle. [[p. 166]]

## Jargon

AP defines jargon as the specialized vocabulary of a profession or group. The rule: avoid it, and where a specialized context requires it, explain any term unfamiliar to most readers. [[p. 295]]

The reasoning is sharper than the rule. [[p. 103]] Jargon exists as insider shorthand, but it also functions as in-group code and as a way to soften or spin a fact rather than state it. AP's illustrations run from a clinician's term for a symptom set, to a business term for pre-decision research, to a military term for accidental civilian killing — that last one a euphemism wearing a term of art. The same entry treats cliché as the same failure: it signals the reader to stop paying attention rather than engaging them. The writer's job is to translate and to dig for the real meaning.

### Plain-language checks

House applications of the 56th-edition plain-language advice. [[p. 646]] These are checks for accurate explanation, not automatic replacements or newly verified 58th-edition entries:

| Jargon | Write instead |
| --- | --- |
| `underlying condition` | other medical conditions |
| `prevalence` | say how common it is |
| `efficacy` | how well it works, or does not |
| `proportion` | share |
| `clinical trials`, `trials` | explain the study type when the distinction matters |
| `literature` | earlier studies |
| `clinician` | name the actual clinical role when relevant; not every clinician is a doctor |
| `pathogen` | explain the disease-causing agent in terms the intended reader understands |

With a critical caveat. If you are not certain a plain synonym is accurate, ask rather than guess: `high blood pressure` safely replaces `hypertension`, but `heart attack` cannot replace `cardiac arrest`, because those are different events. Substituting a plainer term that denotes something else is not simplification. It is an error. [[p. 646]]

### Individually flagged terms

| Flagged | AP's guidance |
| --- | --- |
| `internally displaced person` | People displaced within their own country; short form only on later reference [[p. 269]] |
| `respondents` (immigration court) | Immigrants, asylum-seekers, people seeking to remain [[p. 274]] |
| `asymptomatic` | No symptoms, without symptoms [[p. 62]] |
| `trauma` (loose use) | Injury, wound, bruise, shock [[p. 516]] |
| `officer-involved`, `police-involved` | Say who did what [[p. 378]] |
| `content` (digital) | Name the format — text, video, podcast [[p. 123]] |
| `FAANG`, `GAFAM`, `GAFA` | Avoid [[p. 74]] |
| `handle` (gambling) | Explain rather than assume [[p. 221]] |
| `high functioning`, `low functioning` | Name the actual condition, and only when relevant [[p. 254]] |
| `casualties` | Press for injuries or deaths; if unavailable, say so [[p. 92]] |
| `crisis` (migration) | Subjective; press the source for what they mean [[p. 266]] |
| `chain migration` | Avoid; implies unlawful immigration [[p. 270]] |

## Euphemism

The most transferable material in the book, because the reasoning is general even where the examples are political.

| Euphemism | Write instead | Why |
| --- | --- | --- |
| `passed away`, `passed on` | died, death | Plain euphemism; avoid outside quotes [[p. 151]] |
| `ethnic cleansing` | Describe the campaign — expulsion, violence, killing | Arose to launder atrocity; if used at all, quote it, attribute it, explain it, never as a bare descriptor or headline [[p. 193]] |
| `adult-use` (cannabis) | recreational, nonmedical | Named as euphemism [[p. 326]] |
| `racially charged`, `racially tinged`, `racially motivated` | state plainly what was said or done; use `racist` or `racism` where the conduct fits the definition | These explain little — they gesture at race without committing to a checkable claim [[p. 434-435]] |
| `anti-Asian sentiment` | anti-Asian bias, harassment, particular comments, violence | Same failure: vague where the specific fact exists [[p. 441]] |
| `handicapped`, `differently abled`, `physically challenged` | disabled people, people with disabilities, or the person's stated preference | Softening substitutes obscure rather than respect; use one only inside a quotation or when explaining how a subject describes themself [[p. 165]] |
| `collateral damage` | the accidental killing of civilians | AP's own illustration of jargon working as camouflage [[p. 103]] |

The synthesized principle, and the one `stop-the-slop/voice.md` carries: **a euphemism harms the reader by replacing a checkable fact with a softer label, and can launder the nature of what happened.** The fix is always the same as the fix for jargon — name what was said or done.

## Redundancy

The inherited usage entries illustrate a recurring check for needless repetition; this is not a claim that the complete manual lacks a general maxim.

The nearest general statements: `here` is usually redundant in a datelined lead because the dateline already carries the location [[p. 253]]; `of` is unnecessary after `half` [[p. 245]]; `last` before a named day or month is unnecessary because tense already carries it [[p. 306]]; and the sports chapter's craft section pairs its instruction against stock metaphor with one against exaggeration, describing a play or an outcome in literal terms instead. [[p. 742]]

| Redundant | Write |
| --- | --- |
| `ATM machine` | ATM [[p. 62]] |
| `HIV virus` | HIV [[p. 34]] |
| `HPV virus` | HPV [[p. 261]] |
| `ABM missiles` | ABMs [[p. 24]] |
| `ICBM missiles` | ICBMs [[p. 265]] |
| `SAM missiles` | SAMs [[p. 497]] |
| `10 a.m. this morning` | 10 a.m. [[p. 47]] |
| `10 p.m. tonight` | 10 p.m. [[p. 403]] |
| `last Tuesday`, `next Tuesday` | Tuesday [[p. 508]] |
| `past history` | history [[p. 256]] |
| `a total of` before a figure | the figure [[p. 514]] |
| `all-time record` | record [[p. 40]] |
| `new record` | record [[p. 448, 765]] |
| `future planning` | planning [[p. 400]] |
| `totally destroyed`, `totally demolished` | destroyed, demolished [[p. 155]] |
| `convicted felon` | felon [[p. 205]] |
| `forcible rape` | rape [[p. 214]] |
| `civil lawsuit` | lawsuit [[p. 306]] |
| `widow of the late` | widow of [[p. 557]] |
| `Shariah law` | Shariah [[p. 712]] |
| `Jewish synagogue` | synagogue [[p. 714]] |
| `rarely ever` | rarely [[p. 446]] |
| `accused of allegedly` | one hedge, not two [[p. 40]] |

The pattern across all of them: a word restating something the sentence already establishes, either through an acronym's expansion, a definition, or grammar. That generalization is what belongs in a module — the list is illustration.

## Precision

### Word pairs

| Pair | Distinction |
| --- | --- |
| `affect` / `effect` | Affect the verb influences; effect the verb brings about; effect the noun is a result. Avoid affect as a noun [[p. 32]] |
| `fewer` / `less` | Fewer for countable items, less for bulk. Fewer than 10 applicants; less than $50; but fewer than 50 $1 bills [[p. 206]] |
| `compose` / `comprise` / `constitute` | Compose is to put together, either voice. Comprise is to contain all of, active only — never `is comprised of`. Constitute is the fallback [[p. 115]] |
| `imply` / `infer` | The speaker implies; the listener infers [[p. 278]] |
| `farther` / `further` | Physical distance against degree or abstract progress [[p. 201]] |
| `continual` / `continuous` | Repeated with breaks against genuinely unbroken [[p. 124]] |

### Absolutes

The 56th-edition notes prescribe unmodified `unique` and treat `demolish` and `destroy` as complete actions, making intensifiers redundant in that usage. [[p. 522, 155]] These are recorded style conventions, not proof that partial damage cannot occur. Describe the actual extent accurately rather than forcing a fact into an absolute.

### The governing principle

The inclusive storytelling chapter tells a writer to apply the book's precision standard — the one the disability entries demonstrate — across every subject area, because precise, people-centered wording is not confined to one entry. [[p. 608]]

Choose the word that maps onto the specific fact rather than a broader one that gestures in the right direction, because imprecise language misinforms even when it is not false. Supporting instances:

- Name verifiable attributes instead of labels. The chapter's own case for this is marked as an invention in the working extraction, so here is one built for the purpose: `a night-shift dispatcher with eleven years on the desk` rather than `a veteran employee`. [[p. 608]]
- Let facts carry evaluation. Instead of `hero` or `traitor`, give the checkable record — what the person did, and which offices or roles they held — and let a reader draw the conclusion. [[p. 608]]
- `Merger` is not a loose synonym for acquisition or takeover; most combinations are not mergers of equals, and the wrong word misrepresents who holds power. AP supplies diagnostic questions, such as whose stock is the currency. [[p. 597]]
- Characterizations of extremist groups must be supported by reported evidence — actions, associations, stated positions — rather than reached for as a shortcut. [[p. 42]]

## Naming People and Groups

Directly relevant to `stop-the-slop/voice.md`, because the failure mode is the same one the AI-writing sources describe: a specific person dissolving into a category.

**Against collective abstraction.** Do not use dehumanizing `the` plus adjective constructions — `the disabled`, `the poor`, `the blind`, `the homeless`, `the mentally ill`. They substitute one adjective for a whole identity and flatten a varied group into an abstraction. [[p. 609, 167]]

**Against assumed homogeneity.** Limit `community` for groups of people. Sometimes it is the best available word, but it implies that everyone inside a broad category thinks and behaves alike. [[p. 608-609]] The same chapter's tokenism section holds that no individual stands in for a group's views, that real variation runs inside any demographic category, and that a reporter should look for the internal splits the way they would inside any political coalition. Interview a broad cross-section rather than one or two voices carrying the whole. And when a person's own account cuts against the wider data, give it context beside that data instead of dropping it. [[p. 605-606]]

**Person-first against identity-first.** Determine which the person or group actually prefers rather than defaulting. Where preference cannot be determined, mix both rather than picking one. [[p. 609]]

**Shorthand descriptions.** Do not reduce a person to a relationship or a single role. AP's worked cases: a first lady who also holds a doctorate and teaches; a barrister and human rights author identified through her husband instead of her practice; a former president identified through his spouse. [[p. 473-474]]

**Loaded ordinary idiom.** Watch for everyday phrases built on disability or difference, and reach for a more direct alternative — most sharply when the story itself touches the group the idiom borrows from. [[p. 609]]

**Why any of this is a craft rule and not only an ethical one.** AP states that a single word choice shapes how a reader perceives a person or a scene, so the test is what connotation a candidate word carries past its literal meaning. Its illustration of that test is invented for the purpose, and so is the one supplied here: a hospital that calls a wait a `queue` and one that calls it a `bottleneck` have described the same interval and set two different levels of alarm. [[p. 608]] The connected rule is to choose the most specific accurate description available rather than a broad label, and to let concrete facts carry an evaluation instead of reaching for `hero` or `villain`. [[p. 608]] The specific version is more precise *and* less loaded. The precision and the fairness are the same move, which is why `stop-the-slop/voice.md` can carry it without becoming a politics module.

On race coverage specifically: avoid broad generalization and labels, since race is one part of an identity [[p. 432]]; `people of color` is acceptable broadly but lumps distinct groups together, so prefer naming the groups actually meant — `Black and Latino Americans` rather than the umbrella term, and describe a specific readership or patient population by the groups it actually comprises [[p. 437]]; and do not use `minority` as a singular noun.

## Numbers in Prose

For `stop-the-slop/accuracy.md`. The data journalism chapter is a discipline of honesty about quantity, and it maps directly onto how machine prose mishandles statistics. Framing rule: never let technical jargon or overstatement stand in for a clear explanation of what an analysis concluded. [[p. 620]]

- **A bare number means little.** Anchor it to a comparison — a prior period, a benchmark, a parallel place — matching units and collection methods on both sides, and make the reference point explicit. [[p. 620]]
- **Use rates or per-capita figures** to compare groups of different sizes; for very large populations, a rate per 10,000. [[p. 620]]
- **Pair a ranking with the raw numbers under it**, so a reader can judge whether the ranking means much. [[p. 620]]
- **Adjust for inflation or seasonal effects** before comparing dollar amounts across periods. [[p. 620]]
- **Pick the population base that fits the topic** — voting-age population rather than total population when the subject is how people vote. [[p. 620]]
- **Percent change is not percentage-point change.** Ten percent to thirteen percent is a three-point rise and roughly a thirty percent relative increase. The two figures are not interchangeable, and the second is the one a reader hears. [[p. 620]]
- **Do not compute percent change from a small base.** Report the raw counts. [[p. 620]]
- **Name the measure.** Say whether a figure is the mean, the median, or the mode instead of letting `average` default to the mean by assumption. The mean skews under outliers; the median resists them. [[p. 621]]
- **Do not average subgroup means as if unequal groups had equal size.** Use the appropriate weighting when an overall mean is the intended measure. [[p. 621]]
- **Correlation is not causation.** Look for the mechanism linking two variables, and consider a hidden third factor or plain chance, before implying one produced the other. [[p. 621-622]]
- **Round.** Every digit supplied signals that every digit matters. [[p. 622]]
- **Limit digit density** — roughly eight to ten digits in a paragraph — and convert an unwieldy figure into a fraction or ratio to cut the count. [[p. 622]]
- **State uncertainty and sample size** rather than presenting a figure as more certain than it is, and report a survey's sample size especially when it is small. [[p. 622]]

Two rules from the health and science chapter belong beside these, and `domains/medical.md` stands on them. **Relative and absolute risk are both required, not alternatives.** A relative risk of 2.0 says one group is twice as likely as another and says nothing about how common the outcome is; two in a hundred against four in a hundred is the same ratio and a different fact. Give a reader both. [[p. 641]] The same pairing is demanded for any claim about toxic exposure or carcinogens, so a reader can weigh real-world danger rather than relative alarm. [[p. 645]]

Chart rules — zero-based bar axes, area-scaled circles, no gratuitous 3D, outliers removed only with strong justification — are at [[p. 623]] and belong to `domains/`, not `stop-the-slop/`.

## Verification

For `stop-the-slop/accuracy.md`, from the social media chapter. [[p. 647-656]] The principle transfers exactly: a plausible-looking artifact is not a verified one.

- Material found online meets the same evidentiary bar as anything else.
- Trace to the original source rather than a reposter, then ask the creator when and why they captured it.
- Use reverse image search to help find an original and detect recirculated material; a match or a failed search is not sufficient verification by itself.
- Cross-reference against independent trusted sources.
- Confirm claimed place and time with contextual detail — signage, plates, uniforms, language, weather, vegetation, lighting.
- A verification badge is a signal, not proof; accounts get compromised.
- If one online source carries something central, find a second.
- For any site: check who owns the page and whether that identity can be confirmed, whether working contact information exists, whether it states its own sourcing and whether that sourcing can be checked elsewhere, and whether it accepts open contributions without vetting them first. A crowd-edited reference site is a starting point whose citations must be chased back to primary material. [[p. 655-656]]
- Assume nothing from appearance. Manipulated and generated media are convincing.

## What `emerson-press` Takes

| Module | From AP |
| --- | --- |
| `voice.md` | Small words over big; strong verbs; the active-verb pattern and the drowning test for what a passive is for; the precision principle; euphemism; naming people specifically; word pairs; absolutes |
| `rhythm.md` | One idea per sentence; punctuation density as overload symptom; rewrite rather than repunctuate; modifier stacking; non-use when a construction cannot be saved |
| `formatting.md` | Punctuation serves clarity or goes; parentheses as symptom; list construction and the parallelism test; the serial comma as a conditional clarity call |
| `accuracy.md` | Numbers in prose; attribution and the failure of a bare unnamed source; verification discipline; precision as a fidelity obligation |
| `anti-slop.md` | The cliché argument; jargon as camouflage; the redundancy pattern |
| `restraint.md` | The provisional framing — rules are compromise and judgment, not correctness |
| `domains/education-level/`, all seven tiers | Punctuation, attribution, numerals and confusables, held to the same standard at every tier and taught in a different order; `05-undergraduate.md` adds appositives, composition titles, academic degrees, fractions and quotation integrity |
| `domains/marketing.md` | Puffery and euphemism as evasions of a claim; the precision principle applied to what may be asserted |
| `domains/medical.md` | The health and science jargon table; the plain-synonym caveat; absolute risk stated beside relative; person-first against identity-first |

Left to `domains/press.md`: datelines, wire conventions, anonymous-sourcing procedure, sports agate, media law, chart construction, and every entry that is about publishing rather than writing.

## Support Not Established by This Dossier

An omission from the inherited extraction is not evidence that AP has no guidance on a subject. These are limits on what this dossier can support, especially with the newer AI chapter not fully audited.

**Meta commentary.** The selected notes do not establish an AP-wide ban on throat-clearing, section previews or assistant-register phrases. AP's recorded list guidance includes a brief introduction. [[p. 315]] Other dossiers offer diagnostic ideas; neither they nor this limited AP record justify deleting useful signposting unconditionally.

**Cadence and sentence-length variation.** The recorded short-sentence guidance [[p. 613]] does not establish that AP rejects variation or that machine prose is universally flat. Reader-oriented rhythm advice remains an editorial application, not a measurement supplied by this manual.

**Document architecture.** No comprehensive theory of paragraph or document structure was verified for this refresh. Newsroom structures should be evaluated in their genre, not imported as universal rules from an incomplete extraction.

## Chunk Map

The earlier dossier records an external working extraction of 56 semantic chunks with `[[page N]]` markers and a page-reconstruction check. That historical check was not rerun here and is not reproducible from this repository, which holds no copy of the source text. The map is retained as provenance, not proof of current edition coverage.

The earlier review also recorded a separate extraction under `raw-data/ap-stylebook-data/` and its exclusion from version control. Neither extraction may be committed. This refresh did not inspect or change raw-data or either extraction.

| Chunk | Covers |
| --- | --- |
| `00-00-front-matter` | Foreword, how the book is made, philosophy |
| `01-az-*` through `24-az-*` | A-Z usage, 30 files |
| `25-ch-punctuation` | Punctuation, the tangled sentence, hyphens, parentheses |
| `26-ch-business` | Insider jargon, merger precision |
| `27-ch-inclusive-storytelling` | The style manifesto, naming, tokenism |
| `28-ch-data-journalism` | Numbers in prose, visualization |
| `29-ch-polls-surveys` | Margin of error, sampling |
| `30-ch-health-science` | Cliché list, jargon table, translator framing |
| `31-ch-social-media` | Verification |
| `33-ch-religion-*` | Redundancy instances |
| `34-ch-sports-*` | Sports cliché, redundancy |
| `36-ch-news-values-01..03` | Accuracy, quotation, corrections |
