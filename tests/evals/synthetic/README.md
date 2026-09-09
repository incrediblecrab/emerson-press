# Synthetic backtesting

This experiment uses original synthetic tasks, real model responses and explicitly
automated judgments. It is not a human editorial evaluation and cannot clear the
human-release gate in `tests.scripts.evaluate`.

The primary target is noticeable generic AI-style prose: whether repository-guided
writing has more of the specificity, structure, restraint and rhythm of strong
newsroom work. AP supplies mechanics; factual fidelity remains a guardrail, not
the sole outcome. The primary newsroom comparison requires a genuine `bare-task`
control versus a repository-guided candidate using the same natural brief and
substantial reporting packet.

The archived pilot instead compared full modules with the shared task contract
alone. **Both pilot conditions already used this repository.** That ablation does
not measure repository use versus no repository use. The broader technical, UI,
citation, medical and legal corpus is regression coverage, not by itself an
adequate primary sample of newsroom prose.

Tuning and held-out cases stay separate. Corrections may use tuning findings;
held-out outputs must not be inspected to choose those corrections. Renaming a
fixture does not create an independent observation. The newsroom recipe, grading
criteria, independent reporting-packet families and statistical plan must be
frozen before the primary held-out run.

Known regression-family overlap is resolved before model generation. ClinicFlow
and TaskHaven variants stay together in tuning rather than straddling splits;
the technical destructive-dialog variant stays with its original tuning family.
These corrections change the original per-shard split targets. Use the current
case files and family indices, not the originally requested counts, and do not
equate case totals with independent held-out families.

The completed broad regression corpus contains 260 cases: 44 tuning and 216
held-out labels, with 85 drafts, 116 edits, 59 reviews and 60 no-change cases.
All 26 optional modules are covered. Its indices declare 247 family IDs; that
count is not proof of independence or a substitute for the newsroom sample.
These are authored fixtures, not 260 measured writing outcomes.

## Live response capture

Live execution is optional and incurs Copilot usage. It requires Python 3.11 or
later, an authenticated GitHub CLI, and Copilot CLI:

```sh
.venv/bin/python -m pip install -r tests/requirements-simulation.txt
.venv/bin/python -m tests.scripts.generate tests/evals/runs/EXPERIMENT/jobs.json \
  --output tests/evals/runs/EXPERIMENT/captures --concurrency 4 --order-seed 731
```

A job plan has `schema_version: 1` and a nonempty `jobs` array. Each job has a unique
kebab-case `id`, a prepared-request `request` path relative to the plan, an explicit
`model`, and a model `family`. Requests use `tests.scripts.evaluate.prepare`; do not send
the case's evaluation checks as part of the writing prompt.

The runner creates a fresh SDK session per response. Tools, persistent memory,
custom instructions, skills, configuration discovery, file hooks and host Git
operations are disabled. Managed settings remain enabled. A fixed text-only role
replaces irrelevant coding, tool-routing and tone sections through the SDK's
targeted customization API; runtime safety and policy sections are retained.
The exact configuration and its hash are recorded. This is still a Copilot-hosted
experiment, not a bare-model API test. Its added date wrapper is captured separately
from the requested prompt.
Reasoning effort is set to low where the model supports it; temperature and
generation seed remain service defaults, not controlled parameters.

Each job retains its request, an unreviewed response record and an observed capture
receipt. Receipts include effective user text, model identity and available usage
measurements, excluding account quota snapshots. They do not authenticate an
immutable model-weight snapshot. Keep the entire run and adjacent runtime-state
directory under ignored `tests/evals/runs/`; raw runtime state can contain private
operational metadata and must not be published.

Existing artifacts are not overwritten. `--resume` reuses only records matching
the exact job/request/settings snapshot. Failed attempts remain failures and are
not silently regenerated; three execution failures stop new requests. Any missing
or failed job makes the generation summary incomplete. Neither successful capture
nor the number of outputs says whether the writing is good.

