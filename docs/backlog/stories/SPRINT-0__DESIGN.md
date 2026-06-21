# Design system / shared component library + tokens

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/DESIGN`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** design

## Background

As a designer/developer, I want a shared set of design tokens and core components (buttons, inputs, banners, the blocked-action banner, chips, tables), so that all surfaces look consistent and the compliance UX patterns are reusable.
One design system (tokens, components) shared across web and the two Flutter apps delivers the 'fast and modern, thumb-first' UX the docs demand and avoids re-styling per surface.

## How it works

A shared design system (tokens + core components) consumed by web and both Flutter apps, including the cross-cutting UX patterns (blocked-action banner, consent/age chips, S4 guardrail tag, offline indicator) with accessibility basics verified. Delivers the 'fast, modern, thumb-first' UX and avoids re-styling per surface (ADR-0006).

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

- Stack: Shared design system
- Architecture decisions: [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Design system / shared component library + tokens**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
