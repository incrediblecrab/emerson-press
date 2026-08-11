---
id: sources.ai-slop-research
layer: sources
version: 2.0.0
status: active
budget: none
retrieved: 2026-08-09
consumers:
  - core/anti-slop.md
  - core/restraint.md
  - core/accuracy.md
  - core/voice.md
  - domain/academia.md
  - domain/fiction.md
  - domain/technical.md
---

# Source: The Research Literature on AI Slop

Evidence base for the parts of `core/` that make empirical claims. Every other note in `sources/` records a *practice* — what editors flag, what a stylebook prescribes, what a skill file bans. This one records *measurement*: what has actually been counted, by whom, on what sample, and with what result.

That distinction matters more than it sounds. Most anti-slop advice in circulation, including two of the skill files this repo draws on, is assertion. It is often good assertion. But when a rule here conflicts with a rule there, this note is what settles it, and several of these findings overturn something the practice literature takes for granted.

## The Status Caveat, Read First

Two of these four documents are arXiv preprints and neither had completed peer review at the time of retrieval. The third is an unpublished author manuscript. The fourth is arXiv's own moderation announcement, which is primary and institutional rather than empirical.

Three provenance corrections, because the first version of this note got them wrong and a note about accuracy has no business being loose about its own citations:

- **Miklian and Katsos is an arXiv paper, and the note previously said otherwise.** An earlier revision de-listed it on the grounds that the PDF carried no arXiv stamp. That was wrong. arXiv's own metadata records `citation_arxiv_id` 2606.12073, authors Jason Miklian and John E. Katsos, submitted 10 June 2026. Cite it as `arXiv:2606.12073`. The mistaken de-listing is recorded here rather than quietly removed, on the same principle that put this section in the file. It is still a preprint and still not peer reviewed.
- **Baltes, Cheong and Treude was retitled between versions, and an earlier revision of this note pinned the wrong one.** v1, 28 March 2026, was subtitled *The Growing Burden of AI-Assisted Software Development*; v2 and v3, June 2026, carry *How Developers Discuss the Burden of AI-Assisted Software Development*. This note previously asserted, emphatically, that v1 was current and that the v1 subtitle was the correct one. That was already false when it was written. Cite v3. The correction of the correction is left visible for the same reason the first one was.
- **The Antislop paper discloses its own LLM assistance** in drafting, and states that results and citations were human-produced and human-validated.

There is an obvious irony in building an anti-slop evidence base largely out of unreviewed work on the very platform that had to restrict submissions because of a flood of machine-written papers. It is worth naming rather than hiding. The mitigation is the one `core/accuracy.md` prescribes: attribute every number to the study that produced it, state the sample, and never launder a preprint finding into a bare fact.

One unverified claim, excluded up front. Several news aggregators report that arXiv now imposes a one-year submission ban for egregious AI-generated submissions. That specific sanction could not be confirmed against arXiv's own policy pages, which were read directly. It is not used below.

## 1. Slop Is a Rate, Not a Word List

**Paech, Roush, Goldfeder, and Shwartz-Ziv, arXiv:2510.15061v2.**

The single most useful contribution here is a definition that can be computed. Slop is not a set of bad words. It is an **over-representation ratio**: how often a pattern appears in model output, divided by how often it appears in a human reference corpus. Their human baseline is the `wordfreq` library for single words, and a mix of Reddit creative writing and public-domain Gutenberg texts for n-grams. Two thousand generations per model, from Reddit writing prompts. Stop words are removed before n-gram extraction.

Measured ratios for `gemma-3-12b`, from their Table 1:

| pattern | over-representation |
| --- | --- |
| `elara` | 85,513x |
| `unsettlingly` | 3,833x |
| `shimmered` | 2,882x |
| `stammered` | 2,043x |
| `heart hammered ribs` | 1,192x |
| `voice trembling slightly` | 731x |
| `said voice devoid` | 693x |
| `felt profound sense` | 550x |
| `it's not X, it's Y` | 6.3x |

An earlier version of this note recorded the extreme end as "10³–10⁵, from secondary coverage." That hedge can go. The number is 85,513x and it is in the paper.

