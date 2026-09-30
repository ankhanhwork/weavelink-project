# Seed Edge Case Register

This register records the edge-case evidence required for the Session 7 seed review. It does not replace the canonical entity definitions in `data/04-data-model.md` or the deterministic assertions in `data/seed/generate_seed.py`. The generator validates the in-memory package before it writes any CSV file.

## Current verified evidence

| Requirement | Seed evidence | Automated check | Checked by |
|---|---|---|---|
| Referential integrity | All 66 numerically ordered CSV files | `generate_seed.py` checks every declared FK before writing; SQLite checks the same references at commit. | Đinh An Khánh |
| Deterministic regeneration | All 66 generated CSV files | Fixed UUID namespace, timestamps, seed order and sorted PKs; generation succeeds before files are written. | Đinh An Khánh |
| Unique identity and business keys | `09_users.csv`, `07_products.csv`, `61_orders.csv` | Unique normalized email, SKU, and immutable order-number assertions; the validation schema also has matching unique constraints. | Đinh An Khánh |
| Order money formula | `61_orders.csv` | Every row satisfies merchandise subtotal minus discount plus shipping plus tax plus design fee equals total. | Đinh An Khánh |
| Lifecycle edge cases | Product, staff, design request/version, contract, payment and order CSVs | The generator asserts required lifecycle values, including Archived Product, Deleted StaffAccount, Approved/Assigned DesignRequest and Superseded DesignVersion. | Đinh An Khánh |
| Empty state | `09_users.csv` | A verified Customer with no Design, DesignRequest, Consultation, or Order is asserted. | Đinh An Khánh |
| Date boundary/order | `09_users.csv`, `61_orders.csv`, `64_payment_transactions.csv`, `16_one_time_tokens.csv` | Created timestamps do not exceed updated or paid timestamps; verification/email-change/reset/invitation TTLs are asserted against their specification durations. | Đinh An Khánh |
| Data privacy | `09_users.csv`, `02_assets.csv`, all provider and token fields | Reserved email domain, synthetic asset namespace, synthetic hashes/references and no personal TryOn fixture are asserted or structurally documented. | Đinh An Khánh |

## Enumerated-value and boundary coverage

The rows below record currently verified enum and boundary coverage. Each filename is loaded deterministically and its first column is the primary key. Group B must add a separate row if a later requirement introduces a new enum value, boundary, or business rule.

| Source rule or enumerated field | CSV filename | Primary-key value | Boundary or expected outcome | Checked by |
|---|---|---|---|---|
| Asset ownership, MIME type, and scan status | `02_assets.csv` | All `asset_id` rows | Covers `Dony`/`User`, `PDF`/`PNG`, and `Safe`/`Rejected`. | Đinh An Khánh |
| Product and contract-template lifecycle status | `07_products.csv`; `03_contract_templates.csv` | All `product_id` and `contract_template_id` rows | Covers Product `Draft`/`Hidden`/`Published`/`Archived` and ContractTemplate `Draft`/`Published`/`Archived`. | Đinh An Khánh |
| Staff role and account lifecycle | `20_staff_accounts.csv`; `34_staff_invitations.csv` | All `staff_account_id` and `invitation_id` rows | Covers `Sales`, `SalesAdmin`, `SystemAdmin`; account `Active`, `Invited`, `Suspended`, `Deleted`; invitation delivery `Delivered` and `Failed`. | Đinh An Khánh |
| One-time-token purpose and duration | `16_one_time_tokens.csv` | All `token_id` rows | Covers EmailVerification 24h, PasswordReset 30m, EmailChange 24h and StaffInvitation 48h. | Đinh An Khánh |
| Catalogue branch and printable side | `18_product_versions.csv`; `25_print_areas.csv` | All `product_version_id` and `print_area_id` rows | Covers both garment branches and `Front`/`Back` placement. | Đinh An Khánh |
| Design request and version lifecycle | `50_design_requests.csv`; `51_designs.csv`; `52_design_versions.csv` | All design request, design, and design-version IDs | Covers request `Submitted`/`UnderReview`/`FeeProposed`/`Approved`/`Assigned`/`InProgress`/`Delivered`/`Cancelled`/`Rejected` and version `Draft`/`SharedForReview`/`Approved`/`Superseded`. | Đinh An Khánh |
| Contract and payment lifecycle | `40_contracts.csv`; `64_payment_transactions.csv`; `66_refund_records.csv` | All contract, payment, and refund IDs | Covers contract lifecycle, both `DEPOSIT`/`BALANCE` purposes, payment `Pending`/`Succeeded`/`Failed`/`Expired`, and refund states. | Đinh An Khánh |
| Order lifecycle | `61_orders.csv`; `63_order_timeline_events.csv` | All `order_id` and `event_id` rows | Covers active lifecycle states plus `Cancelled` and `Completed`; timeline records include Customer and Staff actors. | Đinh An Khánh |
| Production sample and batch lifecycle | `60_production_samples.csv`; `37_production_batches.csv`; `58_individual_production_plans.csv` | All sample, batch, and individual-plan IDs | Covers sample, batch, and fallback-plan states, including revision and locked/in-production cases. | Đinh An Khánh |
| Analytics and export state | `14_export_requests.csv`; `38_analytics_events.csv` | All export-request and analytics-event IDs | Covers `CSV`/`XLSX`, all supported datasets, queued/running/succeeded/failed exports, and both analytics source kinds. | Đinh An Khánh |
| Audit, backup, and restore outcome | `10_audit_events.csv`; `11_backups.csv`; `33_restore_journals.csv` | All audit-event, backup, and restore-journal IDs | Covers `INFO`/`WARN`/`ERROR`, succeeded/failed outcomes, and backup/restore `Succeeded`/`Failed`/`Running`. | Đinh An Khánh |
| Numeric and date boundaries | `18_product_versions.csv`; `25_print_areas.csv`; `55_quotes.csv`; `61_orders.csv`; `64_payment_transactions.csv` | All rows in the cited files | Covers MOQ 10, capacity 10,000, positive placement dimensions, text phone values retaining a leading zero, order-money reconciliation, payment expiry and timestamp ordering. | Đinh An Khánh |

