# Screen Spec: S30 Contract Templates and Contracts

| Field | Value |
|---|---|
| Screen ID | `S30` |
| Screen name | Contract Templates and Contracts |
| Actor | Company Admin |
| Priority | P2 |
| Belongs to module | [MFG-09](../specs/spec-MFG-09.md) |
| Route | `/admin/contracts?tab=templates,contracts` |
| Mockup image | Don't have mockup |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The Company Admin switches between versioned contract templates and company contracts. Signed contract versions are immutable and template changes create a new version. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

Don't have mockup

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Contract Templates and Contracts | Yes | Static route title. |
| 2 | Route | Navigation target | /admin/contracts?tab=templates,contracts | Yes | Access checked on server. |
| 3 | tab | Field / control | enum: templates or contracts; default templates | As specified | Templates show template_id, name, current version and active status; contracts show contract_id, order_id, version and lifecycle status. |
| 4 | status | Field / control | enum filtered by tab | As specified | Template statuses Draft, Active, Archived; contract statuses Draft, Ready, Signed, Superseded, Voided. |
| 5 | query / page / page_size | Field / control | trimmed text / integer / integer | As specified | Search template name or contract/order ID; positive bounded paging and allowlisted sort. |
| 6 | company_id | Field / control | server-derived UUID | As specified | All templates/contracts are scoped to the active Company Admin membership. |
| 7 | version | Field / control | integer | As specified | Template edits create a new version; a Signed contract and its PDF snapshot cannot be edited. |
| 8 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid filters; 403 prohibited action; 404 inaccessible contract; 409 stale version/state; 503 dependency failure. |
| 9 | Create template | Action | Open safe template form. | Available when authorized | Destination: S31 |
| 10 | Publish template | Action | Activate validated version for new contracts. | Available when authorized | Destination: S30 |
| 11 | Archive template | Action | Prevent future use while preserving referenced versions. | Available when authorized | Destination: S30 |
| 12 | Edit template | Action | Create a new version; keep previous used versions. | Available when authorized | Destination: S32 |
| 13 | Open contract | Action | Show status and generated PDF. | Available when authorized | Destination: S33 |
| 14 | Switch tabs | Action | Templates and contracts tabs are same routed screen. | Available when authorized | Destination: S30 tab |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no templates or contracts in the selected tab; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one for the documented mutation. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Create template | Activate | Open safe template form. | S31 |
| 2 | Publish template | Activate | Activate validated version for new contracts. | S30 |
| 3 | Archive template | Activate | Prevent future use while preserving referenced versions. | S30 |
| 4 | Edit template | Activate | Create a new version; keep previous used versions. | S32 |
| 5 | Open contract | Activate | Show status and generated PDF. | S33 |
| 6 | Switch tabs | Activate | Templates and contracts tabs are same routed screen. | S30 tab |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Templates and contracts tabs show company-scoped versions and status filters.
2. Signed contract exposes no edit/version replacement action.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-09/F-CONTR-001 | Implements this screen's validated user flow and the linked source function. |
| MFG-09/F-CONTR-002 | Implements this screen's validated user flow and the linked source function. |
| MFG-09/F-CONTR-003 | Implements this screen's validated user flow and the linked source function. |
| MFG-09/F-CONTR-004 | Implements this screen's validated user flow and the linked source function. |
| MFG-09/F-CONTR-005 | Implements this screen's validated user flow and the linked source function. |
| MFG-09/F-CONTR-006 | Implements this screen's validated user flow and the linked source function. |
| MFG-09/F-CONTR-007 | Implements this screen's validated user flow and the linked source function. |
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
