# Cross-module acceptance contract

These are concrete acceptance requirements for the future application, not runtime tests already executed. Module specs supply the detailed per-function cases. [D01–D12](system-decisions.md) govern; [validation report](validation-report.md) distinguishes documentation checks from application testing.

## Worked price-policy v1 examples

All values are integer VND. Apply surcharge per unit, then merge discount=min(subtotal, 840000 VND) once on the total subtotal (30% of the 2,800,000 VND setup-cost planning assumption). Shipping below uses the demo default; real quotes snapshot configured shipping. The documentation validator independently checks these rows.

| Case | Quantity | Unit price | Surcharge | Merge | Shipping | Subtotal | Discount | Total |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| Standard | 10 | 200000 | 5000 | No | 30000 | 2050000 | 0 | 2080000 |
| Merge | 100 | 100000 | 0 | Yes | 30000 | 10000000 | 840000 | 9190000 |
| Rounding | 3 | 100001 | 2 | Yes | 30000 | 300009 | 300009 | 30000 |
| Small subtotal | 1 | 1 | 0 | Yes | 30000 | 1 | 1 | 30000 |

These examples use design_fee_vnd 0. A Complex first order adds its accepted fee outside subtotal: the Merge example with design fee 200000 has unchanged discount 840000 and total 9390000. Tax and merge fee are zero under v1 demo policy. Promo codes are not active. Quantity over product max_units_per_order or 10000 is rejected, even if the price calculation would succeed. Values beyond the payment adapter's bound are rejected before order/payment creation. S23/S25/S34/S35 must show identical stored totals for the submitted snapshot.

## End-to-end scenarios

| ID | Setup and action | Required result |
|---|---|---|
| E2E-01 | Guest registers, verifies email, logs in, customizes a Published product and saves | Customer capability only; owned Saved design with immutable version visible in S17 |
| E2E-02 | Customer submits request; Admin assesses Simple or Complex | Submitted opens S17 with one Admin notice and no payment; Simple becomes Approved at fee 0; Complex remains FeeProposed until exact fee/version acceptance |
| E2E-03 | Admin assigns Approved request and consultant delivers | Matching customer assignment, committed due date, immutable Delivered design with retained request provenance and one owner notification |
| E2E-04 | Customer reviews valid quote and submits concurrent retries | One AwaitingDigitalApproval order via unique consumed_quote_id, same snapshot, no production batch |
| E2E-05 | Customer approves digital design; Dony ships sample; Customer approves received sample; Admin publishes Ready PDF; Customer signs | Exact design/sample evidence is retained; contract is impossible before sample approval; signing alone advances PendingContract to AwaitingDeposit |
| E2E-05A | Customer pays DEPOSIT, receives final goods and pays BALANCE | Verified deposit alone advances to Confirmed; receipt precedes DeliveredAwaitingBalance; verified balance alone advances to Completed |
| E2E-06 | Admin revision races customer signature | Exactly one current-version mutation wins; no unsigned altered content attached to Signed evidence |
| E2E-07 | Forged browser return reports success | No payment/order transition; UI reads persisted state |
| E2E-08 | Repeated valid IPN, mismatched amount and out-of-order failure | One accepted settlement; wrong amount has no effect; later failure cannot downgrade Succeeded |
| E2E-09 | Customer cancels while a deposit callback arrives | Row locking selects a coherent order; cancellation retains Cancelled and creates the policy-based refund if funds arrive; no resurrection |
| E2E-10 | Two eligible opt-in orders are recommended; Admin start races cancellation | Admin-only start atomically commits all members or rejects; no recommendation reserves an order; no partial batch/cancelled member |
| E2E-11 | Seven-day merge window expires without an Admin-started batch | Scheduler starts Individual Production through MFG-07 automatically; discount and due date stay snapshotted |
| E2E-12 | Sales Admin reviews and starts a compatible group with negative estimated net savings | Negative amount remains visible; no acknowledgment gate; batch starts only after explicit authorized Admin action |
| E2E-13 | Assigned Sales ships an InProduction order; Customer confirms receipt | Carrier/tracking/time required; unauthorized Sales cannot act; Shipped does not expose BALANCE until receipt evidence advances to DeliveredAwaitingBalance |
| E2E-14 | Another-company staff guesses order, PDF, export or design UUID | No content disclosure or mutation; object guard returns 404 |
| E2E-15 | A new Dony employee accepts a System Admin-issued invitation | StaffAccount activates exactly once; token is consumed; staff password is never generated or emailed; no customer company or tenant is created |
| E2E-16 | Last active admin is demoted or company with open work is deleted | Operation rejected, access remains recoverable; no orphan work |
| E2E-17 | Duplicate/late payment is received and refunded | Reconciliation balance records both events; neither inflates accepted sales revenue; only eligible original-sale refunds reduce revenue |
| E2E-18 | Export requested with dashboard filters and malicious text cell | Same watermark/totals/company scope; CSV/XLSX treats formula-leading content as text |
| E2E-19 | Old backup selected, later transactions exist and callbacks arrive during recovery | Verified log replay reconstructs committed watermark, queued provider events replay once, no lost orders or duplicate refunds; missing log chain blocks activation |
| E2E-20 | Email service fails during payment/signing/config changes | Business commit and in-app inbox survive; retryable delivery failure is visible in operations |
| E2E-21 | Customer cancels in each preassignment state, including after fee acceptance, while Admin assigns/assesses | Eligible cancellation has no refund; one race winner; stale/state 409; Assigned/InProgress/Delivered/Rejected cannot cancel; repeated cancellation replays |
| E2E-22 | Customer accepts stale/wrong Complex fee; another-company actor assesses | No acceptance/approval or disclosure; exact current proposal and ownership required; proposals cannot be edited after publication |
| E2E-23 | Two first orders from delivered Complex design/copies race | One claims accepted fee; other conflicts; source provenance retained; stale allocation requires reviewed requote; fee outside subtotal and discount |
| E2E-24 | Additional order attempted before fee-bearing order InProduction, then after | Before: 409 DESIGN_FEE_ORDER_PENDING; after: new order design_fee_vnd 0; no duplicate charge |
| E2E-25 | Fee-bearing order cancelled with pending/failed refund, then fully resolved | Allocation remains blocked until attempts/refund resolved; release then charges next new order; no signed snapshot changes; late receipts refunded without reclaiming allocation |
| E2E-26 | Delivered request never ordered; customer opens a legacy S16 URL | Return non-mutating 410 Gone; no invoice/payment/revenue, redirect, or provider session |
| E2E-27 | Fee-bearing order settles then is fully refunded in another range | S43/export revenue includes fee once; visible design-fee component follows paid_at/refunded_at and same filters/exclusions, including negative refund-only range |
| E2E-28 | Default fee changes after proposal; Admin generates/regenerates contract | Existing proposal/accepted fee unchanged; S25/S34/PDF/S35 share exact separate fee line; Admin cannot append another fee |

## Human and deployment facts

Names, course metadata, actual approval and official organization contacts are tracked only in [the factual-input register](user-input-needed.md). Deployment secrets are supplied through runtime configuration. Missing facts must not prevent demo data with explicit fictional labels, but the system must never present that data as verified legal identity.
