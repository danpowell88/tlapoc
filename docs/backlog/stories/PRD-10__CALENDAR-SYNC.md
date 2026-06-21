# Two-way calendar sync (M365 / Google)

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/CALENDAR-SYNC`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

Integrations: Xero & calendar — Outbound integrations that remove double-entry: push sales/payments to Xero, and keep appointments in sync with staff calendars (M365 / Google)

As a practitioner, I want my appointments to appear in Outlook/Google and external busy-time to block my availability, so that I have one source of truth for my time.

Appointments sync both ways with Outlook/Google; external busy events block availability, behind ICalendarProvider (REQ-INT-2).

## Requirements

- My appointments to appear in Outlook/Google and external busy-time to block my availability.
- Traces to requirement(s): REQ-INT-2.

## Acceptance Criteria

- [ ] Creating/moving/cancelling an appointment reflects in the linked Outlook/Google calendar and vice-versa.
- [ ] External busy events block availability in booking (PRD-02).
- [ ] Per-staff opt-in and conflict-resolution rules (open question) supported.
- [ ] Implemented behind ICalendarProvider (swappable).

## UI designs / screenshots

prototype.html — Settings → Integrations.

## Technical notes (high level)

Stack: Ports-and-adapters integration.
Architecture decisions: ADR-0012 (see docs/adr/decision-log.md).
Depends on: PRD-02/CALENDAR.

## Other

Epic: PRD-10 — Integrations: Xero & calendar.
Source PRD: docs/prds/PRD-10-integrations.md.
Backlog key: PRD-10/CALENDAR-SYNC.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
