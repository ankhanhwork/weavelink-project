# Screen Spec: S23 Merge Option

| Field | Value |
|---|---|
| Screen ID | `S23` |
| Screen name | Merge Option |
| Actor | Customer owner |
| Priority | P3 |
| Belongs to module | [MFG-10](../specs/spec-MFG-10.md) |
| Route | `/orders/merge?design_id={id}` |
| Mockup image | `img/S23-merge_option_screen.png` |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The customer explicitly opts into or out of merging and reviews the fixed 5 percent discount policy before quote calculation. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S23 historical reference](img/S23-merge_option_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Merge Option | Yes | Static route title. |
| 2 | Route | Navigation target | /orders/merge?design_id={id} | Yes | Access checked on server. |
| 3 | merge_opt_in | Field / control | explicit boolean | As specified | merge_opt_in: explicit boolean; default false; acceptance stores merge policy_version. |
| 4 | merge_eligible | Field / control | server-derived boolean | As specified | Enable opt-in only for an eligible design/product; otherwise show the reason and keep the standard route available. |
| 5 | merge_discount_vnd | Field / control | server floor(subtotal_vnd*5/100) | As specified | merge_discount_vnd: server floor(subtotal_vnd*5/100); max 3 extra calendar days; company honors promise without batch. |
| 6 | checkout_effect | Field / control | read-only explanation | As specified | Saving preference issues a replacement quote; it creates no batch and applies no merge fee. |
| 7 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 8 | Accept merge policy | Action | Persist explicit opt-in/version then request server quote. | Available when authorized | Destination: S25 |
| 9 | Decline | Action | Persist false and request standard quote. | Available when authorized | Destination: S25 |
| 10 | Read terms | Action | Show versioned conditions without silently accepting. | Available when authorized | Destination: S24 |

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
| 1 | Accept merge policy | Activate | Persist explicit opt-in/version then request server quote. | S25 |
| 2 | Decline | Activate | Persist false and request standard quote. | S25 |
| 3 | Read terms | Activate | Show versioned conditions without silently accepting. | S24 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Explicit opt-in stores policy version and server applies floor(subtotal*5/100), without creating a batch.
2. Decline sets no discount; displayed promise still honored if no batch forms.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-10/F-MER-001 | Implements this screen's validated user flow and the linked source function. |
| MFG-10/F-MER-002 | Implements this screen's validated user flow and the linked source function. |
| MFG-10/F-MER-003 | Implements this screen's validated user flow and the linked source function. |
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