A thousandfold over-use is not a stylistic preference. It is a fingerprint. This is the quantitative version of the account in `sources/field-guide-to-ai-slop.md`: the model regresses to the mean, and the mean is narrow.

## 2. What the Two Thousand Patterns Actually Are

This is the section the earlier note lacked, and its absence let a slogan stand in for a structure. "Token banning becomes unusable at two thousand patterns" was quoted here for a year without anyone recording what the two thousand *were*. Their composition is published, in the configuration file at the paper's Appendix M, and it is more interesting than the headline.

One caution before the table. The 2,000 below is a *per-run pipeline quota*. The lists the project actually released and froze are smaller — 1,000 words, 200 bigrams, 200 trigrams — and their contents have been analyzed directly against the project's own human baseline in `sources/antislop-banlists.md`. Read that note before treating any entry here as a rule; the released bigram list contains eight of the ten most common bigrams in human creative writing.

### The composition is exact

| pattern class | in human corpus | not in human corpus | total |
| --- | --- | --- | --- |
| single words | 920 | 80 | 1,000 |
| bigrams | 300 | 200 | 500 |
| trigrams | 300 | 200 | 500 |
| **total** | **1,520** | **480** | **2,000** |

Half the list is single words. The other half is two- and three-word phrases. There are no longer phrases in it at all: whole-phrase banning exists in the pipeline and its quota is set to zero in this configuration.

**The split down the middle column is the part worth carrying.** The pipeline distinguishes patterns that also occur in human writing from patterns that occur in the human corpus *not once*. For the second group the ratio is not large, it is undefined — there is no human denominator. Those 480 are the constructions a model produces that essentially nobody else does, and they are 24% of the list.

Selection thresholds, since a ranked list is only as good as its cutoffs: words shorter than three characters are excluded; the top 5,000 bigrams and top 5,000 trigrams are scanned, against the top 200,000 words; a pattern must appear across at least three independent prompts to qualify, so that one story's character name cannot carry it. `elara` cleared that bar, which is the finding rather than an artifact.

### What is in them

The paper profiled 67 models and reported which patterns recur across their fingerprints. Regrouped here by the job each word is doing, rather than reproduced in the source's ranked order — the same treatment `sources/ap-stylebook.md` gives a cliché list:

- **Light and motion, the dominant family.** `flickered` appears in the top-120 over-represented list of **98.5% of 67 models**, with `flicker` at 94.0% and `flickering` at 92.5%. Three inflections of one verb are the most reliable machine tell measured anywhere in this literature.
- **Speech attribution that avoids `said`.** `muttered` and `murmured` (82.1%, 73.1%), `whispered` (68.7%).
- **The face and the body doing the emotional work.** `leaned` (82.1%), `gaze` and `grinned` (80.6%), `gestured` (77.6%), `nodded` (73.1%), `glint` and `hesitated` (68.7%), `blinked` (64.2%), `leans` (62.7%).
- **Hedged perception.** `faintly` (62.7%), `unreadable` (62.7%), `hummed` (64.2%).
- **Register intrusions with no business in fiction.** `containment` (77.6%) and `addendum` (74.6%) — bureaucratic nouns surfacing in creative prose, which is a different failure from the others and probably the most diagnostic of the set.

The recurring trigrams, grouped the same way:

- **The whisper complex.** `voice barely whisper` (68.7% of models), `said voice low` (61.2%), `said voice barely` (35.8%), `voice barely audible` (35.8%), `says voice low` (26.9%). Five variants of one gesture.
- **Breath and heartbeat as emotion delivery.** `took deep breath` (44.8%), `take deep breath` (32.8%), `heart pounding chest` (25.4%).
- **Atmosphere by thickness and shadow.** `air thick scent` (49.3%), `casting long shadows` (28.4%), `long shadows across` (19.4%), `air thick smell` (19.4%).
- **Gaze held past the point of meaning.** `eyes never leaving` (29.9%), `smile playing lips` (43.3%), `spreading across face` (22.4%).
- **Vagueness with the cadence of precision.** `something else something` (37.3%), `something else entirely` (26.9%), `could shake feeling` (31.3%), `could help feel` (19.4%).

