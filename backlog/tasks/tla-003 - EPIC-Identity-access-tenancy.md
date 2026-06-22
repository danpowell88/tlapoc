---
id: TLA-003
title: 'EPIC: Identity, access & tenancy'
status: To Do
assignee: []
created_date: '2026-06-22 10:42'
labels:
  - 'type:epic'
  - 'area:web'
  - 'area:api'
  - mvp
  - compliance
  - 'milestone:M1'
dependencies: []
references:
  - docs/prds/PRD-01-foundations-tenancy.md
priority: high
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Who can sign in, what they can do, and the records the whole platform hangs off. Staff and client identity, role-based access control (including the QLD 'designated RN prescriber' role), step-up auth for sensitive actions, an append-only audit trail, the core client record, and — critically — staff credentials feeding the 'canInject' scope-of-practice gate that decides whether a person may administer an injectable right now. Includes the practitioner roster that booking availability is built on.

Derived from PRD-01. Multi-tenant isolation is assumed from the foundations epic; this epic is the application-level identity, roles and core records.

**MVP:** yes. **Surface:** web (staff) · API. Compliance: C4 (scope of practice), C10/C19/C21/C22 (audit, privacy, residency).
<!-- SECTION:DESCRIPTION:END -->
