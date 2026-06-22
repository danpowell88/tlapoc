# PRD-02 — Booking & scheduling (+ client/CRM basics)

> **Stage / Milestone:** M2 · Booking, CRM, intake & consent (PRD-02, PRD-03)  ·  **Phase:** 1  ·  **Stories:** 54

The calendar that runs the front desk and the 360° client record everything hangs off. Bookings are scope-aware (only cleared RN/NP can be booked for injectables) and an injectable booking is gated so it can't proceed to charting without a consult. Includes online self-booking, the visit lifecycle, reminders/reschedule/cancel, waitlist, walk-ins, resources and the client directory.

**Source PRD:** `docs/prds/PRD-02-booking-scheduling.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `CALENDAR` | [Multi-resource calendar — basic grid & booking](../stories/PRD-02__CALENDAR.md) | Story | P0 | 5 | 3 |
| `CALENDAR-HEADER-NAV` | [Calendar: header & date navigation](../stories/PRD-02__CALENDAR-HEADER-NAV.md) | Story | P2 | 2 | 2 |
| `CALENDAR-DAYWEEK` | [Calendar: day / week view toggle & time-axis layout](../stories/PRD-02__CALENDAR-DAYWEEK.md) | Story | P2 | 2 | 2 |
| `CALENDAR-FILTERS` | [Calendar: resource & practitioner filters](../stories/PRD-02__CALENDAR-FILTERS.md) | Story | P2 | 2 | 2 |
| `CALENDAR-DRAG` | [Calendar: drag-to-book, move & resize](../stories/PRD-02__CALENDAR-DRAG.md) | Story | P2 | 2 | 2 |
| `CALENDAR-STATUS-CARDS` | [Calendar: appointment cards, status colours & summary strip](../stories/PRD-02__CALENDAR-STATUS-CARDS.md) | Story | P2 | 2 | 2 |
| `QUIET-WINDOWS` | [Quiet windows — basic idle-slot detection & list](../stories/PRD-02__QUIET-WINDOWS.md) | Story | P1 | 3 | 2 |
| `QUIET-WINDOWS-COST` | [Quiet windows: cost-per-treatment / savings framing](../stories/PRD-02__QUIET-WINDOWS-COST.md) | Story | P2 | 2 | 1 |
| `QUIET-WINDOWS-FEFO` | [Quiet windows: stock-expiry / FEFO tie-in](../stories/PRD-02__QUIET-WINDOWS-FEFO.md) | Story | P2 | 2 | 1 |
| `QUIET-WINDOWS-FILL` | [Quiet windows: one-click fill (recall / waitlist / campaign)](../stories/PRD-02__QUIET-WINDOWS-FILL.md) | Story | P2 | 2 | 1 |
| `ONLINE-BOOK` | [Online self-booking — basic scope-aware flow](../stories/PRD-02__ONLINE-BOOK.md) | Story | P0 | 5 | 2 |
| `ONLINE-BOOK-GENERIC-NAMES` | [Online self-booking: generic names & withheld S4 prices (C9)](../stories/PRD-02__ONLINE-BOOK-GENERIC-NAMES.md) | Story | P2 | 2 | 1 |
| `ONLINE-BOOK-DOB` | [Online self-booking: DOB capture & under-18 flag](../stories/PRD-02__ONLINE-BOOK-DOB.md) | Story | P2 | 2 | 1 |
| `ONLINE-BOOK-CUSTOMISE` | [Online self-booking: owner customise & embed panel](../stories/PRD-02__ONLINE-BOOK-CUSTOMISE.md) | Story | P2 | 2 | 1 |
| `CONSULT-GATE` | [Consult gate on injectable appointments](../stories/PRD-02__CONSULT-GATE.md) | Story | P0 | 5 | 3 |
| `LIFECYCLE` | [Visit lifecycle — basic status state-machine](../stories/PRD-02__LIFECYCLE.md) | Story | P1 | 3 | 2 |
| `LIFECYCLE-BOOKING-CAPTURE` | [Visit lifecycle: booking capture (new/returning, reason, roster)](../stories/PRD-02__LIFECYCLE-BOOKING-CAPTURE.md) | Story | P2 | 2 | 1 |
| `LIFECYCLE-NOSHOW-JOB` | [Visit lifecycle: no-show flag → auto follow-up job](../stories/PRD-02__LIFECYCLE-NOSHOW-JOB.md) | Story | P2 | 2 | 1 |
| `LIFECYCLE-TODAY-BOARD` | [Visit lifecycle: Today KPI tiles & in-room strip](../stories/PRD-02__LIFECYCLE-TODAY-BOARD.md) | Story | P2 | 2 | 1 |
| `LIFECYCLE-ROW-ACTIONS` | [Visit lifecycle: per-row role-appropriate next actions](../stories/PRD-02__LIFECYCLE-ROW-ACTIONS.md) | Story | P2 | 2 | 1 |
| `REMINDERS` | [Reminders — basic scheduling & dispatch](../stories/PRD-02__REMINDERS.md) | Story | P1 | 3 | 2 |
| `REMINDERS-CONFIRM-DECLINE` | [Reminders: confirm / decline handling](../stories/PRD-02__REMINDERS-CONFIRM-DECLINE.md) | Story | P2 | 2 | 1 |
| `REMINDERS-SELF-SERVICE` | [Reminders: self-service reschedule / cancel within policy](../stories/PRD-02__REMINDERS-SELF-SERVICE.md) | Story | P2 | 2 | 1 |
| `REMINDERS-POLICY` | [Reminders: cancellation / no-show policy settings](../stories/PRD-02__REMINDERS-POLICY.md) | Story | P2 | 2 | 1 |
| `WAITLIST` | [Waitlist — basic entries & management](../stories/PRD-02__WAITLIST.md) | Story | P1 | 3 | 2 |
| `WAITLIST-MATCHING` | [Waitlist: matching / backfill engine on slot-freed](../stories/PRD-02__WAITLIST-MATCHING.md) | Story | P2 | 2 | 1 |
| `WAITLIST-OFFER-LIFECYCLE` | [Waitlist: offer lifecycle (offered → accepted / expired)](../stories/PRD-02__WAITLIST-OFFER-LIFECYCLE.md) | Story | P2 | 2 | 1 |
| `WAITLIST-BACKFILL-PROMPT` | [Waitlist: cancel/no-show backfill prompt](../stories/PRD-02__WAITLIST-BACKFILL-PROMPT.md) | Story | P2 | 2 | 1 |
| `WALKINS` | [Walk-ins — basic gate-respecting booking](../stories/PRD-02__WALKINS.md) | Story | P2 | 2 | 1 |
| `WALKINS-ADDON` | [Walk-ins: same-day add-on to an in-progress visit](../stories/PRD-02__WALKINS-ADDON.md) | Story | P2 | 2 | 1 |
| `WALKINS-CONFLICT` | [Walk-ins: resource conflict-flagging before confirm](../stories/PRD-02__WALKINS-CONFLICT.md) | Story | P2 | 2 | 1 |
| `WALKINS-TAGS` | [Walk-ins: VIP / first-time tags & distinct rendering](../stories/PRD-02__WALKINS-TAGS.md) | Story | P2 | 2 | 1 |
| `CLIENT-360` | [Client 360° profile — basic aggregation & header](../stories/PRD-02__CLIENT-360.md) | Story | P1 | 3 | 2 |
| `CLIENT-360-OVERVIEW` | [Client 360: Overview tab (recent activity & at-a-glance)](../stories/PRD-02__CLIENT-360-OVERVIEW.md) | Story | P2 | 2 | 1 |
| `CLIENT-360-CLINICAL-TABS` | [Client 360: clinical & visit tabs (Visits / Treatment plan / Consents & forms)](../stories/PRD-02__CLIENT-360-CLINICAL-TABS.md) | Story | P2 | 2 | 1 |
| `CLIENT-360-COMMERCIAL-TABS` | [Client 360: commercial tabs (Membership & rewards / Billing / Notes & comms)](../stories/PRD-02__CLIENT-360-COMMERCIAL-TABS.md) | Story | P2 | 2 | 1 |
| `PHOTOS-GALLERY` | [Before/after photo gallery — basic consent-gated view](../stories/PRD-02__PHOTOS-GALLERY.md) | Story | P2 | 2 | 2 |
| `PHOTOS-GALLERY-COMPARE` | [Before/after photo gallery: compare & grouping UI](../stories/PRD-02__PHOTOS-GALLERY-COMPARE.md) | Story | P2 | 2 | 1 |
| `PHOTOS-GALLERY-AUDIT` | [Before/after photo gallery: photo-view audit events](../stories/PRD-02__PHOTOS-GALLERY-AUDIT.md) | Story | P2 | 2 | 1 |
| `CLIENT-DIR` | [Client directory — basic search & list](../stories/PRD-02__CLIENT-DIR.md) | Story | P2 | 2 | 2 |
| `CLIENT-DIR-SEGMENTS` | [Client directory: segment filters (All / Members / At-risk / New)](../stories/PRD-02__CLIENT-DIR-SEGMENTS.md) | Story | P2 | 2 | 1 |
| `CLIENT-DIR-SOFT-DELETE` | [Client directory: audited soft-delete](../stories/PRD-02__CLIENT-DIR-SOFT-DELETE.md) | Story | P2 | 2 | 1 |
| `CLIENT-DIR-HEADER-SEARCH` | [Client directory: global header search wiring](../stories/PRD-02__CLIENT-DIR-HEADER-SEARCH.md) | Story | P2 | 2 | 1 |
| `CLIENT-MERGE` | [Client merge — basic duplicate detection & review](../stories/PRD-02__CLIENT-MERGE.md) | Story | P2 | 2 | 1 |
| `CLIENT-MERGE-TRANSACTION` | [Client merge: re-point all child records + MergeLog](../stories/PRD-02__CLIENT-MERGE-TRANSACTION.md) | Story | P2 | 2 | 1 |
| `CLIENT-MERGE-CONFIRM-UI` | [Client merge: confirmation UI & post-merge retirement](../stories/PRD-02__CLIENT-MERGE-CONFIRM-UI.md) | Story | P2 | 2 | 1 |
| `DEPOSITS` | [Booking deposits / card-on-file hold (placeholder)](../stories/PRD-02__DEPOSITS.md) | Story | P2 | 1 | 1 |
| `BOOKING-WIZARD` | [Staff booking wizard — basic scope-aware flow](../stories/PRD-02__BOOKING-WIZARD.md) | Story | P1 | 3 | 2 |
| `BOOKING-WIZARD-CLIENT-STEP` | [Staff booking wizard: new-client creation, under-18 & intake/consent send](../stories/PRD-02__BOOKING-WIZARD-CLIENT-STEP.md) | Story | P2 | 2 | 1 |
| `BOOKING-WIZARD-CONFIRM` | [Staff booking wizard: confirm with policy & reminder scheduling](../stories/PRD-02__BOOKING-WIZARD-CONFIRM.md) | Story | P2 | 2 | 1 |
| `SERVICE-CATALOGUE` | [Services & treatment menu — basic catalogue & S4 flag](../stories/PRD-02__SERVICE-CATALOGUE.md) | Story | P1 | 3 | 2 |
| `SERVICE-CATALOGUE-WIRING` | [Service catalogue: schedule flag wired to scope, rewards & public naming](../stories/PRD-02__SERVICE-CATALOGUE-WIRING.md) | Story | P2 | 2 | 1 |
| `SERVICE-CATALOGUE-ADMIN` | [Service catalogue: capability-gated admin & audit](../stories/PRD-02__SERVICE-CATALOGUE-ADMIN.md) | Story | P2 | 2 | 1 |
| `SERVICE-CATALOGUE-CARD-UI` | [Service catalogue: treatment-menu card UI & status filter](../stories/PRD-02__SERVICE-CATALOGUE-CARD-UI.md) | Story | P2 | 2 | 2 |

_Totals: 54 stories · 74 tasks._
