---
id: sources.antislop-banlists
layer: sources
version: 1.1.0
status: active
budget: none
source:
  title: "auto-antislop / slop-forensics released datasets"
  author: "Samuel J Paech"
  repository: "https://github.com/sam-paech/auto-antislop"
  license: "MIT"
  artifacts:
    - "slop-forensics/data/slop_list.json (1,000 words)"
    - "slop-forensics/data/slop_list_bigrams.json (200 bigrams)"
    - "slop-forensics/data/slop_list_trigrams.json (200 trigrams)"
    - "slop-forensics/results/slop_profile_results.json (38 model profiles)"
    - "data/human_writing_profile.json (6.1 Gc human baseline)"
  human_baseline: "Nitral-AI/Reddit-SFW-Writing_Prompts_ShareGPT"
  method: "analyzed directly; every number below computed from the files, not quoted from the paper"
retrieved: 2026-08-09
consumers:
  - core/anti-slop.md
  - core/restraint.md
  - core/voice.md
  - domain/fiction.md
---

# Source: The Antislop Banlists, Measured Against Their Own Baseline

Companion to `ai-slop-research.md`. That note records what the papers *claim*. This one records what their released data actually contains, because the two are not the same thing, and the gap between them changes how much of this material `core/` can honestly use.

The Antislop project ships the artifact everyone cites second-hand: a list of patterns that language models over-produce. It also ships, in the same repository, the human corpus the list was measured against. Almost nobody checks the second file against the first. Doing so is the whole point of this note. This dossier computed every figure below from the JSON, and none of it appears in the paper.

This dossier reproduces nothing wholesale. Entries appear only as illustration, and this note regroups them by what they reveal rather than keeping source order. The data carries an MIT license; the arrangement below is original.

## The Artifacts Are Not the Ones the Paper Describes

The paper's Appendix M specifies a per-run banlist of 2,000 patterns — 1,000 words, 500 bigrams, 500 trigrams, split into entries that do and do not occur in the human corpus. The repository's *published static lists* are a different object: **1,000 words, 200 bigrams, 200 trigrams.** 1,400 patterns, not 2,000.

Both are real. The 2,000 figure is a pipeline quota, generated fresh per model per run. The 1,400 figure is what the project froze and released. Anyone quoting "2,000 patterns" and then linking the repository is describing one thing and pointing at another. `core/` cites the released lists, because those are the ones that can be inspected.

The human baseline is substantial and worth naming precisely: **6.11 billion characters** of Reddit writing-prompt responses, reduced to the top 500,000 bigrams (201.5 M occurrences) and top 500,000 trigrams (29.7 M). That is the denominator for everything that follows.

## Most of the List Is the Most Ordinary Language There Is

This is the finding that matters, and it is not subtle.

Of the 200 released slop bigrams, **192 (96%) appear in the human top-500k.** Their median rank in human writing is 5,373 — well inside common usage. And at the very top:

| rank in human fiction | bigram | occurrences | on the slop list? |
| --- | --- | --- | --- |
| 1 | could see | 208,668 | **yes** |
| 2 | shook head | 197,604 | **yes** |
| 3 | new york | 132,279 | no |
| 4 | first time | 118,145 | **yes** |
| 5 | looked like | 106,799 | **yes** |
| 6 | long time | 87,829 | **yes** |
| 7 | years ago | 85,114 | **yes** |
| 8 | old man | 83,684 | **yes** |
| 9 | even though | 82,183 | no |
| 10 | one thing | 75,157 | **yes** |

**Eight of the ten most frequent bigrams in human creative writing are on the anti-slop list.** The two exceptions are a place name and a conjunction. The top-ranked slop trigram, `took deep breath`, is likewise the single most common trigram in the human corpus, at 25,189 occurrences.

