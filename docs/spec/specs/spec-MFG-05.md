# Spec Document: Product Design

| Field | Value |
| --- | --- |
| Module ID | `MFG-05` |
| Module name | Product Design |
| Spec version | v1.4 |
| Author (team member) | Group B |
| Date | 2026-09-27 |
| Status | Draft |
| Approved by (Client role) | No approver assigned |
| DBIZ2 source | Historical IDs retained: Function List No. 36-46; `F-DES-001` .. `F-DES-011`; `UC-C02` .. `UC-C04`, `UC-S03`; S09, S13, S15-S22, S38; DBIZ3 collaboration extension S52. External DBIZ2 comparison is not required. |

---

## 1. Purpose and scope (mandatory)

Customers configure, preview and save versioned made-to-order garment designs and may request Dony design assistance with assessment-based pricing. For a Business Buyer, the design commonly represents uniforms or garments for internal use. For a Reseller Shop, it represents the shop's own artwork, branding or specifications that Dony will manufacture for the shop to sell to its customers. Dony does not supply ready-made resale inventory. Self-design/upload/preview/save is MVP Must; assessed design service is MVP Could.

**In scope:** background removal with reversible review; deterministic multi-angle 2D mockups; session-only OpenAI virtual try-on; validate product options/assets; save immutable design versions; list owned designs; create/cancel requests; assess complexity and accept deferred fees; assign via MFG-08; share consultant versions, record customer feedback/approval and staff replies, import unchanged customer sources, and notify authorized participants.

**Out of scope:** payment callback processing is MFG-06; product-rule authoring is MFG-04; order creation is MFG-06.

## 2. Actors (mandatory)

| Actor | Role in this module | Where it comes from |
| --- | --- | --- |
| Customer | Creates own designs/requests and views own results | MFG-05 resolved contract; UC-C02/UC-C03/UC-C04 |
| Sales | Works assigned approved requests | MFG-05 role boundary |
| Sales Admin | Assesses complexity, proposes fees/rejects, assigns, sets committed due date, may deliver | MFG-05 role boundary |
| System | Sends durable request and delivery notifications | MFG-05 function contract |

## 3. User scenarios and acceptance criteria (mandatory)

### US-1 (Must): Design product

Customer configures product-supported colour, material and print method, then edits artwork on the existing 2D front/back garment canvas. Size is deliberately not part of a design; the Customer selects one or more sizes and quantities later on S22. Each supported side has its own printable area; the customer may upload up to five safe PNG/JPEG/WebP assets (10 MiB each), place and resize each asset using X/Y/width/height in millimetres relative to that area's top-left, and preview/save the configuration. Every placement must fit wholly inside its selected printable area. At S22, all selected order sizes must support the design and printable-area geometry; if size-specific product rules make any placed asset invalid, reject the quote with 422 and require an adjusted/new design before order submission. Saving creates an immutable Saved version; edits create a new version and never overwrite an ordered snapshot. Incompatible or stale rules return actionable 422/409 and persist nothing. Only Saved/Delivered versions are orderable. The existing workflow does not imply text layers, 3D editing or artwork rotation controls.

### US-2 (Must): Product customization

Every non-size option and print asset is validated against the current Published product version, ownership, actual MIME, scan result and print-area bounds. Front/back selection, upload list, zoom, drag/resize and numeric placement fields edit the same draft configuration; zoom changes only the view and not physical placement values. Size selection and quantity remain order-level data on S22, enabling one design to cover multiple sizes when current product rules permit it.

### US-3 (Must): View saved design

S17 is the owned-design gallery; S52 contains owned request details, shared versions and feedback. ProofDelivered designs are visible for review but are not orderable. Private staff Drafts are never returned to Customer APIs. Empty pagination is successful; editing an ordered design forks a version.

### US-4 (Could): Request design service

Valid submission creates Submitted, persists an administrator notification and navigates from S15 to S52 at `/design-requests/{request_id}`. No fee is displayed or snapshotted at submission and no payment transaction is created. Sales Admin starts UnderReview in S19, then approves Simple with fee 0, proposes a positive Complex fee, or rejects with a customer-visible reason. Customer explicitly accepts the current Complex fee/version in S52 before Approved becomes eligible for automatic assignment to the current classified lead owner. committed_due_at may be set afterward by Sales Admin only.

The owner may cancel Submitted, UnderReview, FeeProposed or unassigned Approved, including after fee acceptance, without refund. Assigned/InProgress/Delivered reject cancellation; Rejected cannot become Cancelled; repeated cancellation returns the Cancelled result. Cancellation and assignment lock the same request: one wins and a stale/state conflict returns 409. Assessment, acceptance and cancellation require expected_version and Idempotency-Key.

