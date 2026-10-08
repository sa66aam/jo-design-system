# Jo's design language: one home for every project

The visual and interaction language of Jo's products (منصة القمة / Qimma Gate, StandardsHub, the CBAHI PHC accreditation
tool, مكتب ماجد and whatever comes next), its assets and its tools, in one place. It belongs to no single project.
Unified here on 2026-10-08 at Jo's word: «أحتاج الآن تتوحد لغة التصميم من كل الثلاثة مشاريع في مجلد واحد، وكلهم يتكلمون
نفس لغة التصميم بكل الأصول التي تحتاجها ... وهي لغة عامة وشحن أدوات».

**Read first:** `اقرأني.md` (Arabic: the context, how the language travels, the shipping rules), then parts أ and ب of the
guide. The guide is written in Arabic by Jo's choice; this map is in English so any model can find its way.

## What is here

| Path | What it is |
|---|---|
| `اقرأني.md` | the context in Arabic: what this home is, how it came to be, its three laws, shipping, a new project |
| `DESIGN_LANGUAGE_BUILD_GUIDE.md` | **the master guide, version 3.1**: أ the fixed core; ب the variation layer; ج retired and why; د the assets; هـ Qimma as the worked example (§1 to §19); و StandardsHub as the second example (light and depth, the Facility Tour); ز the CBAHI PHC tool as the third (its guide 2.6, verbatim, in English); ح living pages and paintings that move (2026-10-08) |
| `design-language/` | the assets (part د): `core-tokens.css`, `specimen.html` (opens whole with `grid/`), `svg/` (12 marks), `prompts/` (station still life, persona, gate emblem, blend pipeline), `grid/` (Qimma's seven station drawings), `tools/` (`grid-art.py`, `art-palette.py`, `persona-assets.mjs`, `watercolor.py`), `examples/` (`watercolor-v1`, `atom-capsule-v1`, frozen with their hashes) |
| `worlds/standardshub/` | the motion references: `FACILITY_TOUR_ARCHITECTURE.md` with its six screenshots in `tour/`, and `LANDING_FILM.md` (the 12.5 s landing film) |
| `previous/` | version 2.31 of the guide, for decisions that cite its old section numbers |
| `tools/ship.sh` | ships the guide and the assets to every project's mirror and verifies them by SHA-256 |
| `archive/seed-2026-04/` | the first attempt at a shared system (April 2026, one commit), kept verbatim as history |
| `LICENSE` | MIT, from the first seed |

## How the master was built (2026-10-08)

- **Parts أ to هـ and the appendix:** Qimma's master (`naif-gate-app/Lessons and Guides/`) as it stood that day, every
  line kept in order; only the title (3.1) and part د's path changed, a new head note added, and new rows in ب-1 and د.
- **Part و and its nine pointer lines:** from StandardsHub's copy (`docs/design/`, written 2026-09-28), verbatim.
- **Part ز:** the CBAHI PHC guide (`_docs/03_build-guides/`, 29,678 bytes), verbatim, its headings moved down two levels.
- **Part ح:** new.
- Checked by a script: Qimma's lines are a subsequence of the master, part و and its pointers are present, PHC's body is
  present in order, and no em-dash was added beyond the eight the sources carry.

Asset sources: Qimma for `README.md`, `core-tokens.css`, `prompts/`, `svg/` (newest: the gate emblem prompt, Jihan's
persona); StandardsHub for `specimen.html` (reads `grid/` beside it), `grid/` and the three Qimma tools (byte-identical to
Qimma's `tools/`); the Launching Video studio for `watercolor.py` and its example; the trial page for `atom-capsule-v1`.

## Mirrors and shipping

The home is written; mirrors are copied. `bash tools/ship.sh check` reads only; `bash tools/ship.sh ship` copies the guide
and `design-language/` (without `examples/`) to:

- `بوابة نايف القدرات/naif-gate-app/Lessons and Guides/` (guide and assets) and `بوابة نايف القدرات/Lessons and Guides/` (guide)
- `StandardsHub v4/docs/design/` (guide and assets)
- `CBAHI PHC/_docs/03_build-guides/` (guide and assets)

Run it in Jo's Mac terminal when no Claude Code session is working in those repositories; each project commits its mirror
in its own round. The code of a shipped project rules its own surfaces: where a value here differs, fix it here and ship.

## Upkeep

A change to the language lands here first, in the guide (Arabic, in the guide's own voice and structure), with its date
and Jo's words; then ship. A new asset gets its row in part د and in `design-language/README.md`. A new project becomes a
mirror line in `tools/ship.sh` and a line above.
