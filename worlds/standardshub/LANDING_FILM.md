> **A copy (2026-10-08)** of `StandardsHub v4/handoff/03-landing-film.md`, kept in the design language's home as a
> motion reference beside the Facility Tour. The original in StandardsHub's repository is the live one; paths below are
> relative to that repository.

# Order 03 - The consulting front page: «من الفجوة إلى الختم»

**Stamp:** stage 2 live hidden since build `79c4ceb` (carried by `80a6c34`). Turned on for everyone on branch `claude/landing-public` (from `ee8ff98`, the center delete and portal step 1), by Jo's word on 2026-09-26: «ابي انشر الموقع بالانيميشن اعجبني». The previous page stays at `?film=0`.
**Source:** Jo, 2026-09-25, in the project thread "صفحة الهبوط للخدمة الاستشارية"; the plan artifact https://claude.ai/artifact/4TW7YyAWGRxN3FQ7KN3Kvk; the decision card (no character). The design reference is the Qimma paper landing (repo `sa66aam/Qimma`, read only): its film engine from round 147.

## Jo's words (the goal)
"هي واجهة الخدمة الاستشارية، يجب ان يكون فيها هوك بصري مهني... الكور بزنس حقك (اعتماد) وليس اجهزة اسنان او معدات ليزر... تبني فيها انيميشن احترافي حول هذه الخدمة بقصة تنسجها انت... وتبسيطها."
Then, on the plan: "اهم شيء يكون فيه خط رجعة للصفحة السابقة، لكن فكر بإعادة التفكير فيها وبساطتها تحتاج انت تكون مينمالستك وانفورمتيف."

## The film (src/landing/film/)
Twelve and a half seconds, no text, no sound, no character, never CBAHI's mark. The heroes are the standards and the relations between them. (Stage 1 ended on our shield pressed in as a seal; Jo removed it the same night, see Stage 2.)

| Seconds | What happens | What the visitor reads |
|---|---|---|
| 0 to 2.2 | An ink pen draws the ring of the 372 sub-standards | Accreditation is one whole system |
| 2.2 to 3.4 | The seven chapters bleed their colours under the line | Seven chapters, all covered |
| 3.4 to 5.6 | The mock survey's lens circles the ring; nine gaps turn red behind it | Gaps I could not see from inside |
| 5.6 to 7.6 | Each gap threads out to a tag (an owner, a date) and turns gold, faster | Every gap has an owner and a date |
| 7.6 to 9.0 | One gap slips back; a dashed loop re-checks it, then it turns gold | They verify, they do not close on paper |
| 9.0 to 10.3 | A gold wave closes the ring; the tags leave | Ready |
| 9.2 to 12.5 | The inside turns to night like an iris opening, the 209 real relations draw themselves chapter by chapter, and the camera leans in | One connected system |
| 11.3 onward | Signals travel the relations and land with a small gold ring, forever, repeating every 18 seconds | A living system, watched from above |

