---
id: user-interface.applications
layer: user-interface
version: 1.0.1
status: draft
budget: 1715
tokens: 1715
kind: medium
medium: app
mechanics: house
elements: [label, button, form field, error, alert, permission prompt, empty state, progress, onboarding, notification, setting]
evidence:
  - sources/apple-hig.md
  - sources/kill-ai-slop.md
  - sources/stop-slop.md
---

# Interface: Applications

Text inside a product someone is using to get something done. The reader did not open the app to read, and every word is a toll on the way to what they came for.

Platform-neutral house rules. For Apple platforms, load `user-interface/apple-hig.md` as well; it wins on mechanics.

## Detect

- **Marketing voice on a working surface.** *Say goodbye to, meet your new, supercharge, unlock the power of, seamless, effortless, blazing fast.* A landing page may sell. A settings screen may not.
- **Enthusiasm the moment does not contain.** *Awesome! You're all set!* on the completion of a chore.
- **The reader in the third person** — *the user can*, *players are able to* — or `we` doing the reader's work.
- Apology inflation: *Oops, uh-oh, sorry about that.* A joke on a surface the reader crosses every day.
- **Synonym churn.** *Delete*, *Remove*, *Trash*, and *Discard* for one action. *Workspace*, *team*, and *organization* for one container.
- Internal vocabulary escaping: *entity, tenant, endpoint, payload, job.*
- Widget names in guiding copy: *dismiss the modal*, *the button in the popover.* Platform verb mismatch: *click* on a phone.
- `(s)` and slashes standing in for a plural the writer would not choose.
- Register drift between surfaces — jokes in the empty state, legalese in the error, marketing in a settings footer.
- Text that describes the product instead of the reader's situation.

## Write

Address the person: *you*, *your*. Keep *we* for the company doing something the reader needs to know about, and use it rarely. Present tense, active voice, the reader as subject.

One voice, many tones. Tone belongs to the situation, not the brand: a failed payment and a finished workout do not sound alike.

Say the specific thing. *Opens in under a second* survives translation, truncation, and a skeptical reader. *Blazing fast* survives none of them.

One name per thing and one verb per action, decided once and written down. Use the reader's noun, not the schema's — they have *files*, not *objects*. Name the thing, never the control.

Define a term the first time it appears on a screen, because the reader did not necessarily arrive from the previous one.

Do not apologize for something the reader has not been told about yet. Say what happened first.

Write about people first and disability second, unless the community has said otherwise — `domain/medical.md` holds that exception and it survives this layer. Never borrow the name of a condition to label something bad.

## Surfaces

**Labels and actions.** Name the result, verb first, in one or two words. Reserve `OK` for an alert that informs and offers no choice; anywhere there is a decision, the button carries the verb from the title. `Cancel` is the word for abandoning an action, and it is never the default. Hold one capitalization convention per element type. No terminal period. A trailing ellipsis means more input is needed before anything happens. A menu command that flips a state is named for the action it will perform — *Turn HDR Off* when HDR is on. A badge is a status claim; delete it if the interface looks identical once the claim expires.

**Forms.** Every field gets a persistent label; the placeholder shows format (`name@example.com`), never the question. State the requirement before the attempt, not in an error after it. Validate when the answer is complete. Write the fix, not the fault, beside the field. Accept what the reader types and normalize it yourself. Mark the smaller set — if most fields are required, mark the optional ones. Prefill what you know; never prefill a password.

**Errors.** Three jobs: what happened, what it means here, what to do next. Lead in the past tense and in the reader's terms. Name what was kept and what was lost. Give the next action as a button, or say who can fix it and roughly when. Keep the code, after the sentence. No blame, no stack trace, no *Something went wrong*. An error many readers will hit is not a copy problem.

**Alerts and permissions.** Interrupt only for a decision, or for loss that is unexpected and irreversible. Title the consequence, not the question: *Delete 14 photos?* Add one line only if it carries a fact the title cannot. Do not confirm an expected, undoable action. Style an action as destructive when the loss is the surprise, not when it is the point. Ask for a permission where the feature is used, and say what the reader gets for it.