The request stands alone until its delivered design is ordered. The accepted fee is collected only as a separate line in the first order created from that design lineage under MFG-06 BR-008 and rendered by MFG-09; no order means no invoice, charge or collection.

### US-5 (Could): Send design to customer

Assigned consultant/Admin creates immutable Draft versions in S21 and explicitly shares a selected version for Customer review in S52. The design becomes ProofDelivered; a linked Assigned request becomes InProgress and stays InProgress through feedback/revision rounds. Only the owner's approval of the exact current shared version makes the design/request Delivered. Sharing records source_design_request_id; derived copies/versions retain it. Concurrent shares/decisions use version checks and idempotency, with no partial write. Staff may reply to the version-bound feedback in S21; CRM notes remain private.

For Reseller Shops, design_source is CustomerProvided only: ordinary production-oriented adjustments do not require a DesignRequest; larger rebuilding/rework of supplied artwork uses the existing Simple/Complex assessment. Creative design from scratch is available only for Business Buyers. Missing customer_model is triaged in S19 before assessment/assignment; it is not inferred from an attachment.

### US-6 (Must): Remove artwork background

On S13, Customer selects one artwork and opens S49. For a solid background, remove only border-connected pixels within the chosen tolerance, preserving disconnected matching colours inside the artwork. For complex subject backgrounds, provide subject segmentation. Show original and transparent result on a checkerboard before applying. Apply preserves asset ID, selected side and physical X/Y/width/height; it changes only the artwork pixels and increments the draft revision. Cancel leaves the draft unchanged. Restore original is available within the current draft session. Transparent PNG output retains detail and alpha; an already transparent upload is accepted. No operation automatically saves a design.

### US-7 (Must): Preview every supported angle

S50 shares the current S13 draft and shows six prepared 2D views where the selected product has templates: front flat lay, front shaped, left angle, right angle, back flat lay, back shaped. Thumbnail selection displays a large matching preview. Render the same physical print coordinates across views; the centre follows the collar/placket-to-torso curve, chest logos follow the selected wearer side, and back views contain only back artwork. Use calibrated per-template surfaces, perspective, clipping, occlusion and fabric shading to attach ink to the garment. Never call image-generation AI on angle changes. Unsupported template/colour/material combinations must be clearly unavailable rather than illustrated with another product. Mockups show appearance, not measured colour, fit or manufacturing proof.

### US-8 (Could): Try the designed polo on a person

S51 offers labelled synthetic male, female and child presets immediately, and a customer-uploaded PNG/JPEG/WebP photo. Presets are deterministic mockups; uploading does not generate or send images to OpenAI automatically. Customer reviews a disclosure, explicitly consents to sending their photo and designed polo image to OpenAI, then activates Try on me. Backend validates current design and calls OpenAI image edits; a real AI result replaces the top while aiming to preserve identity, pose, background and logo. Offer original/result comparison and replacement/removal of the photo. The result is illustrative and may alter lettering/details; it is never a design asset, saved version, size recommendation, order attachment or manufacturing source.

Personal uploads, try-on inputs/results and removal review buffers are session-only in application storage: no localStorage, sessionStorage, database, object store or image file persistence. Clear on session end, logout, navigation that destroys the workspace or reload. Provider processing/retention is separate and disclosed before consent; do not promise remote deletion at browser close. Consent is unchecked initially and revoked when the photo is replaced or removed. A changed design/photo/session invalidates pending results. Failed or cancelled generation preserves the design and must not trigger automatic paid retries.

### Edge cases

- Another customer or unassigned consultant receives 404/403 without data leakage.
- Requests do not expire automatically; obsolete request AwaitingPayment/Paid/Expired states are removed. Payment-attempt expiry remains in MFG-06.
- Submitted/UnderReview fee is null; stale fee acceptance or assessment after cancellation returns 409 without side effects.
- Email outage leaves in-app notification/state intact.
- Unsafe/oversized attachments are rejected before persistence.

## 4. Flows (mandatory)

### 4.1 Usage flow

```mermaid
flowchart LR
  Product[S09 Product] --> Workspace[S13 Design]
  Workspace --> Remove[S49 Remove background]
  Remove --> Workspace
  Workspace --> Preview[S50 Multi-angle mockups]
  Workspace --> TryOn[S51 Optional OpenAI try-on]
  TryOn --> Workspace
  Preview --> Save[Save version]
  Save --> Gallery[S17 Designs]
  Product --> Request[S15 Request service]
  Request --> Status[S52 Submitted request]
  Status --> Review[S19 UnderReview]
  Review -->|Simple fee 0| Approved[Approved]
  Review -->|Complex| Proposal[S52 FeeProposed]
  Proposal -->|Accept fee| Approved
  Review -->|Reject with reason| Rejected[Rejected]
  Status -->|Cancel| Cancelled[Cancelled]
  Review -->|Cancel| Cancelled
  Proposal -->|Cancel| Cancelled
  Approved -->|Cancel before assignment| Cancelled
  Approved --> Assign[S19 Assignment]
  Assign --> Deliver[S21 Share immutable version]
  Deliver --> Feedback[S52 Customer review]
  Feedback -->|Revision and staff reply| Deliver
  Feedback -->|Owner approval| Gallery
```

