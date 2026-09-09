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

The new primary corpus is being authored as 12 tuning stories and a target of
220 held-out reporting-packet families. These are substantial news updates,
explainers and reported features, not UI labels or citation exercises. A rich
packet should support the requested length without padding; nonessential facts
need not all appear in the story. Each case needs an explicit reporting snapshot
date so a runtime's current date does not silently change the task.

Case count is not independent sample size. Reused events and templates must stay
in the same family and split. Freeze the actual family map, candidate recipe,
model settings, primary contrast, grading protocol and statistical plan before
any primary held-out generation. No such held-out writing result is available yet.

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
