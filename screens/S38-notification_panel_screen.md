# S38 — Notification Panel

| Property | Value |
|---|---|
| Route | `/notifications` |
| Module | MFG-01 |
| Roles and ownership | Authenticated user; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | No mockup supplied. |

## Purpose and data

The authenticated recipient sees their persisted in-app notifications. Opening a target rechecks authorization; email delivery remains secondary. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| notification_id / recipient | UUID plus session-derived owner | Sanitize event/target content; never accept a submitted recipient as authority. |
| read_at / pagination | nullable UTC plus D02 paging | Event/recipient uniqueness suppresses duplicates. |
| target_route | optional internal route | Reauthorize the target when opened; hide invalid or inaccessible deep links. |
| email_delivery_state | secondary read-only status | The persisted in-app inbox remains authoritative. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Mark read | Persist recipient read_at; repeated action is idempotent. | S38 |
| Open notification | Resolve allowlisted target and reauthorize target access. | authorized target route |
| Close | Return to prior validated route. | Origin |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: shared persisted outbox and D03 recipient event contract. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Notification target resolves only to authorized S18, S21, S27, S29, S33 or S35; close returns prior route.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no notifications for this recipient; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. User sees only own persisted notifications and repeated mark-read is idempotent.
2. Opening an unauthorized/stale target is blocked after a fresh server access check.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-01 specification](../specs/spec-MFG-01.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