That last group is the one `core/anti-slop.md` should care about most. The others are creative-writing furniture. `something else entirely` and `couldn't shake the feeling` are gestures at specificity that deliver none, and they transfer to functional prose intact.

Scale, for a sense of the density: one 24B model produced `eyes never leaving` 102 times and `voice barely whisper` 62 times across 96 prompts.

### Two corrections these lists force

**Slop is both universal and model-specific, and the earlier note recorded only half.** The paper's body says fingerprints cluster within model families and differ between them, and the earlier note took that as the whole story. Appendix K and the cross-model tables say the opposite is also true: `flickered` is on 98.5% of 67 models' lists. There is a shared core across essentially every model, with model-specific tails around it. A list built from one model is dated and parochial at its edges and close to universal at its center.

**Every one of these patterns comes from creative writing, and the paper says so.** The prompts are Reddit writing prompts; the baseline is Gutenberg fiction. The authors state the method is bound to whatever domain you profile — point it at a different genre and a different set of tics comes back. What a short story over-uses is not what a specification over-uses. So the widely circulated slop word lists — this repo's included — are *fiction* lists being applied to memos, documentation, and marketing copy. That is a real limit on transfer, and `core/anti-slop.md` should not pretend a list derived from short stories was measured on anything else.

### The suppression numbers, restated correctly

The abstract's claim is that the sampler suppresses 8,000+ patterns with quality intact while token banning becomes unusable at 2,000. The measured curve behind it: token banning falls to **28 out of 100** on their writing rubric at an 8,000-pattern list. The reason is mechanical rather than aesthetic. Bans fire on a token, and tokens are shared — banning `catatonic` when it tokenizes as `cat` + `atonic` bans every word beginning `cat`. The sampler instead waits until a full banned sequence has appeared, backtracks to its first token, multiplies that token's probability by 10⁻¹⁰ˢ, and resamples.

Three results from that design bear directly on `core/restraint.md`:

**Conditional suppression measurably beats unconditional.** The ban-strength parameter `s` runs from 0 to 1, where 1 is a hard ban. At **s = 0.4** the sampler suppressed the patterns in 90% of ordinary generation while permitting them *fully* when a prompt explicitly asked for them. Their test for this is neat: instruct the model to use the banned phrase exactly three times, and see whether it can. A hard ban cannot. A conditional one can. This is the closest thing to a direct measurement of the position `core/restraint.md` already held.

**Maximum suppression destroys the writer, and the trade is quantified.** In their ablation, removing the safeguard that switches off training pressure once a preference is won raised suppression to 98.24% and dropped writing quality from 67.80 to **19.57**. Pushing the other way, tethering too hard held quality at 69.68 and cut suppression to 55.86%. Overcorrection is not a worry someone invented to be contrarian; it is a measured curve with a bad end.

**Even a purpose-built ban needs exceptions to survive contact with real prose.** Their regex family for the `not X, but Y` construction is five expressions, and the primary one carries more than thirty hand-written exclusions — it declines to fire before `right`, `normal`, `true`, `sure`, `still`, `already`, and a long tail of ordinary verbs, plus any adverb. Someone had to carve those out by hand because the construction is not always wrong. The most-cited banned construction in the whole anti-slop literature could not be expressed as a rule without an exception list longer than the rule.

### Three rules the tooling states more plainly than the paper

The pipeline is published under MIT license, and its documentation is blunter about the method's limits than the write-up is.

**No suppression without an alternative.** When the sampler halts on a banned pattern it gathers replacement candidates, and if nothing coherent survives the filter it throws the whole event away rather than record it. The system declines to learn a prohibition it cannot pair with a replacement. That is the design principle `core/restraint.md` should be stated in terms of: a rule that removes something without saying what goes there instead is not a rule, it is a hole. Every ban in this repository should be readable as a substitution.

**Slop is adaptive, so one pass is never enough.** The loop runs at least twice by design — profile, ban, then regenerate *and profile again*, because suppressing the first set surfaces a second set that was sitting underneath it. A model deprived of `flickered` reaches for the next thing. This is the strongest argument available against treating any published list as finished, including the ones in `sources/`. The list is a photograph of one layer.

