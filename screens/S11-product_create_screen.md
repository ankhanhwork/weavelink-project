# Screen Spec: S11 Product Create

| Field | Value |
|---|---|
| Screen ID | `S11` |
| Screen name | Product Create |
| Actor | Company Admin |
| Priority | P2 |
| Belongs to module | [MFG-04](../specs/spec-MFG-04.md) |
| Route | `/admin/products/new` |
| Mockup image | Don't have mockup |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** Product creation validates all fields required for publication; a draft can be saved before publication requirements are complete. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

Don't have mockup

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Product Create | Yes | Static route title. |
| 2 | Route | Navigation target | /admin/products/new | Yes | Access checked on server. |
| 3 | name | Field / control | string, required | As specified | 1..120 trimmed characters. |
| 4 | sku | Field / control | string, required | As specified | Unique within company. |
| 5 | category | Field / control | string, required | As specified | Allowlisted configured category. |
| 6 | unit_price_vnd | Field / control | integer, required | As specified | Nonnegative; never floating point. |
| 7 | supported_sizes/colors/materials | Field / control | arrays, required to publish | As specified | At least one of each; values from configured options. |
| 8 | max_units_per_order | Field / control | integer, required | As specified | 1..10000; quote exceeding capacity returns 422 CAPACITY_EXCEEDED. resolved product rule |
| 9 | image_asset_ids | Field / control | UUID array | As specified | At least one safe image to publish; PNG/JPEG/WebP <=10MiB each, max5. |
| 10 | Save draft | Action | Validate SKU/options/price and create Draft product. | Available when authorized | Destination: S12 |
| 11 | Save and publish | Action | Require all publish fields and safe images then transition to Published. | Available when authorized | Destination: S10 |
| 12 | Cancel | Action | Discard create form. | Available when authorized | Destination: S10 |

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
| 1 | Save draft | Activate | Validate SKU/options/price and create Draft product. | S12 |
| 2 | Save and publish | Activate | Require all publish fields and safe images then transition to Published. | S10 |
| 3 | Cancel | Activate | Discard create form. | S10 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Valid product creates Draft with company-unique SKU and integer price.
2. Duplicate SKU or invalid image returns field errors; no partial product is saved.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-04/F-PROD-005 | Implements this screen's validated user flow and the linked source function. |
| MFG-04/F-PROD-006 | Implements this screen's validated user flow and the linked source function. |
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
