---
id: sources.wida-curriculum
layer: sources
version: 1.0.0
status: active
budget: none
source:
  title: "WIDA English Language Development Standards Framework, 2020 Edition"
  subtitle: "Kindergarten–Grade 12"
  publisher: "Board of Regents of the University of Wisconsin System"
  year: 2020
  extent: "393 pp."
consumers:
  - audience/elementary-lower.md
  - audience/elementary-upper.md
  - audience/middle-school.md
  - audience/high-school.md
  - core/rhythm.md
  - core/formatting.md
---

# Source: WIDA ELD Standards Framework, 2020

Evidence base for the `audience/` layer. Unbudgeted by design: nothing here is loaded into a prompt alongside a draft. This file is what you read when you author or revise an audience module, so the module itself can stay under 250 tokens and still be defensible.

Rules stated in original wording. Reference codes (`ELD-LA.4-5.Argue.Expressive`) and linguistic terms (`nominalization`, `given/new`) are cited as-is because they are identifiers, not prose.

## Why This Source

Most readability tools measure the wrong thing. Flesch-Kincaid counts syllables and sentence length, so it rates `The cat sat on the mat because of the sun` as harder than `Aggregate demand fell`. Lexile does the same with word frequency. Neither can tell you what a twelve-year-old can actually track across a paragraph.

WIDA does. It describes what changes in language as students move through school, at three levels — how a whole text is organized, how sentences combine clauses, how words carry precision — and it does so per grade band, with worked examples. That is a calibration spine for the `audience/` layer, and there is no comparable public document.

### The repurposing caveat

WIDA describes the language development of multilingual learners in K-12 classrooms. It is a standards framework for teachers, and its own front matter says it is not a curriculum, not a reading-level formula, and not a way to categorize a person.

`emerson-press` uses it for something adjacent but different: calibrating prose written *to* a reader at a given level. Two consequences follow.

- WIDA's progressions are evidence about what language does as complexity rises. Treat them as that. Do not treat a grade band as a score to hit.
- The proficiency levels (PL1-PL6) describe a *learner's* development, not a *text's* difficulty. They are useful to audience modules as a map of how complexity is built up, not as a target. An audience module writes to a grade-band profile, never to a proficiency level.

Beyond grade 12 WIDA has nothing to say. `audience/undergraduate.md`, `audience/graduate.md`, and `audience/professional.md` are sourced elsewhere.

## The Framework in Four Components

Four nested components, broad to narrow.

1. **ELD Standards Statements** — five statements framing content and language as one thing rather than two. `ELD-SI` (social and instructional), `ELD-LA` (language arts), `ELD-MA` (mathematics), `ELD-SC` (science), `ELD-SS` (social studies). Identical from kindergarten through grade 12; only the expectations under them change.
2. **Key Language Uses** — four genre families that recur across every discipline: Narrate, Inform, Explain, Argue.
3. **Language Expectations** — goals for what a student does with language, split by grade band, Key Language Use, and mode.
4. **Proficiency Level Descriptors** — a six-level continuum describing how language grows toward those expectations.

### Modes

The four domains collapse into two modes. **Interpretive** covers listening, reading, and viewing. **Expressive** covers speaking, writing, and representing. Viewing and representing are in there deliberately: diagrams, labels, and layout count as language.

For `emerson-press`, the expressive expectations matter most — they describe constructing a text. The interpretive ones tell you what a reader at that band can extract, which is what an audience module is really calibrating against.

### Reference codes

`ELD-LA.2-3.Narrate.Expressive` reads as: language arts, grades 2-3, the Narrate family, expressive mode. Codes are stable and worth citing in a module's `sources:` block, because they resolve to one specific set of statements.

## The Calibration Spine: Three Dimensions, Five Criteria

This is the part the `audience/` layer is actually built on. Language is described along three dimensions, with five criteria between them. Every proficiency descriptor is written against these five.

### Discourse — meaning across a whole text

