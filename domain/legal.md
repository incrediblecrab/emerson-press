---
id: domain.legal
layer: domain
kind: regulated
version: 2.1.0
status: draft
budget: 2621
tokens: 2621
mechanics: bluebook
evidence_floor: 5
---

# Domain: Legal

Memos, briefs, contracts, client letters. Pairs with `citation/bluebook22.md`.

Hedging here is the product. That single fact separates this domain from every other module in the repository, and `core/voice.md`'s instruction to commit has to be read against it. When a lawyer writes *the court would likely hold*, the word *likely* is not a failure of nerve or a rhetorical softener. It is the answer. The client is buying a probability estimate, and a confident answer to an uncertain question is not better writing — it is malpractice with good prose style.

So the rule this module applies is not *hedge less*. It is *hedge with content*. A useless hedge names no fact and no threshold: *it is possible that issues may arise*. A useful one is a conditional with the condition supplied: *probably unenforceable, unless the lease was recorded before March, in which case the priority rule reverses*. The first is evasion. The second is the work.

Legal citation is not a bibliography. It is an argument about authority. A case is binding or persuasive depending on which court and which jurisdiction; a proposition is holding or dictum; a source is good law or was overruled last year. Bluebook signals encode the writer's own confidence in the inferential distance between the cited authority and the sentence it supports. That system is the hardest thing in this domain for a model to fake, because choosing the right signal requires having read the case rather than having seen it cited.

## Detect

### Substance

- Outcome stated as certain: *we will win, the court will hold, this is clearly unenforceable.*
- A hedge with no condition attached, naming no fact that would change the answer.
- Advice untethered from the facts and the jurisdiction it depends on.
- The bad cases missing from a memo. A predictive document that only found helpful authority did not predict anything.
- Counsel that answers a different, easier question than the one asked.
- A recommendation with no next step, no deadline, and no named actor.

### Authority

- A case cited past its holding, or a quotation lifted from dicta and used as though it were the rule.
- Authority not validated for subsequent history — reversed, vacated, superseded, abrogated, or overruled.
- A persuasive court cited as though binding, or no forum identified at all.
- A citation with no pincite behind a specific proposition.
- Signals used interchangeably: `see` where the proposition is stated directly, no signal where the support requires an inferential step, `cf.` as a general-purpose gesture.
- A string cite standing in for an argument.
- Secondary authority cited where primary authority exists and is on point.

### Drafting and register

- Legalese where a plain word works: *hereinafter, aforementioned, pursuant to, said party, witnesseth, the instant case.*
- Doublets and triplets carried by habit — *null and void*, *give, devise and bequeath* — where one word carries the meaning. Some pairs are genuine terms of art; most are scribal inheritance, and the test is whether removing one word changes an outcome.
- Obligations with no obligor: *reasonable efforts shall be made.*
- *And/or.* It is ambiguous, courts have said so repeatedly, and the fix is to write the three cases out.
- An effort standard nobody defined — *reasonable efforts*, *best efforts*, *commercially reasonable* — in an agreement that will be read by people who disagree about what it meant.
- A defined term used two ways, defined and never used, or capitalized without being defined at all.
- A client letter written in a judge's register.
- A question presented that is not a question, or that assumes its own answer.

## Write

Answer first. *Probably not*, then the reason, then what it turns on. The brief answer is the part the client reads, and burying it below the facts section serves the writer's sense of order rather than the reader's need.

Make each hedge do work. Name the fact, the threshold, or the open question that would move the estimate, and say how it could be resolved. *We do not know whether the fund cleared $10 million before December 31; the year-end statement settles it* converts uncertainty into a task.

State the jurisdiction and the standard of review before arguing. An argument that does not say which law governs and how much deference applies is not yet an argument.

Cite for what the court actually held, at the page where it held it. Validate every authority for subsequent history before it goes in a document that leaves the building.

Choose the signal deliberately. No signal means the source states the proposition. `See` means the source supports it through an inferential step you expect the reader to make. `Cf.` means analogous but not on all fours. `But see` and `contra` do the same work in the other direction. Using them precisely is how a reader calibrates trust in the rest of the brief.

