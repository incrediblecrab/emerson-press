# emerson-press

Style modules that keep LLM prose from reading like LLM prose.

## How to use

Load one module from each axis you need and put them in the context alongside your draft or your drafting instruction. There is no runtime and nothing to install — the modules are the artifact.

**1. Always load `core/`.** All six, or the ones that bear on the job. They are the rules that hold regardless of who is reading or what is being written.

**2. Add one `domain/` module** for the genre. This sets the mechanics — which style manual applies — and the evidence floor.

**3. Add one `audience/` module** for the reader. This sets register and calibration. If you do not know the reader, `professional` is the documented default.

**4. Add one `citation/` module** only if the piece carries formal citations. Omit it and the piece simply has none.

**5. Add `user-interface/`** only when the text ships inside a product rather than standing on its own. Load one medium module — `applications` or `website` — and stack overlays on top of it: `accessibility`, `charts`, `apple-hig`.

Skip `## Examples` unless you want before-and-after pairs; they are the largest part of a module and are separable for that reason.

Never load `sources/` alongside a draft. Those are the evidence behind the modules, for the person authoring or revising one.

Where two loaded modules disagree, later wins: `core < domain < citation < audience < user-interface`. The one exception is the evidence floor, which never falls — a change of register is not a change in the standard of proof.

If you cannot load files at all, `quick-guide.md` is the whole standard compressed into one pasteable file: `core/`, the narrative discipline, the calibration rule, and the evidence behind them. It is deliberately self-contained and refers to nothing in this repository, so it stays valid pasted into any prompt anywhere.

### Worked examples

A news feature for a general readership: `core/` + `domain/press.md` + `audience/professional.md`.

An undergraduate research paper in the humanities: `core/` + `domain/academia.md` + `audience/undergraduate.md` + `citation/mla9.md`.

A patient handout: `core/` + `domain/medical.md` + `audience/high-school.md`. The tier sets the vocabulary; `medical`'s rung-5 floor still governs the estimate.

Error messages in a mobile app: `core/` + `domain/technical.md` + `audience/professional.md` + `user-interface/applications.md` + `user-interface/accessibility.md`.

A landing page: `core/` + `domain/marketing.md` + `user-interface/website.md`. `marketing` owns whether the claim is true; `website` owns the page it sits on.

## Layers

```
core/           voice, anti-slop, restraint, accuracy, formatting, rhythm
audience/       elementary-lower, elementary-upper, middle-school,
                high-school, undergraduate, graduate, professional
domain/         press (AP), academia (Chicago), technical (house),
                marketing (AP), fiction (Chicago), legal (Bluebook),
                medical (AMA), general (house)
citation/       mla9, apa7, chicago18, ieee, ama11, bluebook22
user-interface/ accessibility, apple-hig, applications, website, charts
sources/        ap-stylebook, wida-curriculum, signs-of-ai-writing,
                field-guide-to-ai-slop, ai-slop-research,
                antislop-banlists, stop-slop, kill-ai-slop, apple-hig
```

These are orthogonal axes, not a hierarchy. Mix one from each rather than nesting them.

`sources/` is not an axis. It holds the unbudgeted evidence behind the modules — read when authoring or revising one, never loaded alongside a draft.

Citation is optional — omit it and the piece has no formal citations. So is `user-interface/`, which applies only when the text ships inside a product rather than standing on its own as a document.

Precedence, later wins: `core < domain < citation < audience < user-interface`

## Conventions

