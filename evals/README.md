# Local editorial evaluation

This is an offline capture and **human-review** workflow, not an automatic writing
judge. There are no model calls, automatic LLM judgments or benchmark scores
shipped with it. `baseline.json` freezes original instruction hashes and token
counts, **not behavioral results**. See [rubric.md](rubric.md) for human criteria.

Run from the repository root with the existing virtual environment:

```sh
source .venv/bin/activate
python -m scripts.evaluate validate
```

PyYAML, tiktoken and its `o200k_base` tokenizer data must already be available.
All other dependencies are in the standard library. Nothing here installs
dependencies or sends requests to a model. Keep artifacts in ignored
`evals/runs/`; do not commit confidential drafts, credentials or real identifying
information. The unit tests use explicitly synthetic toy response/judgment
fixtures, not actual model results.

## Cases and structural validation

`evals/cases/**/*.json` contains the original synthetic suite: initially **40 cases,
16 tuning and 24 held_out**, with at least eight no_change cases and coverage of
every optional module (currently 26). Valid regression cases may be added.
Validation requires **at least** 40 cases, 16 tuning, 24 held_out and eight no_change,
not an upper limit. Every added case must also receive the required assessments.
Core modules load automatically. Freeze case contents, splits and the comparison
before tuning; never discard an inconvenient held-out result or relabel it as tuning.

Each case has exactly these fields:

| Field | Contract |
| --- | --- |
| `schema_version` | Integer `1` |
| `id` | Lowercase kebab-case, identical to the JSON filename stem; unique in the suite |
| `split` | `tuning` or `held_out` |
| `operation` | `draft`, `edit` or `review` |
| `task` | Nonempty task text |
| `input` | Draft/source text; only drafting permits empty input |
| `source_kind` | `synthetic` |
| `facts` | List of `{id, text}` atomic facts; unique IDs `f1`, `f2`, etc. |
| `modules` | Unique, actual optional `.md` module paths; never core, sources or raw-data |
| `safeguards` | Unique list containing `medical`, `legal`, both, or neither |
| `checks` | Exactly `required_facts`, `forbidden_additions`, `preserve`, `expected_action` |

`required_facts` references fact IDs; `forbidden_additions` and `preserve` are
lists of human-readable requirements. `expected_action` can match the operation,
or be `flag_missing_evidence`; `no_change` is permitted for edit/review only.
Unknown fields, wrong types, duplicate JSON keys/IDs, missing fact references,
bad paths and incompatible genre/citation/reader/interface selections are errors.
Safeguards must exist and cannot redundantly select the primary domain.

Validation checks structure and coverage, **not semantic quality or originality**.
It does not search outputs for keywords or decide whether a fact was preserved.
The author must ensure genuinely synthetic, atomic, sufficient facts; the reviewer
must check omissions as well as additions. `--cases DIR` on `validate` or `report`
supports a pilot directory, but never relaxes the initial-suite release gate.

## Prepare exact requests

```sh
python -m scripts.evaluate prepare evals/cases/CASE.json \
  --variant full --output evals/runs/CASE-full-request.json
python -m scripts.evaluate prepare evals/cases/CASE.json \
  --variant compact --output evals/runs/CASE-compact-request.json
```

Replace `CASE.json` with an actual case path, including any split subdirectory.

| Variant | Instructions |
| --- | --- |
| `task-only` | Operation-specific current task contract, without optional modules or safeguards |
| `legacy-modules` | Frozen original core, then selected original module bodies, without today's task contract or examples |
| `legacy-quick` | Exact original `quick-guide.md` at the frozen revision; optional modules are not appended |
| `full` | Current assembler's operation contract, full core and selected modules/safeguards |
| `compact` | Same assembler/selections, with compact core operating sections |

Legacy variants verify the loaded file/body hashes against `baseline.json` and
require its original Git object to be available. They **reject any standalone
safeguard selection**: there is no invented historical mixed-domain configuration.
This deliberately prevents a complete all-suite legacy comparison where cases
require those safeguards. Task-only/legacy-quick omitted selections are recorded.
No variant loads source dossiers, raw-data or demonstration examples.

