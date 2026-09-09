---
id: domain.technical
layer: domain
kind: functional
version: 2.2.0
status: draft
budget: 2162
tokens: 2162
mechanics: house
evidence_floor: 4
evidence:
  - sources/ai-slop-research.md
---

# Domain: Technical

Documentation, references, guides, READMEs, changelogs. Pairs with `citation/ieee.md` where formal citation is needed at all.

The reader may be troubleshooting, learning, looking up a parameter or evaluating a design. Match that task rather than assuming everyone is stuck or frustrated. Put prerequisites before consequential steps and make the needed answer easy to find.

Minimizing language can hide prerequisites or dismiss real difficulty: *simply run the migration* is not a substitute for permissions, backup and downtime information. Review its effect rather than banning every occurrence of *just* or *simply*, including meaningful technical terms.

Diátaxis offers a useful distinction among a learning-oriented **tutorial**, task-oriented **how-to**, descriptive **reference** and understanding-oriented **explanation**. Choose a primary purpose and separate unrelated detours. Brief explanations and examples can still support a task; neither a guaranteed outcome nor a universal ban on mixed material follows.

Plausible examples can still invent an API, omit a prerequisite or conceal a side effect. Check authoritative documentation and, when authorized and safe, actual behavior. Qualitative reports about review burden are not proof that every generated example fails or that this prompt improves it.

## Detect

### Mode and structure

- Material that frustrates the page's primary purpose, such as an unrelated architecture essay before the first tutorial step.
- A guide with no stated outcome, so the reader cannot tell whether it is the right page.
- Prerequisites discovered at step 7. Versions, permissions, installed dependencies, and required state all belong before step 1.
- A task answer buried below unnecessary background, or an explanation stripped of the context needed to understand it.
- Steps that skip the state change: *configure the service* where the reader needs the file, the key, and the value.
- A troubleshooting section listing symptoms with no causes, or causes with no fixes.

### Minimizing and register

- Minimizers that dismiss difficulty or hide requirements. A literal term such as *simply connected* is not a defect.
- *Should* where the writer means *will*, or where it hides an untested step.
- Person or tense that obscures who performs an action or whether it was actually tested. A deliberate tutorial voice is not automatically wrong.
- Jargon on first use with no definition, or a term used two ways in one page.
- Marketing register in documentation: *powerful*, *seamless*, *blazing fast*, *robust*, *enterprise-grade*.

### Accuracy

- An API surface that does not exist — an invented method, flag, option, or configuration key. The signature failure of this domain.
- Version-sensitive claims lacking a documented scope. Do not label a documented expectation as a test result.
- Code that will not run: missing imports, undeclared variables, `...` standing in for something the reader needs, a placeholder that looks like real credentials.
- Output claimed but not shown, or shown from a different version.
- Deprecated approaches presented as current, or a fix that stopped working two releases ago and nobody re-ran.
- A changelog written for the committer — *refactored the service layer*, *bumped deps*, *various fixes* — rather than for the person deciding whether to upgrade.

## Write

Put the answer first. Task pages open with the task. Reference entries open with what the thing is. Explanation is the one mode allowed to build, and it should say so at the top.

State relevant versions, permissions, tools and initial state before the steps. Make ordered actions and their consequences clear. Keep safety prerequisites before the action; do not bury a write lock, deletion or production effect afterward.

Remove a minimizer when it contributes no useful meaning or understates difficulty. Preserve literal identifiers, quotations and meaningful technical language.

Pin the version. *As of v4.2* converts a claim that rots silently into one that announces its own age. Where behavior changed, say which release changed it.

Provide complete, supported examples where the task needs runnable code. Mark placeholders, environment assumptions and illustrative output. Do not use real credentials or present a partial outline as a tested recipe.

Distinguish observed behavior, a cited specification and an untested expectation. Do not assert that an API exists or does not exist without a basis. Missing documentation is a verification need, not permission to invent an alternative implementation.

Execute examples only with authorization in a suitable environment. A production migration is not a harmless validation command. If a check would be unsafe, unavailable or costly, state the limit rather than claim it ran.

Name one thing one way. Pick the term, define it once, and use it everywhere, including in the code samples and the error strings.

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
- Use source links or formal citations as the task and venue require. Select `citation/ieee.md` only when IEEE style is requested; technical subject matter does not choose it automatically.

## Formats

### Reference

Complete, precise, scannable, and not read in order. Somebody arrived from a search result to check one parameter.

Every entry gets the same shape: what it is, its type, its default, its constraints, what it does, and what it interacts with. Consistency of structure is the feature — it lets a reader jump.

Completeness beats prose. An undocumented parameter is a bug in the reference. Do not teach here; link to the guide that teaches.

Mark known deprecation and removal versions and a supported replacement. If removal is unscheduled, say so rather than inventing a release.

### Guide

One task, one outcome, stated in the title. The reader is competent and is not here to learn the system.

Outcome first, prerequisites second, steps third, verification fourth. The verification step is the one most often missing and the one that decides whether the reader knows they succeeded.

Link to substantial explanations rather than interrupting the task with an unrelated essay. Retain a concise rationale or warning when it helps the reader make the correct choice.

Finish with the failure cases and where to go next.

### README

The first thing anyone reads and usually the last thing anyone updates. It answers four questions fast: what this is, why it exists, how to run it, where to go next.

Open with a sentence a stranger can parse — what the thing does, for whom. Not the tagline.

Then installation that works from a clean machine, a minimal example that runs as printed, and links out to the reference and the guides.

Keep the status honest: what works, what does not, what is planned, what version this describes. A README that oversells is discovered within ten minutes and costs the project a contributor.

### Changelog