- Each module has `## Detect` (tells to flag) and `## Write` (what to do instead), so it serves both drafting and review.
- `## Examples` holds before/after pairs and is loaded only when needed.
- `audience/` modules carry three further sections, because calibration needs them: `## Mechanics` (what a writer should reliably control by that tier), `## Evidence` (the rung on the sourcing ladder), and `## Boundaries` (what changes at the tier below and above).
- `audience/` frontmatter carries `kind: ladder` or `kind: situational`, so a build step can tell a schooling rung from a reader description without parsing prose. `audience/professional.md` carries `default: true` and is the fallback when the reader is unknown. K-12 tiers carry `grades` and `wida_clusters`; tiers above it carry `stage`.
- Modules cite their evidence once, mechanically. `evidence:` is a list of paths into `sources/`, and every dossier carries the reciprocal `consumers:` list, so the link can be checked from either end. The prose citation — the work, the edition, and what was taken from it — lives in the dossier rather than being restated in the frontmatter of every module that draws on it. A module carries `evidence:` exactly when a dossier claims it as a consumer; `citation/` and two `domain/` modules — `general` and `legal` — carry none, because they were drafted from per-style and per-domain research passes rather than from a standing dossier.
- Say a thing once, at the length it takes. `budget` and `tokens` both count the body — not the frontmatter, not `## Examples` — and both record what a module measures rather than a ceiling it must fit. They are there so a change in size is visible in a diff, not to ration anything. A module gets shorter when a rule is redundant or unclear, never because a number said so.
- Counts are `o200k_base`. The recorded `tokens` field is a claim about the file and goes stale silently, so treat it as indicative rather than verified.
- `status` records whether a module is expected to change, not whether it is finished. `active` means shipped and not slated for revision; `draft` means complete in scope but still expected to move before its next version — `core/`, `citation/` and `user-interface/` because the layers around them are still settling, `domain/` because it is over budget and compression is queued. Both values describe complete modules.
- American spelling and punctuation throughout, including inside `sources/`. The two style manuals this repo pins are American, and a module that mixes `catalogue` with `catalog` has already failed the consistency it asks a writer for. Quoted titles keep the spelling of the work being cited.
- Every layer is authored full. Getting the calibration wrong compactly helps nobody, and an early pass that held `domain/` to a 400-token stub proved it: what the limit cut was the material that made the modules worth loading.
- `citation/` makes the case most sharply: a citation rule compressed past the point of being checkable is worse than no rule at all.
- Citation modules carry an `edition` field and pin the edition in the filename. When a style ships a new edition, add a module rather than editing the old one in place.
- `user-interface/` modules carry `kind: medium` or `kind: overlay`, a `medium` field, and a `## Surfaces` section holding the per-element rules for that medium, the way `domain/` carries `## Formats`, plus a `## Boundaries` section naming what the module does not cover. A medium module is loaded alone; overlays load on top of one.
- `evidence_floor` is an integer 0 to 5, or `none` where the ladder does not apply. Only `domain/fiction.md` takes `none`.
- State every rule in original wording rather than lifting a source's phrasing. This is an authoring standard before it is anything else: a rule you have restated is a rule you have understood, and one you have only copied is not. Short factual tokens stay as they are — reference codes, proper names, and the handful of style formulas that go imprecise the moment they are reworded. `raw-data/` holds the page-cited working extraction the dossiers were built from; it is listed in `.gitignore`, so a clone will not have it, and neither are the source texts themselves.

## Audience

Pick the tier you are actually writing at. Each module catches miscalibration in both directions — writing below the level, and writing above it. The second is the common one: a high schooler reaching for dissertation register reads worse, not better.

The layer holds two kinds of tier. Six are rungs on a schooling ladder, each adding one demand on where a claim comes from. One is situational: it describes a reader you are writing *for* rather than a level you have reached.

**Schooling ladder**

| tier | reader | evidence rung | anchor |
| --- | --- | --- | --- |
| `elementary-lower` | K-3 | reason, not yet a source | WIDA ELD 2020 |
| `elementary-upper` | 4-5 | 1. claim carries a reason | WIDA ELD 2020 |
| `middle-school` | 6-8 | 2. source is named | WIDA ELD 2020 |
| `high-school` | 9-12 | 3. source is traceable and characterized | WIDA ELD 2020 |
| `undergraduate` | undergraduate | 4. source is interrogated | AAC&U VALUE, WPA 3.0/4.0 |
| `graduate` | master's, doctoral | 5. uncertainty is quantified | Swales CARS, Hyland, ICMJE |

**Situational**

| tier | reader | evidence rung | anchor |
| --- | --- | --- | --- |
| `professional` | at work: a decision-maker, a peer, or a non-specialist | institutional accountability | Plain Writing Act, ISO 24495-1, Swales, Hyland |

`professional` is the default when the reader is unknown, since most adult writing lands there.

WIDA stops at grade 12, so the tiers above it use writing-studies and plain language anchors instead. The evidence column is a single ladder running the whole height of the repo: each rung adds one demand about where a claim comes from. Reaching for a rung you have not done the work for is the clearest form of over-reach, and it is easier to check than tone.

