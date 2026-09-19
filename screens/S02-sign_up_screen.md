# Screen Spec: S02 Sign Up

| Field | Value |
|---|---|
| Screen ID | `S02` |
| Screen name | Sign Up |
| Actor | Guest |
| Priority | P1 |
| Belongs to module | [MFG-01](../specs/spec-MFG-01.md) |
| Route | `/sign-up` |
| Mockup image | img/S02-sign_up_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** Registration creates a Customer identity in pending-verification state; staff memberships are never created through this form. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S02 historical reference](img/S02-sign_up_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Sign Up | Yes | Static route title. |
| 2 | Route | Navigation target | /sign-up | Yes | Access checked on server. |
| 3 | full_name | Field / control | string, required, trim, 1..100 characters. | As specified | full_name: string, required, trim, 1..100 characters. |
| 4 | email | Field / control | string, required, normalize case, globally unique | As specified | email: string, required, normalize case, globally unique; valid email format. |
| 5 | password | Field / control | string, required, 12..128 characters, spaces allowed | As specified | password: string, required, 12..128 characters, spaces allowed; never echoed or logged. |
| 6 | Verification link | Field / control | cryptographically random, hashed at rest, single-use, 24h expiry. | As specified | Verification link: cryptographically random, hashed at rest, single-use, 24h expiry. |
| 7 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 8 | Create account | Action | Validate fields, create Guest-registered Customer pending verification, queue 24h link; neutral success. | Available when authorized | Destination: S03 |
| 9 | Resend verification | Action | Rate-limit; invalidate prior token; report generic queued state. | Available when authorized | Destination: S02 |
| 10 | Sign in | Action | Navigate to login. | Available when authorized | Destination: S03 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Render the screen-specific form/detail state; if a required route object is absent, show safe not-found and return to the authorized parent route. | Empty initial form or missing detail payload |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one for the documented mutation. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Create account | Activate | Validate fields, create Guest-registered Customer pending verification, queue 24h link; neutral success. | S03 |
| 2 | Resend verification | Activate | Rate-limit; invalidate prior token; report generic queued state. | S02 |
| 3 | Sign in | Activate | Navigate to login. | S03 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. With valid fields, create only a Customer account and queue a single-use verification link expiring in 24h.
2. With duplicate email or delivery failure, return a non-enumerating response and preserve safe form values.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-01/F-USER-001 | Implements this screen's validated user flow and the linked source function. |
| MFG-01/F-USER-002 | Implements this screen's validated user flow and the linked source function. |
| MFG-01/F-USER-003 | Implements this screen's validated user flow and the linked source function. |
The rules in this screen and its linked module specifications are complete for implementation.

## 8. Responsive and accessibility notes

Support 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens. Controls are keyboard-operable with visible focus, logical headings, associated form labels, and aria-live status/error announcements. Text contrast is at least 4.5:1 (large text 3:1); pointer targets are at least 24px. Preserve user-entered data after recoverable failures. Confirm destructive actions, disable duplicate submit while pending, and enforce idempotency on the server.

## 9. Open questions

| # | Question | Blocking? | Status |
|---|---|---|---|
| 1 | No unresolved screen behavior questions remain; routes, fields, permissions, and defaults are resolved in this specification and its linked module requirements. | No | Resolved |

## Completion checklist

- [x] Route, actor, module, priority, and mockup status are identified.
- [x] Element fields, actions, validation, and data ownership are documented.
- [x] Loading, empty, forbidden, error, retry, success, and conflict states are documented.
- [x] Navigation and acceptance scenarios are explicit.
- [x] Responsive and accessibility requirements follow the shared baseline.
- [x] No unresolved screen-level decisions remain.
