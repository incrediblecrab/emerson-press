---
id: sources.wida-curriculum
layer: sources
version: 1.4.0
status: active
budget: none
evidence_kind: publisher-guidance
checked_on: 2026-09-08
verification_status: partial
source_version: "2020 ELD Framework page notes; public framework overview and supplemental reader-guidance scope checked September 8, 2026"
source_urls:
  - https://wida.wisc.edu/teach/standards/eld
  - https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p01-clear-words/
  - https://www.w3.org/WAI/WCAG2/supplemental/about/
  - https://www.iplfederation.org/press-release-part-3/
  - https://www.iplfederation.org/iso-standard/
verification_note: "The live WIDA overview confirms K-12 classroom scope, four components and nonlinear development. Detailed printed-page mappings below are retained historical notes, not a fresh verification of all 393 pages or a validated reader-level model. W3C/IPLF checks concern public scope, not conformance testing or unread normative clauses."
source:
  title: "WIDA English Language Development Standards Framework, 2020 Edition"
  subtitle: "Kindergarten–Grade 12"
  publisher: "Board of Regents of the University of Wisconsin System"
  year: 2020
  extent: "393 pp."
consumers:
  - core/formatting.md
  - core/rhythm.md
  - domain/education-level/01-elementary-lower.md
  - domain/education-level/02-elementary-upper.md
  - domain/education-level/03-middle-school.md
  - domain/education-level/04-high-school.md
---

# Source: WIDA ELD Standards Framework, 2020

Evidence base for the `domain/education-level/` ladder. Unbudgeted by design: nothing here is loaded into a prompt alongside a draft. This file is what you read when you author or revise an education module, so the module itself can stay short and still be defensible.

This dossier states every rule in original wording. Reference codes (`ELD-LA.4-5.Argue.Expressive`) and linguistic terms (`nominalization`, `given/new`) appear as-is because they are identifiers rather than prose. Illustrative phrases and sentences throughout are supplied here rather than taken from the framework; single-word vocabulary examples are WIDA's, and ordinary words carry no expression to protect. Page numbers refer to the printed 2020 framework.

## Why This Source

Formulaic readability measures capture limited text features; they do not establish what an individual reader understands. WIDA adds a useful vocabulary for describing organization, clause relationships and word-level precision. This repository has not measured whether its WIDA-inspired presets outperform another readability approach.

The framework concerns multilingual learners' classroom language development. Using it to adjust prose written to a reader is a house adaptation, not a validated inference about an individual's reading ability or the only available approach.

### Verification and reader-guidance scope