Inside `professional`, the reader varies more than the level does. A term of art is the precise, efficient choice for a peer and a wall for a non-specialist. The same sentence can be correct for one reader and malpractice for another, which is why that module calibrates by reader rather than by rung.

One caution worth stating plainly. Writing above your tier is not itself a fault, and these modules should never be used to push a strong writer down to the mean. The fault is register without control — terms the writer cannot define, complexity that does no work, gravitas borrowed to sound credible. Detection tools that flag "above-expected register" get this wrong constantly and misfire on capable students. The test is ownership, not difficulty.

Register calibration lives here. House style choices — the serial comma, for instance — live in `domain/`, because those vary by publication rather than by reader.

## Domain

Genre, not subject. The module answers what a piece is obliged to do, which is a different question from who reads it. `audience/` sets register; `domain/` sets the obligation, and the two move independently — a patient handout and a journal paper can share a subject and share nothing else.

| module | mechanics | evidence floor | formats |
| --- | --- | --- | --- |
| `press` | AP | 3, attributed in the sentence | news, feature, opinion |
| `academia` | Chicago | 4, source interrogated | essay, research paper |
| `technical` | house | 4, source is executable | reference, guide, README, changelog |
| `marketing` | AP | 4, and 5 for health, safety, efficacy or environmental claims | landing page, product, campaign, release |
| `fiction` | Chicago | none | short story, scene |
| `legal` | Bluebook | 5, plus continued validity | memo, brief, client letter, contract |
| `medical` | AMA | 5 | clinical, patient-facing, public guidance |
| `general` | house | 3 | blog, email, internal document |

**house** in the mechanics column means no external style manual: `core/formatting.md`'s defaults, plus whatever mechanics the module states for itself. It is a real setting rather than an absence — it names the manual that does *not* apply. The four `user-interface/` modules carrying `mechanics: house` take it in the same sense.

Three groupings, carried in frontmatter as `kind`. The **editorial** genres — press, academia, fiction — are governed by craft and by a discipline's own conventions. The **regulated** ones — legal, medical, marketing — are governed by somebody with enforcement power, and their rules are not style preferences that a confident writer may override. The **functional** ones — technical, general — are governed only by whether the reader can act.

That middle group is the reason the layer is not just a tone selector. In marketing an overclaim draws a regulator; in medicine it can cost a reader their health; in law an unvalidated citation is a misrepresentation to a court. `core/voice.md` says commit, and `legal` is the standing exception: a hedge is the product there, and the module asks only that it name the fact that would change the answer.

The evidence floors are the same ladder `audience/` uses, and they are floors rather than settings. Where a tier and a domain disagree, the higher of the two governs, because writing plainly for a non-specialist is a change of register and never a license to lower the standard of proof.

`fiction` is the deliberate outlier. Its floor is `none`, and it inverts `core/formatting.md` and most of the essay habits at once — no thesis, no takeaway, no summary. It is the hardest module in the repo for a model to satisfy, because slop cannot stop itself explaining its own subtext.

## Citation

Pick the style the venue actually requires. The module then does two jobs: it states that style's rules, and it names the neighbouring styles' rules that get mistaken for them.

| style | field | in-text system | edition |
| --- | --- | --- | --- |
| `mla9` | humanities, literature, languages | author-page | 9th (2021) |
| `apa7` | psychology, education, social sciences | author-date | 7th (2019) |
| `chicago18` | history, arts, publishing | notes *or* author-date | 18th (2024) |
| `ieee` | engineering, computer science | bracketed numeral | Reference Guide, 2025 |
| `ama11` | medicine, health sciences | superscript numeral | 11th (2020) |
| `bluebook22` | law | citation sentences, footnotes | 22nd (2025) |

The failure these modules are built against is not ignorance of a style. It is blending — a citation that is three-quarters APA with an MLA container and an IEEE bracket. Models blend because the styles overlap heavily and diverge on small, arbitrary details, which is exactly the shape of thing that gets averaged away.

So the divergences are load-bearing, and each module names the ones that touch it. The DOI is the sharpest: APA, MLA and Chicago all take the resolver form `https://doi.org/10.xxxx`, IEEE takes a bare `doi: 10.xxxx` with a space, and AMA takes a bare `doi:10.xxxx` with none. One identifier, three renderings, no reasoning available from first principles.

