# Immutable finalisation & audited amendments

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/IMMUTABILITY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-05/MAPPING`

## Background

As a injector, I want my finalised note to be locked, with later changes added as visible audited amendments, so that the clinical record is trustworthy and tamper-evident.
Finalisation and amendments: once a treatment note is finalised it is locked, and any later correction is an attributed, audited amendment that preserves the original. The trust backbone of PRD-05 charting on the clinic-first spine after the S4 (Schedule 4 'Prescription Only Medicine') moat (PRD-04); it depends on the injection map (MAPPING) — finalising locks the note and deducts stock — and is depended on by the offline queue (OFFLINE) and adverse-event capture (ADVERSE-EVENT). A finalised note is locked; any later change is an appended, audited amendment preserving the original (REQ-CLIN-4, ADR-0010).

## How it works

As an injector, I want my finalised note to be locked, with later changes added as visible audited amendments, so that the clinical record is trustworthy and tamper-evident.
Immutability is what makes the clinical record stand up in an Australian Health Practitioner Regulation Agency (AHPRA) or Therapeutic Goods Administration (TGA) inspection: once a treatment is finalised, the note can never be silently edited. Any later correction is an appended, audited amendment that preserves the original, so the record shows exactly what was charted at the time and what was changed afterwards, by whom and why.
Finalisation happens server-side, not in the UI. The finalise command runs the close-out (aftercare · recall · 2-day wellbeing call · adverse-event prompt), locks the ChartEntry (status=final, locked=true, finalised_at, author), and — for toxin — triggers the lot deduction + register link from MAPPING in the same transaction. After that, every field of the original note is read-only.
A post-finalise change creates an Amendment: a new linked, append-only entry capturing the author, timestamp, a required reason, and the delta/payload. The original ChartEntry is never mutated; the amendment trail is rendered beneath the locked note so a reader sees the full history. Amendments themselves are immutable and audited (ADR-0010).
Because finalisation is server-side, an offline draft (OFFLINE) can only be finalised once it has synced — the UI keeps 'Finalise' disabled until the draft is on the server, so two devices can never both finalise the same entry. The whole chain (draft edits, finalise, amendments) emits AuditEvents into the append-only audit stream.
Oversight roles (e.g. owner) get a read-only view of finalised notes + their amendment trail; they can review but never edit or finalise.

## Requirements

- My finalised note to be locked, with later changes added as visible audited amendments.

## Acceptance Criteria

- [ ] A finalised note cannot be edited; the API rejects any mutation of a locked ChartEntry.
- [ ] An amendment creates a new linked, audited entry (author, timestamp, required reason, delta) that preserves the original; amendments are themselves immutable.
- [ ] Finalisation happens server-side and is idempotent; an unsynced offline draft cannot be finalised.
- [ ] The finalise close-out captures aftercare, recall, the 2-day wellbeing call and any adverse event before checkout.
- [ ] Finalised notes render read-only with the amendment trail; oversight roles can review but not edit.

## UI designs / screenshots

- 'Finalise & checkout' button with the helper 'Finalising locks the note and deducts the units used from the selected lot in Stock.'
- Close-out modal: a summary line ('Note locked & saved ✓ · 28U deducted from lot B2245') and toggles for recall (rebook ~12 wks) + the aftercare check-in call (+2 days) that project follow-up Jobs (closeoutGo).
- Read-only oversight view for non-editors (the 'Read-only view' chip + read-only point detail) — owner can review charts but not edit or finalise.
- New vs the prototype (build these): the amendment composer (reason required), the rendered amendment trail beneath the locked note, and 'Finalise' disabled until an offline draft has synced.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry (extended)** — + status (draft|final), locked (bool), finalised_at, finalised_by
  - _No field edit after final; the API rejects mutations of a locked entry._
- **Amendment** — id, chart_entry_id (FK), author_id, created_at, reason (required), payload (the delta/added content)
  - _Append-only; original preserved; itself immutable and audited (ADR-0010)._
- **AuditEvent (referenced)** — actor, action (finalise|amend), chart_entry_id, at, detail
  - _Append-only audit stream for the finalise + every amendment._

## Technical notes (high level)

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Immutability model + finalise/amendment migrations**
  EF Core: extend ChartEntry with status/locked/finalised_at/finalised_by; add Amendment (chart_entry_id FK, author, created_at, required reason, payload delta) as an append-only table. Enforce immutability at the data layer where possible (no UPDATE on a locked row) and back it with an AuditEvent stream. tenant_id + Row-Level Security (RLS, the per-tenant database isolation) throughout.
- [ ] **Server-side finalise + amendment API**
  Finalise command (server-side, idempotent): run the close-out (aftercare/recall/wellbeing-call/adverse event (AE) prompt), lock the entry, and for toxin trigger MAPPING's transactional lot deduction + register link. Reject finalising an unsynced draft. Amendment command requires a reason, creates a linked append-only entry, never mutates the original, and rejects any direct edit of a locked entry. Emit finalise + amend AuditEvents (ADR-0010); publish OpenAPI.
- [ ] **Finalise close-out + read-only/amendment UI**
  Build the close-out modal (summary + recall/wellbeing-call toggles that project follow-up Jobs), the locked read-only rendering of a finalised note, the amendment composer (reason required) and the rendered amendment trail. Keep 'Finalise' disabled until an offline draft has synced. Provide the oversight read-only view (review, no edit/finalise). Wire to the API with clear blocked-action reasons; capability-gate edit vs review.
