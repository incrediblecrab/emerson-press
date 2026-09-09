# emerson-press

Writing instructions for concrete, natural prose without generic AI-style filler.

The newsroom target is the specificity, editorial judgment and unforced voice associated with strong New York Times or Wall Street Journal writing. AP style supplies the mechanics; it is not the whole voice. The aim is better writing, not concealed AI involvement or copies of those publications' articles.

A fluent fabrication fails. A good existing passage may need no change. Familiar words, formal language, em dashes and three-item lists are not defects by themselves.

Use these as task-specific editorial guidance, not an automatic quality upgrade.

## Use the instructions

The Markdown files are the product. You do not need to install anything to use them.

Start with the [editorial task contract](stop-the-slop/prompts/task.md). State whether you want a draft, edit or review, what the reader needs, the medium, and which facts or sources are available. A reader's age or degree is not a substitute for knowing their familiarity with the subject.

For a full-reference prompt, load the contract, the six `stop-the-slop/` modules and only the relevant specialized modules. Omit frontmatter and `## Examples` unless you need particular examples. The optional assembler below handles those exclusions.

| Material | What to select |
| --- | --- |
| `stop-the-slop/` | Accuracy, restraint, voice, anti-slop, formatting and rhythm |
| `domains/` | One primary genre: press, non-fiction, fiction, technical, marketing, legal, medical or general |
| `domains/citation/` | A requested citation style: MLA 9, APA 7, Chicago 18, IEEE, AMA 11 or Bluebook 22 |
| `domains/education-level/` | An optional classroom or academic-task preset, not a label imposed on every reader with those credentials |
| `domains/user-interface/` | One task-appropriate medium, applications or website, plus relevant accessibility, Apple or chart guidance; chart guidance can also stand alone |
| `tests/sources/` | Maintenance evidence for authors of the modules; never load these dossiers alongside a draft |

For a news article, select `domains/press.md`. For a patient handout, select `domains/medical.md` and describe the actual reader rather than choosing a grade as a proxy. A product error uses `domains/technical.md`, `domains/user-interface/applications.md` and `domains/user-interface/accessibility.md`.

Healthcare marketing keeps marketing as its primary genre and adds the medical module's `## Safeguards` section. Legal safeguards can be added in the same way. These sections protect substantive claims without importing a different document's citation format.

## Which rule controls?

The selected genre and explicit venue requirements control publication mechanics. Citation modules control bibliographic rendering where formal citations apply. Reader guidance controls explanation and scaffolding. Interface overlays control their named surfaces. Relevant medical and legal safeguards are additive.

None of those choices permits invented facts, altered quotation meaning, fabricated verification or removal of required disclosure. Core stylistic advice is a default, not a reason to erase a deliberate voice.

Put compatible instructions together in a host-supported instruction block. Host rules still apply. A later user request does not automatically override a conflicting system instruction; if standing instructions are used, they must explicitly delegate the style choices allowed in the request.

## Compact guide

[`quick-guide.md`](quick-guide.md) is a generated, self-contained candidate built from the task contract and the core operating sections. It contains no coding-agent policy or changing research statistics.

**The compact candidate has not earned a claim of better writing.** Full-reference packs remain the assembler's default. Use the compact guide when you want to try a smaller instruction set, and compare its behavior rather than assuming fewer tokens are better.

Detailed diagnostics and examples remain in the modules. An example's supplied-facts packet is part of the example, not optional context that can be dropped while keeping its improved output.

## Optional author tools

All tooling, unit tests, evaluation records and source research are centralized in
[`tests/`](tests/README.md). Python 3.10 or later is required only for the author tools:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r tests/requirements-dev.txt
.venv/bin/python -c 'import tiktoken; tiktoken.get_encoding("o200k_base")'
```

The last command fetches the public tokenizer data once; subsequent local checks use its cache. No model credentials are needed.

Build a full-reference press pack and its manifest:

```sh
.venv/bin/python -m tests.scripts.build --profile press --mode draft \
  --output dist/press.md --manifest dist/press.json