### 4.2 Sequence for the main flow

# UC-C02: Design product — SD-05A: Self Design Product

```mermaid
sequenceDiagram
    actor Customer
    participant DesignUI
    participant DesignController
    participant DesignService
    participant CustomerDesignDatabase

    Customer->>DesignUI: customize product design
    DesignUI->>DesignController: submit design
    DesignController->>DesignService: process design
    alt [save success]
        DesignService->>CustomerDesignDatabase: save design
        CustomerDesignDatabase-->>DesignService: saved
        DesignService-->>DesignController: save success
    else [save failed]
        DesignService-->>DesignController: save failed
    end
    DesignController-->>DesignUI: display save result
    DesignUI-->>Customer: display save confirmation
```

# UC-C04: Request design service — SD-05B: Request Design Service

```mermaid
sequenceDiagram
    actor Customer
    actor CompanyAdmin as Sales Admin
    participant RequestUI as S15 / S52
    participant AdminUI as S19
    participant DesignModule
    participant Database
    participant Outbox

    Customer->>RequestUI: Submit validated request on S15
    RequestUI->>DesignModule: Create request with idempotency key
    DesignModule->>Database: Atomically save Submitted and admin outbox event
    DesignModule-->>RequestUI: Request ID, navigate to S52 request view
    Outbox-->>CompanyAdmin: Notify submitted request
    CompanyAdmin->>AdminUI: Start review with expected version
    AdminUI->>DesignModule: Transition Submitted to UnderReview
    CompanyAdmin->>AdminUI: Record complexity, rationale and fee or rejection reason
    AdminUI->>DesignModule: Assess with expected version and key
    alt Simple
        DesignModule->>Database: Approve with fee 0 and customer outbox event
    else Complex
        DesignModule->>Database: Save FeeProposed, amount/version and customer outbox event
        Outbox-->>Customer: Review proposal in S52, no payment now
        Customer->>RequestUI: Accept exact fee and proposal version
        RequestUI->>DesignModule: Accept with expected version and key
        DesignModule->>Database: Atomically record acceptance and Approved, admin outbox event
    else Rejected
        DesignModule->>Database: Save Rejected with reason and customer outbox event
    end
    opt Customer cancels before assignment
        Customer->>RequestUI: Confirm cancellation in eligible state
        RequestUI->>DesignModule: Cancel with expected version and key
        DesignModule->>Database: Lock, cancel only unassigned eligible request, no refund
    end
    CompanyAdmin->>AdminUI: Classify/assign lead in S19; set commitment separately
    AdminUI->>DesignModule: Assign eligible request through MFG-08 with expected versions
    DesignModule->>Database: Atomically assign Approved request to current owner; commitment may be null; cancellation race 409
```

# UC-C03: View saved design — SD-06: View Saved Design

```mermaid
sequenceDiagram
    actor Customer
    participant SavedDesignUI
    participant SavedDesignController
    participant SavedDesignService
    participant SavedDesignDatabase

    Customer->>SavedDesignUI: view saved design
    SavedDesignUI->>SavedDesignController: request design
    SavedDesignController->>SavedDesignService: get design
    SavedDesignService->>SavedDesignDatabase: retrieve design
    SavedDesignDatabase-->>SavedDesignService: design data
    SavedDesignService-->>SavedDesignController: return design
    SavedDesignController-->>SavedDesignUI: send design
    SavedDesignUI-->>Customer: display design
```


## 5. Functional requirements (mandatory)

### 5.1 Functional requirement I/O contract

