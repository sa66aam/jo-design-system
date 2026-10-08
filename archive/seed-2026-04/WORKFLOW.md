# Standing Operating Procedure - Design System Seed Workflow

This is the standard workflow for creating, deploying, and iterating on design system seeds for Jo. Apply this whenever Jo asks to: (a) create a new design system, (b) extract a DNA from existing projects, (c) update an existing seed, or (d) connect a seed to Claude Design.

## Context

Jo maintains separate design systems per use-case domain rather than one universal system. Current and anticipated seeds:

- **jo-design-system** (live, public): hospital reports, CBAHI consulting, leadership documents. Lora + Noto Naskh Arabic, luxe radial surfaces, formal institutional voice.
- **thamar-design-system** (planned): Thamar Al-Nakheel premium dates brand. Warmer palette, hospitality/luxury voice, product-forward layouts.
- **standardshub-design-system** (planned): clinical applications (StandardsHub dental scoring, future SaaS). Clinical precision, dashboard-forward, dense data displays.
- **personal-design-system** (planned): personal projects, family tree app, miscellaneous. Lighter constraints, more experimental.

Never merge these into one system. Each domain has its own visual language, voice, and use cases. Mixing them produces mediocre output across all domains.

## The standard workflow (apply in order)

### Phase 1 - Extraction

When Jo asks to create a new seed from existing work:

1. Before starting extraction, always confirm with Jo whether the new seed warrants its own project or whether it fits inside an existing one. Never auto-create a new seed when an update would do.
2. Identify all source projects, skills, or repos that contain the relevant design DNA. Read them in full, do not skim.
3. Extract design tokens (colors, typography, spacing, radii, shadows) into both `tokens/tokens.css` and `tokens/tokens.json`. The two must mirror each other exactly.
4. Extract written principles into `principles/` folder, one file per concern: `visual-language.md`, `interaction.md`, `arabic-rtl.md`, `failure-modes.md`. Add more files only when a concern genuinely does not fit existing files.
5. Build 3-5 reference components in `components/` folder as standalone HTML files that link to `../tokens/tokens.css`. Each component should demonstrate a key pattern from the DNA.
6. Build one assembled `examples/demo-grid.html` that uses all components together so a visitor can see the system in action with one file open.
7. Render `examples/demo-grid.html` with Playwright at 1400x900 viewport. Save the screenshot as `examples/preview.png` and verify visually that the design intent is preserved.

### Phase 2 - Documentation

Every seed must have these root files before it ships:

- `README.md`: about-this-repo preamble, how-to-use section with Claude Design linking instructions, file tree overview.
- `CLAUDE.md`: written for future Claude instances reading this repo. Treats this repo as the source of truth, not a derived artifact. Documents binding rules, never-do lists, and visual hierarchy enforcement.
- `brand.md`: voice, tone, language policy, target audiences, anti-patterns.
- `CHANGELOG.md`: starts at version 0.1.0 with extraction provenance. Every meaningful update gets a new entry.
- `LICENSE`: MIT or Jo's preferred license. Default to MIT unless told otherwise.
- `.gitignore`: covers node_modules, .DS_Store, *.log, dist, build, IDE folders.

Run a final em-dash sweep across all text files. Replace every em-dash with a hyphen or rephrase. Em-dashes are banned globally across all Jo's outputs.

### Phase 3 - Verification

Before handing off to Jo, produce an integrity report containing:

- Total file count and folder structure (tree view, 2 levels deep)
- Confirmation: zero references that escape the seed folder (no `../` paths pointing outside)
- Confirmation: `tokens.json` parses cleanly
- Confirmation: zero em-dashes in any text file
- Confirmation: visual treatment intact across all components and demo file
- List of any anomalies, missing items, or risks

### Phase 4 - Handoff to Jo's Mac for repo creation

Jo's shell sandbox in Cowork is mount-limited and cannot move folders outside the current project. The Git initialization and GitHub push happen on Jo's Mac. Provide him with a single Terminal block formatted as follows:

```bash
cd "$HOME/Claude co-work/Projects"
mv "CURRENT_PROJECT/_seed-folder-name" "final-repo-name"
cd final-repo-name
git init -q && git add -A && git commit -q -m "Initial commit: <seed-name> seed with <key visual feature>"
gh repo create final-repo-name --public --source=. --remote=origin --push
```

Critical formatting rules for the Terminal block:

- No inline comments (apostrophes in comments break the shell)
- No em-dashes anywhere
- One single paste, no multi-step instructions
- Use `final-repo-name` with hyphens, no spaces, no underscores (matches GitHub naming convention)

Tell Jo what each line does in plain English before the block. Tell him what to expect on screen after each command. Tell him what error states might appear and how to handle them.

After Jo runs the block and sends back the GitHub URL and the short commit hash from `git rev-parse --short HEAD`, log the handoff in the project log file under §15 (or whichever section is current) with:

- Date in Gregorian format (YYYY-MM-DD)
- Repo URL
- Short commit hash
- One-line summary of what the seed contains

### Phase 5 - Connect to Claude Design

After the repo is live, instruct Jo to:

1. Go to claude.ai/design
2. Click "Set up your design system"
3. In "Link code on GitHub", paste the new repo URL
4. Authorize via the GitHub app: choose "Only select repositories" (never "All repositories"), select only the new seed repo
5. Fill in "Company name and blurb" with a one-paragraph description of the seed's purpose
6. Leave .fig file and assets uploads empty unless Jo has specific assets to add
7. Add binding rules to "Any other notes?" by extracting them from the seed's CLAUDE.md so Claude Design enforces them at generation time

### Phase 6 - First test

After Claude Design finishes generating, give Jo a specific test prompt drawn from his actual use case for that seed. The test prompt should exercise the seed's primary domain, not a generic example. The goal is to verify:

- Visual intent is preserved
- Binding rules are respected (em-dashes, numerals, language policy, hierarchy)
- The seed's voice comes through, not a generic Claude voice

If the first test reveals gaps, log them as issues to address in the next CHANGELOG entry. Never silently fix and hope; document and iterate.

## Operating mode reminders (carry across all phases)

- Execute, do not advise. Run shell commands when you have access. Do not hand Jo commands he could have run himself if you could have run them.
- When you genuinely cannot do something (sandbox limits, missing credentials), say so directly and explain the constraint. Do not ask permission for steps you could take.
- Ask one focused question when a real decision is needed (public vs private, naming, scope). Do not ask multiple questions in series.
- Default to public repos for design systems unless Jo signals otherwise. Public is the convention for shareable design DNA.
- Never overwrite Jo's existing repos or files outside the seed folder without explicit confirmation.
- Report outcomes, not recipes. The deliverable is the result, not the instructions to produce the result.

## When NOT to apply this workflow

- When Jo asks for a one-off design or component that does not need to be a seed
- When Jo is iterating on an existing seed (use a focused update, not the full extraction phase)
- When Jo is exploring or sketching ideas, not committing to a system
- When the work belongs inside an existing seed rather than warranting a new one (ask before creating a new seed)

When in doubt about whether a request warrants a new seed or an update to an existing one, ask Jo directly: "Should this be a new seed or an update to <existing-seed-name>?"