- **Organization.** How ideas are arranged to serve a purpose, using patterns characteristic of the genre. Introduction/body/conclusion is a generic pattern; claim/evidence/reasoning is a genre-specific one.
- **Cohesion.** How ideas connect within and across sentences: repeated words, synonyms, pronoun substitution, connectors, omission, the given/new pattern.
- **Density.** How much information is packed into noun groups — whether meaning is expanded across clauses or compressed into modifiers and nominalizations.

### Sentence — grammatical complexity

How relationships between ideas are expressed through clauses: simple, compound, and complex sentences; coordinating and subordinating conjunctions; dependent and independent clauses.

### Word/Phrase — precision

Choosing among everyday, cross-disciplinary, and technical registers, and using shades of meaning deliberately.

- **Everyday**: `dogs` rather than `canines`.
- **Cross-disciplinary**: `analyze`, `evaluate`, `summarize` — academic but not owned by one field.
- **Technical**: `mitosis`, `imperialism` — owned by a field.

### Why five criteria beats one number

Density and grammatical complexity move independently, and they trade off. Science writing is lexically dense but grammatically simple. Literary writing is grammatically complex but lexically sparse. Speech is more grammatically intricate than writing. A single readability score cannot represent that; five criteria can, and it is why `audience/` modules flag over-reach and under-reach separately.

## Key Language Uses

Four genre families. All four are present at every grade and in every discipline; what changes is which are prominent and what they demand.

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

A noun group is a noun plus what modifies it. Academic prose is hard largely because information gets packed into noun groups joined by one weak verb (`is`, `has`, `are`). Expansion happens before the noun (pre-modifiers: determiners, adjectives, quantifiers, classifiers) and after it (post-modifiers: prepositional phrases, relative clauses).

The progression is legible: `kite` → `the kite` → `the torn kite` → `the torn, bright kite` → `the torn, bright, hand-stitched paper kite that snagged on the fence`.

Density rises with the count of content words inside the group. This is the single most reliable knob for audience calibration, and the one LLM prose over-turns by default.

### Nominalization

Turning an event or quality into a thing: `evaporate` → `evaporation`, `persecuting` → `persecution`, `the river kept overflowing` → `recurrent flooding`.

Two effects, and they pull opposite ways.

- It condenses. `Leatherbacks are declining` becomes `this decline`, and the next sentence can build on it.
- It deletes the actor. `Mistakes were made` has a cousin in every nominalization: emphasis lands on the result and whoever caused it disappears.

Useful to `core/voice.md` and `core/accuracy.md`: nominalization is not a defect, it is a trade. Flag it when the actor matters and has vanished.

### Given/new

English written prose builds by putting known information at the front of a sentence and new information at the end. The next sentence picks up that new information as its given — often via nominalization — and adds more.

> Waves along this coast **erode** the cliff face every winter. That **erosion** is what pushed the lighthouse inland twice.

This is the mechanism behind prose that flows, and its absence is why list-shaped LLM paragraphs feel like they do not connect. Resist attaching a single proficiency level to it — where it lands moves sharply across bands and modes, as the caution below shows. What holds everywhere is that prose which never uses it reads flat regardless of vocabulary.

## Grade-Band Profiles

Each profile gives the developmental snapshot, which Key Language Uses carry the load, and the language features WIDA actually names at that band. Features are cumulative — each band assumes everything below it.

### Kindergarten

**Snapshot.** Physical, hands-on, social. Meaning is carried as much by drawing, gesture, and speech as by print.

**Prominent uses.** Language arts: Narrate, Inform. Mathematics: Inform. Science: Inform, Explain. Social studies: Inform. No Argue expectations outside the social-and-instructional standard.

**What the reader can do.** Identify key details, characters, settings, and major events. Identify a main topic. Ask and answer questions about unfamiliar words and about described attributes. Determine what a text is about.

**Discourse.** Pictures, words, and a title carry the topic. Pronouns and renaming reference one entity across a short text (`the girl = she = Nancy`). Connectors establish sequence: `then`, `after`, `and`.