Generative-AI attribution diverges the same way and is newer, so it is worse. APA credits the company that built the tool, Chicago credits the tool itself, MLA credits nobody and makes the tool a container, and Bluebook credits the person who wrote the prompt. AMA names the tool and model but pushes the admission into the methods or acknowledgments, and IEEE goes further and declines to give a citation form at all, asking only that the use be disclosed. A module that invents a form here is worse than one that says the style is silent.

## Interface

Load this only when the text ships inside a product. A blog post has readers; an interface has users, and they did not come to read. Every word is a toll on the way to what they came for, which inverts most of what the other axes assume.

The axis is cut by medium, not by widget, because the same element takes different copy in different places. An error in an app names the next action; an error on a website is a 404 that offers the two pages the reader probably wanted. Cutting by widget would have produced one `errors` module hedging across both.

Two modules are media in the strict sense, and three are overlays that load on top of one. Frontmatter carries `kind: medium` or `kind: overlay`, the way `audience/` distinguishes a schooling rung from a reader description.

**Media** — pick exactly one.

| module | medium | covers |
| --- | --- | --- |
| `applications` | in-product, any platform | labels, forms, errors, alerts, empty states, progress, onboarding, notifications, settings |
| `website` | pages a stranger lands on | landing copy, navigation, titles, link text, forms, 404s, consent, docs |

**Overlays** — add any that apply.

| module | applies when | covers |
| --- | --- | --- |
| `accessibility` | the work ships to real users | labels, hints, alt text, headings, captions, announcements |
| `apple-hig` | the platform is Apple's | capitalization, terminal punctuation, ellipsis semantics, `Cancel`/`OK`, default position |
| `charts` | the product displays data | titles, axes and units, legends, annotations, tooltips, alt text |

So the common loads are `applications` + `accessibility`, `website` + `accessibility`, and on Apple `applications` + `accessibility` + `apple-hig`. Add `charts` to any of them. Never all five.

The two overlays that can disagree with a medium module say so themselves. `apple-hig` wins over `applications` on mechanics and on nothing else — Apple's conventions are mostly arbitrary and entirely load-bearing: title case on a button is a coin flip that landed decades ago, while a trailing ellipsis is a promise readers have learned to read. Breaking the first makes an app look foreign. Breaking the second makes it lie. Behavior — when to interrupt, when to ask, what to name a thing — stays with `applications` even on Apple platforms. `accessibility` decides what must be announced; the medium module decides the wording.

One precedence note, because this axis wins last. `user-interface` governs the attention economy — the reader did not come to read, so every word is a toll. It does not govern register, which stays with `audience/`. A children's app keeps its warmth and a peer tool keeps its terms of art. What these modules strip is unearned brand enthusiasm, not tone the situation has earned.

Two of the sources behind this axis are prescriptive skill files rather than studies, and both are rejected in part. `stop-slop` bans em dashes, adverbs, three-item lists and Wh- openers outright; `core/restraint.md` refuses those bans and the refusal holds here. What survives is the phrase taxonomy and the observation that generated marketing copy claims agency it does not have. `kill-ai-slop` is the more useful of the two because it is the only source in the repo written about interfaces, and its central claim — that decoration is a signal, and a badge or an ordinal or an icon grid usually marks text nobody decided on — is the backbone of `website`.

`charts` has the thinnest external anchor. Apple's guidance covers chart accessibility and little of the writing, so the module leans on Tufte and on plain measurement discipline: unit at the number, denominator with the percent, date on everything, and no trend claimed from two points.

## Status

Authored one at a time. `core/` is complete across all six — voice, anti-slop, restraint, accuracy, formatting, rhythm — and was re-authored full at 1.1.0 rather than held to the original budgets, on the same reasoning `audience/` used: getting the calibration wrong compactly helps nobody. The layer roughly quintupled. A later review argued that `core/` is the highest-leverage place to cut, because it is the only layer that always loads; the argument was declined, since the cost of loading a longer module is nothing next to the cost of a rule that no longer says enough to follow. Each module now carries an `evidence:` list naming the files in `sources/` it was built from. Their bodies do repeat phrasing from `sources/`, because those modules exist to name banned constructions and shared research findings, which have to be quoted exactly to be detected. This is the same footing `domain/marketing.md` and `user-interface/website.md` stand on, described below.

