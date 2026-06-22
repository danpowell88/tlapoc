# Design system / shared component library + tokens

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/DESIGN`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** design

## Background

As a designer/developer, I want a shared set of design tokens and core components (buttons, inputs, banners, the blocked-action banner, chips, tables), so that all surfaces look consistent and the compliance UX patterns are reusable.
One design system (tokens, components) shared across web and the two Flutter apps delivers the 'fast and modern, thumb-first' UX the docs demand and avoids re-styling per surface.

## How it works

Design tokens — colour, typography, spacing, radius, elevation — are defined once in the shared package and consumed by both web (Angular) and Flutter, so a brand change is one edit, not three. Core components cover the everyday set (buttons, inputs, banners, chips, tables) plus the cross-cutting UX patterns the platform leans on: the blocked-action banner (the visible face of a server-side block, ADR-0008), consent/age chips, the S4 guardrail tag, and the offline indicator (for the provider app, ADR-0015).
Components are documented in a simple gallery/storybook so designers and developers see the catalogue and use the canonical version rather than re-implementing. The cross-surface reality (web tokens + Flutter widgets from one token source) is the point — the gallery shows the same component on both.
Accessibility basics are verified for the core components: colour contrast, visible focus, and minimum hit-target size, so the thumb-first promise is real on small screens. These patterns then appear across the prototype screens (chips on charting.png, banners, the S4 guardrail), but DESIGN ships the reusable primitives, not the screens.

## Requirements

- A shared set of design tokens and core components (buttons, inputs, banners, the blocked-action banner, chips, tables).

## Acceptance Criteria

- [ ] Tokens (colour, type, spacing) defined once and consumed by web + Flutter.
- [ ] Core components include the cross-cutting patterns from UX §4 (blocked-action banner, consent/age chips, S4 guardrail tag, offline indicator).
- [ ] Components are documented in a simple gallery/storybook.
- [ ] Accessibility basics (contrast, focus, hit-target size) verified for core components.

## UI designs / screenshots

_Prototype screen: Non-UI / platform scaffolding — no prototype screen._

- A component gallery/storybook; the patterns appear across every prototype screen (e.g. chips on charting.png, banners, the S4 guardrail).

## Technical notes (high level)

- Architecture decisions: [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Define tokens + core components (incl. the cross-cutting compliance patterns) and verify accessibility**
  Build the shared visual foundation consumed by web and both Flutter apps.
  - Tokens (colour, type, spacing, radius, elevation) defined once and consumed by Angular and Flutter from one source.
  - Core components: buttons, inputs, banners, chips, tables, PLUS the cross-cutting patterns — blocked-action banner (the UI face of ADR-0008 server-side blocks), consent/age chips, S4 guardrail tag, offline indicator (ADR-0015).
  - Accessibility basics verified for core components: contrast, visible focus, minimum hit-target size (thumb-first).
- [ ] **Publish the component gallery/storybook and usage docs**
  Make the system discoverable so surfaces use canonical components, not re-implementations.
  - A simple gallery/storybook showing each token and component, ideally the same component on web and Flutter.
  - Usage guidance for the compliance patterns (when to show the blocked-action banner, S4 tag, consent/age chips, offline indicator).
  - How web and Flutter import the package (ties to REPO's shared-package layout).
