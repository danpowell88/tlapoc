# In-app notification centre

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/NOTIFICATIONS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`

## Background

As a staff member, I want an in-app notification centre for events relevant to my role, so that I don't miss time-sensitive things.
Plainly: the header bell and the in-app list of alerts relevant to a person's role — new bookings, failed payments, expiries, safety actions and assigned jobs. It is built on the app shell and the comms channels. In-app is just one delivery target of the same notifier that sends SMS and email, so the channels stay consistent rather than being a separate pipe. The header bell + badges imply an in-app notification surface for alerts (new bookings, failed payments, expiries, AE (adverse event — an unwanted medical occurrence after treatment)/recall, jobs assigned).

## How it works

The header bell + badge implies an in-app notification centre (prototype header notifications icon with the rose dot). It surfaces role-relevant events so time-sensitive things aren't missed: new bookings, failed payments, credential/stock expiries (REG-WATCH), adverse-event/recall actions, and job assignments (ADR-0023).
In-app is one delivery target of the INotifier (the shared notification port that fans out SMS, email and in-app) port (ADR-0012, PRD-07) — the same event that goes out as SMS/email can also drop an in-app notification; channels stay consistent rather than this being a separate bespoke pipe. Each notification carries read/unread state and a per-user badge count, and deep-links to its source (the booking, the failed invoice, the credential, the assigned job).
Targeting is per-user and role-relevant (concern-driven, ADR-0017) — a payment-failure notification goes to roles that handle money/front-desk, a credential expiry to Lead/owner, not to everyone. Read state is per-user (two people seeing the same clinic event each track their own read/unread).
Edge cases: clearing/marking-read updates the badge immediately; a notification whose source the role can no longer access (e.g. after a role switch) degrades gracefully; high-volume events are coalesced rather than flooding the bell.

## Requirements

- An in-app notification centre for events relevant to my role.

## Acceptance Criteria

- [ ] Notifications surface role-relevant events (bookings, failed payments, expiries, AE/recall, job assignment).
- [ ] Read/unread state and a badge count are maintained per user.
- [ ] Each notification deep-links to its source.
- [ ] Channels are consistent with PRD-07 (in-app is one delivery target of INotifier).

## UI designs / screenshots

_Prototype screen: prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip)._

- Prototype: the header bell + badge (dashboard.png) -> a notification list panel; each item shows the event, time and read/unread state and deep-links to its source.
- Per-user read/unread + badge count; role-relevant targeting; consistent with PRD-07 channels (in-app is one INotifier target).

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **Notification** — id, tenant_id, user_id, kind(booking|payment_failed|expiry|ae_recall|job_assigned), source_ref, read(bool), at
  - _Per-user; in-app channel of INotifier (PRD-07); deep-links via source_ref; read state per user._

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Notification model + in-app channel of INotifier**
  Model Notification (per-user, tenant_id + RLS) with kind, source_ref, read state and timestamp. Implement the in-app delivery target of the INotifier (the shared notification port that fans out SMS, email and in-app) port (ADR-0012/PRD-07) so domain events (new booking, failed payment, expiry from REG-WATCH, AE (adverse event — an unwanted medical occurrence after treatment)/recall, job assignment from ADR-0023) fan out to in-app consistently with SMS/email. Target per-user by role relevance (concern-driven); coalesce high-volume events.
- [ ] **Read/unread + badge count API**
  Maintain per-user read/unread state and an unread badge count, with mark-read / mark-all-read that updates the count immediately. Two users seeing the same clinic event each track their own state.
- [ ] **Notification centre UI (header bell + list, deep-linking)**
  Build the header bell + badge and the notification list panel (dashboard.png): each item shows event/time/read-state and deep-links to its source (booking, invoice, credential, assigned job). A source the active role can no longer access degrades gracefully. Loading/empty states.
