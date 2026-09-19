# Spec Document: Contract Management

| Field | Value |
| --- | --- |
| Module ID | `MFG-09` |
| Module name | Contract Management |
| Spec version | v1.0 |
| Author (team member) | Group B |
| Date | 2026-09-19 |
| Status | Draft |
| Approved by (Client role) | No approver identified |
| DBIZ2 source | Function List MFG-09, No. 68–76, `F-CONTR-001`–`F-CONTR-009`; UC-C10, UC-C09, UC-C11, UC-C14, UC-C15, UC-C13; screens S30–S34 and S38 |

---

## 1. Purpose and scope (mandatory)

Company Admins manage versioned templates and generate or regenerate order contracts before signing. Customers review and sign only their own current contract. The system generates PDFs and records an auditable application acknowledgement; it does not claim a certified digital signature. Successful signing atomically advances the order from PendingContract to AwaitingPayment. MFG-06 owns order creation and payment; MFG-07 owns fulfillment/cancellation.

MVP priority: **Should**. The complete-system contract lifecycle, template management and signature evidence are specified here.

## 2. Actors (mandatory)

| Actor | Role in this module | Where it comes from |
| --- | --- | --- |
| Company Admin | Manages same-company templates/contracts and generates or updates unsigned contracts | MFG-09 contract |
| Customer | Reviews and signs own current Ready contract; receives signed copy | MFG-09 contract; UC-C09/UC-C11 |
| System | Renders PDF, validates evidence, transitions order after signing and sends notifications | MFG-09 function contract |
| MFG-06 / MFG-07 | Supplies immutable order snapshots and cancellation events | Module boundaries |

## 3. User scenarios and acceptance criteria (mandatory)

### US-1: Manage templates and generate contract (Should)

Admin selects a compatible active template for a same-company PendingContract order, previews allowlisted placeholders, and generates a server-rendered PDF from immutable customer/order/address/policy snapshots.

1. **Given** no compatible template exists, **when** generation is requested, **then** an actionable empty state appears and generation is blocked.
2. **Given** a template is published or edited, **when** a new version is created, **then** prior contract PDFs and hashes remain unchanged.
3. **Given** required snapshot data is unavailable or the order/template version is stale, **when** generation runs, **then** it fails without creating a Ready contract.

### US-2: Review and sign contract (Should)

Customer signs only the current Ready version for their own PendingContract order. Signing requires explicit consent, matching typed name, current-password reauthentication, and a single-use challenge tied to contract ID/version/hash.

1. **Given** all signature evidence is valid, **when** signing commits, **then** evidence is stored and the order advances to AwaitingPayment.
2. **Given** consent is missing, name mismatches, reauthentication fails, challenge expires/is reused, or version is stale, **when** signing is attempted, **then** no signature or order transition commits.
3. **Given** a contract is signed, **when** it is later cancelled through an eligible order cancellation, **then** it is audibly Voided and its signed artifact/evidence is retained.

### US-3: Update and notify contract (Should)

Before signing, Admin may regenerate from the immutable order snapshot. The prior unsigned version becomes Superseded, and the customer must review/sign the new Ready version.

1. **Given** a Ready contract is regenerated, **when** the new PDF is successfully stored, **then** only then is the prior unsigned version superseded and the customer notified.
2. **Given** a notification email fails, **when** delivery is retried, **then** contract state remains committed and the in-app notice remains available.

### Edge cases

- Same idempotency key and payload replays; changed payload with the same key returns 409.
- Private PDF access requires an authorized expiring link.
- Signed contracts cannot be edited; cancellation voiding is retained in the audit history.

## 4. Flows (mandatory)

### 4.1 Usage flow

MFG-06 creates PendingContract order with immutable snapshots → Admin selects/publishes a compatible template → system renders PDF/hash and marks current contract Ready → customer reviews and submits consent, typed name, reauthentication and challenge → contract is locked and evidence saved → signed event advances order to AwaitingPayment → both parties receive authorized signed-copy links.

### 4.2 Sequence for the main flow

