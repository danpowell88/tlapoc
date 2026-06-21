# Inspection-readiness pack & governance hub

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/INSPECTION-PACK`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/COMPLIANCE-DASH`

## Background

Reporting & compliance dashboards (Governance hub) — Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack.

As a owner, I want a one-click pack that assembles the evidence an inspector would ask for, so that we're always inspection-ready.

A one-click inspection-readiness pack and the cross-case Governance hub (policies sign-off, waste manifests/IPC, DSAR + breach drill) (REQ-RPT-7, ADR-0030, REQ-SEC-8/9).

## Requirements

- A one-click pack that assembles the evidence an inspector would ask for.
- Traces to requirement(s): REQ-RPT-7, REQ-SEC-8, REQ-SEC-9.
- Must satisfy compliance obligation(s): C10.

## Acceptance Criteria

- [ ] The pack assembles consent coverage, the S4 register, registration/insurance status, IPC/waste logs and registers.
- [ ] Policies & procedures sign-off is tracked in the hub.
- [ ] DSAR (APP 12/13) and a breach drill are runnable from the hub.
- [ ] Pack generation is audited.

## UI designs / screenshots

prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0030 (see docs/adr/decision-log.md).
Depends on: PRD-08/COMPLIANCE-DASH.

## Other

Epic: PRD-08 — Reporting & compliance dashboards (Governance hub).
Source PRD: docs/prds/PRD-08-reporting-compliance.md.
Backlog key: PRD-08/INSPECTION-PACK.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C10.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C10); blocked path explains why.
- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
