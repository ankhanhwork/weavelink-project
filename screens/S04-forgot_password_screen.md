# S04 — Forgot Password

| Property | Value |
|---|---|
| Route | `/forgot-password` |
| Module | MFG-01 |
| Roles and ownership | Guest; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | No mockup supplied. |

## Purpose and data

Password recovery returns the same confirmation for known and unknown email addresses. Eligible requests queue a single-use reset link and invalidate the previous link. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| email |  string required, normalized | email: string required, normalized; do not indicate whether it exists. |
| Link request |  max 3 per account/IP/hour | Link request: max 3 per account/IP/hour; resend invalidates prior link. |
| Response |  same neutral confirmation for existing and absent accounts. | Response: same neutral confirmation for existing and absent accounts. |
| API errors | D02 envelope | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Request reset | Apply generic response and queue email only if eligible; invalidate prior link. | S03 |
| Resend | Enforce request limit and queue latest link. | S04 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-01/F-USER-007, MFG-01/F-USER-008, MFG-01/F-USER-009. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Request accepted → S03 with neutral confirmation; reset email link opens S05; sign in → S03.

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

1. For existing and unknown emails, show identical confirmation text and response shape.
2. At fourth request within an hour, return 429 without sending another link.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-01 specification](../specs/spec-MFG-01.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
