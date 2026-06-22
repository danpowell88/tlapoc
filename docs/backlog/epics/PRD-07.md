# PRD-07 — Communications, reminders & recall

> **Stage / Milestone:** M4 · Commerce, comms & integrations (PRD-06, PRD-07, PRD-10)  ·  **Phase:** 1  ·  **Stories:** 22

The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in. Advertising content is produced in the clinic's external tools; the platform has no advertising linter, and the public booking page uses generic names with S4 prices withheld by configuration.

**Source PRD:** `docs/prds/PRD-07-comms-reminders-recall.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `CHANNELS` | [Notification channels (SMS / email / push)](../stories/PRD-07__CHANNELS.md) | Story | P0 | 5 | 3 |
| `REMINDERS-CARE` | [Appointment reminders & confirmations — basic sequence (core)](../stories/PRD-07__REMINDERS-CARE.md) | Story | P1 | 3 | 2 |
| `PRECARE` | [Pre-care instruction sequences (per treatment type)](../stories/PRD-07__PRECARE.md) | Story | P2 | 2 | 1 |
| `AFTERCARE` | [Aftercare instruction sequences (day-0 + day-3, per treatment type)](../stories/PRD-07__AFTERCARE.md) | Story | P2 | 2 | 1 |
| `RECALL` | [Recall / recare worklist](../stories/PRD-07__RECALL.md) | Story | P1 | 3 | 2 |
| `MARKETING-CONSENT` | [Marketing consent & functional unsubscribe (Spam Act)](../stories/PRD-07__MARKETING-CONSENT.md) | Story | P1 | 3 | 3 |
| `BOOKING-PAGE` | [Public booking page: schedule-driven generic names & withheld S4 prices (core)](../stories/PRD-07__BOOKING-PAGE.md) | Story | P1 | 3 | 3 |
| `BOOKING-PAGE-SETTINGS` | [Public booking page: Settings config screen + live preview](../stories/PRD-07__BOOKING-PAGE-SETTINGS.md) | Story | P2 | 2 | 1 |
| `FOLLOWUPS` | [Unified follow-up / job queue — projected signals + lifecycle (core)](../stories/PRD-07__FOLLOWUPS.md) | Story | P2 | 2 | 3 |
| `FOLLOWUPS-FLAG` | [Follow-ups: manual flag → Job](../stories/PRD-07__FOLLOWUPS-FLAG.md) | Story | P2 | 2 | 1 |
| `FOLLOWUPS-AUTOCAT` | [Follow-ups: rules/keyword auto-categorisation (no AI)](../stories/PRD-07__FOLLOWUPS-AUTOCAT.md) | Story | P2 | 2 | 1 |
| `INBOX` | [Omnichannel inbox + lead/reviews (placeholder)](../stories/PRD-07__INBOX.md) | Story | P2 | 1 | 1 |
| `AUTOMATIONS` | [Automation builder — toggleable automations + consent split (core)](../stories/PRD-07__AUTOMATIONS.md) | Story | P2 | 2 | 3 |
| `AUTOMATIONS-PER-TREATMENT` | [Automations: per-treatment-type editing](../stories/PRD-07__AUTOMATIONS-PER-TREATMENT.md) | Story | P2 | 2 | 1 |
| `AUTOMATIONS-STATS` | [Automations: live stats (sent / booked / returned)](../stories/PRD-07__AUTOMATIONS-STATS.md) | Story | P2 | 2 | 1 |
| `REVIEWS` | [Reviews & reputation — request-all, reply/acknowledge/flag + S4 caution (core)](../stories/PRD-07__REVIEWS.md) | Story | P2 | 1 | 3 |
| `REVIEWS-AUTODETECT` | [Reviews: auto-detect negative reviews / complaint keywords → Job](../stories/PRD-07__REVIEWS-AUTODETECT.md) | Story | P2 | 2 | 1 |
| `REVIEWS-SCREEN-KPI` | [Reviews: screen UI + reputation KPIs](../stories/PRD-07__REVIEWS-SCREEN-KPI.md) | Story | P2 | 2 | 1 |
| `LEADS-CRM` | [Lead / prospect CRM — pipeline, stages & convert (core)](../stories/PRD-07__LEADS-CRM.md) | Story | P2 | 1 | 3 |
| `LEADS-NUDGES` | [Leads: consent-gated outbound nudges (1:1 replies exempt, C23)](../stories/PRD-07__LEADS-NUDGES.md) | Story | P2 | 2 | 1 |
| `LEADS-KPI-FOLLOWUPS` | [Leads: conversion KPIs + Follow-ups queue projection](../stories/PRD-07__LEADS-KPI-FOLLOWUPS.md) | Story | P2 | 2 | 1 |
| `CAMPAIGNS` | [Campaigns (external-tool handoff) (placeholder)](../stories/PRD-07__CAMPAIGNS.md) | Story | P2 | 1 | 1 |

_Totals: 22 stories · 38 tasks._
