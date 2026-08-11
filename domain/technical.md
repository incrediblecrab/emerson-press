---
id: domain.technical
layer: domain
kind: functional
version: 2.0.0
status: draft
budget: 2310
tokens: 2310
mechanics: house
evidence_floor: 4
evidence:
  - sources/ai-slop-research.md
---

# Domain: Technical

Documentation, references, guides, READMEs, changelogs. Pairs with `citation/ieee.md` where formal citation is needed at all.

The reader is stuck. That is the defining condition of this domain and the source of most of its rules. Nobody arrives at a troubleshooting page out of curiosity. They came because something failed, they are already frustrated, they are working under a deadline they did not set, and they will read exactly as far as the fix. Every convention below follows from that: front-load the answer, state the prerequisites before the steps, never make the reader read past the thing they need.

It also explains the ban on minimizing language, which is the most-violated rule in the genre. *Simply run the migration.* *Just add the config flag.* *It's easy — obviously you'll want to set the environment variable first.* When those instructions work, the words are noise. When they fail — and the reader is on the page precisely because something failed — they have told someone already struggling that the thing defeating them is trivial. The sentence costs nothing to remove and it is the reason the reader closes the tab and files a support ticket instead.

The second structural failure is a mode error, and Diátaxis names it better than anything else in circulation. Four kinds of document do four incompatible jobs. A **tutorial** takes a beginner through a guaranteed success. A **how-to guide** helps a competent user complete one task. A **reference** describes the machinery exactly and completely. An **explanation** supplies the why. Each serves a different reader in a different state, and mixing two produces a document that fails both: the tutorial that stops to explain architecture loses the beginner, the reference that teaches becomes unscannable for the person who knew what they wanted and came to check an argument's default.

The third thing worth stating is the accuracy problem specific to this domain. A hallucinated method name is indistinguishable from a real one until someone runs it. Baltes and colleagues, studying how developers describe AI-assisted work, found the characteristic burden is not obviously bad output but output plausible enough to require full review — the cost moves from writing to verification. Technical documentation is where that cost lands hardest, because the reader cannot tell a real flag from an invented one and will spend an hour finding out.

## Detect

### Mode and structure

- Two Diátaxis modes in one document: a tutorial that pauses for architecture, a reference that walks the reader through a scenario, a how-to that starts by explaining the domain model.
- A guide with no stated outcome, so the reader cannot tell whether it is the right page.
- Prerequisites discovered at step 7. Versions, permissions, installed dependencies, and required state all belong before step 1.
- The answer below the background. Concept-first ordering serves the writer's understanding, not the reader's problem.
- Steps that skip the state change: *configure the service* where the reader needs the file, the key, and the value.
- A troubleshooting section listing symptoms with no causes, or causes with no fixes.

### Minimizing and register

- *Simply, just, easy, easily, obviously, of course, merely, straightforward, all you have to do, it's trivial to.*
- *Should* where the writer means *will*, or where it hides an untested step.
- First-person plural in instructions — *we'll now configure* — for a reader who is alone.
- Future tense throughout: *the command will create a file.* It creates a file.
- Jargon on first use with no definition, or a term used two ways in one page.
- Marketing register in documentation: *powerful*, *seamless*, *blazing fast*, *robust*, *enterprise-grade*.

### Accuracy

- An API surface that does not exist — an invented method, flag, option, or configuration key. The signature failure of this domain.
- Version-free claims. Behavior described with no statement of what it was tested against is an undated assertion.
- Code that will not run: missing imports, undeclared variables, `...` standing in for something the reader needs, a placeholder that looks like real credentials.
- Output claimed but not shown, or shown from a different version.
- Deprecated approaches presented as current, or a fix that stopped working two releases ago and nobody re-ran.
- A changelog written for the committer — *refactored the service layer*, *bumped deps*, *various fixes* — rather than for the person deciding whether to upgrade.

## Write

Put the answer first. Task pages open with the task. Reference entries open with what the thing is. Explanation is the one mode allowed to build, and it should say so at the top.

State prerequisites before the first step: version, permissions, installed tools, and the state the reader must already be in. Then steps that each change exactly one thing, in the imperative, in the present tense, second person.

Delete every minimizer. There is no case where *simply* improves an instruction. If a step really is short, its shortness will be visible.

Pin the version. *As of v4.2* converts a claim that rots silently into one that announces its own age. Where behavior changed, say which release changed it.

Ship code that runs. Complete imports, real values, the actual output, and a note on anything environment-specific. If it cannot be run as printed, mark what has to be substituted.

Write what you verified. Where a behavior is expected but untested, say so rather than promoting it to documentation, and never name an API you have not confirmed exists.

Name one thing one way. Pick the term, define it once, and use it everywhere, including in the code samples and the error strings.

Write the changelog for the reader deciding whether to upgrade: what broke, what changed, what they must do, and what is now deprecated and until when.

Document the failure modes. What goes wrong, what it looks like, what to do, and what to do when that does not work either.

## Mechanics

Mostly `core/formatting.md`, with a few things that belong to this domain.

- Code in fenced blocks with the language declared. Inline code for identifiers, paths, flags, and literal values — never for emphasis.
- Placeholders in one consistent form, marked as placeholders.
- Numbered lists for ordered steps, bullets for unordered sets. A numbered list whose order does not matter is a false claim about sequence.
- Commands and their output distinguished, so the reader knows what to type.
- Versions as versions: `4.2.0`, not *the latest release*.
- File paths, environment variables, and keys typed exactly, including case.
- Headings that name the task in the reader's words — the words they searched for, not the internal component name.
- Citation is rarely needed. Where a standard or a paper is referenced, `citation/ieee.md` governs; a link to the specification is usually better than a formal reference.