Put the adverse authority in. In a memo it goes in because the client is paying for a prediction and a prediction built only on helpful cases is worth nothing. In a brief it goes in because Model Rule 3.3(a)(2) forbids knowingly failing to disclose legal authority in the controlling jurisdiction that you know to be directly adverse and that opposing counsel has not disclosed — and because they will cite it anyway and you would rather characterize it first.

Draft obligations as active sentences with a named actor, a verb, and a date. Define every standard of effort or delete the phrase. Prefer *must* to *shall* in new drafting; *shall* has been read as both mandatory and merely predictive often enough that its ambiguity is documented.

Write the client letter to the client. Plain language, no Latin, every retained term of art defined once, and a closing that says what the client does next and by when.

## Mechanics

Bluebook, restated. `citation/bluebook22.md` carries the full form.

- Full citation on first reference, short form after, `id.` only for the source immediately preceding with no intervening authority.
- Pincites on anything specific. A case citation without a pincite asserts that the whole opinion supports the sentence.
- Case names italicized in text; the reporter, the court and the year in the parenthetical, with the court dropped where the reporter alone identifies it: `N.Y. Times Co. v. Sullivan, 376 U.S. 254, 279-80 (1964)` names no court because `U.S.` can only be the Supreme Court, while a circuit or state decision must say which one.
- Signals ordered and punctuated as the system requires, with a parenthetical explaining any citation whose relevance is not obvious from the proposition.
- Subsequent history appended where it affects validity.
- Quotations of fifty words or more set as blocks without quotation marks; alterations bracketed and omissions marked, because a misquoted authority is a misrepresentation to the court rather than a typo.
- Defined terms capitalized consistently and used only as defined.
- Citation sentences and citation clauses punctuated as sentences and clauses, which is what distinguishes legal citation from every other system in `citation/`.

## Formats

### Memo

Predictive. Question presented, brief answer, facts, discussion, conclusion.

Write the question presented so it contains the governing law, the legal question, and the two or three facts that will decide it. The brief answer commits to a probability and gives the reason in a sentence.

The discussion runs rule, application, conclusion for each issue, in that order, with the rule synthesized from the authority rather than recited case by case. A discussion that walks through four cases in sequence has not yet extracted a rule.

Candor is the genre's obligation. Model Rule 2.1 asks for independent judgment and candid advice, and a memo that tells a partner or a client what they want to hear has failed at the only thing it was for.

### Brief

Persuasive, and adversarial in a system that expects it. Lead with the strongest ground rather than the most chronological one. State the standard of review early, because it often decides the case.

Frame the facts truthfully and favorably — those are compatible, and the skill of the genre lies in the gap between them. Answer the other side's best argument in its own terms rather than a weakened restatement.

Rule 3.3 governs. You disclose directly adverse controlling authority you know of, unless the other side already has. You also correct yourself, once you learn that a material statement of fact or law you made to the court was false.

### Client letter

Plain language for a reader who is not a lawyer and is probably worried. No Latin, no citations in the body, every necessary term defined once in ordinary words. ISO 24495-2:2025 sets guidelines for legal communication across the legal, governmental, non-governmental and health sectors, and states the purpose plainly: the reader has to understand the document well enough to exercise a right or meet an obligation. That is the standard the client letter is held to, not the writer's comfort.

Say what the situation is, what it means for them, what you recommend, what it will cost, and what happens next. End with the action, the owner, and the date. The jargon shield is the failure mode here: technical language deployed to avoid delivering bad news plainly.

### Contract

Drafted to be read by a hostile reader years later, when everyone who negotiated it has left. Every obligation gets an actor, a verb, and a deadline. Every defined term is defined once, capitalized consistently, and used nowhere else in a different sense.

Write the ambiguity out. Replace `and/or` with the enumerated cases. Give every effort standard a definition or a metric. Say what happens on breach, on delay, and on termination, because those are the clauses that get litigated and the ones drafted with the least attention.

## Evidence

Rung 5 — uncertainty stated to the precision the evidence allows, which in law is a calibrated verbal probability with its contingency named rather than an interval — plus a requirement no other domain in this directory carries: authority must be checked for continued validity before use. Elsewhere a source is either sound or unsound when written and stays that way. In law a proposition that was correct last term can be overruled this one, and citing it is an error that no amount of care at drafting time prevents.

The signal system is the second addition. Where other citation styles record only that a source was consulted, Bluebook signals record the writer's assessment of how far the source is from the claim. That makes legal citation the only system in `citation/` where the form itself carries an epistemic judgment, and the only one where getting the form right requires having read the source.

