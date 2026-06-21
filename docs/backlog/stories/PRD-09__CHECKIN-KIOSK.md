# Reception self-check-in surface (tablet)

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CHECKIN-KIOSK`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/LIFECYCLE`, `PRD-03/GATING`

## Background

Apps (Flutter): client & provider — Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity.

As a client arriving for a visit, I want to check myself in on the reception tablet, so that the team knows I've arrived and I complete anything outstanding.

The prototype's checkin surface is a reception-desk tablet where clients check themselves in (confirm details, complete any outstanding intake/consent), updating the Today board.

## Requirements

- To check myself in on the reception tablet.
- Traces to requirement(s): REQ-BOOK-4.

## Acceptance Criteria

- [ ] A client can self-check-in (verify identity/appointment) on a shared tablet surface.
- [ ] Outstanding intake/consent is prompted and completable at check-in.
- [ ] Check-in updates the visit lifecycle/Today board (PRD-02).
- [ ] The surface is locked-down (no access to other clients' data) and times out between clients.

## UI designs / screenshots

checkin.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-02/LIFECYCLE, PRD-03/GATING.

## Other

Epic: PRD-09 — Apps (Flutter): client & provider.
Source PRD: docs/prds/PRD-09-apps-client-provider.md.
Backlog key: PRD-09/CHECKIN-KIOSK.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C10.

## Tasks (dev pickup)

- [ ] **Web UI** — checkin.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