| FR ID | DBIZ2 Subfunction ID | Requirement (system MUST ...) | Actor | Priority |
| --- | --- | --- | --- | --- |
| FR-001 | F-DES-001 | Render the design workspace using current Published product rules and options. | Customer | Must |
| FR-002 | F-DES-002 | Validate compatibility/assets and produce a nonpersistent 2D preview. | Customer | Must |
| FR-003 | F-DES-003 | Save an immutable design version transactionally with idempotency; preserve source_design_request_id on derived copies/versions. | Customer | Must |
| FR-004 | F-DES-004 | List the owner’s gallery in S17 and request/shared-version detail in S52; expose no private Drafts or CRM data. | Customer | Must (gallery); Could (review/requests) |
| FR-005 | F-DES-005 | Render the design-service request form without a submission fee or payment step. | Customer | Could |
| FR-006 | F-DES-006 | Create a validated Submitted request with idempotency and return S52 request navigation; no submission fee/payment. | Customer | Could |
| FR-007 | F-DES-007 | Start UnderReview and assess complexity: approve Simple with fee 0, propose a Complex fee or reject with a reason, using version checks and idempotency. | Sales Admin | Could |
| FR-008 | F-DES-008 | Notify Dony Sales Admins after submission/acceptance/cancellation and the owner after assessment outcomes/cancellation, using committed outbox events. | System | Could |
| FR-009 | F-DES-009 | List Dony assessment/approved requests for Admin and assigned work for consultants; enforce state-specific authorization. | Sales / Sales Admin | Could |
| FR-010 | F-DES-010 | Create and explicitly share immutable service/technical versions in S21; keep a linked request InProgress through review, preserve provenance, and require owner approval before Delivered. | Sales / Sales Admin | Could |
| FR-011 | F-DES-011 | Notify authorized participants after committed sharing, feedback, reply, confirmation and approval events; link Customer to S52 and staff to S21. | System | Could |
| FR-012 | F-DES-012 | Accept the exact current proposed fee/version for an owned FeeProposed request and atomically record acceptance and Approved. | Customer | Could |
| FR-013 | F-DES-013 | Cancel an owned unassigned Submitted/UnderReview/FeeProposed/Approved request without refund; reject after assignment and replay repeated cancellation. | Customer | Could |
| FR-014 | F-DES-014 | Remove a selected artwork background with before/after review, apply, cancel and session restore; preserve physical placement. | Customer | Must |
| FR-015 | F-DES-015 | Render calibrated deterministic 2D multi-angle mockups from the current validated draft and product template version. | Customer | Must |
| FR-016 | F-DES-016 | Provide synthetic presets and consent-gated OpenAI try-on for an uploaded photo; discard stale results and keep personal images session-only. | Customer | Could |
| FR-017 | F-DES-017 | Append structured owner revision feedback to the current SharedForReview version, keep any request InProgress and notify staff; no fixed cap/surcharge. | Customer | Could |
| FR-018 | F-DES-018 | Record owner approval of the exact current shared version; atomically set design and any active request Delivered. | Customer | Could |
| FR-019 | F-DES-019 | Import unchanged customer-provided artwork into an owned immutable version with source/uploader/channel evidence. | Assigned Sales / Sales Admin | Could |
| FR-020 | F-DES-020 | Record customer-source confirmation for an unchanged import in S21 or S52, separate from approval of Dony changes. | Assigned Sales / Sales Admin / Customer owner | Could |
| FR-021 | F-DES-021 | Append an authorized customer-visible staff reply to a shared version's feedback without changing approval, fee or request state. | Assigned Sales / Sales Admin | Could |

### 5.2 Input / Output contract

