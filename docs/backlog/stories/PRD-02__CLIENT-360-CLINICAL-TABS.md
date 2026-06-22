# Client 360: clinical & visit tabs (Visits / Treatment plan / Consents & forms)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-360-CLINICAL-TABS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-360`

## Background

As a staff member, I want tabs for visit history, treatment plan and consents & forms on the client profile, so that I can review a client's clinical history and consent state in one place.
Plainly: the clinical tabs of the Client 360 profile — visit history, the treatment plan, and consents & forms. Where it fits: a follow-up to the Client 360 basic aggregation & header (PRD-02/CLIENT-360) that adds the clinical tabs on top of the header. Each reads its owning module's data via the aggregation API and respects role-based access control so Reception sees limited clinical info. It sits in Reception (PRD-02).

## How it works

The basic story provides the aggregation API and the header; this follow-up adds the clinical tabs. Tabs render visit history, the treatment plan, and consents & forms.
Each tab reads its owning module's data (visits, plan, consent/intake) via the Client 360 aggregation API and respects role-based access control (RBAC) — Reception sees limited clinical info, not the full clinical record.
Tabs deep-link into charting and follow-ups, and every clinical read is audited (C10), consistent with the basic story's audit obligations.

## Requirements

- Tabs for visit history, treatment plan and consents & forms on the client profile.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Tabs render visit history, the treatment plan, and consents & forms.
- [ ] Each reads its owning module's data via the aggregation API.
- [ ] RBAC is respected (reception sees limited clinical info, not the full clinical record).
- [ ] Tabs deep-link into charting / follow-ups and clinical reads are audited.

## UI designs / screenshots

- Prototype: Client 360 (client-360.png) — Visits, Treatment plan, and Consents & forms tabs.
- Each reads its owning module via the aggregation API; reception sees limited clinical info.
- Tabs deep-link into charting / follow-ups; clinical reads audited.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(reads CLIENT-360 aggregation)** — Visits, Treatment plan, Consents & forms (owned by PRD-04/05/03)
  - _Presentation over the aggregation API; RBAC limits reception's clinical view; reads audited (C10)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Clinical & visit tabs (Visits / Treatment plan / Consents & forms)**
  Behaviour: tabs rendering visit history, the treatment plan, and consents & forms. Requirements: each reads its owning module's data via the aggregation API and respects RBAC (reception sees limited clinical info, not the full clinical record); deep-links into charting / follow-ups; clinical reads are audited.
