# Quiet windows: one-click fill (recall / waitlist / campaign)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/QUIET-WINDOWS-FILL`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/QUIET-WINDOWS`

## Background

As a front-of-house lead, I want to fill a quiet window in one click via recall, a waitlist offer or a targeted campaign, so that the chair gets booked before it sits idle.
Plainly: the action that turns a quiet window into a booking attempt — a one-click choice of recall, a waitlist offer, or a small targeted campaign. Where it fits: a follow-up to the quiet-windows basic detection (PRD-02/QUIET-WINDOWS) that adds the fill action on top of the window list. The fill hands off to existing channels: it creates follow-up jobs handled by Comms (PRD-07) and honours each client's marketing-consent state. It sits in the Reception schedule (PRD-02).

## How it works

The basic panel detects and lists quiet windows; this follow-up adds the action that fills them. A one-click control offers three routes — a recall worklist entry, a waitlist offer to a waiting client, or a small targeted campaign — each handed off to existing channels rather than re-built here.
Each route becomes a follow-up job in the PRD-07 queue and honours the client's marketing-consent state (a campaign never goes to someone who hasn't consented). The window itself is unchanged; this is the demand-side action layered on top.
Every fill records a FillAction (which window, which kind, which job it created, who and when) so the desk has an audit of what was done to fill each window.

## Requirements

- To fill a quiet window in one click via recall, a waitlist offer or a targeted campaign.

## Acceptance Criteria

- [ ] A one-click fill action offers recall, a waitlist offer or a targeted campaign.
- [ ] The action creates the matching follow-up jobs (PRD-07).
- [ ] It honours each client's marketing-consent state.
- [ ] Each fill records a FillAction for audit.

## UI designs / screenshots

- A Fill affordance per quiet-window card opening a small chooser: recall / waitlist offer / targeted campaign.
- Choosing a route creates the matching follow-up job and confirms it; a campaign route respects marketing consent.
- The fill is recorded against the window (FillAction) for audit.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **FillAction** — id, quiet_window_ref, kind(recall|waitlist|campaign), created_job_id, actor_id, at
  - _Audit of what was done to fill a window; the created job is owned by Comms (PRD-07)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **One-click fill (recall / waitlist offer / campaign) + FillAction**
  Behaviour: a one-click action to fill a window via the recall worklist, a waitlist offer, or a small targeted campaign. Requirements: creates the matching follow-up jobs (PRD-07); honours each client's marketing-consent state; records a FillAction (window, kind, created job, actor, at) for audit.
