# Policies & procedures sign-off

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/POLICIES`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/INSPECTION-PACK`

## Background

Reporting & compliance dashboards (Governance hub) — Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack.

As a owner / compliance officer, I want to publish policies and track staff sign-off, so that I can evidence that the team has read current procedures.

The prototype's Governance → Policies screen (signPolicy) tracks staff acknowledgement/sign-off of clinic policies and procedures, part of the Governance hub.

## Requirements

- To publish policies and track staff sign-off.
- Traces to requirement(s): REQ-RPT-7.
- Must satisfy compliance obligation(s): C10, C20.

## Acceptance Criteria

- [ ] Policies are versioned and published to relevant roles.
- [ ] Staff sign-off is recorded per policy version with date; outstanding sign-offs surface.
- [ ] Sign-off status is included in the inspection-readiness pack.
- [ ] Changes to a policy require re-acknowledgement.

## UI designs / screenshots

prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0030 (see docs/adr/decision-log.md).
Depends on: PRD-08/INSPECTION-PACK.

## Other

Epic: PRD-08 — Reporting & compliance dashboards (Governance hub).
Source PRD: docs/prds/PRD-08-reporting-compliance.md.
Backlog key: PRD-08/POLICIES.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C10, C20.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C10, C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
