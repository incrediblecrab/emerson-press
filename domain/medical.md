---
id: domain.medical
layer: domain
kind: regulated
version: 2.2.0
status: draft
budget: 2870
tokens: 2870
mechanics: ama
evidence_floor: 5
evidence:
  - sources/ap-stylebook.md
---

# Domain: Medical

Clinical documentation, research reporting, patient education and public guidance. Use `citation/ama11.md` when the venue requests AMA references, not merely because the subject is health. A patient handout may use prose attribution, formal references or both.

Overstated certainty is a safety defect here, not a stylistic one. In press, an overclaim damages credibility. In marketing, it draws a regulator. In medicine, someone stops a medication, or does not go to the emergency department, or agrees to a procedure they would have declined with the real numbers. The prose is part of the intervention, and it can hurt the reader the way a wrong dose can.

A relative reduction can conceal very different absolute changes: halving a risk from 2 in 10,000 to 1 in 10,000 is not the same benefit as reducing it from 40% to 20%. Report the available absolute rates over the same period and on a common denominator. Natural frequencies can make a comparison easier to follow; no universal superiority claim or permission to invent a baseline follows.

Respect stated language preferences rather than applying person-first or identity-first by reflex. *Autistic person*, *Deaf person* and *person with epilepsy* can each be appropriate in context. An individual's preference controls writing about that person; a group's practices may vary. Do not infer a population-wide preference from a few participants.

## Detect

### Certainty and causation

- Efficacy stated more broadly or confidently than the applicable evidence supports: *this treatment works, X cures Y, safe and effective*.
- Relative risk presented as enough to judge benefit when the relevant absolute baseline is missing.
- Causal verbs on observational data — *causes*, *prevents*, *leads to* — where the design supports only association.
- Statistical significance read as clinical importance. A p-value below .05 in a large trial can describe a difference no patient would notice.
- A single study framed as settled, or a preprint cited without noting that it has not been peer reviewed.
- Mechanism reported as outcome: the drug lowers the marker, therefore it helps the patient. Many do not.
- Surrogate endpoints substituted for the endpoint anyone cares about.
- Screening benefit inferred from survival after diagnosis alone, without considering lead time, selection, overdiagnosis, mortality or harms.
- Relevant uncertainty omitted or overstated. Do not demand an interval for a claim that the underlying work does not quantify.

### Safety mechanics

- Error-prone medication-order forms such as `QD`, `U` or ambiguous drug abbreviations. Use the applicable safety standard; do not expand an ambiguous order by guessing the drug.
- A trailing zero — `1.0 mg`, read as ten — or a naked lead decimal — `.5 mg`, read as five. Both have killed people.
- An actionable medication instruction missing required drug, dose, route, timing or other necessary order details.
- Look-alike sound-alike drug names without the disambiguating form.
- Numbers whose denominators shift between sentences, so the reader has to convert to compare.

### Language about people

- Blanket person-first applied where the community prefers identity-first, or identity-first applied to a condition nobody claims as identity.
- Blame carried by clinical vocabulary: *non-compliant*, *failed the treatment*, *refused*, *denies*, *substance abuser*, *drug seeking*.
- *Committed suicide*, which encodes crime.
- The condition standing in for the person: *the diabetic in bed 4*, *sicklers*.
- Race, sex, or age reported without saying why it is clinically relevant, or a race-based correction applied as though race were a biological variable.
- Elective procedures described in the passive so nobody chose them.

## Write

Give available absolute risks with matching populations, periods and denominators; add relative change when useful. If only a relative figure is supplied, request the baseline or disclose that the absolute effect cannot be established from the record. Do not generate plausible rates to satisfy this instruction.

Give the relevant design and population with a research result, early enough to constrain its interpretation. Use only supplied or verified design details; do not create an age range, sample or prior condition for a more convincing opening.