The ring is computed from the corpus (every bead a real sub-standard in its chapter's place and colour); the gap positions are illustrative. The Arabic page mirrors the film; the shield is never mirrored. Every frame is a pure function of time. It plays once when seen, rests on the seal (the poster), pauses when hidden, replays on a tap, draws the seal at once under reduced motion, and steps its density and grain down when frames run heavy. A lazy chunk of 19 kB (8.5 kB gzip).

## The page: eleven sections become four
1. Hero: two lines ("Ready before the surveyor arrives." / «جاهزية كاملة، قبل أن يصل المُقيّم.»), one line, one door (Request a consultation), the film, and the standards in three numbers (7, 84, 372) with the CBAHI scope line under them.
2. How we work: four stations (mock survey, corrective action plan, portal and team, re-check and visit day), one sentence each. They replace the six services and the six journey steps.
3. What you receive: the report excerpt in both languages, and the export line.
4. The ask: three promises (independent, not affiliated with CBAHI; confidential; bilingual), then WhatsApp and email.
Gone from the new page: the gap board, the standard card, the portal section, the four trust cards. The interactive constellation stays in the Standards Guide inside the platform.

## The switch and the way back
- One home: `src/landing/film/switch.js`. `LANDING_V2 = true` since 2026-09-26, so every visitor sees the new page; until then it was `false`.
- `?film=1` on `/` or `/ar` shows the new page on the live site; the language switch keeps it. `?film=0` shows the current page at any moment, even after the switch is on.
- The current page's sections are not edited for the new one (only `Numbers` and `ConsultSection` gained optional props that the current page does not pass), so turning the switch back to `false` and deploying hosting restores it exactly. Firebase Hosting's release history is a second net.

## Guards
`tests/landingFilm.test.js`: frames pure and repeatable; no chance, clock, text or sound in the film; every colour from the tokens and the mark, never pure black or white; the reads table; the real ring; the Arabic mirror; the rest frame; the switch off and in one home; the current page whole; the film only as a lazy chunk; the copy in both languages. `tests/core.test.js` holds the two languages to one shape and the Arabic to the terms law.

## Stage 2 (2026-09-25 night): the living network and a story for each section
**Jo's words:** «لا أريد شعار المنصة في الوسط، وأدمج بين الكونكشن السابقة وحركتها اللي اعجبتني في دائرة علاقة المعايير، وذيك الشبكة خلها حية كأنها تسجيل فضائي لنواقل عصبية او خطوط طيران تتابعها من الفضاء... اجعل لكل قصة تحت ايضاً قصة صغيرة تحكي خدمتنا ولها علاقة بالمحتوى.»

- **No seal.** `film/seal.js` is gone; the film is `film/network.js`. Nothing of the platform's mark is drawn in the film (guarded).
- **The relations back, from the constellation.** The same 209 links from `core/data/constellation.js`, drawn as the constellation drew them (a curve bent toward the centre, deeper for close neighbours), mirrors in teal, hard dependencies in gold, soft ones faint.
- **Alive, as seen from orbit.** Inside a night disc with faint city lights, signals leave a sub-standard and travel what rests on it, branching in cascades up to three steps deep (a fixed schedule, so every frame is still a pure function of time), each with a short trail, landing with a gold ring on the bead. The loop repeats every 18 seconds. The player paints the still network once and only the signals over it (`film.live`, `renderLive`), so the living part costs a few milliseconds a frame.
- **Point at one (tap on the phone).** Once the film has played, pointing at a sub-standard veils the rest and lights its relations: what it rests on in light teal, what rests on it in gold, with pulses on them; the line under the film names its code and its counts, in words that agree with the number in Arabic (`copy.js` `litUp`/`litDown`; the current page keeps its own wording).
- **The camera leans in** after the tags leave (`PUSH`, `ZEND` 1.32), so the living ring nearly fills the stage, on a phone too; `pick` divides by the same zoom.
- **Six scenes** (`film/scenes.js`, each 3 to 3.6 seconds, 8:5, played once when half seen, then still, mirrored in place for Arabic, glyphs never): the mock survey (a lens walks a checklist, one red row), the corrective action plan (a gap on the ring threads to a tag with an owner and a date and turns gold), the portal and team (a door opens and three cards fly to three faceless people), the re-check and visit day (a calendar ticks, one day slips and is re-checked, the visit day circled in gold), what you receive (one sheet becomes the PDF, the spreadsheet and the private web report with its expiry), and the ask (a clinic threads to a conversation that answers). `Scene.jsx` loads the player lazily; the current page's sections are untouched (the reports and contact sections take the scene only when the new page passes it).

Guards added to `tests/landingFilm.test.js` (15 tests): the living part and focus pure and periodic, the reads (night after the wave, routes done by their end, the push after the tags), the real routes and flights (only mirrors run both ways), no mark in the film, `pick` round trip in both directions, the scenes' shape and use, the player's live and rest states.

A short social clip of the film is optional, later.
