# Back-office tablet: tasks + shift-handover panels

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/BACKOFFICE-TASKS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/BACKOFFICE-TABLET`, `PRD-07/FOLLOWUPS`

## Background

As a clinic staff, I want a tasks + shift-handover panel on the bench tablet, so that the incoming shift sees outstanding work and the handover note together.
Plainly: the back-office tablet panel that shows the team's to-dos and the shift-to-shift handover note side by side. Where it fits: a follow-up to the back-office tablet basic (PRD-09/BACKOFFICE-TABLET) that adds the tasks + handover panel; it reuses the follow-ups/jobs (PRD-07) and shift-handover (PRD-11) modules rather than re-implementing them. The last handover note also appears on the hub.

## How it works

The Tasks & handover panel shows the team's to-dos / restock nudges / compliance dates (PRD-07 jobs) alongside the shift-to-shift handover note (PRD-11). It reuses PRD-07/FOLLOWUPS jobs and PRD-11/SHIFT-HANDOVER (add/read, timestamped + attributed) — no parallel store.
Outstanding jobs surface next to the handover so the incoming shift sees both together; the last handover note also appears on the hub (BACKOFFICE-TABLET). The panel is the bench-side companion to the operations web views.

## Requirements

- A tasks + shift-handover panel on the bench tablet.

## Acceptance Criteria

- [ ] The Tasks & handover panel shows the team's to-dos / restock nudges / compliance dates (PRD-07 jobs).
- [ ] It shows the shift-to-shift handover note (PRD-11), timestamped + attributed.
- [ ] Reuses PRD-07/FOLLOWUPS jobs and PRD-11/SHIFT-HANDOVER (add/read) — no parallel store.
- [ ] Outstanding jobs surface next to the handover; the last handover note also appears on the hub.

## UI designs / screenshots

- Prototype: backroom — tab Tasks & handover (to-dos / restock nudges / compliance dates + handover note).
- Outstanding jobs beside the handover; last handover note on the hub; entries timestamped + attributed.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Job/ShiftHandover** — PRD-07 jobs + PRD-11 handover — tasks + handover panels
  - _Extends BACKOFFICE-TABLET; reuses PRD-07/FOLLOWUPS + PRD-11/SHIFT-HANDOVER; no parallel store._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Tasks panel (PRD-07) + shift-handover panel (PRD-11)**
  Behaviour: the Tasks & handover panel shows the team's to-dos / restock nudges / compliance dates (PRD-07 jobs) alongside the shift-to-shift handover note (PRD-11). Requirements: reuses PRD-07/FOLLOWUPS jobs and PRD-11/SHIFT-HANDOVER (add/read, timestamped + attributed); outstanding jobs surface next to the handover so the incoming shift sees both together; the last handover note also appears on the hub.
