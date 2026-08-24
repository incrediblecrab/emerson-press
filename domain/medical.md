---
id: domain.medical
layer: domain
kind: regulated
version: 2.1.0
status: draft
budget: 2912
tokens: 2912
mechanics: ama
evidence_floor: 5
evidence:
  - sources/ap-stylebook.md
---

# Domain: Medical

Clinical documentation, research reporting, patient education, public guidance. Pairs with `citation/ama11.md`.

Overstated certainty is a safety defect here, not a stylistic one. In press, an overclaim damages credibility. In marketing, it draws a regulator. In medicine, someone stops a medication, or does not go to the emergency department, or agrees to a procedure they would have declined with the real numbers. The prose is part of the intervention, and it can hurt the reader the way a wrong dose can.

The most common way it happens is not a lie. It is a relative risk reported without its base. *Cuts your risk in half* is true of a drop from two in ten thousand to one in ten thousand, and it is the same sentence a writer would use for a drop from forty percent to twenty. Those two facts should not share a sentence, and the fix costs eleven words: give the absolute numbers, in natural frequencies, on a common denominator. Gigerenzer's research is unambiguous that clinicians and patients both reason better from *3 in 1,000* than from *0.3%* — and the finding holds for the clinicians, which is the part that should end the argument.

Person-first language — *a person with epilepsy* rather than *an epileptic* — was a genuine advance, and applying it blindly has become its own failure. Much of the autistic community prefers *autistic person*, and much of the Deaf community prefers *Deaf person*, on the ground that the trait is identity rather than affliction. The AMA manual acknowledges this. A style rule that hard-codes person-first everywhere writes over the stated preference of the people it claims to respect, which was the thing person-first language was invented to stop.

## Detect

### Certainty and causation

- Efficacy stated flatly: *this treatment works, X cures Y, safe and effective* with no population, no effect size, and no interval.
- Relative risk with no absolute baseline. The single most common numerical distortion in health writing.
- Causal verbs on observational data — *causes*, *prevents*, *leads to* — where the design supports only association.
- Statistical significance read as clinical importance. A p-value below .05 in a large trial can describe a difference no patient would notice.
- A single study framed as settled, or a preprint cited without noting that it has not been peer reviewed.
- Mechanism reported as outcome: the drug lowers the marker, therefore it helps the patient. Many do not.
- Surrogate endpoints substituted for the endpoint anyone cares about.
- Screening described by five-year survival, which rises from earlier detection alone. Lead time, length bias, and overdiagnosis all inflate it. Mortality is the honest number.
- Absent uncertainty. Confidence intervals dropped, limitations section missing, generalizability unstated.

### Safety mechanics

- ISMP error-prone forms: `QD` and `QOD`, `U` for units, `IU`, `MS` and `MSO4` and `MgSO4`, `cc`, `µg`, and drug-name abbreviations.
- A trailing zero — `1.0 mg`, read as ten — or a naked lead decimal — `.5 mg`, read as five. Both have killed people.
- Dose without route, frequency, or duration.
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

Give the absolute numbers. If a treatment moves an outcome from 2 in 1,000 to 1 in 1,000, write that, then give the relative figure if it helps. Keep the denominator constant across every comparison in the passage.

Report design before result. *In a randomized trial of 4,200 adults over 60 with prior cardiac events* is not throat-clearing; it is the boundary of the claim, and the reader needs it before the effect size, not after.

Attach the interval to the estimate, and say what the interval means: the range consistent with the data, not the range of possible truths.

Say *associated with* when the design supports association. The discipline costs nothing and it is the difference between reporting a study and overselling it.

Name the population the finding does not cover. Trials in adults do not transfer to children; trials in one ancestry group may not transfer; a six-month endpoint says nothing about year five.

Write *we do not know* when that is the state of the evidence, and say what would resolve it. Uncertainty stated plainly is more trustworthy than false confidence, and patients handle it better than the literature once assumed.

