# Practitioner scorecard

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/SCORECARD`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/BUSINESS-DASH`

## Background

Reporting & compliance dashboards (Governance hub) — Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack.

As a owner, I want a per-practitioner scorecard, so that I can coach the team and see who drives retention.

The prototype's Reports → Scorecard view shows per-practitioner performance (revenue, retention, rebooking, utilisation, outcomes).

## Requirements

- A per-practitioner scorecard.
- Traces to requirement(s): REQ-RPT-1, REQ-RPT-2.

## Acceptance Criteria

- [ ] Scorecard shows per-practitioner revenue, retention/rebooking, utilisation and outcome/revision signals.
- [ ] Date-filterable; financial figures are owner-gated.
- [ ] Drills into the underlying clients/appointments.
- [ ] Reads from the reporting read-models (PRD-08/READ-MODELS).

## UI designs / screenshots

prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-08/BUSINESS-DASH.

## Other

Epic: PRD-08 — Reporting & compliance dashboards (Governance hub).
Source PRD: docs/prds/PRD-08-reporting-compliance.md.
Backlog key: PRD-08/SCORECARD.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
