# PRD-02 — Booking & scheduling (+ client/CRM basics)

> **Stage / Milestone:** M2 · Booking, CRM, intake & consent (PRD-02, PRD-03)  ·  **Phase:** 1  ·  **Stories:** 15

The calendar that runs the front desk and the 360° client record everything hangs off. Bookings are scope-aware (only cleared RN/NP can be booked for injectables) and an injectable booking is gated so it can't proceed to charting without a consult. Includes online self-booking, the visit lifecycle, reminders/reschedule/cancel, waitlist, walk-ins, resources and the client directory.

**Source PRD:** `docs/prds/PRD-02-booking-scheduling.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `CALENDAR` | [Multi-resource calendar (practitioner + room)](../stories/PRD-02__CALENDAR.md) | Story | P0 | 5 | 6 |
| `QUIET-WINDOWS` | [Quiet windows to fill (idle-slot recovery)](../stories/PRD-02__QUIET-WINDOWS.md) | Story | P1 | 3 | 4 |
| `ONLINE-BOOK` | [Online self-booking (scope-aware)](../stories/PRD-02__ONLINE-BOOK.md) | Story | P0 | 5 | 6 |
| `CONSULT-GATE` | [Consult gate on injectable appointments](../stories/PRD-02__CONSULT-GATE.md) | Story | P0 | 5 | 3 |
| `LIFECYCLE` | [Visit lifecycle & status state-machine](../stories/PRD-02__LIFECYCLE.md) | Story | P1 | 3 | 5 |
| `REMINDERS` | [Reminders & self-service reschedule/cancel](../stories/PRD-02__REMINDERS.md) | Story | P1 | 3 | 4 |
| `WAITLIST` | [Waitlist & cancellation backfill](../stories/PRD-02__WAITLIST.md) | Story | P1 | 3 | 4 |
| `WALKINS` | [Walk-ins, same-day add-ons & resources](../stories/PRD-02__WALKINS.md) | Story | P2 | 2 | 4 |
| `CLIENT-360` | [Client 360° profile](../stories/PRD-02__CLIENT-360.md) | Story | P1 | 3 | 5 |
| `PHOTOS-GALLERY` | [Before/after photo gallery (image-use-gated)](../stories/PRD-02__PHOTOS-GALLERY.md) | Story | P2 | 2 | 4 |
| `CLIENT-DIR` | [Client directory: search, filter, merge, soft-delete](../stories/PRD-02__CLIENT-DIR.md) | Story | P2 | 2 | 4 |
| `CLIENT-MERGE` | [Duplicate detection & client merge (audited, history-preserving)](../stories/PRD-02__CLIENT-MERGE.md) | Story | P2 | 2 | 3 |
| `DEPOSITS` | [Booking deposits / card-on-file hold (placeholder)](../stories/PRD-02__DEPOSITS.md) | Story | P2 | 1 | 1 |
| `BOOKING-WIZARD` | [Staff booking wizard (service → practitioner → time → client → confirm)](../stories/PRD-02__BOOKING-WIZARD.md) | Story | P1 | 3 | 5 |
| `SERVICE-CATALOGUE` | [Services & treatment-menu admin (durations, eligible roles, S4 flag)](../stories/PRD-02__SERVICE-CATALOGUE.md) | Story | P1 | 3 | 5 |

_Totals: 15 stories · 63 tasks._
