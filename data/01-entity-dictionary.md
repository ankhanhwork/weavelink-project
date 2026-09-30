---
artifact: Entity Dictionary
step: S1
generated: 2026-09-28
sources: docs/prd.md; docs/spec/README.md; docs/spec/specs/spec-MFG-01.md through spec-MFG-12.md; docs/spec/screens/S01 through S50
---

# WeaveLink Entity Dictionary

## Entities

| Canonical name | Definition (one sentence) | THING/EVENT | Owner | Aliases | Citation |
|---|---|---|---|---|---|
| User | First-party identity holding the normalized email, name, credential hash, verification and access state. | THING | MFG-01 | Customer identity, Member | `spec-MFG-01.md §6 User`; `spec-MFG-02.md §6 User`; approved interrogation: Account deletion |
| StaffAccount | Dony employee role and lifecycle record linked one-to-one to a User when present. | THING | MFG-03 | Employee account | `spec-MFG-01.md §6 StaffAccount`; `spec-MFG-03.md §6 StaffAccount`; approved D3 |
| Session | Revocable authenticated server session for one User. | THING | MFG-01 | — | `spec-MFG-01.md §6 Session`; `spec-MFG-01.md §5.2 BR-004` |
| OneTimeToken | Hashed, purpose-bound, expiring verification, recovery or email-change token. | THING | MFG-01 | Verification token, reset token | `spec-MFG-01.md §6 OneTimeToken`; `spec-MFG-02.md §6 OneTimeToken` |
| Notification | Persisted in-app inbox item for one recipient. | EVENT | MFG-01 | Inbox notification | `spec-MFG-01.md §6 Notification`; `S13-notifications.md §3` |
| OutboxEvent | Durable post-commit delivery event used to create notifications or email work. | EVENT | MFG-01 | Notification/outbox event | `spec-MFG-07.md §6 Notification/outbox event`; `spec-MFG-01.md §5 FR-003/009`; source modules emit their own events through this MFG-01-owned delivery record |
| StaffInvitation | Single-use employee activation invitation. | EVENT | MFG-03 | Invitation | `spec-MFG-03.md §6 StaffInvitation` |
| SystemCapability | Read projection of active staff role capabilities, not a separately persisted table. | THING | MFG-01 | Capabilities | `spec-MFG-01.md §6 SystemCapability`; `spec-MFG-01.md §5.2 BR-002`; approved D1/D3 |
| StaffWorkSummary | Derived open-work counts used to decide whether staff removal is safe. | THING | MFG-03 | Open work counts | `spec-MFG-03.md §6 StaffWorkSummary`; `S48-staff-accounts.md §3 open_work_counts`; approved D1 |
| Product | Dony-owned configurable garment base rather than finished-goods inventory. | THING | MFG-04 | Product base | `spec-MFG-04.md §6 Product`; `README.md §Dony business model` |
| ProductVersion | Immutable version marker and rule/price snapshot for a Product. | EVENT | MFG-04 | Product snapshot version | `spec-MFG-04.md §6 ProductVersion`; `spec-MFG-04.md §5.2 BR-006` |
| ProductSize | Supported size value for a ProductVersion. | THING | MFG-04 | supported_sizes | `S17-product-create.md §3 supported_sizes`; `spec-MFG-04.md §5.2 BR-003`; approved D2 |
| ProductColor | Supported colour value for a ProductVersion. | THING | MFG-04 | available_colors, supported colors | `spec-MFG-04.md §6 Product.available_colors`; `S17-product-create.md §3 supported_sizes/colors/materials`; approved D2 |
| ProductMaterial | Supported material option linked to a MaterialProfile for a ProductVersion. | THING | MFG-04 | materials, material_label | `spec-MFG-04.md §6 Product`; `spec-MFG-04.md §5.5`; approved D2 |
| VolumePricingTier | Aggregate-quantity lower/upper bound and unit price for a ProductVersion. | THING | MFG-04 | volume_pricing_tiers | `spec-MFG-04.md §5.1 FR-006`; `spec-MFG-04.md §5.2 BR-008`; approved D2 |
| ProductOption | Per-garment configurable option and surcharge for a ProductVersion. | THING | MFG-04 | options, print option | `spec-MFG-04.md §6 Product.options`; `S19-product-design-rules.md §3`; approved D2 |
| PrintArea | Bounded side-specific two-dimensional printable geometry for a ProductVersion and size. | THING | MFG-04 | design rule, printable area | `S19-product-design-rules.md §3 print_area`; `S20-design-tool.md §3`; approved D2 |
| ProductImage | Ordered relationship between a ProductVersion and an Asset. | THING | MFG-04 | images, image_asset_ids | `spec-MFG-04.md §6 Product.images`; `S17-product-create.md §3 image_asset_ids`; approved D2/D8 |
| Asset | Private scanned file metadata and storage reference owned by a User or Dony. | THING | MFG-05 | Design asset, PDF asset, delivery evidence | `spec-MFG-04.md §6 Asset`; `spec-MFG-05.md §5.3 BR-005`; approved D8; MFG-04 and MFG-09 reference the MFG-05-owned record |
| ProductSearchIndex | Derived Published-product search projection; physical persistence is a Plan decision. | THING | MFG-04 | Search index | `spec-MFG-04.md §6 ProductSearchIndex`; `spec-MFG-04.md §10 Q2`; approved D1 |
| SearchSynonymSet | Versioned server-owned synonym mapping used by catalogue search. | THING | MFG-04 | Synonym set | `spec-MFG-04.md §6 SearchSynonymSet`; `spec-MFG-04.md §5.2 BR-011` |
| PrintMethod | Print capability and material-compatibility reference. | THING | MFG-04 | — | `spec-MFG-04.md §6 PrintMethod` |
| MaterialProfile | Technical comparison profile keyed by exact material label. | THING | MFG-04 | — | `spec-MFG-04.md §6 MaterialProfile` |
| ChatSession | Five-exchange AI catalogue conversation context whose persistence is deferred to Plan. | THING | MFG-04 | Compare/advisory context | `spec-MFG-04.md §6 ChatSession`; `spec-MFG-04.md §5.5`; approved D1 |
| ChatMessage | One question/answer item in a catalogue AI context window whose persistence is deferred to Plan. | EVENT | MFG-04 | — | `spec-MFG-04.md §6 ChatMessage`; approved D1 |
| Design | Customer-owned design aggregate bound to a Product and immutable versions. | THING | MFG-05 | Saved design | `spec-MFG-05.md §6 Design`; `spec-MFG-05.md §5.3 BR-001` |
| DesignVersion | Immutable saved/imported/staff-produced design content and review state. | EVENT | MFG-05 | Design revision | `spec-MFG-05.md §6 DesignVersion`; `spec-MFG-05.md §5.4` |
| DesignPlacement | Side-specific physical placement of one artwork Asset in a DesignVersion. | THING | MFG-05 | DesignAsset variant, artwork placement | `spec-MFG-05.md §6 DesignAsset variant`; `S20-design-tool.md §3 Artwork placement`; approved D2/D8 |
| DesignRequest | Customer request for assessed Dony design service. | EVENT | MFG-05 | Service request | `spec-MFG-05.md §6 DesignRequest`; `spec-MFG-05.md §5.3 BR-002` |
| DesignRequestAsset | Relationship from a DesignRequest to one safe attachment Asset. | THING | MFG-05 | attachment_ids | `spec-MFG-05.md §5.1 FR-006`; `S24-design-service-request.md §3 attachment_ids`; approved D8 |
| DesignFeedback | Append-only Customer revision decision and structured feedback for one shared DesignVersion. | EVENT | MFG-05 | Customer feedback | `spec-MFG-05.md §6 DesignFeedback / StaffReply`; `spec-MFG-05.md §5.1 FR-017`; approved D4 |
| DesignFeedbackAsset | Relationship from DesignFeedback to one safe image attachment. | THING | MFG-05 | feedback attachment_ids | `spec-MFG-05.md §5.1 FR-017`; approved D8 |
| StaffReply | Append-only customer-visible staff response to DesignFeedback. | EVENT | MFG-05 | DesignFeedback / StaffReply | `spec-MFG-05.md §6 DesignFeedback / StaffReply`; `spec-MFG-05.md §5.1 FR-021`; approved D4 |
| StaffReplyAsset | Relationship from StaffReply to one safe image attachment. | THING | MFG-05 | reply attachment_ids | `spec-MFG-05.md §5.1 FR-021`; approved D8 |
| CustomerApproval | Owner approval evidence for the exact current shared DesignVersion. | EVENT | MFG-05 | Design approval | `spec-MFG-05.md §6 CustomerApproval`; `spec-MFG-05.md §5.1 FR-018` |
| CustomerProvidedConfirmation | Evidence that an unchanged imported design is the Customer's own source. | EVENT | MFG-05 | Source confirmation | `spec-MFG-05.md §6 CustomerProvidedConfirmation`; `spec-MFG-05.md §5.1 FR-020` |
| ProductMockupTemplate | Calibrated per-product rendering template and supported view metadata. | THING | MFG-05 | Mockup template | `spec-MFG-05.md §6 ProductMockupTemplate`; `spec-MFG-05.md §5.1 FR-015` |
| TryOnSessionJob | Session-only AI try-on processing state, explicitly not persisted. | EVENT | MFG-05 | TryOn session job | `spec-MFG-05.md §6 TryOn session job`; `spec-MFG-05.md §5.3 BR-010`; approved D1 |
| Quote | Expiring server-computed immutable commercial proposal owned by a Customer. | EVENT | MFG-06 | Price quote | `spec-MFG-06.md §6 Quote`; `spec-MFG-06.md §5.1 FR-002` |
| QuoteSizeQuantity | Quantity for one supported size in a Quote snapshot. | THING | MFG-06 | quantities, quantity_by_size | `spec-MFG-06.md §5.1 FR-002`; `S30-create-order.md §3 quantity_by_size`; approved D2 |
| Order | Made-to-order commercial aggregate with immutable product, design, buyer, address, quantity and price snapshots. | EVENT | MFG-06 | Production order | `spec-MFG-06.md §6 Order`; approved interrogation: Change over time |
| OrderSizeQuantity | Immutable size quantity copied into an Order snapshot. | THING | MFG-06 | quantity snapshot | `spec-MFG-06.md §6 Order`; `S35-customer-order-detail.md §3 item_snapshot`; approved D2 |
| OrderQuoteCycle | Association preserving each immutable design/quote/sample revision cycle of one Order. | EVENT | MFG-06 | Design/quote approval cycle | `spec-MFG-06.md §5.2 BR-015`; order transition `SampleShipped→AwaitingDigitalApproval`; approved D5 |
| ProductionSample | Versioned physical-sample cycle for an Order. | THING | MFG-06 | Sample | `spec-MFG-06.md §6 ProductionSample`; `spec-MFG-06.md §5.2 BR-015` |
| PaymentTransaction | Immutable DEPOSIT or BALANCE payment attempt and accepted provider outcome. | EVENT | MFG-06 | Payment attempt | `spec-MFG-06.md §6 PaymentTransaction`; `spec-MFG-06.md §5.2 BR-005` |
| RefundRecord | Provider refund record only where full-system refund rules require it. | EVENT | MFG-06 | Refund workflow reference | `spec-MFG-06.md §5.1 FR-005`; `spec-MFG-06.md §5.2 BR-013`; approved interrogation: Cancellation |
| OrderTimelineEvent | Append-only evidence of an Order transition, actor/source and bound versions. | EVENT | MFG-06 | Order timeline event | `spec-MFG-06.md §6 OrderTimelineEvent`; `spec-MFG-07.md §6 Order timeline event`; approved interrogation: Cancellation; MFG-07 reads and causes transitions on the MFG-06-owned record |
| CustomerAssignment | Current Sales ownership plus retained assignment history for a Customer/open lead. | EVENT | MFG-08 | Sales assignment | `spec-MFG-08.md §6 CustomerAssignment`; `spec-MFG-08.md §5.2 BR-001` |
| Consultation | One open classified or unclassified Sales lead for a Customer. | THING | MFG-08 | Consultation (Lead) | `spec-MFG-08.md §6 Consultation (Lead)` |
| LeadDesignLink | Lead-specific commercial scope link to an authoritative Design. | THING | MFG-08 | — | `spec-MFG-08.md §6 LeadDesignLink`; `spec-MFG-08.md §5.2 BR-008` |
| StageHistory | Append-only Consultation pipeline transition. | EVENT | MFG-08 | — | `spec-MFG-08.md §6 StageHistory` |
| InteractionLog | Append-only summary of external Customer contact. | EVENT | MFG-08 | Customer interaction | `spec-MFG-08.md §6 InteractionLog`; `spec-MFG-08.md §5.4` |
| InternalNote | Append-only staff-only Consultation note. | EVENT | MFG-08 | — | `spec-MFG-08.md §6 InternalNote`; `spec-MFG-08.md §5.4` |
| AdminReview | Structured Sales-to-Sales-Admin decision record. | EVENT | MFG-08 | — | `spec-MFG-08.md §6 AdminReview`; `spec-MFG-08.md §5.2 BR-011` |
| ContractTemplate | Versioned Dony-owned contract template. | THING | MFG-09 | — | `spec-MFG-09.md §6 ContractTemplate`; `spec-MFG-09.md §5.2 BR-002` |
| Contract | Immutable generated order contract and private PDF reference. | THING | MFG-09 | — | `spec-MFG-09.md §6 Contract` |
| SignatureEvidence | Customer acknowledgement evidence bound to one Contract version/hash. | EVENT | MFG-09 | Signature | `spec-MFG-09.md §6 SignatureEvidence`; `spec-MFG-09.md §5.2 BR-004/005` |
| FlexiblePreference | Customer's immutable accepted standard/flexible commercial choice on a Quote. | EVENT | MFG-10 | FlexiblePreference | `spec-MFG-10.md §6 FlexiblePreference / production plan`; `spec-MFG-10.md §5.1 FR-003`; approved D4 |
| IndividualProductionPlan | Sales-Admin-approved non-batch plan for a flexible Order. | THING | MFG-10 | production plan | `spec-MFG-10.md §5.1 FR-006`; `spec-MFG-10.md §5.2 BR-003/006`; approved D4 |
| ProductionReadiness | Snapshotted readiness/calendar dates and accepted production window for an Order. | THING | MFG-10 | — | `spec-MFG-10.md §6 ProductionReadiness`; `spec-MFG-10.md §5.3` |
| ProductionCapacityProfile | Versioned shared daily throughput for one garment production type/material identity. | THING | MFG-10 | Capacity profile | `spec-MFG-10.md §6 ProductionCapacityProfile`; approved interrogation: Duplicates |
| MergeRecommendation | Nonbinding calculated batch candidate that reserves no capacity. | THING | MFG-10 | Recommendation | `spec-MFG-10.md §6 MergeRecommendation`; `spec-MFG-10.md §5.2 BR-006`; approved D1 |
| ProductionBatch | Human-approved shared sewing run and lifecycle. | THING | MFG-10 | Batch | `spec-MFG-10.md §6 ProductionBatch` |
| BatchMembership | Exclusive active association between a ProductionBatch and an Order, with release/start history. | EVENT | MFG-10 | — | `spec-MFG-10.md §6 BatchMembership`; `spec-MFG-10.md §5.2 BR-007` |
| ProductEntry | Authenticated Product detail entry evidence used for analytics attribution. | EVENT | MFG-11 | ProductEntry / Journey attribution | `spec-MFG-11.md §6 ProductEntry / Journey attribution`; approved D4 |
| JourneyIntent | Explicit design/order intent and continuation attribution. | EVENT | MFG-11 | Journey attribution | `spec-MFG-11.md §5.3`; `spec-MFG-11.md §6 ProductEntry / Journey attribution`; approved D4 |
| AnalyticsEvent | Deduplicated validated interaction or authoritative business-event projection. | EVENT | MFG-11 | — | `spec-MFG-11.md §6 AnalyticsEvent`; `spec-MFG-11.md §5.4` |
| AnalyticsResult | Protected immutable aggregate result shared by charts, exports and AI. | THING | MFG-11 | — | `spec-MFG-11.md §6 AnalyticsResult`; `spec-MFG-11.md §5.7` |
| ExportRequest | Asynchronous private export job pinned to an AnalyticsResult. | EVENT | MFG-11 | Export job | `spec-MFG-11.md §6 ExportRequest`; `spec-MFG-11.md §5.6/5.7` |
| AIAnalysisResult | Page-memory-only grounded explanation, explicitly not persisted. | EVENT | MFG-11 | — | `spec-MFG-11.md §6 AIAnalysisResult`; `spec-MFG-11.md §5.7`; approved D1 |
| AuditEvent | Redacted append-only operational audit record. | EVENT | MFG-12 | System log | `spec-MFG-12.md §6 AuditEvent`; `spec-MFG-12.md §5.2 BR-001` |
| Backup | Verified encrypted base backup and manifest. | THING | MFG-12 | Backup job | `spec-MFG-12.md §6 Backup`; `spec-MFG-12.md §5.2 BR-002/003` |
| SystemConfig | Immutable activated configuration version. | THING | MFG-12 | Settings version | `spec-MFG-12.md §6 SystemConfig`; `spec-MFG-12.md §5.2 BR-005` |
| RestoreJournal | Restore operation and external payment-event reconciliation record kept outside the restored snapshot. | EVENT | MFG-12 | Restore journal | `spec-MFG-12.md §6 Restore journal`; `spec-MFG-12.md §5.2 BR-004` |

