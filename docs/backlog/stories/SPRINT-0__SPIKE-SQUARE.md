# Spike — Square AU card-on-file recurring autopay

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-SQUARE`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 2 pts  ·  **Area:** integration

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a engineer, I want a spike confirming Square AU can tokenise a card and run recurring charges with failure/dunning handling, so that the membership autopay design is viable (or an alternative is chosen early).

Membership autopay depends on Square AU supporting tokenised card-on-file recurring charges with dunning — flagged 🔬 in the docs. De-risk before committing PRD-06 memberships.

## Requirements

- A spike confirming Square AU can tokenise a card and run recurring charges with failure/dunning handling.

## Acceptance Criteria

- [ ] Prototype tokenises a test card and runs a scheduled recurring charge in Square AU sandbox.
- [ ] Failed-charge / retry behaviour observed; dunning approach outlined.
- [ ] PCI posture confirmed: no PAN stored, only provider tokens (ADR-0007).
- [ ] Go/no-go + findings recorded; feeds PRD-06 memberships.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Ports-and-adapters integration.
Architecture decisions: ADR-0007 (see docs/adr/decision-log.md).
Time-boxed spike — produce findings + a go/no-go, not production code.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/SPIKE-SQUARE.
Phase: 0 · Priority: P1 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Define spike scope, questions & success criteria** — What we must learn before building.
- [ ] **Build a throwaway prototype** — Smallest thing that answers the question.
- [ ] **Evaluate results, risks & options**
- [ ] **Write up findings + go/no-go recommendation (ADR if warranted)**