**The prompts decide the findings.** The documentation says outright that the kind of prompts you use determines the slop that comes back. Section 2's domain caveat is not an inference from a method note; it is how the tool is meant to be operated. Profile marketing copy and you get marketing slop, which nobody has published.

The artifacts also confirm the structure described above rather than implying it: dictionary and non-dictionary n-grams are written to separate ranked files, so the distinction between over-used and never-otherwise-used is a real seam in the analysis rather than a quirk of one configuration.

### What this does not license

The paper measures inference-time and training-time interventions on model weights. `emerson-press` is a prompt-layer artifact and can do neither. The findings transfer as *reasoning about what slop is and how suppression fails*, not as technique. Nothing here says a style module achieves 90% of anything.

## 3. Accusation Does Not Track the Evidence

**Miklian and Katsos, arXiv:2606.12073.** The most consequential finding in this note, and the most uncomfortable.

Method: 25 million Hacker News and Reddit comments, January 2023 to May 2026 — 12 million from HN, 13 million across 18 subreddits. A 137-pattern lexicon in five tiers, validated by per-comment LLM judgment on 7,500 sampled comments; 300 confirmed accusations coded by speech act; and a matched-control comparison of 421 accused parent comments against 2,048 non-accused controls drawn from the same subreddit-month and length band.

**The register grew and displaced its predecessor.** Pejorative-label share rose from 1.5% to 24.4% on Reddit and 2.5% to 26.6% on HN, running roughly parallel with HN two to four points ahead throughout. As a share that is a sixteenfold rise on Reddit and close to elevenfold on HN. A placebo lexicon of pre-2022 inauthenticity words — `shill`, `astroturf`, `sockpuppet` — *fell* over the same window, from 8.3% to 5.3%. The control is what makes the result credible: this is a specific new suspicion, not a general rise in online hostility. Within the pejorative tier, the slop frame went from 12.9% of framings in 2023 to 93.8% in 2026, displacing `drivel`, `garbage`, `word salad` and the rest rather than joining them.

**The tone hardened and the speech act migrated.** Mockery fell from 25.9% of accusations to 7.1%. Gatekeeping rose from 1.9% to 16.5%. Structural protest — objecting to the phenomenon rather than the comment — went from 14.8% to 38.8%.

**The finding that matters.** Six prose markers cleanly separate machine-generated comments from human-written ones, three of them reported here with figures: 30% lower contraction rate, 2.3x the formal-adverb density, 2.9x the sentence-length variance, all at p < 1e-9. Then the same six markers were run on accused human comments against matched non-accused human comments. **None of the six that distinguished machine text predicted accusation.** What predicted accusation instead was body length (longer, odds ratio 1.21) and *shorter* average word length (odds ratio 0.78) — the second one pointing the opposite way from the real signal.

A scope caution on the variance figure, because it appears to contradict `core/rhythm.md`'s founding premise that machine prose is metrically flat. It does not, and the reason is the comparison population. This corpus is forum comments, where the human baseline is a short reply of one or two clauses; a machine-generated comment in the same thread is a multi-paragraph expository block that mixes long sentences with short ones, so it registers as more variable. `core/rhythm.md` is about drafted prose of comparable length and ambition, where the observed failure is the opposite — a run of sentences all landing near the same weight. Neither claim generalizes to the other's population, and a future revision of `rhythm` should say which one it means rather than treating 2.9x as a refutation.

Also worth keeping straight: the stylistic-tell callout — the em dash, the `delve` complaint, the tricolon — is among the *least* reliable tiers in their data, confirmed as a genuine accusation only 17% to 35% of the time depending on platform. The people invoking the tells are frequently not even making the accusation they appear to be making.

### What this means for a style repo

It removes one motive for this project and sharpens another.

**Writing to avoid accusation runs into a floor.** Be exact about where the floor comes from. The matched control compared accused against unaccused *human* comments, so it measures who draws suspicion within the human range. It does not measure what happens when machine-typical prose — which the same study shows sits outside that range — is revised toward it. A null association among humans is also not proof of no causal effect.

What the evidence does support is narrower and still decisive. A large share of accusation is social gatekeeping and in-group signaling that never closely reads the text it is about. No revision reaches that share. The authors name the exposed population, and it is the careful writer: sparing with contractions, high in formality, clean at the surface — the profile a lay reader now takes for machine work, whatever produced it. A module sold as protection against being called a bot is selling something the data cannot deliver.