Its evidence base landed at the same time: `ap-stylebook` from a 56-chunk split of the print edition, verified to rebuild all 1,224 pages byte-identical, plus `signs-of-ai-writing` and `field-guide-to-ai-slop`. Where those disagree with the prescriptive skill files, the cited study wins. `restraint` is the module that decides those conflicts, and it is the reason this repo refuses the unconditional bans — em dashes, all adverbs, three-item lists — that the competing instructions impose.

`ai-slop-research` was added last and is different in kind from the rest of `sources/`: it records measurement rather than practice, which is what lets it settle disputes between the others. It was re-authored at 2.0.0 from the full texts, appendices included, after the first pass had been built from abstracts — which corrected three citation errors and surfaced the structural finding below. Slop is computable as an over-representation ratio against a human baseline, with the measured extreme at 85,513x. The two-thousand-pattern figure everyone quotes is a per-run pipeline quota — 1,000 single words, 500 bigrams and 500 trigrams — and 480 of those entries occur in the human corpus zero times, so their ratio has no denominator at all; the lists the project actually released and froze are smaller, at 1,000 words, 200 bigrams and 200 trigrams, which is the object anyone linking the repository is really pointing at. Contextual suppression at four-tenths strength suppresses 90% of them in ordinary writing while still permitting them when a prompt asks, whereas removing the trainer's safeguard buys 98% suppression at the cost of dropping writing quality from 67.8 to 19.6 — which is the empirical case against unconditional bans, and the reason this repo refuses them. Every one of those patterns was measured on creative writing, which the paper states and which limits how far the lists transfer to functional prose. And a matched-control study of 25 million forum comments found that the features which genuinely separate machine prose from human prose do not predict which human gets accused of writing like a machine; in the same data, stylistic-tell callouts like the em-dash complaint are the least reliable accusation tier measured. That is why no module here is framed as evading detection. Much of accusation is social gatekeeping that never reads closely, so no revision reaches it, and writing well does not need the excuse.

`antislop-banlists` is a companion to it and the only note in `sources/` whose every figure was computed here rather than read off a page. The Antislop project ships its human baseline — 6.11 billion characters — next to its findings, so the released lists can be checked against the corpus that produced them, and almost nobody does it. The check is unflattering to anyone using those lists as prohibitions. Eight of the ten most frequent bigrams in human creative writing are on the anti-slop list, `could see` and `shook head` at the top of both; 96% of the released slop bigrams are ordinary common English, and the highest-ranked slop trigram is the single most common trigram humans write. Only 15% of the n-grams have no human rate at all, and that minority — narrating resolve, decorating scenery with participles — is the only part safe to treat as a flat ban. More than half the word list never occurs in the human corpus's common bigrams at all, and most of that is invented fantasy proper nouns and borrowed franchise vocabulary, including the name of the subreddit the corpus was scraped from, which is a list absorbing its own collection method. Coverage is also thinner than the count suggests: 74% of the trigrams merely extend a listed bigram, and one invented stem consumes twelve of the thousand word slots. Across the 38 profiled models slop correlates with repetition at +0.83 and with vocabulary complexity at +0.01 and length at +0.05, which kills the two folk theories that slop means ornate diction or padding. Within one model family it declines monotonically from 1B to 405B. Across those 38 profiles the spread is 3.4x, which reads as evidence that there is no single machine voice to write against — but that is only half the picture, and `ai-slop-research` corrects it from the appendices the earlier note had not read: `flickered` appears on 98.5% of 67 models' lists. There is a shared core across essentially every model with model-specific tails around it, so a list built from one model is parochial at its edges and close to universal at its center. Either way the tells have a shelf life.

`audience/` is complete across all seven tiers, authored full and unbudgeted for 1.0.0. `citation/` is complete across all six styles, authored full against the editions current as of August 2026: MLA 9, APA 7, Chicago 18, AMA 11, Bluebook 22, and the 2025 IEEE Reference Guide. `bluebook22` is the longest at 1,514, close to half again the size of `mla9`, which is what a style with signals, pincites and cross-references costs to state correctly. Every rule was drafted from a per-style research pass, re-audited against it, and then re-verified a third time in August 2026; the passes caught roughly two dozen errors between them, which is the argument for doing citation work this way rather than from recall.

