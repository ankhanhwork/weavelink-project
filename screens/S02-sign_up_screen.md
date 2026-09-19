# S02 — Sign Up

| Property | Value |
|---|---|
| Route | `/sign-up` |
| Module | MFG-01 |
| Roles and ownership | Guest; server enforces role, company, assignment and ownership per D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S02-sign_up_screen.png](img/S02-sign_up_screen.png); written rules supersede sample text. |

## Purpose and data

Registration creates a Customer identity in pending-verification state; staff memberships are never created through this form. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| full_name |  string, required, trim, 1..100 characters. | full_name: string, required, trim, 1..100 characters. |
| email |  string, required, normalize case, globally unique | email: string, required, normalize case, globally unique; valid email format. |
| password |  string, required, 12..128 characters, spaces allowed | password: string, required, 12..128 characters, spaces allowed; never echoed or logged. |
| Verification link |  cryptographically random, hashed at rest, single-use, 24h expiry. | Verification link: cryptographically random, hashed at rest, single-use, 24h expiry. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Create account | Validate fields, create Guest-registered Customer pending verification, queue 24h link; neutral success. | S03 |
| Resend verification | Rate-limit; invalidate prior token; report generic queued state. | S02 |
| Sign in | Navigate to login. | S03 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-01/F-USER-001, MFG-01/F-USER-002, MFG-01/F-USER-003. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Verification email sent → S03 login after verification; sign in link → S03; home → S01.

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

1. With valid fields, create only a Customer account and queue a single-use verification link expiring in 24h.
2. With duplicate email or delivery failure, return a non-enumerating response and preserve safe form values.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-01 specification](../specs/spec-MFG-01.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