**Empty states.** Four different screens: nothing yet, nothing matching, nothing left, nothing available. Write only the one you are in. *Nothing yet* names what will appear and gives the action that makes it appear. *Nothing matching* echoes the query and the active filters and offers the widening move. *Nothing left* is a plain confirmation. *Nothing available* is a failure — write it as an error. Put nothing permanent on a screen designed to disappear.

**Status and progress.** Name the object and the stage. *Loading*, *Please wait*, and *Authenticating* are true of every wait and informative about none. Give a proportion only when you can track it honestly, and prefer counts — *4 of 12 files*. Change the button while its action runs. Offer `Cancel`, and `Pause` as well when stopping would throw away work. When a process stalls, replace the status with what happened. Distinguish offline from failed. Confirm silently where the result is already visible.

**Onboarding.** Get the reader to one real result, then stop. Teach by letting them do the thing, undoably, on their own data. Ship defaults so setup is optional. Defer every permission to the moment it is needed. Keep a tip to a sentence or two, with the action at the front. Explain your own product's ideas, not the platform's. Make the tour skippable and findable afterwards.

**Notifications.** The notification is the message, not a pointer to it. Title in a few words; body as one complete sentence, left for the system to truncate. Name the actor and the object as the reader would. Assume someone else can see the preview. One notification per event. Choose the interruption level for the reader's stake, not yours; a promotion is opt-in and never urgent. Badge only what is waiting for a decision. Errors go where the reader can act, not here.

**Settings.** Label the effect, not the mechanism. A switch is named, not commanded: phrase it so that on means more of the thing named — *Notifications*, not *Disable notifications*, and not *Turn Notifications Off*, which is a menu command's shape. Write a footer only when it adds a consequence the label cannot carry, and describe the on state. Group by the reader's goal; a section called *Advanced* means the settings in it need better names. Do not restate a system setting or ask for what you can detect. Link to a setting rather than describing where it lives. Say what a setting will not do, when readers reliably expect it to.

## Boundaries

Product surfaces, whatever the platform: a native app, a desktop client, or the logged-in half of a website. The visitor-facing half is `website.md`. Register stays with the genre module, and with whatever `domain/education-level/` tier loads beside it — a children's app keeps its warmth, a peer tool keeps its terms of art. What this module strips is unearned enthusiasm, not earned tone.

Long-form product writing — release notes, help articles, in-app guides — is `domain/technical.md`. Email and other messages that arrive outside the product are neither this module nor `website.md`; use `domain/` until this axis claims them. Conversational surfaces — an assistant's replies, a chat agent's refusals — are not covered here either: they are read rather than scanned, so the attention economy this module assumes does not hold.

## Examples

**Onboarding that tours instead of starting**

> Welcome to Kestrel! Let's take a quick tour of everything you can do. &nbsp; (1 of 7)

> Write your first note. &nbsp; Anything here can be undone. &nbsp; [ Skip ]

**An alert that hides the decision**

> Are you sure? &nbsp; [ Cancel ] [ OK ]

> Delete 14 photos? &nbsp; They'll be removed from all your devices. You can restore them from Recently Deleted for 30 days. &nbsp; [ Cancel ] [ Delete ]

**Requirement revealed by failure**

> Password [ •••••••• ] ⚠ Invalid password.

> Password At least 12 characters, including a number. [ •••••••••••• ]

**Loss unaccounted for**

> Sync failed.

> Sync stopped after 40 of 212 notes. The 40 are up to date on your other devices; the rest are still only on this one. &nbsp; [ Retry ]

**One message for four empty states**

> No data.

> No invoices yet. Invoices appear here after a client pays. &nbsp; [ Create your first invoice ]

**Vague status**

> Loading…

> Loading 212 notes from iCloud. About 20 seconds.

**A notification that points instead of tells**

> Kestrel: You have a new notification. Open the app to view it.

> Dana Osei approved your access request &nbsp; Editor on "Q3 forecast," requested Tuesday.

**Setting named for its mechanism**

> Enable background fetch daemon

> Update in the background Kestrel checks for new notes while it's closed. Uses more battery.

**Synonym churn**

> Menu: *Remove.* Confirmation: *Delete this file?* Button: *Discard.* Toast: *Moved to Trash.*

> Menu: *Delete.* Confirmation: *Delete this file?* Button: *Delete.* Toast: *File deleted.*
