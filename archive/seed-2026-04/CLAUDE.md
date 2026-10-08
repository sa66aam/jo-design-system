# CLAUDE.md - guidance for Claude sessions reading this repo

> **Lessons (2026-09-07):** the cross-project `LESSONS.md` has ONE home: `/Users/jo/Claude co-work/Projects/LESSONS.md`. The `LESSONS.md` copies inside projects are byte-identical mirrors written by `Projects/_sync-lessons.sh`; never write a lesson into a mirror. New lesson = append to the master with the next number (last: 333), then run the sync script.

This file is an instruction surface for future Claude sessions that encounter this design system. If you're a Claude picking up a new project that links this repo (directly or through Claude Design), read this before proposing any visual decisions.

## Who this serves

Jo - a CBAHI accreditation consultant and the person Claude has been collaborating with across ~20 revisions of a bilingual healthcare dashboard and four document-generation skills. Jo is not a software engineer. Explain trade-offs in plain terms. Flag risks rather than assuming fluency.

## The load-bearing commitments

1. **Em-dashes (U+2014) are banned in shipped user-facing text.** Use hyphens or middle dots or rewrite. This rule is in `principles/failure-modes.md`. Do not suspend it for "this one looks better."

2. **Sync over async in the UI layer.** Async belongs at persistence boundaries, not scattered through components. This is a code-shape rule, not a design rule, but it shapes how loading states are designed (skeletons, not spinners on every keystroke).

3. **Arabic is first-class, not a localization afterthought.** Every rendered surface needs to look as considered in Arabic as in English. See `principles/arabic-rtl.md` for the specifics - the short version is: Noto Naskh Arabic exclusively, pair `dir` with font family, export Arabic PDFs via canvas→PNG when the pipeline is Chromium.

4. **The readiness bar is the load-bearing primitive.** Thin (4px), wide tonal span (amber-900 to amber-400), used anywhere a quantitative axis needs to be felt without the bar stealing focus. The three-variable knob (thickness × contrast × span) is documented in `principles/visual-language.md`.

5. **Make the requested change. Do not "while I'm here."** If you spot adjacent issues, name them separately and ask. The history of this codebase has multiple rounds of rework that started as a single-line request and grew into a refactor that needed to be unwound.

## Before editing tokens

`tokens/tokens.css` is the source of truth. `tokens/tokens.json` is a mirror, regenerate it after any CSS edit. The two files are kept in lockstep by hand - there is no build script yet.

If you're tempted to "modernize" the tokens (e.g. fold them into Tailwind config, convert to OKLCH, rewrite as Style Dictionary JSON), stop and ask. The current shape is chosen deliberately to work without a build step.

## Before adding a component

Components in `components/` are reference implementations, not a shipping library. Each one is a single self-contained HTML file that loads `../tokens/tokens.css` and demonstrates one pattern. Prefer adding a new file over extending an existing one.

Do not add JS dependencies. Do not add a package.json. This repo is deliberately dependency-free so it can be cloned into any project's root without conflicting.

## Before changing a principle

The principle docs (`principles/*.md`) encode validated decisions. Each rule has a failure mode behind it. If you think a rule is wrong, grep this repo's `principles/failure-modes.md` for the narrative first. You will almost always find one. The CBAHI PHC project's `LESSONS.md` may contain the original incident if you want deeper context, but this repo is the authoritative source for the rule itself.

If the narrative is outdated or the rule's context no longer applies, propose the change with the new narrative. Do not silently loosen rules.

## This repo is the source of truth

This seed was extracted from the CBAHI PHC dashboard (roughly twenty revisions), the four hospital document skills (report-framework1, bulletin-board, healthcare-slides, pdf-tools), and StandardsHub. That is the origin story, not a dependency.

Going forward:

- Tokens, principles, and components are canonical **here**, not in PHC, not in the skills.
- Updates flow **into** this repo first. If a decision comes out of work in another project, the change lands here, and the consuming project pulls it in.
- Treat PHC and the skills as consumers. Their local copies of tokens or principles will drift; reconcile them against this repo, not the other way around.
- Narrative references to PHC in this repo's docs are history, not live links. Nothing here should `import` or `@import` anything outside its own folder.

## How to answer "should we add X?"

Default to no. This system has graduated through addition-then-subtraction more than once. The current shape is what survived multiple passes of "do we actually need this?"

If X solves a real user pain, name the pain, name the current workaround, and propose X as the smallest possible addition. If X is "nice to have," skip it.

## The moderator-director parity rule

Roles that share an intent share a shape. This was expensive to learn (R20 of CBAHI PHC) and is one of the things this system encodes that a fresh designer wouldn't think to check. Before adding a control to one role's view, grep the other role's view. If the same intent exists there, the control must match. If the intent does not exist there but should, add it in both places in the same change.

## Voice

See `brand.md` for the written voice. The short version: calm, specific, warm but not cloying, no emoji unless the user puts one first, no exclamation points in user-facing strings unless the copy is a genuine celebration.

In agent responses to Jo: minimum formatting, prose over bullets, flag assumptions inline with `[ASSUMPTION - needs verification]`, explain trade-offs rather than just executing.

## Files worth reading, in order

1. `README.md` - the map.
2. `principles/visual-language.md` - what the system looks like and why.
3. `principles/interaction.md` - how controls behave.
4. `principles/arabic-rtl.md` - the bilingual commitments.
5. `principles/failure-modes.md` - the scar tissue.
6. `tokens/tokens.css` - the actual values.
7. `components/*.html` - reference implementations.
8. `examples/demo-grid.html` - everything assembled.

## Files not to edit without asking

- `LICENSE` - MIT on purpose. Changing it changes how the repo can be consumed.
- `CHANGELOG.md` - append only. Don't rewrite past entries; add a new version block at the top.