| FR ID | Input field | Type | Required | Output field | Type | Notes / validation |
| --- | --- | --- | --- | --- | --- | --- |
| FR-001 | product UUID, session | UUID / session | Yes | S13 workspace model | View model | Published Dony configurable product base |
| FR-002 | product/design/options/assets | IDs / configuration | Yes | compatibility and preview UUID | Object | Current rules, ownership, MIME and bounds; 422 incompatible |
| FR-003 | configuration, versions, idempotency key | Object / integers / key | Yes | saved design ID/version and source_design_request_id | Object | Immutable provenance; stale/key conflict 409 |
| FR-004 | page, filters, sort, tab, request_id, session | Integers / values / UUID / session | Optional | own designs or request status/detail | Paginated object / object | Owned requests only; no CRM notes; Saved/Delivered/ProofDelivered designs; no private staff Drafts; empty success |
| FR-005 | product UUID, session | UUID / session | Yes | S15 request form | View model | Published product; no fee amount or payment action |
| FR-006 | product UUID, requirements, attachments, deadline, key | UUID / strings / assets / date / key | Yes | Submitted request ID/version and S52 route | Object | Requirements 20-5000; 0-5 attachments; deadline >=3 days; fee null |
| FR-007 | request_id, action, complexity, rationale, fee_vnd or rejection_reason, expected_version, key | UUID / enum / text / integer VND / version / key | By action | UnderReview, Approved/automatically Assigned, FeeProposed or Rejected request | Object | Sales Admin; rationale/rejection reason 1-500 chars; Simple 0; Complex 1..9999999999; proposal immutable |
| FR-008 | committed submission/assessment/acceptance/cancellation event | Internal event | Yes | durable notification | Object | In-app authoritative; event/recipient deduplicated; private S52/S19 link |
| FR-009 | buyer_organization/assignment/state filters, session | Values / session | Optional | authorized requests | Paginated object | Dony Admin assessment queue; consultant assigned work only |
| FR-010 | design, optional request, base version, scanned assets/options, action, change note, expected_version, key | IDs / values / key | Yes | immutable Draft or current SharedForReview version | Object | Current assigned Sales/Admin; service request Assigned/InProgress; technical lineage may have no request; share makes design ProofDelivered; stale 409. |
| FR-011 | committed version/feedback/reply/approval event | Internal event | Yes | notification/outbox ID | UUID | Deduplicate per recipient; reauthorize S52/S21 deep links; omit private CRM data. |
| FR-012 | request_id, proposal_version, accepted_fee_vnd, expected_version, key | UUID / integers / key | Yes | Approved/automatically Assigned request and acceptance evidence | Object | Owner; FeeProposed only; exact amount/version; repeat key replays; stale/state 409 |
| FR-013 | request_id, expected_version, key | UUID / version / key | Yes | Cancelled request | Object | Owner; preassignment only; repeated cancellation no-op; no refund |
| FR-014 | selected asset, mode, tolerance, draft revision | Asset / enum / integer / version | Yes | transparent PNG review; applied draft revision | Image / version | Solid tolerance 5–100, default 35; subject failure offers solid mode; original immutable in session. |
| FR-015 | product/template version, options, side placements, view ID, revision | IDs / object / integer | Yes | current angle preview | Image/view model | Validated product templates; unsupported views disabled; no paid AI call. |
| FR-016 | person image, derived polo image, explicit external consent, design revision, session/job token | Images / boolean / versions | Yes for generation | generated result, matching design revision, safe error | Session image/object | <=10 MiB/image and <=16 million pixels; server-only API key; no image/secret logging; no automatic paid retry. |
| FR-017 | design_id, design_version_id, change_request_text, preferred_colour?, additional_notes?, attachment_ids, expected_version, key | IDs / text / assets / version / key | Yes by field | feedback and staff notice | Object | Owner; current SharedForReview only; required text 10–500, optional texts 0–500; 0–3 scanned images <=10 MiB; one decision per shared version; stale 409. |
| FR-018 | design_id, current shared version, expected_version, key | IDs / version / key | Yes | approval evidence, Delivered design/request | Object | Owner only; not Draft/Superseded/already decided; race/stale 409; immutable exact-version evidence. |
| FR-019 | classified lead/customer, product/options, scanned assets, original channel, optional request, expected_version, key | IDs / values / key | Yes by mode | owned Design and imported immutable version | Object | Registered linked Customer; assigned staff/Admin; validate current product rules/MIME/scan/ownership; not yet orderable without source evidence. |
| FR-020 | exact unchanged imported version, original channel/source evidence, expected_version, key | IDs / text / key | Yes | CustomerProvidedConfirmation, Saved design | Object | Staff evidence 1–500 chars or explicit owner confirmation; source cannot be Dony-created/changed; stale 409. |
| FR-021 | shared design_version_id, reply text, attachment_ids, expected_version, key | ID / text / assets / key | Yes except attachments | append-only staff reply and owner notice | Object | Current assigned staff/Admin; text 1–5000; 0–3 scanned PNG/JPEG/WebP <=10 MiB; no private CRM data; stale 409. |

### 5.3 Business rules

| Rule ID | Rule | Why it exists |
| --- | --- | --- |
| BR-001 | Design status is Draft, Saved, ProofDelivered or Delivered. Current customer-visible eligibility is defined by section 5.4; immutable content and source_design_request_id survive copies and ordered snapshots. | Preserve designs, approval and fee provenance. |
| BR-002 | Submitted → UnderReview; Simple → Approved; Complex → FeeProposed → Approved on exact acceptance; Approved → Assigned → InProgress → Delivered only on owner approval; share/revision keeps InProgress. UnderReview → Rejected; eligible unassigned states → Cancelled. Delivered/Cancelled/Rejected are terminal; no auto-expiry. | Define request lifecycle without premature delivery. |
| BR-003 | Approved requests automatically follow the current classified lead owner when eligible, without waiting for committed_due_at. Only Sales Admin sets/changes that future commitment. Cancel only Submitted/UnderReview/FeeProposed/unassigned Approved; lock competing transitions. | Keep accountable assignment and cancellation races safe. |
| BR-004 | Fee is null before assessment, 0 for Simple, or integer 1..9999999999 VND for Complex. The configurable design_service_fee_vnd (default 200000) is suggested at assessment and confirmed/overridden by Admin. Accepted fee is collected only through MFG-06 order pricing, never a standalone transaction. | Keep assessed pricing explicit. |
| BR-005 | Attachments are 0-5 PNG/JPEG/WebP files <=10 MiB each, actual MIME checked/scanned. | Protect users and storage. |
| BR-006 | Consultation CRM state is independent and never changes order status. | Keep sales workflow separate from fulfillment. |
| BR-007 | Customer accepts exact Complex proposal amount/version; store customer_id, accepted_fee_vnd, accepted_fee_version equal to proposal_version, and accepted_at. Proposal/approval is immutable; changed work/fee requires eligible cancellation and a new request. All mutations use expected_version and idempotency; no request payment/refund. | Preserve explicit consent and concurrency safety. |
| BR-008 | Material/fabric choices come from Published product rules; selecting a fabric never implies unsupported catalogue additions or different geometry. Size stays on S22. | Keep product validation authoritative. |
| BR-009 | Chest shortcuts use wearer left/right; default 70 mm width and <=90 mm height with aspect ratio retained, clamped to current print bounds. Centre uses the physical print area's centre; users may refine numeric placement. | Make common corporate logo placement usable. |
| BR-010 | Processed artwork may become a scanned private design asset only on explicit design save; session-only personal try-on images/results are excluded from all save/order payloads. Preserve original/processed distinction and immutable saved versions. | Separate reusable production artwork from personal previews. |
| BR-011 | OpenAI credentials remain backend-only in an ignored secret file or secret manager; never return keys/provider raw errors or log request images/headers. Production requires authenticated owner authorization, request quotas and concurrency limits. | Protect credentials and control provider costs. |
| BR-012 | User photo replacement/removal revokes consent; stale job results are ignored. One active generation per customer session; no automatic retries. Cancelling UI work cannot promise cancellation of provider billing/processing. | Prevent wrong-photo results and accidental repeated charges. |

