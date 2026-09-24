# Screen Spec: S14 Product Design Rules

| Field | Value |
|---|---|
| Screen ID | `S14` |
| Screen name | Product Design Rules |
| Actor | Sales Admin |
| Priority | P2 |
| Belongs to module | [MFG-04](../specs/spec-MFG-04.md) |
| Route | `/admin/products/{product_id}/design-rules` |
| Mockup image | img/S14-product_design_rules_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The Sales Admin edits the selected product’s supported sizes, colors, materials, print methods, bounded 2D print area and option surcharges. Saving versions the rules and invalidates unconsumed quotes for review. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![Historical visual reference](img/S14-product_design_rules_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Product Design Rules | Yes | Static route title. |
| 2 | Route | Navigation target | /admin/products/{product_id}/design-rules | Yes | Access checked on server. |
| 3 | product_id | Field / control | UUID path | As specified | product_id: UUID path; expected_version required. |
| 4 | supported_sizes/colors/materials/print_method | Field / control | nonempty allowlisted product-rule options. | As specified | supported_sizes/colors/materials/print_method: nonempty allowlisted product-rule options. |
| 5 | print_area | Field / control | bounded 2D coordinates | As specified | print_area: bounded 2D coordinates; reject nonpositive/out-of-bounds geometry. |
| 6 | option_surcharge_vnd | Field / control | integer >=0 for each supported option | As specified | option_surcharge_vnd: integer >=0 for each supported option; saved rules version new quote policy. |
| 7 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 8 | Save rules | Action | Validate supported options/area/surcharges, increment product version; old quotes require review. | Available when authorized | Destination: S10 |
| 9 | Cancel | Action | Discard changes. | Available when authorized | Destination: S10 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Load the S14 Product Design Rules view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | No Product Design Rules records match the current route/filter; preserve inputs and show only the screen’s authorized next action. | Screen has no eligible or matching record |
| Forbidden/not found | Return a safe 401/403/404 for S14 Product Design Rules without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S14 Product Design Rules, show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S14 Product Design Rules; retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh the committed Product Design Rules data and show the next action permitted by its lifecycle and actor. | Valid action commits |
| Conflict | The Product Design Rules data or lifecycle changed concurrently; reload authoritative state and do not replay a stale mutation. | Stale version, duplicate or invalid lifecycle transition |
## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Save rules | Activate | Validate supported options/area/surcharges, increment product version; old quotes require review. | S10 |
| 2 | Cancel | Activate | Discard changes. | S10 |

Portal: Sales Admin. Route: /admin/products/{product_id}/design-rules. Back preserves the originating route and filters. Fallback: Customer→S26; Sales Admin→S28; Sales→S20; System Admin→S41; Guest→S01. Enforce role, ownership and assignment before rendering.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Valid rule change increments product version and requires review of an earlier quote.
2. Out-of-bounds print area, unsupported option or negative/noninteger surcharge is rejected.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-04/F-PROD-007 | **Update Product** — Render an authorized product edit model with current version. |
| MFG-04/F-PROD-008 | **Update Product** — Update allowlisted product fields atomically with expected-version checks. |
| MFG-04/F-PROD-011 | **Publish Product** — Change product visibility to an explicitly requested valid state. |


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