```mermaid
sequenceDiagram
  actor C as Customer
  participant O as Order service
  participant K as Contract service
  C->>O: Submit valid quote
  O-->>K: PendingContract + immutable snapshots
  K->>K: Render PDF and content hash
  K-->>C: Ready notice and review link
  C->>K: Consent + typed name + password reauth + challenge
  K->>K: Lock current version, verify, persist evidence
  K->>O: Signed event
  O->>O: PendingContract → AwaitingPayment
  K-->>C: Signed copy notice
```

## 5. Functional requirements (mandatory)

| FR ID | DBIZ2 Subfunction ID | Requirement (system MUST ...) | Actor | Priority |
| --- | --- | --- | --- | --- |
| FR-001 | F-CONTR-001 | List compatible active templates for same-company PendingContract orders. | Company Admin | Should |
| FR-002 | F-CONTR-002 | Preview safe rendered placeholders from an authorized template version. | Company Admin | Should |
| FR-003 | F-CONTR-003 | Fill immutable draft contract from authoritative stored order/customer/address/item/amount/policy snapshots. | Company Admin | Should |
| FR-004 | F-CONTR-004 | Render and persist PDF/hash as Ready transactionally with idempotency and private asset access. | System | Should |
| FR-005 | F-CONTR-005 | Notify customer of Ready contract after commit using authorized review link. | System | Should |
| FR-006 | F-CONTR-006 | List contracts and create/update/publish/archive versioned templates with allowlisted placeholders. | Company Admin | Should |
| FR-007 | F-CONTR-007 | Regenerate unsigned PendingContract documents from snapshots, supersede prior version after storage, and notify; cancellation may void while retaining evidence. | Company Admin / System | Should |
| FR-008 | F-CONTR-008 | Record customer application acknowledgement with consent, matching name, recent reauthentication and one-time challenge bound to contract version/hash. | Customer | Should |
| FR-009 | F-CONTR-009 | Notify customer and same-company management after successful signing; only then advance order PendingContract→AwaitingPayment. | System | Should |

### 5.1 Input / Output contract

| FR ID | Input field | Type | Required | Output field | Type | Notes / validation |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | order_id, order_type | UUID / enum | Yes | compatible template IDs, versions, names | Array | Same-company Admin; PendingContract only |
| FR-002 | template_id, version | UUID / integer | Yes | preview model and placeholder map | Object | Allowlist and escape text; no template code execution |
| FR-003 | order_id, template_id/version, expected order version | UUIDs / integers | Yes | immutable draft and content_hash | Object/hash | Missing snapshot value 422; stale data 409 |
| FR-004 | draft, template version, Idempotency-Key | Object/version/key | Yes | contract_id/version, PDF asset ID, expiring URL | Object | Retry same payload replays |
| FR-005 | Ready contract event | Internal event | Yes | outbox notification ID | UUID | After commit; deduplicated |
| FR-006 | filters; template name/content/expected_version | Values / structured body / integer | Optional by action | contract list or versioned template | Paginated object | Same-company Admin; create/update/publish/archive; archive blocks new use and preserves past contracts; stale/duplicate 409; invalid fields 422 |
| FR-007 | order/contract/template versions, expected order version, Idempotency-Key | UUIDs/versions/key | Yes | superseded/new Ready references and notice ID | Object | Signed version immutable |
| FR-008 | contract ID/version/hash, consent, typed name, current password, one-time challenge, key | Values | Yes | Signed metadata and evidence receipt | Object | Typed name matches account full name after trim/case normalization; reauth ≤5 min; challenge bound to ID/version/hash, expires in 10 min and is single-use |
| FR-009 | committed signing event | Internal event | Yes | delivery IDs and signed-copy links | UUIDs/authorized URLs | Notify both parties after commit |

### 5.2 Business rules

