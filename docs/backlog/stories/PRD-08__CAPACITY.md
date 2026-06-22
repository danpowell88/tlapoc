# Capacity & utilisation report

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/CAPACITY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`

## Background

As a owner, I want capacity and utilisation reporting, so that I can fill quiet windows and right-size rosters.
This story reports how full the clinic actually runs: utilisation by practitioner, room/chair and device over a date range, with the quiet windows highlighted so they can be filled from the waitlist or a recall. It sits in the Reporting layer (step 6 of the clinic-first build): it reads from the reporting read-models (READ-MODELS) over appointment, roster and resource data, so it depends on those. Utilisation is an operational metric, not financial — no money figures here. The prototype's Reports → Capacity view reports chair/room/practitioner utilisation and quiet windows (overview/trends).

## How it works

Capacity & utilisation reporting so the owner can fill quiet windows and right-size rosters. Computes utilisation — booked vs available time — by practitioner, by room/chair and by device, over a date range, with an overview and a trend view (goRep('capacity'), overview/trends sub-views). Reads from the reporting read-models (READ-MODELS) over appointment, roster (PRD-01 ROSTER) and resource (PRD-11 ROOMS-DEVICES) data.
Quiet windows — recurring low-utilisation slots — are highlighted so they can feed the waitlist/recall fill loop (PRD-02 WAITLIST, PRD-07 RECALL): the same data that says 'Wednesday afternoons run at 41%' is what a flash promo or waitlist offer targets. The Insights strip already surfaces this ('Wed runs at just 63% utilisation — your best slot for waitlist offers or a flash promo').
Utilisation is an operational metric, not financial — no money figures here (revenue-per-chair-hour lives on the scorecard); visible to owner/manager.

## Requirements

- Capacity and utilisation reporting.

## Acceptance Criteria

- [ ] Utilisation by practitioner, room/chair and device over a date range, with an overview and a trend view.
- [ ] Quiet windows (recurring low-utilisation slots) are highlighted to feed waitlist/recall fill.
- [ ] Reads from the reporting read-models over appointment/roster/resource data.
- [ ] Matches the prototype's capacity metrics; operational only (no money figures).

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Reports → Capacity (reports.png, goRep('capacity'), overview/trends via goRepSub) — utilisation by resource with quiet-window highlights.
- Overview: utilisation tiles/bars by practitioner, room/chair, device; Trends: utilisation over time.
- Quiet-window highlight with a hand-off into waitlist/recall fill.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) CapacityMetrics** — period, practitioner_id?/room_id?/device_id?, booked_minutes, available_minutes, utilisation, quiet_windows[]
  - _Projection over appointments + roster (PRD-01) + resources (PRD-11); feeds waitlist/recall fill; operational._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection: capacity & utilisation**
  Project CapacityMetrics = booked vs available minutes by practitioner, room/chair and device over a window, computing utilisation and detecting quiet windows (recurring low-utilisation slots). Available time comes from the roster (PRD-01 ROSTER) and resource definitions (PRD-11 ROOMS-DEVICES); booked time from appointments. Support overview + trend (time-series) queries over the read schema.
- [ ] **Web UI: capacity report (overview + trends) with quiet-window fill**
  Build the Capacity tab with overview/trends sub-views (goRepSub): utilisation by resource as tiles/bars (overview) and over time (trends), with quiet windows highlighted and a hand-off action into waitlist/recall fill (PRD-02/PRD-07). Operational metric only — no money figures.
