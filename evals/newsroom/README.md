# Newsroom writing backtest

The question is whether repository-guided writing reduces noticeable generic
AI-style prose and improves the specificity, progression and natural voice of
a newspaper story. AP supplies mechanics. Factual fidelity is a separate guardrail,
not the entire definition of good writing.

## Comparison and evidence

`bare-task` supplies the same ordinary brief and reporting packet without any
repository writing contract or modules. `task-only` adds the repository contract;
`full` and `compact` add their corresponding press recipes. A comparison against
`task-only` alone cannot establish the effect of using the repository.

The new corpus includes [12 tuning stories](tuning-index.json) and a planned
220-case primary collection whose independent-family count is still under review.
These are substantial news updates, explainers and reported features, not UI
labels or citation exercises. A rich
packet should support the requested length without padding; nonessential facts
need not all appear in the story. Each case needs an explicit reporting snapshot
date so a runtime's current date does not silently change the task.

The 12 tuning packets contain 252 numbered fact entries across straight news,
business/labor, explainers and reported features, with three cases in each group.
Their briefs explicitly identify a fictional writing exercise; the source record
is not real reporting, legal authority, medical advice or current market data.
Before any writing generation, a source-quality review corrected worker totals,
a strict placement threshold, combined-issuer attribution, budget/spending and
denominator confusion, blood-component scope, and overbroad legal and regulatory
claims. Unsupported general statistics were scoped to fictional source records.
This is input cleanup, not evidence of a writing-model improvement.

The [prospective tuning design](tuning-design.json) freezes those packets and
plans 72 drafts: GPT-6 Astra and Claude Sonnet 5 each write under bare, full and
compact instructions. It also fixes the opposite-family judges, all three paired
contrasts and separate pointwise assessments. These current available models were
selected before treatment outcomes; earlier mini/Haiku stress trials remain
separate. This registration contains no results and does not authorize a
held-out run or establish a statistically powered sample.

All 72 planned drafts have now been captured and checked against that registration,
with matching model/settings and zero observed tool calls. They are retained in
`artifacts/modern-tuning-writing.jsonl.xz`, and [every unchanged draft is readable](examples/tuning-modern/README.md).
Complete transport coverage is not a quality result.

Case count is not independent sample size. Reused events and templates must stay
in the same family and split. Freeze the actual family map, candidate recipe,
model settings, primary contrast, grading protocol and statistical plan before
any primary held-out generation. No such held-out writing result is available yet.

All 220 input packets have received bounded within-shard model source reviews
and parent checks of coverage, source bindings and recorded changes. This is not
external verification of every scientific, financial or legal claim.

| Input shard | Cases | Provisional families | Fact entries |
| --- | ---: | ---: | ---: |
| [Civic](civic-index.json) | 74 | 73 | 1,628 |
| [Science](science-index.json) | 73 | 68 | 1,456 |
| [Business](business-index.json) | 73 | 73 | 1,460 |
| **Total** | **220** | **214** | **4,544** |

The final cross-shard/tuning-family review and power plan remain unfinished.
Shared programs and conservative template clusters reduce the family count;
neither the remaining labels nor the source audits prove independence.
The [mean-inference component](mean-inference.md) documents a finite-sample
candidate method and its randomization, missingness and independence limits.
It is not a primary-study registration or a writing result.

The [civic source-review bundle](artifacts/civic-source-review-manifest.json)
retains the exact before/after packets and index, the unchanged model audit and
separate parent decisions. One source sentence now distinguishes a three-week
watering trial from a rotation-cycle length. A claimed enrollment problem was
rejected because it conflated current pupil totals with future projections; the
auditor also supplied an incorrect weekday. These are input and reviewer
corrections, not evidence that the writing instructions work. The
[measured summary](artifacts/civic-source-review-summary.json) records no primary
writing outputs and no human reviews.

