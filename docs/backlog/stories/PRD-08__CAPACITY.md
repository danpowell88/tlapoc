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

- [ ] **Capacity KPI tiles (overall utilisation + idle capacity)**
  Behaviour: a row of headline tiles for overall chair utilisation and idle capacity over the selected window. Requirements: utilisation = booked vs available minutes from the read-models; idle capacity is shown as hours (the dollar value of idle time lives on the scorecard, not here); operational metric only, no money figures; shares the Reports date presets.
- [ ] **Utilisation by practitioner and by resource (overview)**
  Behaviour: the overview sub-view shows utilisation by practitioner and by room/chair/device as tiles/bars. Requirements: available time per resource comes from the roster (PRD-01 ROSTER) and resource definitions (PRD-11 ROOMS-DEVICES), booked time from appointments; bars make under-used resources obvious; reads the read-models, never OLTP.
- [ ] **Utilisation trends sub-view (time series)**
  Behaviour: the trends sub-view (goRepSub 'trends') plots utilisation over time so the owner can see direction, not just a snapshot. Requirements: time-series query over the capacity projection for the selected resources/window; consistent with the overview totals; operational only.
- [ ] **Quiet-window highlight + hand-off to waitlist / recall fill**
  Behaviour: highlight recurring low-utilisation windows (e.g. 'Wed runs at just 63% utilisation') and offer a hand-off to fill them. Requirements: the same quiet-window data feeds the Reception waitlist (PRD-02 WAITLIST) and recall (PRD-07 RECALL) fill loop; the hand-off creates the matching follow-up action; quiet-window detection is configurable (threshold + horizon).
- [ ] **Read-model / projection: capacity & utilisation**
  Behaviour: project CapacityMetrics = booked vs available minutes by practitioner, room/chair and device over a window, computing utilisation and detecting quiet windows (recurring low-utilisation slots). Requirements: available time from roster (PRD-01 ROSTER) + resource definitions (PRD-11 ROOMS-DEVICES), booked time from appointments; support overview + trend (time-series) queries over the read schema; eventual consistency acceptable; operational, no money.
