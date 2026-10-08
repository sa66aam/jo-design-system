# Worked example: a living page (design language part ح), «كبسولة الذرة» (frozen 2026-10-08)

A single-file HTML page, published as Jo's private claude.ai artifact on 2026-10-07
(`https://claude.ai/artifact/5M5UGQ74t2G2mcmqNomuqN`, "التجربة 1"): a lesson capsule for a school platform
(Chemistry 1, lesson 2-1, the atom), built on the devices studied in `references/cards/boris_cherny-1.md` and
painted with `design-language/tools/watercolor.py`. Frozen here as published, with its images.

**Jo's verdict, 2026-10-08:** «كبسولة الذرة كانت رائعة جدًا، وهي مثال لبناء مواقع حية أو إضافة شرائح داخل مواقع»; and,
on recording it: «إذا كان ذلك يستحق أن يُذكر في ملف Endorsement، وليس في انتظار التجربة، فأنا أجيزها». So this page is
the studio's approved pattern for living pages: a whole site, or a section dropped into an existing one
(`DESIGN_LANGUAGE_BUILD_GUIDE.md`, part ح).

## What it carries (each one reusable)

| Device | Where in `index.html` |
|---|---|
| One material for everything: warm paper ground, sepia ink, Noto Naskh Arabic and Lora, colours as tokens with a dark theme in which the paintings stay on paper inside a framed print | `:root` and the two dark blocks |
| One reading column (about 36rem) with paintings breaking out to about 66rem | `.col`, `.wide` |
| A sticky ruler of the class's 45 minutes, read from the scroll position, that jumps on a tap and on the arrow keys | `.rulerbar`, `#ruler`, `draw()`, `update()`, `jump()` |
| Chapter heads hung from the book's ribbon bookmark | `.ribbon` |
| The coach's cheat card (a big number or formula, its unit, the line, a catalogue code), with a trap variant | `.cheat`, `.eye.trap` |
| Paintings as a still base with layers that move (the lamp breathing, tea steam, three electron shells turning, a flame, bubbles: seven layers), multiplied onto paper | `.stage img.ly` and the keyframes |
| Two arrivals: the wash bloom (a mask grown from 1% to 270%) and the pencil drawing that develops into colour; the first screen is complete at rest, only paintings below the fold wait | `.bleed`, `.develop`, the IntersectionObserver |
| On phones, a wide painting pinned under the bar while the view travels across it | `figure.paint.pin`, `pan()` |
| An explorer the student moves (atomic number 1 to 20): shells drawn live, the last shell marked, one plain line on what the element wants, the twenty rows folded beneath | `.explore`, `drawAtom()`, `verdictOf()` |
| A closing "workshop" showing how the paintings were made (the four steps) | `.workshop` |
| Reduced motion respected: no animation, no arrival | the last media block |

## Rebuild or reuse

Open `index.html` beside `img/`. To reuse the pattern for another subject: copy the folder, replace the words
(Arabic in the subject's own voice; Jo's rules on screen: Western digits, no em-dash on outward pages), redraw
the scenes for the subject (`design-language/examples/watercolor-v1/scenes.py` is the pattern) and paint them
with `design-language/tools/watercolor.py`, then replace the explorer with the subject's own interactive. Publish a page as an
artifact from a Cowork or Claude session; inside an existing site it drops in as a section, its tokens mapped to
the site's.

## Open from the trial

The lab bench's grey counter carries blooms too heavy for a large flat area; the ink shows a faint digital edge at
200% zoom (`../watercolor-v1/README.md`). The fonts were seen in the browser of the build machine only as
fallbacks (its network refused Google Fonts); Jo judged the page on his own screen.

## Hashes as frozen

```
8cf6653cd95cb0bb8a3d6bce8c91b9ebe04b2bb12c132f8e640dda7766374081  index.html
fbb81c4800c7969fafe1192867eed19fff4693ebd43580eaca7e4a05b67ef657  img/atom-e1.jpg
f10b586f1f703717f0dd50416b745d1613999a4432a798089766158e6b0c00af  img/atom-e2.jpg
3c4f84ac5052dce17735e0febb947e87f0c56ab415abee8e8703a17e6a1d88c0  img/atom-e3.jpg
f68db959691d41b31fa64a23c7830580f5efc1bf4fd4673a1d15d46130c10dd7  img/atom-e4.jpg
3f5423fa32dfd518c5e606772ba3bd955b02286d3cd1a0e61e2c5dff086ee91f  img/atom.jpg
30ea5fa792cf653eb2676235abce328501c0aabadaf088c6b3f54c29fe41eaf2  img/bleed.png
c564b7d04f48c2791985c4bbd1c7119aade0c3353de138e19965e91895c187b7  img/desk-glow.jpg
2a32d09c255164f7ddffc4ce2084290fe7774f2d8a9e9e3470628f1beb8bc828  img/desk-small.jpg
89ff0b8f95e9cc0ba7df0d90a9a5bd0c5169a83fd6a78f4ced6cba6775650408  img/desk-steam.jpg
4db2b6a3fe23c07505064fe312dd4c9e58f24aae85e0adb3d475f2fc675733a5  img/desk.jpg
8932bed964da76d848d4f8d7079ede713902516714242ba7511918deb8d5d613  img/desk.stage-1-flat.jpg
f0e6f5b27fce9b9ead50b419f968fdd749ad282d416e078d009bd0129de65e53  img/desk.stage-3-wash.jpg
4c431212a5f6ad3231af60bfbe71b96bdf6eda02a3df89e8f5ac8bff4c9b08cb  img/desk.stage-4-ink.jpg
31353cf5225b914d9b77a0907324b259cd7abbf1ccf2d7de57a44a15968db720  img/lab-bubbles.jpg
9310f455f96d235d31447154d2a3ece986d6998d2b0a24df6bf29ba4da138eb2  img/lab-flame.jpg
3782ec36c14514fd8344bbeecb8f002f643bf0aa771667347836358b363cd3e5  img/lab.jpg
```

`img/atom-e4.jpg` (the fourth shell) is painted but unused: sodium fills three shells.