**Writing well remains entirely winnable.** Every tell in `core/anti-slop.md` is independently a defect: vague where it should be specific, inflated where it should be measured, hedged where someone should take a position. It was worth fixing before anyone was accused of anything. That is the ground `core/` should stand on, because it is the ground that does not wash out.

**A reader's suspicion is not evidence.** `core/restraint.md` already says detection is unreliable. This adds that accusation is frequently not *attempting* detection. That is a warning to anyone using these modules as a checklist against another person's writing.

The authors also separate the reader side from the writer side. `core/` is a writer-side instrument and cannot fix a reader-side social dynamic.

## 4. The Cost Lands on Someone Else

**Baltes, Cheong, and Treude, arXiv:2603.27249v3.** Qualitative coding of 1,154 posts from 15 Reddit and Hacker News threads into 15 codes across three clusters — Review Friction, Quality Degradation, Forces and Consequences. 978 posts drew at least one code, yielding 1,603 codings. Coding was done with LLM assistance under human decision authority, across four review rounds and 234 post-level revisions, which the paper discloses as a threat to validity.

Their organizing claim is the useful part: this is a **tragedy of the commons**. The individual producing slop gains; the costs land on reviewers, maintainers, and everyone downstream. Cheap to generate, expensive to read.

What the code frequencies say about the discourse: the three largest codes are structural drivers (26.2%), tool limitations (23.2%), and mitigations (23.1%). Sarcasm ranks fourth at 15.8% — irony is not a garnish on this conversation, it is a sixth of it.

Observations worth carrying:

- **Goodhart's Law in the incentives.** Contribution graphs, bounty payouts, and search ranking reward volume over worth, so volume is what they get.
- **Adoption is often imposed** rather than chosen. The paper's title phrase comes from a developer describing a mandated tool rollout.
- **The asymmetry is measurable in workload.** One team reported 30 pull requests a day across six reviewers.
- **The failure modes are specific.** An agent that hallucinated external services and then mocked out the services it had hallucinated, producing an internally coherent and entirely fictional integration. Another that skipped authorization in middleware and then mocked out authorization in the tests so they would pass.
- **The mitigations are concrete and transferable**: a size ceiling per change, mandatory self-review before asking for peer review, a synchronous walkthrough where the author explains their choices, and the norm that ownership never transfers to the tool.
- **Craft erosion, and specifically an inversion**: the enjoyable work gets automated and the cleanup is what remains.
- **The deskilling loop.** Using these tools well requires experience that was acquired without them.

### What this means for a style repo

It supplies the ethical spine the rest of the repo argues around without quite stating. The reason to cut a hollow paragraph is not that it looks machine-written. It is that somebody has to read it. Every unearned word is a small tax levied on a stranger who did not agree to pay it.

This is also the honest answer to *why bother*, and a better one than evading detection, which finding 3 took away.

## 5. The Institutional Consequence Arrived

**arXiv, 31 October 2025**, plus arXiv's standing moderation policy, both read directly.

The change: review and survey articles and position papers in arXiv's CS category must now be accepted at a peer-reviewed journal or conference *before* submission, with documentation. Without it, they will likely be rejected.

Points that are easy to garble:

- **Technically, nothing changed.** Neither content type was ever on arXiv's list of accepted submissions. Both had been taken at moderator discretion, because the few that arrived were good.
- **The stated cause is volume, not machine authorship as such.** Hundreds of review articles now arrive monthly, and arXiv describes the majority as "little more than annotated bibliographies, with no substantial discussion of open research issues."
- Workshop-level review is explicitly stated not to meet the bar.
- Papers *studying* technology's social impact are unaffected, which is why the preprints above were postable.

arXiv's standing generative-AI policy, separately: significant use of text-to-text tools must be reported; authors take "full responsibility for all its contents, irrespective of how the contents were generated," including fabricated references; and such tools must not be listed as authors.

### What this means for a style repo

**"Annotated bibliography with no substantial discussion" is a structural diagnosis from a body that reads at scale, and it is exactly what `core/anti-slop.md` calls structure standing in for content.** Complete scaffolding, correct sections, real citations, nothing argued. An institution independently arriving at the same description is decent evidence the tell is real.

