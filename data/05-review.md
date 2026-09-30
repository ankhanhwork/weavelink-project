---
artifact: Data Model Review
step: S6
generated: 2026-09-28
sources: docs/prd.md; docs/spec/README.md; docs/spec/specs/spec-MFG-01.md through spec-MFG-12.md; docs/spec/screens/S01 through S50; data/01-entity-dictionary.md; data/02-crud-matrix.md; data/03-erd.mmd; data/04-data-model.md; data/seed/*.csv
---

# WeaveLink Data Model Review

## Rubric

| Criterion | Result | Evidence from the input | Minimum change proposed |
|---|---|---|---|
| Completeness | Pass | Every persisted field group in module §5 I/O and §6 entity tables is represented directly, as a cited normalized child, or as a cited immutable snapshot in `04-data-model.md`. Transient/derived objects are explicitly excluded under `01-entity-dictionary.md` D1. | None. Revisit only if the Plan step chooses persistence for catalogue chat/search projections. |
| Correctness | Pass | Cardinalities follow explicit ownership, lifecycle and version language in MFG-01..12; every ERD relationship has a citation comment. `04-data-model.md` assigns a type only in its Spec-declared data types section and leaves all other field types unassigned for the Plan step. Order cancellation and change-over-time behavior use the confirmed human answers. | None. |
| Minimality | Pass | Identity values live on User rather than being duplicated on StaffAccount; no BuyerOrganization master, cancellation table, SystemCapability table, StaffWorkSummary table, search-index table, MergeRecommendation table, TryOn table or AI chat/result table is introduced. | None. |
| Readability | Pass | The logical model is grouped into identity, catalogue, design, order/payment/contract, CRM/production and analytics/operations domains; canonical aliases are recorded in `01`. | None. |
| Extensibility | Pass | Product rules and order quantities are normalized and versioned; immutable Quote/Order snapshots and OrderQuoteCycle preserve historical behavior when current catalogue data changes. | None. |
| Integration | Pass | VNPay uses PaymentTransaction/provider identities and RestoreJournal; SMTP/in-app delivery uses OutboxEvent/Notification; private files use Asset; AI try-on and analytics conversation are transient according to the external-system boundaries. | None. Provider/runtime selection remains a Plan task and is not invented here. |
| Traceability | Pass | Every table row, spec-declared type, conflict decision and ERD relationship cites `docs/spec/` or a confirmed human decision grounded in the interrogation module. Natural-key coverage explicitly assesses all 66 logical tables without promoting operational uniqueness rules into unsupported business identities. | None. |

## Seed scenario coverage

Coverage means that the CSV package contains the persistent data prerequisites and representative states for the scenario. It does not claim that application code, external providers or deferred screens exist.
`Must` is the approved MVP path; `Should`, `Could`, and `Won't` retain the meanings defined in `docs/prd.md §1`. Release status is recorded here instead of inventing a priority column in product tables.

| Scenario ID | Rows that make it runnable | Covered? |
|---|---|---|
| MFG-01 US-1 Register account | `users`, `one_time_tokens`, `outbox_events` | Yes (Must/MVP) |
| MFG-01 US-2 Log in | `users`, `staff_accounts`, `sessions` | Yes (Must/MVP) |
| MFG-01 US-3 Forgot password | `users`, `one_time_tokens`, `outbox_events` | Yes (Must/MVP) |
| MFG-01 US-4 Reset password | consumed and active rows in `one_time_tokens`; revoked row in `sessions` | Yes (Must/MVP) |
| MFG-01 US-5 Log out | revoked row in `sessions` | Yes (Must/MVP) |
| MFG-01 US-6 View notifications | read/unread and failed-email rows in `notifications` | Yes (Must/MVP) |
| MFG-02 US-1 View profile | active verified rows in `users` | Yes (Should) |
| MFG-02 US-2 Manage profile | versioned/updated rows in `users` and email-change token row | Yes (Should) |
| MFG-02 US-3 Edit profile | `users.version` and `updated_at` rows | Yes (Should) |
| MFG-02 US-4 Change password | `users`, current/revoked `sessions` | Yes (Should) |
| MFG-03 US-1 Add staff | `users`, `staff_accounts`, `staff_invitations` | Yes (Could) |
| MFG-03 US-2 Update staff | Active/Suspended/Invited rows in `staff_accounts` | Yes (Could) |
| MFG-03 US-3 Deactivate/delete staff | Suspended row plus retained assignment/history records | Yes (Could) |
| MFG-03 US-4 Manage staff | role/lifecycle variants in `staff_accounts` | Yes (Could) |
| MFG-04 US-1 View catalogue | Published `products`, versions, images, options, sizes, colors, materials and tiers | Yes (Must) |
| MFG-04 US-2 Search products | Published products and `search_synonym_sets` | Yes (Should) |
| MFG-04 US-3 Add product | Draft row in `products` with normalized child data | Yes (Should) |
| MFG-04 US-4 Update product | immutable `product_versions` structure and version fields | Yes (Should) |
| MFG-04 US-5 Delete product | Draft and Archived lifecycle evidence in catalogue schema; no unsupported historical hard-delete row | Yes (Should) |
| MFG-04 US-6 Publish/unpublish | Published, Hidden and Draft rows in `products` | Yes (Should) |
| MFG-04 US-7 Manage catalogue | complete normalized catalogue dataset | Yes (Should) |
| MFG-04 US-8 Everyday keyword search | exact synonym examples and searchable product labels | Yes (Should) |
| MFG-04 US-9 AI Compare | six products across two branches, five material profiles and supported print data | Yes for data prerequisites (Should); provider runtime not simulated |
| MFG-04 US-10 Product advisory | same grounded Product/MaterialProfile/PrintMethod facts | Yes for data prerequisites (Should); provider runtime not simulated |
| MFG-05 US-1 Design product | Saved `designs`, immutable versions and placements | Yes (Must) |
| MFG-05 US-2 Product customization | product rules, assets, placements and versions | Yes (Must) |
| MFG-05 US-3 View saved design | Saved/Delivered/ProofDelivered/Draft rows | Yes (Must) |
| MFG-05 US-4 Request design service | DesignRequest lifecycle states from Submitted through terminal states | Yes (Could) |
| MFG-05 US-5 Send design to customer | shared versions, feedback, replies and approvals | Yes (Could) |
| MFG-05 US-6 Remove background | original/processed Asset metadata and placement preservation fields | Yes for data prerequisites (Should); transient processing is intentionally not seeded |
| MFG-05 US-7 Preview supported angles | Front/Back `product_mockup_templates` | Yes (Should) |
| MFG-05 US-8 Virtual try-on | valid design/product/assets exist | Yes for data prerequisites (Should); personal photos/jobs are intentionally session-only |
| MFG-06 US-1 Create order/digital approval | Quote, size quantities, Order, cycle and timeline rows | Yes (Must) |
| MFG-06 US-2 Physical sample | all sample states including RevisionRequested and Approved | Yes (Must) |
| MFG-06 US-3 Contract/deposit | Ready/Signed contracts and succeeded DEPOSIT transactions | Yes (Must) |
| MFG-06 US-4 Delivery/balance/completion | Shipped, DeliveredAwaitingBalance and Completed Orders with evidence and BALANCE | Yes (Must) |
| MFG-06 US-5 Reconcile/refund | Pending/Succeeded/Failed/Expired payments and limited full-system refund records | Yes (Should reconciliation / Could refund); Must/MVP manual-refund behavior is not replaced |
| MFG-07 US-1 Track order | every canonical Order status and append-only timeline | Yes (Must) |
| MFG-07 US-2 Cancel order | Cancelled Order and cancellation timeline evidence; no cancellation table | Yes (Must/MVP pre-deposit cancellation; Could full cancellation) |
| MFG-07 US-3 Update order status | canonical state/timeline examples | Yes (Must) |
| MFG-08 US-1 Assign/reassign Sales | active/history `customer_assignments` | Yes (Could) |
| MFG-08 US-2 Work Sales Pipeline | all principal open/closed-lost pipeline states | Yes (Could) |
| MFG-08 US-3 CRM context/notes/reviews | scoped designs, interactions, notes and review outcomes | Yes (Could) |
| MFG-09 US-1 Manage/generate contracts | template statuses and Contract Draft/Ready/Signed/Superseded/Voided | Yes (Must/Could) |
| MFG-09 US-2 Review/sign contract | `signature_evidence` bound to Signed contracts | Yes (Must) |
| MFG-09 US-3 Update/notify contract | Superseded/Voided/Ready rows plus outbox events | Yes (Could) |
| MFG-10 US-1 Choose production terms | standard/flexible rows in `flexible_preferences` | Yes (Could) |
| MFG-10 US-2 Prioritize scheduled production | ScheduledOpen batches and memberships | Yes (Could) |
| MFG-10 US-2a Calculate calendar/capacity | readiness calendar and unique active capacity profiles | Yes (Could) |
| MFG-10 US-3 Group/fallback | shared batches plus individual Approved/Started/Completed plans | Yes (Could) |
| MFG-11 US-1 Business overview | validated events and Overview results | Yes (Should) |
| MFG-11 US-2 Export result | Queued/Running/Succeeded/Failed export jobs | Yes (Could) |
| MFG-11 US-3 Funnel/waiting states | ProductEntry, JourneyIntent, milestone events and Funnel results | Yes (Could) |
| MFG-11 US-4 Prompt analysis | protected AnalyticsResult facts exist | Yes for data prerequisites (Could); page-memory conversation is intentionally not persisted |
| MFG-12 US-1 Monitor logs | INFO/WARN/ERROR redacted audit rows | Yes (Won't) |
| MFG-12 US-2 Backup/restore | successful/failed/running backups and restore journals | Yes (Won't), with row-count exception below |
| MFG-12 US-3 Configure system | three immutable configuration versions | Yes (Won't), with row-count exception below |

## Seed quantity exceptions

These exceptions avoid inventing unsupported business data merely to reach five rows.

| Table | Rows | Reason and evidence |
|---|---:|---|
| `search_synonym_sets.csv` | 1 | The spec defines one versioned mapping but leaves ownership/storage to Plan (`spec-MFG-04.md §10 Q3`); extra releases would invent change history. |
| `print_methods.csv` | 2 | Direct print is specified in `spec-MFG-04.md §9`; embroidery is explicitly referenced as separate decoration in MFG-10. No additional named methods are invented. |
| `customer_provided_confirmations.csv` | 4 | Only unchanged Customer-provided imports may receive this evidence (`spec-MFG-05.md §5.4`); Dony-created/changed versions are deliberately excluded. |
| `refund_records.csv` | 3 | Refund is Could/full-system behavior; MVP BR-019 uses `manual_refund_required` and explicitly creates no provider refund request. |
| `system_configs.csv` | 3 | MFG-12 is Won't and configuration versions must represent actual approved changes; extra versions would invent a change history. |
| `restore_journals.csv` | 3 | MFG-12 is Won't and restore operations are exceptional; the rows cover Succeeded, Failed and Running without inventing more operations. |

## Integrity-check results

- Generator: `data/seed/generate_seed.py`
- Regeneration command: `uv run data/seed/generate_seed.py`
- Output: 66 CSV files, 589 rows, UTF-8, LF, header row, deterministic UUIDs and sorted primary keys.
- Passed: all checked foreign keys; unique normalized email; unique SKU; unique immutable order number; unique active production type/material profile; one design-fee-bearing first Order; every Order total formula; Cancelled/Completed coverage; verified Customer empty state.

## Files produced

| File | Step | Status |
|---|---|---|
| `data/01-entity-dictionary.md` | S1 | Complete |
| `data/02-crud-matrix.md` | S2 | Complete |
| `data/03-erd.mmd` | S3 | Complete; Mermaid only |
| `data/04-data-model.md` | S4 | Complete; conceptual ERD embedded unchanged |
| `data/data-model-MFG-01.md` through `data/data-model-MFG-12.md` | S7 | Module ownership indexes generated from the canonical whole-system model |
| `data/schema/schema-MFG-01.sql` through `data/schema/schema-MFG-12.sql` | S7 | SQLite validation schema; all foreign keys are deferrable and validated at seed-load commit |
| `data/schema/load_seed.py` | S7 | Creates the schema and imports numerically ordered CSV files in filename order |
| `data/seed/generate_seed.py` | S5 | Complete; version-controlled deterministic generator |
| `data/seed/*.csv` (66 files) | S5/S7 | Complete; generated, version-controlled, and numerically ordered for deterministic SQLite loading |
| `data/05-review.md` | S6 | Complete |
| `.gitignore` | S5 | Generator-only ignore rule added |

