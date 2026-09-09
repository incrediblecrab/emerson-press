# Provisional synthetic, model-assessed backtesting

`python -m scripts.simulate` validates and reports **automated** paired assessments.
It does not call models, execute experiments, update instructions, or manage Git.
The parent/operator owns those actions and any checkpoints. This workflow never
produces human judgments or satisfies `scripts.evaluate`'s human release gate.
Model judgments can be wrong. Findings are conditional on the declared writers,
judges, synthetic distribution and scenario-family independence assumptions.

This document describes the version-1 simulation schema. The separately
registered source-aware acquisitions in the [newsroom study](newsroom/README.md)
use different judgment formats; do not relabel or coerce their captures into this
schema. The primary newsroom protocol has not yet been frozen.

## Fixed-sample planning

```sh
python -m scripts.simulate power
python -m scripts.simulate power --test sign_test
python -m scripts.simulate power --test sign_test --families 220
```

Two explicit, predeclared designs are available. Both use one-sided alpha `0.025`,
null preference `0.50`, target preference `0.60`, and target power `0.80`.

* **`bounded_mean` (default): 509 independent held-out scenario families.**
  Family scores lie in `[0,1]`, including ties and averages over models/judges.
  Hoeffding's inequality gives a conservative p-value
  `exp(-2*n*max(mean-0.5, 0)^2)` (one when the mean is at most one half).
  The sample calculation is
  `ceil((sqrt(log(1/.025)) + sqrt(log(1/.20)))^2 / (2*.10^2))`.
  At 509 families, the rejection threshold is approximately `0.56020`; under
  independent bounded scores with expected mean `0.60`, power is **at least**
  `0.80067`. This deliberately conservative design does not require no ties.
* **`sign_test`: 199 independent, decisive held-out scenario families.**
  Enumerating exact binomial upper tails gives critical wins `114`, actual null
  rejection probability at most `.025`, and power `0.803714` at probability `.60`.
  This estimand is the probability that a family's mean favors the candidate,
  **conditional on not tying**, not the magnitude-weighted mean preference.
  Tied family means are reported and reduce the effective sign-test sample; they
  are not replaced by extra cases. The power claim assumes the planned number
  of decisive families. Exact-test power is discrete: rounding 199 to another
  number does not automatically preserve power. `power --families N` checks it.

The earlier **220 held-out families plus 40 tuning cases** target described the
broad synthetic suite, not a separately established newsroom-quality sample.
Those cases are regression coverage for the clarified newsroom question and
must not automatically enter its primary sample. A newly declared newsroom
sample needs its own realistic briefs/reporting packets and independent-family
mapping. The design count now refers only to **primary** held-out families.
For a design actually containing 220 independent
binary/decisive units, cutoff **126** has power **0.8147148049349376** at `.60`
and null rejection probability at most `.025`. This is explicitly a
**binary-case benchmark approximation**, not promised power for the actual
multi-model, clustered, model-assessed preference magnitude. Ties reduce the
decisive sign-test sample; averaging and judge errors change the relationship
between a binary preference probability and a mean score. The bounded-mean
alternative still requires 509 independent families for its conservative power
guarantee. Forty tuning cases do not contribute to either held-out sample.
Separate authors and disjoint subject areas help diversify scenarios but do not,
by themselves, establish independence or make each author an independent draw.

These are planning calculations, not experimental scores and not promises of
significance. Freeze the design, sample, requests, models and judge instructions
before seeing outcomes. No optional stopping, replacement of difficult cases,
or post-hoc switch between tests. Tuning families never count toward the
confirmatory sample. A pilot is always insufficient for a confirmatory signal.

### Do not conflate the two effects

The tie-half-credit **mean preference** starts with judgment scores
`win=1, tie=0.5, loss=0`, then averages within pairs, writers, cases and scenario
families. Its denominator includes tied outcomes.

