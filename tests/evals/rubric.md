# Editorial evaluation

Judge the writing against its task and source packet. The central promise is useful, specific prose without conspicuous generic AI-style padding, not merely error-free output. Professional newsroom writing, including the strengths associated with The New York Times and The Wall Street Journal, is an editorial target: reporting-led structure, precise language, useful context and deliberate rhythm. It is not a request to copy their articles or a claim that an output meets their standards.

AP style supplies house mechanics, not the whole voice or a substitute for editorial judgment. A polished fabrication still fails. This rubric evaluates documents, not their authors.

## Noticeable generic writing

Assess the effect of the language in context. A stock phrase, em dash, three-part list, technical term or long sentence is not inherently a defect. Identify passages that materially weaken the piece:

| Test | Noticeable weakness | Desired result |
| --- | --- | --- |
| Reporting-led opening | Announces the topic's importance in reusable language before telling the news | Leads with a specific development, finding, tension or supported scene |
| Information gain | Rephrases earlier points or adds paragraphs that contribute no fact, explanation or useful connection | Each paragraph advances the reader's understanding |
| Specificity | Substitutes vague praise, abstractions or grand implications for the available actors and evidence | Names who did what, what changed, and which consequences the record supports |
| Shape and progression | Imposes the same symmetrical template, signposting and recap regardless of the story | Organizes the material around this story's actual question and evidence |
| Voice and rhythm | Sounds mechanically uniform, overdecorated or insistently conversational | Uses an appropriate, unforced voice and purposeful changes in pace |
| Ending | Restates a generic lesson or forecasts significance without support | Ends on a supported consequence, unresolved question, telling detail or useful final fact |

Distinguish an isolated minor edit from **salient slop**: generic framing, repetition or templating prominent enough to distract from the reporting or make the piece feel interchangeable. Record the relevant passages and explain their effect. Do not infer who wrote the text, assign an authorship probability or use a detector.

For newsroom experiments, report editorial preference and the incidence of salient slop separately from factual and mechanical errors. A faithful answer can still be dull or generic; fluent prose can still fail fidelity. Missing or refused articles are task failures, not clean examples with no slop. AP mechanics must be checked against the applicable supplied or verified rules, not invented recollections of an unread manual.

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
