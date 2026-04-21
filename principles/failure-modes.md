# Failure modes

A list of failures this system has shipped, and the rules that exist because of them. Read this before proposing a "small cleanup" - most small cleanups in this codebase have a scar story behind the specific choice they're about to undo.

## Em-dash in user-facing strings

**What happened:** A CBAHI dashboard tally row rendered `{date} - {count}` with a U+2014 em-dash. Arabic text elsewhere on the page rendered correctly. The em-dash displayed fine in Chromium but rendered as tofu in a specific PDF export path. The minister received a document with a box where a dash should have been.

**The rule:** Em-dashes (U+2014) are banned in all shipped user-facing text. JSDoc and block comments are exempt because they're compiler-stripped.

**How to apply:** Before shipping, grep for the U+2014 character (`\u2014` in regex, option-shift-hyphen on macOS) in `src/**/*.{js,jsx,tsx}` and in any string template. Replace with hyphens, middle dots (`·`), or rewrite the sentence. Don't special-case "but this one looks better with an em-dash", the next file you add won't know about the exception.

## Scattered awaits in the UI layer

**What happened:** Phase 34 attempted to "save as you go" by sprinkling `await save(...)` calls across input handlers. Three weeks later, the app had intermittent flicker on every keystroke, and two bugs where the same field saved twice in different shapes. Rollback was hard because the scattered awaits had grown entangled with validation.

**The rule:** The UI layer reads sync. The only async boundary is the persistence bridge at boot. Writes queue and flush at named points (blur, submit, navigation, visibility change).

**How to apply:** If you're tempted to add `await` in a component, stop and ask: can this value be pre-fetched into the bridge, then read sync? If yes, do that. If no, commit at a boundary event, not inside a render path.

## Restructuring at the user's pain point

**What happened:** In R15 the user asked for a thinner progress bar. The response shipped a thinner bar *plus* a refactor of the tile grid, a rename of `DomainTile` to `ChapterTile`, and a reshuffled color palette. Three changes in one PR, two of them unrequested. The user had to review the whole thing to find the one change they asked for, then the bar change turned out to need a follow-up anyway because the refactor moved the component that held the h-1 class.

**The rule:** Make the requested change. Do not "while I'm here" the surrounding area. If you spot other issues, list them separately and ask.

**How to apply:** When asked to change X, the diff should touch X. If the diff touches Y because of genuine coupling, name the coupling in the commit message so the user can push back.

## Assumption-based edits

**What happened:** Several times, a session started by assuming the shape of `config.js` or the name of a prop based on how similar files tend to look. Some of those assumptions were wrong, and the edits shipped before the user caught them. Each one needed a revert round.

**The rule:** Before editing, verify with grep or Read. If you make an assumption, flag it inline with `[ASSUMPTION - needs verification]` in the proposal.

**How to apply:** Prefer two minutes of grep over a one-line edit that needs a two-day unwind. Memory of "a similar file had this shape" is not verification.

## Mocking the integration boundary

**What happened (not this project, but a lesson carried in):** A project mocked the database in integration tests because the real DB was slow. The mocks drifted from the real schema over a year. A production migration passed CI and broke production because the mocks had been lying the whole time.

**The rule:** Integration tests hit the real integration boundary. Use a test database, not a mock one. If the test is slow, fix the test environment, not the boundary.

**How to apply:** Ask "is this a unit test or an integration test?" Unit tests can mock anything. Integration tests can mock external services *only* - never the internal layer they claim to integrate with.

## "Improve" the tangential data during a targeted rewrite

**What happened:** A request to rewrite chapter `PC` localization strings also "fixed" five OLD-format data artifacts the session happened to notice in neighboring files. The user had been keeping those OLD artifacts verbatim for a reason - they were the baseline against which the migration was being measured. The "improvement" invalidated the comparison.

**The rule:** Preserve non-scope OLD data artifacts verbatim. If something looks wrong but isn't in scope, ask before changing it.

**How to apply:** The scope of a task is what the user asked for, not what you see while you're in the file. When in doubt, narrower.

## Over-formatting conversational responses

**What happened:** Responses grew headers, bullets, and bolding for simple questions. A two-sentence answer became a mini-report with three H3s. The user couldn't tell what was important because everything was emphasized.

**The rule:** Minimum formatting to be clear. Prose and paragraphs for explanations. Bullets only when the content is genuinely a list.

**How to apply:** Before sending, look at the response. If it has more than two levels of hierarchy and the question was conversational, flatten it.

## "AI" in user-facing strings

**What happened:** An early version of a feature had buttons labeled "AI Enrichment" and "AI Refine." Users asked what the AI was doing and got into debates about whether they wanted "AI" touching their data at all. The feature was identical in function to non-AI enrichment, just with better defaults.

**The rule:** Don't name buttons after the implementation. Name them after the user outcome. "Enrichment," "Generate," "Refine" - not "AI Enrichment."

**How to apply:** Grep for `AI` in user-facing strings. If it's describing the mechanism, rename. If it's genuinely distinguishing from a non-AI path the user chooses between, keep it.

## "Upscale" meaning only size

**What happened:** A request to "upscale" an icon was interpreted as a pixel-density bump. The user meant "make it bigger *and* visually simpler so it survives the larger rendering" - big and busy is worse than small and busy, because the busy-ness now dominates.

**The rule:** "Upscale" means literal size increase *plus* density simplification. Fewer strokes, bolder shapes, more whitespace inside the glyph.

**How to apply:** When the user asks to make something bigger, ask yourself if the current design will *improve* at the larger size or just get noisier. If noisier, redesign.

## The compounding principle

Every rule in this file exists because the compounded cost of the failure was disproportionate to the cost of prevention. A two-minute grep prevents a two-day unwind. A single bundled PR's review time prevents three weeks of intermittent bugs. Choose the two minutes every time.
