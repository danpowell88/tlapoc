# PRD-09 — Apps (Flutter): client & provider

> **Stage / Milestone:** M5 · Reporting & apps (PRD-08, PRD-09)  ·  **Phase:** 1  ·  **Stories:** 27

Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity. One codebase, two flavours, sharing auth, the API client and the design system.

**Source PRD:** `docs/prds/PRD-09-apps-client-provider.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `CLIENT-JOURNEY` | [Client app: shell, sign-in & home (basic)](../stories/PRD-09__CLIENT-JOURNEY.md) | Story | P1 | 3 | 2 |
| `CLIENT-BOOK` | [Client app: in-app booking over PRD-02](../stories/PRD-09__CLIENT-BOOK.md) | Story | P2 | 2 | 1 |
| `CLIENT-INTAKE` | [Client app: intake + consent, e-signed on device](../stories/PRD-09__CLIENT-INTAKE.md) | Story | P2 | 2 | 2 |
| `CLIENT-PUSH` | [Client app: push token + notification inbox](../stories/PRD-09__CLIENT-PUSH.md) | Story | P2 | 2 | 1 |
| `CLIENT-CARE` | [Client app: my care health hub (basic)](../stories/PRD-09__CLIENT-CARE.md) | Story | P2 | 2 | 1 |
| `CLIENT-REWARDS` | [Client app: rewards, perks & referrals](../stories/PRD-09__CLIENT-REWARDS.md) | Story | P2 | 2 | 1 |
| `CLIENT-ACCOUNT` | [Client app: account, memberships & card-on-file](../stories/PRD-09__CLIENT-ACCOUNT.md) | Story | P2 | 2 | 1 |
| `PHOTO-COMPARE` | [Client app: consent-gated before/after gallery with drag-to-compare](../stories/PRD-09__PHOTO-COMPARE.md) | Story | P2 | 2 | 3 |
| `AFTERCARE-GUIDE` | [Client app: day-by-day aftercare guidance + escalation](../stories/PRD-09__AFTERCARE-GUIDE.md) | Story | P2 | 2 | 3 |
| `CLIENT-PRIVACY` | [Client app: account, privacy & access/correction](../stories/PRD-09__CLIENT-PRIVACY.md) | Story | P2 | 2 | 2 |
| `PROVIDER-DAY` | [Provider app: day schedule & open patient](../stories/PRD-09__PROVIDER-DAY.md) | Story | P1 | 3 | 3 |
| `PROVIDER-ROOMSIDE` | [Provider app: room-side injection mapping (basic)](../stories/PRD-09__PROVIDER-ROOMSIDE.md) | Story | P1 | 3 | 2 |
| `PROVIDER-CAMERA` | [Provider app: native-camera before/after capture](../stories/PRD-09__PROVIDER-CAMERA.md) | Story | P1 | 3 | 1 |
| `PROVIDER-FINALISE` | [Provider app: server-side finalise → immutable record](../stories/PRD-09__PROVIDER-FINALISE.md) | Story | P1 | 3 | 1 |
| `PROVIDER-OFFLINE` | [Provider app: offline-tolerant workflows + sync indicator](../stories/PRD-09__PROVIDER-OFFLINE.md) | Story | P1 | 3 | 2 |
| `APP-DISTRIBUTION` | [App distribution & code-push posture](../stories/PRD-09__APP-DISTRIBUTION.md) | Story | P2 | 2 | 4 |
| `CHECKIN-KIOSK` | [Reception self-check-in surface (basic)](../stories/PRD-09__CHECKIN-KIOSK.md) | Story | P2 | 2 | 2 |
| `CHECKIN-DETAILS` | [Kiosk: details review + today's health check](../stories/PRD-09__CHECKIN-DETAILS.md) | Story | P2 | 2 | 1 |
| `CHECKIN-FORMS` | [Kiosk: outstanding intake/consent at the desk](../stories/PRD-09__CHECKIN-FORMS.md) | Story | P2 | 2 | 1 |
| `CHECKIN-ARRIVALS` | [Kiosk: reception arrivals board feed](../stories/PRD-09__CHECKIN-ARRIVALS.md) | Story | P2 | 2 | 1 |
| `BACKOFFICE-TABLET` | [Back-office / bench tablet surface (basic)](../stories/PRD-09__BACKOFFICE-TABLET.md) | Story | P2 | 2 | 1 |
| `BACKOFFICE-OPENCOLD` | [Back-office tablet: open/close + cold-chain panels](../stories/PRD-09__BACKOFFICE-OPENCOLD.md) | Story | P2 | 2 | 1 |
| `BACKOFFICE-STOCK` | [Back-office tablet: stock + S4 register + waste panels](../stories/PRD-09__BACKOFFICE-STOCK.md) | Story | P2 | 2 | 1 |
| `BACKOFFICE-TASKS` | [Back-office tablet: tasks + shift-handover panels](../stories/PRD-09__BACKOFFICE-TASKS.md) | Story | P2 | 2 | 1 |
| `CLIENT-CONCERN` | [Client 'report a concern' → follow-up bridge (basic)](../stories/PRD-09__CLIENT-CONCERN.md) | Story | P1 | 3 | 2 |
| `CONCERN-TRIAGE` | [Staff Follow-ups: view / call back / resolve a concern](../stories/PRD-09__CONCERN-TRIAGE.md) | Story | P1 | 3 | 1 |
| `CONCERN-ESCALATE` | [Concern: escalate to adverse event / complaint](../stories/PRD-09__CONCERN-ESCALATE.md) | Story | P1 | 3 | 1 |

_Totals: 27 stories · 43 tasks._
