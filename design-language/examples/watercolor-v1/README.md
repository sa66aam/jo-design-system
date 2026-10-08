# Worked example: the watercolour engine, v1 (frozen 2026-10-08)

`tools/watercolor.py` on one scene, a study desk, with one moving layer (the lamp's light), frozen as rendered.
The engine was built on 2026-10-07 for Jo's trial of the illustrated-companion techniques
(`Launching Video/references/cards/boris_cherny-1.md`) and moved into the studio on 2026-10-08 on Jo's word («نبغى ندمج كل الجديد
فيها»). The method it serves: part ح of `DESIGN_LANGUAGE_BUILD_GUIDE.md` here, and in films `Launching Video/ARCHITECTURE.md` 6. A copy of the Launching Video studio's `build-reference/examples/watercolor-v1/`.

## What is here

| Path | What it is |
|---|---|
| `scenes.py` | draws the flat passes by code (SVG through cairosvg, the example's only extra package): each shape once, rendered as a fill pass and an ink pass. It draws all three trial scenes; only the desk is frozen here |
| `in/desk.color.png`, `in/desk.line.png` | the desk's two passes, 1600x1000 |
| `in/desk-glow.color.png`, `in/desk-glow.line.png` | the lamp's light, a separate layer of the same size |
| `out/desk.png` | the painting |
| `out/desk.stage-1-flat.png` to `-4-ink.png` | the steps: the flat pass, the paper alone, the wash on paper, the ink on paper |
| `out/desk-glow.png` | the light as a layer on white (`--layer`): multiplied over `desk.png`, its opacity breathing between 0.55 and 0.78 over 5.5 s, it reads as a lamp that is on |
| `out/bleed.png` | the wet-wash bloom mask (`--bleed`): a page grows it from 1% to 270% over 2 s so a painting arrives like a wash spreading |

## Rebuild

From this home's root, with Python 3, NumPy and OpenCV (`opencv-python-headless`); `scenes.py` also needs cairosvg:

```
cd design-language/examples/watercolor-v1 && python3 scenes.py in && python3 ../../tools/watercolor.py in/desk.color.png in/desk.line.png out desk --stages && python3 ../../tools/watercolor.py in/desk-glow.color.png in/desk-glow.line.png out desk-glow --layer && python3 ../../tools/watercolor.py --bleed out/bleed.png
```

`scenes.py in` writes the other scenes' passes too; they are not part of the frozen example.

## The hashes as rendered

Rendered in the cloud container (Ubuntu, x86_64, Python 3.11, OpenCV 5.0.0, NumPy 2.4), seed 7 (the bleed mask 21).
Two runs gave the same bytes. Another OpenCV build or CPU may differ in the last bit of a filter; judge such a
copy by eye against `out/desk.png`, not by its hash.

```
a448fd96c57804271346ade9ee95b9e127fb81f46a397822b17d9c4d264be0c9  in/desk.color.png
2c38d02f0912b8acea64084e941f1a87c5069f89863b7579b5e14dec60e58cf0  in/desk.line.png
7fd0bb554d41e469047b9bd12e72e6988d8d9480cddb0f29ea5f160409bca9b1  in/desk-glow.color.png
19a260f8339913bbeedb37d7df39ed8f975d9b3c7ee94ee0c4dc1bbd22dc5b42  in/desk-glow.line.png
c3851601425e92aa15244bc63329a61b60bac841e1009855ff4ed7fb028a0de5  out/desk.png
c29b11013cececad548caebf43adbc69a0ba627dc094528ae5b30f893404ff0a  out/desk.stage-1-flat.png
995a394e3d6d8c00cb63d3e9e242674d35842218a16f7e2c2c6104ee51274190  out/desk.stage-2-paper.png
93f11ab43933cf11a21ef14cdd4cd227800845fb6aa654bf5bb4479180b9d886  out/desk.stage-3-wash.png
107522aa691a4173c7587a3e51e7b958505bbec5ba08362622037994c7e674a6  out/desk.stage-4-ink.png
835afb80932b2a99177d44435c228cfed4b9fe2f1f4922bd473d40d8cea95bcd  out/desk-glow.png
72c98a12e07795ed0d341c7fa473c7ef092a9c59ccecff160ed7147fd692826b  out/bleed.png
```

## What the trial showed, and what is still open

- The first version read as coloured pencil on sandpaper, not watercolour (D-73); the steps that cured it are
  named in the tool's header.
- Jo judged the look on the trial page and approved it as a pattern (2026-10-08; `../atom-capsule-v1/`).
  Open from the trial all the same: the lab bench's grey
  counter carried blooms too heavy for a large flat area (a per-region `--backruns` limit is the likely fix);
  the ink shows a faint digital edge at 200% zoom.
- Words are never painted by this engine: Arabic is set by the composition or drawn by `tools/wordshapes.py`
  (the same law as the character station, `motion-studio/MOTION-STUDIO.md` 3.3).
