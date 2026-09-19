# S07 — Change Password

| Property | Value |
|---|---|
| Route | `/profile/change-password` |
| Module | MFG-02 |
| Roles and ownership | Member; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | No mockup supplied. |

## Purpose and data

This form changes only the authenticated user password. It requires the current password, retains the current session and revokes other sessions. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| current_password |  required secret | current_password: required secret; verify against stored hash. |
| new_password |  required 12..128 characters | new_password: required 12..128 characters; spaces allowed. |
| confirm_password |  required exact match | confirm_password: required exact match; reject current/new equality. |
| session_effect | server rule | On success retain the current session and revoke all other sessions. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Change password | Verify current password, hash new password, revoke other sessions, show confirmation. | S06 |
| Cancel | Discard unsaved password fields. | S06 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-02/F-PROF-004, MFG-02/F-PROF-005. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Password changed → S06; cancel → validated origin or S06.

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

1. Correct current password and matching 12..128-char new password update hash and revoke other sessions.
2. Incorrect current password or confirmation mismatch leaves stored password unchanged.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-02 specification](../specs/spec-MFG-02.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