The **conditional sign preference** counts whether each final family mean is
above or below `0.5`, discarding exactly tied family directions from the sign-test
denominator. It is `winning_family_directions / non_tied_family_directions`.
It is not the mean preference, and the exact sign-test p-value does not test a
mean-preference effect. A study containing 220 raw families can have far fewer
than 220 non-tied sign observations.

When winning and losing family scores have different magnitudes, a conditional
sign signal can coexist with a tie-half-credit mean below one half. The
direction-based test has no extra mean-preference veto; such a result supports
only its declared conditional-direction effect, not an improvement in mean
preference. The bounded-mean test still requires a positive mean effect through
its own one-sided p-value.

Reports separately expose `raw_families`, `decisive_families`, `tied_families`,
`conditional_sign_preference` and `tie_half_credit_mean_preference` inside
`inference`, with an explicit `tested_effect`. `power_at_observed_effect` is
always null. The compatibility field `effective_design_adequate` is only the
stated hypothetical benchmark check—not measured or promised power. In
particular, observing ties does **not** entitle the report to repeat the
220-decisive-unit 80% planning claim. No non-tie rate or unconditional power is
estimated from an incomplete valid subset.

## Protocol schema (version 1)

Use `scripts.evaluate.prepare` first. Seal the following object with
`evaluate.seal(value, "protocol_sha256")`; omit that field when sealing.
All artifact paths below are relative to the **protocol file's directory**,
not the observations file. Absolute paths also work.

```text
{
  schema_version: 1,
  kind: "synthetic_protocol",
  id: lowercase-kebab-case,
  phase: "pilot" | "confirmatory",
  primary_outcome: "overall-preference" | "newsroom-editorial-preference",  # optional; legacy default overall-preference
  instruction_revision: full 40-character lowercase Git commit,
  design: {test: "bounded_mean" | "sign_test", independent_families: integer},
  contrasts: [
    {id, candidate, baseline, primary: boolean}
  ],
  cases: [
    {id, family_id, split: "tuning" | "held_out", case_sha256,
     sample_role: "primary" | "regression",
     requests: {variant: {path, sha256: prepared_request.request_sha256}}}
  ],
  writers: [{id, model: exact recorded identifier, family, settings: object}],
  judges:  [{id, model: exact recorded identifier, family, settings: object}],
  judge_assignment: "all" | "opposite-family",  # optional; default "all"
  evidence_format: "quoted-excerpts" | "line-ranges",  # optional; default "quoted-excerpts"
  response_envelope: "json-only" | "json-or-fence",  # optional; default "json-only"
  replicates: positive integer,
  seed: integer,
  judge_instructions: nonempty, frozen judging instructions,
  protocol_sha256
}
```

There must be exactly one explicitly declared primary contrast; it is **not**
locked to full versus task-only. Current supported variants are `bare-task`,
`task-only` and the assembler's pack variants (`full`, `compact`, `focused`).
Compact comparisons remain exploratory. Operation/selection restrictions from
the assembler still apply; for example, focused currently supports draft/edit.
Every case needs a pinned request for every variant named in the contrasts.
Model metadata/settings are operator-declared, not authenticated; recorded model
aliases are not immutable weight snapshots.
Credential-bearing settings fail.

`bare-task` contains the same natural brief/reporting packet with an empty
repository-instruction payload and no instruction modules. It still runs under
the declared neutral/managed runtime; it is not an instruction-free model.
`task-only` **does contain the repository task contract**. Thus the earlier
full/task-only pilot cannot answer repository guidance versus no repository
guidance, nor can its old preference judgments be relabeled as newsroom-editorial
judgments. Reports expose `comparison_scope` and `primary_outcome` explicitly.
They also expose the public `evaluate.comparison_kind` label: bare/current
contrasts are `repository-instruction-comparison`; full/compact classification
is unchanged. Validation uses the public evaluate request/result validators,
including rejection of resealed contaminated bare controls and nonempty manifests.

