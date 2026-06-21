# PRD-09 — Apps (Flutter): client & provider

> **Stage / Milestone:** M5 · Reporting & apps (PRD-08, PRD-09)  ·  **Phase:** 1  ·  **Stories:** 10

Two Flutter apps over the shared .NET API: a client app (book, intake/consent, photos, memberships, rewards, balances, card-on-file) and a provider app (room-side charting, injection mapping, camera capture, consult/Rx, finalise) — the latter resilient to treatment-room connectivity. One codebase, two flavours, sharing auth, the API client and the design system.

**Source PRD:** `docs/prds/PRD-09-apps-client-provider.md`

## Stories

| Key | Story | Type | Priority | Est | Tasks |
|---|---|---|---|---|---|
| `CLIENT-JOURNEY` | [Client app: book → intake → consent journey](../stories/PRD-09__CLIENT-JOURNEY.md) | Story | P1 | 3 | 1 |
| `CLIENT-CARE` | [Client app: my care, memberships, rewards & card-on-file](../stories/PRD-09__CLIENT-CARE.md) | Story | P2 | 2 | 1 |
| `CLIENT-PRIVACY` | [Client app: account, privacy & access/correction](../stories/PRD-09__CLIENT-PRIVACY.md) | Story | P2 | 2 | 2 |
| `PROVIDER-DAY` | [Provider app: day schedule & open patient](../stories/PRD-09__PROVIDER-DAY.md) | Story | P1 | 3 | 1 |
| `PROVIDER-ROOMSIDE` | [Provider app: room-side charting, camera & finalise](../stories/PRD-09__PROVIDER-ROOMSIDE.md) | Story | P1 | 3 | 2 |
| `PROVIDER-OFFLINE` | [Provider app: offline-tolerant workflows + sync indicator](../stories/PRD-09__PROVIDER-OFFLINE.md) | Story | P1 | 3 | 2 |
| `APP-DISTRIBUTION` | [App distribution & code-push posture](../stories/PRD-09__APP-DISTRIBUTION.md) | Story | P2 | 2 | 4 |
| `CHECKIN-KIOSK` | [Reception self-check-in surface (tablet)](../stories/PRD-09__CHECKIN-KIOSK.md) | Story | P2 | 2 | 1 |
| `BACKOFFICE-TABLET` | [Back-office / bench tablet surface](../stories/PRD-09__BACKOFFICE-TABLET.md) | Story | P2 | 2 | 1 |
| `CLIENT-CONCERN` | [Client 'report a concern' → follow-up / AE bridge](../stories/PRD-09__CLIENT-CONCERN.md) | Story | P1 | 3 | 4 |

_Totals: 10 stories · 19 tasks._
