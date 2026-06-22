# Automations: per-treatment-type editing

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/AUTOMATIONS-PER-TREATMENT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/AUTOMATIONS`

## Background

As a owner / front desk, I want to edit each automation per treatment type, so that different treatments get the right cadence and content.
Plainly: let each automation be tuned per treatment type, so a filler client and a skin client get the right cadence and content (e.g. recall at ~12 weeks for anti-wrinkle vs a different interval for filler). Where it fits: a follow-up to the automations core (PRD-07/AUTOMATIONS), which toggles automations on/off; this adds per-treatment editing of the linked Sequence. Editing changes the linked Sequence's steps/offsets/templates; owner/front-desk gated.

## How it works

Each automation can be edited per treatment type so a filler client and a skin client get the right cadence/content (e.g. Recall — anti-wrinkle ~12 wks vs a different interval for filler). This extends the automations core (PRD-07/AUTOMATIONS).
Editing changes the linked Sequence's steps/offsets/templates (PRD-07/REMINDERS-CARE); changes are owner/front-desk gated; the default set matches the prototype cards (Recall, Aftercare, Win-back, Birthday, No-show follow-up, Review request).

## Requirements

- To edit each automation per treatment type.

## Acceptance Criteria

- [ ] Each automation can be edited per treatment type (e.g. Recall — anti-wrinkle ~12 wks vs a different interval for filler).
- [ ] Editing changes the linked Sequence's steps/offsets/templates (PRD-07/REMINDERS-CARE).
- [ ] Changes are owner/front-desk gated.
- [ ] The default set matches the prototype cards (Recall, Aftercare, Win-back, Birthday, No-show follow-up, Review request).

## UI designs / screenshots

- Prototype: Comms -> Automations — per-treatment editing of each automation card (cadence/content per treatment type).

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **Automation (extends PRD-07/AUTOMATIONS)** — per-treatment_type editing of the linked Sequence steps/offsets/templates
  - _No new entity; edits the linked Sequence (PRD-07/REMINDERS-CARE)._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Per-treatment-type editing of automations**
  Behaviour: each automation can be edited per treatment type (e.g. Recall — anti-wrinkle ~12 wks vs a different interval for filler). Requirements: editing changes the linked Sequence's steps/offsets/templates (PRD-07/REMINDERS-CARE); owner/front-desk gated; the default set matches the prototype cards.