Follow the community's stated preference on identity. *Autistic person*, *Deaf person*, *person with diabetes*, *person with schizophrenia*. When writing about an individual, use theirs. When writing about a group whose preference is contested, say so once rather than picking silently.

Describe behavior without judging it. *Took the medication three days a week* rather than *non-compliant*. *Did not respond to treatment* rather than *failed treatment* — the treatment failed the patient, and the sentence should say so in that direction.

Give the patient the action and the threshold. What to do, how much, how often, for how long, and the specific signs that mean call now.

## Mechanics

AMA style, restated. `citation/ama11.md` carries the full form.

- Numbered citations in order of appearance, superscript, outside terminal punctuation.
- Superscript numerals are the manuscript form. Patient-facing and public-guidance text attributes in prose instead — name the study, the journal and the year in the sentence — because a superscript points at a reference list the reader will not be given.
- Journal titles abbreviated per the NLM Catalog. Up to six authors listed; beyond that, the first three and *et al.*
- Conventional units, with SI units in parentheses; give the conversion factor at first mention.
- A leading zero on every dose or measurement below one — 0.5 mg, never .5 mg — and never a trailing zero after a whole number. No leading zero on a statistic that cannot exceed 1: *P* = .04, not *P* = 0.04.
- Doses written out — units, not `U`; daily, not `QD`; micrograms as `mcg`.
- Generic drug names, with the brand in parentheses on first mention if it matters.
- Trial registration number and funding source disclosed. ICMJE authorship criteria checked against each name on the paper.
- The reporting guideline that matches the design, cited by version: CONSORT 2025 for trials, SPIRIT 2025 for trial protocols, PRISMA 2020 for systematic reviews, STROBE 2007 for observational studies. CONSORT 2025 replaced the 2010 statement in April 2025 and adds an open-science item, so a paper checked against the older list is checked against a superseded one.

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

Plain language, roughly eighth-grade reading level, and an eighth-grade reading level is not a simplification of the content — it is a translation of it. The numbers stay true. ISO 24495-3:2026 draws the line this section depends on: writing about a scientific subject for readers outside the field is its own task, with its own standards, and distinct from writing aimed at experts inside it.

Lead with what to do. Structure follows the reader's questions: what this is, what it means for me, what I do now, when I call someone.

One idea per paragraph, short sentences, no Latin, every retained term defined in the sentence that introduces it. Natural frequencies, common denominators, absolute numbers.

A plainer word is only a translation when it denotes the same thing. *High blood pressure* stands in for *hypertension* safely. *Heart attack* does not stand in for *cardiac arrest* — those are different events with different treatments, and swapping one for the other is a clinical error wearing the costume of plain language.

Name the red flags explicitly and separately, with a threshold and a destination. *Call 911 if the chest pain lasts more than a few minutes or comes with sweating or shortness of breath* — not *seek care if symptoms worsen*.

Say who this does not apply to, and send them somewhere.

### Public guidance

Health writing at population scale — guidance, campaign material, anything addressed to everyone.

The risk-number obligations bind hardest here, because the audience cannot ask a follow-up question and the material will be quoted out of context by someone who did not read the qualifier.

Give absolute risk. Say what changed and what did not when guidance is revised, because unexplained reversals cost more trust than the original error did. State the uncertainty rather than projecting a confidence that later evidence will embarrass.

Safe-messaging conventions apply to suicide and self-harm: no method detail, no presentation of a death as inevitable or as a solution, means-restriction framing, and resources in the piece.

## Evidence

Rung 5 for any clinical claim, tied with `legal` for the highest floor in this directory: uncertainty given a number — the interval on the estimate, the design that licenses it, and the population it covers. The sources that can carry that are a peer-reviewed study, a systematic review, or a guideline from a body that publishes its methodology. Preprints are labeled. Press releases about studies are not studies.

Rung 5 is also a floor rather than a ceiling here, because a study can be real, peer reviewed, correctly cited, and still not support the sentence built on it. Design, population, endpoint, and effect size all have to match the claim. The citation being valid is necessary and nowhere near sufficient.