For the clarified primary question, declare:

```json
{
  "primary_outcome": "newsroom-editorial-preference",
  "contrasts": [
    {"id": "newsroom", "candidate": "full", "baseline": "bare-task", "primary": true}
  ]
}
```

This is a protocol fragment, not a captured result. `focused` may instead be an
explicit candidate when compatible with the predeclared tasks.

In newsroom mode **every protocol case must declare `sample_role`**. Only
primary-role cases enter editorial preference estimates, model breakdowns,
bootstrap intervals and the independent-family sample size. Regression-role
cases retain their own task-oriented assessment and remain in fidelity/regression
gates and required coverage. A family represented in both roles counts at most
once, with only its primary cases entering preference inference. Any family
connected to a primary case must have one consistent split, including its
regression relatives. For historical
overall-preference protocols, an omitted role retains the previous `primary`
default. Role labels are operator declarations, not proof of newsroom relevance.

`design.independent_families` is the fixed number of distinct **primary** held-out
`family_id`s, not the number of outputs. Every member of a primary-connected
family must use the same split. Related perturbations, repeated situations and paraphrases belong in
one family. Exact copies differing only in case ID/split are rejected even inside
one family; copies must not increase that family's weight. Software cannot prove
that renamed or paraphrased scenarios are truly
independent; the operator must audit this claim. More models, judges, replicates
or cases in one family do not increase the independent sample size.
For a **tuning-only pilot**, use `phase: "pilot"` and
`design.independent_families: 0`; do not relabel tuning cases as held out to make
the schema accept them. Power and held-out inference are then null. A confirmatory
protocol still requires a positive held-out sample with the predeclared adequacy.

Regression-only families may retain historical cross-split labels without
inventing new family IDs or changing stored case hashes. Such overlaps are
explicitly flagged in `coverage.regression_split_overlap_families` and warnings,
and never enter the primary sample count. Promoting any member of an overlapping
family into the primary sample is rejected. This is not permission to overlook
leakage in a primary sample.

The parent-reported risk-shard audit (65 cases, 52 families, including cross-split
families) reinforces that broad case counts are not independent held-out counts.
That suite remains regression coverage. The new bounded **12-case newsroom tuning
set** is likewise a pilot: use `phase: "pilot"`, primary-role tuning cases, and
`design.independent_families: 0`. It establishes no held-out inference or powered
claim, regardless of the number of writer/judge replies.

With `judge_assignment: "opposite-family"`, only declared judges from families
different from a writer's family have planned slots for that writer. At least one
eligible judge is required per writer. With two writer/judge families this supports
Haiku judging GPT outputs and GPT judging Haiku outputs, without inventing missing
same-family assessments. Assignment is part of the frozen protocol hash.

For prospective line-based acquisition, set `evidence_format: "line-ranges"`
before sealing. `judge_prompt(...)` then numbers the unchanged response lines;
`rationale.a`, `rationale.b` and every failure's `passage` must be model-selected
inclusive `[start_line, end_line]` integer ranges. The captured `assessment`
retains the **original parsed range assessment**, separately from the exact raw
`judge_response` and its hash. `resolve_assessment(...)` copies only the selected
original lines for validation/reporting; it never changes the winner, reasons,
failure categories or regression flags. Invalid ranges remain malformed.

If the acquisition accepts a single outer `json` Markdown fence, predeclare
`response_envelope: "json-or-fence"`. The default `json-only` remains strict.
Either policy preserves the unchanged raw response; neither repairs malformed
JSON or semantic evidence. Format and envelope policy are covered by the protocol
hash, so old quoted attempts cannot be pooled with a new line-based acquisition.

Validation checks prepared-request seals, case hashes, rendered payloads, and
instruction/module hashes against the pinned Git revision. Do not mix instruction
revisions. New findings and instruction changes require a separately labeled
protocol; retain the earlier observations, including failures.

### System and runner identity