**Full authorial responsibility regardless of generation** is the rule `core/accuracy.md` operationalizes. Verification is the price of putting a name on the work.

**Disclosure is orthogonal to style.** No module should imply that writing well substitutes for saying a tool was used, or that disclosure is required where it is not. That is a venue question.

## What `core/` Takes

| finding | module | how it lands |
| --- | --- | --- |
| Slop is an over-representation ratio | `anti-slop` | density framing, not word bans |
| 85,513x at the extreme, measured | `anti-slop` | the mechanism is real, lists are its symptoms |
| 24% of banned patterns never occur in human text | `anti-slop` | the sharpest tells have no human denominator |
| `flickered` on 98.5% of 67 models | `anti-slop` | a shared core exists beneath the model-specific tails |
| Vagueness trigrams transfer, scenery does not | `anti-slop` | which half of a fiction list is worth importing |
| Every published list is creative-writing derived | `restraint` | states the limit on transfer to functional prose |
| Token banning collapses to 28/100 at 8k | `restraint` | empirical basis for refusing unconditional bans |
| Ban-strength 0.4 suppresses 90%, permits on request | `restraint` | conditional beats unconditional, measured |
| Removing the safeguard: 98% suppression, quality 19.57 | `restraint` | overcorrection is a measured curve |
| The `not X, but Y` regex needs 30+ exceptions | `restraint` | no worthwhile ban survives without judgment |
| A ban with no viable alternative is discarded | `restraint` | every prohibition must name a substitution |
| Suppressing one layer surfaces the next | `restraint` | no published list is ever finished |
| Accusation ignores the real features | `restraint` | evasion is not an achievable goal |
| Stylistic-tell callouts are the least reliable tier | `restraint` | the em-dash complaint is noise |
| Reader side ≠ writer side | `restraint` | `core/` is writer-side only |
| Tragedy of the commons | `anti-slop` | the reason the rules exist at all |
| Annotated bibliography, nothing argued | `anti-slop` | structure standing in for content |
| Full responsibility regardless of tool | `accuracy` | verification is not optional |
| Fabricated references are the author's | `accuracy` | citations that cannot be checked |

## What `core/` Deliberately Does Not Take

- **Any technique from the Antislop framework.** Sampler backtracking and token-level fine-tuning operate on weights and logits. A prompt-layer module has neither, and borrowing the vocabulary would overstate what these files do.
- **The banlists themselves as a word list.** They are fiction-derived, model-dated, and 1,000 of the 2,000 entries are single words whose only offense is frequency. `core/anti-slop.md` takes the vagueness family and the reasoning, and leaves the scenery.
- **Any promise about detection outcomes.** Finding 3 forecloses it.
- **The workforce and labor material** in Baltes et al. It is real and it is not a writing rule.
- **Disclosure requirements.** Venue policy, not house style. If it belongs anywhere it is `domain/academia.md`.
- **The unverified one-year ban.** Not confirmed at the source.

## Limits of This Note

All three papers were read in full for version 2.0.0, appendices included. The earlier version was built from abstracts and secondary coverage, and its stated limits said so; that is what let three citation errors and a missing structural finding survive in a note whose whole purpose is settling disputes about evidence. The corrections are recorded in the status caveat rather than quietly applied.

What remains uncertain is unchanged. Two of the four documents are unreviewed and one is unpublished. Two study Hacker News and Reddit specifically, which are not a sample of writing in general and skew technical, male, and English-speaking — a limitation the accusation finding in particular should be read against, and one the authors name themselves, along with the observation that `slop` is a lexically English pejorative whose equivalents in other languages may not have consolidated the same way. The Antislop measurements are creative-writing measurements, stated as such above and easy to forget one section later.

The rules in `core/` were derived independently from editorial practice, and most of this note only tells you which of them now have measurement behind them. But two findings are load-bearing. The accusation result is why `core/restraint.md` and the README refuse to frame any module as evading detection. The suppression curves are why this repo refuses unconditional bans on constructions — including the ones its competitors ban outright. Where a finding moves a rule, the honest record says so and carries the caveat with it.