Plainer words for a client with no legal training, and the same estimate underneath them. The pincite, the subsequent-history check and the calibration of the hedge are not register, so no tier on the ladder reaches them.

## Boundaries

Against `core/voice.md`. Direct conflict, resolved in this module's favor by precedence. `voice` says commit; legal writing commits to a probability, and stripping the qualifiers changes the meaning of the advice rather than tightening it. `core/restraint.md` states the general principle: a flagged construction that is doing work stays.

Against `non-fiction`. Both cite densely, and the citations do different jobs. A note in a history tells the reader where a fact came from so they can go and check it. A legal citation asserts that an institution with power over the reader has already decided something, and its form encodes how much power. Legal history and biography of the bench are `non-fiction`; anything a client or a court will act on is this.

Against `medical`. The nearest neighbor in this directory. Both are regulated, both treat overstatement as a professional failure rather than a stylistic one, and both write simultaneously for a specialist and a lay reader. The difference is that medical writing's lay reader may act on it alone, while a client letter sits inside a continuing relationship in which questions can be asked.

With `domain/education-level/`. Load none of it and the reader is an adult: a judge for the brief, the client for the letter, and the formats above already set the distance between them. Reach for a tier only when the reader is genuinely at a schooling level — teaching material for a legal-studies class, a clinic letter to a client still in high school. Plain language changes the words. The estimate stays where the authority put it.

## Examples

*Raimonde v. Van Vlerah* is a real Ohio decision, cited accurately. *Ruiz v. Marchetti Software* and *Alvarez v. Sentinel Mut.* are invented, reporter cites and all, because an example of a case pushed past its holding needs a holding the reader cannot go and check. Nothing invented here may leave this page.

**Certainty a lawyer cannot sell**

> You will win this case. The non-compete is clearly unenforceable.

> The non-compete is probably enforceable in narrowed form. Ohio courts do not void an overbroad restraint; under *Raimonde v. Van Vlerah*, 42 Ohio St. 2d 21 (1975), they reform it to what is reasonably necessary to protect the employer's legitimate interest, weighing hardship to the employee and injury to the public. A three-year, North-America-wide restraint with no customer limitation will very likely be cut back — plausibly to the states where she actually sold, and to a year — and enforced as cut. What would change that is evidence that the overbreadth was deliberate, or that reformation would require rewriting rather than trimming. The confidentiality clause is narrower, severable under the agreement's own terms, and likely to survive intact.

**Hedge that says nothing**

> It is possible that the arrangement may potentially raise certain issues that could warrant further consideration.

> The arrangement probably triggers the disclosure requirement. It turns on whether the fund cleared $10 million in assets before December 31. The year-end statement resolves it, and I can tell you within a day of receiving it.

**Legalese for its own sake**

> Pursuant to the aforementioned agreement, Lessee shall hereinafter be obligated to remit payment on or before the first day of each calendar month.

> The tenant pays rent by the first of each month.

**Obligation with nobody in it**

> Reasonable efforts shall be made to complete the migration in a timely manner.

> Vendor must complete the migration by June 30, 2027. Vendor must dedicate at least two full-time engineers to it. If completion slips more than 14 days, Customer may terminate without penalty and Vendor must refund fees paid for the unstarted phases.

**A case pushed past its holding**

> Courts have held that click-through agreements are unenforceable. *Ruiz v. Marchetti Software*, 512 F.3d 44 (6th Cir. 2008).

> *Ruiz* declined to enforce a click-through agreement where the terms sat behind an unlabeled hyperlink below the fold. 512 F.3d 44, 51 (6th Cir. 2008). It did not reach agreements whose terms appear on the page itself, *see id.* at 53 n.7, and two later panels enforced those. Our facts are the second kind.

**Signal used carelessly**

> Contracts of adhesion are unenforceable in this circuit. *See* *Ruiz*, 512 F.3d at 51.

> Adhesion alone does not void a contract in this circuit; unconscionability requires both procedural and substantive elements. *Ruiz*, 512 F.3d at 51. *But see* *Alvarez v. Sentinel Mut.*, 604 F.3d 112, 119 (6th Cir. 2010) (suggesting in dicta that extreme procedural unfairness may suffice).
