# S05 — Reset Password

| Property | Value |
|---|---|
| Route | `/reset-password?token={token}` |
| Module | MFG-01 |
| Roles and ownership | Guest with single-use token; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | No mockup supplied. |

## Purpose and data

The token query parameter authorizes one password reset for 30 minutes. Successful reset revokes all sessions and consumes the token. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| token |  required query secret | token: required query secret; single-use hashed token; 30m expiry. |
| new_password |  required, 12..128 characters, spaces allowed. | new_password: required, 12..128 characters, spaces allowed. |
| confirm_password |  required | confirm_password: required; exact match with new_password. |
| reset_effect | server rule | A successful reset consumes the token and revokes every existing session for that user. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Reset password | Validate single-use token/password match, update hash, revoke all sessions. | S03 |
| Request new link | Discard token route and open recovery. | S04 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-01/F-USER-010, MFG-01/F-USER-011. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Password reset success → S03; expired/used token → S04 for new link.

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

1. With valid token and matching valid passwords, consume token once, hash password and revoke all sessions.
2. With expired/reused token or mismatch, reject safely; no password or token is echoed.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-01 specification](../specs/spec-MFG-01.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
