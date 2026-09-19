# S30 — Contract Templates and Contracts

| Property | Value |
|---|---|
| Route | `/admin/contracts?tab=templates,contracts` |
| Module | MFG-09 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin switches between versioned contract templates and company contracts. Signed contract versions are immutable and template changes create a new version. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| tab | enum: templates or contracts; default templates | Templates show template_id, name, current version and active status; contracts show contract_id, order_id, version and lifecycle status. |
| status | enum filtered by tab | Template statuses Draft, Active, Archived; contract statuses Draft, Ready, Signed, Superseded, Voided. |
| query / page / page_size | trimmed text / integer / integer | Search template name or contract/order ID; D02 pagination bounds and allowlisted sort. |
| company_id | server-derived UUID | All templates/contracts are scoped to the active Company Admin membership. |
| version | integer | Template edits create a new version; a Signed contract and its PDF snapshot cannot be edited. |
| API errors | D02 envelope | 400 malformed; 422 invalid filters; 403 prohibited action; 404 inaccessible contract; 409 stale version/state; 503 dependency failure. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Create template | Open safe template form. | S31 |
| Publish template | Activate validated version for new contracts. | S30 |
| Archive template | Prevent future use while preserving referenced versions. | S30 |
| Edit template | Create a new version; keep previous used versions. | S32 |
| Open contract | Show status and generated PDF. | S33 |
| Switch tabs | Templates and contracts tabs are same routed screen. | S30 tab |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-09/F-CONTR-001, MFG-09/F-CONTR-002, MFG-09/F-CONTR-003, MFG-09/F-CONTR-004, MFG-09/F-CONTR-005, MFG-09/F-CONTR-006, MFG-09/F-CONTR-007. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Create template → S31; edit template → S32; open contract → S33; template/contracts tab remains S30.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no templates or contracts in the selected tab; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Templates and contracts tabs show company-scoped versions and status filters.
2. Signed contract exposes no edit/version replacement action.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-09 specification](../specs/spec-MFG-09.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
