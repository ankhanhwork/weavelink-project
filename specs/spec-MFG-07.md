# Spec Document: Order Management

| Field | Value |
| --- | --- |
| Module ID | `MFG-07` |
| Module name | Order Management |
| Spec version | v1.0 |
| Author (team member) | Group B |
| Date | 2026-09-19 |
| Status | Draft |
| Approved by (Client role) | No approver identified |
| DBIZ2 source | Function List `MFG-07`, No. 53–59, `F-ORD-001`–`F-ORD-007`; use cases UC-C08 Track Order, UC-C07 Cancel Order, UC-S04 Update Status; screens S26, S27, S28, S29, S30, S38 |

---

## 1. Purpose and scope (mandatory)

Customers can view their orders and follow progress. Company Admins and an assigned same-company Sales Consultant can advance fulfillment; an owning Customer or same-company Company Admin can cancel when the order state permits. This module consumes order, payment, refund and contract events; it does not create orders, settle payment, or generate contracts.

MVP priority: **Should**, per the project MVP Scope. The module is documented for the complete system. Order creation/payment belongs to MFG-06; contract generation/signature to MFG-09; production batches to MFG-10. MFG-07 function IDs must be qualified with `MFG-07/` because MFG-08 independently reuses `F-ORD-001`–`F-ORD-007`.

## 2. Actors (mandatory)

| Actor | Role in this module | Where it comes from |
| --- | --- | --- |
| Customer | Views own orders/details and cancels own eligible order | MFG-07 resolved contract; UC-C07/UC-C08 |
| Company Admin | Views same-company orders, cancels with reason, advances fulfillment | MFG-07 resolved contract; UC-S04 |
| Sales Consultant | Advances fulfillment only for customers actively assigned to the consultant in the same company; cannot cancel | MFG-07 resolved contract |
| System / MFG-06 / MFG-10 | Supplies verified payment/refund and batch events; not an interactive actor | Inter-module contracts |

## 3. User scenarios and acceptance criteria (mandatory)

### US-1: Track order status (Should)

As a Customer, I can list and inspect my own orders, status timeline, immutable price/address snapshot, payment/refund summary and shipment details. Staff views are restricted to their company and authorized role.

1. **Given** the customer has no orders, **when** the list is loaded, **then** an empty paginated result is returned.
2. **Given** an order ID is not accessible to the actor, **when** its detail is requested, **then** the response is 404 and discloses no object data.
3. **Given** catalog prices or address data later change, **when** an old order is viewed, **then** the stored snapshot is shown without recalculation.

### US-2: Cancel order (Should)

An owning Customer or same-company Company Admin can cancel in an allowed state. A Company Admin supplies a reason. Consultants cannot cancel.

1. **Given** an order is PendingContract or AwaitingPayment, **when** an authorized actor cancels it, **then** it becomes Cancelled.
2. **Given** an order is Confirmed, **when** it is not yet in production and has no active batch, **then** an authorized actor may cancel it.
3. **Given** a paid order is cancelled, **when** cancellation commits, **then** the order remains Cancelled and MFG-06 receives a full-refund request; the order is retained and inventory is not restocked.
4. **Given** an order is in production, shipped, delivered, or linked to a batch, **when** cancellation is attempted, **then** it is rejected with 409; a Planned batch must first be dissolved by an Admin.
5. **Given** cancellation races with production or batch assignment, **when** both mutations contend, **then** one commits and the other returns 409.

### US-3: Update order status (Should)

Company Admin or the consultant actively assigned to the customer in the same company advances fulfillment through valid successive states.

1. **Given** verified payment and a Confirmed order, **when** authorized staff advance it, **then** only Confirmed→InProduction→Shipped→Delivered is accepted.
2. **Given** the target is Shipped, **when** carrier and tracking number are valid, **then** the server records shipped_at and makes the tracking information available.
3. **Given** a status event commits, **when** notification delivery is delayed or fails, **then** committed status remains visible in the inbox and email is retryable.
4. Duplicate commands are idempotent; stale versions and skipped transitions return 409.

### Edge cases