Exact writer settings already participate in A/B pairing and are checked against
the protocol; exact judge settings are bound to every observation. In addition,
all declared writers and judges in one protocol must now share one runner
configuration. Only `model_selection` and `reasoning_effort` may differ between
models in that shared comparison, because model selection and supported reasoning
controls are explicitly model-specific. Both fields still remain in exact
per-model settings matching and hashes.

Every other settings field contributes to shared runner identity: transport,
SDK/runtime version, system role, wrapper declaration, permission/managed settings,
tool availability, and temperature/seed declarations. Unknown settings are
included, not silently ignored. Mixed configurations are rejected; use separate
protocols rather than pooling old and revised harness conditions.

For the parent runner's settings convention, record the complete system
configuration at `settings.session_options.system_message` and its canonical
JSON SHA-256 at `settings.system_message_config_sha256`. If either is present,
both are required and the hash is verified. This includes the exact `content`
text and section-removal/customization controls, not merely a role description.
If `model_selection` is present, it must match the declared model.

Reports expose `runner_identity.shared_settings` and its SHA-256, plus exact
writer/judge settings hashes by model ID. The protocol hash binds these settings
as well. Even re-labeling an old observation with a new protocol hash cannot
adopt its old-system writer records: their captured settings must still match.
These checks validate declared identity, not that every hosted instruction is
observable or that a neutral role has actually removed all persona effects.

## Transport qualifications and historical captures

The initial foundation pilot used `github-copilot-sdk==1.0.13` with installed
Copilot CLI `1.0.84-3`. Its fresh `mode="empty"` sessions used private
per-run storage, no tools, memory/config/skills/hooks/Git/session-store access
disabled, and infinite sessions off. **Managed settings remain enabled.**
Both `gpt-5.4-mini` and `claude-haiku-4.5` responded in setup probes. GPT supports
an explicitly supplied low reasoning setting; Haiku does not. Temperature and
seed remain **service defaults, not controlled generation parameters**.
These setup probes provide transport evidence only: no cost/quality conclusion
is established, and they must never enter the benchmark's independent-case count.

These historical profiles are not the current writing configuration. Later
newsroom captures used a customized text-only writing role and also included
GPT-6 Astra and Claude Sonnet 5. Consult the exact archived settings and
[newsroom account](newsroom/README.md), not the old empty-session description,
when interpreting a particular acquisition.

The parent subsequently preserved **64 real setup/tuning responses** from 16 old
tuning cases × two conditions × two writer families. In that initial empty-mode
transport, a Haiku full-condition news edit mentioned needing to call an advisor
despite observed zero available tools and zero tool calls. That is a
**harness/persona confound**, not evidence for an anti-slop instruction change.
Commentary instead of a medical no-op paragraph and insertion of the exercise
word “fictional” are likewise tuning observations awaiting a neutral-role retest,
not grounds here for changing library rules. No preference scores are inferred
from those examples.

Empty-session mode alone therefore does not establish a neutral editorial role.
Later pilots isolated a text-only system role while retaining permission and
managed-policy controls and preserving its exact text/configuration hash.
Keep the initial 64 captures under their original setup/tuning label; never pool
them with the revised-system transport or count responses as independent cases.
Later captures still contained occasional unsolicited commentary; a role
configuration is not proof that all persona effects have been removed.

An earlier, different CLI probe reported a successful tool-disabled `gpt-5.4-mini` call through
Copilot CLI **1.0.84-3**, with a prepended `current_datetime` wrapper and roughly
**11,900 hosted input tokens even for a 50-word submitted prompt**. Those are
parent-observed transport characteristics, not measurements performed by this
tool; do not assume that measured overhead applies to the new empty-session SDK
transport. A tool-disabled CLI invocation is **not** pure API/model isolation, an
instruction-free baseline, or evidence of controlled temperature.