```

Try the same selection with `--variant compact`, using a different output path. Exports refuse to overwrite existing artifacts. The manifest records actual assembled token counts, source hashes and selected examples; it is not a quality score.

`--variant focused` is an experimental draft/edit recipe that omits `## Detect` checklists from every selected module while retaining the other guidance, mechanics, boundaries and safeguards. Its first source-matched tuning pass did not improve literal artifact compliance. Full remains the default; focused is not a review recipe or a demonstrated quality improvement.

Profiles also cover general writing, technical documentation, marketing websites, healthcare marketing, patient handouts, Apple applications and explicitly requested graduate research papers. For a custom selection, use repeated `--module` arguments instead of `--profile`:

```sh
.venv/bin/python -m tests.scripts.build --mode edit \
  --module domains/non-fiction.md --module domains/citation/mla9.md
```

Use `--safeguard medical` or `--safeguard legal` for applicable mixed-domain claims. Add a particular example with `--example stop-the-slop/accuracy.md#causation-from-correlation`; selectors use the slug of a standalone bold example heading. Incompatible selections and unknown examples fail explicitly.

## Evidence and evaluation

The AP dossier distinguishes its 56th-edition basis from [public 58th-edition updates](https://www.ap.org/media-center/press-releases/2026/new-ap-stylebook-features-expanded-artificial-intelligence-chapter/), released May 27, 2026. AP's [July 23, 2026 newsroom AI update](https://www.ap.org/the-definitive-source/announcements/ap-updates-newsroom-standards-for-artificial-intelligence/) describes approved assistance with human review and a disclosure framework. That organizational policy is separate from choosing AP punctuation. A complete entry-level review of the licensed 58th edition remains outstanding.

Source dossiers identify their evidence type, version, checked date and verification limits. A practitioner observation is not a controlled experiment. A corpus frequency is not a quality score. A source absent from a search is not proved nonexistent.

The [evaluation workflow](tests/evals/README.md) uses original supplied-fact cases, frozen original instructions and real response records. The [rubric](tests/evals/rubric.md) requires fidelity, useful content and respect for intentional voice. It includes no-op cases and treats human preference separately from prompt size.

The [model-only tuning pilot](tests/evals/synthetic/README.md) retains its actual responses, failed judgments and negative findings. Its full-versus-task-contract comparison used repository instructions in both conditions; it did not test repository use against an untreated draft. The [newsroom study](tests/evals/newsroom/README.md) uses a `bare-task` control and explicit assessment of noticeable generic prose, not factuality alone.

The modern newsroom tuning result is mixed and judge-dependent; it does not establish an overall gain or slop elimination. A separate [scoped-accuracy revision pilot](tests/evals/newsroom/README.md#source-checking-and-the-scoped-revision) preserved the tested warnings but did not establish better prose than the earlier recipe. Earlier results must not be attributed to the revised payload.

The [completed primary backtest](tests/evals/newsroom/primary-results.md) covered 438 drafts across 219 cases and 212 family clusters. Full won 167 judgments, bare won 152, 114 tied and five preferences were missing. The preregistered randomized 95% mean-preference interval, [0.4076, 0.5553], included the neutral score of 0.5. Judges agreed on only 73/214 completely assessed pairs. The study did not establish a preference gain or elimination of noticeable slop; [every unchanged draft](tests/evals/newsroom/examples/primary/README.md) and all failed judgments remain available.

Full remains the assembler's existing default, not an empirically established best recipe. Compact was not the primary contrast and is not promoted by this result. No human-reviewed editorial-superiority claim is established.

See [CONTRIBUTING.md](tests/CONTRIBUTING.md) for source maintenance, generated artifacts and regression checks. Copyrighted working texts in `raw-data/` must remain untracked and out of prompt exports. Existing file-specific attribution and license notices still apply; no blanket license is inferred from them.