- Invalid pagination/filter input returns 400; invalid cancellation fields return 422.
- Unauthorized object identifiers return 404; authenticated but prohibited actions return 403.
- Email failure never rolls back committed order or notification state.

## 4. Flows (mandatory)

### 4.1 Usage flow

Customer opens order history → selects an order → server checks ownership → renders stored order snapshot and timeline. For cancellation, server checks actor, state, batch membership and expected version → commits Cancelled → emits refund request when paid and a notification event. For fulfillment, authorized staff advance one valid state at a time; Shipped requires carrier and tracking number.

### 4.2 Sequence for the main flow

```mermaid
stateDiagram-v2
  [*] --> PendingContract
  PendingContract --> AwaitingPayment: current contract signed
  AwaitingPayment --> Confirmed: verified full payment
  Confirmed --> InProduction
  InProduction --> Shipped
  Shipped --> Delivered
  PendingContract --> Cancelled
  AwaitingPayment --> Cancelled
  Confirmed --> Cancelled: eligible and unbatched
```

## 5. Functional requirements (mandatory)

FR identifiers are local to MFG-07. Access is server-checked: customers require ownership and staff require same-company authorization. Unauthenticated, prohibited and inaccessible requests return 401, 403 and 404 respectively. Mutations use UUIDs, UTC timestamps, expected-version checks and idempotency. Notifications use a transactional outbox, retry policy, and do not roll back committed state.

| FR ID | DBIZ2 Subfunction ID | Requirement (system MUST ...) | Actor | Priority |
| --- | --- | --- | --- | --- |
| FR-001 | F-ORD-001 | List own orders with pagination and allowlisted status/date filters; default newest first; empty results are valid. | Customer | Should |
| FR-002 | F-ORD-002 | Return an authorized order snapshot, timeline, contract/payment/refund summaries and tracking details without recalculating historical prices. | Customer / same-company staff | Should |
| FR-003 | F-ORD-003 | Cancel eligible orders with trimmed 1–500 character reason, expected_version and Idempotency-Key; retain order and request full refund through MFG-06 when paid. | Owning Customer / same-company Company Admin | Should |
| FR-004 | F-ORD-004 | Notify customer and same-company management after cancellation commit; deduplicate recipients/events and include refund status when relevant. | System | Should |
| FR-005 | F-ORD-005 | Provide paginated same-company admin dashboard with allowlisted status/date/customer filters and counts. | Company Admin | Should |
| FR-006 | F-ORD-006 | Advance only Confirmed→InProduction→Shipped→Delivered; require same-company Admin or actively assigned consultant; Shipped requires carrier, tracking_number and server shipped_at. | Company Admin / assigned Sales Consultant | Should |
| FR-007 | F-ORD-007 | Notify order owner after committed status change with timestamp and safe tracking link; suppress duplicates and retry email. | System | Should |

### 5.1 Input / Output contract

| FR ID | Input field | Type | Required | Output field | Type | Notes / validation |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | page, page_size, filters, sort | Integer / allowlisted values | Optional | order summaries, total, page, page_size | Paginated object | page ≥1; page_size 1–100 |
| FR-002 | order_id, session | UUID / session | Yes | authorized order snapshot and timeline | Object | Own customer or same-company staff; inaccessible ID 404 |
| FR-003 | order_id, reason_for_cancellation, expected_version, Idempotency-Key | UUID, string, integer, key | Yes | status, refund workflow reference | Object | Valid transitions only; duplicate key replays |
| FR-004 | committed cancellation event | Internal event | Yes | notification/outbox IDs | UUIDs | After commit; deduplicated |
| FR-005 | filters, page, page_size | Allowlisted values / integers | Optional | company order list and counts | Paginated object | Same-company only |
| FR-006 | order_id, target status, carrier, tracking_number, expected_version, Idempotency-Key | UUID, enum, strings, integer, key | Yes | updated order and timeline | Object | Carrier/tracking required for Shipped |
| FR-007 | committed status event | Internal event | Yes | durable notification/outbox IDs | UUIDs | After commit; inbox authoritative |

### 5.2 Business rules

