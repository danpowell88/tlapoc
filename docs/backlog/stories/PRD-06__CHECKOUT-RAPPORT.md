# Checkout: client-rapport panel (derived from history)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CHECKOUT-RAPPORT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/CHECKOUT-ASSIST`

## Background

As a front desk, I want a one-line rapport panel at the till derived from the client's history, so that I can personalise the interaction without digging through records.
Plainly: a small read-only panel at the till that surfaces a client's preferences, recent treatments and a connection cue, to help the desk personalise. Where it fits: a follow-up to the post-visit rebooking core (PRD-06/CHECKOUT-ASSIST) that adds the rapport cue beside it. It is read-only, derived from the Client 360, with no money figures, and respects RBAC (role-based access control) — no clinical detail beyond what reception may see.

## How it works

A one-line rapport panel derived from the client record — preferences ('Natural finish · a chamomile tea on arrival'), recent treatments, and a connection cue ('Birthday in 12 days · referred by Hannah L.') — helps the desk personalise.
It is read-only, derived from the Client 360; no money figures; respects RBAC (role-based access control) — no clinical detail beyond what reception may see. This extends the post-visit rebooking core (PRD-06/CHECKOUT-ASSIST).

## Requirements

- A one-line rapport panel at the till derived from the client's history.

## Acceptance Criteria

- [ ] A one-line rapport panel shows preferences ('Natural finish · a chamomile tea on arrival'), recent treatments and a connection cue ('Birthday in 12 days · referred by Hannah L.').
- [ ] It is read-only, derived from the Client 360; no money figures.
- [ ] It respects RBAC (role-based access control) — no clinical detail beyond what reception may see.
- [ ] Empty/derived states are handled.

## UI designs / screenshots

- Prototype: Checkout client-rapport panel — preferences + recent treatments + connection cue (e.g. 'Birthday in 12 days · referred by Hannah L.').

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(derived from Client 360)** — preferences + recent treatments + connection cue
  - _No new entity; read-only; RBAC-scoped, no money figures._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Client-rapport panel (derived from history)**
  Behaviour: a one-line rapport panel derived from the client record — preferences, recent treatments and a connection cue — to help the desk personalise. Requirements: read-only, derived from the Client 360; no money figures; respects RBAC (role-based access control), no clinical detail beyond what reception may see.
