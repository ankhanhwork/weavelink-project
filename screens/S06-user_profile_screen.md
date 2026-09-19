# S06 — User Profile

| Property | Value |
|---|---|
| Route | `/profile` |
| Module | MFG-02 |
| Roles and ownership | Member; server enforces role, company, assignment and ownership per D01. |
| Priority | P3 |
| Mockup | Historical mockup: [img/S06-user_profile_screen.png](img/S06-user_profile_screen.png); written rules supersede sample text. |

## Purpose and data

The signed-in user can edit full_name and request a pending email change. The current email remains active until the new address is verified; memberships are display-only. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / required | Validation and source |
|---|---|---|
| full_name | string, required | Editable; trim; length 1..100. D03 |
| email | normalized email, read-only display | Change flow requests new email and verifies it before replacement; email remains globally unique. D03 refinement |
| pending_email | normalized email, optional | Show pending verification status; current email remains active until verified. D03 refinement |
| role memberships | enum array, read-only | Display assigned roles; Member cannot assign self. D01 |
| expected_version | version, required on update | Stale profile edit returns 409. D02 |
## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Save profile | Check expected_version, update full_name and updated_at. | S06 |
| Change password | Open current/new password form. | S07 |
| Sign out | Revoke current session, clear cookie, record audit event. | S03 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-02/F-PROF-001, MFG-02/F-PROF-002, MFG-02/F-PROF-003; MFG-01/F-USER-006. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Edit profile stays S06; change password → S07; logout → S03; orders → S26; designs → S17.

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

1. A user can update only own full_name; stale expected_version returns 409 without overwriting.
2. Role display cannot be edited by Member; logout revokes current server session.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-02 specification](../specs/spec-MFG-02.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
