# Screen Spec: S26 Customer Order List

| Field | Value |
|---|---|
| Screen ID | `S26` |
| Screen name | Customer Order List |
| Actor | Customer owner |
| Priority | P1 |
| Belongs to module | [MFG-07](../specs/spec-MFG-07.md) |
| Route | `/orders` |
| Mockup image | `img/S26-customer_order_list_screen.png` |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The customer lists only orders they own, with status, order number, placed date, total VND and allowlisted filters. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S26 historical reference](img/S26-customer_order_list_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Customer Order List | Yes | Static route title. |
| 2 | Route | Navigation target | /orders | Yes | Access checked on server. |
| 3 | page/page_size/status | Field / control | integer page>=1, size1..100 default20; canonical status enum | As specified | Allowlist `AwaitingDigitalApproval`, `DigitalDesignApproved`, `SampleInPreparation`, `SampleShipped`, `PendingContract`, `AwaitingDeposit`, `Confirmed`, `InProduction`, `Shipped`, `DeliveredAwaitingBalance`, `Completed`, `Cancelled`; allow date sorting. |
| 4 | Rows | Field / control | order_id UUID, created_at, status, total_vnd integer, product summary. | As specified | Rows: order_id UUID, created_at, status, total_vnd integer, product summary. |
| 5 | ownership_scope | Field / control | session-derived, read-only | As specified | Return only the current customer's orders; filters cannot broaden ownership. |
| 6 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 7 | Open order | Action | Load current customer's order detail and actions. | Available when authorized | Destination: S27 |
| 8 | Filter/sort | Action | Query only owned orders. | Available when authorized | Destination: S26 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Load the S26 Customer Order List view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | Show no orders owned by this customer; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Return a safe 401/403/404 for S26 Customer Order List without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S26 Customer Order List, show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S26 Customer Order List; retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh S26 Customer Order List from the committed server response, expose only the next role/state-allowed action and announce the result via aria-live. | Mutation commits |
| Conflict | For a stale S26 Customer Order List version or lifecycle state, reload authoritative data, explain the conflict and require explicit review before resubmission. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Open order | Activate | Load current customer's order detail and actions. | S27 |
| 2 | Filter/sort | Activate | Query only owned orders. | S26 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Sales Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks internal role, customer ownership and staff assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Sales Admin, S20 for Sales, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Customer sees only own orders with the current design/sample/contract/payment/fulfillment status and immutable VND total.
2. Opening another customer's order id returns 404 without revealing its existence.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-07/F-ORD-001 | UI touchpoint for **Order List View**; this screen defines the visible action/result, while the module spec owns server authorization, validation and persistence. |
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
