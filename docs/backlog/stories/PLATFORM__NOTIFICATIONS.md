# In-app notification centre

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/NOTIFICATIONS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`, `PRD-07/CHANNELS`

## Background

Platform shell, navigation & cross-cutting UX — The cross-cutting product surfaces the prototype exercises that don't belong to a single feature PRD: the app shell + collapsible workspace navigation, the role-tailored Today dashboard, global search, the in-app notification centre, the clinic switcher, the persona/active-role + scope-of-practice display, and the owner-only financial (.fin) gating that hides money figures from non-owner roles.

As a staff member, I want an in-app notification centre for events relevant to my role, so that I don't miss time-sensitive things.

The header bell + badges imply an in-app notification surface for alerts (new bookings, failed payments, expiries, AE/recall, jobs assigned).

## Requirements

- An in-app notification centre for events relevant to my role.
- Traces to requirement(s): REQ-NOTIF-1.

## Acceptance Criteria

- [ ] Notifications surface role-relevant events (bookings, failed payments, expiries, AE/recall, job assignment).
- [ ] Read/unread state and a badge count are maintained per user.
- [ ] Each notification deep-links to its source.
- [ ] Channels are consistent with PRD-07 (in-app is one delivery target of INotifier).

## UI designs / screenshots

prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PLATFORM/APP-NAV, PRD-07/CHANNELS.

## Other

Epic: PLATFORM — Platform shell, navigation & cross-cutting UX.
Source PRD: docs/ux/README.md.
Backlog key: PLATFORM/NOTIFICATIONS.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
