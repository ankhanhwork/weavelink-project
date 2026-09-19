# S41 — Company and Staff Accounts

| Property | Value |
|---|---|
| Route | `/system/companies` |
| Module | MFG-03 |
| Roles and ownership | System Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The System Admin provisions companies and staff memberships, sends invitations, changes lifecycle status and soft-deletes eligible records while protecting last active administrators. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| company_id / version | UUID / integer | Server-issued; expected_version required for lifecycle edits. |
| legal_name / display_name | strings, required | Trimmed; legal name 1..200 characters, display name 1..100. |
| tax_id / address | strings, required | Tax ID 1..30 characters; address 1..500. |
| admin_contact_info | name, email, phone | Initial admin contact; normalize email and validate phone using D06. |
| initial_admin_email | normalized email, required | Create 48-hour single-use invite atomically with company. |
| company_status | Provisioning, Active, Suspended, Deleted | Provisioning activates only when initial admin accepts; suspension blocks new catalog/order/payment activity but preserves customer reads/reconciliation. |
| staff email / role / status | normalized email / Company Admin or Sales Consultant / Invited, Active, Suspended, Deleted | Customers are not staff; only System Admin provisions memberships. |
| API errors | D02 envelope | 400 malformed; 403 prohibited; 404 inaccessible company; 409 duplicate/stale/last-admin protection; 422 invalid fields. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Create company | Create Provisioning company with required tax_id, address and initial admin contact/invite; activate only after invite acceptance. | S41 |
| Invite staff | Create 48h single-use invitation for Company Admin/Sales Consultant. | S41 |
| Suspend/reactivate | Enforce company work/read/reconciliation policy; audit transition. | S41 |
| Soft delete | Confirm; retain history and revoke sessions; protect last active admins. | S41 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-03/F-ACC-001, MFG-03/F-ACC-002, MFG-03/F-ACC-003, MFG-03/F-ACC-004, MFG-03/F-ACC-005, MFG-03/F-ACC-006, MFG-03/F-ACC-007, MFG-03/F-ACC-008. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Company detail/staff invite/edit remains S41; config/logs → S39/S40; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no companies or staff memberships matching filters; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Staff invite accepts only assignable staff roles and expires after 48h; customer role is not provisioned here.
2. Deleting/demoting the last active System Admin or Company Admin is rejected; soft delete retains business history.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-03 specification](../specs/spec-MFG-03.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