Here, `request.prompt` and `judge_prompt` mean the exact **authored/submitted
payloads**. Their hashes do not cover unobserved hosted system instructions,
dynamic wrappers, repository context or provider policies. A `task-only` payload
can still reach a model with substantial hosted instructions. Unknown context can
confound the contrast; more scenarios do not remove that confounding.

Record only generation controls actually supplied and honored. Do not populate
`temperature: 0` merely because deterministic behavior is desired. The existing
`writers[].settings` and `judges[].settings` objects can include a fixed,
operator-declared transport description, for example:

```json
{
  "transport": {
    "kind": "copilot-cli",
    "version": "1.0.84-3",
    "tools_disabled": true,
    "current_datetime_wrapper": true,
    "hosted_context_observability": "partial",
    "temperature_control": "not_verified"
  }
}
```

These settings are matched across paired variants, not independently verified.
Keep per-invocation transport traces, effective messages when observable, actual
usage and timestamps in separate credential-free audit artifacts; do not put
variable usage or timestamps in the fixed settings object. Preserve the exact
submitted payload as this API's `judge_prompt`, not a reconstructed hosted prompt.
Switching to an SDK or changing system-message controls requires a newly pinned
transport/protocol. Until those controls are verified, findings remain explicitly
conditional on the hosted CLI environment and its uncontrolled context/settings.
For the SDK transport, record the verified configuration above rather than copying
the historical CLI example. Log the parent-observed SDK events with `event.to_dict()`;
bare `dataclasses.asdict()` is not a safe JSON serialization path for UUID/timedelta
values. Per-call user-message and usage evidence belongs in those audit artifacts,
not in fixed pair-matching settings. Disabling local features does not establish
that all managed/provider context has been removed.

## Execution interface (parent/operator owned)

Public functions in `scripts.simulate`:

```python
power_plan(test="bounded_mean", families=None) -> dict
validate_protocol(root, protocol, *, base_dir=Path(".")) -> dict
pair_seed(protocol, case_id, contrast_id, writer_id, replicate) -> int
judge_prompt(protocol, case, responses={"a": text, "b": text}) -> str
capture_judgment(
    root, protocol, *, base_dir, case_id, contrast_id, writer_id,
    replicate, judge_id, pair_key, judge_prompt, judge_response,
    status="assessed", error=None,
) -> dict
report(root, protocol_path, observations_path) -> dict
pilot_report(root, directory, *, expected_pairs, candidate="full",
             baseline="task-only", seed_base=731) -> dict
```

For each planned case × contrast × writer × replicate:

1. Run both pinned requests using that writer's declared settings. Capture actual
   outputs with `evaluate.record`; do not trim text or invent missing outputs.
2. Create a standard `evaluate.blind` A/B key, using `simulate.pair_seed(...)`.
   All assigned judges for this slot assess this same pair. Do not expose the key, variant,
   writer identity, or model metadata to judges.
3. Obtain the exact judge prompt using `simulate.judge_prompt(...)`. It includes
   the case's task/evidence/checks and unchanged A/B text, not variant labels.
   Invoke the declared judge externally, then call `capture_judgment` with the
   exact prompt/response. Append its sealed object as one JSONL line.

The raw judge response must be JSON with exactly:

```text
{
  winner: "a" | "b" | "tie",
  rationale: {a: exact A excerpt, b: exact B excerpt, reason: explanation},
  hard_failures: {
    a: [{category, passage: exact excerpt, requirement, reason}],
    b: [{category, passage: exact excerpt, requirement, reason}]
  },
  important_regressions: {a: boolean, b: boolean}
}
```

For a **primary newsroom case**, the response additionally requires `editorial`
with exactly six dimensions:

```text
editorial: {
  lead:         {a: rating, b: rating},
  substance:    {a: rating, b: rating},
  structure:    {a: rating, b: rating},
  specificity:  {a: rating, b: rating},
  rhythm_voice: {a: rating, b: rating},
  ap_mechanics: {a: rating, b: rating}
}
rating: {
  level: "generic" | "mixed" | "professional" | "not_applicable",
  passage: exact excerpt | [start_line, end_line] | null,
  reason: nonempty explanation
}
```