The [science bundle](artifacts/science-source-review-manifest.json) retains both
original model audits, literal-evidence checks and separate parent arbitration.
Six packets received source revisions: among them, an overdue-inspection
calculation and speed-limit conflict, incompatible Apex observatory timelines,
an unsupported first-approval claim and unverified background rules/statistics.
The withdrawn transmission-loss percentage also required changing its associated
check. The [summary](artifacts/science-source-review-summary.json) distinguishes
these revisions from writing-model errors. Two nonliteral audit quotations and
a mistaken claim that snapshot dates were absent remain visible in the evidence.

The [business bundle](artifacts/business-source-review-manifest.json) preserves
all 73 packets and the index unchanged. Its model audit proposed no grounded
corrections or within-shard mergers; that is not a certification of error-free
sources or an independent sample. The [summary](artifacts/business-source-review-summary.json)
keeps those limits explicit. No source-review record is a human assessment or a
primary prose-quality result.

The first live smoke check uses the one pre-existing substantial press-drafting
tuning case in the broad regression suite: the Bay Cross timetable explainer.
Eight real responses cover two writers and four recipes, including the genuinely
untreated control. Its brief already has strong source constraints, so it is not
a representative efficacy sample. The records are retained in
`artifacts/starter-writing.jsonl.xz`.

All eight outputs are also [readable as unchanged text files](examples/transit/README.md).
On this one case, the blinded pairwise judges preferred both full and compact
over `bare-task` for both writer models. Full versus compact split by writer.
This is a small positive preference signal, not four independent wins or evidence
that the repository eliminates slop.

## The 12-packet tuning result

**This automated pilot does not establish an overall writing improvement or
elimination of noticeable slop.** Full instructions won 11 comparisons against
bare prompts, lost 11 and tied one; one assessment was invalid. Compact won 11,
lost 10 and tied one against bare prompts, with two invalid assessments.

All 72 paired judgments were captured; 68 passed the frozen parser. The four
failures remain in the [paired archive](artifacts/modern-tuning-paired.jsonl.xz)
and [summary](artifacts/modern-tuning-paired-summary.json). They were not silently
retried or removed from the planned denominator.

The table shows **wins / ties / losses / invalid**, from the perspective of the
first recipe in each contrast. Every cell represents the same 12 tuning packets.

| Writer; judge | Full vs. bare | Compact vs. bare | Full vs. compact |
|---|---|---|---|
| Claude Sonnet 5; GPT-6 Astra | 10 / 0 / 2 / 0 | 8 / 0 / 4 / 0 | 9 / 0 / 3 / 0 |
| GPT-6 Astra; Claude Sonnet 5 | 1 / 1 / 9 / 1 | 3 / 1 / 6 / 2 | 2 / 3 / 6 / 1 |

That striking difference cannot yet be assigned to the writers: each writer had
only one judging model, so writer and judge preferences are confounded.
[A preregistered rater crossover](rater-crossover-design.json) therefore reused all
24 full-versus-bare pairs and their 48 individual articles with the other judge.
It changed no writing, facts or A/B orientation and selected no favorable cases.
The added judgments are a measurement diagnostic, not extra independent stories
or a search for a judge that will endorse the repository.

The separate pointwise pass also captured all 72 responses. Its original parser
accepted 70. Two responses omitted `text-` from otherwise valid paragraph IDs;
an explicitly labeled reanalysis of **all 72 unchanged responses** restores that
prefix only when the exact paragraph exists. Unknown paragraphs and duplicate
IDs still fail. This required no new model calls and changed no level, reason or
factual judgment. Both original failures remain in the
[pointwise archive](artifacts/modern-tuning-pointwise.jsonl.xz) and
[summary](artifacts/modern-tuning-pointwise-summary.json).

These cells show **absent / minor / salient** after that mechanical ID recovery:

| Writer; judge | Bare | Full | Compact |
|---|---|---|---|
| Claude Sonnet 5; GPT-6 Astra | 1 / 11 / 0 | 6 / 6 / 0 | 4 / 8 / 0 |
| GPT-6 Astra; Claude Sonnet 5 | 6 / 6 / 0 | 1 / 10 / 1 | 6 / 6 / 0 |

No untreated article was rated salient. This cohort therefore cannot demonstrate
that a recipe eliminates conspicuous slop. The one salient full-instruction
rating is not a powered estimate of harm either. Paired slop ratings often differ
from these single-article judgments and must not be substituted for them.