A returned capture is saved before response-record validation. If that later
validation rejects the response, its returned data remain beside `failure.json`;
the attempt is not regenerated. A transport failure may have no complete capture.
Observed tool counters must be explicitly present and zero, not missing or
boolean stand-ins. Known runtime/RPC failures are retained; custom transports
can declare specific additional exception classes through `capture_errors`,
not a blanket `Exception` catch.

## Current experiment boundary

The first pilot captured 64 responses using only the original 16 tuning cases with
GPT-5.4 mini and Claude Haiku 4.5, under both instruction conditions. It exposed
irrelevant agent-workflow narration even with zero available tools. Those records
are retained as a runtime-foundation pilot, not pooled with the neutral-role rerun
or a powered comparison. This harness correction is not an anti-slop rule learned
from held-out results.

Setup probes are not benchmark observations. A new prospectively separated corpus
and automated-assessment protocol are being prepared; no powered result or
editorial-superiority claim is established by the tuning work.

The original pilot archives here retain **152 writing responses**, all from repeated use of the same
16 original tuning cases: 64 under the runtime foundation, 64 under the neutral
role, 16 after an output-contract clarification and eight final-contract smoke
responses. No held-out writing has been generated. These are not 152 independent
cases; family independence has not been established for this old fixture set.

Each writing `.jsonl.xz` archive contains exact response records and sanitized
capture receipts. Judgment archives instead contain the blinded pair key, writer
result hashes, judge request/capture, raw assessment or failure, and any selected
line ranges. Adjacent manifests record compressed and uncompressed hashes.
Python's standard-library `lzma` reads the JSONL payload. Runtime state remains
private; no archive contains human ratings. The refocused newsroom work and its
separate article outputs are documented in [the newsroom study](../newsroom/README.md).

## What the tuning actually found

The first complete automated judging pass did **not establish an advantage for
the full pack**. Opposite-family judges marked the neutral pilot as follows:

| Writer | Full preferred | Task contract preferred | Tie |
|---|---:|---:|---:|
| Claude Haiku 4.5 | 5 | 6 | 5 |
| GPT-5.4 mini | 3 | 5 | 8 |
| Total | 8 | 11 | 13 |

These are 32 unadjudicated model opinions about 16 tuning cases, not 32 independent
trials or human preferences. The captured full prompts averaged 10,451.6
`o200k_base` tokens versus 750 for the shared contract alone: about 13.9 times the
prompt payload, without an established quality gain. This is not a billable-cost
ratio; it excludes runtime context, caching and provider pricing.

The judge itself needed debugging. The original quoted-excerpt format produced
21 valid judgments and 11 invalid attempts. All 32 pairs were reassessed, not just
the failures, using model-selected line ranges and programmatically extracted
exact excerpts. That produced 32 valid records. Traceability improved; judgment
correctness was not thereby established. Both entire attempts are retained.

Parent-AI inspection confirmed two failures to return the requested artifact:
a no-op news edit and a dialog edit that stopped despite an authoritative record
resolving the draft's error. Two citation-rule flags were not confirmed as hard
failures: absence of a formatting rule from a bibliographic fact packet does not
prove the rule wrong, and both sides made similar metadata assertions.
[The arbitration record](artifacts/pilot-arbitration.json) preserves these limits
without rewriting the raw model judgments.

The task contract now explicitly requires the edited document even for a no-op,
keeps completion checks out of the requested artifact, and distinguishes a
resolved draft/source difference from genuinely missing information. In three
repeated tuning tasks, literal expected-artifact matches rose from 6/12 to 10/12
across both instruction conditions. This is a small descriptive shape check, not
a causal or statistical quality estimate. Requested arithmetic-correction notes
were retained in all four corresponding responses.

The clarification is **not a reliability guarantee**. Final-contract news edits
returned the item in all four responses, but one still added a long assessment.
The four dialog responses also returned an edit, but extra process narration and
unsupported keyboard-detail inferences still occurred. No compact-mode promotion,
powered superiority claim or human-release decision follows from these pilots.

Thirty-minute checkpoints use ordinary Git commits and pushes. They do not dispatch
GitHub Actions; the authoring workflow is manual-only.