Retain a supplied, relevant uncertainty interval and identify its type and level. Interpret it under the study's assumptions; do not invent an interval or present it as all possible values. Qualitative observations and individual reports can state their limits in words.

Say *associated with* when the design supports association. The discipline costs nothing and it is the difference between reporting a study and overselling it.

Name the population the finding does not cover. Trials in adults do not transfer to children; trials in one ancestry group may not transfer; a six-month endpoint says nothing about year five.

State what is unknown and, where known, what evidence could help resolve it. Do not invent a future test, accessible record or reassuring outcome.

Follow the community's stated preference on identity. *Autistic person*, *Deaf person*, *person with diabetes*, *person with schizophrenia*. When writing about an individual, use theirs. When writing about a group whose preference is contested, say so once rather than picking silently.

Describe documented behavior without judging it. Use a recorded frequency instead of *non-compliant* only when that frequency is known. Clarify what *failed treatment* means — response, adverse effects, access or something else — rather than inventing a clinical explanation.

For patient instructions, communicate the authorized action, timing and escalation signs clearly. If essential clinical details are missing or ambiguous, flag the material for qualified clinical review rather than completing an order or creating a treatment plan.

## Mechanics

Use the venue's requested clinical or publication convention. `citation/ama11.md` handles AMA references where formal citations apply; its source dossier records verification limits.

- Numbered citations in order of appearance, superscript, outside terminal punctuation.
- Superscripts suit a manuscript using AMA references. Do not impose them on a handout lacking a reference list, or remove a supplied accessible reference list merely because the audience includes patients. Use enough source identification for this document's purpose.
- Journal titles abbreviated per the NLM Catalog. Up to six authors listed; beyond that, the first three and *et al.*
- Use the units required by the clinical setting or venue. Convert only from a supported value with a verified factor; preserve meaningful precision.
- In medication instructions, use a leading zero below one and avoid an unnecessary trailing zero on a whole dose. Do not erase meaningful trailing-zero precision from laboratory or measurement results. Statistical notation follows the selected manual.
- Avoid error-prone dose abbreviations under the applicable medication-safety policy. This does not authorize guessing an ambiguous medication, route or schedule.
- Generic drug names, with the brand in parentheses on first mention if it matters.
- Report real registration, funding, authorship and disclosure information under the venue's requirements. Never claim an authorship or checklist review occurred unless it did.
- Choose the reporting guideline appropriate to the design, such as CONSORT, SPIRIT, PRISMA or STROBE, and verify the version adopted by the venue. Naming a checklist does not prove that the study satisfies it.

## Formats

### Clinical

Written for another clinician, under time pressure, in a document that is also a legal record.

Precise, structured, no filler. Abbreviate only from the approved list. Record what you observed and what you did, and mark inference as inference rather than folding it into the observation.

Hedge where the evidence hedges. *Consistent with* and *cannot exclude* are exact terms, not softening, and a reader in this genre reads them exactly.

The note will be read by someone who was not there, possibly years later, possibly in a deposition. Write for that reader.

### Research reporting

Written for a peer reviewer hunting the flaw and a clinician deciding whether the finding reaches their patient. Both read adversarially, and neither reads in order.

Methods before results, results before interpretation, and the interpretation held to what the design supports. Pick the reporting checklist for the design while planning the study, not while formatting the manuscript — it governs what has to be measured and recorded before there is anything to write up.

State the limitation a reviewer would raise. Naming your own weakness reads as candor; omitting it invites the reviewer to find it and to ask what else is missing.

### Patient-facing

