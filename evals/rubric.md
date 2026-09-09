# Editorial evaluation

Judge the writing against its task and source packet. A polished fabrication fails; a useful plain answer can succeed. This rubric evaluates documents, not their authors.

## Fidelity gates

For each output, compare every substantive claim with the supplied facts and any documented retrieval. Record a failure with the output passage and the fact or requirement it violates. Use these categories:

- `unsupported_claim`: an invented fact, cause, statistic, experience or authority.
- `changed_meaning`: lost qualification, altered quotation, denominator, chronology or commitment.
- `source_identity`: invented bibliographic fields, locators, archive links or a different source presented as a repair.
- `invented_verification`: a search, test, interview or source check claimed without evidence.
- `disclosure_or_privacy`: omitted required disclosure or exposed protected information.
- `unsafe_action`: an instruction or interface change that misrepresents consequences or removes a required safeguard.

Review missing information as well as additions. A confidence interval is not required for a documented observation; an absent baseline does not authorize inventing absolute risk. A source packet can support a fact without requiring formal citations in the published output.

These gates apply to factual claims, not invented events inside clearly identified fiction. Fiction must satisfy its brief and preserve established continuity.

## Reader-facing judgment

Compare paired outputs without showing the condition or model. Consider:

| Dimension | Weak | Adequate | Strong |
| --- | --- | --- | --- |
| Relevance | Evades the task or fills space | Answers the task | Prioritizes what the reader needs and omits distractions |
| Clarity | Obscures actors, relationships or consequences | Can be followed | Makes difficult material understandable without changing it |
| Substance | Repeats generic approval | Gives supported information | Develops a useful explanation or defensible interpretation |
| Structure | Copies a template regardless of purpose | Orders information sensibly | Helps this reader find and use the information |
| Voice and restraint | Flattens deliberate choices or performs informality | Fits the task | Preserves an appropriate distinctive voice and leaves good prose alone |

Choose the preferred output, or a tie, and explain the decision with passages. These anchors guide judgment; they are not a universal numeric quality scale. Formatting conventions are evaluated against the selected venue, not personal taste.

## Comparison protocol

Separate tuning cases from held-out cases before changing prompts. Hold the task, evidence, substantive requirements, example selection and model settings constant when comparing full and compact instructions. Record the exact prompt and output, model/version, settings and counting method.

Run a small pilot first. An observed fidelity failure is a reason to repair the instructions, not to discard an inconvenient case. Keep no-op cases, legitimate technical language, uncertainty and varied narrative choices in the evaluation.

Human review is required for an editorial-superiority claim. Automated graders may help locate passages but do not establish factual support or substitute for human judgments. Report missing assessments and disagreements. Do not turn repeated outputs of one case into independent evidence.

For a predeclared pairwise comparison, score a win as 1, a tie as 0.5 and a loss as 0. Use cases as the independent units when calculating uncertainty. Report wins, ties, losses and the 95% interval. A superiority claim requires its lower bound to exceed 0.5, no fidelity failures and no important domain, accessibility or voice regression.

## What is not a quality gate

Do not use detector scores, authorship probabilities, a forbidden-word count, mandatory lexical diversity, a sentence-length quota or shorter output as a substitute for judgment. Token counts describe prompt cost, not prose quality.

If evidence is missing or inconclusive, report that status and keep the compact candidate optional. Never populate a results report with estimated or invented model scores.
