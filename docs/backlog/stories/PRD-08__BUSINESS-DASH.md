# Business analytics dashboards

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/BUSINESS-DASH`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`

## Background

Reporting & compliance dashboards (Governance hub) — Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack.

As a owner, I want dashboards for revenue, retention, no-shows, conversion, at-risk, big spenders and membership MRR/churn, filterable by date and practitioner, so that I can run the business on real numbers.

Revenue, retention/churn, no-shows, cancellations, conversion, at-risk, big spenders, membership MRR/churn and per-practitioner mix, date-filterable (REQ-RPT-1/2). Money figures owner-gated.

## Requirements

- Dashboards for revenue, retention, no-shows, conversion, at-risk, big spenders and membership MRR/churn, filterable by date and practitioner.
- Traces to requirement(s): REQ-RPT-1, REQ-RPT-2.

## Acceptance Criteria

- [ ] Core dashboards match the prototype's metrics on the same date range.
- [ ] Date-range presets + custom filtering; per-practitioner views.
- [ ] Reward-cost vs retention surfaces (from PRD-06).
- [ ] All money figures are gated behind the owner financial capability.

## UI designs / screenshots

prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-08/READ-MODELS.

## Other

Epic: PRD-08 — Reporting & compliance dashboards (Governance hub).
Source PRD: docs/prds/PRD-08-reporting-compliance.md.
Backlog key: PRD-08/BUSINESS-DASH.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
