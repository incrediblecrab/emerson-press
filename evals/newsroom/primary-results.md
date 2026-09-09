# Primary newsroom result

**The registered backtest did not establish a mean writing-preference gain or
removal of noticeable generic prose.** Full had a small observed preference
lead, but the preregistered interval included the neutral score. The judges
disagreed substantially, and salient-slop ratings did not show a reduction.
This is model-only evidence from synthetic reporting packets, not a human
editorial verdict or proof that the instructions never help.

## What was actually acquired

The [protocol](primary-protocol.json) was published before writing. It fixed
219 cases in 212 audited family clusters, one writer per family, full versus
genuine `bare-task`, and both GPT-6 Astra and Claude Sonnet 5 as judges.
Each writer received 106 families: 110 cases for GPT and 109 for Claude.
Families, not files, repeated drafts or judgments, are the inferential units.

| Acquisition | Planned | Valid records or assessments | Missing assessments |
| --- | ---: | ---: | ---: |
| Writing | 438 | 438 | 0 |
| Paired preference | 438 | 433 | 5 |
| Pointwise style/fidelity | 876 | 769 | 107 |

Every planned job was attempted once. All 438 drafts and 1,311 returned judgment
captures were retained; three provider-filter failures have failure records
rather than complete captured responses. Of the returned judgments, 109 failed
the frozen parser. They were not repaired or regenerated.

The initial three-filter circuit-breaker stop left 561 jobs untouched.
A [published operational deviation](artifacts/primary-continuation-01.json)
authorized first attempts for those original jobs, not retries or replacement
judges. The original plan, failed attempts, initial summary and continuation
chain remain in the [acquisition-control archive](artifacts/primary-acquisition-controls-manifest.json).
No recipe, source packet, judge prompt, parser, model assignment, weight or
auxiliary randomization table changed.

## Primary preference result

| Judge | Full preferred | Bare preferred | Tie | Missing |
| --- | ---: | ---: | ---: | ---: |
| GPT-6 Astra | 127 | 81 | 11 | 0 |
| Claude Sonnet 5 | 40 | 71 | 103 | 5 |
| **Total judgments** | **167** | **152** | **114** | **5** |

These are judgment counts, not 438 independent observations. Scoring full = 1,
tie = 0.5 and bare = 0, then applying the frozen equal family/case/judge weights,
the observed family mean lies between **0.5124 and 0.5242** under every possible
completion of the five missing preferences. Those are missing-data bounds,
**not a confidence interval**. There are 207 completely scored families and
five incomplete ones; none was dropped or given a replacement rating.

The preregistered **randomized 95% mean interval is [0.4076, 0.5553]**. It includes
0.5, so the primary signal criterion was not met. The frozen auxiliary table
yielded 101 to 103 possible successes; those are deliberately added
randomization outcomes, not evaluator votes. The [method](mean-inference.md)
retains the original fractional scores and requires both a positive interval
and a positive raw-mean lower bound.

The original 0.8119 joint-power lower bound was conditional on independent,
complete family scores with expected mean 0.60. It was a planning calculation,
not a promise of significance, a guarantee under missingness, or proof that
these synthetic clusters are independent.

### Writer and judge dependence

| Assigned writer subset | GPT judge: family mean | Claude judge: family mean | Both judges |
| --- | ---: | ---: | ---: |
| GPT-6 Astra, 106 families | 0.5755 | 0.3184-0.3656 | 0.4469-0.4705 |
| Claude Sonnet 5, 106 families | 0.6368 | 0.5189 | 0.5778 |

These are descriptive means or missing-score bounds, not subgroup confidence
intervals. The writers had different assigned families, so the table is not a
same-case model ranking. The GPT judge's overall mean was 0.6061; the Claude
judge's was 0.4186-0.4422. Selecting only the favorable judge would contradict
the registered equal-weight comparison.

Both judges supplied valid preferences for 214 pairs. They agreed exactly on
**73/214 (34.1%)**, directly reversed one another on 42, and differed between a
tie and a preference on 99. Exact paragraph evidence made the opinions
traceable; it did not make them agree.

## Noticeable generic prose

