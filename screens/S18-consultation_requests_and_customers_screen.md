# Screen Spec: S18 Consultation Requests and Customers

| Field | Value |
|---|---|
| Screen ID | `S18` |
| Screen name | Consultation Requests and Customers |
| Actor | Company Admin |
| Priority | P2 |
| Belongs to module | [MFG-05](../specs/spec-MFG-05.md) |
| Route | `/admin/consultations?tab=requests,customers` |
| Mockup image | Don't have mockup |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The Company Admin switches between paid design requests awaiting assignment and company-scoped consultation/customer records. Only active same-company consultants are eligible for assignment. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

Don't have mockup

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Consultation Requests and Customers | Yes | Static route title. |
| 2 | Route | Navigation target | /admin/consultations?tab=requests,customers | Yes | Access checked on server. |
| 3 | tab | Field / control | enum: requests or customers; default requests | As specified | Requests show paid DesignRequest id, status, product, customer display name, requested_deadline and committed_due_at; customers show consultation id and CRM status. |
| 4 | status | Field / control | allowlisted request or CRM status enum | As specified | Filter applies to the selected tab lifecycle only; design request and CRM states remain distinct. |
| 5 | product_id | Field / control | optional UUID | As specified | Same-company product filter on requests tab; inaccessible IDs return 404. |
| 6 | requested_deadline_from/to | Field / control | optional local dates | As specified | Inclusive start and exclusive end; reject reversed range; display in Asia/Ho_Chi_Minh. |
| 7 | page / page_size / sort | Field / control | integer / integer / enum | As specified | documented pagination bounds; sort allowlist is requested_deadline, created_at or status. |
| 8 | customer_id / company_id | Field / control | server-derived UUIDs | As specified | Never accepted as scope input; internal notes visible to authorized staff only. |
| 9 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid filters; 403 prohibited action; 404 inaccessible request/customer; 429 rate limit; 503 dependency failure. |
| 10 | Assign paid request | Action | Open assignment with active same-company consultants. | Available when authorized | Destination: S19 |
| 11 | Open request | Action | View status/details and authorized notes. | Available when authorized | Destination: S21 |
| 12 | Switch tab | Action | Preserve company filters and route state. | Available when authorized | Destination: S18 tab |
| 13 | Open customer record | Action | Show staff-only company-scoped consultation context. | Available when authorized | Destination: S18 customers tab |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no paid requests awaiting assignment or customer consultations; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one for the documented mutation. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Assign paid request | Activate | Open assignment with active same-company consultants. | S19 |
| 2 | Open request | Activate | View status/details and authorized notes. | S21 |
| 3 | Switch tab | Activate | Preserve company filters and route state. | S18 tab |
| 4 | Open customer record | Activate | Show staff-only company-scoped consultation context. | S18 customers tab |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Unpaid request is not assignable; Paid request appears as eligible within its company only.
2. Customer tab excludes other companies and internal notes remain staff-only.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-08/F-ORD-001 | Implements this screen's validated user flow and the linked source function. |
| MFG-08/F-ORD-002 | Implements this screen's validated user flow and the linked source function. |
| MFG-08/F-ORD-003 | Implements this screen's validated user flow and the linked source function. |
| MFG-08/F-ORD-004 | Implements this screen's validated user flow and the linked source function. |
Additional linked modules: [MFG-08](../specs/spec-MFG-08.md).

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