A request records the complete case, split, operation, exact `instructions`,
serialized `input`, exact `prompt`, assembly manifest, case/prompt hashes and an
overall request hash. The model-facing prompt separates the task from a JSON data
packet containing only facts and draft; evaluation checks are not exposed as an
answer key. Input content is never executed. Manifest tokens count **instructions**
with `o200k_base`; the request's `prompt_tokens` counts the **entire prompt**,
including task and serialized input, with that same tokenizer. Neither count
includes provider chat framing or measures prose quality.
Object hashes use canonical UTF-8 JSON with sorted keys and no extra whitespace;
prompt and response hashes cover the exact UTF-8 text.

Supply the exact `prompt` string through your separately authorized model
interface. Do not substitute a conversation with extra instructions, history,
retrieval or tools. Use the same snapshot and settings for both variants. This
workflow neither invokes that interface nor proves what it actually received.

## Capture actual responses

Save the real UTF-8 response, then import it without trimming or normalization:

```sh
python -m scripts.evaluate record evals/runs/CASE-full-request.json \
  --response evals/runs/CASE-full-response.txt \
  --model EXACT-PROVIDER-MODEL-SNAPSHOT --family provider-model-family \
  --settings evals/runs/settings.json --output evals/runs/CASE-full-result.json
```

`settings.json` must be an object describing the actual generation settings:
temperature, seed where supported, token limits, reasoning controls, etc. Include
all relevant settings and use the same object for a pair. Do not put credentials,
authorization headers, passwords or access tokens in it. Obvious credential keys
are rejected recursively, but this is **not a general secret scanner**.
Nonfinite JSON numbers, duplicate keys and empty/whitespace-only responses fail.

Records preserve response bytes as decoded UTF-8 text (including CRLF and trailing
whitespace), response hash, request and operator-declared model snapshot/family/
settings. Status is always `captured-unreviewed`. Model metadata, response origin
and later human attestations are **operator-supplied, not independently verified**.
Hashes detect accidental changes; they are not signatures or proof of provenance.
Changing an existing case invalidates its old comparisons rather than silently
adopting their judgments. Adding cases preserves unchanged cases' hash-matched
evidence, but leaves the enlarged suite incomplete until new cases are assessed.
Existing request/result/report files are never overwritten.

## Blind and review

```sh
python -m scripts.evaluate blind evals/runs/CASE-full-result.json \
  evals/runs/CASE-compact-result.json --seed 731 --output evals/runs/pair-001
```

The output directory must not exist. It contains only two response-text files,
`a.txt` and `b.txt`, plus a **private** `key.json` mapping to hash-identified result
records. Seeded assignment is reproducible and independent of argument order; text
is not modified to remove clues within an answer. Use neutral pair directory names.
Give reviewers only the two texts, the case task/input/facts/checks, and the rubric.
**Do not share the directory wholesale, key, requests or model/variant metadata.**
The organizer retains the key and later attaches its `pair_id` to the assessment.

Pairing requires identical case/hash, operation, model snapshot, family and settings,
with different variants. **Full/compact pairs additionally require identical ordered
source module/section selections and hashes, contract hash, safeguard selections
and named-example selections.** Manifest selections must agree with the case and
automatic core. Optional-module and safeguard rendered hashes must also match;
only core rendering may differ. A current rule change cannot count as compression.
The importer checks the rendered module and contract hashes against the actual
captured instruction text, not merely against another manifest.

Private keys and reports label these pairs `matched-compression`. Comparisons
involving an original legacy variant are instead `legacy-instruction-comparison`;
their instruction sources and contracts intentionally differ. Task-only comparisons
without legacy are `instruction-ablation`. A result against legacy/task-only is not
evidence that compression preserved the corrected full rules. Labels stay out of
reviewers' text files. Changed records, mappings or exported text are report errors.

Write one JSON object per line to `evals/runs/judgments.jsonl`. Each judgment has
exactly the following fields; do not generate a filled judgment using a model:

| Field | Required human/organizer value |
| --- | --- |
| `schema_version` | Integer `1` |
| `pair_key` | Path to `key.json`, relative to the JSONL file (or absolute) |
| `pair_id` | Exact ID from that key |
| `reviewer_id` | Stable non-identifying `reviewer-` plus 8–32 random lowercase hex digits |
| `assessor` | Literal `"human"` |
| `human_attestation` | Boolean `true`, explicitly confirmed by the human |
| `winner` | `"a"`, `"b"` or `"tie"` chosen by that human |
| `rationale` | `{ "a": exact excerpt from a, "b": exact excerpt from b, "reason": nonempty explanation }` |
| `hard_failures` | `{ "a": [failure objects], "b": [failure objects] }`, explicit empty lists when none |
| `important_regressions` | `{ "a": boolean, "b": boolean }`, explicit flags for important domain/accessibility/voice regressions |

Each hard-failure object has exactly `category`, `passage`, `requirement`, `reason`.
Category is one of `unsupported_claim`, `changed_meaning`, `source_identity`,
`invented_verification`, `disclosure_or_privacy`, `unsafe_action`. Quote an actual
passage and identify the violated fact/requirement and consequence. For an
**omission**, quote the surrounding output, reference the missing fact ID, and
explain what was lost. Explain any important regression in the rationale.
Attestation means the reviewer checked all required facts, prohibited additions,
protected material and expected action—not just fluency. The tool verifies that
quoted excerpts occur, not that the explanation is correct.

Repeated `(pair_id, reviewer_id)` entries are errors, even across different copies
or orientations of a mapping. Different reviewers may assess the same pair;
disagreements remain visible rather than being quietly discarded.

## Report and conservative release gate

```sh
python -m scripts.evaluate report evals/runs/judgments.jsonl \
  --candidate compact --baseline full --seed 1729 \
  --output evals/runs/report.json
```

The report includes human-assessment wins/ties/losses, unique pairs, assessed and
missing cases, disagreements, per-model/settings cohorts, fidelity failures and
regression flags for both sides. Input hashes and assessed pair IDs support audit.
The held-out score uses win `1`, tie `0.5`, loss
`0`: average reviewers within each pair, pairs within a model/settings-case,
then model/settings cohorts within each case. Cases have equal weight. Repeated
outputs or reviewers never become independent samples.

A seeded 5,000-draw percentile bootstrap resamples held-out cases for a 95%
interval. Below eight distinct held-out cases the interval is `null`; fewer than
24 can never satisfy the gate, and all held-out cases in an enlarged suite must
also be assessed. This is uncertainty conditional on this suite,
these declared configurations and these judgments—not a universal editorial
quality score or a guarantee on other tasks.

**Every case, including added regressions, is treated as a mandatory hard case.**
The release status can be `superiority_supported` only when:

1. The entire current suite passes structural/coverage and minimum-adequacy checks.
2. Every observed model/settings cohort has human assessments for every case,
   including tuning and held-out; at least two declared model families are present.
3. No candidate fidelity failure or important regression is reported on any case.
4. The held-out case-clustered 95% lower bound is strictly greater than `0.5`.

A sparse second family cannot meet coverage. Conflicting family labels for the
same snapshot are rejected. Reports also reject mixed instruction revisions:
each variant must retain the same prompt for a given case, the same source
snapshot for each module and the same contract for each operation. A valid pair
does not justify pooling it with pairs from another revision. Fidelity failure
blocks even a stylistically preferred answer. The tool does not authenticate family labels, enforce model-side blinding
or prove held-out non-exposure; operators must enforce those protocol conditions.
It cannot establish confidence in a tiny pilot by counting more reviewers.

Absent files/assessments produce an honest `incomplete` report with missing cases
and `null` scores when no data exist—not invented zeros or a passing release.
Complete but uncertain comparisons are `inconclusive`; complete comparisons with
candidate fidelity failures/regressions are `blocked`. Keep compact optional unless
the gate is supported by real, protocol-compliant evidence.

Exit codes: `0` for successful validate/prepare/record/blind, or a supported report;
`1` for incomplete suite validation or an incomplete/blocked/inconclusive report;
`2` for malformed input, incompatible evidence, hash errors or refused overwrites.
Structural validation success makes no behavioral claim.

Run only the local workflow tests with:

```sh
python -m unittest discover -s tests -p 'test_evaluate.py'
```

The tests create and clean up their own project-local synthetic module/case
fixtures. They do not recount or depend on the live module corpus.
