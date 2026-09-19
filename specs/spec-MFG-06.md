# MFG-06 — Checkout, Order Creation, and Payment

**Contract:** Complete-system target. Shared contracts D01–D03 and D06–D08, D11–D12 in [system-decisions.md](../docs/system-decisions.md) are authoritative. Human facts belong only in [user-input-needed.md](../docs/user-input-needed.md). Preserve original function meanings: F-PAY-001 checkout, 002 order summary, 003 create order, 004 gateway request, 005 callback/reconciliation, 006 receipt/result.

## Actors and boundaries

Authenticated Customer checks out one saved self-design or delivered consultant design for one Published product, one company, and one shipping address. This module owns quote/checkout, order creation and payment request initiation. Order tracking, cancellation and fulfillment after submission belong to MFG-07. Contract generation/signing belongs to MFG-09. Design service checkout uses purpose SERVICE and an existing AwaitingPayment request from MFG-05; it cannot create design requests. Customer identity and price come from server session and snapshots, never submitted IDs or totals. Staff cannot check out on behalf of a customer.

`Quote`: UUID quote_id, company_id, customer_id, product_id/product_version, design_id/design_version, quantity_by_size, address snapshot, merge preference/policy version, subtotal_vnd, merge_discount_vnd, shipping_vnd, merge_fee_vnd, tax_vnd, total_vnd, expires_at (30 minutes), version. `Order`: immutable D06 identity and snapshots with initial status PendingContract, nullable contract_id/batch_id. Payment transaction schema and state follow D08, exactly one resource purpose ORDER or SERVICE. Amounts and quantities are integers.

## Function contracts

| FR / function | Inputs and output | Validation, effects, failures |
|---|---|---|
| FR-001 / F-PAY-001 Checkout View | Authenticated customer session; route product_id/design_id; no business body. Output S22 checkout form view model with saved orderable design, product options, size quantities, shipping-address fields, merge option and current product/rule version. | Customer identity from session; design is owned and Saved/Delivered, product Published, same company. Draft/foreign/incompatible design is 404 or 422. Capacity is checked at quote/submit; no inventory reservation. Forms expose allowed choices only. |
| FR-002 / F-PAY-002 Order Summary View | `product_id`, `design_id`, `quantity_by_size` (positive integer quantities, total 1..10000), shipping address `{recipient_name,phone,address_line,ward,province,country}`, merge opt-in/policy version; output immutable quote preview with quote_id, full breakdown and 30-minute expiry. | Server recomputes using stored price/rules: subtotal=sum(qty*(unit_price+option surcharge)); discount=floor(subtotal*5/100) if eligible opted-in else 0; shipping from quote policy snapshot (default 30000), merge fee 0, tax 0; total=subtotal-discount+shipping. Validate D06 address lengths and VN phone. Require same-company Published product and current orderable design/product versions, available manufacturing capacity, and eligible merge option. Changed/expired quote requires new quote and customer review. Errors 422 invalid fields, 409 stale version or changed quote; 422 CAPACITY_EXCEEDED when quantity exceeds max_units_per_order. This is the one authoritative amount shown in S23/S25/S34/S35. |
| FR-003 / F-PAY-003 Create Order Logic | `quote_id`, expected quote version, Idempotency-Key UUID, explicit submit confirmation; output order UUID/status PendingContract, immutable line/address/price snapshots, merge preference/policy version, created_at/version. | Customer owns unexpired quote; revalidate product/design/rules/capacity and lock quote before atomic order creation. Client cannot override total, company, customer or snapshots. Same key/payload returns original order; changed payload 409. A unique consumed_quote_id constraint also returns the original order when the same quote is submitted under a different key. No batch created at checkout. Notify same-company Admin that the new PendingContract order awaits explicit contract generation in MFG-09; no automatic signing or implicit admin approval. Payment is not yet permitted. |
| FR-004 / F-PAY-004 Payment Request Gen | For ORDER: order_id, Idempotency-Key. For SERVICE: request_id, purpose=SERVICE, Idempotency-Key. Output payment_id, provider_reference, hosted redirect URL and 15-minute expiry. | ORDER must have current Signed contract and AwaitingPayment state; SERVICE must be AwaitingPayment. Derive amount from immutable payable snapshot. One active Pending attempt per resource; repeat initiation reuses it; after failure create a new provider reference. Return validated VNPay redirect/hash from server adapter. Provider failure returns 503/no false payment and does not fail order/request. |
| FR-005 / F-PAY-005 IPN Handler Logic | Provider-signed VNPay GET query event (preserve raw query parameters for adapter validation); output acknowledged event/result and resulting payment/resource/refund statuses. Also exposes authorized admin reconciliation/refund operation: payment_id, expected_version, Idempotency-Key for full refund only. | Verify signature, merchant, reference, amount, currency, unique provider transaction ID; server notification is authoritative. Lock resource and settle once. Duplicate event is no-op. Valid late success may promote Failed/Expired to Succeeded, never downgrade; cancelled/expired resource or competing settlement records funds and starts full refund without resurrection. Payment success changes ORDER AwaitingPayment→Confirmed (MFG-07) or SERVICE AwaitingPayment→Paid (MFG-05). Failed payment does not fail order. Refund states None→Pending→Succeeded/Failed, success only after provider verification/reconciliation; failed refund remains retryable/visible. Unknown/mismatched callback has no business effect and creates redacted audit event. Reconcile unresolved attempts by provider query after timeout/outage. |
| FR-006 / F-PAY-006 Receipt View | Browser return transaction_id/payment_id and authenticated session; output S35 order or S16 service receipt/result view model with current status, amount, purpose, safe next route and retry/poll guidance. | Browser return opens receipt and polls server; it never marks paid. Check transaction ownership. Pending/outage shows Processing; Success only from verified callback; Failed/Expired can initiate a fresh attempt if resource remains payable. Include refund status when present. Unknown/inaccessible transaction 404; never trust submitted `payment_status`, amount, billing, customer or provider result. |

