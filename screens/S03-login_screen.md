# S03 — Log In

| Property | Value |
|---|---|
| Route | `/login` |
| Module | MFG-01 |
| Roles and ownership | Guest; invitation acceptance resolves invited staff role and company membership on the server. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S03-login_screen.png](img/S03-login_screen.png); written rules supersede sample text. |

## Purpose and data

The form has two explicit modes: email/password authentication and staff invitation acceptance. Invitation acceptance follows the existing-account or new-account path in D02. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / required | Validation and source |
|---|---|---|
| mode | enum, required | Login or staff invitation acceptance. D03 refinement |
| email | string, required | Trim and case-normalize; global uniqueness. D03 |
| password | secret, required for login | Verify hash; never log or echo. D03 |
| return_to | internal URL, optional | Allowlisted route only; reject external redirects. D03 |
| invitation_token | secret, required in invitation mode | Hashed, single use, 48-hour expiry. D03 |
| full_name / new_password | string/secret, required for invited new staff | full_name 1..100; password 12..128; existing account authenticates then accepts invite. D01/D03 |
| failed attempts | server counter | Limit 5 per account/IP within 15 minutes; return 429. D03 |
## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Authenticate | Verify hash/rate limit, set secure session cookie, redirect to allowlisted return_to or authenticated role D11 default. | return_to or role default |
| Accept invitation | Existing identity authenticates then accepts; new invitee supplies full_name/password; consume invite and activate membership atomically. | S41 completion, then role default |
| Forgot password | Open recovery. | S04 |
| Register | Open registration. | S02 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-01/F-USER-004, MFG-01/F-USER-005. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Valid session → validated return_to, else Customer S26, Company Admin S28, Sales Consultant S20 or System Admin S41; invitation link opens invitation mode; forgot password → S04; register → S02.

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

1. With valid credentials, establish secure HttpOnly SameSite=Lax session and use only internal return route.
2. After five failed attempts per account/IP in 15m, reject further login attempts with 429.
3. Given a valid staff invitation, an existing identity must authenticate before atomic membership activation; a new invitee supplies name/password, consumes the invite once, and reaches the invited role's default route.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-01 specification](../specs/spec-MFG-01.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
