# Screen Spec: S42 Merge Console

| Field | Value |
|---|---|
| Screen ID | `S42` |
| Screen name | Merge Console |
| Actor | Company Admin |
| Priority | P2 |
| Belongs to module | [MFG-10](../specs/spec-MFG-10.md) |
| Route | `/admin/merge-batches` |
| Mockup image | Don't have mockup |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The Company Admin selects eligible same-company orders into a batch, reviews the explicit demo savings calculation and transitions batch state under atomic membership rules. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

Don't have mockup

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Merge Console | Yes | Static route title. |
| 2 | Route | Navigation target | /admin/merge-batches | Yes | Access checked on server. |
| 3 | candidate filters | Field / control | company, product, material, color, print method, confirmed_at | As specified | Only confirmed, paid, signed-current-contract, opted-in, uncancelled, unbatched orders in same company and within 3 days. |
| 4 | selected_order_ids | Field / control | UUID array, minimum 2 | As specified | Lock/revalidate atomically; total quantity <=10000; one batch per order. |
| 5 | setup_cost_vnd | Field / control | integer, read-only | As specified | Demo assumption 100000; gross saving=(order_count-1)*100000. |
| 6 | customer_discount_vnd / estimated_net_saving_vnd | Field / control | integer VND | As specified | Customer discounts=sum merge discounts; net=gross-discounts; show negative value and require acknowledgement. |
| 7 | setup_minutes_saved | Field / control | integer, read-only estimate | As specified | (order_count-1)*30; does not alter customer deadline. |
| 8 | batch_status | Field / control | Planned, InProduction, Completed | As specified | Only Planned may dissolve; membership immutable after production starts. |
| 9 | Refresh candidates | Action | Query only opted-in Confirmed candidates with matching company, product, production compatibility, and merge window. | Available when authorized | Destination: S42 |
| 10 | Estimate | Action | Compute gross/net savings and setup minutes; disclose negative net and require acknowledgement. | Available when authorized | Destination: S42 |
| 11 | Create batch | Action | Require >=2; lock/revalidate all selected orders; create immutable membership. | Available when authorized | Destination: S42 |
| 12 | Start/dissolve/complete | Action | Enforce batch state transitions; dissolution only Planned; production transitions atomic. | Available when authorized | Destination: S42 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no orders eligible for merge under current policy; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one for the documented mutation. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Refresh candidates | Activate | Query only opted-in Confirmed candidates with matching company, product, production compatibility, and merge window. | S42 |
| 2 | Estimate | Activate | Compute gross/net savings and setup minutes; disclose negative net and require acknowledgement. | S42 |
| 3 | Create batch | Activate | Require >=2; lock/revalidate all selected orders; create immutable membership. | S42 |
| 4 | Start/dissolve/complete | Activate | Enforce batch state transitions; dissolution only Planned; production transitions atomic. | S42 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Promise production_due_at at confirmation +7 calendar days for standard production and +10 for merge. Setup-time savings never shorten this customer promise; if no batch forms within 3 days, release individual production at the promised merge discount. | Project implementation assumptions |
| SR-005 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Batch creation atomically revalidates >=2 eligible same-company orders and total qty <=10000.
2. Negative net savings are visible and require admin acknowledgement; no order price/deadline changes on dissolve.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-10/F-MER-004 | Implements this screen's validated user flow and the linked source function. |
| MFG-10/F-MER-005 | Implements this screen's validated user flow and the linked source function. |
| MFG-10/F-MER-006 | Implements this screen's validated user flow and the linked source function. |
| MFG-10/F-MER-007 | Implements this screen's validated user flow and the linked source function. |
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
