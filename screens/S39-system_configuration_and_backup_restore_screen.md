# S39 — System Configuration and Backup/Restore

| Property | Value |
|---|---|
| Route | `/system/configuration` |
| Module | MFG-12 |
| Roles and ownership | System Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The System Admin edits typed allowlisted global configuration and runs backup/restore operations. Secret fields show status only; price-policy v1 constants remain read-only. Restore requires reauthentication, exact backup ID, verified log chain, pre-restore backup and maintenance mode. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / required | Validation and source |
|---|---|---|
| settings_version / expected_version | integer, required on save | Complete allowlisted configuration validates and activates atomically. D10 |
| public_company_contacts | typed nullable values | Omit unset phone/social links; never invent business identifiers. D10/D11 |
| SMTP/VNPay secret references | write-only secret-reference strings | Show configured/not configured only; never reveal secret values. D03/D10 |
| design_service_fee_vnd | integer | Range 1..9999999999 VND; default 200000. D05/D10/D11 |
| shipping_vnd | integer | Configurable nonnegative VND; default 30000. D06/D10 |
| merge_discount_percent | integer, read-only in v1 | Fixed at 5 despite broader allowlist in later configuration; D09 v1 decision. |
| standard_production_days / merge_extra_days | integer, read-only in v1 | Fixed at 7 / 3 days; customer promise is production_due_at, not carrier delivery. D09 |
| daily_backup_time | HH:mm, editable | Asia/Ho_Chi_Minh; default 02:00. D10/D11 |
| daily_retention_count / weekly_retention_count | integers, editable | Daily 1..30 default 7; weekly 1..12 default 4; retain required transaction logs/assets for all retained bases. D10/D11 |
| backup_id | UUID, required for restore | Require reauth and exact confirmation; checksum/schema validation and pre-restore backup. D10 |
| maintenance_mode / restore_lock | server state | One restore at a time; payment callbacks queue durably and replay idempotently. D10 |
## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Save settings | Validate allowlist and complete config version atomically; secrets are reference-only; audit and notify after commit. | S39 |
| Run backup | Queue backup; show state until checksums/schema manifest verified. | S39 |
| Restore backup | Reauthenticate, confirm exact ID, prebackup and enter maintenance; replay callbacks idempotently after validation. | S39 |
| View logs | Open redacted audit viewer. | S40 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-12/F-SYS-003, MFG-12/F-SYS-004, MFG-12/F-SYS-005, MFG-12/F-SYS-006, MFG-12/F-SYS-007, MFG-12/F-SYS-008. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Save validated config stays S39; backup/restore actions stay S39; logs → S40.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Render the screen-specific form/detail state; if a required route object is absent, show safe not-found and return to the authorized parent route. | Empty initial form or missing detail payload |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Allowlisted settings version activates atomically only after validation and emits audit/notification.
2. Restore requires reauth/confirmation/prebackup; failure keeps maintenance enabled and does not report success.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-12 specification](../specs/spec-MFG-12.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