One concrete issue worth testing is repeated source-limit language. The full
GPT municipal-bond draft repeatedly states what a number or record does *not*
establish, even where the claim is already narrowly framed. This suggests testing
whether scope can be expressed more naturally without repeating disclaimers.
It does not justify removing material uncertainty, safety warnings or useful
fiction labels. Factual flags remain model concerns, not a verified error count.
A flagged quotation omission is not automatically fabrication; it must be
assessed against the actual brief and protected meaning.

The sample is 12 tuning reporting packets, not 72 independent stories or human
reader reviews. No efficacy p-value, default promotion, NYT/WSJ-equivalent quality
or independently verified factual-cleanliness claim follows from these results.

### What changing the judge revealed

The crossover captured all 72 new judgments. Twenty of 24 paired assessments and
all 48 pointwise assessments passed their original parsers. The four additional
paired failures are retained in the [archive](artifacts/rater-crossover.jsonl.xz)
and [full report](artifacts/rater-crossover-summary.json).

These are the original and crossover **full-versus-bare** preferences together:

| Writer | Judge | Full wins | Bare wins | Ties | Invalid |
|---|---|---:|---:|---:|---:|
| Claude Sonnet 5 | GPT-6 Astra | 10 | 2 | 0 | 0 |
| Claude Sonnet 5 | Claude Sonnet 5 | 2 | 4 | 2 | 4 |
| GPT-6 Astra | Claude Sonnet 5 | 1 | 9 | 1 | 1 |
| GPT-6 Astra | GPT-6 Astra | 6 | 6 | 0 | 0 |

Only 19 of the 24 pairs had valid assessments from both judges. On those, the
judges agreed on the preference in **8/19**, or about 42%; eight pairs switched
directly between full and bare, with the remaining disagreements involving ties.
The five pairs missing a usable judgment remain listed, not imputed as wins or
discarded from the coverage account.

This limits any claim of stable editorial superiority. It does not prove that
every disagreement is a grader error: differences can be subtle or subjective,
and each new response also adds stochastic variation. Neither judge rated any
untreated article salient. More calls on the same stories would not turn these
results into independent evidence of slop elimination.

The original writers were told that their reporting notes were fictional, while
judging treated those notes as a fixed record. That can leave the permitted scope
of invention less clear than it should be. The next bounded revision pilot uses
an explicit fixed-record brief in **every** newsroom condition and distinguishes
mandatory inclusions from a mere list of source quotations. Its comparisons must
remain separate from the earlier ordinary-brief cohort.

### Source checking and the scoped revision

[The bounded fidelity audit](artifacts/fidelity-focus-audit-summary.json) covers
32 existing flag records on seven articles from two cases, not the whole cohort.
After checking the source text, the parent retained 27 record-fidelity concerns,
kept four as coverage questions rather than fabricated assertions, and rejected
one flag about a faithful partial quotation. Repeated flags can concern the same
passage; these are not 27 independent errors or an error rate. The supported
concerns include invented interviews, quotations and court-record claims, as well
as narrower wording, time and scope issues.

The [audit bundle](artifacts/fidelity-focus-audit.jsonl.xz) retains the raw agent
report and separate parent corrections. Two elided excerpts and one flattened
paragraph break were replaced with literal source context in the parent record.
Both stages are automated source checking, not human or outside verification.

The current task contract and accuracy guidance clarify three things: a fictional
reporting packet does not grant permission to invent reporting; drafting can
select source material without reproducing every quotation; and material scope
can often be expressed in the claim rather than in a repeated disclaimer.
Necessary uncertainty, warnings and disclosures remain protected. New examples
contrast an unnecessary disclaimer with a limitation that answers the reader's
actual question.

[The revision pilot](scope-revision-design.json) freezes the earlier full recipe
against this scoped revision and a bare control. It plans 24 drafts from four
already-seen newsroom families, plus 16 warning, quotation, voice and grammar
regression responses. Both judges assess the newsroom writing. The current full
recipe is therefore **not the same payload** as the earlier full-recipe archives;
the revision must not inherit their results or be presented as a default-promotion
or powered-efficacy result.

