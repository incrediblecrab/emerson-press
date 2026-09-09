---
id: sources.ai-slop-research
layer: sources
version: 2.3.0
status: active
budget: none
evidence_kind: mixed-research
checked_on: 2026-09-08
verification_status: partial
source_version: "Selected final publications (2024-2025); Antislop v2 (2025-10-21), Miklian/Katsos v1 (2026-06-10), Baltes et al. historical v3 (2026-06-13) with v4 metadata/abstract checked; provider versions and watchlist limits below"
source_urls:
  - https://doi.org/10.1126/sciadv.adt3813
  - https://aclanthology.org/2025.coling-main.426/
  - https://doi.org/10.1126/sciadv.adn5290
  - https://arxiv.org/abs/2510.15061v2
  - https://arxiv.org/abs/2606.12073v1
  - https://arxiv.org/abs/2603.27249v3
  - https://arxiv.org/abs/2603.27249v4
  - https://info.arxiv.org/help/moderation/index.html
  - https://arxiv.org/html/2607.19257v1
  - https://model-spec.openai.com/2026-08-18.html
  - https://developers.openai.com/api/docs/guides/prompt-engineering
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
verification_note: "Selected journal/ACL records and abstracts, and provider guidance, were independently checked in the 2026-09-08 research artifact. This refresh also checked arXiv version metadata/abstracts and standing moderation policy. It is not a systematic review or a reproduction of experiments; detailed historical tables are not newly audited, and watchlist results remain unread."
retrieved: 2026-08-09
consumers:
  - stop-the-slop/accuracy.md
  - stop-the-slop/anti-slop.md
  - stop-the-slop/restraint.md
  - stop-the-slop/rhythm.md
  - stop-the-slop/voice.md
  - domains/education-level/07-post-graduate.md
  - domains/fiction.md
  - domains/non-fiction.md
  - domains/technical.md
---

# Source: The Research Literature on AI Slop

Selected evidence for writing decisions, not a universal definition of slop. Lexical frequency, writing quality, diversity, authorship and reader suspicion are different outcomes. A study measuring one does not automatically establish another, and research does not settle every editorial preference.

All summaries below are original. The session artifact `ai-writing-research.json`, checked September 8, verifies selected primary records and abstracts, not every result in every paper. Earlier full-reading claims are historical provenance, not a claim that this refresh reproduced those readings or analyses.

## Selected Peer-Reviewed Support

### Lexical Population Change: Kobak and Colleagues