The floor stands where the reader is a patient with no clinical training at all. A handout gets shorter sentences and the same interval, the same denominator, the same statement of who the finding does not cover. A `domain/education-level/` tier sets the words. Rung 5 sets what may be said with them.

## Boundaries

Against `press`. Health journalism sits in both. `press` owns attribution, structure, and the reporting craft; `medical` owns the numbers. When a story reports a study, the risk-communication rules here govern the paragraph that gives the result, and the ban on hyping a single paper survives any editor's appetite for a stronger headline.

Against `marketing`. The dangerous overlap. Pharmaceutical and device promotion, wellness copy, and health-adjacent product claims all pull toward marketing's register and are held to this module's evidence floor. Substantiation is not satisfied by a mechanism, a testimonial, or a study in mice.

Against `non-fiction`. Science writing, illness memoir and the history of a trial all sit here at book length, and all of them make claims a reader may act on. `non-fiction` governs the prose and this module governs every live claim inside it — the estimate, the denominator, the population the finding covers. A finding written for a journal and the same finding written for patients are different documents, not one document at two reading levels.

Against `legal`. Both are regulated and both treat overstatement as a professional failure rather than a stylistic one. The difference that matters at the boundary is the reader's next move: a client can ask a follow-up question inside a continuing relationship, while a patient may act on a handout alone. Where the two meet — informed consent, an adverse-event notice, a capacity assessment — `legal` owns what the document must contain and this module owns how the risk is stated.

With `domain/education-level/`. The default reader is an adult, and the split that matters — a colleague for the clinical note, a patient for the handout — is set by format rather than by tier. Load a tier when the reader is a student or a child, and it will shorten the sentences and simplify the words. It will not move the estimate. A handout that overstates certainty to sound reassuring has failed at the thing it was for.

## Examples

**Relative risk with no floor under it**

> The new drug cuts your risk of stroke in half.

> Among adults over 65 with atrial fibrillation, about 2 in 100 had a stroke each year on the older drug and about 1 in 100 on the new one. That is one stroke prevented for every 100 people treated for a year. Serious bleeding rose from about 1 in 200 to about 1 in 150.

**Association promoted to cause**

> Coffee prevents liver disease.

> In a UK Biobank cohort of 494,585 adults followed for a median of about 11 years, coffee drinkers had a lower rate of chronic liver disease than non-drinkers (Kennedy et al., *BMC Public Health*, 2021). The study was observational and cannot establish cause; coffee drinkers differed from non-drinkers in ways the analysis could only partly adjust for.

**Screening measured by the flattering number**

> Five-year survival for screen-detected cases is 92%, compared with 61% for cases found after symptoms. Screening works.

> Screening finds cancers earlier, which lengthens the interval between diagnosis and death whether or not it postpones the death. It also finds tumors that would never have caused harm. Both effects raise five-year survival without saving anyone. The trials that tracked deaths found the screened group's breast-cancer mortality about 20% lower (Marmot et al., *Lancet*, 2012). How much overdiagnosis comes with that benefit is genuinely contested: the same panel put it near 3 overdiagnosed cancers per death prevented, the Cochrane review closer to 10, and the 2024 USPSTF modeling closer to 2. Give the range and name the source rather than picking the flattering end.

**A dose written dangerously**

> Give 1.0 mg IV, U 10 insulin QD, MSO4 prn.

> Give 1 mg intravenously. Give 10 units of insulin daily. Give morphine sulfate as needed — dose, route, and interval specified.

**Person-first applied over a stated preference**

> Individuals with autism and individuals with deafness often report difficulties with services designed for individuals without those conditions.

> Autistic people and Deaf people often report that services designed around hearing, non-autistic norms do not fit them. Both communities largely prefer identity-first language; this piece follows that preference.

**Blame in the chart**

> Patient is non-compliant with insulin and denies alcohol use. Failed metformin.

> Patient reports taking insulin about three days a week and describes the cost as the main barrier. Reports no alcohol use. Metformin did not bring HbA1c below target after four months.