Evidence follows `evidence_format`; null is permitted only for `not_applicable`,
which still requires an explanation. Raw ranges remain in the captured assessment
and are resolved only for validation/reporting. Missing dimensions are malformed
judgments, not silently inferred ratings. Regression cases use the original
four-field judgment schema without this newsroom-specific object.

In newsroom mode the primary-case `winner` measures editorial prose preference:
specific rather than interchangeable leads, substance rather than empty/general
claims, purposeful rather than repetitive structure, supported specificity,
intentional rhythm/voice, and relevant AP mechanics. These are broad professional
newsroom qualities—not imitation of an outlet's wording, publication certification,
AI-authorship inference, word bans, or sentence/lexical quotas.
Factual fidelity and consequential regressions are **separate gates**, not the
primary preference question. A polished fabrication can receive a stylistic
preference but must not clear the factual gate. No numeric composite is invented
from the six qualitative levels. Reports preserve them as unadjudicated
`editorial_assessments`.

Failure categories are the six categories in `evals/rubric.md`. Empty lists mean
the judge reported no fidelity failure, not that fidelity was independently
verified. For an omission, quote surrounding output and identify the missing
fact/requirement. Preference and fidelity are separate outcomes.
Important-regression flags must be actual booleans and explained in the rationale.
The earlier three-field `fidelity_failures` response format remains readable
without changing its raw text, but is reported as lacking regression assessments;
it cannot support a new synthetic-signal conclusion without those assessments.

`capture_judgment` returns a record with exactly:

```text
schema_version, kind: "automated_judgment", assessor: "model",
protocol_sha256, case_id, contrast_id, writer_id, replicate, judge_id,
judge: {model, family, settings},
pair_key, pair_id, status,
judge_prompt, judge_prompt_sha256, judge_response, judge_response_sha256,
assessment, error, observation_sha256
```

Statuses: `assessed`, `writer_failed`, `judge_failed`, `malformed_judge`.
`assessment` is parsed JSON only for `assessed`, otherwise `null`. Invalid or
empty judge JSON becomes `malformed_judge` with its exact raw response retained.
For writer failure, `pair_key`, `pair_id`, judge prompt/response and their hashes
are `null`; supply the error. For judge failure, retain the real pair and exact
prompt, any returned text (or `null`), and the error. Do not manufacture a pair or
response. Every failed writer slot must be recorded for each planned judge.

One record is allowed per planned slot. Duplicate slots or pair/judge observations
are rejected, including copied keys and renamed judge IDs. Failed/malformed slots
remain failed, not silently replaced by convenient retries. A later rerun must be
separately labeled and retain the earlier data.

JSONL records are separated by literal LF characters. Valid Unicode separators
inside captured JSON strings, including U+0085, U+2028 and U+2029, remain part of
the record rather than becoming artificial malformed lines.

## Preserved execution-only tuning pilots

The parent's session-owned `judge_pilot.py` uses its own stored prompt and
`731 + pair_number` blinding schedule. Do **not** rewrite those captured prompts,
responses or keys to pretend that they were produced by a later powered protocol.
Use the retrospective adapter:

```sh
python -m scripts.simulate pilot-report \
  evals/runs/initial-tuning/neutral-judges --expected-pairs 32 \
  --output evals/runs/initial-tuning/neutral-pilot-report.json
```

The adapter reads only the named directory's `pair-NNN` jobs and their referenced
writer records. Each pair has `key.json`, `judge-request.json`, a preserved
`judge-capture.json` when a response was returned, and either `assessment.json`
or `failure.json`. A finished `capture-summary.json` is checked when present.
The caller supplies the expected pair count; absent jobs and failed/malformed
captures cannot shrink the denominator. Extra pair directories are reported.

