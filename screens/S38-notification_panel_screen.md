# Screen Spec: S38 Notification Panel

| Field | Value |
|---|---|
| Screen ID | `S38` |
| Screen name | Notification Panel |
| Actor | Authenticated user |
| Priority | P3 |
| Belongs to module | [MFG-01](../specs/spec-MFG-01.md) |
| Route | `/notifications` |
| Mockup image | img/S38-notification_panel_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The authenticated recipient sees their persisted in-app notifications. Opening a target rechecks authorization; email delivery remains secondary. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![Historical visual reference](img/S38-notification_panel_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Notification Panel | Yes | Static route title. |
| 2 | Route | Navigation target | /notifications | Yes | Access checked on server. |
| 3 | notification_id / recipient | Field / control | UUID plus session-derived owner | As specified | Sanitize event/target content; never accept a submitted recipient as authority. |
| 4 | read_at / pagination | Field / control | nullable UTC plus bounded paging | As specified | Event/recipient uniqueness suppresses duplicates. |
| 5 | target_route | Field / control | optional internal route | As specified | Reauthorize the target when opened; hide invalid or inaccessible deep links. |
| 6 | email_delivery_state | Field / control | secondary read-only status | As specified | The persisted in-app inbox remains authoritative. |
| 7 | order lifecycle event | Notification payload | safe design/sample/contract/deposit/production/shipment/receipt/balance label | Optional | Deep link to S27, S29, S34 or S35 only after fresh authorization; never include provider secrets. |
| 7 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 8 | Mark read | Action | Persist recipient read_at; repeated action is idempotent. | Available when authorized | Destination: S38 |
| 9 | Open notification | Action | Resolve allowlisted target and reauthorize target access. | Available when authorized | Destination: authorized target route |
| 10 | Close | Action | Return to prior validated route. | Available when authorized | Destination: Origin |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Load the S38 Notification Panel view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | Show “You are all caught up” when no unread or recent notification exists. | Screen has no eligible or matching record |
| Forbidden/not found | Return a safe 401/403/404 for S38 Notification Panel without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S38 Notification Panel, show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S38 Notification Panel; retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh the committed Notification Panel data and show the next action permitted by its lifecycle and actor. | Valid action commits |
| Conflict | The Notification Panel data or lifecycle changed concurrently; reload authoritative state and do not replay a stale mutation. | Stale version, duplicate or invalid lifecycle transition |
## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Mark read | Activate | Persist recipient read_at; repeated action is idempotent. | S38 |
| 2 | Open notification | Activate | Resolve allowlisted target and reauthorize target access. | authorized target route |
| 3 | Close | Activate | Return to prior validated route. | Origin |

Portal: Authenticated user. Route: /notifications. Back preserves the originating route and filters. Fallback: Customer→S26; Sales Admin→S28; Sales→S20; System Admin→S41; Guest→S01. Enforce role, ownership and assignment before rendering.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. User sees only own persisted notifications and repeated mark-read is idempotent.
2. Opening an unauthorized/stale target is blocked after a fresh server access check.
3. Each committed digital approval, sample dispatch/decision, contract readiness/signature, deposit, shipment/receipt and balance event creates at most one notification per recipient; email failure does not roll back state.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|


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
