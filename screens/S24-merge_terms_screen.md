# Screen Spec: S24 Merge Terms

| Field | Value |
|---|---|
| Screen ID | `S24` |
| Screen name | Merge Terms |
| Actor | Guest/Customer |
| Priority | P3 |
| Belongs to module | [MFG-10](../specs/spec-MFG-10.md) |
| Route | `/merge-terms` |
| Mockup image | img/S24-merge_terms_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** This read-only public/customer page explains merge eligibility, timing, price and production effects from the current merge policy. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![Historical visual reference](img/S24-merge_terms_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Merge Terms | Yes | Static route title. |
| 2 | Route | Navigation target | /merge-terms | Yes | Access checked on server. |
| 3 | policy_version | Field / control | immutable terms version shown and included in order quote on explicit opt-in. | As specified | policy_version: immutable terms version shown and included in order quote on explicit opt-in. |
| 4 | policy_terms | Field / control | versioned read-only content | As specified | Explain discount capped at min(subtotal, 840,000 VND = 30% of 2,800,000 VND setup-cost assumption); system may recommend compatible orders for up to seven days after deposit; Sales Admin makes the final decision and starts any batch; standard/merge production due 7/10 calendar days after deposit; no guarantee that other orders will merge. |
| 5 | acceptance_effect | Field / control | read-only explanation | As specified | Opening terms records no consent; acceptance occurs only on S23 with the displayed policy version. |
| 6 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 7 | Return to order choice | Action | Preserve validated origin; no preference is recorded by page view. | Available when authorized | Destination: S23 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Load the S24 Merge Terms view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | No Merge Terms records match the current route/filter; preserve inputs and show only the screen’s authorized next action. | Screen has no eligible or matching record |
| Forbidden/not found | Return a safe 401/403/404 for S24 Merge Terms without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S24 Merge Terms, show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S24 Merge Terms; retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh the committed Merge Terms data and show the next action permitted by its lifecycle and actor. | Valid action commits |
| Conflict | The Merge Terms data or lifecycle changed concurrently; reload authoritative state and do not replay a stale mutation. | Stale version, duplicate or invalid lifecycle transition |
## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Return to order choice | Activate | Preserve validated origin; no preference is recorded by page view. | S23 |

Portal: Guest/Customer. Route: /merge-terms. Back preserves the originating route and filters. Fallback: Customer→S26; Sales Admin→S28; Sales→S20; System Admin→S41; Guest→S01. Enforce role, ownership and assignment before rendering.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Opening terms alone does not set merge_opt_in; only return action preserves source route.
2. Displayed terms state discount cap/calculation, rolling-window policy, 7/10-day production target after deposit, and batch non-guarantee.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-10/F-MER-002 | **Select Merge** — Display versioned merge policy text and record accepted policy version. |


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
