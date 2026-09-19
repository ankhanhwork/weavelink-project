# Screen Spec: S25 Order Summary

| Field | Value |
|---|---|
| Screen ID | `S25` |
| Screen name | Order Summary |
| Actor | Customer owner |
| Priority | P1 |
| Belongs to module | [MFG-06](../specs/spec-MFG-06.md) |
| Route | `/orders/summary?quote_id={id}` |
| Mockup image | `img/S25-order_summary_screen.png` |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The customer reviews an unexpired server quote with integer VND line amounts, delivery address, selected merge policy and expiry before submitting the order. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S25 historical reference](img/S25-order_summary_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Order Summary | Yes | Static route title. |
| 2 | Route | Navigation target | /orders/summary?quote_id={id} | Yes | Access checked on server. |
| 3 | quote_id | Field / control | UUID | As specified | quote_id: UUID; server quote lasts 30 minutes and binds product/design/policy versions. |
| 4 | subtotal_vnd | Field / control | sum(quantity*(unit_price_vnd+option_surcharge_vnd)), integer. | As specified | subtotal_vnd: sum(quantity*(unit_price_vnd+option_surcharge_vnd)), integer. |
| 5 | merge_discount_vnd | Field / control | floor(subtotal*5/100) when opted-in | As specified | merge_discount_vnd: floor(subtotal*5/100) when opted-in; else 0. |
| 6 | price_breakdown | Field / control | integer VND, read-only | As specified | Show snapshotted subtotal, discount, shipping, merge fee, tax and total; default shipping is 30000, merge fee/tax are 0. |
| 7 | quote_id / expected_version / Idempotency-Key | Field / control | required submission contract | As specified | Never submit a client total; an expired/superseded quote returns to requote and explicit review. |
| 8 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 9 | Submit order | Action | Revalidate unexpired quote and versions; atomically create PendingContract order/snapshots with idempotency. | Available when authorized | Destination: S34 |
| 10 | Edit quantities/address | Action | Requote and show changed breakdown before submit. | Available when authorized | Destination: S22 |
| 11 | Change merge preference | Action | Requote with explicit preference. | Available when authorized | Destination: S23 |

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
| 1 | Submit order | Activate | Revalidate unexpired quote and versions; atomically create PendingContract order/snapshots with idempotency. | S34 |
| 2 | Edit quantities/address | Activate | Requote and show changed breakdown before submit. | S22 |
| 3 | Change merge preference | Activate | Requote with explicit preference. | S23 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Valid unexpired quote submission creates one PendingContract order and immutable address/price snapshots.
2. Expired quote or changed product/design version requires requote and review; duplicate same key returns same order.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-06/F-PAY-002 | Implements this screen's validated user flow and the linked source function. |
| MFG-06/F-PAY-003 | Implements this screen's validated user flow and the linked source function. |
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