It checks:

* Tuning split only, case/request/prompt/response hashes, pair identity and recorded
  order, and exact case/data packets in each stored judge prompt.
* Consistent captured instruction snapshots, runner/system configuration,
  per-model settings, observed judge model and tool-count evidence.
* Opposite-family judges, using the family declarations in the preserved writer
  records. It does not invent family labels for otherwise unknown judge models.
* Stored assessments against the preserved raw model response, including every
  hard-failure object and important-regression flag.

The quoted-excerpt pilot's single outer `json` Markdown fence is recognized
without changing the captured response or its hash; the envelope policy is
reported. Separately recorded model-selected-line pilots are also supported:
inclusive line ranges are checked, expanded deterministically from the original
A/B text, and compared with the saved derived assessment. This is evidence-location
decoding, not a new rating or a search for a better quote. Invalid ranges or
nonmatching quoted excerpts remain malformed. Different judge instructions or
evidence formats cannot be pooled in one report.
Reacquiring the **entire** line-evidence pilot is a new acquisition, not a repair
of the earlier quoted-passage attempts. Keep both directories and all attempts.
Do not assemble a seemingly complete run from successful original quotes plus
selected replacements for only failed quotes. The adapter never applies parent
arbitration notes by editing model ratings; retain such notes separately with
their provenance. Arbitration does not make the observations human verified.

The adapter is read-only apart from the explicitly requested new report file.
It preserves references and hashes to the raw captures, exposes unadjudicated
model assessments, and reports all failures/exclusions. Descriptive win/tie/loss,
case-weighted preference, fidelity flags and important regressions are separate.
If any planned assessment failed, is absent, or was excluded,
`case_weighted_preference` is null. `valid_subset_case_weighted_preference` and
the raw counts are explicitly subset-only descriptions, not defensible estimates
for the full acquisition. Nonliteral-quote and malformed-JSON failures can select
which outputs remain; missingness must not be assumed random.
Its status is **always `incomplete`**, with no retroactively invented protocol or
instruction revision, no independent-family claim, and null power, p-value and
bootstrap interval. `human_verified` and `promotion_eligible` remain false.
CLI exit `1` is therefore expected even when every pilot artifact validates.

The first neutral-role tuning pilot and the focused regeneration after the task
contract clarification belong to separate snapshots. A report/checklist response
to an artifact request is a tuning observation for parent arbitration, not an
automatic instruction edit by this tooling. No held-out output needs to be read
to inspect these pilots, and neither pilot contributes to the powered sample.

## Validation and reporting

```sh
python -m scripts.simulate validate PROTOCOL.json
python -m scripts.simulate validate PROTOCOL.json --observations OBSERVATIONS.jsonl
python -m scripts.simulate report PROTOCOL.json OBSERVATIONS.jsonl --output REPORT.json
```

Reports include all planned/missing slots, malformed lines, exclusions, explicit
request/judge failures, raw win/tie/loss counts, per-case and per-family preferences,
model/judge breakdowns, fidelity flags, and frozen input hashes. Aggregation first
averages judges within a pair, replicates within a writer-case, writers within a
case, then cases within a family. Each independent family has equal inferential
weight. A separate descriptive case-weighted preference is also reported.
The preference numerator and denominator cover primary-role cases only;
`regression_coverage` is reported separately. Fidelity and important-regression
flags from **either** sample role can block a signal. Complete primary evidence
may be described while regression checks remain unfinished, but the overall
status stays incomplete until every planned gate has coverage.
For incomplete prospective data, full-sample mean fields, p-values and bootstrap
intervals are null; any remaining subset descriptions are explicitly labeled.
Model breakdowns describe only valid observations for that model.

A seeded 5,000-draw family-cluster bootstrap gives a descriptive 95% interval
(null below eight families). The predeclared test supplies the p-value; bootstrap
Monte Carlo noise is not a second significance gate. Exact sign-test ties and
its different estimand are explicitly reported. Compact p-values are exploratory,
not multiplicity-adjusted confirmatory claims.