## Implied but never declared

| Field name | Source | Why it looks like an entity |
|---|---|---|
| supported_sizes | `S17-product-create.md §3`; `spec-MFG-04.md §5.2 BR-003` | Repeating values with version ownership; approved as ProductSize under D2. |
| available_colors | `spec-MFG-04.md §6 Product`; `spec-MFG-04.md §5.2 BR-016` | Repeating product variants; approved as ProductColor under D2. |
| materials / material_label | `spec-MFG-04.md §6 Product`; `spec-MFG-04.md §5.5` | Multi-material options must link to exact MaterialProfile labels; approved as ProductMaterial. |
| volume_pricing_tiers | `spec-MFG-04.md §5.1 FR-006`; `spec-MFG-04.md §5.2 BR-008` | Ordered repeating bounds/prices; approved as VolumePricingTier. |
| design_rules / print_area | `spec-MFG-04.md §6 Product`; `S19-product-design-rules.md §3` | Versioned repeating side/size geometry; approved as PrintArea/ProductOption. |
| quantity_by_size | `S30-create-order.md §3`; `spec-MFG-06.md §5.1 FR-002` | Repeating size/quantity facts copied to Quote and Order; approved as size-quantity children. |
| artwork placement | `S20-design-tool.md §3`; `spec-MFG-05.md §6 DesignAsset variant` | Repeating Asset/version/side geometry; approved as DesignPlacement. |
| request/feedback/reply attachment_ids | `spec-MFG-05.md §5.1 FR-006/017/021` | Repeating safe Asset references requiring relationship tables; approved as DesignRequestAsset, DesignFeedbackAsset and StaffReplyAsset under D8. |
| design/quote/sample cycle | `spec-MFG-06.md §5.2 BR-015` | Revision creates repeatable immutable cycle evidence; approved as OrderQuoteCycle. |
| refund workflow reference | `spec-MFG-06.md §5.1 FR-003/005`; `spec-MFG-06.md §5.2 BR-013` | Provider refund has its own status/reference only for full-system refund behavior; approved as RefundRecord. |

