# Provider app: day schedule & open patient

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-DAY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

Apps (Flutter): client & provider — Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity.

As a injector/prescriber, I want to see my day and open a patient with consult/consent status shown before I chart, so that I work room-side with the right context and gates.

The provider sees their day and opens a patient with consult+consent status verified before charting (REQ-APP-2).

## Requirements

- To see my day and open a patient with consult/consent status shown before I chart.
- Traces to requirement(s): REQ-APP-2.

## Acceptance Criteria

- [ ] Schedule shows the practitioner's day; opening a patient shows consult+consent status.
- [ ] Provider signs in via Entra SSO, tenant-scoped.
- [ ] The consult+consent gate (PRD-03/04) is enforced before charting opens.
- [ ] Quick links to map/photos/finalise.

## UI designs / screenshots

client-app.html, treatment-room.html, checkin.html, backroom.html.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0004 (see docs/adr/decision-log.md).
Depends on: PRD-05/NOTE-TEMPLATE.

## Other

Epic: PRD-09 — Apps (Flutter): client & provider.
Source PRD: docs/prds/PRD-09-apps-client-provider.md.
Backlog key: PRD-09/PROVIDER-DAY.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
