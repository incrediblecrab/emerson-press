# Synthetic backtesting

This experiment uses original synthetic tasks, real model responses and explicitly
automated judgments. It is not a human editorial evaluation and cannot clear the
human-release gate in `scripts.evaluate`.

The primary comparison is full writing instructions versus the shared task
contract alone. Tuning and held-out cases stay separate. Corrections may use tuning
findings; held-out outputs must not be inspected to choose those corrections.
Renaming a fixture does not create an independent observation.

## Live response capture

Live execution is optional and incurs Copilot usage. It requires Python 3.11 or
later, an authenticated GitHub CLI, and Copilot CLI:

```sh
.venv/bin/python -m pip install -r requirements-simulation.txt
.venv/bin/python -m scripts.generate evals/runs/EXPERIMENT/jobs.json \
  --output evals/runs/EXPERIMENT/captures --concurrency 4 --order-seed 731
```

A job plan has `schema_version: 1` and a nonempty `jobs` array. Each job has a unique
kebab-case `id`, a prepared-request `request` path relative to the plan, an explicit
`model`, and a model `family`. Requests use `scripts.evaluate.prepare`; do not send
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
directory under ignored `evals/runs/`; raw runtime state can contain private
operational metadata and must not be published.

Existing artifacts are not overwritten. `--resume` reuses only records matching
the exact job/request/settings snapshot. Failed attempts remain failures and are
not silently regenerated; three execution failures stop new requests. Any missing
or failed job makes the generation summary incomplete. Neither successful capture
nor the number of outputs says whether the writing is good.

## Current experiment boundary

The first pilot captured 64 responses using only the original 16 tuning cases with
GPT-5.4 mini and Claude Haiku 4.5, under both instruction conditions. It exposed
irrelevant agent-workflow narration even with zero available tools. Those records
are retained as a runtime-foundation pilot, not pooled with the neutral-role rerun
or a powered comparison. This harness correction is not an anti-slop rule learned
from held-out results.

Setup probes are not benchmark observations. A new prospectively separated corpus
and automated-assessment protocol are being prepared; no powered result or
editorial-superiority claim is established by this setup.

Both completed pilots are retained in `artifacts/`: 64 responses under the runtime
foundation and 64 under the neutral role, each covering the **same 16 tuning cases**.
These are not 128 independent cases. Each `.jsonl.xz` archive contains exact
response records and sanitized capture receipts; its adjacent manifest records
compressed and uncompressed hashes. Python's standard-library `lzma` can read the
JSONL payload. Neither pilot has human ratings or a published preference score.

Ten-minute checkpoints use ordinary Git commits and pushes. They do not dispatch
GitHub Actions; the authoring workflow is manual-only.