`domain/` is complete across all eight, re-authored full at 2.0.0 after a first pass that hit the stub's 400-token budget and was the wrong artifact for it — the same correction `core/` and `audience/` already made. 19,017 tokens combined, 1,958 to 2,705 each, so compression is the next task there. The `budget` field moved from 400 to the measured size in the same pass: 400 predated the layer having a `## Formats` section, which carries three or four sub-genres and roughly a third of every module. Once that section existed the ceiling was abandoned rather than raised, so `budget` here records what each module measures, as it does in every other layer. Whether `domain/` should carry a target at all is the one thing here worth a second opinion.

What the compressed pass cost is the argument for the convention. It dropped datelines and wire conventions that `sources/ap-stylebook.md` explicitly assigns to `press`, the Bluebook signal grammar, the Diátaxis mode error, and the identity-first exception in `medical` — each a rule the shorter module had no room to state and no way to state partially. Only one domain module loads at a time, so a combined set is roughly 11,000 tokens, not 19,017.

`marketing` repeats phrasing from `sources/` in eight places, all of them the named constructions it exists to ban — *say goodbye to X*, *unlock the power of X* — which have to be quoted exactly to be detected, and which `user-interface/website.md` quotes on the same footing. `core/anti-slop.md` does the same for a different family, the negative parallelism of *not just X, but Y*. `press` names the eight states AP never abbreviates, which is a rule that cannot be stated without naming them.

Five domain decisions worth recording, because each cuts against a core rule or a layer boundary. `legal` keeps hedging: *likely* and *a court would probably* are the product there, not slop, and the module asks only that the hedge name the fact that would change it. `medical` treats overstated certainty as a safety defect rather than a style one, which is why it demands absolute risk beside relative and a red-flag route to care in anything patient-facing — and it refuses blanket person-first language, because the autistic and Deaf communities largely prefer identity-first and a rule that overrides a stated preference has failed at the thing person-first language was invented to do. `fiction` sets aside `core/formatting.md`'s structural apparatus — headings, lists, tables, which narrative does not use — and inverts the essay habits `core/` otherwise assumes: no thesis, no takeaway, no summary. Its single hardest test is that slop cannot stop itself explaining its own subtext. `marketing` was rebuilt around substantiation once `user-interface/website.md` took the page surface: that module owns the hero, the kicker and the stat row, this one owns whether the claim is true, in every medium. Its organizing fact is that marketing is the only genre where the evidence must exist before publication as a matter of law and where the reader never sees it — and its organizing argument is that puffery is non-actionable precisely because no reasonable consumer relies on it, which is the law's way of saying the claim cannot be checked.

One precedence nuance surfaced and is stated in `academia` and repeated in the regulated modules. `audience/` wins over `domain/`, but what it wins is register. A patient handout written for a non-specialist gets shorter sentences and plainer words; it does not get a softer truth obligation. Audience governs how it reads, domain governs what may be claimed.

`user-interface/` is complete across all five modules, authored full for 1.0.0. Nothing here loads all five at once: two are media and you pick one, three are overlays and you add what applies. `applications` is the longest at 1,702, because it carries nine surfaces and a product has more places to put a sentence than a page does.

Its evidence base is three dossiers written for it: `apple-hig` from a 156-file mirror of the guidelines, plus `stop-slop` and `kill-ai-slop`. Three modules repeat phrasing from `sources/`, on the same footing as `domain/marketing.md`: `website` in twenty-four places and `applications` in seven, all of them the invented stat rows and stock openers those modules exist to ban, which have to be quoted exactly to be detected. `apple-hig` repeats one sentence of button mechanics from its own dossier — the rule is four words long in any phrasing that is still correct.

Three decisions worth recording. The axis is cut by medium rather than by widget, which was the second attempt — a first pass produced twelve surface-named modules, and every one of them ended up hedging between an app and a web page. A later review found the true seam is what the reader has committed to rather than the technology they arrived by, which is why the logged-in half of a website is `applications`; the medium labels are kept because they are what a writer reaches for, and each module's `## Boundaries` states the commitment test outright. And `accessibility` sits alongside the media rather than inside them, because the copy it governs is the only copy some readers get, and folding it into `applications` would have made it optional in exactly the projects that skip it already.

