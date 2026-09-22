# Screen Spec: S39 System Configuration and Backup/Restore

| Field | Value |
|---|---|
| Screen ID | `S39` |
| Screen name | System Configuration and Backup/Restore |
| Actor | System Admin |
| Priority | P2 |
| Belongs to module | [MFG-12](../specs/spec-MFG-12.md) |
| Route | `/system/configuration` |
| Mockup image | Don't have mockup |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The System Admin edits typed allowlisted global configuration and runs backup/restore operations. Secret fields show status only; price-policy v1 constants remain read-only. Restore requires reauthentication, exact backup ID, verified log chain, pre-restore backup and maintenance mode. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

Don't have mockup

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | System Configuration and Backup/Restore | Yes | Static route title. |
| 2 | Route | Navigation target | /system/configuration | Yes | Access checked on server. |
| 3 | settings_version / expected_version | Field / control | integer, required on save | As specified | Complete allowlisted configuration validates and activates atomically. |
| 4 | public_company_contacts | Field / control | typed nullable values | As specified | Omit unset phone/social links; never invent business identifiers. |
| 5 | SMTP/VNPay secret references | Field / control | write-only secret-reference strings | As specified | Show configured/not configured only; never reveal secret values. |
| 6 | design_service_fee_vnd | Field / control | integer | As specified | Suggested Complex assessment fee: range 1..9999999999 VND; default 200000. Changes affect future assessments only; Simple uses 0 and existing proposals/accepted fees remain unchanged. |
| 7 | shipping_vnd | Field / control | integer | As specified | Configurable nonnegative VND; default 30000. |
| 8 | merge_discount_percent | Field / control | integer, read-only in v1 | As specified | Fixed at 5 despite broader allowlist in later configuration; fixed release rule. |
| 9 | standard_production_days / merge_extra_days | Field / control | integer, read-only in v1 | As specified | Fixed at 7 / 3 days; customer promise is production_due_at, not carrier delivery. |
| 10 | daily_backup_time | Field / control | HH:mm, editable | As specified | Asia/Ho_Chi_Minh; default 02:00. |
| 11 | daily_retention_count / weekly_retention_count | Field / control | integers, editable | As specified | Daily 1..30 default 7; weekly 1..12 default 4; retain required transaction logs/assets for all retained bases. |
| 12 | backup_id | Field / control | UUID, required for restore | As specified | Require reauth and exact confirmation; checksum/schema validation and pre-restore backup. |
| 13 | maintenance_mode / restore_lock | Field / control | server state | As specified | One restore at a time; payment callbacks queue durably and replay idempotently. |
| 14 | Save settings | Action | Validate allowlist and complete config version atomically; secrets are reference-only; audit and notify after commit. | Available when authorized | Destination: S39 |
| 15 | Run backup | Action | Queue backup; show state until checksums/schema manifest verified. | Available when authorized | Destination: S39 |
| 16 | Restore backup | Action | Reauthenticate, confirm exact ID, prebackup and enter maintenance; replay callbacks idempotently after validation. | Available when authorized | Destination: S39 |
| 17 | View logs | Action | Open redacted audit viewer. | Available when authorized | Destination: S40 |

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
| 1 | Save settings | Activate | Validate allowlist and complete config version atomically; secrets are reference-only; audit and notify after commit. | S39 |
| 2 | Run backup | Activate | Queue backup; show state until checksums/schema manifest verified. | S39 |
| 3 | Restore backup | Activate | Reauthenticate, confirm exact ID, prebackup and enter maintenance; replay callbacks idempotently after validation. | S39 |
| 4 | View logs | Activate | Open redacted audit viewer. | S40 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Company Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales Consultant routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks role, company, membership, ownership and assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Company Admin, S20 for Sales Consultant, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Allowlisted settings version activates atomically only after validation and emits audit/notification.
2. Restore requires reauth/confirmation/prebackup; failure keeps maintenance enabled and does not report success.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-12/F-SYS-003 | Implements this screen's validated user flow and the linked source function. |
| MFG-12/F-SYS-004 | Implements this screen's validated user flow and the linked source function. |
| MFG-12/F-SYS-005 | Implements this screen's validated user flow and the linked source function. |
| MFG-12/F-SYS-006 | Implements this screen's validated user flow and the linked source function. |
| MFG-12/F-SYS-007 | Implements this screen's validated user flow and the linked source function. |
| MFG-12/F-SYS-008 | Implements this screen's validated user flow and the linked source function. |
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