**Sentence.** Simple sentences. Causal `because` and `so`. Comparison through `both`, `same`, `different`.

**Word/phrase.** Nouns to label. Verbs for action, feeling, and behavior. Prepositional phrases for where. Adjectives for one added detail. Relating verbs `be` and `have` to define or classify. Sequential signals `first`, `second`, `then`, `last`.

**Calibration.** One idea per sentence. Name the topic and keep naming it. Anchor every abstraction to something observable.

### Grade 1

**Snapshot.** A jump from kindergarten. A sense of story structure appears, and so does the opinion with a reason attached.

**Prominent uses.** Adds Argue in social studies. Language arts still Narrate and Inform.

**What the reader can do.** Identify a central message from key details. See how a character's attributes and actions contribute to an event. Notice words that suggest feeling or appeal to the senses. Define a topic, not just name it.

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

**Calibration.** Two clauses maximum, joined by one connector. A claim can now carry one reason. Technical vocabulary is allowed if it is defined on the spot.

### Grades 2-3

**Snapshot.** Narrative structure becomes deliberate. The difference between a story and an informational text is visible to the reader, and so is the difference between a claim with support and one without.

**Prominent uses.** Language arts: Narrate, Inform. Mathematics, science, and social studies all shift to Explain and Argue. This is the band where explanation and argument arrive across the curriculum.

**What the reader can do.** Identify a central message and a main idea. Distinguish literal from nonliteral language. Describe relationships between a series of events, ideas, or procedural steps.

**New at this band.**

- Headings to organize (`Habitat`, `Diet`).
- Expanded noun groups (`the old man on the block`).
- Adverbials and prepositional phrases for time and place (`a hundred years ago`).
- Saying verbs for dialogue: `yelled`, `whispered`.
- Synonyms and renaming for cohesion, beyond pronouns.
- Single nouns standing for abstract concepts: `habitat`, `ecosystem`, `watershed`.
- Clauses expressing time (`before the thaw`, `once the pressure drops`).
- A wider range of clause connectors: `because`, `but`, `when`, `like`, `so`, `so that`.
- Sensory and literary language, onomatopoeia.
- Factual statements held free of evaluative language — an explicit contrast between `brown caribou` and `really cool caribou`.
- Statements that disagree or counter a claim.
- Evaluative language to judge behavior or summarize an event.

**Calibration.** Coherence across a multi-paragraph text is now the goal, not just within a sentence. Abstraction is allowed if it has been built from concrete instances first. Neutral register becomes a distinct choice.

### Grades 4-5

**Snapshot.** Argument moves outside personal experience. Objective stance becomes something a writer selects rather than falls into.

**Prominent uses.** Language arts adds Argue to Narrate and Inform — all three. Mathematics, science, and social studies: Explain and Argue.

**What the reader can do.** Identify a theme from details. Analyze how characters develop across event sequences. Handle figurative language including metaphor and simile. Summarize main ideas. Evaluate the impact of word choice. Analyze competing points of view on the same event. Evaluate how details, reasons, and evidence support a point.

**New at this band.**

- Dependent and relative clauses adding detail (`the ferry, which ran only on weekends`).
- A range of tenses, used to place events relative to one another in time.
- Passive voice used deliberately to keep focus on the topic.
- Nominalization to condense (`Leatherbacks are declining` → `this decline`).
- Modality for obligation and certainty: `might`, `could`, `must`, `need to`.
- First person versus third person as a stance choice.
- Ellipsis to cut repetition.
- Hedging: `could`, `might`, `sometimes`, `usually`.
- Topic nouns opening sentences and paragraphs.
- Connectors that elaborate: `so`, `this means`, `therefore`, `as a result`.
- That-clauses linking claim to evidence (`This shows that…`).
- Connectors signalling an alternative view: `one way`, `another way`, `on the other hand`.
- Summary statements that reiterate or call for a response.

