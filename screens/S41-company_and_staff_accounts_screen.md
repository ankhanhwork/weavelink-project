# Screen Spec: S41 Company and Staff Accounts

| Field | Value |
|---|---|
| Screen ID | `S41` |
| Screen name | Company and Staff Accounts |
| Actor | System Admin |
| Priority | P2 |
| Belongs to module | [MFG-03](../specs/spec-MFG-03.md) |
| Route | `/system/companies` |
| Mockup image | Don't have mockup |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The System Admin provisions companies and staff memberships, sends invitations, changes lifecycle status and soft-deletes eligible records while protecting last active administrators. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

Don't have mockup

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Company and Staff Accounts | Yes | Static route title. |
| 2 | Route | Navigation target | /system/companies | Yes | Access checked on server. |
| 3 | company_id / version | Field / control | UUID / integer | As specified | Server-issued; expected_version required for lifecycle edits. |
| 4 | legal_name / display_name | Field / control | strings, required | As specified | Trimmed; legal name 1..200 characters, display name 1..100. |
| 5 | tax_id / address | Field / control | strings, required | As specified | Tax ID 1..30 characters; address 1..500. |
| 6 | admin_contact_info | Field / control | name, email, phone | As specified | Initial admin contact; normalize email and require 8..15 digits with optional leading + for phone. |
| 7 | initial_admin_email | Field / control | normalized email, required | As specified | Create 48-hour single-use invite atomically with company. |
| 8 | company_status | Field / control | Provisioning, Active, Suspended, Deleted | As specified | Provisioning activates only when initial admin accepts; suspension blocks new catalog/order/payment activity but preserves customer reads/reconciliation. |
| 9 | staff email / role / status | Field / control | normalized email / Company Admin or Sales Consultant / Invited, Active, Suspended, Deleted | As specified | Customers are not staff; only System Admin provisions memberships. |
| 10 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 403 prohibited; 404 inaccessible company; 409 duplicate/stale/last-admin protection; 422 invalid fields. |
| 11 | Create company | Action | Create Provisioning company with required tax_id, address and initial admin contact/invite; activate only after invite acceptance. | Available when authorized | Destination: S41 |
| 12 | Invite staff | Action | Create 48h single-use invitation for Company Admin/Sales Consultant. | Available when authorized | Destination: S41 |
| 13 | Suspend/reactivate | Action | Enforce company work/read/reconciliation policy; audit transition. | Available when authorized | Destination: S41 |
| 14 | Soft delete | Action | Confirm; retain history and revoke sessions; protect last active admins. | Available when authorized | Destination: S41 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no companies or staff memberships matching filters; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one for the documented mutation. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Create company | Activate | Create Provisioning company with required tax_id, address and initial admin contact/invite; activate only after invite acceptance. | S41 |
| 2 | Invite staff | Activate | Create 48h single-use invitation for Company Admin/Sales Consultant. | S41 |
| 3 | Suspend/reactivate | Activate | Enforce company work/read/reconciliation policy; audit transition. | S41 |
| 4 | Soft delete | Activate | Confirm; retain history and revoke sessions; protect last active admins. | S41 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Staff invite accepts only assignable staff roles and expires after 48h; customer role is not provisioned here.
2. Deleting/demoting the last active System Admin or Company Admin is rejected; soft delete retains business history.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-03/F-ACC-001 | Implements this screen's validated user flow and the linked source function. |
| MFG-03/F-ACC-002 | Implements this screen's validated user flow and the linked source function. |
| MFG-03/F-ACC-003 | Implements this screen's validated user flow and the linked source function. |
| MFG-03/F-ACC-004 | Implements this screen's validated user flow and the linked source function. |
| MFG-03/F-ACC-005 | Implements this screen's validated user flow and the linked source function. |
| MFG-03/F-ACC-006 | Implements this screen's validated user flow and the linked source function. |
| MFG-03/F-ACC-007 | Implements this screen's validated user flow and the linked source function. |
| MFG-03/F-ACC-008 | Implements this screen's validated user flow and the linked source function. |
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