| Rule ID | Rule | Why it exists |
| --- | --- | --- |
| BR-001 | Contract states are Draft→Ready→Signed; Draft/Ready can become Superseded; Draft/Ready/Signed may become Voided on eligible cancellation. | Keep contract and order lifecycle aligned. |
| BR-002 | Published template versions and signed contracts are immutable. | Preserve the reviewed and signed artifact. |
| BR-003 | Placeholder values come only from authoritative order/customer/address snapshots and allowlisted fields. | Prevent untrusted template execution or drift. |
| BR-004 | Successful signature evidence is application acknowledgement, not a certified digital signature. | State the signature capability accurately. |
| BR-005 | Only a current Ready contract for an owned PendingContract order can be signed; successful signature alone advances the order to AwaitingPayment. | Prevent signing stale contracts or premature payment. |

Contract amounts must match the quote/payment screens using the same VND snapshot. PDF render/storage must succeed before a contract becomes Ready. If cancellation is eligible, the contract becomes Voided with artifact and signature evidence retained.

## 6. Key entities (mandatory)

| Entity | Attributes (from Input/Output fields) | Relationships |
| --- | --- | --- |
| ContractTemplate | UUID, company_id, name, version, structured body, active, timestamps, version | Company-owned; published versions are immutable. |
| Contract | UUID, order_id, company_id, version, template_version, content_hash, PDF asset UUID, status, ready/signed/voided timestamps, evidence, version | Belongs to order/company; versioned; unsigned prior version may be superseded. |
| SignatureEvidence | signer_id from session, typed_name, consent_text_version, contract_hash, server_timestamp, observed IP/user_agent, challenge digest | Bound to one contract version/hash; never trusts client-reported identity/IP. |

## 7. Screens involved

| Screen ID | Screen name | Priority | Screen Spec file |
| --- | --- | --- | --- |
| S30 | Contract list and templates tabs | Should | Module screen |
| S31 | Create contract template | Should | Module screen |
| S32 | Edit contract template | Should | Module screen |
| S33 | Company Admin contract detail | Should | Module screen |
| S34 | Customer contract review/signature | Should | Module screen |
| S38 | Notifications | Should | Shared notification screen |

## 8. Success criteria (mandatory)

| SC ID | Criterion | How it is measured |
| --- | --- | --- |
| SC-001 | Rendered contract total and terms match immutable order snapshots. | Compare PDF hash/content and VND totals with quote/payment screens. |
| SC-002 | Only the customer can sign the current Ready version with all required evidence. | Verify ownership, consent, name, reauthentication, challenge and stale-version cases. |
| SC-003 | Signed documents remain immutable and notifications survive email outage. | Verify artifact retention, audit evidence, inbox and retry behavior. |

## 9. Assumptions

- Company Admin and customer authorization are resolved server-side.
- PDF assets are private; URLs expire after authorization.
- MVP priority is Should; no certified digital-signature claim is made.

## 10. Open questions

| # | Question | Blocking? | Owner | Status |
| --- | --- | --- | --- | --- |
| 1 | Resolved decisions: Group B; course DBIZ 3; no approver identified; course/demo use only; MVP priority Should. | No | Group B | Resolved |
| 2 | No remaining open questions. | No | Group B | Resolved |

## 11. Traceability to DBIZ2

| Spec section | DBIZ2 source | Location |
| --- | --- | --- |
| 1–2 Scope and actors | MFG-09 Function List No. 68–76 | `F-CONTR-001`–`F-CONTR-009` |
| 3 Scenarios | UC-C10, UC-C09, UC-C11, UC-C14, UC-C15, UC-C13 | Use-case labels; resolved workflows in this specification |
| 4 Signing flow | PendingContract to AwaitingPayment | MFG-06/MFG-09 module contract |
| 5–6 FRs and entities | `F-CONTR-001`–`F-CONTR-009` | Function List MFG-09 |
| 7 Screens | S30–S34, S38 | Screen List and module contract |

## Completion checklist

- [x] All nine MFG-09 functions have FR rows and contracts.
- [x] Template versioning, PDF integrity, signature evidence, order transition and notifications are specified.
- [x] Customer/company authorization and immutability rules are recorded.
- [x] Resolved inputs are recorded and no unresolved placeholders remain.
- [x] Traceability identifies function IDs, use cases and screens.

Template source: DBIZ3 Product Design Package specification template.

DBIZ3, FTU.
