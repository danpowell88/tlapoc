# App distribution & code-push posture

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/APP-DISTRIBUTION`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app, provider-app
>
> **Depends on:** `SPRINT-0/FLUTTER`

## Background

Apps (Flutter): client & provider — Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity.

As a mobile developer, I want a store-distribution and (where viable) code-push pipeline for both apps, so that we can ship and patch the apps responsibly.

Store distribution + code-push (e.g. Shorebird) where the compliance posture allows (open question) (ADR-0006).

## Requirements

- A store-distribution and (where viable) code-push pipeline for both apps.
- Traces to requirement(s): REQ-APP-1, REQ-APP-2.

## Acceptance Criteria

- [ ] Both apps distribute via internal/store channels from CI.
- [ ] Code-push viability for the compliance posture is assessed and documented.
- [ ] Versioning + minimum-supported-version handling in place.
- [ ] Crash/usage telemetry feeds observability.

## UI designs / screenshots

client-app.html, treatment-room.html, checkin.html, backroom.html.

## Technical notes (high level)

Stack: Flutter client app; Flutter provider app.
Architecture decisions: ADR-0006 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/FLUTTER.

## Other

Epic: PRD-09 — Apps (Flutter): client & provider.
Source PRD: docs/prds/PRD-09-apps-client-provider.md.
Backlog key: PRD-09/APP-DISTRIBUTION.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Client app UI (Flutter)**
- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
