---
id: sources.kill-ai-slop
layer: sources
version: 1.2.0
status: active
budget: none
evidence_kind: practitioner
checked_on: 2026-09-08
verification_status: historical
source_version: "35-tell catalog and scanner as described in the 2026-08-09 dossier; repository commit and site revision not recorded"
source_urls:
  - https://github.com/yetone/kill-ai-slop
  - https://killaislop.com/
verification_note: "The retained practitioner catalog was reassessed, not freshly checked out or executed. Pattern matches do not validate authorship, usability, accessibility or prompt efficacy. Coverage and tell IDs are historical; Apache-2.0 attribution is retained."
source:
  title: "kill-ai-slop"
  subtitle: "A field guide to the visual and copy tics of AI-generated products."
  author: "yetone"
  publisher: "GitHub / killaislop.com"
  year: 2026
  extent: "35 tells; SKILL.md, taxonomy.md, detection.md, fixes.md, scan.mjs"
  license: "Apache-2.0"
  url: "https://github.com/yetone/kill-ai-slop"
  retrieved: 2026-08-09
consumers:
  - core/formatting.md
  - core/restraint.md
  - domain/marketing.md
  - user-interface/accessibility.md
  - user-interface/applications.md
  - user-interface/charts.md
  - user-interface/website.md
---

# Source: kill-ai-slop

A practitioner catalog of interface and marketing defaults, including text near controls and product claims. It supplies review questions for those surfaces, not empirical authority for all interface writing or accessibility requirements.

Unbudgeted by design. Read when authoring or revising a `user-interface/` module.

This dossier restates the catalog in original wording. Flagged phrases appear as flagged phrases, because the phrase is the finding. The taxonomy's numbering appears as-is because the tell ids are identifiers that the scanner's `--only=` flag takes.

## Why This Source

Three useful features of the recorded artifact.

**It addresses product surfaces.** Landing pages, labels, stat rows and badges have different tasks from a continuous essay. A short label still needs meaning, and a product statistic still needs verifiable support.

**It includes a scanner.** The historical account describes `scan.mjs` matching source-code patterns and reporting `file:line`. Such a match can establish the presence of a pattern under the scanner's definition, not that AI produced it or that it is a usability defect. The scanner was not executed in this refresh.

**It includes triage before editing.** The recorded workflow asks whether a flagged choice is intentional and useful. That is compatible with `core/restraint.md`; it is not an independent experiment validating this repository, and independence between practitioner sources has not been established.

### The repurposing caveat

The retained examples are chiefly visual: color ramps, radii, shadows, spinner centering and typeface selection. `emerson-press` writes words. Three consequences.

- **Take the copy tells and the framing; leave the CSS.** Tells 13, 14, 15, 23, 29, and 30 are about text. The rest are cited here only where the *mechanism* transfers.
- **It emphasizes marketing surfaces** — hero sections, feature grids and landing pages. This record does not establish guidance for all the tasks of a settings screen or permission dialog.
- **It challenges unexamined defaults.** This can motivate asking what a choice communicates. It is an editorial framing, not a measurable definition of all low-quality AI output.

## The Six Principles

Principles recorded from `SKILL.md`, restated as practitioner preferences rather than universal design requirements:

1. Decide before you decorate. Every choice must be explainable.
2. One accent, one voice.
3. Hierarchy comes from scale and space. Coloring words is a shortcut.
4. Subtract first.
5. Specific beats punchy.
6. Decoration must mean something. An icon, a badge, a callout is a signal.

Principle 5 resembles the field-guide essay's preference for specificity and the house approach in `core/voice.md`. Repetition across sources does not establish independent empirical support. Use specificity when it makes a supported claim or action clearer.

Principle 6 suggests a useful question: what will a reader infer from a badge or callout, and is that inference justified? The magnitude of any trust effect is not measured by this catalog.

## The Copy Tells

### Tell 14 — the AI copywriting voice

The centerpiece, and the tell this project's `user-interface/website.md` is built against. The named surface forms:

