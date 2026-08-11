---
id: user-interface.apple-hig
layer: user-interface
version: 1.0.0
status: draft
budget: 1228
tokens: 1228
kind: overlay
medium: apple
mechanics: hig
elements: [button, menu item, alert, notification, setting, purpose string]
evidence:
  - sources/apple-hig.md
---

# Interface: Apple HIG

Apple's conventions are mostly arbitrary and entirely load-bearing. Title case on a button is a coin flip that landed decades ago; a trailing ellipsis is a promise the reader has learned to read. The difference matters, because breaking an arbitrary convention makes an app look foreign, while breaking a load-bearing one makes it lie.

Overrides `user-interface/applications.md` on mechanics — casing, terminal punctuation, ellipsis, the default button's position, and the standard element vocabulary — and on nothing else. What an alert may interrupt for, when to ask a permission, and what a setting is called stay with `applications`. Everything above it in the stack still applies.

## Mechanics

**Capitalization.** Title case: buttons, menu items and menu titles, view and window titles, labels, segmented controls, pop-up menu items, tab and toolbar item labels. Sentence case: alert body text, help text, field hints, notification bodies, settings footers, and everything longer than a label. Title case capitalizes the first and last word, and every word between except articles, coordinating conjunctions, and prepositions of four letters or fewer.

An alert title takes whichever case its shape calls for. A fragment or a short question is title case with no period — `Delete Draft?`. A title written as a complete sentence is sentence case and takes terminal punctuation — `Your subscription expired on 3 August.`

**Terminal punctuation.** No period on a button, menu item, label, or fragment title. Periods go in body text, and in anything written as a complete sentence, including a title.

**Ellipsis.** A trailing ellipsis means the command needs more input before anything happens — `Save As…`, `Print…`, `Export…`. A command that acts immediately never takes one, even if a sheet appears to report progress. `Delete` deletes; `Delete…` would mean you get asked what.

**Ampersand.** Spelled *and* in body text; `&` only where space is tight and the convention is already established in that element.

## Detect

- Sentence case on a button, title case in an alert body.
- **A period on a button**, or on an alert title written as a fragment.
- **Case chosen by element rather than by shape** in an alert title: a fragment set in sentence case, a full sentence set in title case.
- An ellipsis on a command that acts immediately, or a missing ellipsis on one that opens a dialog to collect input.
- **`OK` on a button that acts.** `OK` means *I have read this* on an alert that offers no choice. Where there is a decision, the button carries the verb.
- `Cancel` used for anything other than abandoning the action, or made the default, or paired with a `Cancel`/`Don't Cancel` question.
- **`Yes` and `No` as button labels**, which forces the reader back to the title to find out what they are agreeing to.
- The default button in the leading position, or on the destructive action.
- **Platform-wrong verbs**: *click* on iOS, *tap* on macOS, *press* for a pointer.
- Explaining Apple's own conventions — how a gesture works, what a share sheet is — which the reader learned from the system, not from you.
- A notification title that repeats the app name the system already shows.
- **Apple's proper nouns renamed or miscapitalized**: *Apple id*, *touch ID*, *the home screen*, *iCloud drive*.

## Write

Use Apple's terms for Apple's things — *Sign in with Apple*, *iCloud Drive*, *Face ID*, *the Home Screen* — capitalized as Apple capitalizes them, and use your own terms for yours.

Prefer *turn on* and *turn off* to *enable* and *disable*, *choose* for an option and *select* for an object, *sign in* rather than *log in*.

Write once for every platform: *choose*, not *click* or *tap*, unless the gesture itself is the instruction.

Write for translation. Short sentences, no idiom, no puns, no words that carry the layout — *below*, *to the left* — because the layout flips in Arabic and the string grows by a third in German.

## Surfaces

**Alerts.** Case the title by its shape, body in sentence case. Buttons are one or two words, title case, no period, carrying the verb from the title. Put the default in the trailing position — the right in a left-to-right language, the left where the layout mirrors — and never on the destructive action. `Cancel` always accompanies a destructive action. What an alert may interrupt for is `applications`.

**Purpose strings.** Apple shows your sentence inside the system's own prompt, so write one sentence in sentence case naming the feature and the data it uses. When to ask is `applications`.

**Notifications.** Title in a few words, body as one complete sentence in sentence case. Never repeat the app name; the system already shows it.

**Settings.** Footers in sentence case, describing the on state. What a setting is called, and how it is grouped, is `applications`.

## Boundaries

Follow the mechanics on Apple platforms. Do not carry them onto the web or onto Android, where title case on a button reads as an import.

This module changes how Apple's standard elements are written, never what they are for. Behavior — when to interrupt, when to ask, what to name a thing — stays with `user-interface/applications.md` even on Apple platforms. Apple's conventions also say little about empty states, chart text, marketing pages, or long-form product writing; for those, `applications.md`, `website.md`, and `charts.md` hold, and `core/` holds under all of them.

## Examples

**Ellipsis on a command that acts**

> Delete… &nbsp; Print &nbsp; Save As

> Delete &nbsp; Print… &nbsp; Save As…

**`Yes`/`No` on a decision**

> Are you sure you want to discard this draft? &nbsp; [ No ] [ Yes ]

> Discard Draft? &nbsp; You can't undo this. &nbsp; [ Cancel ] [ Discard ]

**Default button on the destructive action**

> Move 40 items to the Trash? &nbsp; [ **Move to Trash** ] [ Cancel ]

> Move 40 Items to the Trash? &nbsp; [ Cancel ] [ **Move to Trash** ]

**Alert with no decision in it**

> Success! Your file has been saved successfully. &nbsp; [ OK ]

*Delete the alert. The saved file is the confirmation.*

**Purpose string that describes the system, not the reader**

> This app would like to access your location.

> Kestrel tags each note with the place you wrote it. Everything works without it; you'd type the place yourself.

**Alert title cased by element instead of by shape**

> your subscription expired on 3 august. &nbsp; [ OK ]

> Your subscription expired on 3 August. &nbsp; [ Not Now ] [ **Renew** ]

**A platform verb and a word that carries the layout**

> Tap the blue button below to dismiss this modal.

> Choose Continue.

**Notification repeating the app name**

> Kestrel &nbsp; Kestrel: New comment on your note

> Dana Osei commented on "Q3 forecast" "Can you check the March number before Friday?"
