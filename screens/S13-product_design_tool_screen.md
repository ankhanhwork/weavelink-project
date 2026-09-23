# Screen Spec: S13 Product Design Tool

| Field | Value |
|---|---|
| Screen ID | `S13` |
| Screen name | Product Design Tool |
| Actor | Customer owner |
| Priority | P1 |
| Belongs to module | [MFG-05](../specs/spec-MFG-05.md) |
| Route | `/designs/new?product_id={id}` |
| Mockup image | img/S13-product_design_tool_screen.png |
| Status | Resolved implementation specification |

## 1. Purpose

**Shown when:** The customer edits a private 2D design tied to an owned product version. Saving creates a version; ordered snapshots are never overwritten. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

**The user leaves this screen when:** An authorized action in section 5 succeeds, the user follows a role-allowed global route, or they return to the validated originating route.

## 2. Mockup

![S13 historical reference](img/S13-product_design_tool_screen.png)

Written behavior below takes precedence over obsolete sample content.

## 3. Element inventory

| # | Element | Type | Content / data source | Required | Validation |
|---|---|---|---|---|---|
| 1 | Screen heading | Heading | Product Design Tool | Yes | Static route title. |
| 2 | Route | Navigation target | /designs/new?product_id={id} | Yes | Access checked on server. |
| 3 | product_id/product_version | Field / control | required immutable selection | As specified | product_id/product_version: required immutable selection; unsupported or changed version requires reload. |
| 4 | size/color/material/print_method | Field / control | required values from current product rules. | As specified | size/color/material/print_method: required values from current product rules. |
| 5 | uploaded image | Field / control | PNG/JPEG/WebP, actual MIME checked, <=10MiB each, max5 | As specified | uploaded image: PNG/JPEG/WebP, actual MIME checked, <=10MiB each, max5; scan unsafe content. |
| 6 | print-area coordinates | Field / control | bounded to configured printable area | As specified | print-area coordinates: bounded to configured printable area; saved config versioned; drafts not orderable. |
| 7 | API errors | Field / control | standard API error envelope | As specified | 400 malformed; 422 invalid fields; 409 stale/duplicate; 429 rate limit; 503 dependency failure |
| 8 | Preview | Action | Render 2D configuration using current product rule and safe assets. | Available when authorized | Destination: S13 |
| 9 | Save design | Action | Persist immutable version owned by customer. | Available when authorized | Destination: S17 |
| 10 | Continue to order | Action | Allowed only saved design. | Available when authorized | Destination: S22 |
| 11 | Request consultant | Action | Start design service request. | Available when authorized | Destination: S15 |

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
| 1 | Preview | Activate | Render 2D configuration using current product rule and safe assets. | S13 |
| 2 | Save design | Activate | Persist immutable version owned by customer. | S17 |
| 3 | Continue to order | Activate | Allowed only saved design. | S22 |
| 4 | Request consultant | Activate | Start design service request. | S15 |

Home and public catalog are available to Guest and authenticated users. Customer designs and customer orders are Customer-only; profile and notifications require authentication. Sales Admin routes: S10, S18, S28, S30, S36, S42 and S43. Sales routes: S20 and assigned-only S21. System Admin routes: S39, S40 and S41. The server rechecks internal role, customer ownership and staff assignment for every route and notification target. Back returns to the validated originating route and preserves list filters; without one, use S26 for Customer, S28 for Sales Admin, S20 for Sales, S41 for System Admin, and S01 for Guest.

## 6. Screen-level rules

| Rule ID | Rule | Source |
|---|---|---|
| SR-001 | Access and ownership are checked server-side; do not trust submitted customer, company, role, price, or provider status. Apply 401/403/404 behavior and the field rules above. | Authorization and data ownership requirements |
| SR-002 | IDs are UUIDs; timestamps are UTC and displayed in Asia/Ho_Chi_Minh; money and quantities are integers. Mutations use expected_version; significant create/sign/pay/batch operations use idempotency keys. | Data representation and concurrency requirements |
| SR-003 | Apply the module lifecycle and validation rules linked below; preserve immutable submitted snapshots. | Module specification |
| SR-004 | Selected product and technical defaults are project implementation decisions; do not invent factual company, author, client-approval, or course identifiers. | Project implementation assumptions |

### Acceptance scenarios

1. Saved design stores product and rule versions plus customer ownership; image is private scanned asset.
2. Draft cannot be ordered; invalid coordinate or changed rule blocks save and preserves editable configuration.

## 7. Linked requirements

| FR ID (from the module spec) | What this screen does for it |
|---|---|
| MFG-05/F-DES-001 | Implements this screen's validated user flow and the linked source function. |
| MFG-05/F-DES-002 | Implements this screen's validated user flow and the linked source function. |
| MFG-05/F-DES-003 | Implements this screen's validated user flow and the linked source function. |
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
