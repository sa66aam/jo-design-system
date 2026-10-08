# Changelog

All notable changes to Jo's Design System are documented here.

## [0.2.0] - 2026-04-21

### Added
- `WORKFLOW.md` at repo root: the Standing Operating Procedure for creating, deploying, and iterating on design system seeds. Covers all six phases from extraction through first test, operating-mode reminders, and the guardrails around when NOT to spin up a new seed.
- Phase 1 now opens with a confirmation step: before any extraction, confirm with Jo whether the new seed warrants its own project or fits inside an existing one. Prevents auto-spinning new seeds when an update would do.

### Changed
- `README.md` file tree now lists `WORKFLOW.md` and links to it as the canonical process reference for seed work.

### Notes
- This repo now serves a dual role: the living design system for Jo's hospital and consulting work, and the process anchor for every other seed in the landscape (thamar-design-system, standardshub-design-system, personal-design-system). Future Cowork sessions should read `WORKFLOW.md` before starting any seed task.

## [0.1.0] - 2026-04-21

### Added
- Initial seed extracted from CBAHI PHC project, the 4 hospital skills (report-framework1, bulletin-board, healthcare-slides, pdf-tools), and StandardsHub.
- Token system: colors, typography, spacing, radii, shadows.
- Principles: visual language, interaction, Arabic/RTL handling, failure modes.
- Three reference components: progress bar, domain tile, hero band.
- Demo grid showing all components assembled.
- Luxe radial hero treatment: layered radial gradients, SVG noise overlay, hairline top highlight, semi-transparent inner panel with backdrop blur.

### Notes
- This seed is the source of truth for Jo's Design System going forward.
- Future updates should be tracked as new entries in this changelog.
- Repo is independent of the CBAHI PHC project; references to PHC in docs are narrative (origin story), not functional dependencies.
