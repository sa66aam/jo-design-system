# Arabic and RTL

Bilingual Arabic/English is the default in every project this system touches. Arabic is not a translation layer; it's a first-class render target that has to look as considered as the English.

These rules come from months of PDF export breakage, font-fallback humiliation, and one shipped document where the Arabic numerals ran left-to-right inside a right-to-left sentence.

## Noto Naskh Arabic, exclusively

The Arabic font stack is `'Noto Naskh Arabic', 'Traditional Arabic', serif`. The first is the only one we actually want; the second is a Windows-era fallback that prevents the worst outcome; the serif default is a last-resort safety net so the browser doesn't render tofu.

Never use Amiri for body text - it's a display face, tuned for headlines, and sits awkwardly next to Lora. Never use the system Arabic fallback on macOS (Geeza Pro) or Windows (Arial Unicode MS) - they have shaping bugs on certain diacritic combinations that don't show up until you print.

Load Noto Naskh Arabic via @fontsource or a self-hosted @font-face block. Don't rely on the user having it installed.

## Direction switches on the element, not the string

`dir="rtl"` on the element tells the browser to reverse the inline flow. It does not change the font. A `<p dir="rtl">` in Lora will render Arabic letters in sequence but unshaped - which looks like a ransom note cut from disconnected letter tiles. Pair the direction switch with a font switch, always.

CSS pattern:

```css
[dir="rtl"]       { font-family: var(--font-ar); }
[lang="ar"]       { font-family: var(--font-ar); }
```

The second selector is for inline fragments inside an LTR parent - `<span lang="ar">...</span>` picks up the Arabic font without flipping direction.

## Numbers stay Western in medical/accreditation contexts

CBAHI, the Saudi Ministry, and every audit body this work touches uses Western digits (0-9), not Arabic-Indic (٠-٩). Don't auto-convert. If Arabic prose contains a percentage, render it as `٪73` or `73%` - whichever the source document uses - but don't let the framework silently swap.

## Export Arabic to PDF as raster, not vector

Chromium's print-to-PDF pipeline handles Arabic shaping correctly at screen zoom levels but breaks at print zoom levels in specific edge cases (isolated `yaa` + hamza, tatweel + shadda combinations). The reliable path for charts and any canvas-rendered Arabic is:

1. Render to a `<canvas>` in the browser at 2x or 3x the target size.
2. Export as PNG.
3. Embed the PNG in the PDF via Playwright or whatever PDF pipeline is in play.

This trades file size for reliability. The file-size cost is small; the failure mode of shipping a broken PDF to a minister is not.

## Bullet points and lists need a non-breaking space after the marker

Standard bullets render fine in Arabic LTR but break in nested lists. The fix is to use a non-breaking space (`\u00A0` / `&nbsp;`) after each bullet character instead of a regular space. The rendering engine treats the bullet + marker + NBSP + text as a single token that wraps cleanly.

Same goes for numbered lists: `1.\u00A0Item one` in source.

## xlsx: set `readingOrder: "rtl"` on Arabic cells

If you're writing an Excel file with Arabic content (via xlsx.js, openpyxl, or any library that exposes cell properties), the cell's reading order must be set explicitly:

```js
cell.alignment = { readingOrder: 'rtl', horizontal: 'right' };
```

Without this, Excel will render the text in the cell editor correctly (because it sniffs direction from the first strong character) but will align it to the left. In a table where half the cells are English and half Arabic, the misalignment is immediately visible and looks careless.

## Don't mirror icons that carry direction

A right-pointing chevron means "next" in English and "previous" in Arabic. Mirror it. A magnifying glass icon doesn't point anywhere - don't mirror it. The test: if a literal-minded person would be confused by the mirrored version, keep the original.

Currency symbols, graphs, and logos never mirror.

## Layout mirrors; numbers and measurements don't

When the direction flips, everything in the flow reverses: the sidebar moves to the right, the progress bar fills from right to left, the breadcrumb reads right to left. But the *values* don't flip. `73%` stays `73%`, not `%37`. A date of `2026-04-20` stays that way. The mirror is about layout and reading flow, not about character-level reversal.

## Test in the worst case first

The hardest Arabic rendering case is a mixed string: Arabic prose with an English medical term in parentheses, followed by a Western number, in a right-to-left table cell, exported to PDF, viewed on Adobe Reader.

Build your template against that case. If it looks right there, the simpler cases will look right too. If you build against the easy case (pure Arabic in a single paragraph), you'll ship the hard case broken.

## Wrap, don't hyphenate

Arabic doesn't hyphenate at line breaks the way English does. Turn off CSS hyphens for RTL content:

```css
[dir="rtl"] { hyphens: none; word-break: normal; }
```

The text will wrap at word boundaries only. Lines will be slightly more variable in length than English; that's correct.