Terse, versioned, and read in reverse. Somebody arrived with a working system to find out what upgrading will cost them, which makes this the one format here read adversarially — the reader is hunting for a reason not to proceed.

Put breaking changes first and label them breaking. Every entry answers what broke, what changed, what the reader must do, and what is now deprecated and until when.

Write the consequence, not the work. *Refactored the service layer*, *bumped deps* and *various fixes* are notes to the committer, and they leave the reader with nothing to decide on.

Assume the reader is several versions behind. They read entries in a run rather than one at a time, so each entry names its version and stands without the three above it.

## Evidence

The legacy `evidence_floor: 4` emphasizes examining the relevant implementation, documentation or observed behavior. Execution can test a claim, but it does not eliminate judgment about versions, environment, coverage or side effects.

Some behavior cannot safely or practically be tested in the available setting. Record the real check and its scope, and disclose what remains unverified. A version pin does not prove a test occurred or make one environment representative of every deployment.

A beginner's getting-started page is checked against the same running system as a maintainer's reference. Simplify the vocabulary as far down the ladder as the reader needs; a version number does not simplify, and a command nobody ran does not become true for a novice.

## Boundaries

Against `user-interface/`. A real boundary now that the layer exists. This module documents software; `user-interface/` writes the software's own words. Error message text belongs to `user-interface/applications.md`; the troubleshooting page that explains the error belongs here. Button labels are theirs; the guide that tells the reader which button belongs to this module.

Against `non-fiction`. Choose by task rather than page count or the mere presence of an argument. Technical books, architectural explanations and decision records can belong here; narrative histories of a system may fit nonfiction.

Against `marketing`. The most common contamination in the genre. Product documentation written by an organization that also sells the product drifts into promotional register — *powerful*, *seamless*, *enterprise-grade* — and every such word makes the document less useful to a reader who is stuck. Documentation states what the software does, including what it does badly.

Against `general`. Both are functional and share the front-loading discipline. `technical` adds the mode distinction, the version obligation, and the executable-source evidence standard. When the piece has no software in it, `general` governs.

With `domain/education-level/`. Describe the actual reader's familiarity and support needs. Use classroom presets for classroom tasks, not as labels for every novice, expert or person with a degree. Clear beginner instruction keeps the same accuracy and safety standard.

## Examples

These are independent synthetic documentation records. Commands describe a hypothetical product; supplied test reports are not tests performed by the assistant.

**Minimizing a step the reader is stuck on**

**Supplied facts:** The reviewed migration command below targets a disposable staging database and holds a write lock while it runs. It requires a backup and an authorized maintenance window. The team's supplied test used 10 million rows and took about 20 minutes; other sizes are unmeasured. ERR_SCHEMA_DRIFT means a schema change outside the migration system, and a recovery guide with that title is available.

> Simply run the migration script and you're done. It's straightforward.

> Back up the database and arrange an authorized maintenance window: the migration holds a write lock. First run the reviewed command against the disposable staging database:
>
> ```bash
> ./bin/migrate --config config/staging.yaml
> ```
>
> The team's recorded test took about 20 minutes on 10 million rows; that is not a duration guarantee. If it exits with `ERR_SCHEMA_DRIFT`, see Recovering from schema drift.

**Two modes in one document**

**Supplied facts:** The task is to reorganize a tutorial outline, not supply verified commands. Its intended outcome is a local server and one disposable record. The supplied prerequisites are Node 22+, Postgres 16+ and an empty local database with write access. An Architecture overview exists; installation and startup commands have not been supplied or run.

> ## Getting Started
>
> Before we begin, it's worth understanding the architecture. The system uses an event-sourced model where state is derived from an append-only log. This design was chosen because...

> ## Getting started
>
> This tutorial is intended to guide you through running the server locally and creating one disposable record.
>
> **You need:** Node 22+, Postgres 16+ and an empty local database with write access.
>
> *Outline only: installation, startup and record-creation steps still need verified commands.*
>
> *Why the system stores events rather than state:* Architecture overview.

**Invented API surface**

**Supplied facts:** No SDK version, API reference or execution record is supplied. Neither the existence nor absence of an autoRetry method has been established, and no retry/error-handling contract is known.

> Call `client.autoRetry(true)` to enable automatic retries.

> Verify the supported retry API for the chosen SDK version before publishing this instruction. The supplied material does not establish whether `client.autoRetry(true)` exists, what errors are retryable or whether repeating the operation is safe.

**A version-free claim**

**Supplied facts:** The supplied API documentation for version 4.2.0 states that GET /records sorts by created_at descending. It says ordering before version 4.0.0 was unspecified. No execution is claimed.

> The API returns results sorted by creation date.

> As documented for v4.2.0, `GET /records` returns results sorted by `created_at` descending. Before v4.0.0 the order was unspecified; do not rely on it for those older servers.

**A changelog written for the committer**

**Supplied facts:** Release 4.3.0 changes created_at from a Unix timestamp to RFC 3339 with an offset. The team fixed a CSV-import timeout threshold at 10 MB and verified a 12 MB file; arbitrary file sizes were not tested. legacy_fetch starts warning in 4.3.0 and its removal in 5.0 is the supplied approved plan.

> - Refactored the service layer - Bumped dependencies - Various bug fixes and improvements

> **4.3.0 — Breaking.** `GET /records` now returns `created_at` as RFC 3339 with an offset instead of a Unix timestamp. Parsers expecting an integer will fail.
>
> **Fixed.** CSV imports no longer hit the former 10 MB timeout threshold. The team verified a 12 MB file.
>
> **Deprecated.** `client.legacy_fetch()` warns in 4.3.0 and is scheduled for removal in 5.0.
