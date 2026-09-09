---
id: sources.antislop-banlists
layer: sources
version: 1.2.0
status: active
budget: none
evidence_kind: dataset-analysis
checked_on: 2026-09-08
verification_status: historical
source_version: "Historical 2026-08-09 inspection of auto-antislop/slop-forensics; repository commit, dataset revision and analysis script were not pinned"
source_urls:
  - https://github.com/sam-paech/auto-antislop
verification_note: "The artifact inventory below preserves the earlier dossier's descriptions, not newly verified sizes. Its local overlap, rank, clustering, score and correlation calculations have not been replicated from tracked scripts and data pins. Numerical tables are retired as current evidence; no raw corpus was downloaded."
source:
  title: "auto-antislop / slop-forensics released datasets"
  author: "Samuel J Paech"
  repository: "https://github.com/sam-paech/auto-antislop"
  license: "MIT"
  artifacts:
    - "slop-forensics/data/slop_list.json (1,000 words)"
    - "slop-forensics/data/slop_list_bigrams.json (200 bigrams)"
    - "slop-forensics/data/slop_list_trigrams.json (200 trigrams)"
    - "slop-forensics/results/slop_profile_results.json (38 model profiles)"
    - "data/human_writing_profile.json (6.1 Gc human baseline)"
  human_baseline: "Nitral-AI/Reddit-SFW-Writing_Prompts_ShareGPT"
  method: "Earlier dossier reported direct JSON analysis; calculations were not preserved with a tracked script and immutable data pins and were not rerun in this refresh"
retrieved: 2026-08-09
consumers:
  - stop-the-slop/anti-slop.md
  - stop-the-slop/restraint.md
  - stop-the-slop/voice.md
  - domains/fiction.md
---

# Source: Antislop Lists and Their Reference Baseline

Companion to `ai-slop-research.md`. This records a historical inspection of released artifacts, not an independent validation of the project's metric or of prompt-level writing instructions. The project's data carries an MIT license; this account and its arrangement are original.

## Verification Boundary

Earlier revisions reported exact overlaps, human-frequency ranks, corpus sizes, stem clusters, model scores and correlations as locally computed facts. No tracked analysis script or immutable input pins establish those calculations in this repository. The tables have therefore been retired, not silently promoted into current evidence. The sizes in the frontmatter are retained historical inventory descriptions.

A pipeline's per-run selection quota, a published static list and a retained human-frequency table are different artifacts. Do not use a quota from the paper as the size of a released list. Likewise, do not treat a frequency profile as the complete raw corpus.

## What Absence and Overrepresentation Mean

**Overrepresentation is relative to a comparator.** A phrase can be frequent in human writing and still occur disproportionately in sampled model output. Its ratio does not establish that a particular use is bad, unnecessary or machine-authored.

**Absence from the retained top-500,000 n-grams is not absence from human language.** An omitted entry may fall below the retention cutoff, differ under tokenization or stop-word removal, or be uncommon in the selected genre. It need not have zero occurrences even in the original corpus. A word missing from retained bigrams is not a measured zero in a complete unigram distribution either.

The earlier inference from missing entries to a flatly bannable, exclusively machine-made minority is withdrawn. No subset of these lists earns a prohibition by having an absent or undefined denominator. Preprocessed n-grams also need not be literal adjacent phrases in the original prose.

**The reference population matters.** The historical analysis used a Reddit creative-writing baseline. Fiction names, scenery and dialogue habits are not a representative sample of documentation, journalism, academic argument or English generally. The earlier precise claims about how much of the list was genre vocabulary are unreplicated; the domain mismatch remains a reason to test transfer rather than assume it.

## What the Model Comparisons Cannot Establish

The earlier correlation table described a 38-model snapshot, without a tracked date or analysis pin. Its coefficients are not current verified findings.

Even if replicated, near-zero sample correlations with vocabulary complexity or length would mean little measured *linear association in that sample*. They would not establish independence, exclude nonlinear relationships, prove that verbosity never matters, or define slop universally. A correlation with a repetition score would not establish that repetition is the only cause of poor prose.

Nor was the model-size ladder a controlled scaling experiment: releases and fine-tunes can differ in data, training, decoding and prompts. It cannot establish that larger models inevitably eliminate these habits. A shared prefix is also only a rough clustering heuristic, not proof that entries have the same meaning.

## Useful Writing Instructions

These are house applications of the measurement limits, not tested prompt interventions:

- Review repetition where it displaces information or makes distinct points indistinguishable. Retain repeated names and technical terms when they preserve reference.
- Ask what a sentence adds: a fact, relation, qualification, consequence or necessary orientation. Replace empty reassurance or decorative scenery with relevant supported detail, or omit it.
- Evaluate diction and length against the reader's task. Neither ornate language nor brevity settles accuracy, usefulness or originality.
- Treat a lexical list as a source of review questions, not a detector or a find-and-replace specification. No listed word should require an edit without a reader-facing reason.
- Do not use list length as evidence of coverage: overlapping n-grams and related forms can count the same habit repeatedly. The amount of overlap here remains unverified.

No consumer should import the retired figures, a categorical ban, a model ranking or a writing-quality guarantee from this dossier. Sampler suppression, token banning and fine-tuning are separate interventions discussed in `ai-slop-research.md`; their results do not quantify prompt efficacy.

## Revalidation Needed Before Reusing Numbers

A future numerical claim needs an immutable repository/data revision or content hash, a tracked analysis method, preprocessing and retention rules, the exact denominator, and model/prompt provenance. Correlations additionally need their sample definition, metric definitions and uncertainty considered. That work was deliberately not performed in this bounded source refresh. Until then, the old tables are historical unreplicated notes, not quantitative support for modules.
