# Source-aware model acquisition

`tests.scripts.newsroom_judge` acquires model opinions, not human reviews or release
approval. It uses the source-aware preference and pointwise templates; the older
six-dimension `tests.scripts.simulate` acquisition is a different protocol.

## Prepared requests

`preference_request(root, first_record, second_record, judge_model)` assigns the
first record to A and the second to B. It requires a compatible full/bare-task
draft pair with the same case, writer and settings. The full record determines
the candidate side; caller-supplied labels cannot reverse that binding.
`pointwise_request(root, record, judge_model)` prepares one article's assessment.

The judge sees only the ordinary task, supplied facts, complete unchanged article
text, indexed evidence paragraphs and measured word counts. Record identities,
writer/model labels, variants, family assignments and hidden checks remain in
metadata outside the prompt. Self-identifying words already in an article are
not silently removed.

`validate_request(root, request, records_by_result_sha256)` rebuilds the request
from validated writer records and the current template. It checks the source,
orientation, response hashes, paragraph text and whole-response word counts,
including resealed metadata changes. Freeze these inputs and implementation
hashes before acquiring primary outcomes.

Paragraphs preserve every character; whitespace-only edges attach to neighboring
content rather than becoming selectable empty evidence. Word counts use
`len(response.split())`, including headlines, markup tokens, commentary and
Unicode whitespace. A soft length target alone is not a factual falsehood.

## Strict response parsing

`parse_assessment(request, raw_response)` returns the unchanged parsed assessment
and programmatically extracted evidence. Preference has exactly `winner`,
`reason`, `evidence_a` and `evidence_b`; each side needs at least one supplied
integer paragraph ID. Pointwise has exactly `level`, `reason`, `evidence`,
`fidelity` and `fidelity_reason`. Evidence is required for minor/salient style
ratings or a fidelity flag.

Duplicate JSON keys, extra fields, unknown or repeated IDs, booleans and string
IDs are rejected. One exact outer lowercase `json` fence with LF line endings is
accepted. There is no prefix recovery, opinion rewriting, selective repair or
automatic request for a replacement judgment. Raw rejected responses remain
available.

## Capture and continuation

Pass an externally started `generate.LiveTransport` to:

```python
await newsroom_judge.run_jobs(
    root, jobs, records_by_result_sha256, output, transport,
    concurrency=4, order_seed=731,
)
```

Each job contains exactly `id` and its prepared `request`. The complete plan is
validated before capture and binds model settings, request hashes, code hashes
and launch order. Returned captures are saved before validation. Observed model
identity, explicit zero tool counters, timestamps and response hashes are checked;
missing counters are not assumed to be zero.

Three transport or receipt-validation failures stop new starts. Malformed
assessment JSON does not trigger that transport circuit breaker. Every failure
or unstarted job remains visible and retains its planned statistical weight.
An interrupted transport may provide no complete response.

`resume=True` is verification-only and makes no new capture. After an
infrastructure repair, `resume=True, continue_unstarted=True` explicitly permits
first attempts for untouched jobs. All existing artifacts are verified before
new starts. Failed or incomplete attempts are never retried, and deleted attempt
directories are not reclassified as untouched. Continuation summaries form an
append-only hash-linked history; the original summary is preserved.

Hashes establish local consistency, not authenticated model weights or human
judgment. Runtime safety/managed policies and the observed date wrapper remain;
this is not a claim of zero host context or controlled generation randomness.
