# Client 'report a concern' → follow-up / AE bridge

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-CONCERN`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-07/FOLLOWUPS`, `PRD-05/ADVERSE-EVENT`

## Background

Apps (Flutter): client & provider — Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity.

As a client, I want to report a concern after my treatment from the app, so that the clinic responds quickly if something's wrong.

The prototype's client app lets a client report a post-treatment concern, which bridges into staff follow-ups (and can escalate to an adverse event/complaint). A safety-critical client→clinic channel.

## Requirements

- To report a concern after my treatment from the app.
- Traces to requirement(s): REQ-CLIN-5, REQ-CLI-4.
- Must satisfy compliance obligation(s): C12, C24.

## Acceptance Criteria

- [ ] A client can submit a concern (with optional photo, consent-respecting) from the app.
- [ ] The concern raises a follow-up job for staff (PRD-07) with the client/treatment linked.
- [ ] Staff can call back, resolve, or escalate to an adverse event (PRD-05) / complaint (PRD-11).
- [ ] The client sees acknowledgement; the exchange is recorded and audited.

## UI designs / screenshots

client-app.html — Report a concern; prototype Follow-ups.

## Technical notes (high level)

Stack: Flutter client app.
Depends on: PRD-07/FOLLOWUPS, PRD-05/ADVERSE-EVENT.

## Other

Epic: PRD-09 — Apps (Flutter): client & provider.
Source PRD: docs/prds/PRD-09-apps-client-provider.md.
Backlog key: PRD-09/CLIENT-CONCERN.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C12, C24.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C12, C24); blocked path explains why.
- [ ] **Client app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
