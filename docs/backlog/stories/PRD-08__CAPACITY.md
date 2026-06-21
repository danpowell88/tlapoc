# Capacity & utilisation report

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/CAPACITY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`

## Background

Reporting & compliance dashboards (Governance hub) — Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack.

As a owner, I want capacity and utilisation reporting, so that I can fill quiet windows and right-size rosters.

The prototype's Reports → Capacity view reports chair/room/practitioner utilisation and quiet windows (overview/trends).

## Requirements

- Capacity and utilisation reporting.
- Traces to requirement(s): REQ-RPT-1, REQ-RPT-2.

## Acceptance Criteria

- [ ] Utilisation by practitioner, room/chair and device over a date range, with trend view.
- [ ] Quiet windows are highlighted (feeds waitlist/recall fill).
- [ ] Reads from the reporting read-models.
- [ ] Matches the prototype's capacity metrics.

## UI designs / screenshots

prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-08/READ-MODELS.

## Other

Epic: PRD-08 — Reporting & compliance dashboards (Governance hub).
Source PRD: docs/prds/PRD-08-reporting-compliance.md.
Backlog key: PRD-08/CAPACITY.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