[*Delving into LLM-assisted writing in biomedical publications through excess vocabulary*](https://doi.org/10.1126/sciadv.adt3813), **Science Advances, July 2, 2025**. The final article analyzes more than 15 million biomedical abstracts and estimates a **13.5% lower bound** on the share of 2024 abstracts in the studied population processed with LLMs. The primary record and publisher-supplied abstract were checked through Europe PMC; an [open record is available](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219543/).

This is a population-level lexical-shift estimate with a particular corpus, period and inference method. It is not a quality rating, a bad-word inventory, a test of prompt bans or proof of an individual author's tool use. The older preprint's 10% estimate is not the final result used here.

**Writing implication:** a changing word distribution can motivate examining habits in comparable texts. Whether to revise a particular sentence still depends on accuracy, meaning and the reader's task.

### Lexical Causes: Juzek and Ward

[*Why Does ChatGPT Delve So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models*](https://aclanthology.org/2025.coling-main.426/), **COLING, January 2025**. The ACL Anthology record and abstract establish a peer-reviewed conference paper investigating lexical overrepresentation.

The authors describe evidence consistent with an RLHF contribution, but their exploratory causal results are mixed and visibility into model development is limited. This does not establish one cause across providers, models or genres. Detailed preference-study effect sizes were not independently checked and are not used here.

**Writing implication:** review habitual inflated diction in context. Neither an RLHF explanation nor a frequency difference establishes that every use of a focal word is worse.

### Quality and Diversity: Doshi and Hauser

[*Generative AI enhances individual creativity but reduces the collective diversity of novel content*](https://doi.org/10.1126/sciadv.adn5290), **Science Advances, July 12, 2024**. In a constrained short-fiction experiment, access to GPT-4-generated story ideas improved ratings of human-written stories, particularly for less creative writers, while making stories more similar across writers. The publisher introduction and primary record/abstract were checked; an [open record is available](https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/).

This is human writing assisted by AI ideas, not an experiment comparing all AI-written prose with all human prose. Quality and across-story diversity moved in different directions.

**Writing implication:** assess usefulness and variation separately. A polished, well-rated response can still resemble many other responses; surface difference alone is not quality either. No result here quantifies the benefit of this repository's prompts.

## arXiv Provenance

All three papers below have arXiv records. The former description of two preprints and one unattached manuscript was inconsistent and is retired.

| Paper | Version used and verification boundary |
| --- | --- |
| Samuel Paech, Allen Roush, Judah Goldfeder and Ravid Shwartz-Ziv, *Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models* | [2510.15061v2](https://arxiv.org/abs/2510.15061v2), October 21, 2025; first submitted October 16. Metadata and abstract checked; detailed appendix measurements not re-audited here. |
| Jason Miklian and John E. Katsos, *“That's AI Slop, You Bot!” Studying Accusations, Evidence, and Credibility in Online Discourse Towards LLM-Generated Comments* | [2606.12073v1](https://arxiv.org/abs/2606.12073v1), June 10, 2026. Metadata and abstract checked. |
| Sebastian Baltes, Marc Cheong and Christoph Treude, *“An Endless Stream of AI Slop”: How Developers Discuss the Burden of AI-Assisted Software Development* | Historical reading: [2603.27249v3](https://arxiv.org/abs/2603.27249v3), June 13, 2026. A [v4 dated August 28, 2026](https://arxiv.org/abs/2603.27249v4) is now available; its metadata and abstract were checked, not its full results. v3 is not the latest version. |

These are version-specific arXiv citations. Peer-reviewed venue publication of these papers was not established in this refresh. arXiv moderation is not peer review, but an arXiv record or an absent journal-reference field also does not prove that a paper has never undergone review elsewhere.

### Antislop: Three Different Interventions

The paper profiles patterns against human baselines and tests ways to reduce overproduction. Historical method notes describe Reddit creative-writing prompts, `wordfreq` for words, and Reddit/Gutenberg reference material for n-grams. These do not establish a universal English baseline or transfer performance in technical, medical or legal writing.

Keep the interventions separate:

| Intervention | What changes | What it does not establish |
| --- | --- | --- |
| Token banning | Inference-time exclusion of tokens; shared token pieces can block more than the intended word or phrase. | An effect size for natural-language instructions to avoid a construction. |
| Antislop Sampler | Inference-time sequence detection, backtracking and probability adjustment during resampling. It does not fine-tune model weights. | That a prompt-only module implements this sampler or inherits its suppression/quality trade-off. |
| Final Token Preference Optimization (FTPO) | Training-time token-level preference optimization that changes model weights. | That its ablation results belong to token banning, sampler strength or ordinary prompt revision. |

The abstract reports substantial suppression under its experimental conditions. This dossier does not carry those percentages into prompt instructions. Earlier detailed suppression tables and cross-model frequency tables require checking the exact experiment, model, baseline and rubric before reuse; they are not newly verified here.

The code/results release is attributed to the authors under [MIT licensing](https://github.com/sam-paech/auto-antislop). The previous dossier also recorded the authors' disclosure of LLM drafting assistance and human responsibility for results and citations; that is a disclosure, not a validation method.

**Two corrections govern reuse.** A pattern absent from a truncated reference table is not proven absent from human writing. And a high rate in a sampled set of models is not a universal authorship fingerprint. `antislop-banlists.md` retires the unreplicated local overlap and correlation figures; this note no longer cites them as independent confirmation.

### Accusation: Discourse and Association, Not a Revision Experiment

Miklian and Katsos analyze 25 million Hacker News and Reddit comments from 2023-2026, using LLM-assisted judgments, speech-act coding and matched comparisons of accused and non-accused human comments. They report a growing pejorative discourse and find that prose features distinguishing their AI/human comparison did not predict which human comments were accused. They interpret accusations partly as social gatekeeping.

That finding concerns association within selected online communities. It does not establish an irreducible percentage of accusations, prove that no revision can affect suspicion, or test the causal effect of revising machine-generated prose. A null association among humans is not proof of no intervention effect. Earlier forum-specific sentence-variance figures also cannot establish a universal claim that machine prose is either flat or unusually varied.

**Writing implication:** improve identifiable reader-facing faults rather than promise protection from accusation. Suspicion is not authorship evidence. Keeping this repository out of the detection business is a house boundary supported by these limitations, not a theorem that evasion is impossible.

### Developer Burden: Reported Experience, Not Prevalence

Baltes, Cheong and Treude qualitatively analyze **1,154 Reddit and Hacker News posts**, organizing concerns about review friction, quality degradation, incentives and consequences. Their abstract frames the burden as costs that can be passed from generators to reviewers and maintainers.

This is a qualitative account of selected discourse. Code frequencies describe that coded material, not workforce prevalence. Participants' workload and failure anecdotes are reported experiences, not independently audited benchmarks or causal rates. The earlier account notes model-assisted coding under author review; those design limits matter when interpreting the themes.

**Writing implication:** make a draft easy to verify and review; do not use volume as a proxy for contribution. Self-review, bounded changes and clear ownership are candidate practices, not interventions whose effectiveness this corpus measured.

## Institutional Policy Is a Separate Evidence Type

arXiv's [standing moderation policy](https://info.arxiv.org/help/moderation/index.html), checked September 8, requires significant generative text-tool use to be reported consistently with subject methodology standards, holds human authors responsible for the contents, and says not to list the tool as an author.

This is venue policy, not experimental evidence for a style rule. Good prose does not replace disclosure, and arXiv's requirements do not automatically bind other venues. The earlier October 2025 CS content-type summary was not re-audited here and should not be cited as a current submission rule from this dossier. The previously reported one-year sanction remains unverified and excluded.

## Provider Advice and a Research Watchlist

Provider documentation is operational advice, not an independent experiment validating this repository:

- **OpenAI Model Spec, [August 18, 2026](https://model-spec.openai.com/2026-08-18.html):** higher-authority instructions take precedence; later messages can supersede earlier instructions at the same authority. A later user request does not thereby override a system instruction. This is not a universal within-message last-line-wins rule.
- **OpenAI's [living prompt-engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering):** recommends model snapshot pins and evaluation suites and distinguishes high-level instructions from input prompts. It does not independently demonstrate that a shorter writing guide performs better.
- **Anthropic's [living prompting guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices):** recommends clear constraints, useful motivation and relevant, diverse examples, with model-specific considerations. Its advice and suggested example counts are not a universal optimum or attributable to all providers.

**WATCHLIST only:** [*Prompt Design at Scale*, arXiv:2607.19257v1](https://arxiv.org/html/2607.19257v1), July 2026. The research artifact checked the introduction, experimental design and stated contributions, including instruction count/format/role placement and synthetic long-context retrieval. **Full results were not reviewed.** It can motivate future local ablations, not establish an editorial rule count, token ceiling or repository effect size.

## What Modules Can Responsibly Take

1. Check concrete claims and relationships, not just lexical cues. Specificity must be supported; invented detail is not an improvement.
2. Preserve accurate terminology, meaningful repetition and necessary uncertainty. A lower pattern count is not itself better writing.
3. Judge quality, diversity and reviewer burden separately on the intended task. Do not generalize a fiction or forum result to every domain.
4. Label house choices as choices. No cited study measures the efficacy of these Markdown modules; that requires a separately authorized, version-pinned local evaluation.

## Compact Correction Log

- Miklian/Katsos is arXiv:2606.12073, not an unattached manuscript. Baltes et al.'s later subtitle replaces the v1 subtitle; v4 availability is now recorded without claiming a full v4 review.
- The final Kobak article's 13.5% lower bound replaces the older 10% preprint figure.
- Truncated-corpus absence, universal lexical fingerprints, unreplicated dataset tables and cross-intervention suppression claims are no longer grounds for module rules.
- Accusation associations and qualitative developer reports no longer support causal impossibility or population-prevalence claims. Provider advice and watchlist designs remain separate from tested writing effects.