**Calibration.** One embedded clause per sentence, not two. Stance is now explicit — objective, evaluative, or personal — and should be consistent within a piece. Evidence must be linked to the claim by an actual sentence.

### Grades 6-8

**Snapshot.** Counterclaims arrive. So does the ability to adjust the strength of a statement rather than only its content.

**Prominent uses.** Language arts: Narrate, Inform, Argue. Mathematics, science, social studies: Explain and Argue.

**What the reader can do.** Track a theme developing over a whole text. Analyze how a character develops in relation to events or dialogue. Evaluate the impact of word choice on meaning and tone. Summarize a central idea distinct from prior belief. Analyze how an author handles conflicting evidence. Evaluate the relevance and sufficiency of evidence and the validity of reasoning.

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

**Calibration.** Two layers of clause nesting is the ceiling. A claim without a counterclaim reads as under-reach at this band. Technical terms are fine when cued. Stacked nominalization is the characteristic over-reach.

### Grades 9-12

**Snapshot.** Strategic choice across the board. Not just what is said, but which genre, which register, which degree of certainty, and what the audience will need convinced of.

**Prominent uses.** Same distribution as 6-8, with a marked rise in what Argue demands.

**What the reader can do.** Track themes across a text. Analyze how authorial choices about character relate to setting, sequence, and context. Evaluate the impact of word choice on meaning, tone, and explicit versus implicit point of view. Summarize central ideas of primary and secondary sources. Analyze rhetoric used to advance a purpose. Evaluate and corroborate relevance and sufficiency of evidence and validity of reasoning.

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
- Less polarized language so a claim reads as considered rather than partisan.

**Calibration.** This band's characteristic failure is dissertation cosplay — field jargon without context, stacked nominalizations, borrowed authority. Its other failure is hedging everything into mush. WIDA's own framing is useful here: the goal is an objective stance achieved through less polarized wording, not through refusing to claim anything.

## The Six-Level Continuum

Six proficiency levels, each cumulative — level 4 contains 1 through 3. Level 6 is open-ended, on the grounds that language development does not stop. WIDA notes that a person's levels differ across modes: someone can speak at one level and write at another.

Read the following as the shape of how complexity is built, not as targets. This is the expressive continuum for grades 9-12, which is what writing calibration cares about most.

| Criterion | L1 | L2 | L3 | L4 | L5 | L6 |
| --- | --- | --- | --- | --- | --- | --- |
| **Organization** | Short text, predictable order, formulaic openers | Generic order: introduction, body, conclusion | Genre-specific patterns (position, argument, call to action) | Genre patterns plus deliberate signalling between paragraphs | Genre patterns with a wide range of relationship signals | Genres combined flexibly for a chosen effect |
| **Cohesion** | A growing set of devices: demonstratives, repetition | Expanding set: given/new, whole/part, class/subclass | Flexible set: ellipsis, substitution, omission | Devices chosen to suit the genre and the field | Wide variety, discipline-specific | Strategic, and used creatively |
| **Density** | Some elaboration (`these five rules`) | More types (classifiers: `Roman empire`) | Embedded clauses after the noun | Embedded clauses plus condensing by nominalization | Flexible elaboration, growing ways to condense | Elaboration and condensation chosen for effect |
| **Grammatical complexity** | Simple sentences, clauses emerging | Simple or compound, familiar coordination | Compound, broader range of joining techniques | Compound and complex, varied, matched to genre | Wide variety showing condition, cause, concession, contrast | Strategic; aware that sentence shape itself creates effect |
| **Precision** | Growing repertoire, growing precision | Idioms and collocations | Adverbials of time, manner, place; verb types; abstract nouns | Evaluation and obligation, used precisely | Wide variety, precise, matched to genre and discipline | Flexible and strategic across contexts |

Four things worth carrying into `core/`:

- **Genre-specific organization arrives before complex sentences do.** Knowing the shape of the thing precedes being able to build long sentences. Prose that has sentence machinery but no genre shape is inverted, and that is exactly the failure mode of generated text.
- **Nominalization is a level-4 move** in this table. It is not sophistication by default. It is a specific tool for condensing given information so a sentence can carry new information.
- **Level 6 is defined by flexibility, not by maximum complexity.** The top of the scale is choosing the simple sentence when the simple sentence is right. This is the single most useful thing WIDA contributes to `core/restraint.md`.
- **The levels are re-scaled per band and per mode, not absolute.** WIDA prints a separate table for every grade band in each of the two modes, and a feature moves between columns across them. Given/new is the sharpest case: level 4 for grades 4-5 expressive, level 6 for grades 4-5 interpretive, and level 2 for grades 9-12 expressive. The same construction spans nearly the whole scale depending on which table you are reading. So a level number means nothing without its band and mode, and the ordering of features within one table matters more than the number attached to any of them.

## Social and Instructional Language

`ELD-SI` runs alongside the four content standards and splits at only one point, between K-3 and 4-12. It covers how people talk to each other while working: agreeing on norms, checking what was meant, working through a question with peers, saying where one personally stands.

Useful for audience modules because it names the interpersonal moves that belong at each band, and the 4-12 column is noticeably more demanding.

| | K-3 | 4-12 |
| --- | --- | --- |
| **Narrate** | Share ideas about lived experience; connect stories to images; ask questions about what others shared; recount and restate; discuss how a story might end | Same first two; press on what went unexplained or unsaid; retell in a way that carries the exchange forward; bring it to a close and say what comes next |
| **Inform** | Define and classify objects; describe characteristics, patterns, behavior; describe parts and wholes; sort and summarize ideas | Sort what is fact from what is reading-in, and what is settled from what is not; report patterns both stated and inferred; lay out a system's parts against the whole; boil down how things relate and what matters most |
| **Explain** | Share initial thinking; describe cycles, steps, causes and effects; compare and contrast; offer suggestions; revise understanding on feedback | Put first thinking into words; walk through cycles and sequences with what drives them and what follows; weigh cases where the variables and conditions themselves shift; put up alternatives that surface more of what is contributing; rework on feedback |
| **Argue** | Ask about others' opinions; support an opinion with reasons; clarify on feedback; defend a change of mind; revise an opinion on new information | Raise questions across competing viewpoints; back or push against a stated view, a starting assumption, or a reading of something; clarify on feedback; weigh how one's thinking shifted and name what was given up for what; sharpen claims as evidence arrives |

The K-3 → 4-12 jump worth noting: what others said becomes what nobody said; objects become facts against interpretations; comparing two fixed things becomes comparing things whose variables move; standing by a change of mind becomes accounting for it, trade-offs included.

## Linguistic Vocabulary

Terms WIDA uses precisely, worth using the same way in module prose.

**Clause types.**
- *Independent* — stands alone, has subject and predicate.
- *Dependent* (subordinate) — cannot stand alone (`as the caterpillars grow`).
- *Relative* — a dependent clause opening with `that`, `who`, or `which`, adding detail to a noun.
- *Conditional* — poses a hypothesis or imposes a condition, usually with `if` or `unless`.

**Sentence types.** *Simple* is one independent clause, and is not necessarily short. *Compound* is two or more independent clauses. *Complex* has one independent and one or more dependent clauses, and is how intricate relationships get expressed.

**Connectors,** grouped by the relationship they signal:
- Addition: `and`, `and then`, `furthermore`, `in addition`, `besides`
- Cause and consequence: `because`, `so`, `therefore`, `consequently`, `due to`, `as a result`
- Comparison and contrast: `but`, `instead`, `in other words`, `however`, `while`, `on the other hand`, `despite`
- Concession: `while`, `although`
- Condition: `if`, `unless`
- Purpose: `in order to`, `so`
- Sequence: `first`, `second`, `finally`, `to start with`, `in short`
- Time: `when`, `then`, `next`, `afterward`, `at the same time`, `meanwhile`, `previously`