### 5.4 Versioned website collaboration (confirmed 2026-09-27)

S17 is the gallery, S52 is customer request/version review, S21 is staff design execution and replies, and S19/S20 are CRM orchestration. Customer-provided imports require a registered linked Customer and classified lead. Sources are CustomerUploaded, CustomerProvidedImport, DonyTechnicalAdjustment or DonyDesign; store uploader/time, original channel and change note. Original request attachments remain read-only references and are not automatically converted into V1.

Version content is immutable. Review state is separate: Draft → SharedForReview → Approved or Superseded. Customer self-saved versions are Saved/orderable under the existing S13 rule. An unchanged imported version becomes Saved/orderable only with CustomerProvidedConfirmation for that exact file. Staff may record source evidence in S21; the owner may confirm it in S52. This is not CustomerApproval and cannot be used on a Dony change. Dony-adjusted/service versions are ProofDelivered and non-orderable while review is pending; only authenticated CustomerApproval of the current SharedForReview version makes them Delivered/orderable. Review events are append-only and retain evidence/time/version.

The review-loop transition applies to Dony work. A customer save or exact unchanged-import confirmation can establish an Approved current version directly, with eligibility based on CustomerSave or CustomerProvidedConfirmation rather than CustomerApproval. Source confirmation selects that exact import as current and supersedes the prior current version; it never approves Dony work. A private/unconfirmed Draft remains non-orderable. The server returns the actual committed request state: Simple assessment or Complex fee acceptance may return Assigned rather than Approved when an eligible current lead owner exists, together with the unchanged approval/acceptance evidence.

Creating a private Draft does not switch the current shared/accepted version. Sharing explicitly selects the next current version, supersedes the previous shared version, resets current design eligibility to ProofDelivered, updates the CRM projection to InReview and notifies the owner. Already-created order snapshots remain immutable and continue under their order-specific lifecycle. Superseded approved history does not grant approval to a new current version.

A current shared version accepts exactly one owner decision: approval or revision. Approval atomically records CustomerApproval and Delivered design/request. Revision appends structured feedback, marks that version's decision as revision requested, keeps the request InProgress and the design non-orderable; staff prepare/share the next immutable version. Duplicate identical keys replay; competing or stale decisions return 409. No revision-attempt cap, shared free-round counter or revision surcharge is introduced. MFG-06 retains unlimited classroom sample rework, no separate sample fee and explicit approval of changed quotes. Terminal Delivered requests cannot be reopened by a feedback action; later order revision follows MFG-06.

Customer feedback is version-bound, with change_request_text 10–500 trimmed chars, preferred_colour/additional_notes each optional 0–500, and 0–3 safe image attachments <=10 MiB each. Staff replies are 1–5000 trimmed chars with the same attachment constraints; only current assigned Sales or Sales Admin writes them in S21. Actual PNG/JPEG/WebP MIME, scan and ownership are required before storage. A reply changes no approval, fee or design lifecycle state. Only shared and previously shared versions, Customer feedback and authorized public staff replies enter S52; private Drafts, CRM interactions, internal notes and Admin Review records never do.

