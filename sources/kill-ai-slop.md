---
id: sources.kill-ai-slop
layer: sources
version: 1.0.0
status: active
budget: none
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
  - user-interface/website.md
  - user-interface/applications.md
  - user-interface/charts.md
  - user-interface/accessibility.md
  - core/formatting.md
  - core/restraint.md
  - domain/marketing.md
---

# Source: kill-ai-slop

The only source in this directory about *interfaces*. Everything else here studies prose — a page, an essay, an article — read start to finish by someone who chose to read it. This one studies text that appears on a screen next to a button, in a product the reader is trying to use for something else.

Unbudgeted by design. Read when authoring or revising a `user-interface/` module.

Restated in original wording. Flagged phrases are reproduced as flagged phrases. The taxonomy's numbering is cited as-is because the tell ids are identifiers that the scanner's `--only=` flag takes.

## Why This Source

Three things it has that no prose source does.

**It is about the surface `user-interface/` covers.** A landing page, a button label, a stat row, a badge. Prose sources have nothing to say about a four-word label, because a four-word label has no rhythm, no paragraph shape, and no place to put a citation.

**It ships a working detector.** `scan.mjs` is a dependency-free Node scanner that greps real source for the code-level signature of each tell and reports `file:line`. That means its claims are falsifiable in a way a prose checklist is not: you can run it against a shipped product and count. A tell that never fires on real code is a tell somebody imagined.

**It builds triage into the workflow.** The skill's third step separates slop from intentional before anything is changed, on the stated grounds that a gradient, a serif, or an emoji can be a real defended choice. That step is `core/restraint.md`, arrived at independently and applied to a codebase. It is the strongest external corroboration this project has that the restraint module is load-bearing rather than decorative.

### The repurposing caveat

The catalog is roughly four-fifths visual: color ramps, radii, shadows, spinner centering, typeface selection. `emerson-press` writes words. Three consequences.

- **Take the copy tells and the framing; leave the CSS.** Tells 13, 14, 15, 23, 29, and 30 are about text. The rest are cited here only where the *mechanism* transfers.
- **It targets marketing surfaces hardest** — hero sections, feature grids, landing pages. That maps onto `domain/marketing.md` more than onto a settings screen. The failure modes of a permission dialog are not in this source.
- **Its enemy is the default, not the flourish.** The stated definition of slop is what a machine reaches for when it has no taste but wants to look impressive. That is a narrower and better target than "AI wrote it," and it is the definition `user-interface/` adopts.

## The Six Principles

Stated in `SKILL.md` and held on every fix. Restated:

1. Decide before you decorate. Every choice must be explainable.
2. One accent, one voice.
3. Hierarchy comes from scale and space. Coloring words is a shortcut.
4. Subtract first.
5. Specific beats punchy.
6. Decoration must mean something. An icon, a badge, a callout is a signal.

Principle 5 is the same claim `sources/field-guide-to-ai-slop.md` reaches by a different road — cultivate specificity — and the same one `core/voice.md` is built on. Three independent sources converging on it is the reason it sits at the top of `core/` rather than inside a domain module.

Principle 6 is the one this source adds. In prose, an unearned flourish costs attention. In an interface, an unearned badge costs *trust*, because the reader has learned that a badge means something and this one does not.

## The Copy Tells

### Tell 14 — the AI copywriting voice

The centerpiece, and the tell this project's `user-interface/website.md` is built against. The named surface forms:

- `It's not just X — it's Y` — the binary contrast, already carried by `core/anti-slop.md` as negative parallelism. Worth noting that the two most popular anti-slop tools in circulation independently name this construction as the single strongest tell.
- `Say goodbye to X`
- `Meet your new X`
- `Supercharge your X`
- `Unlock the power of X`
- `In seconds, not [longer unit]`
- `blazing fast`, `effortless`, `seamless`, `game-changer`, `next-level`
- **`X theater`** — dismissing a practice as *security theater*, *standup theater*, *process theater*. Called out as a recurring generated-copy tic. This one appears in no prose source and is worth carrying.
- Punchy three-word triads set as whole paragraphs: `Fast. Beautiful. Yours.`
- The em-dash habit, and specifically em-dash triplets.

The diagnosis given is the useful part: symmetrical, one notch too excited, specifics-free. Not any single phrase — the rhythmic fingerprint.

