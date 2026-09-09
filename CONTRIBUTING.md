# Contributing

Improve the reader's result, not the number of rules. Before adding an instruction, identify a failure it fixes and a legitimate case it must leave alone. Preserve existing useful detail rather than forcing every module under a token ceiling.

## Editing modules

Keep the existing frontmatter, IDs and `## Detect`/`## Write` structure. `## Write` is the canonical operating section for compact core exports; essential exceptions and safeguards must not exist only in an introduction or diagnostic list.

Put `## Examples` last. Give each example a unique standalone bold heading and an inline `**Supplied facts:**` packet. The packet must support the accepted output, including any dates, figures, quotation, bibliographic details or verification claims. Mark synthetic scenarios clearly. Do not turn a hypothetical demonstration into a claim about a real person or study.

Before-and-after pairs must distinguish editing from enrichment or proposals. Unknown source fields stay unknown. A grammatical repair must not become a new contract term, a fabricated interview or an invented confidence interval. Preserve legitimate no-op cases.

Specialized modules keep their scope: citation formatting does not override clinical meaning; reader support does not select a publication manual or demand original research. `domain/medical.md` and `domain/legal.md` expose `## Safeguards` before their examples for mixed-domain use.

UI modules declare `kind: medium` or `kind: overlay`; only overlays can declare the boolean `standalone: true`. Adding a core file also requires a deliberate update to the ordered `CORE` registry in `scripts/modules.py`, so the file cannot silently disappear from exports.

Use original wording, American spelling and the selected style's actual exceptions. Do not infer a primary source's wording or omissions from a paraphrased extraction.

## Source provenance

Each module's `evidence:` links to source dossiers; each dossier's `consumers:` lists the reciprocal modules. A dossier supports only the claims it identifies, not every proposition in a consumer.

Source dossiers also carry:

| Field | Meaning |
| --- | --- |
| `evidence_kind` | Publisher guidance, peer-reviewed/preprint/mixed research, dataset analysis, practitioner/community observation or house inference |
| `source_version` | The actual edition, revision or dated baseline; state missing pins rather than inventing them |
| `source_urls` | Public source locations, not a substitute for reading the relevant material |
| `checked_on` | Date the described check was performed |
| `verification_status` | `verified`, `partial`, `historical` or `unverified` |
| `verification_note` | What was checked and what remains unsupported or inaccessible |

Use precise source locators for load-bearing claims. Distinguish an initial preprint from its later journal version, a print manual from a living update, and a rule from a publisher's public summary. A paywall or failed retrieval is a limitation, not permission to infer a rule.

Locally computed figures need an attributable input version and a reproducible method. Otherwise qualify or retire the figures. Absence from a truncated frequency list does not mean absence from human language. Study accuracy does not determine its false-positive rate. Results from sampling or training interventions do not measure prompt-only instructions.

Keep source-specific license and attribution notices. Never commit copyrighted source books, large working extractions, credentials or confidential records. `raw-data/` is ignored and checked against the Git inventory. The loader also rejects paths resolving into private/dependency directories, including case variants and symlink aliases. Licensing original reusable material requires an explicit owner decision.

## Authoring checks

Install the author dependencies as described in the README. After editing, regenerate the guide and recount metadata:

```sh
.venv/bin/python -m scripts.build --write-quick-guide
.venv/bin/python -m scripts.check --recount
.venv/bin/python -m scripts.evaluate validate
.venv/bin/python -m unittest discover -s tests
```

`tokens` and legacy `budget` measure a module body with frontmatter and `## Examples` through EOF removed. They are observations, not ceilings. Exports count their actual assembled text separately, including the task contract and selected examples. Counts use `o200k_base` with literal token-marker text treated as ordinary text.

The guide is generated from `prompts/task.md` and core operating sections. Edit those sources, not the generated guide. The build and checker share one Markdown parser, including fenced-code handling and example selection.

Checks cover structural invariants, compatible profiles, reciprocal links, source metadata, example-packet presence and generated drift. Examples must be the final level-two section so later operating rules cannot silently disappear from exports. A packet's presence does not prove that it supports the example. Checks also do not establish that a source supports a claim, that a platform rule is current or that the prose is good. Test every new failure gate with a healthy fixture, plant the defect, and verify its nonzero exit and diagnostic.

## Evaluation and release decisions

The initial evaluation corpus separates tuning and held-out cases. Do not move a failing held-out case into tuning to improve a report. Add regression cases for discovered failures and document changes to an evaluation set before comparing results.

`evals/baseline.json` pins the original instructions to Git commit `3ddd4e5ddea42afbeda05eefffd3669dbb86c8fc`; authoring checks therefore need that history. Keep original, corrected-full and compact conditions distinct. For a compression comparison, the corrected-full and compact conditions must use the same substantive rules, task evidence and example selection.

Use only actual response records and explicit human judgments for a superiority claim. Record model/version and settings, keep source/prompt/response hashes, and report uncertainty and missing assessments. Verify that the captured text matches its rendered-component hashes, and do not pool pairs from different instruction revisions. Do not use detector scores, word-list compliance or fewer tokens as evidence of better writing.

Evaluation runs stay under ignored `evals/runs/` until reviewed for publication. Do not include private prompts, credentials or identifying reviewer details. A release report should state its scope and limits, not hide a failed comparison.

Full-reference packs remain the default until the predeclared evaluation gate supports a change. The compact guide is available for experimentation, not presented as a proven improvement.