CustomerProvided is mandatory for B2B2C: no creative design from scratch. Ordinary production validation creates a DonyTechnicalAdjustment version without a DesignRequest; substantial rework of supplied artwork may use the unchanged Simple/Complex fee workflow. B2B allows CustomerProvided or DonySupportRequired. Fee proposals and first-order fee allocation remain unchanged; no standalone design payment is introduced.

Eligible Approved requests follow the classified lead's current Sales owner atomically at approval/fee acceptance or lead assignment, even if committed_due_at is null. Reassignment transfers active Assigned/InProgress requests and retains their dates. Admin sets or changes the absolute future commitment separately; missing is not overdue. Request cancellation and assignment lock the same record and cannot both win. Prospective/unclassified leads cannot create owned designs or activate service work until customer linkage/classification is resolved.

## 6. Key entities (mandatory)

| Entity | Attributes (from Input/Output fields) | Relationships |
| --- | --- | --- |
| Design | customer/product IDs and optional buyer_organization_id, product/design versions, status, options, assets, preview, source_design_request_id nullable, timestamps | Immutable saved versions; customer-owned and Dony staff-authorized; server-derived provenance retained on copies; client cannot clear/replace it |
| DesignRequest | customer_id, buyer_organization_id?, product_id, requirements, attachments, requested_deadline, committed_due_at nullable until Admin sets it, complexity, rationale/rejection_reason, assessed_by/at, fee_vnd, proposal_version, accepted_fee_version, accepted_fee_vnd, accepted_by/at, fee_order_id nullable, fee_allocation_version, state, assignee, version | Standalone until order creation; optional organization identifies a Business Buyer or Reseller Shop but grants no authority; Approved before assignment; MFG-06 BR-008 owns fee allocation. |
| DesignVersion | design/version IDs, immutable assets/configuration, source, uploader/time, original channel, change note, review_state and current/shared references | Exact-version source and approval evidence; private Drafts excluded from customer APIs. |
| DesignFeedback / StaffReply | ID, design_version_id, author/role/time, structured feedback or reply text, safe attachment IDs, decision/key | Append-only customer-visible exchange; current owner/staff authorization; no CRM notes. |
| CustomerApproval | customer_id, design_version_id, approved_at, request/version/key | Owner-only approval of the exact current shared version; never staff-authored. |
| CustomerProvidedConfirmation | design_version_id, confirmer/time, original channel, source evidence/key | Unchanged imports only; separate from approval of Dony work. |
| Consultation | customer_id, buyer_organization_id?, sales_user_id, notes, related IDs, CRM status | Internal notes visible only to assigned Sales and Sales Admin. |
| Notification | event/recipient/type/payload/delivery state | Deduplicated; in-app record authoritative |
| DesignAsset variant | Original/processed artwork reference, side, X/Y/width/height mm, processing method | Owned scanned asset on explicit save; preserves original artwork lineage. |
| ProductMockupTemplate | Product/version, view ID, base image, calibrated surface grid, masks, material/colour support | Per-product rendering assets; no personal data. |
| TryOn session job | Session/job token, design revision, consent, processing state, transient photo/result | Application memory only; no persisted personal photo/result entity. |

## 7. Screens involved

| Screen ID | Screen name | Priority | Screen Spec file |
| --- | --- | --- | --- |
| S09 | Product detail and design entry | Must | `screens/S09-product_detail_screen.md` |
| S13 | Product design workspace | Must | `screens/S13-product_design_tool_screen.md` |
| S17 | Customer design gallery | Must (saved self-design) | `screens/S17-customer_designs_screen.md` |
| S15 | Design service request | Could | `screens/S15-design_service_request_screen.md` |
| S19 | Sales Admin assessment / commitment within pipeline | Could | `screens/S19-consultation_assignment_screen.md` |
| S20/S21 | Assigned pipeline / per-design staff workspace | Could | `screens/S20-consultant_tasks_and_customers_screen.md`, `screens/S21-consultation_detail_screen.md` |
| S22 | Order eligible design | Must | `screens/S22-create_order_screen.md` |
| S52 | Customer request status and design feedback/approval | Could | `screens/S52-delivered_designs_and_feedback_screen.md` |
| S38 | Notifications | Could | `screens/S38-notification_panel_screen.md` |
| S49 | Remove artwork background | Must | `screens/S49-remove_background_screen.md` |
| S50 | Product multi-angle mockups | Must | `screens/S50-product_mockups_screen.md` |
| S51 | Virtual try-on | Could | `screens/S51-virtual_try_on_screen.md` |

## 8. Success criteria (mandatory)

