# In-app notification centre

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/NOTIFICATIONS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`, `PRD-07/CHANNELS`

## Background

As a staff member, I want an in-app notification centre for events relevant to my role, so that I don't miss time-sensitive things.
The header bell + badges imply an in-app notification surface for alerts (new bookings, failed payments, expiries, AE/recall, jobs assigned).

## How it works

An in-app notification centre surfacing role-relevant events (new bookings, failed payments, expiries, AE/recall, job assignment) with read/unread state + a badge count per user; each notification deep-links to its source. In-app is one delivery target of INotifier (PRD-07).
So time-sensitive things aren't missed.

## Requirements

- An in-app notification centre for events relevant to my role.

## Acceptance Criteria

- [ ] Notifications surface role-relevant events (bookings, failed payments, expiries, AE/recall, job assignment).
- [ ] Read/unread state and a badge count are maintained per user.
- [ ] Each notification deep-links to its source.
- [ ] Channels are consistent with PRD-07 (in-app is one delivery target of INotifier).

## UI designs / screenshots

_Prototype screen: prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip)._

- Prototype: the header bell + badge (dashboard.png) -> a notification list; each item deep-links to its source.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **Notification** — id, tenant_id, user_id, kind, source_ref, read(bool), at
  - _Per-user; in-app channel of INotifier._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Web UI** — prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).