Use the actual patient's familiarity, language and access needs, not an automatic eighth-grade proxy. The numbers and clinical distinctions stay true. IPLF's public [May 12, 2026 announcement](https://www.iplfederation.org/press-release-part-3/) describes ISO science-writing guidance for relevant, understandable and usable communication without sacrificing accuracy. That public scope is not a claim that the full normative standard was read.

Lead with what to do. Structure follows the reader's questions: what this is, what it means for me, what I do now, when I call someone.

Keep instructions manageable, explain unfamiliar terms and use common denominators where a numerical comparison needs them. Retain a familiar medical term when it is the clearest name for the condition or action.

A plainer word is only a translation when it denotes the same thing. *High blood pressure* stands in for *hypertension* safely. *Heart attack* does not stand in for *cardiac arrest* — those are different events with different treatments, and swapping one for the other is a clinical error wearing the costume of plain language.

Name the clinician-approved red flags and escalation route clearly, with any relevant threshold and local contact information. Do not invent a symptom threshold, emergency number for an unknown location or reassurance that changes when someone should seek care.

Say who this does not apply to, and send them somewhere.

### Public guidance

Health writing at population scale — guidance, campaign material, anything addressed to everyone.

The risk-number obligations bind hardest here, because the audience cannot ask a follow-up question and the material will be quoted out of context by someone who did not read the qualifier.

Give absolute risk. Say what changed and what did not when guidance is revised, because unexplained reversals cost more trust than the original error did. State the uncertainty rather than projecting a confidence that later evidence will embarrass.

Safe-messaging conventions apply to suicide and self-harm: no method detail, no presentation of a death as inevitable or as a solution, means-restriction framing, and resources in the piece.

## Evidence

The legacy `evidence_floor: 5` means careful, claim-appropriate support, not numerical uncertainty on every sentence. Attribute a patient report or chart observation as such. Support general treatment claims with appropriate current clinical evidence or guidance; identify design, population and endpoint when interpreting research. Label preprints, and do not treat a press release as the underlying study.

A real, correctly cited study can still fail to support the sentence built on it. Design, population, endpoint, estimated effect and relevant limitations must fit the claim.

Patient communication keeps the same truth standard while selecting the details needed for the decision. Preserve meaningful uncertainty and denominators; do not force an irrelevant or unavailable interval into a handout. Reader support never creates evidence or clinical expertise.

## Boundaries

Against `press`. Health journalism sits in both. `press` owns attribution, structure, and the reporting craft; `medical` owns the numbers. When a story reports a study, the risk-communication rules here govern the paragraph that gives the result, and the ban on hyping a single paper survives any editor's appetite for a stronger headline.

Against `marketing`. The dangerous overlap. Pharmaceutical and device promotion, wellness copy, and health-adjacent product claims all pull toward marketing's register and are held to this module's evidence floor. Substantiation is not satisfied by a mechanism, a testimonial, or a study in mice.

Against `non-fiction`. Science writing, illness memoir and the history of a trial all sit here at book length, and all of them make claims a reader may act on. `non-fiction` governs the prose and this module governs every live claim inside it — the estimate, the denominator, the population the finding covers. A finding written for a journal and the same finding written for patients are different documents, not one document at two reading levels.

Against `legal`. Both are regulated and both treat overstatement as a professional failure rather than a stylistic one. The difference that matters at the boundary is the reader's next move: a client can ask a follow-up question inside a continuing relationship, while a patient may act on a handout alone. Where the two meet — informed consent, an adverse-event notice, a capacity assessment — `legal` owns what the document must contain and this module owns how the risk is stated.

With `domain/education-level/`. Choose optional classroom presets only for an appropriate educational task. Age or credentials alone do not establish a patient's knowledge. Describe the actual reader and format; neither permits a changed estimate or unsupported reassurance.

## Safeguards

- Preserve clinical meaning, populations, outcomes, units, denominators and relevant uncertainty. Do not turn a marker change, association or isolated study into an established patient benefit.
- Give relevant absolute risks when available over matching periods and denominators. If a baseline, interval or design detail is missing, request or qualify it rather than inventing it.
- Keep observations, patient reports, inferences and general recommendations distinct. Do not fabricate patient history, adherence, test results or reasons for behavior.
- Preserve authorized medication and escalation instructions. Flag ambiguous drugs, units, doses, routes or timing for qualified clinical review; a copyedit cannot safely complete an unknown order.
- Respect privacy and stated language preferences. Do not add identifying details or infer a group's preference from an individual.
- These safeguards apply to relevant claims in press, marketing or other genres without importing AMA citation format or asserting that a medical review has occurred.

## Examples

These are synthetic evidence records and editing exercises, not treatment recommendations or verified reports of real studies.

**Relative risk with no floor under it**

**Supplied facts:** A fictional randomized comparison reports one-year stroke rates of 2 in 100 on the older drug and 1 in 100 on the new drug among adults over 65 with atrial fibrillation. Serious-bleeding rates are 5 and 7 in 1,000, respectively, over that year. No uncertainty interval or individual treatment recommendation is supplied.

> The new drug cuts your risk of stroke in half.

> In this trial of adults over 65 with atrial fibrillation, the one-year stroke rate was 20 in 1,000 on the older drug and 10 in 1,000 on the new one. Serious bleeding occurred at rates of 5 and 7 in 1,000, respectively.

*Review note: the supplied summary lacks uncertainty estimates; these rates are not an individual prescribing recommendation.*

**Association promoted to cause**

**Supplied facts:** A fictional observational cohort reports less chronic liver disease among coffee drinkers than nondrinkers. The supplied summary does not isolate coffee from other group differences or provide sample size, follow-up duration or a quantified effect.

> Coffee prevents liver disease.

> Coffee drinkers had a lower rate of chronic liver disease in this observational cohort. The comparison does not establish that coffee prevented disease; other differences between the groups could contribute.

**Screening measured by the flattering number**

**Supplied facts:** The supplied comparison gives five-year survival after diagnosis of 92% for screen-detected cases and 61% for cases detected after symptoms. Earlier diagnosis and detection of tumors that would not cause harm can affect this measure. No mortality comparison or quantified overdiagnosis estimate is supplied.

> Five-year survival for screen-detected cases is 92%, compared with 61% for cases found after symptoms. Screening works.

> Five-year survival after diagnosis is 92% for screen-detected cases and 61% for cases detected after symptoms. That comparison alone does not show that screening reduces deaths. Earlier diagnosis can lengthen measured survival without postponing death, and detecting tumors that would not cause harm can also raise the survival rate. Mortality and harms require separate evidence.

**A dose written dangerously**

**Supplied facts:** These are incomplete synthetic order fragments, not instructions to administer medication. The first drug is unnamed; the insulin formulation and route are missing; the last abbreviation is ambiguous and lacks dose, route and timing details. No authorized corrected order is supplied.

> Give 1.0 mg IV, U 10 insulin QD, MSO4 prn.

> Clarification required before these fragments can be used as medication instructions. Confirm each drug, dose, route and schedule against an authorized order; do not guess what "MSO4" means.

*Notation-only observations: an unnecessary trailing zero can be removed, and "units" and "daily" avoid the ambiguous abbreviations. Those edits do not complete the orders.*

**Person-first applied over a stated preference**

**Supplied facts:** Participants in this fictional interview record request the terms autistic people and Deaf people. They report barriers in services designed around hearing, non-autistic norms. No estimate of a whole community's preferences is supplied.

> Individuals with autism and individuals with deafness often report difficulties with services designed for individuals without those conditions.

> The autistic and Deaf participants interviewed for this piece said services designed around hearing, non-autistic norms did not fit them. This piece follows their requested identity-first language.

**Blame in the chart**

**Supplied facts:** The synthetic chart contains the labels below and a patient report of no alcohol use. It gives no insulin frequency, cost barrier, reason for the metformin label, treatment duration or HbA1c target.

> Patient is non-compliant with insulin and denies alcohol use. Failed metformin.

> Patient reports no alcohol use.

*Clarification required: document actual insulin use and relevant barriers rather than "non-compliant." Establish whether "failed metformin" means limited response, adverse effects or another issue. The source does not support adding a frequency, cost explanation or test result.*