## Conflicts requiring a human decision

| Type (synonym / collision / shared ownership / type mismatch) | Items | Sources | What must be decided | Decision |
|---|---|---|---|---|
| synonym | Order timeline event / OrderTimelineEvent | `spec-MFG-06.md §6`; `spec-MFG-07.md §6` | Canonical name | Use `OrderTimelineEvent`. |
| synonym | Consultation / Consultation (Lead) | `spec-MFG-05.md §6`; `spec-MFG-08.md §6` | Whether both describe the CRM lead | Use one `Consultation` owned by MFG-08; MFG-05 references it. |
| collision | Notification / Notification-outbox event | `spec-MFG-01.md §6`; `spec-MFG-07.md §6` | Inbox record versus delivery event | Keep separate `Notification` and `OutboxEvent` entities (approved D4). |
| shared ownership | User identity fields / StaffAccount identity fields | `spec-MFG-01.md §6`; `spec-MFG-03.md §6` | Authoritative owner of name/email/password | User owns identity fields; StaffAccount owns role/lifecycle (approved D3). |
| type mismatch | Product.material_label / supported materials | `spec-MFG-04.md §6`; `S17-product-create.md §3` | Single label versus multi-material Product | Normalize to ProductMaterial rows, each referencing one MaterialProfile (approved D2). |
| synonym | capacity / max_units_per_order | `spec-MFG-04.md §6`; `S17-product-create.md §3` | Canonical field | Use `max_units_per_order`; it is a validation ceiling, not stock. |
| collision | DesignFeedback / StaffReply | `spec-MFG-05.md §6`; `spec-MFG-05.md §5.1 FR-017/021` | One table or distinct event types | Separate entities (approved D4). |
| collision | FlexiblePreference / production plan | `spec-MFG-10.md §6`; `spec-MFG-10.md §5.1 FR-003/006` | Commercial consent versus operational plan | Separate FlexiblePreference and IndividualProductionPlan/ProductionBatch (approved D4). |
| collision | ProductEntry / Journey attribution | `spec-MFG-11.md §6`; `spec-MFG-11.md §5.3` | Entry versus intent | Separate ProductEntry and JourneyIntent (approved D4). |
| shared ownership | BuyerOrganization snapshot | `spec-MFG-06.md §6`; `README.md §Dony business model` | Master organization or transaction value object | No master table; embed immutable buyer snapshot fields in Quote, Order and Contract (approved D7). |
| deletion behavior | Customer account and commercial history | approved interrogation: Account deletion; `spec-MFG-03.md §5.2 BR-006` | Cascade delete versus retained history | Revoke access; retain justified commercial evidence, then delete/anonymize personal data when retention no longer applies. |
