# Screen Spec: S18 Product Edit

| Field | Value |
|---|---|
| Screen ID | `S18` |
| Screen name | Product Edit |
| Actor | Sales Admin |
| Priority | Should (MVP) |
| Belongs to module | [MFG-04](../specs/spec-MFG-04.md) |
| Route | `/admin/products/{product_id}/edit` |
| Mockup image | img/S18-01-product-edit.png |
| Status | Resolved implementation specification |


## 1. Purpose

**Shown when:** A Sales Admin edits a Dony-owned configurable garment base using version checks. Publishing requires all required production and design-rule fields; submitted order snapshots remain unchanged. The record is not finished-goods inventory. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![Screen mockup](img/S18-01-product-edit.png)

The mockup illustrates the defined workflow. Fictional sample values do not replace the field, lifecycle and release-scope rules below.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Product Edit | Yes | Static route title. |
| 2 | Route | Navigation target | /admin/products/{product_id}/edit | Yes | Access checked on server. |
| 3 | product_id | Field / control | UUID, required | As specified | Current Dony-owned product base. |
| 4 | name/sku/category | Field / control | string, required | As specified | Same constraints as S17; SKU unique across Dony's single product catalogue. |
| 5 | unit_price_vnd | Field / control | integer, required | As specified | Nonnegative integer VND. |
| 6 | supported options/capacity | Field / control | arrays/integer | As specified | Current product rules; max_units_per_order 1..10000. |
| 7 | expected_version | Field / control | version, required | As specified | Stale edit returns 409. |
| 8 | quote consequence | Field / control | server state | As specified | Rule changes invalidate old quote for review; submitted snapshots unchanged. |
| 9 | Save changes | Action | Check expected_version; persist changes; invalidate/requote affected unsubmitted quote. | Available when authorized | Destination: S16 |
| 10 | Edit design rules | Action | Open rules editor. | Available when authorized | Destination: S19 |
| 11 | Cancel | Action | Discard edits. | Available when authorized | Destination: S16 |

## 4. States

**Loading, access, errors and retry:** Show a labelled Loading state while reads resolve. A missing or inaccessible route returns a safe 401/403/404 without disclosing protected records. Error states show the API code, message, field_errors and request_id while preserving safe input. Retry transient reads; retry a mutation only with the original idempotency key and identical payload. Preserve safe user input after recoverable failures.

| State | What the user sees | Trigger |
|---|---|---|
| Empty | Not applicable to this single-record route; a missing or inaccessible record uses Forbidden/not found. | The route identifies one record. |
| Success | Refresh the committed Product Edit data and show the next action permitted by its lifecycle and actor. | Valid action commits |
| Conflict | The Product Edit data or lifecycle changed concurrently; reload authoritative state and do not replay a stale mutation. | Stale version, duplicate or invalid lifecycle transition |
## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Save changes | Activate | Check expected_version; persist changes; invalidate/requote affected unsubmitted quote. | S16 |
| 2 | Edit design rules | Activate | Open rules editor. | S19 |
| 3 | Cancel | Activate | Discard edits. | S16 |

Portal: Sales Admin. Route: /admin/products/{product_id}/edit. Back preserves the originating route and filters. 

### Production-rule navigation

After MFG-10 activation, the existing Edit design rules action opens [S19](S19-product-design-rules.md) to maintain merge-enabled products, the per-product small-order threshold, production-type/material identities and shared garments-per-working-day capacity profile. Keep these controls in the rules editor rather than creating duplicate product settings on S46. Preserve product identity, version and return context.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Check access and ownership on the server; never trust submitted customer, company, role, price, stage or provider status. Apply the documented 401/403/404 behavior and field rules. | Project baseline |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected versions and idempotency keys where specified. | Project baseline |
| SR-003 | Apply the owning module's lifecycle and validation rules; preserve immutable submitted snapshots and design versions. | Project baseline |
| SR-004 | Use documented project assumptions; do not invent factual company, author, client-approval or course identifiers. | Project baseline |

### Acceptance scenarios

1. A current-version update saves and increments product version; stale version returns 409.
2. Changed rules invalidate affected unsubmitted quote for explicit review; signed/submitted snapshots remain unchanged.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-04/F-PROD-007 | **Update Product** — Render an authorized product edit model with current version. |
| MFG-04/F-PROD-008 | **Update Product** — Update allowlisted product fields atomically with expected-version checks. |


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
