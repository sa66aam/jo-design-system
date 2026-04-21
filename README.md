# Jo's Design System

## About this repo

This is the design system that powers Jo's projects across hospital reporting, CBAHI consulting, the Thamar dates brand, and personal applications. It is the canonical source of truth for design tokens, visual principles, and reference components. Updates to the design language happen here first.

A portable seed for the visual and interaction language that has evolved across Jo's bilingual (Arabic/English) healthcare and accreditation work. Drop this repository into any new project's root, or link it into Claude Design so future sessions start with the same vocabulary.

This is not a CSS framework. It is a set of tokens, principles, and reference components that encode specific design decisions Jo has validated through roughly twenty revisions of the CBAHI PHC dashboard and four bilingual document skills. Each decision has a failure mode behind it - read `principles/failure-modes.md` if you want to know why a given rule exists before you propose changing it.

## What's in here

```
tokens/
  tokens.css        CSS custom properties - drop into any HTML project
  tokens.json       Machine-readable mirror for tooling / build scripts

principles/
  visual-language.md   One signal per axis; gradient bars; warm neutrals
  interaction.md       Dropdowns, focus, write-through boundaries
  arabic-rtl.md        Noto Naskh Arabic, direction vs font, PDF export
  failure-modes.md     Every rule has a scar behind it

components/
  progress-bar.html    R20-tuned readiness bar (thin + wide-span)
  domain-tile.html     Chapter card with badge, bar, scoring columns
  hero-band.html       Gradient header with glass dropdown shell

examples/
  demo-grid.html       8 tiles under one hero band, all tokens assembled

fonts/
  README.md            Notes on Lora + Noto Naskh Arabic loading

brand.md               Voice, tone, one-liner about who this system serves
CLAUDE.md              Guidance for Claude sessions reading this repo
CHANGELOG.md           Versioned log of tokens, principles, and component changes
LICENSE                MIT
```

## How to use

The primary path is Claude Design. Open the "Set up your design system" page in Claude Design, and paste this repo's GitHub URL into the "Link code on GitHub" field. Future Claude sessions opened through Claude Design will see the tokens, principles, and components without you having to re-explain anything, and any change committed here propagates the next time a session loads the link.

## Quick start (direct integration)

### In a plain HTML page

```html
<link rel="stylesheet" href="tokens/tokens.css" />
<style>
  .card {
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    border: var(--glass-border);
    border-radius: var(--radius-xl);
    padding: var(--space-6);
  }
</style>
```

### In a React project

```jsx
import './tokens/tokens.css';

function ChapterTile({ code, title, pct, counts }) {
  return (
    <div className="tile" style={{ '--stroke': `var(--${code.toLowerCase()}-primary)` }}>
      {/* See components/domain-tile.html for the full pattern */}
    </div>
  );
}
```

## What this system is not

It is not a component library with build tooling. There is no npm package, no webpack plugin, no Tailwind preset. The tokens live as CSS custom properties because that is the smallest useful unit that works in any HTML, React, or Vue project without a build step.

It is not opinionated about framework. Use React, Vue, Svelte, vanilla HTML, HTMX - the tokens compile to the same CSS either way.

It is not a theme toggle. There is no dark mode. Glass-on-gradient is the house look, and inverting it into dark mode would mean building a parallel set of decisions that have not been validated. If you need dark mode, fork this and earn your own scars.

## The domain palette

The eight CBAHI chapter colors (LD, PC, MIS, LB, MM, MOI, IPC, FMS) are included because they are the most heavily exercised and road-tested palette in this system. For non-healthcare projects, you can either:

- Remap them semantically (e.g. LD → "governance," PC → "customer," etc.), or
- Replace the eight with your own domain list, keeping the shape: `{primary, light, accent, gradient}` per domain.

The palette design rule is: each primary must have enough contrast against white that a code badge with it as an outline reads at 12px. The provided eight all pass that bar.

## The R20 moment

If one decision in this system is worth preserving above the others, it's the readiness bar: thin (4px / `h-1`), wide tonal span (amber-900 to amber-400), muted enough to sit next to a number without competing with it. That shape came out of R20 of the CBAHI PHC dashboard after five earlier attempts got progressively worse. It's documented in `principles/visual-language.md` and exemplified in `components/progress-bar.html`.

## License

MIT. Use it anywhere, no attribution required. If something in here saves you a day of debugging, pay it forward by writing down the failure mode behind your own next design decision.