On September 8, 2026, the [public WIDA overview](https://wida.wisc.edu/teach/standards/eld), especially its Proficiency Level Descriptors section, confirmed that language development is not a linear process and pointed readers to pages 31–34 of the 2020 framework. Its four-component overview does not verify every page-level paraphrase below.

The detailed grade/mode mappings retain printed-page locators from the earlier dossier. They require checking against the 2020 framework before being promoted into a new externally attributed requirement. In particular, this dossier does not license clause-count ceilings, mandatory counterclaims or delayed attribution.

[W3C's clear-words guidance](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p01-clear-words/) concerns actual language and access needs; its [status page](https://www.w3.org/WAI/WCAG2/supplemental/about/) says this supplemental material is not required for WCAG conformance. IPLF's [May 12, 2026 science-writing announcement](https://www.iplfederation.org/press-release-part-3/) emphasizes relevance, findability, understanding and use without sacrificing accuracy. Its [scope explanation](https://www.iplfederation.org/iso-standard/) distinguishes science communication from specialist scientific papers. These public summaries do not establish unread ISO clauses.

### The repurposing caveat

WIDA describes the language development of multilingual learners in K-12 classrooms. It is a standards framework for teachers, and Section 2 sets out what it is not: not a stand-in for a curriculum, not ready-made lessons, not a step-by-step recipe, not a grading tool [[p. 37-38]], not an exhaustive inventory of what a student can do, and not grounds for lowering expectations or restricting access to complex material [[p. 36]]. The proficiency descriptors carry their own warning: a level is a snapshot of one performance, not a label for a person. [[p. 33-34]]

`emerson-press` uses it for something adjacent but different: calibrating prose written *to* a reader at a given level. Two consequences follow.

- WIDA's descriptions concern classroom language development. They are not a score to hit or proof that a specific reader cannot follow a feature.
- The proficiency levels (PL1-PL6) describe contextual performances, not a text's difficulty or a permanent person-label. The education modules are optional task scaffolds, not proficiency classifications.

Beyond grade 12 WIDA has nothing to say. The three tiers above it — `05-undergraduate.md`, `06-graduate.md`, `07-post-graduate.md` — are sourced elsewhere. So is the working-adult register, which is now the unmarked default rather than a module: load a `domain/` genre module with nothing from `domain/education-level/` beside it and you are writing for an adult at work.

## The Framework in Four Components

Four nested components, broad to narrow. [[p. 25]]

1. **ELD Standards Statements** — five statements framing content and language as one thing rather than two. `ELD-SI` (social and instructional), `ELD-LA` (language arts), `ELD-MA` (mathematics), `ELD-SC` (science), `ELD-SS` (social studies). Identical from kindergarten through grade 12; only the expectations under them change. [[p. 26]]
2. **Key Language Uses** — four genre families that recur across every discipline: Narrate, Inform, Explain, Argue. [[p. 28-30]]
3. **Language Expectations** — goals for what a student does with language, split by grade band, Key Language Use, and mode.
4. **Proficiency Level Descriptors** — a six-level continuum describing how language grows toward those expectations. [[p. 33-34]]

`ELD-SI` is different in kind from the other four. It covers how people talk to each other while working — agreeing on norms, checking what somebody meant, working a question through with peers, saying where one personally stands — and it applies at every proficiency level, every grade, and inside every subject rather than sitting beside them. [[p. 26-27]]

### Modes

The four domains collapse into two modes. **Interpretive** covers listening, reading, and viewing. **Expressive** covers speaking, writing, and representing. Viewing and representing are in there deliberately: diagrams, labels, and layout count as language. [[p. 30-31]]

Expressive expectations concern producing language; interpretive expectations concern receiving it. Neither alone validates a prompt for a particular reader. The retained mappings below vary by band and mode and do not support a uniform one-step offset between comprehension and production.

### Reference codes

`ELD-LA.2-3.Narrate.Expressive` reads as: language arts, grades 2-3, the Narrate family, expressive mode. [[p. 30-31]] Codes are stable and worth citing in a module's `sources:` block, because they resolve to one specific set of statements.

## The Calibration Spine: Three Dimensions, Five Criteria

This is the part the `domain/education-level/` ladder is actually built on. WIDA describes language along three dimensions, with five criteria between them, and writes every proficiency descriptor against those five. [[p. 34-35]]

### Discourse — meaning across a whole text

- **Organization.** How a writer arranges ideas to serve a purpose, using patterns characteristic of the genre. Introduction/body/conclusion is a generic pattern; claim/evidence/reasoning is a genre-specific one.
- **Cohesion.** How ideas connect within and across sentences: repeated words, synonyms, pronoun substitution, connectors, omission, the given/new pattern.
- **Density.** How much information a noun group carries — whether the writer spreads meaning across clauses or compresses it into modifiers and nominalizations.

### Sentence — grammatical complexity

How clauses express relationships between ideas: simple, compound, and complex sentences; coordinating and subordinating conjunctions; dependent and independent clauses.

### Word/Phrase — precision

Choosing among everyday, cross-disciplinary, and technical registers, and using shades of meaning deliberately.

- **Everyday**: `dogs` rather than `canines`.
- **Cross-disciplinary**: `analyze`, `evaluate`, `summarize` — academic but not owned by one field.
- **Technical**: `mitosis`, `imperialism` — owned by a field.

### Why five criteria beats one number

Density and clause complexity are distinct features. The prior notes on page 256 discuss differences across registers; they do not establish universal rankings of all science, literary, spoken and written language. The house use of several criteria is a way to inspect different burdens, not a measured guarantee of comprehension.

## Key Language Uses

Four genre families. All four are present at every grade and in every discipline; what changes is which are prominent and what they demand. The tables and progressions in this section restate Section 2. [[p. 28-30]]

| Use | Job | Genres |
| --- | --- | --- |
| Narrate | Represent experience through stories and histories | Personal recounts, short stories, anecdotes, news stories, autobiography, biography, historical recounts |
| Inform | Convey factual information about a topic | Descriptive, classifying, comparative, and compositional reports; lab, investigation, design, and problem-solution reports |
| Explain | Account for how something works or why it happens | Sequential, causal, cyclical, systems, factorial, and consequential explanations |
| Argue | Justify a claim with evidence and reasoning | Exposition, discussion, challenge, review, interpretation, critical response |

### They blend

These are families, not boxes. An explanation usually informs on the way through — naming, defining, comparing — and may open with an anecdote. An argument may embed a narrative to reach the audience. Genre boundaries in real prose are soft, and prose that treats them as hard reads mechanical.

The distinctions that do carry weight:

- **Inform vs. Explain.** Inform describes or classifies clouds. Explain accounts for why it rains. The move from description to mechanism is the whole difference.
- **Explain vs. Argue.** Explain starts from an assumption that the thing is true and asks how or why. Argue tries to make the audience believe something or act.

### Narrate through the years

- **Early elementary.** Share and reflect on lived experience; retell or invent stories that rely on knowledge shared with the audience; combine drawing and approximate spelling.
- **Upper elementary and middle.** Add detail about people, scenes, settings, and actions; build images through description; handle more complicated plots; move between spoken and written registers; hold a longer text together.
- **Middle and high school.** Add nuance to description; use dialogue to reveal motive; underscore why an event matters; control pace to direct attention; build tension; make the whole thing cohere.

### Inform through the years

- **Early elementary.** Report on well-known topics; write about people, places, and familiar things nearby.
- **Upper elementary and middle.** Report on researched topics at a distance and in general terms; organize entities by composition and classification; compare and contrast; analyze features.
- **Middle and high school.** Produce extended classifications and technical material with real precision; carry research findings into different report types.

The shift is from describing what is in front of you to classifying abstractions into deeper taxonomies. What a writer can do here depends on topic knowledge, not just language.

### Explain through the years

- **Early elementary.** Share observations about how and why familiar, observable things happen; use diagrams and drawings alongside speech and some writing; handle sequence and cycles.
- **Upper elementary and middle.** Convey underlying causes; identify consequences; connect distinct ideas.
- **Middle and high school.** Build more complex cause-and-effect chains; handle abstract concepts and relationships among them; use multiple sources of evidence to substantiate an underlying cause.

The shift is from observable phenomena to unobservable mechanism, and from single cause to multiple causes and multiple effects.

### Argue through the years

- **Early elementary.** Express likes, dislikes, and emotions about familiar topics; share an opinion in a short multimodal text.
- **Upper elementary.** Substantiate claims with evidence and reasoning on topics outside personal experience; elaborate from research, data, or citation; engage other voices and perspectives.
- **Middle and high school.** Adjust the strength of a stance; refer to other perspectives; weigh evidence and evaluate sources; connect evidence to claim; contextualize primary and secondary sources; conduct and present research.

The shift is from personal opinion about everyday things to research, data, and textual evidence about abstractions — and it requires increasing control over language that expresses attitude and possibility.

## Three Features Common to All Four

These recur regardless of genre, and each is a lever `core/` can pull.

### Noun groups

A noun group is a noun plus what modifies it. Academic prose is hard largely because information gets packed into noun groups joined by one weak verb (`is`, `has`, `are`). Expansion happens before the noun (pre-modifiers: determiners, adjectives, quantifiers, classifiers) and after it (post-modifiers: prepositional phrases, relative clauses). [[p. 257]]

The progression is legible, and this instance is built for this dossier rather than taken from the framework: `kite` → `the kite` → `the torn kite` → `the torn, bright kite` → `the torn, bright, hand-stitched paper kite that snagged on the fence`.

The notes on page 257 connect lexical density with information packed into groups. Inspecting that packing can reveal a reader burden, but no evidence here establishes it as the single most reliable calibration control or a universal model failure.

### Nominalization

Turning an event or quality into a thing: `evaporate` → `evaporation`, `persecuting` → `persecution`, `the river kept overflowing` → `recurrent flooding`. [[p. 258]]

Two effects, and they pull opposite ways.

- It condenses. `The glacier is retreating` becomes `this retreat`, and the next sentence can build on it. (Invented here; WIDA's own worked case is not reproduced.)
- It can omit an actor, but need not: *the council's decision* retains one. Inspect whether agency is needed and supplied rather than treating every nominalization as evasion.

The passive-voice notes describe choices about emphasis and agency. [[p. 258]] Passive voice and nominalization are different grammatical devices, not evidence of one authorial motive. Both can be useful; an unknown actor must not be invented to replace either.

Useful to `core/voice.md` and `core/accuracy.md`: neither device is a defect, and each is a trade. Flag it when the actor matters and has vanished.

### Given/new

English written prose builds by putting known information at the front of a sentence and new information at the end. The next sentence picks up that new information as its given — often via nominalization — and adds more. [[p. 256]]

> Waves along this coast **erode** the cliff face every winter. That **erosion** is what pushed the lighthouse inland twice.

This is one useful cohesion pattern, illustrated here with invented sentences. It is not the only way prose connects, and its absence does not identify AI authorship. Do not attach a single universal proficiency level to it; the retained band/mode mappings differ.

## Grade-Band Profiles

Each profile summarizes retained notes about selected classroom expectations. The features are not onset ages, hard ceilings or guarantees of what an individual reader can do. **House scaffold** paragraphs below are editorial adaptations, not WIDA requirements.

### Kindergarten [[p. 43-62]]

**Snapshot.** Physical, hands-on, social. Drawing, gesture, and speech carry as much meaning as print does.

**Prominent uses.** Language arts: Narrate, Inform. Mathematics: Inform. Science: Inform, Explain. Social studies: Inform. No Argue expectations outside the social-and-instructional standard.

**Interpretive goals in the retained notes.** Identify key details, characters, settings, and major events. Identify a main topic. Ask and answer questions about unfamiliar words and about described attributes. Determine what a text is about.

**Discourse.** Pictures, words, and a title carry the topic. Pronouns and renaming reference one entity across a short text (`the girl = she = Nancy`). Connectors establish sequence: `then`, `after`, `and`.

**Sentence.** Simple sentences. Causal `because` and `so`. Comparison through `both`, `same`, `different`.

**Word/phrase.** Nouns to label. Verbs for action, feeling, and behavior. Prepositional phrases for where. Adjectives for one added detail. Relating verbs `be` and `have` to define or classify. Sequential signals `first`, `second`, `then`, `last`.

**House scaffold.** Make the topic and its connections visible. Use concrete examples when helpful; keep a multi-clause sentence when the reader can follow its relationship.

### Grade 1 [[p. 63-84]]

**Snapshot.** A jump from kindergarten. A sense of story structure appears, and so does the opinion with a reason attached.

**Prominent uses.** Adds Argue in social studies. Language arts still Narrate and Inform.

**Interpretive goals in the retained notes.** Identify a central message from key details. See how a character's attributes and actions contribute to an event. Notice words that suggest feeling or appeal to the senses. Define a topic, not just name it.

**New at this band.**

- Compound sentences joined by `and`.
- Conditional `if/then` for simple relationships.
- Timeless present for generalizable facts (`floats`, `sinks`, `eats`).
- Qualifiers: `some`, `all`, `many`.
- Comparatives: `-er`, `-est`, `bigger than`, `more`, `both`, `but`.
- Openers that address the reader directly: `Did you know?`
- Technical terms when supported (`tadpole`, `life cycle`).
- Speculation: `I think`, `I wonder if`.
- Declarative statements that present a conclusion.
- A summary statement that restates the position.

**House scaffold.** Make reasons and conditional relationships explicit. Define an unfamiliar technical term where useful. Split a sentence when comprehension improves, not because it crosses a numerical clause limit.

### Grades 2-3 [[p. 85-106]]

**Snapshot.** Narrative structure becomes deliberate. The difference between a story and an informational text is visible to the reader, and so is the difference between a claim with support and one without.

**Prominent uses.** Language arts: Narrate, Inform. Mathematics, science, and social studies all shift to Explain and Argue. This is the band where explanation and argument arrive across the curriculum.

**Interpretive goals in the retained notes.** Identify a central message and a main idea. Distinguish literal from nonliteral language. Describe relationships between a series of events, ideas, or procedural steps.

**New at this band.**

- Headings to organize (`Habitat`, `Diet`).
- Expanded noun groups introducing a character (`the tall woman next door`; invented here).
- Adverbials and prepositional phrases for time and place (`a hundred years ago`).
- Saying verbs for dialogue: `yelled`, `whispered`.
- Synonyms and renaming for cohesion, beyond pronouns.
- Single nouns standing for abstract concepts: `habitat`, `ecosystem`, `watershed`.
- Clauses expressing time (`before the thaw`, `once the pressure drops`).
- A wider range of clause connectors: `because`, `but`, `when`, `like`, `so`, `so that`.
- Sensory and literary language, onomatopoeia.
- Factual statements held free of evaluative language. WIDA draws the contrast explicitly with a paired animal description; the pair here is invented to the same shape: `gray wolf` against `super scary wolf`.
- Statements that disagree or counter a claim.
- Evaluative language to judge behavior or summarize an event.

**House scaffold.** Practice coherence across paragraphs and connect unfamiliar abstractions to examples. Choose a neutral register when the task needs it, not as a ban on other voices.

### Grades 4-5 [[p. 107-140]]

**Snapshot.** Argument moves outside personal experience. Objective stance becomes something a writer selects rather than falls into.

**Prominent uses.** Language arts adds Argue to Narrate and Inform — all three. Mathematics, science, and social studies: Explain and Argue.

**Interpretive goals in the retained notes.** Identify a theme from details. Analyze how characters develop across event sequences. Handle figurative language including metaphor and simile. Summarize main ideas. Evaluate the impact of word choice. Analyze competing points of view on the same event. Evaluate how details, reasons, and evidence support a point.

**New at this band.**

- Dependent and relative clauses adding detail (`the ferry, which ran only on weekends`).
- A range of tenses, used to place events relative to one another in time.
- Passive voice used deliberately to keep focus on the topic.
- Nominalization to condense (`The glacier is retreating` → `this retreat`; invented here).
- Modality for obligation and certainty: `might`, `could`, `must`, `need to`.
- First person versus third person as a stance choice.
- Ellipsis to cut repetition.
- Hedging: `could`, `might`, `sometimes`, `usually`.
- Topic nouns opening sentences and paragraphs.
- Connectors that elaborate: `so`, `this means`, `therefore`, `as a result`.
- That-clauses linking claim to evidence (`This shows that…`).
- Connectors signaling an alternative view: `one way`, `another way`, `on the other hand`.
- Summary statements that reiterate or call for a response.

**House scaffold.** Make stance and evidence relationships explicit. Keep useful embedded clauses when comprehensible; there is no one-clause ceiling. Name sources and discuss relevant credibility questions at an accessible level.

### Grades 6-8 [[p. 141-178]]

**Snapshot.** The retained argument tasks emphasize counterclaims and calibrated strength. They do not establish that these abilities first appear in this band or that every task requires opposition.

**Prominent uses.** Language arts: Narrate, Inform, Argue. Mathematics, science, social studies: Explain and Argue.

**Interpretive goals in the retained notes.** Track a theme developing over a whole text. Analyze how a character develops in relation to events or dialogue. Evaluate the impact of word choice on meaning and tone. Summarize a central idea distinct from prior belief. Analyze how an author handles conflicting evidence. Evaluate the relevance and sufficiency of evidence and the validity of reasoning.

**New at this band.**

- Nominalization condensing a whole clause (`the river kept overflowing` → `recurrent flooding`), and naming ideologies (`colonization`, `feudalism`).
- Adverbial and embedded clauses supporting a claim with quotes, examples, data.
- Contrastive connectors differentiating claim from counterclaim: `unlike`, `as opposed to`, `although`, `on the other hand`.
- Graduation — adjusting intensity with nouns, adjectives, verbs, adverbs (`somewhat`, `extremely`).
- First, second, and third person used to build alliance or hold neutrality.
- Collocations as a cohesive resource.
- Complex sentences clarifying causal, linked, time-bound, or sequential relationships.
- Passive voice to keep emphasis on the topic; active verbs to foreground agent and recipient.
- Modality that opens the field to other positions rather than only asserting.
- Given/new patterns linking and condensing across sentences.
- Literary devices supporting evidence and interpretation.
- Pace control in narrative; tension and suspense.
- Summary statements that restate a claim or call for action.

**House scaffold.** Explain genuine competing views when relevant, without inventing opposition to a settled fact. Support needed terminology and simplify burdensome nesting according to the reader, not a two-layer ceiling.

### Grades 9-12 [[p. 179-216]]

**Snapshot.** Strategic choice across the board. Not just what is said, but which genre, which register, which degree of certainty, and what the audience will need convinced of.

**Prominent uses.** Same distribution as 6-8, with a marked rise in what Argue demands.

**Interpretive goals in the retained notes.** Track themes across a text. Analyze how authorial choices about character relate to setting, sequence, and context. Evaluate the impact of word choice on meaning, tone, and explicit versus implicit point of view. Summarize central ideas of primary and secondary sources. Analyze rhetoric used to advance a purpose. Evaluate and corroborate relevance and sufficiency of evidence and validity of reasoning.

**New at this band.**

- Combining genres deliberately for effect.
- Refuting counterclaims with valid reasoning and sufficient evidence.
- If/then clauses supporting inferential conclusions (`If the sampling held, then…`).
- Deletion, substitution, and ellipsis to cut repetition.
- Short and complex sentences alternated to control pace.
- Evaluative nouns, adjectives, verbs, and adverbs assessing positive or negative qualities.
- A wider hedging range: `undoubtedly`, `is likely`, `probable`, `a possibility`.
- Objective and evaluative language used together to adjust precision, soften tone, and acknowledge others.
- Corroborating across primary and secondary sources.
- Anticipating what evidence a given audience will require.
- Wording pitched away from either pole, so a claim reads as considered rather than partisan.

**House scaffold.** Explain warrants, examine relevant sources and calibrate conclusions. Avoid borrowed authority and decorative method language. Neutrality does not require a midpoint between claims or suppression of a supported judgment.

## The Six-Level Continuum

Six proficiency levels, each cumulative — level 4 contains everything through level 4, not only its own descriptor. Level 6 is open-ended, on the grounds that language development does not stop. A person's levels differ across modes: someone can speak at one level and write at another. [[p. 33-34]]

One caution belongs beside that and gets dropped constantly: **this is not a strict ladder.** How a learner actually moves depends on how familiar the topic, the audience, and the situation are, so a path through the levels can wander rather than climb evenly. [[p. 33-34]] A writer reaching for a rung is describing a text, not a trajectory.

Read the following as a retained summary of the grades 9-12 expressive table, not a reading-level target or a fresh transcription check. [[p. 351-352]] It does not establish that production descriptors are the best predictor of reader comprehension.

| Criterion | L1 | L2 | L3 | L4 | L5 | L6 |
| --- | --- | --- | --- | --- | --- | --- |
| **Organization** | Short text, predictable order, some paragraph openers | Generic order: opening, middle, closing | Genre-specific patterns (a stated position, arguments, a call to action) with varied openers | Genre patterns pairing claims with counterclaims or rebuttals, plus deliberate signaling between paragraphs | Genre patterns with a wide range of relationship signals across the text | Genres combined flexibly for a chosen audience and effect |
| **Cohesion** | A growing set of devices: demonstratives, repetition | Expanding set: given/new, whole/part, class/subclass | Flexible set: ellipsis, substitution, omission | Devices chosen to suit the genre and the field | Wide variety, discipline-specific | Devices used flexibly and strategically |
| **Density** | Elaboration by demonstrative (`those three warnings`) | Elaboration by added classifier (`desert climate`) | Embedded clauses after the noun | Embedded clauses plus condensing by nominalization | Flexible elaboration, growing ways to condense | Elaboration and condensation chosen strategically |
| **Grammatical complexity** | Simple sentences, clauses emerging | Simple or compound, familiar coordination | Compound, broader range of joining techniques | Compound and complex, varied, matched to genre, plus ways to lengthen or shorten a sentence | Wide variety showing condition, cause, concession, contrast | Multiple techniques for building complex clause relationships, matched to genre, audience, and discipline |
| **Precision** | Growing repertoire, growing precision | Idioms and collocations | Adverbials of time, manner, place; verb types; abstract nouns | Evaluation and obligation, used precisely | Wide variety, precise, matched to genre and discipline | Flexible and strategic across contexts |

Four things worth carrying into `core/`:

- **Organization and sentence complexity are separate criteria.** Their placement in this table does not establish a universal psychological sequence or a mechanism of generated-text failure.
- **Nominalization is a level-4 move** in this table. It is not sophistication by default. It is a specific tool for condensing given information so a sentence can carry new information.
- **Flexibility is not maximum complexity.** A simple sentence can be an appropriate advanced choice. This supports an editorial analogy, not a measured claim about this prompt library.
- **The levels are re-scaled per band and per mode, not absolute.** WIDA prints a separate table for every grade band in each of the two modes, and a feature moves between columns across them. Given/new is the sharpest case, and it descends one step per band inside the expressive tables: level 5 at grades 2-3 [[p. 341]], level 4 at grades 4-5 [[p. 343-344]], level 3 at grades 6-8 [[p. 347-348]], level 2 at grades 9-12 [[p. 351-352]]. In the interpretive tables it sits at level 5 for grades 6-8 [[p. 345-346]] and level 4 for grades 9-12 [[p. 349-350]], and it does not appear in the grades 4-5 interpretive cohesion row at all [[p. 342]]. So a level number means nothing without its band and its mode, and the ordering of features within one table matters more than the number attached to any of them.

## Social and Instructional Language

`ELD-SI` runs alongside the four content standards and splits at only one point, between K-3 and 4-12. It covers how people talk to each other while working: agreeing on norms, checking what someone meant, working through a question with peers, saying where one personally stands. [[p. 26-27, 293-318]]

Useful to an education module because it names the interpersonal moves that belong at each band, and the 4-12 column is noticeably more demanding.

| | K-3 | 4-12 |
| --- | --- | --- |
| **Narrate** | Share ideas about lived experience; connect stories to images; ask questions about what others shared; recount and restate; discuss how a story might end | Same first two; press on what went unexplained or unsaid; retell in a way that carries the exchange forward; bring it to a close and say what comes next |
| **Inform** | Define and classify objects; describe characteristics, patterns, behavior; describe parts and wholes; sort and summarize ideas | Sort what is fact from what is reading-in, and what is settled from what is not; report patterns both stated and inferred; lay out a system's parts against the whole; boil down how things relate and what matters most |
| **Explain** | Share initial thinking; describe cycles, steps, causes and effects; compare and contrast; offer suggestions; revise understanding on feedback | Put first thinking into words; walk through cycles and sequences with what drives them and what follows; weigh cases where the variables and conditions themselves shift; put up alternatives that surface more of what is contributing; rework on feedback |
| **Argue** | Ask about others' opinions; support an opinion with reasons; clarify on feedback; defend a change of mind; revise an opinion on new information | Raise questions across competing viewpoints; back or push against a stated view, a starting assumption, or a reading of something; clarify on feedback; weigh how one's thinking shifted and name what was given up for what; sharpen claims as evidence arrives |

The K-3 → 4-12 jump worth noting: what others said becomes what nobody said; objects become facts against interpretations; comparing two fixed things becomes comparing things whose variables move; standing by a change of mind becomes accounting for it, trade-offs included.

## Linguistic Vocabulary

Terms WIDA uses precisely, worth using the same way in module prose. All of these come from the glossary. [[p. 253-262]]

**Clause types.** [[p. 253]]
- *Independent* — stands alone, has subject and predicate.
- *Dependent* (subordinate) — cannot stand alone (`as the caterpillars grow`).
- *Relative* — a dependent clause opening with `that`, `who`, or `which`, adding detail to a noun.
- *Conditional* — poses a hypothesis or imposes a condition, usually with `if` or `unless`.

**Sentence types.** [[p. 259]] *Simple* is one independent clause, and is not necessarily short. *Compound* is two or more independent clauses. *Complex* has one independent and one or more dependent clauses, and is how intricate relationships get expressed.

**Connectors,** grouped by the relationship they signal: [[p. 254]]
- Addition: `and`, `and then`, `furthermore`, `in addition`, `besides`
- Cause and consequence: `because`, `so`, `therefore`, `consequently`, `due to`, `as a result`
- Comparison and contrast: `but`, `instead`, `in other words`, `however`, `while`, `on the other hand`, `despite`
- Concession: `while`, `although`
- Condition: `if`, `unless`
- Purpose: `in order to`, `so`
- Sequence: `first`, `second`, `finally`, `to start with`, `in short`
- Time: `when`, `then`, `next`, `afterward`, `at the same time`, `meanwhile`, `previously`

**Verb types,** a distinction that does real work in `core/voice.md`: [[p. 261]]
- *Doing* — action: `pull`, `attract`, `pollinate`
- *Relating* — relationship: `is`, `belongs to`, `consists of`, `has`
- *Thinking* — thought: `consider`, `imagine`, `wonder`
- *Feeling* — feeling: `admire`, `detest`, `respect`
- *Saying* — speech: `confirm`, `ask`, `whisper`, `challenge`, `contradict`

**Cohesive devices.** [[p. 253, 257, 259, 260]]
- *Lexical cohesion* — repetition, synonyms, antonyms, hyponyms, class and subclass, whole and part.
- *Reference devices* — personal pronouns, articles, demonstratives, qualifiers, comparatives, and text reference (`That is what makes a tide chart worth keeping`).
- *Substitution and omission* — `We had two ladders, and I took the shorter one`; `Some hinges rust quickly, but others do not`.

**Other terms.**
- *Coherence* — whether the text makes sense as a whole. *Cohesion* — whether its parts are tied together. Coherence can fail while cohesion holds, which is exactly what fluent nonsense is. [[p. 253]]
- *Lexical density* — how much information a noun group carries. [[p. 257]]
- *Evaluative language* — nouns, verbs, and adjectives expressing attitude, judgment, or feeling. [[p. 255]]
- *Connotation and denotation* — dictionary meaning versus associated meaning. WIDA supplies a pair; this one is built for the dossier: `frugal` and `stingy` denote the same spending habit and pass opposite judgments on it. [[p. 254]]
- *Passive voice* — makes the recipient of an action the subject, keeping attention on a result, avoiding blame, or leaving the actor unnamed. WIDA states that third use plainly, which is a good precedent for `core/accuracy.md`. [[p. 258]]

## Mapping to `emerson-press`

| Module | WIDA bands | What it draws |
| --- | --- | --- |
| `domain/education-level/01-elementary-lower.md` | K, 1, 2-3 | Concrete anchors; explicit sequence and reasons; source naming when useful |
| `domain/education-level/02-elementary-upper.md` | 4-5 | Clear stance and evidence relationships; supported unfamiliar terms; no clause ceiling |
| `domain/education-level/03-middle-school.md` | 6-8 | Genuine competing views where relevant; calibrated claims; source evaluation without a nesting quota |
| `domain/education-level/04-high-school.md` | 9-12 | Warrants; relevant source comparison; purposeful pace and evidence-calibrated stance |
| `core/rhythm.md` | continuum | Sentence-type variety as a deliberate effect, not a metric |
| `core/formatting.md` | discourse organization | Headings and visuals as language; genre-specific organizational patterns |
| `core/voice.md` | word/phrase, verb types | Doing verbs over relating verbs; nominalization deleting the actor |
| `core/restraint.md` | level 6 | Flexibility, not maximum complexity, defines the top of the scale |
| `core/accuracy.md` | passive voice, evaluative language | Named uses of passive; connotation versus denotation |

The last three rows are available rather than drawn. `voice`, `restraint` and `accuracy` reach the same conclusions from the anti-slop evidence and cite that instead, so this dossier does not claim them in `consumers:` and they do not carry it in `evidence:`. They are listed because a future revision of any of the three should read these bands before restating the rule from scratch.

The three academic presets above grade 12 are outside WIDA's scope. Their research-writing checks are identified as house guidance; an AP link supports mechanics, not a university's assignment requirements. Reader-oriented plain-language principles can be useful at any educational stage. Public ISO summaries can inform a scope discussion without pretending that the normative text was read, and science communication must not be conflated with specialist research-paper requirements.

## What This Source Does Not License

WIDA states its own limits, and they transfer cleanly.

- Not a curriculum, not ready-made lessons, not a step-by-step recipe, not a grading tool. [[p. 37-38]]
- Not a complete inventory of the language of school. It does not try to be. [[p. 36]]
- Not a way to categorize a person. `a student at PL1` is a snapshot of one performance, not a label. [[p. 33-34]]
- Not grounds for lowering expectations or restricting access to complex material. [[p. 36]]
- Not a strict ladder. Movement through the levels depends on how familiar a topic, an audience, and a situation are, so the path varies. [[p. 33-34]]

One further limit is this repo's rather than WIDA's: do not cite a proficiency level for a grade-band rule. If a feature appears at both a grade band and a PL, cite the grade band. The PL is a different axis and not a target.

The `emerson-press` translation is a house hypothesis about scaffolding, not a validated measure of what a reader can track. Adjust density, clause relationships and explicit support to the actual reader. Never make a grade label a ceiling on sources, syntax, ideas or the standard of truth.
