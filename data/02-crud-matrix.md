---
artifact: CRUD Matrix
step: S2
generated: 2026-09-28
sources: docs/spec/docs/function-list.md; docs/spec/specs/spec-MFG-01.md through spec-MFG-12.md; docs/spec/screens/S01 through S50
---

# WeaveLink CRUD Matrix

Ops apply to persisted logical records. Read-only projections and transient objects are identified in Anomalies rather than treated as tables.

## Interactions

| Function | Entity | Ops | Citation |
|---|---|---|---|
| F-USER-001 Registration Screen | User | R | `spec-MFG-01.md §5 FR-001`; `S04-customer-sign-up.md §3` |
| F-USER-002 Registration Logic | User | C | `spec-MFG-01.md §5 FR-002` |
| F-USER-003 Send verification link | OneTimeToken | C,U | `spec-MFG-01.md §5 FR-003`; `spec-MFG-01.md §5.2 BR-005` |
| F-USER-003 Send verification link | OutboxEvent | C | `spec-MFG-01.md §5 FR-003` |
| F-USER-004 Login Screen | User | R | `spec-MFG-01.md §5 FR-004` |
| F-USER-004 Login Screen | StaffAccount | R | `spec-MFG-01.md §5 FR-004` |
| F-USER-005 Login Logic | User | R | `spec-MFG-01.md §5 FR-005` |
| F-USER-005 Login Logic | StaffAccount | R | `spec-MFG-01.md §5 FR-005` |
| F-USER-005 Login Logic | Session | C | `spec-MFG-01.md §5 FR-005` |
| F-USER-006 Logout | Session | U | `spec-MFG-01.md §5 FR-006` |
| F-USER-008 Recovery validation | User | R | `spec-MFG-01.md §5 FR-008` |
| F-USER-009 Reset-link issue | OneTimeToken | C,U | `spec-MFG-01.md §5 FR-009` |
| F-USER-009 Reset-link issue | OutboxEvent | C | `spec-MFG-01.md §5 FR-009` |
| F-USER-010 Token verification | OneTimeToken | R | `spec-MFG-01.md §5 FR-010` |
| F-USER-011 Reset password | User | U | `spec-MFG-01.md §5 FR-011` |
| F-USER-011 Reset password | OneTimeToken | U | `spec-MFG-01.md §5 FR-011` |
| F-USER-011 Reset password | Session | U | `spec-MFG-01.md §5 FR-011` |
| F-USER-012 View notifications | Notification | R | `spec-MFG-01.md §5 FR-012` |
| F-USER-013 Mark notification read | Notification | U | `spec-MFG-01.md §5 FR-013` |
| F-PROF-001 View profile | User | R | `spec-MFG-02.md §5 FR-001` |
| F-PROF-002 Edit profile screen | User | R | `spec-MFG-02.md §5 FR-002` |
| F-PROF-003 Save profile/email change | User | U | `spec-MFG-02.md §5 FR-003` |
| F-PROF-003 Save profile/email change | OneTimeToken | C | `spec-MFG-02.md §5 FR-003`; `spec-MFG-02.md §5.2 BR-003` |
| F-PROF-004 Change-password screen | User | R | `spec-MFG-02.md §5 FR-004` |
| F-PROF-005 Change password | User | U | `spec-MFG-02.md §5 FR-005` |
| F-PROF-005 Change password | Session | U | `spec-MFG-02.md §5 FR-005` |
| F-ACC-001 List staff | StaffAccount | R | `spec-MFG-03.md §5 FR-001` |
| F-ACC-002 Staff creation form | StaffAccount | R | `spec-MFG-03.md §5 FR-002` |
| F-ACC-003 Issue invitation | StaffInvitation | C,U | `spec-MFG-03.md §5 FR-003`; `spec-MFG-03.md §5.2 BR-003` |
| F-ACC-003 Issue invitation | OutboxEvent | C | `spec-MFG-03.md §5 FR-003` |
| F-ACC-004 Create staff account | User | C | `spec-MFG-03.md §5 FR-004`; approved D3 |
| F-ACC-004 Create staff account | StaffAccount | C | `spec-MFG-03.md §5 FR-004` |
| F-ACC-004 Create staff account | StaffInvitation | C | `spec-MFG-03.md §5 FR-004` |
| F-ACC-005 View staff detail | StaffAccount | R | `spec-MFG-03.md §5 FR-005` |
| F-ACC-006 Update staff | StaffAccount | U | `spec-MFG-03.md §5 FR-006` |
| F-ACC-006 Update staff | Session | U | `spec-MFG-03.md §5 FR-006` |
| F-ACC-007 Removal eligibility | StaffAccount | R | `spec-MFG-03.md §5 FR-007` |
| F-ACC-007 Removal eligibility | CustomerAssignment | R | `spec-MFG-03.md §6 StaffWorkSummary`; `S48-staff-accounts.md §3 open_work_counts` |
| F-ACC-007 Removal eligibility | DesignRequest | R | `spec-MFG-03.md §6 StaffWorkSummary` |
| F-ACC-007 Removal eligibility | Order | R | `spec-MFG-03.md §6 StaffWorkSummary` |
| F-ACC-008 Soft-delete staff | StaffAccount | U | `spec-MFG-03.md §5 FR-008` |
| F-ACC-008 Soft-delete staff | Session | U | `spec-MFG-03.md §5 FR-008` |
| F-ACC-008 Soft-delete staff | AuditEvent | C | `spec-MFG-03.md §5 FR-008` |
| F-PROD-001 Browse catalogue | Product | R | `spec-MFG-04.md §5 FR-001` |
| F-PROD-001 Browse catalogue | ProductImage | R | `S14-product-catalog.md §3` |
| F-PROD-002 Product detail | Product | R | `spec-MFG-04.md §5 FR-002` |
| F-PROD-002 Product detail | ProductSize | R | `S15-product-detail.md §3` |
| F-PROD-002 Product detail | ProductColor | R | `S15-product-detail.md §3` |
| F-PROD-002 Product detail | ProductMaterial | R | `S15-product-detail.md §3` |
| F-PROD-002 Product detail | VolumePricingTier | R | `spec-MFG-04.md §5.2 BR-008` |
| F-PROD-002 Product detail | ProductOption | R | `S15-product-detail.md §3` |
| F-PROD-003 Search products | Product | R | `spec-MFG-04.md §5 FR-003` |
| F-PROD-004 Product management list | Product | R | `spec-MFG-04.md §5 FR-004` |
| F-PROD-005 Product creation form | Product | R | `spec-MFG-04.md §5 FR-005` |
| F-PROD-006 Save product | Product | C | `spec-MFG-04.md §5 FR-006` |
| F-PROD-006 Save product | ProductVersion | C | `spec-MFG-04.md §5.2 BR-006` |
| F-PROD-006 Save product | ProductSize | C | `spec-MFG-04.md §5.1 FR-006`; approved D2 |
| F-PROD-006 Save product | ProductColor | C | `spec-MFG-04.md §5.1 FR-006`; approved D2 |
| F-PROD-006 Save product | ProductMaterial | C | `spec-MFG-04.md §5.1 FR-006`; approved D2 |
| F-PROD-006 Save product | VolumePricingTier | C | `spec-MFG-04.md §5.1 FR-006`; approved D2 |
| F-PROD-006 Save product | ProductOption | C | `spec-MFG-04.md §5.1 FR-006`; approved D2 |
| F-PROD-006 Save product | ProductImage | C | `spec-MFG-04.md §5.1 FR-006`; approved D2/D8 |
| F-PROD-007 Product edit model | Product | R | `spec-MFG-04.md §5 FR-007` |
| F-PROD-008 Update product | Product | U | `spec-MFG-04.md §5 FR-008` |
| F-PROD-008 Update product | ProductVersion | C | `spec-MFG-04.md §5.2 BR-006` |
| F-PROD-008 Update product | ProductSize | C,R | `S19-product-design-rules.md §3`; approved D2 |
| F-PROD-008 Update product | ProductColor | C,R | `S19-product-design-rules.md §3`; approved D2 |
| F-PROD-008 Update product | ProductMaterial | C,R | `S19-product-design-rules.md §3`; approved D2 |
| F-PROD-008 Update product | ProductOption | C,R | `S19-product-design-rules.md §3`; approved D2 |
| F-PROD-008 Update product | PrintArea | C,R | `S19-product-design-rules.md §3`; approved D2 |
| F-PROD-009 Archive confirmation | Product | R | `spec-MFG-04.md §5 FR-009` |
| F-PROD-010 Archive/delete product | Product | U,D | `spec-MFG-04.md §5 FR-010`; `spec-MFG-04.md §5.2 BR-005` |
| F-PROD-011 Visibility change | Product | U | `spec-MFG-04.md §5 FR-011` |
| F-PROD-012 Product Finder | Product | R | `spec-MFG-04.md §5 FR-012..017` |
| F-PROD-012 Product Finder | SearchSynonymSet | R | `spec-MFG-04.md §5.2 BR-011` |
| F-PROD-013 AI Compare | Product | R | `spec-MFG-04.md §5 FR-018..025` |
| F-PROD-013 AI Compare | MaterialProfile | R | `spec-MFG-04.md §5 FR-025` |
| F-PROD-013 AI Compare | PrintMethod | R | `spec-MFG-04.md §5 FR-023/025` |
| F-PROD-014 Product advisory | Product | R | `spec-MFG-04.md §5 FR-021..025` |
| F-PROD-014 Product advisory | MaterialProfile | R | `spec-MFG-04.md §5 FR-025` |
| F-PROD-014 Product advisory | PrintMethod | R | `spec-MFG-04.md §5 FR-023/025` |
| F-DES-001 Design workspace | Product | R | `spec-MFG-05.md §5 FR-001` |
| F-DES-001 Design workspace | PrintArea | R | `S20-design-tool.md §3` |
| F-DES-002 Preview design | Asset | R | `spec-MFG-05.md §5 FR-002` |
| F-DES-002 Preview design | ProductOption | R | `spec-MFG-05.md §5 FR-002` |
| F-DES-003 Save design | Design | C,U | `spec-MFG-05.md §5 FR-003` |
| F-DES-003 Save design | DesignVersion | C | `spec-MFG-05.md §5 FR-003` |
| F-DES-003 Save design | DesignPlacement | C | `S20-design-tool.md §3`; approved D2 |
| F-DES-004 View designs | Design | R | `spec-MFG-05.md §5 FR-004` |
| F-DES-004 View designs | DesignRequest | R | `spec-MFG-05.md §5 FR-004` |
| F-DES-004 View designs | DesignVersion | R | `spec-MFG-05.md §5 FR-004` |
| F-DES-005 Request form | Product | R | `spec-MFG-05.md §5 FR-005` |
| F-DES-006 Submit request | DesignRequest | C | `spec-MFG-05.md §5 FR-006` |
| F-DES-006 Submit request | DesignRequestAsset | C | `spec-MFG-05.md §5.1 FR-006`; approved D8 |
| F-DES-006 Submit request | OutboxEvent | C | `spec-MFG-05.md §5 FR-006/008` |
| F-DES-007 Assess request | DesignRequest | U | `spec-MFG-05.md §5 FR-007` |
| F-DES-008 Notify request event | OutboxEvent | C | `spec-MFG-05.md §5 FR-008` |
| F-DES-009 List design work | DesignRequest | R | `spec-MFG-05.md §5 FR-009` |
| F-DES-009 List design work | CustomerAssignment | R | `spec-MFG-05.md §5.3 BR-003` |
| F-DES-010 Create/share version | Design | C,U | `spec-MFG-05.md §5 FR-010` |
| F-DES-010 Create/share version | DesignVersion | C,U | `spec-MFG-05.md §5 FR-010` |
| F-DES-010 Create/share version | DesignPlacement | C | `spec-MFG-05.md §6 DesignAsset variant`; approved D2 |
| F-DES-011 Notify collaboration | OutboxEvent | C | `spec-MFG-05.md §5 FR-011` |
| F-DES-012 Accept fee | DesignRequest | U | `spec-MFG-05.md §5 FR-012` |
| F-DES-013 Cancel request | DesignRequest | U | `spec-MFG-05.md §5 FR-013` |
| F-DES-014 Remove background | Asset | C,R | `spec-MFG-05.md §5 FR-014`; `spec-MFG-05.md §5.3 BR-010` |
| F-DES-015 Render mockups | ProductMockupTemplate | R | `spec-MFG-05.md §5 FR-015` |
| F-DES-015 Render mockups | DesignVersion | R | `spec-MFG-05.md §5 FR-015` |
| F-DES-016 Virtual try-on | DesignVersion | R | `spec-MFG-05.md §5 FR-016` |
| F-DES-017 Revision feedback | DesignFeedback | C | `spec-MFG-05.md §5 FR-017`; approved D4 |
| F-DES-017 Revision feedback | DesignFeedbackAsset | C | `spec-MFG-05.md §5.1 FR-017`; approved D8 |
| F-DES-017 Revision feedback | Asset | R | `spec-MFG-05.md §5 FR-017` |
| F-DES-018 Approve design | CustomerApproval | C | `spec-MFG-05.md §5 FR-018` |
| F-DES-018 Approve design | Design | U | `spec-MFG-05.md §5 FR-018` |
| F-DES-018 Approve design | DesignRequest | U | `spec-MFG-05.md §5 FR-018` |
| F-DES-019 Import design | Design | C | `spec-MFG-05.md §5 FR-019` |
| F-DES-019 Import design | DesignVersion | C | `spec-MFG-05.md §5 FR-019` |
| F-DES-020 Confirm customer source | CustomerProvidedConfirmation | C | `spec-MFG-05.md §5 FR-020` |
| F-DES-020 Confirm customer source | Design | U | `spec-MFG-05.md §5 FR-020` |
| F-DES-021 Staff reply | StaffReply | C | `spec-MFG-05.md §5 FR-021`; approved D4 |
| F-DES-021 Staff reply | StaffReplyAsset | C | `spec-MFG-05.md §5.1 FR-021`; approved D8 |
| F-PAY-001 Order workflow model | Design | R | `spec-MFG-06.md §5 FR-001` |
| F-PAY-001 Order workflow model | Product | R | `spec-MFG-06.md §5 FR-001` |
| F-PAY-002 Create quote | Quote | C | `spec-MFG-06.md §5 FR-002` |
| F-PAY-002 Create quote | QuoteSizeQuantity | C | `spec-MFG-06.md §5 FR-002`; approved D2 |
| F-PAY-002 Create quote | ProductVersion | R | `spec-MFG-06.md §5 FR-002` |
| F-PAY-002 Create quote | DesignVersion | R | `spec-MFG-06.md §5 FR-002` |
| F-PAY-003 Create/advance order | Order | C,U | `spec-MFG-06.md §5 FR-003` |
| F-PAY-003 Create/advance order | OrderSizeQuantity | C | `spec-MFG-06.md §6 Order`; approved D2 |
| F-PAY-003 Create/advance order | OrderQuoteCycle | C | `spec-MFG-06.md §5.2 BR-015`; approved D5 |
| F-PAY-003 Create/advance order | ProductionSample | C,U | `spec-MFG-06.md §5 FR-003` |
| F-PAY-003 Create/advance order | OrderTimelineEvent | C | `spec-MFG-06.md §5.2 BR-010` |
| F-PAY-004 Start payment | PaymentTransaction | C | `spec-MFG-06.md §5 FR-004` |
| F-PAY-004 Start payment | Order | R | `spec-MFG-06.md §5 FR-004` |
| F-PAY-005 Reconcile/refund | PaymentTransaction | R,U | `spec-MFG-06.md §5 FR-005` |
| F-PAY-005 Reconcile/refund | RefundRecord | C,U | `spec-MFG-06.md §5 FR-005`; `spec-MFG-06.md §5.2 BR-013` |
| F-PAY-005 Reconcile/refund | Order | U | `spec-MFG-06.md §5.2 BR-003/006` |
| F-PAY-005 Reconcile/refund | OrderTimelineEvent | C | `spec-MFG-06.md §5.2 BR-010` |
| F-PAY-006 Payment summary | Order | R | `spec-MFG-06.md §5 FR-006` |
| F-PAY-006 Payment summary | PaymentTransaction | R | `spec-MFG-06.md §5 FR-006` |
| F-PAY-006 Payment summary | RefundRecord | R | `spec-MFG-06.md §5 FR-006` |
| F-ORD-001 List own orders | Order | R | `spec-MFG-07.md §5 FR-001` |
| F-ORD-002 Order detail | Order | R | `spec-MFG-07.md §5 FR-002` |
| F-ORD-002 Order detail | OrderTimelineEvent | R | `spec-MFG-07.md §5 FR-002` |
| F-ORD-002 Order detail | Contract | R | `spec-MFG-07.md §5 FR-002` |
| F-ORD-002 Order detail | PaymentTransaction | R | `spec-MFG-07.md §5 FR-002` |
| F-ORD-003 Cancel order | Order | U | `spec-MFG-07.md §5 FR-003`; approved interrogation: Cancellation |
| F-ORD-003 Cancel order | OrderTimelineEvent | C | `spec-MFG-07.md §5 FR-003`; approved interrogation: Cancellation |
| F-ORD-003 Cancel order | RefundRecord | C | `spec-MFG-07.md §5.2 BR-003`; only when applicable |
| F-ORD-004 Cancellation notice | OutboxEvent | C | `spec-MFG-07.md §5 FR-004` |
| F-ORD-005 Staff order list | Order | R | `spec-MFG-07.md §5 FR-005` |
| F-ORD-005 Staff order list | CustomerAssignment | R | `spec-MFG-07.md §5 FR-005` |
| F-ORD-006 Fulfilment transition | Order | U | `spec-MFG-07.md §5 FR-006` |
| F-ORD-006 Fulfilment transition | OrderTimelineEvent | C | `spec-MFG-07.md §5 FR-006` |
| F-ORD-007 Status notice | OutboxEvent | C | `spec-MFG-07.md §5 FR-007` |
| F-SALES-001 Admin pipeline | Consultation | R | `spec-MFG-08.md §5 FR-001` |
| F-SALES-002 Lead context | Consultation | R | `spec-MFG-08.md §5 FR-002` |
| F-SALES-002 Lead context | LeadDesignLink | R | `spec-MFG-08.md §5 FR-002` |
| F-SALES-003 Assign/reassign | CustomerAssignment | C,U | `spec-MFG-08.md §5 FR-003` |
| F-SALES-003 Assign/reassign | Consultation | U | `spec-MFG-08.md §5 FR-003` |
| F-SALES-003 Assign/reassign | StageHistory | C | `spec-MFG-08.md §5 FR-003` |
| F-SALES-003 Assign/reassign | DesignRequest | U | `spec-MFG-08.md §5 FR-003` |
| F-SALES-004 Sales notices | OutboxEvent | C | `spec-MFG-08.md §5 FR-004` |
| F-SALES-005 My pipeline | Consultation | R | `spec-MFG-08.md §5 FR-005` |
| F-SALES-005 My pipeline | CustomerAssignment | R | `spec-MFG-08.md §5 FR-005` |
| F-SALES-006 Lead activity | Consultation | R | `spec-MFG-08.md §5 FR-006` |
| F-SALES-006 Lead activity | StageHistory | R | `spec-MFG-08.md §5 FR-006` |
| F-SALES-006 Lead activity | InteractionLog | R | `spec-MFG-08.md §5 FR-006` |
| F-SALES-007 Lead detail | Consultation | R | `spec-MFG-08.md §5 FR-007` |
| F-SALES-007 Lead detail | InternalNote | R | `spec-MFG-08.md §5 FR-007` |
| F-SALES-007 Lead detail | AdminReview | R | `spec-MFG-08.md §5 FR-007` |
| F-SALES-008 Pipeline actions | Consultation | U | `spec-MFG-08.md §5 FR-008` |
| F-SALES-008 Pipeline actions | StageHistory | C | `spec-MFG-08.md §5 FR-008` |
| F-SALES-008 Pipeline actions | InteractionLog | C | `spec-MFG-08.md §5 FR-008` |
| F-SALES-008 Pipeline actions | InternalNote | C | `spec-MFG-08.md §5 FR-008` |
| F-SALES-008 Pipeline actions | AdminReview | C,U | `spec-MFG-08.md §5 FR-008` |
| F-SALES-008 Pipeline actions | LeadDesignLink | C,U | `spec-MFG-08.md §5 FR-008` |
| F-CONTR-001 Find templates | ContractTemplate | R | `spec-MFG-09.md §5 FR-001` |
| F-CONTR-001 Find templates | Order | R | `spec-MFG-09.md §5 FR-001` |
| F-CONTR-002 Preview template | ContractTemplate | R | `spec-MFG-09.md §5 FR-002` |
| F-CONTR-003 Generate draft | Contract | C | `spec-MFG-09.md §5 FR-003` |
| F-CONTR-003 Generate draft | Order | R | `spec-MFG-09.md §5 FR-003` |
| F-CONTR-004 Persist Ready contract | Contract | C,U | `spec-MFG-09.md §5 FR-004` |
| F-CONTR-004 Persist Ready contract | Asset | C | `spec-MFG-09.md §5 FR-004` |
| F-CONTR-005 Ready notice | OutboxEvent | C | `spec-MFG-09.md §5 FR-005` |
| F-CONTR-006 Manage templates | ContractTemplate | C,R,U | `spec-MFG-09.md §5 FR-006` |
| F-CONTR-007 Regenerate contract | Contract | C,U | `spec-MFG-09.md §5 FR-007` |
| F-CONTR-008 Sign contract | SignatureEvidence | C | `spec-MFG-09.md §5 FR-008` |
| F-CONTR-008 Sign contract | Contract | U | `spec-MFG-09.md §5 FR-008` |
| F-CONTR-008 Sign contract | Order | U | `spec-MFG-09.md §5.2 BR-005` |
| F-CONTR-009 Signing notice | OutboxEvent | C | `spec-MFG-09.md §5 FR-009` |
| F-MER-001 Show production choice | Product | R | `spec-MFG-10.md §5 FR-001` |
| F-MER-001 Show production choice | ProductionCapacityProfile | R | `spec-MFG-10.md §5.2 BR-004/005` |
| F-MER-002 Show terms | SystemConfig | R | `spec-MFG-10.md §5 FR-001/002`; `spec-MFG-12.md §5.2 BR-006` |
| F-MER-003 Save preference | FlexiblePreference | C,U | `spec-MFG-10.md §5 FR-003` |
| F-MER-003 Save preference | Quote | U | `spec-MFG-10.md §5 FR-003` |
| F-MER-004 Recommend plans | Order | R | `spec-MFG-10.md §5 FR-004` |
| F-MER-004 Recommend plans | ProductionBatch | R | `spec-MFG-10.md §5 FR-004` |
| F-MER-004 Recommend plans | ProductionCapacityProfile | R | `spec-MFG-10.md §5 FR-004` |
| F-MER-005 Calculate benefit | ProductionBatch | R | `spec-MFG-10.md §5 FR-005` |
| F-MER-005 Calculate benefit | FlexiblePreference | R | `spec-MFG-10.md §5 FR-005` |
| F-MER-006 Approve/start plan | ProductionBatch | C,U | `spec-MFG-10.md §5 FR-006` |
| F-MER-006 Approve/start plan | BatchMembership | C,U | `spec-MFG-10.md §5 FR-006` |
| F-MER-006 Approve/start plan | IndividualProductionPlan | C,U | `spec-MFG-10.md §5 FR-006`; approved D4 |
| F-MER-006 Approve/start plan | ProductionReadiness | C,U | `spec-MFG-10.md §5.2 BR-002/003` |
| F-MER-006 Approve/start plan | Order | U | `spec-MFG-10.md §5.2 BR-006` |
| F-MER-007 Planning notice | OutboxEvent | C | `spec-MFG-10.md §5 FR-007` |
| F-DA-001 Dashboard | AnalyticsResult | C,R | `spec-MFG-11.md §5 FR-001`; `spec-MFG-11.md §6` |
| F-DA-001 Dashboard | AnalyticsEvent | R | `spec-MFG-11.md §5.4` |
| F-DA-002 Metric detail | AnalyticsResult | C,R | `spec-MFG-11.md §5 FR-002` |
| F-DA-003 Export | ExportRequest | C,R,U | `spec-MFG-11.md §5 FR-003`; `spec-MFG-11.md §5.6` |
| F-DA-003 Export | AnalyticsResult | R | `spec-MFG-11.md §5.6` |
| F-DA-004 Funnel | ProductEntry | R | `spec-MFG-11.md §5.3/5.4` |
| F-DA-004 Funnel | JourneyIntent | R | `spec-MFG-11.md §5.3/5.4` |
| F-DA-004 Funnel | AnalyticsEvent | R | `spec-MFG-11.md §5.4` |
| F-DA-004 Funnel | AnalyticsResult | C,R | `spec-MFG-11.md §5 FR-004` |
| F-DA-006 AI analysis | AnalyticsResult | R | `spec-MFG-11.md §5.5` |
| F-SYS-001 View logs | AuditEvent | R | `spec-MFG-12.md §5 FR-001` |
| F-SYS-002 Search logs | AuditEvent | R | `spec-MFG-12.md §5 FR-002` |
| F-SYS-003 Backup console | Backup | R | `spec-MFG-12.md §5 FR-003` |
| F-SYS-004 Run backup | Backup | C,U | `spec-MFG-12.md §5 FR-004` |
| F-SYS-005 Restore | Backup | R | `spec-MFG-12.md §5 FR-005` |
| F-SYS-005 Restore | RestoreJournal | C,U | `spec-MFG-12.md §5 FR-005`; `spec-MFG-12.md §5.2 BR-004` |
| F-SYS-005 Restore | Session | U | `spec-MFG-12.md §5.2` restore success rule |
| F-SYS-006 Settings form | SystemConfig | R | `spec-MFG-12.md §5 FR-006` |
| F-SYS-007 Save configuration | SystemConfig | C | `spec-MFG-12.md §5 FR-007`; versioned activation |
| F-SYS-007 Save configuration | AuditEvent | C | `spec-MFG-12.md §5 FR-007` |
| F-SYS-008 Config notice | OutboxEvent | C | `spec-MFG-12.md §5 FR-008` |

