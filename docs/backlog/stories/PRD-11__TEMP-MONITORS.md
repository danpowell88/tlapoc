# Temperature monitor management

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/TEMP-MONITORS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web, integration
>
> **Depends on:** `PRD-04/COLD-CHAIN`

## Background

As a owner / staff, I want to manage temperature monitors, see their readings and act on breaches, so that cold-chain is continuously evidenced without manual logging.
The prototype's Operations → Temperature monitors (openMonitor/monitorJob) manages wireless cold-chain sensors (the ESP32 design), charts readings and raises breach jobs.

## How it works

Manage wireless cold-chain sensors (the ESP32 design): register/provision monitors per fridge/location authenticating to the per-clinic API, chart readings over time, and raise breach jobs; detect missing heartbeats (dead monitor). Manual fridge log (OPENCLOSE) and monitors reconcile into one cold-chain record (C13).
Continuous, evidenced cold-chain without manual logging.

## Requirements

- To manage temperature monitors, see their readings and act on breaches.
- Compliance: [C13](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Monitors can be registered/provisioned per fridge/location and authenticate to the per-clinic API.
- [ ] Readings chart over time; a breach raises a job and flags affected stock.
- [ ] Missing heartbeats (dead monitor) are detected and surfaced.
- [ ] Manual fridge log (OPENCLOSE) and monitors reconcile into one cold-chain record (C13).

## UI designs / screenshots

_Prototype screen: prototype.html — Operations → Temperature monitors._

- Prototype: Operations -> Temperature monitors (ops-monitors.png) — monitor list per fridge, live/charted temps, breach alerts, dead-monitor detection (openMonitor/monitorJob).

![ops-monitors — prototype screen](../screens/ops-monitors.png)

## Suggested data model

- **Monitor** — id, tenant_id, location_id, fridge, api_key_ref, last_heartbeat, status
  - _ESP32; missing heartbeat -> alert._
- **(reuses) TempLog/Excursion** — (PRD-04 COLD-CHAIN)
  - _Manual + device readings reconcile._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Monitor — id, tenant_id, location_id, fridge, api_key_ref, last_heartbeat, status (ESP32; missing heartbeat -> alert.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Enforce compliance gate + audit events**
  Enforce C13 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Integration adapter, sync & config**
  Implement the provider behind its swappable port:
  - Connection/config (OAuth tokens stored encrypted) + the field mapping this story needs.
  - Trigger on the relevant event; idempotent sync with retries, back-off and a visible reconciliation/status.
  - Handle partial failures + replays; surface errors to the user.
  - Residency: AU-resident or APP-8-assessed + consented before any PII leaves (C21).
- [ ] **Web UI**
  Build on the Angular web app: the ops-monitors per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Operations -> Temperature monitors (ops-monitors.png) — monitor list per fridge, live/charted temps, breach alerts, dead-monitor detection (openMonitor/monitorJob).
