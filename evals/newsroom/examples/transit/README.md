# Transit explainer: unchanged model outputs

**Synthetic exercise, not a real transit report.** These are all eight original
model responses, not hand-edited improvements or selected best-case excerpts.
They are separate drafts from the same reporting packet, not edits of one another.
The [reporting packet](../../../synthetic/cases/public-press-transit-recommendation.json)
sets a May 8, 2026 snapshot and asks for a 350–500-word explainer. Its unusually
explicit source constraints make this a smoke check, not a representative sample
of ordinary writing prompts.

| Writer | No repository instructions | Task contract only | Full press recipe | Compact press recipe |
|---|---|---|---|---|
| Claude Haiku 4.5 | [Bare](claude-haiku-4-5-bare-task.txt) | [Contract](claude-haiku-4-5-task-only.txt) | [Full](claude-haiku-4-5-full.txt) | [Compact](claude-haiku-4-5-compact.txt) |
| GPT-5.4 mini | [Bare](gpt-5-4-mini-bare-task.txt) | [Contract](gpt-5-4-mini-task-only.txt) | [Full](gpt-5-4-mini-full.txt) | [Compact](gpt-5-4-mini-compact.txt) |

Unlike the bare Haiku response, its full-recipe response has no unnecessary
`[date from minutes]` placeholder and uses fewer subheads. The GPT baseline is already
fairly direct; a guided response is not automatically a dramatic improvement.
Headings and recap sentences are not inherently wrong, so compare how well each
one serves this particular explainer rather than merely counting them.

The stronger-model pairwise judges preferred full and compact over bare for both
writers, but full versus compact split. Pointwise slop labels were only absent or
minor, and the Haiku outputs retained factual concerns. For instance, its compact
version invents announcement channels. This is evidence to inspect, not a claim
of NYT/WSJ quality, factual clearance or statistically demonstrated slop removal.

`manifest.json` links every exact text to its recorded response and result hashes.
