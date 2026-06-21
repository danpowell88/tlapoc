# Design system / shared component library + tokens

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/DESIGN`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** design

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a designer/developer, I want a shared set of design tokens and core components (buttons, inputs, banners, the blocked-action banner, chips, tables), so that all surfaces look consistent and the compliance UX patterns are reusable.

One design system (tokens, components) shared across web and the two Flutter apps delivers the 'fast and modern, thumb-first' UX the docs demand and avoids re-styling per surface.

## Requirements

- A shared set of design tokens and core components (buttons, inputs, banners, the blocked-action banner, chips, tables).

## Acceptance Criteria

- [ ] Tokens (colour, type, spacing) defined once and consumed by web + Flutter.
- [ ] Core components include the cross-cutting patterns from UX §4 (blocked-action banner, consent/age chips, S4 guardrail tag, offline indicator).
- [ ] Components are documented in a simple gallery/storybook.
- [ ] Accessibility basics (contrast, focus, hit-target size) verified for core components.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Shared design system.
Architecture decisions: ADR-0006 (see docs/adr/decision-log.md).

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/DESIGN.
Phase: 0 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Design system / shared component library + tokens**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