- `It's not just X — it's Y` — a contrast worth checking for substance, not a validated strongest tell. Other checklists naming it does not increase its empirical authority.
- `Say goodbye to X`
- `Meet your new X`
- `Supercharge your X`
- `Unlock the power of X`
- `In seconds, not [longer unit]`
- `blazing fast`, `effortless`, `seamless`, `game-changer`, `next-level`
- **`X theater`** — dismissing a practice through a label rather than explaining its deficiency. The label can also express a legitimate critique; check the argument instead of prohibiting the phrase.
- Punchy three-word triads set as whole paragraphs: `Fast. Beautiful. Yours.`
- The em-dash habit, and specifically em-dash triplets.

The useful diagnosis is enthusiasm or symmetry without a concrete claim. A real contrast, accurate performance statement or appropriate brand voice should not fail merely for sharing one of these forms.

Prefer a supported description of what the product does and what changes for the user. A measured opening time or memory figure may help, but never invent a statistic to make a generic claim sound specific.

### Tell 13 — highlighted keywords

Check whether coloring or bolding words communicates useful hierarchy. Color can create a mistaken expectation of a link, depending on the interface. This is a design review question, not an independently measured universal effect or a ban on emphasis.

### Tell 15 — emoji everywhere

Repeated decorative emoji can distract from a label's task. A separate **house accessibility check** is whether the actual markup exposes emoji names to assistive technology and makes a control harder to understand. Behavior depends on markup, platform and assistive technology; this catalog does not establish a normative accessibility rule or a universal announcement behavior.

### Tell 23 — badge and pill spam

`✨ New`, `β Beta`, `🔥 Popular` used as decoration rather than status. Diagnosis: manufacturing fake buzz. Fix: a badge only for real status. The generalized rule for `user-interface/` — a status word must be falsifiable. If nothing changes when it stops being true, it was decoration.

### Tell 29 — the invented stat row

An impressive-looking usage, uptime or support figure needs support. Real numbers need not be odd or precise-looking. Verify the source, time window, denominator and scope before publishing a claim; make estimates and service commitments distinguishable from measurements.

This applies the house accuracy principle to an interface. The catalog does not quantify how one false number changes trust in adjacent true ones.

### Tell 30 — the 01/02/03 section markers

Giant ordinals may imply a sequence or ranking that the content does not have. Keep numbering for a real order, reference system or navigational purpose; do not manufacture a sequence merely to decorate unrelated feature sections.

### Tells 10 and 11 — the kicker and the display sentence

A tiny tracked-caps label above every heading that restates the heading, and a whole marketing sentence set at display size. Both are the same failure — size and ornament standing in for the decision about what matters. The copy consequence: if the kicker restates the heading, one of them is empty.

### Tell 28 — the all-caps card grid

Interchangeable cards with a shouted label and a number, faking structure while stuffing unrelated things into identical boxes. The text version of `core/formatting.md`'s two-row table.

## Where It Is Thin

- **Coverage is limited.** The retained catalog chiefly addresses marketing and visual defaults; it does not establish comprehensive guidance for settings, errors, forms or notifications.
- **It is not an accessibility standard.** Check actual behavior and applicable authoritative guidance separately.
- **Tell 14 bundles different questions.** Voice, register, specificity, rhythm and punctuation share an identifier; that arrangement is not evidence that they have one cause or one remedy.
- **The claims are practitioner judgments.** The scanner can locate patterns; it does not validate their badness, detector accuracy or the efficacy of a prompt.

## What `emerson-press` Takes

1. **Question unexamined defaults.** A house framing for assessing what a choice communicates, not a universal definition or an inference about who made it.
2. **Triage before edit.** A compatible practitioner workflow, not independent empirical confirmation of `core/restraint.md`.
3. **Decoration as signal** — a review question for status words, badges and other elements that invite a factual inference.
4. **Verification of product statistics**, without treating precise-looking figures as inherently credible.
5. **Named marketing constructions** — `say goodbye to`, `meet your new`, `supercharge`, `unlock the power of`, `seamless`, `effortless`, `X theater` — split between `user-interface/website.md`, which permits selling, and `user-interface/applications.md`, which does not.
6. **Check what numbering means** — sequence, rank or reference — and retain it when it serves that purpose.

## What `emerson-press` Refuses

The visual catalog is outside this writing system's scope, and neither its copy examples nor its scanner matches become automatic prohibitions. The historical account distinguishes `stop-slop`'s categorical em-dash ban from this catalog's concern with habitual use. Preserve the contextual judgment without claiming that this comparison proves either prompt effective.
