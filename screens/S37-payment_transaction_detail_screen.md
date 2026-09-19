# S37 — Payment Transaction Detail

| Property | Value |
|---|---|
| Route | `/admin/payments/{payment_id}` |
| Module | MFG-06 |
| Roles and ownership | Company Admin; server enforces role, company, assignment and ownership per D01. |
| Priority | P2 |
| Mockup | No mockup supplied. |

## Purpose and data

The Company Admin inspects a same-company payment’s immutable provider and reconciliation details and may retry only an eligible full-amount refund. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / requirement | Validation / source |
|---|---|---|
| payment_id / company_id | UUID / server-derived UUID | Payment belongs to current company; inaccessible ID returns 404. |
| purpose / resource_id | ORDER or SERVICE / UUID | Read-only link to originating order or design request. |
| amount_vnd / currency | integer / VND | Immutable provider amount; show full value to authorized same-company admin. |
| provider_reference / transaction_id | redacted text / UUID | Mask secrets and sensitive provider references. |
| refund_status / refund_amount_vnd | None, Pending, Succeeded, Failed / integer VND | Full original amount only; no partial input; successful refund is immutable. |
| expected_version / Idempotency-Key | integer / UUID | Refund initiation is idempotent; retry same key/payload only after eligible provider failure. |

## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Initiate/retry refund | Full amount only; require eligible status; idempotently request provider; status remains Pending until verified. | S37 |
| Open related order/request | Navigate only if company and resource authorization passes. | S29 or S16 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-06/F-PAY-005, MFG-07/F-ORD-003. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Refund initiate/retry remains S37; related order → S27 or company order → S29; payment list → S36.

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

1. Eligible full refund moves to Pending and succeeds only on verified provider result.
2. Partial amount cannot be submitted; duplicate same-key request returns same refund operation.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-06 specification](../specs/spec-MFG-06.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