All 40 planned responses are now captured in
`artifacts/scope-revision-writing.jsonl.xz`. Both full-recipe conditions matched the
exact requested regression text in 6/8 replies. The four mismatches preserve the
tested meaning and medical warning, but include small medical copyedits or an
unrequested preamble before an otherwise unchanged news item. The
[text comparison](artifacts/scope-revision-regression-summary.json) and
[separate review](artifacts/scope-revision-regression-review.json) retain that
distinction. This revision did not fix no-op artifact delivery; its newsroom
results also do not establish a quality gain.

All 80 planned judgments were captured. The simpler preference schema accepted
32/32 responses; the pointwise schema accepted 45/48. The three rejected responses
had duplicate or unexpected JSON fields and remain in the
[assessment archive](artifacts/scope-revision-assessments.jsonl.xz) and
[summary](artifacts/scope-revision-assessment-summary.json).

| Scoped full compared with | Scoped wins | Ties | Other recipe wins |
|---|---:|---:|---:|
| Earlier full recipe | 6 | 3 | 7 |
| Bare prompt | 8 | 2 | 6 |

Each row contains 16 judgments on four already-seen story families, with two
writers and two judges. The judges agreed on only 2/8 writer-case comparisons of
the two full revisions and 4/8 scoped-versus-bare comparisons. Neither the small
bare-control advantage nor the slight loss against the earlier recipe is a
powered estimate. The clearer source-use obligations are retained without
claiming that this pilot proved better writing.

The pointwise labels were not uniformly favorable either: scoped full received
two salient ratings, while the earlier full recipe and bare control received one
each, among 16 planned ratings per condition. One scoped and two reference
assessments were invalid. These are repeated model ratings, not independent
article-level incidence or proof of a treatment effect.

[Direct checks of objective claims](artifacts/scope-revision-assessment-caveats.json)
also caught two roughly 750-word allegations about responses containing 607 and
649 whitespace-separated words **including their headlines**. A claimed holdout
subtraction was not established by a record describing sale inquiries rather
than completed purchases. Raw judgments remain unchanged. Genuine concerns,
including a county called a city and a hurricane date conflated with a program's
age, must not be dismissed because other flags were mistaken.

## Grading the prose, not its supposed author

[The judge prompt](judge-prompt.md) asks for editorial preference, separate slop
levels and factual flags. Salient slop means prominent generic framing,
information-free repetition, vague abstraction or a mechanical template that
weakens this particular story. An isolated minor edit is not the same claim.
Em dashes, triads, formality, necessary qualifications and useful length are not
automatic defects. Both outputs may be AI-generated; this is not an authorship
detector.

Models receive anonymous texts and the same source record. For current judging,
the original text is shown unchanged. A separate paragraph index supplies exact
source context for citations; it is not part of the article. Exact captured
requests, outputs, settings and receipts remain available. A grounded excerpt
does not prove that an interpretation is correct, and model opinions are not
human reviews.

The starter exposed a measurement limit: the same draft received different slop
levels and factual flags when paired with different alternatives. Those labels
must not be pooled as stable per-article incidence. The separate
[pointwise prompt](pointwise-prompt.md) assesses each article without a competing
version; identical article/brief/judge inputs share one assessment.

All eight pointwise model responses were retained. The first validator rejected
one solely because its valid evidence IDs were listed out of article order.
Removing that irrelevant ordering constraint and revalidating every unchanged
response produced eight valid assessments, with **no new model calls or changed
model decisions**. Unknown or duplicated IDs still fail. The original rejection
is retained alongside the reanalysis.

| Writer | Bare task | Task contract | Full | Compact |
|---|---|---|---|---|
| Claude Haiku 4.5 | Minor | Absent | Absent | Minor |
| GPT-5.4 mini | Absent | Minor | Minor | Absent |

These are pointwise model labels for one constrained source packet. Neither
untreated draft was rated salient in that assessment, so this case cannot show
elimination of conspicuous slop. All four Haiku drafts received factual flags;
none of the GPT drafts did. Those flags remain model opinions, not a completed
independent fact audit. For example, the compact Haiku draft promises website
and service-notification announcements absent from the packet: cleaner language
cannot excuse invented product commitments.

