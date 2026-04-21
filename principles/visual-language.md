# Visual language

Written at the end of R20 of the CBAHI PHC dashboard, after roughly twenty revisions where each round deleted one confident idea from the round before. These are the rules that survived.

## One signal per axis

If a number already communicates readiness, the container shouldn't also shout it. A progress bar next to the number `73%` that is also tinted red-amber-green is redundant. Pick which surface carries the categorical claim (usually the number or its badge) and let the bar carry the quantitative axis alone. Colors, gradients, and shapes are expensive - spend them once per axis.

In practice: if the tile header has a colored domain badge, the body's progress fill should be neutral (the readiness gradient, not a domain color). If the bar is the domain gradient, the header's badge can drop its fill and become a thin outline.

## Gradient bars are a three-variable knob

Thickness, endpoint contrast, and tonal span all modulate how a gradient progress bar reads. Getting one right with the other two wrong is worse than a flat solid bar.

- **Too thin + too narrow a span** reads as flat. The eye can't find the gradient.
- **Too thick + too wide a span** reads as a category flag (stoplight, stripe). It pulls focus from the number next to it.
- **Thin (h-1, 4px) + wide span (≥ 500 Tailwind units between endpoints)** reads as *quietly quantitative* - you feel the progression without the bar competing with the label.

The house default is amber-900 → amber-400 on a 4px bar. It's an earned setting, not a preference.

## Metric columns are nouns, not verbs

The four scoring columns under a chapter tile (Met / Partial / Not Met / N/A) are categories, not steps. Don't animate them in sequence on mount, don't stagger their appearance, don't imply a flow from left to right. They're a grid, not a timeline.

If the user needs sequence cues, put them on the progress fill (which has a real duration axis) or on the navigation, not on the facts.

## Warm neutrals, not cool grays

The brand accent family runs amber → gold → forest → crimson - all warm. Tailwind's default slate/zinc/cool grays fight those hues. Use the `--gray-*` scale in `tokens.css`: slate-family with a slight warm lean. Under Noto Naskh Arabic body text, the difference between a cool gray and the warm gray is the difference between "clinical LED" and "paper under a lamp."

## Glass over gradient, never glass over glass

Translucent surfaces (`--glass-bg`) need a visible backdrop to register. Stacking two glass cards on top of each other turns the upper one into a muddy rectangle. If a card needs to sit *inside* a hero band, give the band a gradient and the card the glass; if the container is already flat, skip glass on the card and use a solid white with a 1px border.

## Headers carry identity, bodies carry data

The top band of any section is where the domain color lives (hero gradient + white-on-color chrome). Everything below the band uses the neutral scale, with domain color sneaking back only as thin accents (the left stroke on a tile, the progress fill). The body should be scannable in grayscale; reprinting a dashboard in B&W shouldn't erase the information, only the personality.

## No em-dashes in user-facing text

U+2014 is banned across the codebase in shipped strings. Use hyphens, middle dots (`·`), or rewrite. The rule is cheap to violate (one keystroke on macOS: option-shift-hyphen) and expensive to sweep. Install it as muscle memory, not a linter rule to suppress.

## One font per script, not one font for both

English body: **Lora** (humanist serif, real italics, tabular numerals).
Arabic body: **Noto Naskh Arabic** (correct ligatures, proper diacritic stacking, no shaping bugs in Chromium PDF export).
Never let the Arabic fall back to a system font - it will render as disconnected letters at best, tofu at worst. Wrap Arabic fragments inside English prose in `<span lang="ar">` so the font switch happens inline without flipping direction.

## Write rules you can feel, not rules you have to remember

A good design rule has a failure mode you can point at. "Use 12px spacing between tightly-related items" is forgettable. "If two things touch, the user will read them as one sentence" is not. This file (and its sibling docs) err toward the second form.