The stated fix: real numbers, real nouns, real consequences, said the way one person explains something to another. The worked patch replaces `It's not just an editor — it's a movement. Say goodbye to friction.` with an opening time and a memory figure.

### Tell 13 — highlighted keywords

Coloring or bolding scattered words mid-paragraph. Stated reason: when every word is emphasized, none is. This is `core/formatting.md`'s bold-spam entry, independently observed, and the interface version is worse because a colored word inside body text is indistinguishable from a link.

### Tell 15 — emoji everywhere

A rocket on launch, a lightning bolt on fast, a lock on secure, on every heading, button, and bullet. Named as borrowed warmth standing in for a tone the words should have carried. The interface-specific cost, which prose sources miss: a screen reader announces the emoji name aloud, so decorative emoji in a label become spoken noise. That consequence belongs to `user-interface/accessibility.md`.

### Tell 23 — badge and pill spam

`✨ New`, `β Beta`, `🔥 Popular` used as decoration rather than status. Diagnosis: manufacturing fake buzz. Fix: a badge only for real status. The generalized rule for `user-interface/` — a status word must be falsifiable. If nothing changes when it stops being true, it was decoration.

### Tell 29 — the invented stat row

`10k+ developers, 99.9% uptime, 24/7 support` on a product that launched yesterday. The best line in the taxonomy, restated: real numbers are odd and specific, and one invented figure poisons every true one beside it. Fix: show a number only if you measured it, and say where it came from.

This is `core/accuracy.md` in an interface, and the poisoning claim is the part `core/accuracy.md` does not currently make.

### Tell 30 — the 01/02/03 section markers

Giant faint ordinals beside every marketing section. The argument is about meaning rather than taste: numbering is a claim that these things happen in this order, and feature sections have no order. Number install steps and changelogs; do not number a grid.

### Tells 10 and 11 — the kicker and the display sentence

A tiny tracked-caps label above every heading that restates the heading, and a whole marketing sentence set at display size. Both are the same failure — size and ornament standing in for the decision about what matters. The copy consequence: if the kicker restates the heading, one of them is empty.

### Tell 28 — the all-caps card grid

Interchangeable cards with a shouted label and a number, faking structure while stuffing unrelated things into identical boxes. The text version of `core/formatting.md`'s two-row table.

## Where It Is Thin

- **No settings, no errors, no forms, no notifications.** The catalog stops at the marketing surface. Everything a person uses after signing up is outside it, and that gap is most of `user-interface/`.
- **No accessibility axis.** Emoji, gradient text, and icon-only buttons all have screen-reader consequences that the taxonomy does not mention.
- **Tell 14 is one entry doing the work of a dozen.** Voice, register, specificity, rhythm, and punctuation are collapsed into a single id because the scanner needs one regex family per id. That is a tool constraint, not a finding.
- **Self-referential where the other sources are cited.** The strongest passages are assertions of taste, well argued and unsourced. The scanner makes the *presence* of a pattern checkable; it does not make the pattern bad.

## What `emerson-press` Takes

1. **Slop defined as the default rather than as the machine.** What gets reached for when no decision was made. This is the framing `user-interface/` uses throughout, and it is why the axis flags a generic label rather than a long one.
2. **Triage before edit.** Independent confirmation of `core/restraint.md`, from a project that had to build it or drown in false positives.
3. **Principle 6, decoration as signal** — the source of the falsifiable-status and badge rules in `user-interface/applications.md`, and of the whole detection list in `user-interface/website.md`.
4. **The invented stat row**, including the poisoning argument.
5. **Named marketing constructions** — `say goodbye to`, `meet your new`, `supercharge`, `unlock the power of`, `seamless`, `effortless`, `X theater` — split between `user-interface/website.md`, which is where selling is allowed, and `user-interface/applications.md`, which is where it is not.
6. **Ordinals as an ordering claim**, which generalizes past marketing into any numbered interface list.

## What `emerson-press` Refuses

The visual catalog, which is out of scope, and the em-dash entry, for the reason given in `sources/stop-slop.md`. Note the divergence between the two repositories here: `stop-slop` bans the em dash outright, while this source flags only the *habit* and the *triplet*. On this one point, `kill-ai-slop` is closer to the evidence, and closer to `core/restraint.md`.