| Condition | Absent | Minor | Salient | Missing | Planned ratings |
| --- | ---: | ---: | ---: | ---: | ---: |
| Full | 166 | 201 | 11 | 60 | 438 |
| Bare-task | 159 | 226 | 6 | 47 | 438 |

No valid rating used `unassessable`. GPT called no bare article salient and two
full articles salient. Claude called six bare and nine full articles salient.
Among articles with both pointwise ratings, **none was called salient by both
judges**. Full therefore did not demonstrate elimination of a consistently
detected baseline problem.

The fixed-family salient-prevalence bounds are **2.59%-16.51% for full** and
**1.42%-12.03% for bare**. Missingness allows a bare-minus-full change from
**-15.09 to +9.43 percentage points**. These are descriptive completion bounds,
not confidence intervals or a separately powered slop-reduction test. The raw
11 versus six salient ratings must not be presented as a proven increase either.

Pointwise measurement was a substantial limitation: Claude had 106 missing
ratings out of 438 planned, versus one for GPT. Claude's 104 format failures
included 83 extra-field responses, nine duplicate-key responses, eight other
JSON-syntax failures and four missing-evidence responses; two further ratings
were filtered. The remaining preference failures were four malformed Claude
responses and one filtered response. The frozen rejection rules were preserved
even when an extra field looked removable.

### Two inspectable examples

These examples were selected after analysis to illustrate limitations, not as
additional independent evidence.

The [full glass-furnace response](examples/primary/newsroom-held-business-news-glass-furnace/full.txt)
opens with an unrequested drafting note, including "Let me check in with the
advisor before finalizing," and ends with a word-count/compliance checklist.
The [bare response](examples/primary/newsroom-held-business-news-glass-furnace/bare-task.txt)
starts with its headline. The complete full output, including that scaffolding,
was captured and graded; no tools were observed being exposed or called. GPT
called it salient while Claude called it absent. This is a concrete
artifact-delivery problem and a grading disagreement, not a claim that either
whole article is factually verified.

The laundromat feature shows a different problem:
[bare](examples/primary/newsroom-held-civic-laundromat-noticeboard/bare-task.txt)
and [full](examples/primary/newsroom-held-civic-laundromat-noticeboard/full.txt)
both accumulate cautions about what a noticeboard does not establish or provide.
The full version explicitly says "the reporting record provides no broader
attendance result." Claude called both versions salient; GPT rated bare absent
and full minor. The possible defect is the density and repetition of caveats,
not the mere presence of a negation or a necessary qualification.

## Fidelity, length and practical implications

Valid pointwise ratings contained 108 fidelity flags for full and 113 for bare.
They are **model allegations, not confirmed factual errors**. GPT supplied
93 full and 100 bare flags; Claude supplied 15 and 13, respectively. No human fidelity or
editorial review was performed, and `no_flag` is not verified truth.

Complete-response word counts had medians of 543 for full and 568 for bare,
with ranges of 415-718 and 461-738. These include headlines, markup tokens and
commentary. Shorter output is not, by itself, better reporting or better prose.

The repository should be presented as task-specific editorial guidance, not
an automatic slop-removal system. Full remains the assembler's existing
default, **not an empirically established best recipe**. Compact was not the
primary contrast and is not promoted by this result. No new phrase bans,
extra writing pilots or post hoc recipe changes were used to seek a win.

Before claiming broad improvement, measurement needs stronger agreement and
human editorial review, alongside source-fidelity checks. These now-exposed
primary cases retain their original registered split; they must not be reused
as a fresh unseen holdout after further tuning.

## Audit trail

[Machine-readable results](artifacts/primary-results.json),
[independent verification](artifacts/primary-verification.json),
[preference slots](artifacts/primary-preference-manifest.json),
[pointwise slots](artifacts/primary-pointwise-manifest.json) and
[every unchanged draft](examples/primary/README.md) are retained.
The independent check reparsed all 1,202 valid assessments, recomputed the
family means, missingness bounds and agreement counts, directly inverted the
binomial tails for the registered interval, and checked all 438 word counts.
It verifies arithmetic and traceability, not the correctness of model opinions.
