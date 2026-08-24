---
id: user-interface.website
layer: user-interface
version: 1.0.1
status: draft
budget: 1378
tokens: 1378
kind: medium
medium: web
mechanics: house
elements: [landing page, heading, navigation, page title, link text, form, 404, consent banner, documentation]
evidence:
  - sources/kill-ai-slop.md
  - sources/stop-slop.md
  - sources/apple-hig.md
  - sources/field-guide-to-ai-slop.md
---

# Interface: Website

Pages a stranger arrives at, usually sideways, usually from a search result, usually to answer one question. Unlike an application, a website is allowed to sell, and that permission is why generated slop clusters here. The register of every other landing page is the path of least resistance, and copy written in it persuades without making one checkable claim.

Everything here assumes a reader who has not signed in. Product surfaces behind a login are `user-interface/applications.md`, browser or not.

## Detect

- **The claim that fits any product.** Swap in a competitor's name and nothing breaks. *The modern way to X.* *Built for teams that move fast.*
- **The named marketing constructions.** *It's not just X — it's Y. Say goodbye to X. Meet your new X. Supercharge your X. Unlock the power of X. In seconds, not hours.* *Seamless, effortless, blazing fast, game-changing, next-level.*
- Dismissal as a tic: *no more standup theater*, *X, reimagined.*
- **Punchy triads set as a paragraph.** *Fast. Beautiful. Yours.*
- **The invented stat row.** *10k+ developers, 99.9% uptime, 24/7 support* on a product that launched last month. Genuine figures come out lopsided and precise, and a single fabricated one discredits every honest number sharing the row.
- **A kicker above each heading, restating it**, and a full marketing sentence typeset at display size.
- Ordinals — *01, 02, 03* — over sections that have no order.
- **Badge and pill spam.** *✨ New*, *🔥 Popular*, *β Beta* as decoration. Emoji as bullet markers and heading ornaments.
- Keywords bolded or colored mid-paragraph, which is indistinguishable from a link.
- Feature grids of interchangeable cards, each with an icon that relates to nothing.
- **Throat-clearing.** *Here's the thing. In today's fast-paced world. The truth is.*
- Testimonials with no name, role, or company. Logos of companies that are customers of a customer.
- **`Learn more` four times on one page**, pointing at four destinations.
- A 404 that apologizes and offers only the home page.
- A consent banner where *Accept All* is a button and *Reject* is a link in a submenu, or one that describes the reader's rights in language written to be skipped.
- Docs that explain the platform rather than the product, or that open with what the product is *not*.
- Text set inside an image, which is invisible to search, translation, and speech.

## Write

Say what the thing is in the first sentence, in the words the reader would search for. A stranger should be able to answer *what is this and is it for me* without scrolling.

Replace every unfalsifiable claim with a number, a noun, or a consequence. If you cannot measure it, describe the mechanism instead. The page has to leave somewhere for a number to go; whether that number is substantiated, and how long the substantiation lasts, is `domain/marketing.md` and its rule governs.

Label every figure on the page with what it counts and as of when, so a stat row cannot show a bare number.

Let hierarchy come from what matters, not from size. If a kicker restates its heading, one of them is empty; delete that one.

Number only genuinely ordered things — install steps, a changelog, a migration. A feature grid has no order and numbering it makes a false claim.

Write link text that stands alone, because assistive technology and search engines both read it out of context.

Name the person in a testimonial, with role and company, or cut it. Attribution and material-connection disclosure themselves are `domain/marketing.md`'s call; on this page, give a quote the same visual weight as the claim it supports rather than setting it as decoration.

Keep the page in one voice. Marketing register stops at the product boundary: the pricing page may sell, the billing settings screen may not.

Put text in text. Write for the reader first and the crawler never.

## Surfaces

**Landing page.** One claim, one action. Lead with the specific thing the product does, then the evidence for it, then the ask. Cut any sentence that survives having the product's name swapped out.

**Navigation and page titles.** Name destinations, not concepts. *Pricing*, *Docs*, *Changelog* — not *Solutions*, *Resources*, *Platform*. A title tag is the page's name plus the site's, in that order, and it is read out of context in a result list.

**Forms.** Ask for the fewest fields that let you do the next thing. Label every field persistently, state requirements before the attempt, and say what happens after submission — who replies, and roughly when. Write a validation message as the fix rather than the fault, beside the field it belongs to: *Enter an address in the form name@example.com*, not *Invalid input*.

**Error pages.** A 404 says the page is gone and offers the two or three places the reader probably wanted, plus search. A 500 says the failure is ours and whether to retry. Neither needs a joke or an illustration of a lost astronaut.

**Consent and legal.** State plainly what is collected, why, and who else gets it. Give accept and reject equal weight and equal reach. Write the summary so that reading only the summary is not a trap.

**Documentation.** Open with what the thing does and the smallest working example. Task-ordered, one outcome per page. Version anything that changes. Do not explain the language, the shell, or the platform — link to them.

## Boundaries

Pages a visitor reaches without being logged in, plus the public documentation. Anything behind the sign-in — settings, dashboards, the product itself — is `applications.md`, even though it is reached by a URL and rendered in a browser. The seam is what the reader has committed to, not the technology.

Marketing claims themselves — what may be asserted, whether it is substantiated, how a testimonial is attributed — are `domain/marketing.md`, in every medium. This module governs the page: hero, kicker, badge, stat row, display type, navigation, link text and the surface conventions that go with them. A tell listed in both places is listed once as a page convention and once as a claim about the world; where they meet, the substantiation floor is not negotiable by layout.

## Examples

**A claim that fits any product**

> The modern platform for teams that move fast. Seamless, effortless, built for scale.

> Kestrel turns email threads into notes. Forward one to notes@kestrel.app and it appears in your workspace within a few seconds.

**Negative parallelism plus a triad**

> It's not just a code editor — it's a movement. Fast. Beautiful. Yours.

> A code editor. Opens in under a second, on about half the memory of the Electron ones.

**The invented stat row**

> 10k+ developers &nbsp; 99.9% uptime &nbsp; 24/7 support

> 1,840 accounts as of July 2026 &nbsp; 99.7% uptime over the last 90 days (status page) &nbsp; Support replies weekdays, usually within four hours

**Kicker restating its heading**

> PLATFORM ## Our Platform

> ## Import from Jira in one pass

**Navigation named for the company, not the visitor**

> Solutions &nbsp; Platform &nbsp; Resources &nbsp; Why Kestrel

> Pricing &nbsp; Docs &nbsp; Changelog &nbsp; Customers

**A 404 that only apologizes**

> Oops! 🚀 Looks like you're lost in space! &nbsp; [ Go home ]

> That page doesn't exist. It may have moved when we reorganized the docs in June. &nbsp; [ Search docs ] [ Changelog ] [ API reference ]

**A consent banner written to be skipped**

> We value your privacy. We and our 847 partners use cookies to enhance your experience. &nbsp; [ Accept All ] &nbsp; *Manage preferences*

> We use cookies to keep you signed in, and analytics to see which docs pages get read. Analytics data goes to Plausible. Nothing is sold. &nbsp; [ Accept ] [ Reject ]

**Documentation that starts anywhere but the point**

> Welcome to the Kestrel documentation! In today's fast-paced development landscape, managing notes has never been more crucial.

> Kestrel's API creates and updates notes. Every request needs a bearer token.
>
> ```bash
> curl -H "Authorization: Bearer $TOKEN" https://api.kestrel.app/v1/notes
> ```