## Coverage per entity

| Entity | Created by | Read by | Updated by | Deleted by |
|---|---|---|---|---|
| User | F-USER-002, F-ACC-004 | F-USER-001/004/005/008, F-PROF-001/002/004 | F-USER-011, F-PROF-003/005 | — |
| StaffAccount | F-ACC-004 | F-USER-004/005, F-ACC-001/002/005/007 | F-ACC-006/008 | Soft-delete through F-ACC-008 |
| Session | F-USER-005 | — | F-USER-006/011, F-PROF-005, F-ACC-006/008, F-SYS-005 | — |
| OneTimeToken | F-USER-003/009, F-PROF-003 | F-USER-010 | F-USER-003/009/011 | — |
| Notification | Owning outbox projection | F-USER-012 | F-USER-013 | — |
| OutboxEvent | Notification-producing functions | Worker projection | Delivery worker | — |
| StaffInvitation | F-ACC-003/004 | — | F-ACC-003 | — |
| Product and normalized children | F-PROD-006 | F-PROD-001..014, F-DES-001/002, F-PAY-001/002 | F-PROD-008/011 | Draft hard-delete only; otherwise archive |
| Asset/ProductImage | Upload/save/generate functions | Product, design, contract and evidence functions | Scan/lifecycle processing | No unsupported deletion rule |
| SearchSynonymSet | Seed/admin source not specified | F-PROD-012 | Administration not specified | — |
| PrintMethod/MaterialProfile | Seed/reference source | F-PROD-013/014 | Administration not specified | — |
| Design/DesignVersion/Placement | F-DES-003/010/019 | F-DES-004/015/016, F-PAY-001/002 | F-DES-010/018/020 | — |
| DesignRequest | F-DES-006 | F-DES-004/009, F-ACC-007 | F-DES-007/012/013/018, F-SALES-003 | — |
| DesignFeedback/StaffReply and their Asset links; Approval/Confirmation | F-DES-017/021/018/020 | Collaboration detail views | Append-only | — |
| Quote and QuoteSizeQuantity | F-PAY-002 | F-PAY-003, F-MER-003 | F-MER-003 replacement | — |
| Order and OrderSizeQuantity | F-PAY-003 | F-PAY-004/006, F-ORD-001/002/005, contract/merge functions | Payment, fulfilment, contract and planning functions | — |
| OrderQuoteCycle/ProductionSample | F-PAY-003 | Order detail/contract generation | F-PAY-003 | — |
| PaymentTransaction/RefundRecord | F-PAY-004/F-PAY-005 | F-PAY-005/006, F-ORD-002 | F-PAY-005 | — |
| OrderTimelineEvent | Order/payment/fulfilment transitions | F-ORD-002, analytics projection | Append-only | — |
| Consultation and CRM children | F-SALES-003/008 or approved S27 lead action | F-SALES-001/002/005/006/007 | F-SALES-003/008 | — |
| ContractTemplate | F-CONTR-006 | F-CONTR-001/002 | F-CONTR-006 | Archive only |
| Contract/SignatureEvidence | F-CONTR-003/004/007/008 | F-ORD-002 and contract views | F-CONTR-004/007/008 | Void/supersede only |
| FlexiblePreference | F-MER-003 | F-MER-005 | F-MER-003 | — |
| ProductionReadiness/Plan/Batch/Membership | F-MER-006 | F-MER-004/005/006 | F-MER-006 | Release membership before start only |
| ProductionCapacityProfile | Approved S19 write | F-MER-001/004/006 | Approved S19 write | Inactivation/versioning only |
| ProductEntry/JourneyIntent/AnalyticsEvent | Validated collector/owning events | F-DA-001/004 | Append-only | Retention cleanup only |
| AnalyticsResult | F-DA-001/002/004 | F-DA-001/002/003/004/006 | — | Seven-day expiry cleanup |
| ExportRequest | F-DA-003 | F-DA-003 | F-DA-003 worker | Seven-day expiry cleanup |
| AuditEvent | Business/system actions | F-SYS-001/002 | Append-only | 365-day retention cleanup |
| Backup | F-SYS-004 | F-SYS-003/005 | F-SYS-004 worker | Retention cleanup |
| SystemConfig | F-SYS-007 | F-MER-002, F-SYS-006 | New version, not in-place | — |
| RestoreJournal | F-SYS-005 | Restore/reconciliation worker | F-SYS-005 | — |

