# Temperature monitor management

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/TEMP-MONITORS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web, integration
>
> **Depends on:** `PRD-04/COLD-CHAIN`

## Background

Facility, infection-control, emergency & complaints — The record-keeping that evidences AHPRA's facility, infection-control and emergency obligations, plus a complaints register with the mandated AHPRA pathway.

As a owner / staff, I want to manage temperature monitors, see their readings and act on breaches, so that cold-chain is continuously evidenced without manual logging.

The prototype's Operations → Temperature monitors (openMonitor/monitorJob) manages wireless cold-chain sensors (the ESP32 design), charts readings and raises breach jobs.

## Requirements

- To manage temperature monitors, see their readings and act on breaches.
- Traces to requirement(s): REQ-MED-7.
- Must satisfy compliance obligation(s): C13.

## Acceptance Criteria

- [ ] Monitors can be registered/provisioned per fridge/location and authenticate to the per-clinic API.
- [ ] Readings chart over time; a breach raises a job and flags affected stock.
- [ ] Missing heartbeats (dead monitor) are detected and surfaced.
- [ ] Manual fridge log (OPENCLOSE) and monitors reconcile into one cold-chain record (C13).

## UI designs / screenshots

prototype.html — Operations → Temperature monitors.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public); Ports-and-adapters integration.
Architecture decisions: ADR-0026 (see docs/adr/decision-log.md).
Depends on: PRD-04/COLD-CHAIN.

## Other

Epic: PRD-11 — Facility, infection-control, emergency & complaints.
Source PRD: docs/prds/PRD-11-facility-complaints.md.
Backlog key: PRD-11/TEMP-MONITORS.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C13.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C13); blocked path explains why.
- [ ] **Web UI** — prototype.html — Operations → Temperature monitors.
- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