## Formats

### Reference

Complete, precise, scannable, and not read in order. Somebody arrived from a search result to check one parameter.

Every entry gets the same shape: what it is, its type, its default, its constraints, what it does, and what it interacts with. Consistency of structure is the feature — it lets a reader jump.

Completeness beats prose. An undocumented parameter is a bug in the reference. Do not teach here; link to the guide that teaches.

Mark deprecations with the version that deprecated them, the version that removes them, and the replacement.

### Guide

One task, one outcome, stated in the title. The reader is competent and is not here to learn the system.

Outcome first, prerequisites second, steps third, verification fourth. The verification step is the one most often missing and the one that decides whether the reader knows they succeeded.

No detours. Link to the explanation rather than including it. A guide that stops to justify its design choices has become a different document.

Finish with the failure cases and where to go next.

### README

The first thing anyone reads and usually the last thing anyone updates. It answers four questions fast: what this is, why it exists, how to run it, where to go next.

Open with a sentence a stranger can parse — what the thing does, for whom. Not the tagline.

Then installation that works from a clean machine, a minimal example that runs as printed, and links out to the reference and the guides.

Keep the status honest: what works, what does not, what is planned, what version this describes. A README that oversells is discovered within ten minutes and costs the project a contributor.

## Evidence

Rung 4 — the source is interrogated — with a property no other domain in this directory has: the primary source is executable. A claim about software can be checked by running it, which means interrogation is not a matter of judgment but of doing the thing.

That raises the standard rather than lowering it. Where a historian must weigh a source and a clinician must assess a trial, a technical writer can simply find out, so an unverified claim in this genre is a decision not to check. The version pin is what makes the verification durable: *tested against 4.2.0 on Linux* records what was interrogated and when it stops being evidence.

This is a floor, not a setting. Where the audience tier sits at a higher rung, the tier governs; where this floor is higher, it governs. Plain writing for a non-specialist is a change of register and never a lower standard of proof.

## Boundaries

Against `user-interface/`. A real boundary now that the layer exists. This module documents software; `user-interface/` writes the software's own words. Error message text belongs to `user-interface/applications.md`; the troubleshooting page that explains the error belongs here. Button labels are theirs; the guide that tells the reader which button belongs to this module.

Against `academia`. Both are precise and both cite, and they cite for opposite reasons. An academic citation situates a claim among peers. A technical reference points at a specification so the reader can go read the authority instead of trusting the page.

Against `marketing`. The most common contamination in the genre. Product documentation written by an organization that also sells the product drifts into promotional register — *powerful*, *seamless*, *enterprise-grade* — and every such word makes the document less useful to a reader who is stuck. Documentation states what the software does, including what it does badly.

Against `general`. Both are functional and share the front-loading discipline. `technical` adds the mode distinction, the version obligation, and the executable-source evidence standard. When the piece has no software in it, `general` governs.

With `audience/`. A reference is for `professional` at peer register; a getting-started guide is often `professional` at non-specialist register, and the tier changes the assumed vocabulary, not the accuracy. Writing down does not mean minimizing — plain language and *simply* are unrelated, and the second is the one to cut.

## Examples

**Minimizing a step the reader is stuck on**

> Simply run the migration script and you're done. It's straightforward.

> Run the migration:
>
> ```bash
> ./bin/migrate --config config/prod.yaml
> ```
>
> It takes about 20 minutes on a database of 10 million rows and holds a write lock the whole time. If it exits with `ERR_SCHEMA_DRIFT`, the schema was modified outside the migration system — see Recovering from schema drift.

**Two modes in one document**

> ## Getting Started
>
> Before we begin, it's worth understanding the architecture. The system uses an event-sourced model where state is derived from an append-only log. This design was chosen because...

> ## Getting started
>
> By the end of this page you will have the server running locally and will have created one record.
>
> **You need:** Node 20+, Postgres 14+, and a database you can write to.
>
> 1. Install the package...
>
> *Why the system stores events rather than state:* Architecture overview.

**Invented API surface**

> Call `client.autoRetry(true)` to enable automatic retries.

> There is no auto-retry setting. Wrap the call and retry on the transient error classes:
>
> ```python
> import time
>
>
> def fetch_with_retry(client, record_id, attempts=3):
>     for attempt in range(attempts):
>         try:
>             return client.fetch(record_id)
>         except (TimeoutError, ConnectionError):
>             if attempt == attempts - 1:
>                 raise
>             time.sleep(2**attempt)
> ```
>
> Verified against client 4.2.0.

**A version-free claim**

> The API returns results sorted by creation date.

> As of v4.2, `GET /records` returns results sorted by `created_at` descending. Before v4.0 the order was unspecified; do not rely on it if you support older servers.

**A changelog written for the committer**

> - Refactored the service layer - Bumped dependencies - Various bug fixes and improvements

> **Breaking.** `GET /records` now returns `created_at` as RFC 3339 with an offset instead of a Unix timestamp. Parsers expecting an integer will fail.
>
> **Fixed.** Imports of CSV files over 10 MB no longer time out.
>
> **Deprecated.** `client.legacy_fetch()` warns as of this release and is removed in 5.0.