Nothing is wrong with the list. It is a *ratio*, and these entries earn their place by being over-produced relative to an already-high human rate. But it means the list cannot be read as a set of phrases to avoid. Applied literally to human prose it would delete ordinary English — `could see`, `first time`, `years ago` — and the writing left behind would be worse, not cleaner. Anyone who ships it as a find-and-replace has misread the artifact.

The word list behaves the same way. `nodded` is the 227th most common word in the human corpus and sits on the list; so do `stared` (438th), `leaned` (533rd), `glanced` (558th), `whispered` (724th), `paused` (878th), `sighed` (997th).

## Where the List Is Safe to Use Literally

The inverse of the above is the usable part. A minority of entries are absent from the human top-500k altogether — constructions with no meaningful human rate at all:

- **8 of 200 bigrams**, including `thick scent`, `dipped horizon`, `beacon hope`, `faces etched`, `casting warm`.
- **52 of 200 trigrams**, including `whatever challenges lay`, `newfound sense purpose`, `mind racing possibilities`, `casting warm glow`, `painting sky hues`, `voice steady despite`, `flicker something akin`.

Sixty patterns out of four hundred — **15%** — are genuine model artifacts rather than over-used human phrasing. These are the entries a writer can treat as flat prohibitions, and they cluster tightly around two habits: **narrating resolve** (`whatever challenges lay`, `knew road ahead`, `newfound sense purpose`) and **decorating scenery with participles** (`casting warm glow`, `painting sky hues`, `horizon casting long`). Both are already what `core/anti-slop.md` targets. The data confirms the aim rather than extending it.

## Half the Word List Is Genre Contamination

Of the 1,000 released words, **541 (54.1%) never occur in any of the human corpus's 500,000 most common bigrams.** That sounds like a strong signal until you read the entries. Excluding verb forms, 457 remain, and the overwhelming majority are invented proper nouns:

- **Fantasy and sci-fi character, place, and species names** — the dominant family by a wide margin. Names like `elara`, `kael`, `aelara`, `thalor`, `zephyrion`, `xylos`, `vorath`.
- **Genre furniture** — `archmage`, `grimoire`, `spellbook`, `commlink`, `datapad`, `plasteel`, `medbay`, `chestplate`, `sellsword`, `greatsword`.
- **Named-franchise leakage** — at least 23 entries are borrowed intellectual property or platform artifacts: `muggle`, `crucio`, `aurors`, `dursleys`, `geralt`, `rivia`, `dovahkiin`, `whiterun`, `dragonborn`, `doomguy`, `homelander`, `azathoth`, `roomba`, `missingno`, `truffula`, and — conclusively — `writingprompts`, the name of the subreddit the corpus was scraped from.

That last entry is the tell. The list has absorbed its own collection method.

None of this is a defect of the pipeline, which measured exactly what it was pointed at. It is a defect of *reuse*. More than half the published word list describes what fiction-writing prompts elicit, and carries no information about functional prose at all. For a system that writes documentation, press copy, or academic argument, the majority of the headline artifact is inert.

## The Lists Are Nested, So They Cover Less Than They Appear To

Two structural measurements, both computed here:

- **148 of the 200 trigrams (74%) are extensions of a bigram already on the bigram list.** The 400 n-gram slots do not encode 400 independent patterns.
- **186 of the 457 non-verb absent words (41%, or 18.6% of the entire 1,000-word list) are morphological variants of a stem already present.**

The redundancy is concentrated. A single invented stem, `xylo-`, consumes twelve slots (`xylos`, `xyloth`, `xylosian`, `xylosians`, `xylossian`, `xylossians`, `xylothian`, `xylothians`, and more). `aeth-` takes eleven, `zeph-` eight, `kael-` seven, `mala-` seven.

Effective coverage is therefore far below nominal size. This is the practical argument against list-length as a quality measure — and it lines up with the paper's own finding that an 8,000-token banlist collapses writing quality to 28/100. Long lists are not more thorough. They are more repetitive.

## Slop Is Repetition, Not Vocabulary and Not Length

