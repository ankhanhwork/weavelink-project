# S34 — Contract Detail (Customer)

| Property | Value |
|---|---|
| Route | `/contracts/{contract_id}` |
| Module | MFG-09 |
| Roles and ownership | Customer owner; server enforces role, company, assignment and ownership per D01. |
| Priority | P1 |
| Mockup | Historical mockup: [img/S34-contract_detail_screen_customer.png](img/S34-contract_detail_screen_customer.png); written rules supersede sample text. |

## Purpose and data

The customer reviews the generated contract and signs only after explicit consent, typed full-name match, recent password reauthentication and a one-time contract-bound challenge. Signing records immutable evidence. All identifiers and permissions come from the server session; list filters are allowlisted and recoverable failures preserve entered values.

## Fields and validation

| Field | Type / required | Validation and source |
|---|---|---|
| contract_id | UUID, required | Customer must own associated order; inaccessible ID returns 404. D01/D07 |
| pdf_asset_id | private UUID | Authorized expiring download URL (10 minutes); no public asset URL. D02/D07 |
| consent | boolean, required true | Explicit acceptance of displayed consent text version; checkbox alone does not sign. D07 |
| consent_text_version | version, required | Persisted with evidence. D07 |
| typed_full_name | string, required | 1..100; trimmed/casefold match to authenticated profile full_name. D07 |
| password | secret, required at signing | Reauthenticate; valid within 5 minutes; never logged or stored in evidence. D07 |
| signing_challenge | one-time token, required | Server binds contract UUID/version/content hash; expires in 10 minutes; single use. D07 |
| Idempotency-Key | UUID, required | Same key/payload returns signed version; changed payload returns 409. D02/D07 |
| signature evidence | server-generated record | signer, name, consent version, hash, timestamp, server IP/user-agent, challenge digest. D07 |
## Actions and navigation

| Action | Result | Destination |
|---|---|---|
| Request signing challenge | Require explicit consent, typed name and recent password reauth; issue contract-bound 10m one-use challenge. | S34 |
| Sign | Verify challenge/hash/version and transactionally record evidence; order advances to AwaitingPayment. | S35 |
| Download/view PDF | Authorized private URL; no public asset URL. | S34 |
### Global navigation access

Home and public catalog are available to Guest and authenticated users. Customer designs, orders, profile and notifications require the customer’s authenticated session. Company Admin routes are S10, S18, S28, S30, S36, S42 and S43; Sales Consultants use S20 and assigned-only S28/S29/S21 access; System Admin routes are S39, S40 and S41. The server rechecks company, membership, ownership and assignment for every route and notification target.
Functions: MFG-09/F-CONTR-008, MFG-09/F-CONTR-009. Global navigation and back behavior follow D11. Auth return paths must be internal allowlisted routes.

## Workflow transitions

Successful sign → S35 payment; back to customer order → S27; PDF download stays S34.

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

1. Correct consent, typed profile name, recent password and valid contract-bound challenge records evidence once and moves order to AwaitingPayment.
2. Expired/replayed challenge, changed hash/version or missing consent rejects signing; checkbox alone never signs.

## Responsive and accessibility

Follow D11: 360px through desktop; stack columns and use labelled horizontal-scroll tables on narrow screens; keyboard-operable controls, visible focus, logical headings, associated form labels, aria-live status/error announcements, contrast >=4.5:1 (large text >=3:1), pointer targets >=24px. Preserve form data after recoverable failures; confirm destructive actions; disable duplicate submit while pending and enforce D02 idempotency server-side.

## Source documents

- [MFG-09 specification](../specs/spec-MFG-09.md)
- [Canonical decisions D01-D12](../docs/system-decisions.md)
- [Human factual input register](../docs/user-input-needed.md)