| SC ID | Criterion | How it is measured |
| --- | --- | --- |
| SC-001 | MVP self-design safely saves versioned, orderable work. | Verify rule validation, saved versions and order eligibility. |
| SC-002 | Simple approval or explicit Complex fee acceptance makes a request assignable; cancellation is limited to preassignment states. | Verify both assessment branches, fee consent, cancellation/assignment races and deferred order fee. |
| SC-003 | Ownership, assignment, idempotency and concurrent delivery are enforced; all functions map to FRs. | Exercise authorization/retry/race cases and compare F-DES IDs with FRs. |
| SC-004 | Removal preserves interior colours, original recovery and coordinates. | Compare border-connected/subject inputs; apply/cancel/restore and save/reopen tests. |
| SC-005 | Multi-angle prints follow calibrated garment surfaces and matching side. | Visually approve all angles and chest/centre/bounds cases per product template; no provider request on switching. |
| SC-006 | Personal images and secrets do not enter persistent application storage or client credentials. | Inspect save payloads/storage/logs; test no-consent, quota/failure, stale result and session disposal paths. |

## 9. Assumptions

- DBIZ 3 classroom demo by Group B; no approver; demo business/contact data are fictional samples.
- Self-design is Must; assessed design service and consultant workflow are Could.
- Sales Admin assesses; S52 owns acceptance/cancellation. There is no S16 screen or standalone design-service payment route; legacy URLs must not create payment side effects.
- FR-007/F-DES-007 replaces obsolete settlement with assessment; FR-012/F-DES-012 adds fee acceptance; FR-013/F-DES-013 formalizes existing US-4/BR-002/BR-003 cancellation, not a second cancellation function.
- No order means no collection; first-order fee allocation and subsequent-order rules are MFG-06 BR-008.
- 2D preview is required; 3D preview is outside this scope.

## 10. Open questions

| # | Question | Blocking? | Owner | Status |
| --- | --- | --- | --- | --- |
| 1 | Are any design/request state, fee, deadline, cancellation, refund or delivery decisions still undecided? | No | Group B | Resolved — no remaining open questions; sections 3–6 define the complete behavior. |

## 11. Traceability to DBIZ2

Historical IDs are retained; external DBIZ2 comparison is not required.

| Spec section | DBIZ2 source | Location |
| --- | --- | --- |
| Scope and actors | Function List MFG-05 | Rows 36–46 plus new rows 95–96; IDs appear in FR table |
| Design/customize | UC-C02; F-DES-001..003 | S13; sections 3 and 5 |
| Saved designs | UC-C03; F-DES-004 | S17; sections 3 and 5 |
| Service request/delivery | UC-C04, UC-S03; F-DES-005..013 | S15, S19-S21, S52; SD-05B/05C; sections 3 and 5 |
| Design add-ons | User-approved 2026-09-27 extension of UC-C02; F-DES-014..016 (new, not historical DBIZ2 IDs) | S13, S49-S51; US-6..8; FR-014..016 |

| Website collaboration | User-confirmed 2026-09-27 extension; F-DES-017..021 | S17 gallery, S19/S20 pipeline, S21 staff workspace, S52 customer review; section 5.4 |

## Completion checklist

- [x] Scope, actors, scenarios, flows and edge cases are defined.
- [x] Function, state, entity, screen and ID traceability is complete.
- [x] MVP priorities and demo assumptions are explicit.
- [x] No unresolved placeholders remain.


## 12. Design add-on implementation handoff

The user validated the OpenAI try-on demo as feasible on 2026-09-27. This is feasibility acceptance, not a client signature or a guarantee of exact identity/logo preservation. Polo is the first demo product; it does not amend MFG-04 catalogue/seed data. Self-design saving/order rules remain unchanged. S49/S50 are Must extensions; S51 is Could, following the existing preview as Must and advanced AI as optional. No local try-on fallback is required.

Production source of truth is this module and S13/S49/S50/S51. Reusable prototype code remains in `demo/polo`: `web/render.js` (calibrated grids and wearer chest geometry), `web/geometry.js`, `web/print-surface.js` (single-assignment alpha-safe rasterization and fabric light), `web/session-guard.js`/`app.js` (revision/session invalidation), `server.py` (validation, connected background removal), `ai.py` (OpenAI multipart image edits with person first, polo second). The prototype uses gpt-image-1 with high input fidelity, medium quality and no retries; model selection belongs in backend configuration in production. It is not a sizing engine.

The approved left/right demo grids were manually calibrated against collar alignment. Their numeric values belong to the current synthetic template only; reuse the algorithm and verify new templates rather than copying offsets across products. Keep client physical coordinates independent of preview geometry. Subject background removal is separate from virtual try-on; local rembg in part 01 is permitted, while part 03 exclusively uses OpenAI.

For this local demo only, backend resolves `docs/env/.env`; never include it in the documentation-only branch. Environment OPENAI_API_KEY takes precedence. Production uses server secrets, owner-authenticated endpoints, private asset storage and bounded jobs; do not copy the loopback demo security boundary as production authorization. Provider retention must be disclosed separately from session-only application storage.
