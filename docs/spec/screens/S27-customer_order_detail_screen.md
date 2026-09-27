# Screen Spec: S27 Customer Order Detail

| Field | Value |
|---|---|
| Screen ID | `S27` |
| Screen name | Customer Order Detail |
| Actor | Customer owner |
| Priority | P1 |
| Belongs to module | [MFG-07](../specs/spec-MFG-07.md) |
| Route | `/orders/{order_id}` |
| Mockup image | `img/S27-customer_order_detail_screen.png` |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The customer sees one owned made-to-order order’s immutable design, physical-sample, quantity, delivery, price, contract, deposit, balance and production snapshots, with only the action owned by the current lifecycle state enabled. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S27 historical reference](img/S27-customer_order_detail_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Customer Order Detail | Yes | Static route title. |
| 2 | Route | Navigation target | /orders/{order_id} | Yes | Access checked on server. |
| 3 | order_id / item_snapshot | Field / control | UUID and read-only snapshot | As specified | Owner only; show immutable quantities, address and price breakdown. |
| 4 | status enum | Field / control | canonical MFG-06 lifecycle plus Cancelled | As specified | `AwaitingDigitalApproval`, `DigitalDesignApproved`, `SampleInPreparation`, `SampleShipped`, `PendingContract`, `AwaitingDeposit`, `Confirmed`, `InProduction`, `Shipped`, `DeliveredAwaitingBalance`, `Completed`, `Cancelled`. |
| 5 | design / sample / contract / deposit / balance / refund / batch | Field / control | read-only related projections | As specified | Show version/evidence and authoritative current states; never infer state from email or browser return. |
| 6 | cancellation_eligibility / reason | Field / control | server boolean plus required string 1..500 | As specified | Allow eligible pre-deposit states or pre-production unbatched Confirmed; captured funds start policy-based refund. |
| 7 | carrier / tracking_number / shipped_at / delivery_evidence_verified_at / auto_confirm_at / received_at | Fulfillment timeline | Read-only shipment and receipt evidence | By lifecycle state | Verified delivery proof and countdown are visible while Shipped; receipt timestamp appears after Customer confirmation or scheduled auto-confirmation at DeliveredAwaitingBalance/Completed. |
| 8 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 9 | Cancel order | Action | Confirm; enforce state/no-batch/preproduction; schedule policy-based refund for captured funds. | Available when authorized | Destination: S26 |
| 10 | Approve digital design | Action | Bind current design/quote version and advance `AwaitingDigitalApproval→DigitalDesignApproved`; stale version requires review. | Only in AwaitingDigitalApproval | Destination: S27 |
| 11 | Approve received sample | Action | Confirm physical receipt and approval of the current sample/design version; advance `SampleShipped→PendingContract`. | Only in SampleShipped | Destination: S27 |
| 12 | Request sample revision | Action | Submit reason and return through a new immutable digital-design/quote approval cycle; do not overwrite prior evidence. | Only in SampleShipped | Destination: S27 |
| 13 | View contract | Action | Open the authorized current contract only after sample approval. | Only in PendingContract or later | Destination: S34 |
| 14 | Pay deposit | Action | Open exact `DEPOSIT` amount only after current contract is Signed and order is `AwaitingDeposit`. | Only in AwaitingDeposit | Destination: S35 |
| 15 | Confirm delivery receipt | Action | Record Customer receipt evidence and immediately advance `Shipped→DeliveredAwaitingBalance`; no dispute action is in MVP. | Only in Shipped | Destination: S27 |
| 16 | Pay remaining balance | Action | Open exact positive `BALANCE` amount only after receipt is recorded; a zero balance follows automatic completion without a payment action. | Only in DeliveredAwaitingBalance with positive balance | Destination: S35 |

When staff records verified carrier/POD evidence, S27 shows the evidence timestamp and a three-calendar-day auto-confirmation countdown. There is no dispute button or dispute state in the MVP. If the Customer does not confirm before expiry, the scheduled event records receipt and changes the order to `DeliveredAwaitingBalance`.

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Load the S27 Customer Order Detail view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | No Customer Order Detail records match the current route/filter; preserve inputs and show only the screen’s authorized next action. | Screen has no eligible or matching record |
| Forbidden/not found | Return a safe 401/403/404 for S27 Customer Order Detail without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S27 Customer Order Detail, show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S27 Customer Order Detail; retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh authoritative order timeline; no dispute action exists, and proof of delivery does not immediately change Shipped. | Valid action commits |
| Conflict | Order changed since load: refresh events and suppress actions invalid for the new status. | Stale version, duplicate or invalid lifecycle transition |
## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Cancel order | Activate | Confirm eligibility and schedule a policy-based refund for captured funds. | S26 |
| 2 | Approve digital design | Activate | Bind reviewed design/quote versions and request sample preparation. | S27 |
| 3 | Approve or revise received sample | Activate | Persist immutable approval/revision evidence and select the corresponding next state. | S27 |
| 4 | View contract | Activate | Open the current sample-bound contract. | S34 |
| 5 | Pay deposit or remaining balance | Activate | Pass server-derived purpose and exact payable amount. | S35 |
| 6 | Confirm delivery receipt | Activate | Record receipt before exposing BALANCE payment. | S27 |

Portal: Customer owner. Route: /orders/{order_id}. Back preserves the originating route and filters. Fallback: Customer→S26; Sales Admin→S28; Sales→S20; System Admin→S41; Guest→S01. Enforce role, ownership and assignment before rendering.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Digital approval binds the reviewed version; stale design/quote returns 409 and cannot start sample preparation.
2. Only the current shipped sample can be approved or revised; approval opens contract generation, while revision preserves history and restarts digital approval.
3. Cancellation succeeds only in an allowed pre-production unbatched state; captured funds use the stored refund policy.
4. Deposit payment is visible only in `AwaitingDeposit`; remaining-balance payment is visible only in `DeliveredAwaitingBalance` after receipt evidence and when the balance is positive; zero balance completes through the authoritative MFG-06 path without a provider attempt.
5. Cancellation after batch assignment or production start returns 409 and leaves order unchanged.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-07/F-ORD-002 | **Order Detail View** — Show only the authenticated customer’s authorized order snapshot, lifecycle timeline, contract/payment/refund summaries and shipment tracking; never recalculate historical prices. |
| MFG-07/F-ORD-003 | **Cancel eligible order and request refund** — Allow cancellation only in permitted pre-production states, require a reason and idempotency/version checks, and request a policy-based refund without allowing the client to set its amount. |
| MFG-07/F-ORD-004 | **Cancel Notify Logic** — Notify the customer and Dony Sales Admin after committed cancellation; deduplicate events and include refund status when relevant. |


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