The Apple guidelines are documentation for a platform, not a style manual, so `apple-hig` states the conventions and `sources/apple-hig.md` records where they are inferred rather than sourced. The gaps worth knowing: Apple says almost nothing about empty states, and its accessibility guidance covers what to label without giving the wording.

Verified current as of August 2026: WIDA ELD 2020 remains the standing edition, and the Consortium now runs to 42 states, territories and federal agencies — New York joined as the 42nd and begins ACCESS testing in 2026-2027. Massachusetts and New Jersey are both members, New Jersey since 2005. CWPA approved Outcomes Statement 4.0 on 2026-03-04; `undergraduate.md` cites both 3.0 and 4.0 while 4.0 propagates. The one pin that is knowingly stale is AP: this repo was built from the 56th edition, and the 58th, 2026-2028, was released in May 2026. It expands the artificial-intelligence chapter and adds *AI agent*, *AI slop* and *vibe coding* — entries that bear on `core/anti-slop.md` — and closes *healthcare* to one word. Reading the 58th against `sources/ap-stylebook.md`, `domain/press.md` and the seven `audience/` tiers is the largest outstanding task in the repository. Until that happens, `domain/press.md` carries the pin and the two known changes in its own body, because `sources/` never loads alongside a draft and a caveat nobody sees is not a caveat.

Three citation findings worth recording, because each reverses something a model is likely to assert confidently. IEEE abolished the bracketed range — `[1]-[4]` is now written `[1], [2], [3], [4]`. Chicago 18 cut the author threshold in a note to two, so three authors already take `et al.`, and it retired the 3-em dash for repeated names. APA revised its generative-AI formats in September 2025, adding a `[Generative AI chat]` descriptor and superseding the 2023 ChatGPT guidance still in wide circulation.

Bluebook 22 carries one open question, narrowed but not closed in August 2026. Law library guides at BYU, Richmond and Georgetown, plus TypeLaw, agree that rule 18.2.1(d) *requires* an archival link or an "on file" parenthetical for every internet citation, where the 21st edition merely encouraged it — and they read it as reaching every internet source, not only volatile ones. Six independent guides keyed to the 22nd edition say "requires" or "must"; one BYU post says "should," which is most likely a softened paraphrase but cannot be excluded as the rule's actual word. The rule text is subscription-walled and has never been read directly here. `bluebook22.md` states the requirement and marks the on-file statement as a fallback rather than a co-equal option; confirm against the manual before relying on it in a filing.

## Refresh

This repository is re-verified monthly. Most of what it cites does not move, and checking everything every month is how a review becomes a ritual that stops catching things. The split below is what the August 2026 pass produced.

Check every month, because these moved within the last year or move on no schedule at all. The **AP Stylebook** edition and its year span — AP publishes in late May of even years, the 58th covers 2026-2028, and this is the pin that went stale. The **Apple Style Guide**, reissued each June, and the OS generation each September. **arXiv preprint versions**: read the submission-history block, not just the abstract, because `2603.27249` gained two versions and a new title in one quarter. **Wikipedia:Signs of AI writing**, edited several times a week. The **IEEE Reference Guide**, which is a live document with no change log. **Generative-AI citation guidance in every style**, the fastest-moving category here. **WIDA consortium membership**. **FTC Green Guides** and the Part 465 rule. **ICMJE Recommendations**, whose AI section is the volatile part. **WCAG 3's** draft status. And the two prescriptive skill files, which are active repositories where a single commit changes a tell count.

Check annually, or when something announces itself. Case law and the actual-malice doctrine. ABA Model Rule numbering. The Plain Writing Act. WCAG 2.2 success criteria. The Framework for Success in Postsecondary Writing and its habits of mind. STROBE, CONSORT and PRISMA. ISO 24495-1. The 1984 FTC substantiation statement. AAC&U VALUE dimensions. The frozen Antislop banlist files. And the edition *numbers* of MLA 9, APA 7, Chicago 18 and AMA 11 — the editions are stable even while their AI guidance is not.

Two standing cautions for whoever runs the pass. A style manual behind a subscription wall has never been read directly here; where a rule rests on secondary guides, the module says so, and that hedge is not decoration. And when a source corrects itself, correct the correction rather than overwriting it — `sources/ai-slop-research.md` carries three provenance corrections and one correction of a correction, which is the honest shape of a file whose subject is accuracy.