## Data-rule fixture coverage

The rows below cover business rules that create, constrain or prohibit persisted data. Rules that only regulate a live request, authorization response, provider call, scheduler or UI behavior remain in the module spec and are followed through `data/07-end-to-end-traceability.md`; this package does not invent a fake persisted record for a session-only or external action.

| Source rule(s) | Seed evidence | Generator assertion or review outcome |
|---|---|---|
| MFG-01 BR-001 | `09_users.csv` | Normalized email is unique and uses the synthetic `example.invalid` domain. |
| MFG-01 BR-004, BR-007 | `19_sessions.csv`; `16_one_time_tokens.csv` | Session timestamps and token TTL are checked; password reset lasts exactly 30 minutes. |
| MFG-01 BR-005–006 | `16_one_time_tokens.csv`; UUID/version fields across CSVs | Token purpose/hash fixtures and deterministic UUID/version values are generated before write. |
| MFG-02 BR-002–BR-004 | `09_users.csv`; `16_one_time_tokens.csv`; `05_outbox_events.csv` | Email-change token lasts 24 hours; user/session/notification prerequisites are present. |
| MFG-03 BR-002–BR-003, BR-006 | `20_staff_accounts.csv`; `34_staff_invitations.csv` | Staff lifecycle includes Deleted; invitation fixture uses a 48-hour token. |
| MFG-04 BR-001–BR-003, BR-005 | `07_products.csv`; `18_product_versions.csv`; catalogue children | SKU uniqueness, complete lifecycle fixtures, versions and required product-child prerequisites are present. |
| MFG-04 BR-002, BR-008 | `18_product_versions.csv`; `36_volume_pricing_tiers.csv`; `55_quotes.csv` | MOQ/capacity/tier boundaries and integer-VND quote/order arithmetic are checked. |
| MFG-05 BR-001–BR-005, BR-007 | `50_design_requests.csv`; `51_designs.csv`; `52_design_versions.csv`; approval/feedback tables | Request and design lifecycles, exact fee states, immutable version history and evidence rows are represented. |
| MFG-05 BR-010–BR-012 | `02_assets.csv`; `29_product_mockup_templates.csv` | Synthetic safe design assets/templates are present; personal TryOn photo/result is intentionally absent. |
| MFG-06 BR-001–BR-005, BR-012 | `55_quotes.csv` through `64_payment_transactions.csv` | Order lifecycle, immutable quote/order data, one pending attempt per order/purpose and every order-money formula are asserted. |
| MFG-06 BR-008–BR-010, BR-015–BR-019 | `59_order_quote_cycles.csv`; `60_production_samples.csv`; `63_order_timeline_events.csv`; `05_outbox_events.csv` | Revision cycles, sample states, timeline records and notification prerequisites are represented without replacing MVP limits. |
| MFG-07 BR-001–BR-005 | `61_orders.csv`; `63_order_timeline_events.csv`; `13_customer_assignments.csv` | Cancellation/completion states, actor timeline evidence and Sales assignment scope prerequisites are represented. |
| MFG-08 BR-001–BR-011 | `13_customer_assignments.csv`; `12_consultations.csv`; `22_admin_reviews.csv` through `54_interaction_logs.csv` | Active assignment uniqueness, stage history, scoped design, interaction/note/review fixtures are present. |
| MFG-09 BR-001–BR-005 | `03_contract_templates.csv`; `40_contracts.csv`; `41_signature_evidence.csv` | Template/contract state variants, immutable signed evidence and sample-bound contract fixtures are present. |
| MFG-10 BR-001–BR-010 | `56_flexible_preferences.csv`; `65_production_readiness.csv`; batch/plan tables | Flexible policy/incentive, readiness, capacity, batch, membership and individual-plan fixtures are present. |
| MFG-11 BR-001–BR-011 | `01_analytics_results.csv`; `17_product_entries.csv`; `24_journey_intents.csv`; `38_analytics_events.csv`; `14_export_requests.csv` | Result metadata, linked evidence and export lifecycle are available; no fabricated persistent AI conversation exists. |
| MFG-12 BR-001–BR-006 | `10_audit_events.csv`; `11_backups.csv`; `21_system_configs.csv`; `33_restore_journals.csv`; `05_outbox_events.csv` | Redacted audit states, backup/restore outcomes, secret references and ConfigChanged notice fixture are present. |

## Regeneration proof

- Generator: `data/seed/generate_seed.py`
- Deterministic basis: fixed UUID namespace, fixed timestamps, sorted primary keys and `seed-order.json`; no pseudorandom input is used.
- Regeneration command: `uv run data/seed/generate_seed.py`
- Expected output: 66 CSV files and 597 rows; validation runs before write and reports every assertion as `PASS`.
- Load command: `uv run data/schema/load_seed.py --database data/schema/weavelink-midterm.db`
- Cross-artifact command: `uv run data/tools/check_data_package.py` and `uv run data/tools/check_end_to_end_traceability.py`
