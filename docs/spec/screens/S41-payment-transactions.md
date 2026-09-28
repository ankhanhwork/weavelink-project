# Screen Spec: S41 Payment Transaction List

| Field | Value |
|---|---|
| Screen ID | `S41` |
| Screen name | Payment Transaction List |
| Actor | Sales Admin |
| Priority | Should (MVP); in-system refund actions are Could |
| Belongs to module | [MFG-06](../specs/spec-MFG-06.md) |
| Route | `/admin/payments` |
| Mockup image | img/S41-01-payment-transactions.png |
| Status | Resolved implementation specification |


## 1. Purpose

**Shown when:** The Sales Admin lists Dony payment transactions and refunds using provider status, purpose, amount, timestamps and order/request reference filters. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

**MVP scope:** view and reconcile DEPOSIT/BALANCE transactions only. MVP creates no in-system refunds (MFG-06 BR-019); refund fields show `None` or the `manual_refund_required` flag, and refund actions below are Could.

## 2. Mockup

![VNPay order deposit and balance transactions in the Sales Admin console](img/S41-01-payment-transactions.png)

The regenerated view follows the original neighboring payment console layout and uses synthetic transactions. VNPay is the only provider; DEPOSIT and BALANCE are order payment purposes, and settlement remains server-authoritative.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Payment Transaction List | Yes | Static route title. |
| 2 | Route | Navigation target | /admin/payments | Yes | Access checked on server. |
| 3 | purpose | Field / control | enum: DEPOSIT, BALANCE | As specified | Purpose is immutable and belongs to one order; no SERVICE or generic ORDER purpose. |
| 4 | status / refund_status | Field / control | allowlisted transaction/refund enums | As specified | Filter Pending, Succeeded, Failed or Expired where applicable. |
| 5 | date_from / date_to | Field / control | optional local dates | As specified | Inclusive start, exclusive end; display Asia/Ho_Chi_Minh. |
| 6 | rows | Field / control | payment_id, resource_id, integer amount_vnd, currency, status, created_at | As specified | Mask provider references; omit card secrets and other-Dony business data. |
| 7 | page / page_size / sort | Field / control | integer / integer / enum | As specified | documented pagination bounds; sort by created_at, amount_vnd or status. |
| 8 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 403 prohibited; 404 inaccessible payment; 422 invalid filters; 503 dependency failure. |
| 9 | Open transaction | Action | Load redacted payment/refund detail. | Available when authorized | Destination: S42 |
| 10 | Filter list | Action | Preserve allowlisted filters and pagination on refresh/back. | Available when authorized | Destination: S41 |

## 4. States

**Loading, access, errors and retry:** Show a labelled Loading state while reads resolve. A missing or inaccessible route returns a safe 401/403/404 without disclosing protected records. Error states show the API code, message, field_errors and request_id while preserving safe input. Retry transient reads; retry a mutation only with the original idempotency key and identical payload. Preserve safe user input after recoverable failures.

| State | What the user sees | Trigger |
|---|---|---|
| Empty | Show “No transactions” for selected order/date filters and retain them. | Screen has no eligible or matching record |
| Success | Refresh the committed Payment Transaction List data and show the next action permitted by its lifecycle and actor. | Valid action commits |
| Conflict | The Payment Transaction List data or lifecycle changed concurrently; reload authoritative state and do not replay a stale mutation. | Stale version, duplicate or invalid lifecycle transition |
## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Open transaction | Activate | Load redacted payment/refund detail. | S42 |
| 2 | Filter list | Activate | Preserve allowlisted filters and pagination on refresh/back. | S41 |

Portal: Sales Admin. Route: /admin/payments. Back preserves the originating route and filters. 

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Check access and ownership on the server; never trust submitted customer, company, role, price, stage or provider status. Apply the documented 401/403/404 behavior and field rules. | Project baseline |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected versions and idempotency keys where specified. | Project baseline |
| SR-003 | Apply the owning module's lifecycle and validation rules; preserve immutable submitted snapshots and design versions. | Project baseline |
| SR-004 | Use documented project assumptions; do not invent factual company, author, client-approval or course identifiers. | Project baseline |

### Acceptance scenarios

1. List contains Dony DEPOSIT/BALANCE attempts with order link, masked provider references and page bounds.
2. Payment records belong to Dony's single operating system; customer ownership is still checked on customer-facing views, and pending attempts are not represented as revenue.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-06/F-PAY-005 | **Make Payment** — Verify and deduplicate provider notifications by order and purpose; accept settlement once, perform the purpose-specific order transition, and support authorized reconciliation/refunds without resurrecting cancelled orders. |


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
- [x] Responsive and accessibility requirements are documented in this screen.
- [x] No unresolved screen-level decisions remain.