**Verb types,** a distinction that does real work in `core/voice.md`:
- *Doing* — action: `pull`, `attract`, `pollinate`
- *Relating* — relationship: `is`, `belongs to`, `consists of`, `has`
- *Thinking* — thought: `consider`, `imagine`, `wonder`
- *Feeling* — feeling: `admire`, `detest`, `respect`
- *Saying* — speech: `confirm`, `ask`, `whisper`, `challenge`, `contradict`

**Cohesive devices.**
- *Lexical cohesion* — repetition, synonyms, antonyms, hyponyms, class and subclass, whole and part.
- *Reference devices* — personal pronouns, articles, demonstratives, qualifiers, comparatives, and text reference (`That is what makes a tide chart worth keeping`).
- *Substitution and omission* — `We had two ladders, and I took the shorter one`; `Some hinges rust quickly, but others do not`.

**Other terms.**
- *Coherence* — whether the text makes sense as a whole. *Cohesion* — whether its parts are tied together. Coherence can fail while cohesion holds, which is exactly what fluent nonsense is.
- *Lexical density* — how much information a noun group carries.
- *Evaluative language* — nouns, verbs, and adjectives expressing attitude, judgment, or feeling.
- *Connotation and denotation* — dictionary meaning versus associated meaning. WIDA's example: `cheap` as inexpensive, versus `cheap` as stingy.
- *Passive voice* — foregrounds the result, and may be chosen to hide who is responsible or to avoid naming an actor. WIDA states that use case plainly, which is a good precedent for `core/accuracy.md`.

## Mapping to `emerson-press`

| Module | WIDA bands | What it draws |
| --- | --- | --- |
| `audience/elementary-lower.md` | K, 1, 2-3 | One-idea sentences; concrete anchors; sequence and cause words; opinion with one reason |
| `audience/elementary-upper.md` | 4-5 | One embedded clause; explicit stance; evidence linked to claim by a sentence; hedging arrives |
| `audience/middle-school.md` | 6-8 | Counterclaims; graduation of intensity; two-layer nesting ceiling; nominalization as condensing |
| `audience/high-school.md` | 9-12 | Warrants; refutation; pace control; objective stance via less polarized wording |
| `core/rhythm.md` | continuum | Sentence-type variety as a deliberate effect, not a metric |
| `core/formatting.md` | discourse organization | Headings and visuals as language; genre-specific organizational patterns |
| `core/voice.md` | word/phrase, verb types | Doing verbs over relating verbs; nominalization deleting the actor |
| `core/restraint.md` | level 6 | Flexibility, not maximum complexity, defines the top of the scale |
| `core/accuracy.md` | passive voice, evaluative language | Named uses of passive; connotation versus denotation |

The last three rows are available rather than drawn. `voice`, `restraint` and `accuracy` reach the same conclusions from the anti-slop evidence and cite that instead, so this dossier does not claim them in `consumers:` and they do not carry it in `evidence:`. They are listed because a future revision of any of the three should read these bands before restating the rule from scratch.

Modules beyond grade 12 — `undergraduate`, `graduate`, `professional` — are outside this source. They cite AAC&U, WPA, ISO 24495-1, and plain-language guidance instead.

## What This Source Does Not License

WIDA states its own limits, and they transfer cleanly.

- Not a curriculum, not a lesson plan, not a step-by-step process.
- Not a complete inventory of the language of school. It does not try to be.
- Not a way to categorize a person. `a student at PL1` is a snapshot of one performance, not a label.
- Not grounds for lowering expectations or restricting access to complex material.
- Not a reason to cite a proficiency level for a grade-band rule. If a feature appears at both a grade band and a PL, cite the grade band. The PL is a different axis and not a target.

The `emerson-press` translation: a grade band describes what a reader can track, not a ceiling on what they may be told. An audience module adjusts the machinery of the prose — clause depth, noun-group density, connector explicitness — and never the ambition of the content.
