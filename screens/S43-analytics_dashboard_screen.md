# Screen Spec: S43 Analytics Dashboard

| Field | Value |
|---|---|
| Screen ID | `S43` |
| Screen name | Analytics Dashboard |
| Actor | Company Admin |
| Priority | P3 |
| Belongs to module | [MFG-11](../specs/spec-MFG-11.md) |
| Route | `/admin/analytics` |
| Mockup image | Don't have mockup |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The Company Admin views company-scoped read-only metrics for the selected local date range and product filter. Exports use the same metric rules and snapshot watermark. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

Don't have mockup

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Analytics Dashboard | Yes | Static route title. |
| 2 | Route | Navigation target | /admin/analytics | Yes | Access checked on server. |
| 3 | date_start / date_end | Field / control | local dates, inclusive/exclusive | As specified | Default last 30 local calendar days; maximum 366 days; reject start >= end. |
| 4 | product_id | Field / control | optional UUID | As specified | Same-company product only; filter related orders. |
| 5 | revenue_vnd | Field / control | integer VND aggregates | As specified | Accepted ORDER settlement by paid_at less refunds by refunded_at; design-fee component included; exclude duplicate/late receipts and their refunds. |
| 6 | order_count / cancellation_count | Field / control | integer counts | As specified | Count orders by created_at in all states; cancellations shown separately. |
| 7 | new_customers | Field / control | integer count | As specified | Distinct customers whose first submitted order in this company falls in range. |
| 8 | refreshed_at / timezone | Field / control | UTC timestamp / Asia/Ho_Chi_Minh | As specified | Always display snapshot watermark and local range; zero-data metrics are zero. |
| 9 | export_format / export_limit | Field / control | CSV or XLSX / max 100000 rows | As specified | Same filters/formulas/watermark; prevent spreadsheet formula injection. |
| 10 | Apply date/product filters | Action | Recompute authoritative company-scoped metrics; display timezone/range/refreshed_at. | Available when authorized | Destination: S43 |
| 11 | Export CSV/XLSX | Action | Same filters/formulas and snapshot watermark; <=100000 rows; neutralize formula injection. | Available when authorized | Destination: S43 |
| 12 | Open order | Action | Navigate only to authorized company order detail. | Available when authorized | Destination: S29 |
| 13 | design_fee_revenue_vnd | Read-only revenue component | Design fees included in order revenue | Yes | Sum order design_fee_vnd on accepted settlements by paid_at less the same component on full refunds by refunded_at; same filters/watermark/exclusions; no double-counting; zero/negative range values allowed. |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no metrics during the selected date range; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one for the documented mutation. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Apply date/product filters | Activate | Recompute authoritative company-scoped metrics; display timezone/range/refreshed_at. | S43 |
| 2 | Export CSV/XLSX | Activate | Same filters/formulas and snapshot watermark; <=100000 rows; neutralize formula injection. | S43 |
| 3 | Open order | Activate | Navigate only to authorized company order detail. | S29 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Revenue equals successful ORDER payments minus successful ORDER refunds by their respective timestamps; design-fee component is included and displayed separately without adding it again.
2. Zero-data period shows zeros; export matches filter/formula/watermark and rejects >100000 rows.
3. S43 and exports show the same design-fee revenue component; Simple/repeat orders contribute 0, and no order/payment produces no fee revenue. Full refunds subtract the original fee component.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-11/F-DA-001 | Implements this screen's validated user flow and the linked source function. |
| MFG-11/F-DA-002 | Implements this screen's validated user flow and the linked source function. |
| MFG-11/F-DA-003 | Implements this screen's validated user flow and the linked source function. |
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
