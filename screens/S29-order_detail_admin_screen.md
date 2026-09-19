# Screen Spec: S29 Order Detail (Admin)

| Field | Value |
|---|---|
| Screen ID | `S29` |
| Screen name | Order Detail (Admin) |
| Actor | Company Admin/Assigned Consultant |
| Priority | P2 |
| Belongs to module | [MFG-07](../specs/spec-MFG-07.md) |
| Route | `/admin/orders/{order_id}` |
| Mockup image | Don't have mockup |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The Company Admin sees any same-company order; a consultant sees only an order tied to their current assignment. Mutations follow order state and expected_version. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

Don't have mockup

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Order Detail (Admin) | Yes | Static route title. |
| 2 | Route | Navigation target | /admin/orders/{order_id} | Yes | Access checked on server. |
| 3 | order_id / snapshots | Field / control | UUID and read-only data | As specified | Same company or assigned consultant only; price, address, design and contract snapshots cannot be edited. |
| 4 | target_status / expected_version | Field / control | required mutation inputs | As specified | Permit only the next fulfillment state: Confirmed -> InProduction -> Shipped -> Delivered from the current version. |
| 5 | carrier / tracking_number | Field / control | strings required for Shipped | As specified | Server records shipped_at; Delivered records delivered_at. |
| 6 | cancellation_reason | Field / control | string 1..500, Company Admin only | As specified | Require current cancellation eligibility; assigned consultants cannot cancel. |
| 7 | contract_action | Field / control | Company Admin only | As specified | Open S33 to create/revise an unsigned version; never mutate a Signed contract. |
| 8 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 9 | Generate contract | Action | Snapshot current order/customer data and chosen template. | Available when authorized | Destination: S33 |
| 10 | Update fulfillment | Action | Apply only next fulfillment transition; consultant assignment guard; record tracking/dates. | Available when authorized | Destination: S29 |
| 11 | Cancel order | Action | Company Admin with reason and eligibility; consultants cannot cancel. | Available when authorized | Destination: S28 |
| 12 | Merge batch | Action | Open batch console. | Available when authorized | Destination: S42 |

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
| 1 | Generate contract | Activate | Snapshot current order/customer data and chosen template. | S33 |
| 2 | Update fulfillment | Activate | Apply only next fulfillment transition; consultant assignment guard; record tracking/dates. | S29 |
| 3 | Cancel order | Activate | Company Admin with reason and eligibility; consultants cannot cancel. | S28 |
| 4 | Merge batch | Activate | Open batch console. | S42 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Only valid next fulfillment transition is applied; shipment requires carrier, tracking and timestamp.
2. Consultant cannot cancel order or bypass payment/contract gates; stale order version returns 409.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-07/F-ORD-005 | Implements this screen's validated user flow and the linked source function. |
| MFG-07/F-ORD-006 | Implements this screen's validated user flow and the linked source function. |
| MFG-07/F-ORD-007 | Implements this screen's validated user flow and the linked source function. |
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
