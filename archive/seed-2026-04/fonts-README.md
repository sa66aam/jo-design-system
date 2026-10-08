# Fonts

This system uses two font families, one per script. Both are free, open-licensed, and hosted on Google Fonts. The stack is intentionally short because long fallback chains produce surprising shifts in production.

## Lora (English body + display)

- **Use for:** all English text (body, titles, metrics, labels).
- **Why:** humanist serif with real italics (not obliques), tabular numerals that align in columns, and a x-height that works at 14px through 48px without tuning.
- **Weights we use:** 400 (regular), 500 (medium), 600 (semibold), 700 (bold).
- **Google Fonts:** https://fonts.google.com/specimen/Lora
- **NPM:** `@fontsource/lora`

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
```

## Noto Naskh Arabic (Arabic body + display)

- **Use for:** all Arabic text, regardless of context. Never let Arabic fall back to a system font.
- **Why:** correct shaping for Naskh ligatures, proper diacritic stacking, and reliable rendering under Chromium's print-to-PDF pipeline. The only Arabic body face we have validated end-to-end for this system.
- **Weights we use:** 400 (regular), 500 (medium), 600 (semibold), 700 (bold).
- **Google Fonts:** https://fonts.google.com/noto/specimen/Noto+Naskh+Arabic
- **NPM:** `@fontsource/noto-naskh-arabic`

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
```

## Self-hosting (recommended for PDF pipelines)

If the output is a PDF generated through Playwright or Puppeteer, self-host both fonts. The print renderer does not wait for external font loads reliably, and you will ship a PDF with a serif Latin fallback standing in for the Arabic.

Install via fontsource:

```bash
npm install @fontsource/lora @fontsource/noto-naskh-arabic
```

Then import the weights you actually use:

```js
import '@fontsource/lora/400.css';
import '@fontsource/lora/500.css';
import '@fontsource/lora/600.css';
import '@fontsource/lora/700.css';
import '@fontsource/lora/400-italic.css';

import '@fontsource/noto-naskh-arabic/400.css';
import '@fontsource/noto-naskh-arabic/500.css';
import '@fontsource/noto-naskh-arabic/600.css';
import '@fontsource/noto-naskh-arabic/700.css';
```

## Do not use

- **Amiri** - display face, wrong for body text, clashes with Lora's weight.
- **Cairo / Tajawal / Rubik Arabic** - modern sans Arabics that don't match the Lora pairing.
- **System Arabic fallbacks** (Geeza Pro on macOS, Arial Unicode MS on Windows) - produce shaping bugs on diacritic combinations that only appear in print.
- **Inter / SF Pro / Roboto** on the English side - Lora is the house face; sans swaps change the whole system's feel.

## Why two families instead of a single variable one

Lora is a serif. Noto Naskh Arabic is a Naskh. There is no single family that does both well, and pairing a serif with a Naskh reads more harmonious than pairing a sans-Latin with an Arabic of any style. The bilingual pairing is the decision; the fallbacks are just the safety net.
