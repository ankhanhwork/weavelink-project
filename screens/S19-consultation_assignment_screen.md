# S19 — Consultation Assignment

| Property | Value |
|---|---|
| Route | `/admin/design-requests/{request_id}/assignment` |
| Module | MFG-05 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin assigns one eligible Paid, unassigned DesignRequest to an active Sales Consultant in the same company and records the committed due date. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| request_id | UUID path parameter | Request must be Paid and unassigned, or eligible for atomic reassignment. |
| consultant_id | UUID, required | Active Sales Consultant membership in same company. |
| committed_due_at | UTC timestamp, required | Admin commitment at assignment; requested_deadline remains customer preference. |
| expected_version | integer, required | Stale request returns 409; assignment and due date save atomically. |
| company_id / customer_id | server-derived UUIDs | Never accepted as form input; scope comes from active company session. |
| API errors | D02 envelope | 400 malformed; 403 prohibited; 404 inaccessible; 409 stale/duplicate assignment; 422 invalid consultant/date. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Assign consultant | Atomic assign/reassign, record committed_due_at, notify after commit. | S18 requests tab |
| Cancel | Leave request unchanged. | S18 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-08/F-ORD-003, MFG-08/F-ORD-004. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Successful assignment → S18 requests tab; cancel → S18.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Render the screen-specific form/detail state; if a required route object is absent, show safe not-found and return to the authorized parent route. | Empty initial form or missing detail payload |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Assignment succeeds only for active same-company consultant and records committed_due_at atomically.
2. Concurrent/stale assignment returns 409 and does not create duplicate notices.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-05 specification](../specs/spec-MFG-05.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
