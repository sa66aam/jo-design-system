# Facility Tour Architecture Reference

> **What this is.** The build reference of StandardsHub's Facility Tour: the architecture behind it, the scene on each
> device, the theme (the building's plan at night) and what makes it feel like a different place from scoring. It is
> written so the tour can be rebuilt in another product, first Jo's CBAHI PHC tool (a separate repository), without
> reading StandardsHub's code first. Section 7 maps every piece onto PHC as it stood on 2026-09-28.
>
> **Read from** the live build `f7496ee` (2026-09-28): the version 5 plan (`6d3b4cf`), the moonlit cards and the other
> surveyor's half (`e18c4a5`). Every value below was read from the code that day. The code is the truth: where it and
> this file differ, the code wins and this file is corrected in the same change.
>
> **Its family.** The tour is one surface of StandardsHub's design language, recorded in part و of
> `DESIGN_LANGUAGE_BUILD_GUIDE.md` beside this file. The laws StandardsHub builds and reviews against are in
> `.claude/skills/standardshub-design/SKILL.md` and pinned by `tests/v5.test.js` and `tests/tour.test.js`.
>
> **See it.** The screenshots in `docs/design/tour/` (listed in 4.4), and the live tour with fictional data (demo mode,
> memory only): `https://st-hubs.web.app/app/c/demo-center/v/demo-visit/tour?demo=1`.

---

## 1. What the tour is

- **The walking face of the survey.** The sub-standards a surveyor checks on the move: observation (OBS), interview
  (INT) and dental record review (DEN; the records are read inside the clinic, right after the treatment they
  document, Jo 2026-09-26). Document review (DOC) and personnel files (PER) stay on the scoring board.
- **The building's order, not the manual's.** 18 stations from the entrance to the leadership interview. Each station
  is a page; each page is a list of prompts; a prompt is an action (observe, ask, request, check) with whom to ask and
  what to listen for; under each prompt, on a thread, the sub-standards it covers, scored right there.
- **The scores are the board's.** The tour scores with the board's own card and writes the same score documents, so
  a score given on the walk is on the board at once and the other way round (Jo, 2026-09-24: keep the findings as they
  are). The camera on each card files the photo under that sub-standard. The tour stores nothing of its own in the
  cloud.
- **Two doors.** `/app/c/:centerId/v/:visitId/tour`, the tour of one visit, scored and photographed live; and
  `/tour`, the route to read, with nothing to score.
- **Why a world of its own.** Scoring is desk work in the manual's order (chapter, standard, sub-standard), seated,
  two hands, often a laptop. The tour is a walk through a building with a phone in one hand, a patient in the chair and
  a receptionist waiting for the next question. Another posture, another order, another pace, so another ground,
  another light and another way to move. Jo's brief for version 5 (2026-09-27): the tour was "all solid and beige",
  make it more innovative. The answer was the building's own plan.

## 2. The laws it keeps

| # | Law | Where it holds |
|---|---|---|
| 1 | The tour stores nothing of its own: scores are the visit's score documents, photos are the visit's evidence; only device preferences live on the device | `src/tour/store.js`, `core/sync/repo.js` |
| 2 | Display never writes: a station's progress, a prompt's standing, the route's dots and the findings sheet are derived from the live scores on every render | `core/tour/index.js`, `tests/tour.test.js` |
| 3 | One write path: the board's card (`useScoreCard` to `repo.setScore`), `repo.ackLink`, `repo.addPhoto` and `repo.removePhoto`; no module of the tour writes | `src/tour/TourMode.jsx` header |
| 4 | The content is anchored and tested: T1 every OBS, INT and DEN sub-standard appears at least once; T2 every code exists, prompt ids are unique, kinds are known; T3 no em-dash, no Eastern digits, English inside Arabic only as the terms law allows; T4 a drawing for every station | `tests/tour.test.js` |
| 5 | The scoring stays English (Jo, 2026-09-23: Arabic is never the scoring): the card on the walk is the board's English card; the tour's chrome, stations and prompts are bilingual | `src/tour/scoreCards.jsx` |
| 6 | One thumb: every control used on the move sits in the lower half or in the dock; 44 px touch targets at least, 52 to 56 px for the walk's own actions, score buttons 54 px | `tour.css` |
| 7 | The content is a draft until Jo approves each station, and says so on every station | `stations.v0.json` `status` |
| 8 | A finalized visit is read only for both surveyors | `board.readOnly` |
| 9 | Motion is transform and opacity; every reveal has its conceal; nothing loops (three beats, then rest); reduced motion lands at once | `tour.css` |
| 10 | In Arabic the route mirrors, the pager's scroll sign flips and the arrows turn; pictures of places never mirror | `parts.jsx`, `TourMode.jsx`, `art.jsx` |

## 3. Architecture

### 3.1 Module map

| File | Size | Role |
|---|---|---|
| `src/core/tour/stations.v0.json` | 52 KB | The content: 18 stations, 100 prompts, 208 distinct sub-standards |
| `src/core/tour/index.js` | 5 KB | Pure helpers over the content and a map of scores. No React, no I/O |
| `src/tour/TourMode.jsx` | 20 KB | The surface: the doors, the visit's live data, the pager, the sheets, the dock |
| `src/tour/parts.jsx` | 14 KB | `StationHead`, `RouteMap`, `PromptCard`, `RouteList`, `NextCard` |
| `src/tour/scoreCards.jsx` | 7 KB | `TourScoreCard` (the board's card, tour-sized) and `OtherHalfCard` |
| `src/tour/sheets.jsx` | 15 KB | `Sheet` (a native dialog), `CodeSheet`, `FindingsSheet`, `RouteSheet`, `SeatSheet` |
| `src/tour/store.js` | 5 KB | Device state: the tour's language, the station open per visit, the other half opened; `scopeOf` |
| `src/tour/copy.js` | 10 KB | The chrome's words in English and Arabic, Arabic counted nouns picked at render time |
| `src/tour/art.jsx`, `stationArt.jsx` | 9 KB | The 18 station drawings as data on a 48 grid, and their renderer |
| `src/tour/icons.jsx` | 3 KB | The control icons on a 24 grid |
| `src/tour/tour.css` | 55 KB | The whole theme, 2,355 lines |

What the tour borrows from the platform (`src/core/`), never from a shell: `ui/useScoreCard.js` (the card's behavior),
`ui/scoring.jsx` (`ScoreButtons`, `ActivityBadge`, `SampleLabel`), `ui/findingCompanion.jsx` (the finding's
companion), `ui/relationNotes.jsx` (alerts across surveyors), `ui/photos.jsx` and `ui/photoDesk.js` (the camera, the
thumbnails, the viewer), `ui/mixed.jsx` (English inside Arabic), `ui/syncStatus.jsx` (the truth pill),
`scoring/seats.js`, `scoring/seatChoice.js`, `scoring/visitModel.js`, `relations/`, `sync/hooks.js`, `sync/repo.js`.
The boundary is enforced by eslint: `src/tour/` reads `core/` only; the shells never import the tour; `App.jsx` loads
it lazily as its own surface.

### 3.2 Routes and doors

- `App.jsx`: `const TourMode = surface(() => import('./tour/TourMode.jsx'))`, mounted at
  `/app/c/:centerId/v/:visitId/tour` (the most specific route wins over `/app/*`) and at `/tour`.
- Doors in: on the phone the home card and the center's bar (Tour beside Scoring) and scoring's bar; on the desktop and
  the iPad the workspace chip. Doors out: the brand goes back to the center, and the context line's **Scoring** goes to
  the same visit's board.
- `VisitDoor`: a navy splash while the sign-in resolves; a porcelain gate card (sign in with Google) when signed out;
  `VisitTour` reads the center, the visit, its scores, its acknowledgments and its photos live; a gate card says the
  visit is not available when it is missing or deleted.

### 3.3 The content model

One JSON file, versioned (`version: "v0-draft-2026-09-26"`, `status: "draft"`), with the kinds and the stations:

```json
{
  "kinds": {
    "observe": { "en": "Observe", "ar": "لاحظ" },
    "ask":     { "en": "Ask",     "ar": "اسأل" },
    "request": { "en": "Request", "ar": "اطلب" },
    "check":   { "en": "Check",   "ar": "افحص" }
  },
  "stations": [
    {
      "id": "clinic-setup",
      "icon": "chair",
      "en": { "title": "Dental clinic: set-up and zones", "where": "Any dental procedure room, before a patient sits" },
      "ar": { "title": "العيادة: التجهيز والمناطق", "where": "أي غرفة إجراءات أسنان، قبل جلوس المريض" },
      "prompts": [
        {
          "id": "clinic-sinks",
          "kind": "observe",
          "codes": ["IPC.2.3", "IPC.3.2"],
          "en": "Two sinks within easy reach of the dentist and the assistant, stocked with soap, alcohol hand rub and paper towels.",
          "ar": "مغسلتان في متناول الطبيب والمساعد، ومعهما صابون ومعقم كحولي ومناشف ورقية."
        }
      ]
    }
  ]
}
```

An `ask` prompt adds `who` (`{ "en": "Receptionist", "ar": "موظف الاستقبال" }`) and `expect`, what to listen for
(`{ "en": "Full name as in the ID document and the ID number; a working appointment system.", ... }`).

How a prompt is written: an action a surveyor takes at a place, drawn from the linked sub-standards' own text and
explanations, one full thought, the Arabic under the house's terms law (an English medical or quality term stays
English unless its Arabic is settled: `biofilm control`, `non-return valve`). The mix: 40 observe, 36 ask, 18 check, 6
request.

The walk, in order (the station's id, its drawing, its title, its prompts, its sub-standards):

| # | Station | Drawing | Title | Prompts | Codes |
|---|---|---|---|---|---|
| 1 | `entrance` | entrance | Entrance and reception | 6 | 15 |
| 2 | `clinic-setup` | chair | Dental clinic: set-up and zones | 6 | 9 |
| 3 | `changeover` | spray | Between two patients | 6 | 11 |
| 4 | `treatment` | gloves | During treatment | 7 | 17 |
| 5 | `dental-records` | record | Dental Records | 10 | 29 |
| 6 | `radiology` | radiation | Radiology | 6 | 11 |
| 7 | `sterilization` | autoclave | Sterilization unit | 5 | 8 |
| 8 | `waste` | biohazard | Dirty utility and medical waste room | 5 | 8 |
| 9 | `janitor` | mop | Janitor room | 4 | 5 |
| 10 | `lab` | lab | Dental laboratory | 8 | 22 |
| 11 | `storage` | fridge | Storage and materials refrigerator | 3 | 5 |
| 12 | `utility` | compressor | Compressor and utility room | 4 | 6 |
| 13 | `corridors` | cable | Corridors, electrical and fire safety | 6 | 13 |
| 14 | `emergency` | aed | Emergency readiness | 4 | 5 |
| 15 | `records` | files | Medical records | 4 | 7 |
| 16 | `laser` | laser | Laser and aesthetics rooms | 5 | 11 |
| 17 | `staff` | talk | Staff on the floor | 5 | 11 |
| 18 | `leadership` | table | Leadership and quality interview | 6 | 17 |

Coverage, measured on 2026-09-28: the corpus holds 372 sub-standards (OBS 105, INT 66, DEN 29, DOC 124, PER 48); the
walk carries all 200 of OBS, INT and DEN (T1), plus 8 others met on the way (7 DOC, 1 PER), 208 in all; two
sub-standards are met at two stations. In a two-surveyor visit 113 of them are Surveyor A's and 95 Surveyor B's. The
dental records sit inside the clinic, after During treatment, in the order a record is read: registration,
assessment, radiographs, plan, consent, the procedure, education, discharge, events, then how every entry is written.

### 3.4 The pure helpers (`src/core/tour/index.js`)

| Export | What it returns |
|---|---|
| `TOUR_ACTIVITIES` | `['OBS', 'INT', 'DEN']` |
| `tourCodes` | the sub-standards the walk must carry, in the manual's order |
| `stations`, `kinds`, `TOUR_VERSION`, `TOUR_STATUS` | the content |
| `promptIndex` | prompt id to `{ station, prompt, stationIndex }` |
| `stationsByCode` | code to the set of station ids that carry it |
| `stationCodes(station)` | the station's distinct codes, in the order the surveyor meets them |
| `coverage(codes)` | `{ total, covered, missing }` (T1) |
| `firstStationOf(code)` | the index of the first station that carries it, or -1 |
| `stationProgress(station, values, scope)` | `{ scored, total, gaps, done }`; a gap is NM or PM; `scope` keeps it to the codes this device scores |
| `promptStanding(prompt, values)` | `'NM'` if any code is Not Met, else `'PM'` if any is Partial, `'FM'` once every code is scored with no gap (N/A counts as scored), else `null` |
| `gapsByStation(values, scope)`, `pendingByStation(values, scope)` | the walk read back: each code once, at the first station it is met |

`values` is a plain map `{ code: 'FM' | 'PM' | 'NM' | 'NA' }` built from the live score documents on every render.

### 3.5 Data and state

```
TourMode (language, document direction, html.is-tour)
  VisitDoor (sign-in gate)
    VisitTour: live reads of the center, the visit, its scores, its acknowledgments, its photos
      ScoredTour: values, conflicts, ceilings, the seat, the other half, the scope  ->  the `board` object
        Tour: the station on show, the sheet, the photo viewer, the card brought into view
          StationHead / PromptCard (TourScoreCard | OtherHalfCard) / NextCard / the dock / the sheets
  Tour with board = null   (the /tour door: the route to read)
```

The `board` object every part receives: `centerId`, `visitId`, `samples`, `readOnly` (the visit is finalized),
`scores` (code to its document), `values`, `conflicts` (the relation alerts per code), `ceilings` (the highest
consistent score before a tap), `scope` (a set of codes, or null for the whole visit), `split`, `seat`, `mySeat`,
`setSeat`, `seatLabelOf(code)`, `other` (the other half opened: `{ all, codes, setAll, toggle }`), `ack`, `photos`.

What stays on the device (localStorage, never in the cloud, each read inside a try so a private window still works):

| Key | Holds |
|---|---|
| `sh4.tour.lang` | the tour's language (`en` or `ar`) |
| `sh4.tour.at.<visitId or route>` | the station open, by its id (so a route that gains a station opens the same place; an old index is read once) |
| `sh4.tour.other.<visitId>` | the other half opened here: `{ "all": false, "codes": ["LD.13.2"] }` |
| `sh4.seat.<visitId>` | the half this device scores; shared with the board |

What the tour writes, all through `core/sync/repo.js` (which stamps `_schema`, `_build`, `_by`, `_updatedAt`, `_rev`):

| Document | Fields | Written by |
|---|---|---|
| `centers/{c}/visits/{v}/scores/{code}` | `value` (`FM` `PM` `NM` `NA` or `null`), `note`, `finding`, `findingAccepted`, `documentName`, `location` | the card: a tap on a score, the note after 700 ms or on blur; a second tap on the chosen score writes `null` and keeps the note |
| `centers/{c}/visits/{v}/acks/{linkId}` | `decision`, `note` | keeping two scores that contradict each other, with a reason |
| `centers/{c}/visits/{v}/evidence/{photoId}` | `code`, `width`, `height`, `bytes`, `capturedAt`, `deleted` | the camera: the bytes to Storage first, `centers/{c}/visits/{v}/evidence/{photoId}.jpg`, then the record; a removal is a tombstone |

### 3.6 Two surveyors

- A visit is `FULL` (one surveyor, every sub-standard) or `SPLIT` (Surveyor A and Surveyor B, each with the half
  CBAHI's allocation table gives surveyor 1 and surveyor 2; `seatOfCode(code)`). `visit.seats` holds each seat's email;
  `seatOfEmail` finds the device's own seat; the seat on show is the device's choice, shared with the board.
- **The scope** is what this device scores on the walk: its own half plus the codes of the other half it opened; with
  the whole other half open, the whole visit (`scopeOf`). Progress, the route's dots, the map's stops and the findings
  all follow it; a station with nothing in scope says "Nothing to score here: this station is Surveyor B's" and its
  stop turns quiet.
- **A card in scope** is `TourScoreCard`. **A card outside it** is `OtherHalfCard`: quieter, its live score as a word
  in its hue, the sub-standard's text clamped to two lines, what the other surveyor wrote, the photos, and **Score
  here** (a pen), which opens that one sub-standard on this device.
- **Opened one at a time**, a card wears a gold ring, its seat's name and **Lock**, which gives it back. **With the
  whole half open** (the seat sheet), the cards carry their seat's name only, so gold stays a small dose.
- **The station head** carries two chips: the seat ("Surveyor A") and the other half ("Surveyor B: read only",
  "Surveyor B: 2 open", "Surveyor B: open"; quiet glass while read only, gold once something is open). Either opens
  the seat sheet: which half, then the other half read only or all of it open, and a line on opening one at a time.
- Every score still writes its one document through the board's own card, which either surveyor may write; nothing
  new is stored.

### 3.7 The score card on the walk

The board's card, tour-sized, one per sub-standard under its prompt, English and left to right inside an Arabic page
(`lang="en" dir="ltr"`), and memoized with stable callbacks so walking never redraws a card:

1. **The top line:** the code as the chapter's jewel (a tap opens the sub-standard's sheet), the survey activity's
   badge, the sample the activity needs (staff interviewed, dental records), the count of open relation alerts, and the
   camera at the end.
2. **The sub-standard's text**, 16 px, as the manual says it.
3. **Four keys**, N/A, Not Met, Partial, Fully Met, 54 px tall, white porcelain that rises off the card; the chosen one a
   jewel of its state; a second tap clears; the phone buzzes for 8 ms.
4. **On Not Met or Partial:** the surveyor's note (and a document name for a document review) with the finding
   companion's jewel in its corner; an accepted finding says so in gold.
5. **The photos** as thumbnails that open the viewer.
6. **The relation notes:** a contradiction with another sub-standard (across surveyors too), or the ceiling before a
   tap (worded as "Highest consistent score now: Partially met, because" the other code "is Partially met").
7. **The finding companion** (Generate, directives, Accept) as on the board.

### 3.8 Photos

`usePhotoDesk(centerId, visitId)` is one desk shared by the tour and both shells' cards, so a photo taken on the walk
shows under the same card on the board as it arrives. Capture is one native file input without `capture`, so the
iPhone offers the camera, the library and files; the picture is downscaled on the device; the bytes go to Storage and
then one record; the truth pill counts the photo until both are saved; offline it waits and goes again; a failed one
retries or is discarded from the viewer; the viewer zooms (two fingers, a double tap, a trackpad pinch) and closes by
itself when the last photo of that sub-standard is removed anywhere.

### 3.9 How it moves

- **The pager.** The stations sit side by side as pages in one horizontal scroll box with mandatory snapping, one
  station per swipe (`scroll-snap-type: x mandatory`, `scroll-snap-stop: always`); each page scrolls on its own, so a
  station walked before opens where it was left. Only the station on show and its two neighbours are drawn.
- **Which station is on show:** `Math.round(Math.abs(scrollLeft) / clientWidth)`; the absolute value because in a
  right to left page `scrollLeft` runs negative. `place(i, glide)` scrolls to `(rtl ? -1 : 1) * i * clientWidth`,
  smoothly for a neighbour, at once for a far jump (a long glide past every station reads as noise) and under reduced
  motion. A turned phone or a resized window keeps the station on show. On an iPad with a keyboard the arrows walk,
  their direction following the language.
- **A jump to a card** (`focusCode`): the station on show if it carries the code, else the first that does; the page
  scrolls the card 96 px under its top and the card flashes gold for 1.7 s. A code the walk does not carry opens its
  sheet instead, with the way to the board.
- **The sheets** are native `<dialog>` elements (a focus trap, Escape and the top layer for free): on a phone they rise
  from the foot within thumb reach, on an iPad and a laptop they settle as a centered panel of 640 px. The walk steps
  back behind a veil while one is up (`scale(0.965)`). A sheet asked to close stays on screen while it sinks (200 ms;
  180 ms as a panel) and is let go by a 230 ms timer, never by the animation's end, so it can never stay behind as an
  invisible wall.
- **The sheets:** the route (the path of stations, tap one to go there); the findings (two tabs: every sub-standard
  scored Not Met or Partial with its note and photo count, and what is not scored yet, station by station; Copy puts
  the findings on the clipboard as plain text); a sub-standard (the manual's text, its standard, where the walk meets
  it, what it mirrors, rests on and reaches, its score now and the way to its card); the seat (3.6).
- **The route as a path** (`RouteList`, a sheet on phones and iPads, the rail on a laptop): one line through the
  stops' tiles, measured from the first tile's middle to the last (`--line-top`, `--line-len`, `--walked`, kept on the
  list by a `ResizeObserver`); a quiet dotted track the whole way, the walked stretch drawn over it in gold, drawn from
  the first stop to yours when the route opens; your stop lit, "You are here" under it, its ring beating three times,
  then resting; the list opens scrolled to your stop.
- **The route as a map** (`RouteMap`, across the station's head on phones and iPads): an SVG of 360 by 64; the stops
  spread evenly along x at `y = 32 + 17 * sin(0.78 i + 0.4)`; one smooth line through them (Catmull-Rom as cubic
  Bezier segments, `c1 = p1 + (p2 - p0) / 6`, `c2 = p2 - (p3 - p1) / 6`), so the walked stretch is the same curve drawn
  only as far as the stop you are at; mirrored in Arabic (`scaleX(-1)`: a route has no fixed orientation of its own);
  hidden on a laptop, where the rail is the route.
- **The dock:** Back, the route button (a dot per station and "5 / 18"), Next. A dot is lit white where you are, teal
  once its station is scored in full, ringed in coral when it holds a gap, faint when the station is the other
  surveyor's.
- **The context line:** the center's name and the visit's title (each truncating within its own direction), the truth
  pill, and the way to Scoring.

### 3.10 Accessibility

Every icon button has a label; the route's stop carries `aria-current="step"`; each station page is labeled "Station
5 of 18"; the dialogs are labeled; focus is visible (teal on the plan); the drawings are decorative (`aria-hidden`);
under forced colors the plan becomes `Canvas` and the grid goes; reduced motion stops every animation and transition
listed in 5.7.

## 4. The scene

### 4.1 Phone (390 px, the first device)

```
 +--------------------------------------------------+
 | [mark] Facility Tour          [العربية] [Findings 3]|  top bar: a dark glass capsule
 +--------------------------------------------------+
   Al Waha Dental Center . Mock survey   (Saved)  Scoring      the context line
   STATION 5 OF 18  [Draft]                  +---------+
   Dental Records                            | drawing |      the plate: the station's
   ---- (the gold thread)                    |  lit on |      drawing on a glass tile
   At the dentist's desk: the record of the  |  glass  |
   patient you just watched, then more ...   +---------+
   o--o--o--o--(@)- - o - - o - - o - - o - - o              the map: walked in gold, you are here
   [==============---------]                                   the meter
   [Surveyor A] [Surveyor B: read only]  7 of 29 scored  * 2 gaps
   +------------------------------------------------+
   | (list) Check                                 (o)|  the guidance: moonlit porcelain,
   | Read the assessment: a full history and         |  the place's standing as a gem
   | examination with vital signs ...                |
   +------------------------------------------------+
    :  +--------------------------------------------+
    :  | [PC.3.3] Dental Records  (link 1)     (cam)|  a score card: the chapter's jewel
    :  | The sub-standard's text, as the manual ... |
    :  | [ N/A ][ Not Met ][ Partial ][ Fully Met ] |  54 px keys
    :  +--------------------------------------------+
    :  +--------------------------------------------+
    :  | MOI.2.3  Surveyor B            Partial     |  the other half: a quiet card
    :  | ...                        [pen Score here]|
    :  +--------------------------------------------+
   +------------------------------------------------+
   | [art]  NEXT STATION                          > |  the next card: glass with a gold edge
   |        Radiology                               |
   +------------------------------------------------+
 +--------------------------------------------------+
 | [ < Back ]   . . . . @ . . . . .    [ Next > ]  |  the dock: dark glass, Next the gold jewel
 |                 route  5 / 18                    |
 +--------------------------------------------------+
```

The screen is one column of fixed height (`100dvh`): the top bar, the context line, the pages, the dock. Nothing but
the page scrolls. The top bar hides the Findings label under 440 px; under 380 px the plate is 84 px and the dock's
buttons narrower.

### 4.2 iPad (700 px and up)

The plate grows to 124 px with 34 px corners; the station's name to 32 px; the guidance card breathes (20 px); the
dock stands centered at `min(760px, 100% - 28px)` with 140 px buttons; the dots run in one line; the sheets become a
centered panel (640 px) that settles in place instead of rising.

### 4.3 Laptop (1024 px and up)

```
 +------------------------------------------------------------------------------+
 | [mark] Facility Tour                                  [العربية] [Findings]   |
 +------------------------------------------------------------------------------+
   context line
   +-------------------------+    +------------------------------------------+
   | TOUR ROUTE              |    | the station head (no map: the rail is it)|
   | [art] Entrance      :   |    | the prompts and their cards              |
   | [art] Clinic set-up :   |    |                                          |
   | [art] ...     (gold) :  |    |                                          |
   | [art] You are here  (@) |    |  max 780 px                              |
   | [art] Radiology     .   |    |                                          |
   +-------------------------+    +------------------------------------------+
                        +-----------------------------------+
                        | [ Back ]   . . . @ . . .  [ Next ]|
                        +-----------------------------------+
```

A grid of a 320 px rail and the main column, 30 px apart, in at most 1,200 px, centered. The rail is dark glass on the
plan, the stops in light: the tiles navy glass, the walked tiles ringed in gold, the scored ones teal, yours ringed in
gold with a glow.

### 4.4 The screenshots

Taken from the live build `f7496ee` in demo mode (fictional data, memory only) on 2026-09-28, the mock survey of a
two-surveyor visit, this device in Surveyor A's seat. No console error on any of them.

| File | Device | What it shows |
|---|---|---|
| `tour/phone-en-station.jpg` | phone, 390 by 844, English | station 5, Dental Records: the head with its drawing on the glass tile, the map (walked in gold, you are here, a gap ringed in coral, a scored stop teal), the seat and the other half's chips, a guidance card, the dock with Next in gold |
| `tour/phone-en-cards.jpg` | phone, English | one of Surveyor B's sub-standards opened with Score here: the gold ring, its seat, Lock, the four keys and the camera; under it another of B's cards, quiet, with Score here |
| `tour/phone-en-route.jpg` | phone, English | the route as a sheet over the veiled plan: the path walked in gold, "You are here", each stop's count and gaps |
| `tour/phone-ar-station.jpg` | phone, Arabic | the same station right to left: the map from the right, the arrows turned, the Dental Records term kept in English inside the Arabic |
| `tour/ipad-en-station.jpg` | iPad upright, 820 by 1180 | station 2 with scored cards: the chosen key a jewel of its state, the met gem lit in the guidance's corner |
| `tour/laptop-en-station.jpg` | laptop, 1440 by 900 | the rail as the route on the plan, the map hidden, the main column beside it |

## 5. The theme: the building's plan at night

### 5.1 The idea

The ground is the plan of the building, drawn at night: navy to teal, a fine drawing grid, a teal light over the head
of the station where you stand, a faint gold light rising from the foot. The walk is drawn on it in gold. What you read
and score is moonlit porcelain that floats high off the plan, its long shadow falling into the navy. The chrome is dark
glass. The one lit action is gold: Next. The score hues appear only where a score carries that meaning, on its own
card. Everything else on the plan speaks in four inks: light (the text), teal (done, and the way), gold (the walk and
the next step), coral (a gap).

### 5.2 Tokens

The plan's own, declared on `.tour`:

| Token | Value | Use |
|---|---|---|
| `--bp-1` | `#14224f` | navy, the plan's top (also `html.is-tour` and the splash) |
| `--bp-2` | `#123a5a` | the middle |
| `--bp-3` | `#0b4a57` | teal-navy, the foot |
| `--bp-ink` | `#f1f7f6` | text on the plan |
| `--bp-soft` | `rgba(228, 241, 239, 0.8)` | secondary text on the plan |
| `--bp-mute` | `rgba(228, 241, 239, 0.6)` | quiet text on the plan |
| `--bp-teal` | `#6fd6cd` | done, links, the station's count, focus |
| `--bp-gold` | `#e5c461` | the walked route, you are here |
| `--bp-coral` | `#ff9d92` | a gap, on the dark plan only |
| `--bp-glass` | `rgba(16, 32, 64, 0.62)` | the top bar |
| `--bp-glass-edge` | `inset 0 1px 0 rgba(255,255,255,.16), inset 0 0 0 1px rgba(255,255,255,.1)` | every dark glass edge |
| `--bp-card` | `linear-gradient(180deg, #e7eef2 0%, #dee6eb 55%, #d5dfe5 100%)` | moonlit porcelain |
| `--bp-card-quiet` | `linear-gradient(180deg, #e0e8ed 0%, #d3dde3 100%)` | the other half's cards |
| `--bp-card-edge` | `rgba(255, 255, 255, 0.5)` | the card's lit edge |
| `--bp-float` | `inset 0 1px 0 rgba(255,255,255,.85), 0 0 0 1px rgba(6,18,36,.3), 0 2px 4px rgba(4,14,30,.24), 0 24px 46px -18px rgba(4,14,30,.78)` | a card floating high off the plan |

The house's tokens the tour also reads (a product that rebuilds the tour defines these, or its own equivalents, under
`.tour`): `--ink #1d3349`, `--ink-body #37434f`, `--ink-soft #55606c`, `--ink-mute #626d79`, `--teal #0f6a74`,
`--teal-hi #1b8f92`, `--teal-wash rgba(15,106,116,.08)`, `--gold-1 #e5c461`, `--gold-2 #b8912e`, `--gold-text
#86692a`, `--gold-wash rgba(229,196,97,.16)`, `--gold-thread linear-gradient(90deg, #e5c461, #b8912e)`, `--jewel
linear-gradient(170deg, #1b8f92 0%, #0f6a74 48%, #0a4a57 100%)`, `--jewel-rim`, `--jewel-glow`, `--jewel-gold
linear-gradient(170deg, #f6e3a1 0%, #e5c461 45%, #c79d36 100%)`, `--sheet-face`, `--sheet-edge`, `--sheet-lift`,
`--sheet-press`, `--shadow-rest`, `--well #f4f7f6`, `--well-lo #edf1f0`, `--hair`, `--hair-strong`, the chapter's
`--ch` with `--ch-hi`, `--ch-lo`, `--ch-glow` mixed from it, the score states (`--met #3f6b3a`, `--partial #86652b`,
`--notmet #97474a`, `--na #756a58`, each with its `-bg` and `-line`), `--r-chip 999px`, `--r-xl 28px`, `--swim
cubic-bezier(0.2, 0.7, 0.3, 1)`, `--t-fast 160ms`, `--t-state 220ms`, `--font-en`, `--font-ar`. Their full values are in
`src/core/design/tokens.css`.

### 5.3 The ground

```css
.tour {
  background:
    radial-gradient(70% 42% at 86% 6%, rgba(27, 143, 146, 0.46), transparent 70%),   /* the teal light over the head */
    radial-gradient(64% 40% at 4% 100%, rgba(229, 196, 97, 0.14), transparent 72%),  /* the gold light from the foot */
    radial-gradient(50% 36% at 0% 34%, rgba(56, 92, 170, 0.18), transparent 70%),    /* a breath of blue at the side */
    linear-gradient(165deg, var(--bp-1) 0%, var(--bp-2) 48%, var(--bp-3) 100%);
}
/* the drawing grid: major lines every 64 px, minor every 16, fading toward the foot */
.tour::before {
  position: absolute; inset: 0; pointer-events: none; content: '';
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.055) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.055) 1px, transparent 1px),
    linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
  background-size: 64px 64px, 64px 64px, 16px 16px, 16px 16px;
  background-position: -1px -1px;
  mask-image: linear-gradient(180deg, #000 0%, rgba(4, 14, 30, 0.7) 60%, rgba(4, 14, 30, 0.35) 100%);
}
```

The light is in the top far corner in both languages (a light has no reading direction). The ground is the element's
own background inside a screen of fixed height, so it never stretches down a long page.

### 5.4 Materials on the plan

- **Dark glass**, for the chrome: the top bar (`--bp-glass`, blur 16 px, saturate 1.4, 20 px corners, 10 px from the
  screen's edges), the dock (`rgba(14, 28, 58, 0.76)`, blur 20 px, 24 px corners, rising into the thumb zone on
  entry), the rail (`rgba(12, 28, 58, 0.42)`), the next card (glass with a gold edge and a gold light in its corner).
  Every glass edge is `--bp-glass-edge`, every glass shadow a navy one. The brand's mark sits on a small porcelain tile,
  so its navy reads on the dark bar.
- **Moonlit porcelain**, for what is read and scored: the guidance (22 px corners), the score cards (18 px), the lock
  notice, the sign-in card. On the navy, pure white glared (Jo, 2026-09-28 06:05: the floating components on the navy
  are too white; dim them and keep them lifted), so the white carries a cool breath of the plan (`--bp-card`), a softer
  lit edge (`--bp-card-edge`) and a long shadow that falls well below (`--bp-float`). The fields and washes inside a
  card take the card's own tone, never white. The quiet variant (`--bp-card-quiet`) is the other half's.
- **White keys**: the four score buttons stay white porcelain, because they are touched and must rise off the dimmed
  card. The sheets stay white too: they float over their own veil, not on the plan.
- **The glass tile** for a station's drawing: `linear-gradient(160deg, #22507a, #173b60 70%)` under a soft light at its
  crown, an inner rim, a teal glow of 42 px around it, 100 px square with 30 px corners (124 and 34 from 700 px). The
  drawing takes its inks from the tile: `--art-accent rgba(111,214,205,.22)`, `--art-paper #1d466b`, `--art-teal
  var(--bp-teal)`, `--art-gold #f0d98f`.
- **The gold jewel**, the one lit action: Next in the dock (`--jewel-gold`, navy words, a lit rim, a gold glow), the
  finish card's Findings, and the small gold count of findings in the top bar. Nothing else on the plan is gold but the
  walk.
- **The standing gem**: a place's standing is an 11 px lit gem in the guidance card's far top corner, in the hue of the
  lowest score given there (met, partial, not met), with a halo of its hue; a Not Met also tints the card's edge. Never a
  stripe on the card's side.
- **The chapter's jewel** on each code: `linear-gradient(165deg, var(--ch-hi), var(--ch) 55%, var(--ch-lo))`, white
  code, a ring and a glow of the chapter.
- **The kinds of prompt** in their own inks on a wash of themselves: observe teal, ask navy blue `#2c4a8c`, request the
  gold's text ink, check the soft ink.
- **The thread**: the sub-standards hang under their guidance on a dotted line drawn on the plan
  (`2px dotted rgba(255, 255, 255, 0.3)`).

### 5.5 Light and state

| State | On the map | In the dock | On the route |
|---|---|---|---|
| You are here | a gold stop with a white rim and a glow, its halo beating three times (1.5 s each) | a white dot, scaled 1.25, with a halo | your tile ringed in gold with a glow, its ring beating three times; "You are here" |
| Walked (behind you on the route, not a score) | the line drawn in gold, the stop's rim gold | | the gold stretch of the line, the tile ringed in gold |
| Scored in full | a teal stop with a glow | a teal dot with a glow | a teal-lit tile |
| Holds a gap | a coral rim | a coral ring | the count of gaps in the not met ink (coral on the rail) |
| The other surveyor's | faint (0.4) | faint | the text faint |

The station's meter is a teal bar with a glow on a dark track; the station's count of gaps is coral with a small
glowing dot; the station's name has a 44 by 3 px gold thread under it.

### 5.6 Type

Lora for English, Noto Naskh Arabic for Arabic; Arabic a step larger and looser, never tracked, never in capitals.

| Element | English | Arabic |
|---|---|---|
| The tour's body | 17 px | 18 px |
| The station's name | 27 px, 1.18 (32 from 700 px) | 28 px, 1.45 |
| The station's count | 12.5 px, bold, capitals, tracked 0.1 em, teal | the same, not tracked |
| Where the station is | 15 px, 1.5 | 15 px |
| A prompt's words | 18 px, 1.55 (19 from 700 px) | 19.5 px, 1.85 |
| Listen for | 15 px, 1.55, on a teal wash | the same |
| The score card's text | 16 px, 500, 1.55 (always English) | |
| The next station's name | 19 px | |
| The dock's buttons | 16 px, 600 | |

### 5.7 Motion

All on the house's swim curve, `cubic-bezier(0.2, 0.7, 0.3, 1)`: a station arriving rises 14 px in 440 ms; the dock
rises into the thumb zone in 420 ms on entry; a sheet rises in 320 ms and sinks in 200 ms (a panel: 280 and 180); the
veil comes in 260 ms and goes in 200 ms; the walk steps back behind a sheet in 360 ms; the route's gold draws itself in
560 ms; the stop you are at beats three times; a card brought into view flashes gold for 1.7 s. Under reduced motion
every one of them lands at once.

### 5.8 The drawings

18 pictures of places, hand drawn on a 48 grid in 1.7 strokes with round ends, one accent wash per drawing, gold only
where the real object carries it (the radiation sign, the defibrillator's bolt, the laser's spark). Pictures of
places, never decoration, and they never mirror in Arabic (a room does not change sides when the language does). They
are data (`ART` in `art.jsx`), so a drawing's classes take their inks from wherever it sits: `af` accent fill and stroke,
`a` accent fill, `f` ink fill, `s` and `s-dot` the accent line, `gf` gold, `pf` the paper that hides a line behind a
shape (the tile's own colour), `thick` and `beam` heavier strokes.

## 6. Why it feels like another place, and why it is still the same product

| | Scoring (the board) | The Facility Tour |
|---|---|---|
| Ground | the light atmosphere: celadon mist lit by the chapter's colour and a pool of gold | the building's plan at night: navy to teal, a drawing grid, a teal light over the head |
| Order | the manual's: chapter, standard, sub-standard | the building's: 18 stations in walking order |
| The unit | a sub-standard's card | a place, with prompts that say what to do there |
| Guidance | the three cards (the surveyor's activity, what to look for, the possible deficiency), Arabic | a prompt per action, whom to ask, what to listen for, bilingual |
| Moving around | lists, the chapter chips, the navigator | a route: pages swiped with the finger, the walk as a map, you are here, Next |
| The one lit action | the teal jewel with the gold thread (Finalize, Next in a chapter) | Next, the gold jewel |
| Cards | white porcelain on the mist | moonlit porcelain floating higher on the dark plan |
| Chrome | light glass | dark glass |
| Pictures | small activity icons | the place's own drawing, lit on a glass tile, at every station |
| Posture | seated, two hands, desktop, iPad or phone | standing, one thumb, the phone first |

What they share, so the surveyor never learns two products: the same score card and the same four score colours, the
chapter's jewel on every code, the finding companion, the truth pill, the camera and the photos, the gold thread, Lora
and Noto Naskh Arabic, the swim curve. A score given in either place is the same document.

## 7. Rebuilding it in CBAHI PHC

### 7.1 PHC as it stood on 2026-09-28 (read only, never changed from here)

- `Projects/CBAHI PHC`, one app at the root: React 19, Vite 7, Tailwind 4, Firebase 12 (Firestore; Auth with email and
  password and custom claims `centerId` and `moderator`; Storage), hosting on the Firebase project `sfhd-ready`.
- **No router:** `App.jsx` (3,699 lines, one large file by design) holds a `currentPage` state; any path but the root
  is rewritten to `/`.
- **The phone** is a twin chosen outside the working component: a wrapper per surface picks the phone or the desktop
  component (`LiveScoringSurface`: `isPhone ? <PhoneScoring/> : <ScoringPage/>`), `usePhone.js` at 500 px.
- **The corpus** (`src/data/standards.js`): 8 chapters, 115 standards, 570 sub-standards, activity types DOC 316, OBS
  90, MRR 85 (medical record review), INT 38, PER 41. Chapter colours in `DOMAIN_COLORS` (`src/lib/config.js`).
- **The scores:** one map per center, `{ subId: record }`, in localStorage (`cbahi_phc_{centerId}_scores`) mirrored to
  `centers/{centerId}/state/scores` (field `scores`, merged). Values `2`, `1`, `0`, `'NA'`; a clear writes `null`.
  Record fields `value`, `rawComment`, `finding`, `findingAccepted`, `documentName`, `scoredAt`, plus `scoredBy` and
  `previousSurveyors`. One write path: `App.handleScoreChange`, which stops when `isCenterWriteSafe(centerId)` is false,
  saves locally, backs up, then mirrors after 500 ms.
- **Surveyors split by chapter claims**, not halves: `survey.mode` is `'all'` or `'chapters'`, and each
  `chapterBlocks[code]` holds `surveyorName`, `claimedAt`, `submittedAt`. A visit is an assessment
  (`ASSESS_${Date.now()}`), one unlocked at a time, under `centers/{c}/surveyDocs/{surveyId}`.
- **Evidence exists:** `EvidenceControl.jsx` on every card (a file input without `capture`), `evidenceStore.js` (a map
  in `state/evidence`), `evidenceStorage.js` (1600 px JPEG at 0.72 to `centers/{c}/evidence/{subId}/{id}.jpg`, PDFs to
  10 MB).
- **No tour.** Only a Visit Day entry (`surveyDayContent.js`, `facility-tour`, 11:30 to 12:30, observation, both
  surveyors) and the findings' standard opening "During the facility tour,".
- **Language:** no i18n library and no app-wide switch; paired fields (`nameAr`, `titleAr`); Lora and Noto Naskh Arabic.
- **Design:** PHC design language v2.6: the paper canvas (`.phc-canvas`), translucent cards (`rgba(255,255,255,.88)`),
  warm shadows, saturated score colours (`#059669`, `#d97706`, `#dc2626`). The master design language (3.0) retires
  most of these; see part ج and part و of the guide.
- **Its rules:** `npm run build` before any commit that touches `src/`; a deploy is chained and only on Jo's go; the
  three invariants (saving is synchronous, every state document carries `_updatedAt`, every key is
  `cbahi_phc_{centerId}_*`); one write point (`storage.set` to `mirrorToFirestore`, a synced key registered in
  `SUFFIX_TO_DOC` and `DOC_MAP`); an added feature is additive and never changes scoring or sync (the header of
  `evidenceStore.js`); no router, no TypeScript, no splitting of the large files; no test runner (the gates are the
  build and eslint); no em-dash, Western digits, no "AI" in labels; plan mode for any sync or storage work; the
  Regression Prevention Check before a commit.

### 7.2 The map, piece by piece

| The tour in StandardsHub | In PHC | The port |
|---|---|---|
| Doors: `/app/c/:c/v/:v/tour` and `/tour` | `currentPage` state, no router | a `currentPage` value `tour` with the center and the open assessment in context; the route to read when none is open; doors from the scoring page, the dashboard and the phone's scoring |
| One responsive surface, layout by width | the form factor chosen outside the component | one `TourSurface` wrapper that passes the same component to every device (the tour lays itself out by width: pages, then the rail from 1024 px) |
| `stations.v0.json`, 18 stations of a dental center | none | PHC's own stations, same schema (3.3), written for a primary health care center |
| `TOUR_ACTIVITIES = ['OBS','INT','DEN']`, 200 sub-standards | OBS 90, INT 38, MRR 85: 213 of 570 | `['OBS', 'INT', 'MRR']`; the medical records read where the care happens, as the dental records are |
| Score values `FM PM NM NA null`, one document per sub-standard | `2 1 0 'NA' null`, one map per center | an adapter `letterOf(record)` (2 to FM, 1 to PM, 0 to NM, NA to NA) so the helpers of 3.4 run unchanged; writes go through `handleScoreChange` only |
| The card: `useScoreCard` behind the board's card, tour-sized | `SubstandardCard` and `ScoreButton` | PHC's own card with a tour size (larger keys, the text at reading size), never a second card; the note is `rawComment` |
| Writes: `core/sync/repo.js` | `storage.set` to `mirrorToFirestore`, the `isCenterWriteSafe` gate | the same path; the tour adds no synced key |
| Surveyor A and B by CBAHI's table, the other half opened all or one at a time | chapter claims | the scope is the chapters this surveyor claimed; "the other half" becomes "the other chapters": read only, all open, or one at a time with Score here and Lock |
| Relation alerts and ceilings (StandardsHub's relations engine) | the finding hints (`MockFindingHint`, `PriorFindingHint`) | leave the alerts out, or show PHC's hints on the card |
| Photos: `usePhotoDesk`, one record per photo | `EvidenceControl`, `evidenceStore`, `evidenceStorage` | mount `EvidenceControl` on each tour card; the findings sheet counts from `evidenceStore` |
| Device state `sh4.tour.*`, `sh4.seat.*` | keys `cbahi_phc_{centerId}_*` | `cbahi_phc_{centerId}_tour_lang`, `_tour_at_{assessmentId}`, `_tour_other_{assessmentId}`: device only, never in `SUFFIX_TO_DOC` |
| The tour's own language switch, bilingual content, the card English | no switch; paired fields | the tour's own switch, as here |
| Content laws T1 to T4 (vitest) | no test runner | `scripts/check-tour.mjs` run before the build: coverage, valid codes, unique ids, known kinds, a drawing per station, no em-dash, no Eastern digits |
| `tour.css` over the house tokens | v2.6 tokens | copy `tour.css` whole and define the house tokens of 5.2 under `.tour`, so nothing else in PHC moves |
| The chapter's jewel (`--ch` from the corpus colour) | `DOMAIN_COLORS` | set `--ch` from `getDomainColor(chapter).primary` on each card |
| The station drawings (dental rooms) | none | keep the drawing rules of 5.8; reuse what fits (entrance, sterilization, waste, janitor, storage, utility, corridors, emergency, records, talk, table) and draw the rest (triage, vaccination and the cold chain, the pharmacy, sample collection) |

### 7.3 Decisions for Jo before the port

1. **The score colours on the tour's cards:** PHC's own (the saturated set its board wears today) or the calm set the
   design language moved to. Recommended: whatever PHC's board wears, so the two faces of one visit agree; move both
   together when PHC's board moves.
2. **Where the medical records are read:** inside the care areas, right after the care they document (as the dental
   records here), or at a records station. Recommended: inside, as here.
3. **The stations and their order** for a primary health care center, reviewed like StandardsHub's (draft until
   approved, station by station).

### 7.4 The order of work

1. The content and its check: PHC's stations as JSON, `scripts/check-tour.mjs` green (coverage of OBS, INT and MRR).
2. The pure helpers of 3.4, with the value adapter.
3. The surface and the theme: `tour.css` with its token block, the pager, the dock, the head with its map, the route
   and its sheet, the rail on a laptop; empty cards first.
4. The score card on the walk, through `handleScoreChange`, and the live reads of the open assessment.
5. The camera (`EvidenceControl`) and the findings sheet.
6. The chapter claims as the scope, then the other chapters opened all or one at a time.
7. Arabic: the chrome, the stations, the prompts; the pager's scroll sign; the map mirrored.
8. Screenshots at 390, 820, 1180 and 1440, English and Arabic; the checklist of 7.6; Jo's word.

### 7.5 Traps StandardsHub already paid for

- **White on the navy glares** (LESSONS #612): the cards on the plan are moonlit porcelain, not the light pages' white;
  measure every text colour again on the dimmer face.
- **Floating is three things** (#611): a living ground, a card of another material, and a shadow whose ambient layer
  falls visibly below the card. A card that only has an outline reads as cut out of the plan.
- **A score colour is never decoration**; gold stays a small dose (the walk, Next, the count); a gap on the dark plan
  is coral, on porcelain the not met ink.
- **Right to left scrolling**: `scrollLeft` is negative in Arabic; take its absolute value and scroll to the negative.
- **Draw only the station on show and its neighbours**; a full route of drawn pages is slow on a phone.
- **Close a sheet by a timer**, never by an animation's end, or a skipped animation leaves an invisible wall.
- **iOS Safari scrolls sideways what is not locked** (#633): hold the page's other axis and the back swipe.
- **An approval given before the change existed does not cover it** (#620): the deploy word comes after Jo has seen the
  tour, in the thread that did the work.
- **A reply lost to a dropped connection is a result the user never received** (#622): commit first, then report.

### 7.6 Done means

- Every OBS, INT and MRR sub-standard of PHC is on the walk, and the check says so.
- A score given on the walk is on the board at once, and the other way round, on two devices.
- A photo taken on the walk shows under the same card on the board.
- The scope follows the chapter claims; the other chapters open all at once or one at a time, and Lock gives one back.
- 390, 820, 1180, 1440, English and Arabic: no sideways scroll, no console error, focus visible, reduced motion
  respected, every card floating at the top of the page and scrolled, Next the only gold action.

## 8. Files to read first, in this order

1. `src/core/tour/index.js`, then `stations.v0.json` (the model).
2. `src/tour/TourMode.jsx` (the flow), `store.js` (the device), `parts.jsx` (the head, the map, the prompt).
3. `src/tour/scoreCards.jsx` and `core/ui/useScoreCard.js` (the card), `sheets.jsx` (the sheets).
4. `src/tour/tour.css` (the theme) with `src/core/design/tokens.css` (the house's tokens).
5. `tests/tour.test.js` and the Facility Tour block of `tests/v5.test.js` (what is pinned).
6. `PARITY.md`, the row "Facility Tour Mode" (the behaviour device by device), and `PROJECT_LOG.md` Entries 37, 38,
   61 to 63 (why it is this way).
