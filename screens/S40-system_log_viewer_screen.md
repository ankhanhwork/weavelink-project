# S40 — System Log Viewer

| Property | Value |
|---|---|
| Route | `/system/logs` |
| Module | MFG-12 |
| Roles and ownership | System Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The System Admin searches append-only, redacted audit events by severity, date range and allowlisted event fields. Severity is INFO, WARN or ERROR; entries cannot be edited or deleted. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / required | Validation and source |
|---|---|---|
| level | enum, optional | INFO, WARN, ERROR only; derived server-side, no DEBUG selector. D10 refinement |
| date_from/date_to | ISO-8601 timestamps, optional | Range validated; UTC stored, Asia/Ho_Chi_Minh displayed; max range policy enforced. D02/D10 |
| search_query | trimmed string, optional | Search allowlisted actor/target/action/request_id fields only. D10 |
| company_id/target_id/action/outcome | allowlisted filters | System Admin only; redact sensitive target details and secrets. D01/D10 |
| audit row | read-only event | Actor, company, target, action, outcome, request_id, timestamp. Append-only. D10 |
| retention | 365 days | Expired audit events are not returned. D10 |
## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Search logs | Query append-only redacted events by allowlisted filters. | S40 |
| Open target | Navigate only when current System Admin is authorized for target; otherwise show redacted event detail here. | authorized detail or S40 |
| Configuration | Open settings and operations. | S39 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-12/F-SYS-001, MFG-12/F-SYS-002. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Log target opens authorized related detail where permitted; config → S39; home → S01.

## States

| State | Behavior | Trigger |
|---|---|---|
| Loading | Labelled progress/skeleton; disable duplicate submit. | Request starts |
| Empty | Show no audit events matching the allowlisted query; preserve filters where present and explain eligibility/filter conditions. | Successful query returns no rows |
| Forbidden/not found | Safe message without revealing inaccessible identifiers. | 401/403/404 |
| Error | Show code, message, field_errors, request_id; preserve entered values. | Request failure |
| Retry | Retry reads on transient failure; reuse the same idempotency key only for mutations that require one under D02. | Recoverable failure |
| Success | Show committed state and next valid action; announce via aria-live. | Mutation commits |
| Conflict | Explain stale state; reload; never silently overwrite. | 409 |

## Acceptance scenarios

1. Audit row contains actor/company/target/action/outcome/request id/time without password/token/card data.
2. Search respects date/level filters and 365-day retention; log entries cannot be edited or deleted.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-12 specification](../specs/spec-MFG-12.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