Statuses are **`synthetic_signal`**, **`inconclusive`**, or **`incomplete`**.
A signal requires the primary contrast, complete valid planned data, adequate
fixed-sample design, and its predeclared test threshold. Candidate fidelity or important-regression flags
keep the overall conclusion inconclusive even when stylistic preference favors
it. All fidelity findings remain visible separately. Pilots, failed requests,
malformed judges, missing observations, or underpowered plans are incomplete.
No status authorizes promotion: `promotion_eligible` and `human_verified` are
always false. A model-assessed signal is provisional, not editorial superiority.

Exit `0` means structurally valid input for `validate`, or a provisional signal
for `report`; `1` means an incomplete/inconclusive report or invalid observations;
`2` means invalid protocol/arguments or a refused output overwrite. Absent
observations produce an incomplete report with null scores, never invented data.

Keep real run artifacts in ignored `evals/runs/`, without credentials, identifying
information or confidential text. Tests use explicitly synthetic, project-local
fixtures and never represent experiments:

```sh
python -m unittest tests.test_simulate
```

## Final version-1 runner handoff

The protocol schema and public signatures above are the execution contract.
For prospective opposite-family judging, set `judge_assignment: "opposite-family"`
before sealing the protocol. To use the selected line-evidence acquisition, also
set `evidence_format: "line-ranges"` and, if accepting the pilot's single-fence
envelope, `response_envelope: "json-or-fence"`.
Pin each request's **`request_sha256`**, not a
filesystem-byte hash, under its case/variant reference. All artifact references
resolve from the protocol file's directory.

1. Validate the frozen protocol with `validate_protocol(...)`.
2. Preserve actual writer responses with `evaluate.record(...)`; make one A/B
   key per case/contrast/writer/replicate using `pair_seed(...)`.
3. Generate the submitted payload with `judge_prompt(...)`. The base response
   contract is exactly `winner`, `rationale`, `hard_failures`,
   `important_regressions`; excerpts or ranges follow the predeclared evidence
   format. Primary newsroom cases additionally require the six-dimension
   `editorial` object. No human attestation field exists.
4. Verify observed SDK model/settings against the declared judge, retain the raw
   SDK evidence separately, and call `capture_judgment(...)` with the unchanged
   submitted prompt and raw response. Append the returned sealed observation to
   JSONL. Do not turn malformed responses into repaired ratings.
5. Call `report(root, protocol_path, observations_path)`. Use `pilot_report(...)`
   only for the preserved execution-only tuning layout—not to retroactively
   manufacture a powered protocol.

A model-assessed signal, when supported for its explicitly stated effect, is
still provisional. This API never grants an automated promotion or human
verification.

### Grounding and arbitration are different

A complete line-grounded acquisition establishes that the model-selected evidence
can be traced to the responses. It does **not** establish that the judge correctly
interpreted those passages or applied a style manual. In particular, absence of
a formatting rule from a bibliographic fact packet does not by itself make
applying that rule an unsupported factual claim or a source-identity regression.
Similar metadata requirements asserted on both sides also need comparative,
task-specific assessment rather than asymmetric assumptions.

Reports mark fidelity and regression flags as `unadjudicated-model-assertions`.
The importer preserves the model's original flags; parent arbitration notes and
their provenance remain separate. The parent-confirmed artifact omissions and
unconfirmed manual-rule flags must not be silently converted into new model
ratings or human verification.

The completed line-based pilot still consists of old tuning fixtures without an
established independent-family mapping. Thirty-two valid judgments are not
thirty-two independent cases. Likewise, before/after artifact-return diagnostics
on three repeated tuning cases are not a twelve-case validation sample or evidence
of general editorial superiority. Residual commentary and other limitations
remain open tuning findings, not proof that a powered quality gate has passed.
