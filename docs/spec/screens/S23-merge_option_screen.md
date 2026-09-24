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

**Shown when:** The customer explicitly opts into or out of merging and reviews the versioned 840,000 VND per-order discount (30% of Dony's 2,800,000 VND setup-cost assumption), capped at subtotal. State merge production completes 10 days after deposit, compared with 7 days for a separate run. Show the number of compatible confirmed orders waiting without exposing identities. Compatible orders may be recommended to Sales Admin during the rolling seven-day window after deposit; only Sales Admin can approve and start a batch.

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
| 5 | merge_discount_vnd | Field / control | 840000 VND, capped at subtotal | As specified | Server applies min(subtotal_vnd, 840000); per-order discount is fixed by policy version. |
| 6 | checkout_effect | Field / control | read-only explanation | As specified | Saving preference issues a replacement quote; it creates no batch and applies no merge fee. |
| 7 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 8 | Accept merge policy | Action | Persist explicit opt-in/version then request server quote. | Available when authorized | Destination: S25 |
| 9 | Decline | Action | Persist false and request standard quote. | Available when authorized | Destination: S25 |
| 10 | Read terms | Action | Show versioned conditions without silently accepting. | Available when authorized | Destination: S24 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Load the S23 Merge Option view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | No Merge Option records match the current route/filter; preserve inputs and show only the screen’s authorized next action. | Screen has no eligible or matching record |
| Forbidden/not found | Return a safe 401/403/404 for S23 Merge Option without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S23 Merge Option, show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S23 Merge Option; retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh the committed Merge Option data and show the next action permitted by its lifecycle and actor. | Valid action commits |
| Conflict | The Merge Option data or lifecycle changed concurrently; reload authoritative state and do not replay a stale mutation. | Stale version, duplicate or invalid lifecycle transition |
## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Accept merge policy | Activate | Persist explicit opt-in/version then request server quote. | S25 |
| 2 | Decline | Activate | Persist false and request standard quote. | S25 |
| 3 | Read terms | Activate | Show versioned conditions without silently accepting. | S24 |

Portal: Customer owner. Route: /orders/merge?design_id={id}. Back preserves the originating route and filters. Fallback: Customer→S26; Sales Admin→S28; Sales→S20; System Admin→S41; Guest→S01. Enforce role, ownership and assignment before rendering.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Explicit opt-in stores policy version and server applies min(subtotal, 840000 VND), without creating a batch.
2. Decline sets no discount; displayed promise still honored if no batch forms.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-10/F-MER-001 | **Select Merge** — Show standard versus merge price/deadline and eligibility summary for saved eligible designs; do not create a batch. |
| MFG-10/F-MER-002 | **Select Merge** — Display versioned merge policy text and record accepted policy version. |
| MFG-10/F-MER-003 | **Select Merge** — Save preference on owned quote, compute versioned discount capped at 840,000 VND (30% of 2,800,000 VND setup-cost assumption) and issue a new immutable 30-minute quote. |


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