## State, integration and security

Order lifecycle: quote→Order(PendingContract) via F-PAY-003; only MFG-09 signing changes to AwaitingPayment; verified full settlement changes it to Confirmed. A failed attempt has no order transition. Payment attempt states Pending→Succeeded/Failed/Expired, with verified late success allowed from Failed/Expired. Refund states None→Pending→Succeeded/Failed; only full-amount refund is supported. One pending attempt per resource; same amount is shown in quote, summary, contract, and payment screens. Provider transaction/event IDs are permanently unique; idempotency keys retained at least 7 days. Use transaction locks, unique constraints and outbox for effects.

```mermaid
sequenceDiagram
  actor C as Customer
  participant W as Checkout/Payment
  participant K as Contract service
  participant V as VNPay
  C->>W: Request quote and inspect breakdown
  C->>W: Submit quote with idempotency key
  W->>W: Revalidate and create PendingContract order
  W-->>K: PendingContract available for Company Admin generation
  K-->>C: Ready contract for review/signature
  C->>K: Sign contract
  K->>W: Signed event; order becomes AwaitingPayment
  C->>W: Request payment
  W-->>C: Hosted VNPay redirect
  V->>W: Signed server notification
  W->>W: Verify, deduplicate, settle + outbox
  C->>W: Return/poll receipt (read-only)
```

VNPay adapter follows the versioned [protocol contract](../docs/integrations/vnpay.md), including sandbox signature, amount, return and notification checks. Merchant credentials are environment settings and never documented here.

## Acceptance and screens

Acceptance: checkout rejects another customer's or draft design; invalid address, unsupported options or insufficient capacity blocks quote/order without write; exact fixed formula and amount appears consistently on S23/S25/S34/S35; quote expires at 30 minutes and changed product/design rules require explicit requote/review; duplicate order submit returns the same order; altered payload with same key conflicts; checkout creates PendingContract and no batch; unsigned order cannot initiate ORDER payment; duplicate/invalid callbacks never double-confirm; callback amount/signature mismatch has no business effect; browser success URL alone never settles; failure leaves order AwaitingPayment and allows fresh attempt; late/cancelled-resource funds are recorded and refunded without resurrection; refund failure remains visible/retryable; email/outbox failure cannot reverse order/payment state.

Screens: S22 captures quantities/shipping and requests a quote; S23 records merge preference; S24 displays the accepted policy; S25 reviews the immutable quote and submits the order; S16 shows service payment/result; S35 shows order payment/receipt; S27 shows customer refund status; S36/S37 provide Company Admin transaction reconciliation/refund views; S38 shows notifications. Traceability: F-PAY-001..006 / FR-001..006; UC-C05 Finalize Order and UC-C12 Make Payment. MFG-07 handles post-submission order management.