The repository profiles **38 models** on a common slop score. Computing correlations across them:

| slop score vs. | r |
| --- | --- |
| repetition score | **+0.83** |
| vocabulary complexity | +0.01 |
| average length | +0.05 |

Slop tracks repetition almost completely, and has **no relationship whatsoever** to how complex the vocabulary is or how long the output runs. Two folk theories die here: that slop means inflated diction, and that slop means padding. Neither survives contact with the data. A model can write long, ornate prose with a low slop score, and terse plain prose with a high one. What makes it slop is reaching for the same construction again.

Model spread is wide — **19.8 to 67.7, a 3.4× range**. Within a single family, holding training recipe roughly constant, the effect is monotonic in scale:

| Llama model | slop score |
| --- | --- |
| 3.2-1B | 61.1 |
| 3.2-3B | 57.5 |
| 3.1-8B | 53.3 |
| 3.1-70B | 47.8 |
| 3.1-405B | 45.1 |

Five sizes spanning 400× in parameters, declining without exception. "AI writing sounds like this" is not a claim about AI writing. It is a claim about small models, and it ages as they get larger.

## What `core/` Takes

| finding | module | how it lands |
| --- | --- | --- |
| 8 of the 10 commonest human bigrams are on the list | `restraint` | the strongest available proof that banlists are not banlists |
| 96% of slop bigrams are common human English | `anti-slop` | density framing over word bans, restated with a number |
| Only 15% of n-grams have no human rate | `anti-slop` | the sharp, flatly-bannable minority is small and nameable |
| The absent set is resolve-narration and participle scenery | `anti-slop` | confirms the existing targets, does not extend them |
| 54.1% of the word list (541 of 1,000) never occurs in human bigrams, most of it invented proper nouns | `restraint` | the limit on transferring fiction lists to functional prose |
| `writingprompts` is on the list | `restraint` | a list can absorb its own collection method |
| 74% of trigrams extend a listed bigram | `anti-slop` | list length overstates coverage |
| One stem consumes 12 slots | `restraint` | more entries is not more thorough |
| slop vs. repetition r = +0.83 | `anti-slop` | repetition is the mechanism, named precisely |
| slop vs. vocabulary r = +0.01 | `voice` | ornate diction is a separate fault; do not conflate |
| slop vs. length r = +0.05 | `voice` | brevity is a separate virtue; do not conflate |
| 3.4× spread across 38 models | `restraint` | the variation is real, but it is the tail and not the center — see the correction in `sources/ai-slop-research.md`, which finds `flickered` on 98.5% of 67 models' lists |
| Monotonic decline 1B → 405B | `restraint` | tells are model-generation artifacts with a shelf life |

## What `core/` Does Not Take

**The lists themselves.** No module imports these entries as prohibitions. The released word list is majority fiction vocabulary, and the n-gram lists are majority ordinary English. Importing either would make the system worse at the prose it actually writes.

**The slop score.** The project defines it over creative-writing generations against a Reddit fiction baseline. It does not measure whether a release note or a methods section is any good, and no module should imply it does.

**Any claim that a low score means good writing.** The metric is one-directional. It detects a specific failure. Its absence is not a virtue.

## Limits

The human baseline is a single genre from a single platform — Reddit writing-prompt responses. It is large, and it is not representative of English. `could see` ranking first says as much about amateur first-person fiction as about human language. Every ratio in this note inherits that framing, including the ones that flatter the argument.

The 38-model profile is undated in the released file and includes preview and community fine-tunes alongside production models. Treat the ordering as indicative, and the scaling ladder — same family, five sizes — as the more defensible comparison.

The stem-clustering figure uses a four-character prefix, which is a blunt instrument. It will merge unrelated words occasionally, and it will miss variants that diverge early. The direction of the result is safe; the exact count is not.

None of this is a criticism of the project, which released its baseline alongside its findings and thereby made this note possible. That is more than most of the practice literature does.
