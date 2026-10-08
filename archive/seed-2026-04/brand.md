# Brand

## Who this is for

Jo - CBAHI accreditation consultant. Works across four primary health-care centers distributed over roughly 1,500 km, reporting into a Saudi Ministry survey deadline (October 2026). Lives in bilingual (Arabic / English) documents that have to look as considered on a director's desk as on a minister's.

## Voice

Calm and specific. The work this system supports has real stakes - accreditation scores, survey findings, staff roster decisions - and the design language should feel like a careful colleague, not a cheerful mascot.

Prefer the concrete noun over the abstract one. "Chapter LD" beats "this area." "63 of 72 standards scored" beats "making good progress."

Warm, not cloying. Warm grays instead of cool ones. A gold accent on a chapter tile. Noto Naskh Arabic set at a generous line-height because it was designed to breathe.

No exclamation points in data UI. The user is looking at percentages; they do not need the interface to be excited on their behalf.

No emoji in shipped strings unless the user's message had one first. In conversational agent responses, the same default applies.

## Tone by surface

- **Dashboard headers:** factual. `Self-assessment · Center A · 570 standards` - not `Welcome to your dashboard!`
- **Empty states:** instructive. `No survey in progress. Start one from the History tab.` - not `Nothing here yet!`
- **Confirmation dialogs:** neutral. `Clear the current scoring?` - not `Are you sure? This cannot be undone!`
- **Error states:** diagnostic. `Could not reach Firestore. Last synced 4 minutes ago.` - not `Oops, something went wrong.`
- **Success states:** minimal. A checkmark and a timestamp. Not a toast with a sparkle.

## Visual tone

Glass over gradient, not glass over glass. Thin progress bars that imply quantity without shouting. Neutral body copy with color reserved for identity (chapter strokes, score columns). One signal per axis.

Print-ready at all times. Every screen should also make sense as a static PDF export because half of this work ends up on a director's desk in a binder.

## What this brand isn't

It is not a dashboard style. It is not a SaaS aesthetic. It is not gradient-first (gradients are a specific tool, used specifically). It is not dark-mode-ready (no one has asked; the healthcare audience uses bright rooms and laptops on desks).

It is not "AI-themed." Don't name buttons with "AI" in them. The tool is the outcome, not the mechanism.

## One-liner

*A quiet, bilingual instrument panel for people whose work gets audited.*

## If you had to write a product description

*Jo's design system is the set of visual and interaction decisions that survived twenty revisions of a CBAHI accreditation dashboard. It is small, dependency-free, and opinionated about the things that matter - progress bars, Arabic rendering, the shape of dropdowns - and deliberately silent about the things that don't. Drop it into any project that will eventually produce a PDF for a minister.*