## What calibration did and did not establish

Four original synthetic controls check obvious repetition, useful added detail,
identical prose with purposeful punctuation, and an invented reopening date.
They are test controls, not professional reference articles. Each attempt uses
two judging models and both A/B orientations: 16 calls, not 16 independent cases.

| Attempt | Valid assessments | Met the original control expectations | Limitation |
|---|---:|---:|---|
| v2: physical-line references, smaller judges | 14/16 | 14/16 | Two references counted sentences as if they were supplied lines |
| v3: short evidence segments, smaller judges | 13/16 | 13/16 | Multiple-ID formatting failed; one rationale mistook evidence-window boundaries for broken article prose |
| v5: original text plus paragraph index, stronger judges | 14/16 | 13/16 | Two schema failures; one judge reasonably distinguished minor underspecification from perfectly clean prose |

All 48 raw assessments and failures are retained together in
`artifacts/grader-calibration-attempts.jsonl.xz`, separated by attempt. They must
not be pooled as an accuracy estimate. Two setup attempts sent no model inference
requests: one lacked a runtime directory; another requested a native agent alias
not available through the SDK. Model IDs must come from the runtime's actual
catalog.

The stronger available judges are GPT-6 Astra and Claude Sonnet 5. Calibration
has not established perfect schema compliance, factual judgment or human-level
editorial agreement. In particular, an identical pair must tie, but a reasonable
minor edit does not prove that purposeful punctuation is salient slop. Preserve
those distinctions instead of changing a result into a success claim.

No powered superiority, elimination of slop, compact-default promotion or human
editorial approval is claimed from this smoke work.

## Editing an existing AI draft

The cleanup smoke gives each writer its own exact captured bare draft and the
same reporting packet. It compares ordinary editing with full and compact
repository-guided editing, preserving the original word-range brief. This
controls for the benefit of another editing pass rather than attributing every
before/after change to the repository.

Six actual edits and six valid blinded pairwise judgments are retained in the
`starter-cleanup-*` artifacts. They share the same one reporting family:

| Writer | Full versus ordinary edit | Compact versus ordinary edit |
|---|---|---|
| Claude Haiku 4.5 | Ordinary edit preferred | Ordinary edit preferred |
| GPT-5.4 mini | Tie | Ordinary edit preferred |

This smoke does not show that the existing recipes remove slop better than
ordinary editing. The full Haiku response still publishes a long diagnostic
checklist and uses `12 p.m.` despite the supplied noon rule. All of those outputs
remain unedited in the archive; the earlier drafting wins are not a reason to
hide the cleanup losses.

The experimental `focused` draft/edit recipe therefore omits `## Detect`
checklists from all selected modules, retaining every other default section,
mechanics, boundary and safeguard. A source-matched full/focused tuning
comparison tests this specific hypothesis; fewer instructions are not presumed
better, and useful diagnostic cues may be lost. Full remains the default.

That comparison captured all 32 planned responses. On four fixed no-op/grammar
tasks, both full and focused matched the expected artifact in 6/8 replies. The
failed cases differed, and neither condition eliminated extra commentary.
Focused Haiku also narrated calls to an unavailable advisor in the longer
drafting and cleanup tasks, despite zero available or executed tools in the
capture evidence. The complete attempt is retained in `focused-tuning-writing`.
It does not establish that removing diagnostics solves the writing problem.

A separate runtime-identity probe investigates that workflow-like narration
without changing the prepared writing prompts. It uses the SDK's documented
identity-group customization while explicitly preserving safety, organization
instructions and runtime policies; tools and host operations remain disabled.
A runtime change must not be pooled with earlier profiles or presented as a
writing-library improvement.

That probe returned 12/12 responses. Unavailable-advisor mentions appeared in
3/12 matching earlier responses and 1/12 under the group customization. The
narration was reduced in this small rerun, not eliminated; different stochastic
outputs do not establish causation or complete runtime neutrality. The normal
runner profile has not been silently replaced, and both cohorts are retained.
