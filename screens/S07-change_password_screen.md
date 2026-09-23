# Screen Spec: S07 Change Password

| Field | Value |
|---|---|
| Screen ID | `S07` |
| Screen name | Change Password |
| Actor | Member |
| Priority | P3 |
| Belongs to module | [MFG-02](../specs/spec-MFG-02.md) |
| Route | `/profile/change-password` |
| Mockup image | img/S07-change_password_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** This form changes only the authenticated user password. It requires the current password, retains the current session and revokes other sessions. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![Historical visual reference](img/S07-change_password_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Change Password | Yes | Static route title. |
| 2 | Route | Navigation target | /profile/change-password | Yes | Access checked on server. |
| 3 | current_password | Field / control | required secret | As specified | current_password: required secret; verify against stored hash. |
| 4 | new_password | Field / control | required 12..128 characters | As specified | new_password: required 12..128 characters; spaces allowed. |
| 5 | confirm_password | Field / control | required exact match | As specified | confirm_password: required exact match; reject current/new equality. |
| 6 | session_effect | Field / control | server rule | As specified | On success retain the current session and revoke all other sessions. |
| 7 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 8 | Change password | Action | Verify current password, hash new password, revoke other sessions, show confirmation. | Available when authorized | Destination: S06 |
| 9 | Cancel | Action | Discard unsaved password fields. | Available when authorized | Destination: S06 |

## 4. States

| State | What the user sees | Trigger |
|---|---|---|
| Loading | Load the S07 Change Password view model and show labelled progress; keep writes disabled until route data and authorization are resolved. | Request starts |
| Empty | No Change Password records match the current route/filter; preserve inputs and show only the screen’s authorized next action. | Screen has no eligible or matching record |
| Forbidden/not found | Return a safe 401/403/404 for S07 Change Password without revealing inaccessible record, customer, staff or payment details. | 401/403/404 |
| Error | For S07 Change Password, show the API code, message, field_errors and request_id; preserve safe user-entered values. | Request failure |
| Retry | Retry transient reads for S07 Change Password; retry a mutation only with its original idempotency key and identical payload, never as a new side effect. | Recoverable failure |
| Success | Refresh the committed Change Password data and show the next action permitted by its lifecycle and actor. | Valid action commits |
| Conflict | The Change Password data or lifecycle changed concurrently; reload authoritative state and do not replay a stale mutation. | Stale version, duplicate or invalid lifecycle transition |
## 5. Interactions and navigation

| # | Element | User action | System response | Goes to screen |
|---|---|---|---|---|
| 1 | Change password | Activate | Verify current password, hash new password, revoke other sessions, show confirmation. | S06 |
| 2 | Cancel | Activate | Discard unsaved password fields. | S06 |

Portal: Member. Route: /profile/change-password. Back preserves the originating route and filters. Fallback: Customer→S26; Sales Admin→S28; Sales→S20; System Admin→S41; Guest→S01. Enforce role, ownership and assignment before rendering.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Correct current password and matching 12..128-char new password update hash and revoke other sessions.
2. Incorrect current password or confirmation mismatch leaves stored password unchanged.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-02/F-PROF-004 | **Change Password** — Render the secure password-change form. |
| MFG-02/F-PROF-005 | **Change Password** — Verify the current password, replace the hash and revoke other sessions. |


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
