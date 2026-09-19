# Cross-module acceptance contract

These are concrete acceptance requirements for the future application, not runtime tests already executed. Module specs supply the detailed per-function cases. [D01–D12](system-decisions.md) govern; [validation report](validation-report.md) distinguishes documentation checks from application testing.

## Worked price-policy v1 examples

All values are integer VND. Apply surcharge per unit, then floor the 5% merge discount once on the total subtotal. Shipping below uses the demo default; real quotes snapshot configured shipping. The documentation validator independently checks these rows.

| Case | Quantity | Unit price | Surcharge | Merge | Shipping | Subtotal | Discount | Total |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| Standard | 10 | 200000 | 5000 | No | 30000 | 2050000 | 0 | 2080000 |
| Merge | 100 | 100000 | 0 | Yes | 30000 | 10000000 | 500000 | 9530000 |
| Rounding | 3 | 100001 | 2 | Yes | 30000 | 300009 | 15000 | 315009 |
| Small subtotal | 1 | 1 | 0 | Yes | 30000 | 1 | 0 | 30001 |

Tax and merge fee are zero under v1 demo policy. Promo codes are not active. Quantity over product max_units_per_order or 10000 is rejected, even if the price calculation would succeed. Values beyond the payment adapter's bound are rejected before order/payment creation. S23/S25/S34/S35 must show identical stored totals for the submitted snapshot.

## End-to-end scenarios

| ID | Setup and action | Required result |
|---|---|---|
| E2E-01 | Guest registers, verifies email, logs in, customizes a Published product and saves | Customer capability only; owned Saved design with immutable version visible in S17 |
| E2E-02 | Customer creates a service request, fails first payment, retries and settles | One request created before payment; no assignment/paid notice until one verified settlement; one Paid transition |
| E2E-03 | Admin assigns paid request and consultant delivers | Matching customer assignment, committed due date, immutable Delivered design and one owner notification |
| E2E-04 | Customer reviews valid quote, submits it twice with different keys | One PendingContract order via unique consumed_quote_id, same snapshot, no production batch |
| E2E-05 | Admin publishes Ready PDF, customer reauthenticates and signs | Evidence binds current version/hash; order AwaitingPayment only after atomic signature commit |
| E2E-06 | Admin revision races customer signature | Exactly one current-version mutation wins; no unsigned altered content attached to Signed evidence |
| E2E-07 | Forged browser return reports success | No payment/order transition; UI reads persisted state |
| E2E-08 | Repeated valid IPN, mismatched amount and out-of-order failure | One accepted settlement; wrong amount has no effect; later failure cannot downgrade Succeeded |
| E2E-09 | Customer cancels while a payment success arrives | Row locking selects a coherent order; cancellation retains Cancelled and creates full refund if funds arrive; no resurrection |
| E2E-10 | Two eligible opt-in orders form a batch while one is cancelled concurrently | Atomic batch membership or complete rejection; no partial batch and no cancelled order produced |
| E2E-11 | Merge window expires without a batch | Individual production retains 5% discount and snapshotted production deadline |
| E2E-12 | Admin dissolves Planned batch, then cancels an eligible paid member | Historical membership retained; active batch link removed; full refund workflow visible independently |
| E2E-13 | Assigned consultant ships an InProduction order | Carrier/tracking/time required; unauthorized consultant cannot act; only Shipped then Delivered allowed |
| E2E-14 | Another-company staff guesses order, PDF, export or design UUID | No content disclosure or mutation; object guard returns 404 |
| E2E-15 | Company first admin invitation is accepted by new staff | Provisioning company activates exactly once; token consumed; staff password is never generated/emailed |
| E2E-16 | Last active admin is demoted or company with open work is deleted | Operation rejected, access remains recoverable; no orphan work |
| E2E-17 | Duplicate/late payment is received and refunded | Reconciliation balance records both events; neither inflates accepted sales revenue; only eligible original-sale refunds reduce revenue |
| E2E-18 | Export requested with dashboard filters and malicious text cell | Same watermark/totals/company scope; CSV/XLSX treats formula-leading content as text |
| E2E-19 | Old backup selected, later transactions exist and callbacks arrive during recovery | Verified log replay reconstructs committed watermark, queued provider events replay once, no lost orders or duplicate refunds; missing log chain blocks activation |
| E2E-20 | Email service fails during payment/signing/config changes | Business commit and in-app inbox survive; retryable delivery failure is visible in operations |

## Human and deployment facts

Names, course metadata, actual approval and official organization contacts are tracked only in [the factual-input register](user-input-needed.md). Deployment secrets are supplied through runtime configuration. Missing facts must not prevent demo data with explicit fictional labels, but the system must never present that data as verified legal identity.