## Anomalies

| Kind | Entity or function | Hypothesis (missing function / surplus entity) | Resolution |
|---|---|---|---|
| Entity with no C | SearchSynonymSet | Missing administration function | Retain as a versioned seed/reference entity; storage/administration remains a Plan decision (`spec-MFG-04.md §10 Q3`). |
| Entity with no C | PrintMethod, MaterialProfile, ProductMockupTemplate | Missing administration function | Retain as seeded reference data because product comparison/mockup functions require them; do not invent admin functions. |
| Entity with no C | ProductionCapacityProfile | Missing function in function list | The approved S19 extension is its write surface (`S19-product-design-rules.md §Deferred production-flexibility fields`). |
| Entity with no C/U/D | StaffWorkSummary | Surplus persisted entity | Treat as a derived read projection, not a table or CSV (approved D1). |
| Entity with no C/U/D | ProductSearchIndex | Surplus mandated table | Treat as a logical derived projection; physical storage is a Plan decision (approved D1). |
| Entity with no C/U/D | MergeRecommendation | Surplus persisted entity | Treat as a transient calculation that reserves nothing (approved D1). |
| Entity with no C/U/D | TryOnSessionJob, AIAnalysisResult | Surplus persisted entity | Keep session-memory only as explicitly required; no table/CSV (approved D1). |
| Function touching no entity | F-USER-007 Recovery form | Missing function | Screen-only function; no persisted interaction required. |
| Function touching no entity | Static About/Contact screens | Missing function | Static content; intentionally outside business data CRUD. |
| Multiple creators | Notification | Ownership unclear | Owning modules create OutboxEvent; MFG-01 projection creates the recipient Notification, separating ownership (approved D4). |
| Multiple creators | AuditEvent | Ownership unclear | Events originate across modules but MFG-12 owns schema, redaction and retention. |
| Declared entity untouched | SystemCapability | Surplus entity | Derive from active StaffAccount and User capability; no separate table (approved D1/D3). |
| Declared entity untouched | ChatSession/ChatMessage | Missing persistence decision | Exclude from persisted model/CSV until the Plan decision; the five-turn behavior remains a transient contract (approved D1). |