| Rule ID | Rule | Why it exists |
| --- | --- | --- |
| BR-001 | States are PendingContract→AwaitingPayment→Confirmed→InProduction→Shipped→Delivered; only PendingContract/AwaitingPayment and eligible unbatched Confirmed orders can be cancelled. | Preserve contract, payment and production lifecycle. |
| BR-002 | Batch-linked orders cannot be cancelled until an Admin dissolves their Planned batch. | Keep batch membership atomic. |
| BR-003 | Paid cancellation triggers MFG-06 full-refund processing; no inventory restock occurs. | Made-to-order production and payment ownership. |
| BR-004 | Every access is checked server-side; customers require ownership and staff require same-company authorization. | Prevent cross-customer/company access. |

## 6. Key entities (mandatory)

| Entity | Attributes (from Input/Output fields) | Relationships |
| --- | --- | --- |
| Order | UUID, company_id, customer_id, design_id/version, quote_id, policy_version, status, merge_opt_in, contract_id, batch_id?, immutable address/quantity/price snapshots, tracking_number?, carrier?, shipped_at?, version, timestamps | Belongs to company/customer; linked to quote, contract and optional batch; emits payment/refund/status events. |
| Order timeline event | Order ID, prior/target status, actor, timestamp, request/idempotency reference | Belongs to one order; append-only. |
| Notification/outbox event | Order ID, event type, recipients, delivery state | Created transactionally after order mutation. |

## 7. Screens involved

| Screen ID | Screen name | Priority | Screen Spec file |
| --- | --- | --- | --- |
| S26 | Customer order history | Should | `screens/S26-customer_order_list_screen.md` |
| S27 | Customer order detail and refund status | Should | `screens/S27-customer_order_detail_screen.md` |
| S28 | Company Admin order dashboard | Should | Module screen; same-company list and filters |
| S29 | Production management | Should | Module screen; status progression |
| S30 | Contract tab | Should | MFG-09 contract boundary |
| S38 | Notifications | Should | Shared notification screen |

## 8. Success criteria (mandatory)

| SC ID | Criterion | How it is measured |
| --- | --- | --- |
| SC-001 | Every order read is limited to the actor's ownership/company scope and returns the stored snapshot. | Verify authorized and unauthorized customer/staff requests; inaccessible IDs return 404. |
| SC-002 | Only valid cancellation and fulfillment transitions commit, including under concurrent requests. | Exercise state-transition matrix and race tests; one winner, stale loser 409. |
| SC-003 | Notifications and refund requests are durable and deduplicated after order commit. | Inspect outbox/inbox and refund event for retries and duplicate commands. |

## 9. Assumptions

- Orders are made to order; cancellation does not restock inventory.
- MFG-06 is authoritative for settlement/refunds, and MFG-10 is authoritative for batch membership.
- MVP prioritizes this module as Should; manual tracking remains an acceptable operational fallback.

## 10. Open questions

| # | Question | Blocking? | Owner | Status |
| --- | --- | --- | --- | --- |
| 1 | Resolved decisions: Group B author; course DBIZ 3; no approver identified; demo/course use only; MVP priority Should. | No | Group B | Resolved |
| 2 | No remaining open questions. | No | Group B | Resolved |

## 11. Traceability to DBIZ2

| Spec section | DBIZ2 source | Location |
| --- | --- | --- |
| 1–2 Scope and actors | Function List MFG-07 | Rows 53–59; source identifiers retained in each FR |
| 3 Scenarios | UC-C08, UC-C07, UC-S04 | Use-case identifiers; resolved behavior in this specification |
| 4 Flow | Order lifecycle and MFG-06/MFG-10 events | Current module contracts described inline above |
| 5–6 FRs and entities | F-ORD-001..007 | Function List MFG-07; IDs are module-qualified because MFG-08 reuses local IDs |
| 7 Screens | S26–S30, S38 | Screen list and current MFG-07 contract |

## Completion checklist

- [x] All seven MFG-07 functions are represented by FR rows and contracts.
- [x] Resolved access, cancellation, refund, batch, status and notification rules are recorded.
- [x] MVP priority and answered administrative inputs are reflected.
- [x] No unresolved placeholders remain.
- [x] Traceability identifies source module and local ID namespace.

Template source: DBIZ3 Product Design Package specification template.

DBIZ3, FTU.
