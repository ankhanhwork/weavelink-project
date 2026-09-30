# Seed Edge Case Register

This register records the edge-case evidence required for the Session 7 seed review. It does not replace the canonical entity definitions in `data/04-data-model.md` or the deterministic assertions in `data/seed/generate_seed.py`.

## Current verified evidence

| Requirement | Seed evidence | Automated check | Checked by |
|---|---|---|---|
| Referential integrity | All 66 numerically ordered CSV files | `generate_seed.py` checks every declared FK; SQLite checks the same references at commit. | Đinh An Khánh |
| Unique identity and business keys | `09_users.csv`, `07_products.csv`, `61_orders.csv` | Unique normalized email, SKU, and immutable order-number assertions. | Đinh An Khánh |
| Order money formula | `61_orders.csv` | Every row satisfies merchandise subtotal minus discount plus shipping plus tax plus design fee equals total. | Đinh An Khánh |
| Status edge cases | `61_orders.csv` | At least one `Cancelled` Order and one `Completed` Order are asserted. | Đinh An Khánh |
| Empty state | `09_users.csv` | A verified Customer with no Design, DesignRequest, Consultation, or Order is asserted. | Đinh An Khánh |
| Date boundary/order | `09_users.csv`, `61_orders.csv`, `64_payment_transactions.csv` | Created timestamps do not exceed updated or paid timestamps. | Đinh An Khánh |

## Required completion before submission

The rows below record currently verified enum and boundary coverage. Each filename is loaded deterministically and its first column is the primary key. Group B must add a separate row if a later requirement introduces a new enum value, boundary, or business rule.

| Source rule or enumerated field | CSV filename | Primary-key value | Boundary or expected outcome | Checked by |
|---|---|---|---|---|
| Asset ownership, MIME type, and scan status | `02_assets.csv` | All `asset_id` rows | Covers `Dony`/`User`, `PDF`/`PNG`, and `Safe`/`Rejected`. | Đinh An Khánh |
| Product and contract-template lifecycle status | `07_products.csv`; `03_contract_templates.csv` | All `product_id` and `contract_template_id` rows | Covers product `Draft`/`Hidden`/`Published` and template `Draft`/`Published`/`Archived`. | Đinh An Khánh |
| Staff role and account lifecycle | `20_staff_accounts.csv`; `34_staff_invitations.csv` | All `staff_account_id` and `invitation_id` rows | Covers `Sales`, `SalesAdmin`, `SystemAdmin`; account `Active`, `Invited`, `Suspended`; invitation delivery `Delivered` and `Failed`. | Đinh An Khánh |
| One-time-token purpose | `16_one_time_tokens.csv` | All `token_id` rows | Covers `EmailVerification`, `PasswordReset`, `EmailChange`, and `StaffInvitation`. | Đinh An Khánh |
| Catalogue branch and printable side | `18_product_versions.csv`; `25_print_areas.csv` | All `product_version_id` and `print_area_id` rows | Covers both garment branches and `Front`/`Back` placement. | Đinh An Khánh |
| Design lifecycle and review state | `50_design_requests.csv`; `51_designs.csv`; `52_design_versions.csv` | All design request, design, and design-version IDs | Covers every seeded request state, design status, design source, and review state. | Đinh An Khánh |
| Contract and payment lifecycle | `40_contracts.csv`; `64_payment_transactions.csv`; `66_refund_records.csv` | All contract, payment, and refund IDs | Covers contract lifecycle, both `DEPOSIT`/`BALANCE` purposes, payment `Pending`/`Succeeded`/`Failed`/`Expired`, and refund states. | Đinh An Khánh |
| Order lifecycle | `61_orders.csv`; `63_order_timeline_events.csv` | All `order_id` and `event_id` rows | Covers active lifecycle states plus `Cancelled` and `Completed`; timeline records include Customer and Staff actors. | Đinh An Khánh |
| Production sample and batch lifecycle | `60_production_samples.csv`; `37_production_batches.csv`; `58_individual_production_plans.csv` | All sample, batch, and individual-plan IDs | Covers sample, batch, and fallback-plan states, including revision and locked/in-production cases. | Đinh An Khánh |
| Analytics and export state | `14_export_requests.csv`; `38_analytics_events.csv` | All export-request and analytics-event IDs | Covers `CSV`/`XLSX`, all supported datasets, queued/running/succeeded/failed exports, and both analytics source kinds. | Đinh An Khánh |
| Audit, backup, and restore outcome | `10_audit_events.csv`; `11_backups.csv`; `33_restore_journals.csv` | All audit-event, backup, and restore-journal IDs | Covers `INFO`/`WARN`/`ERROR`, succeeded/failed outcomes, and backup/restore `Succeeded`/`Failed`/`Running`. | Đinh An Khánh |
| Numeric and date boundaries | `18_product_versions.csv`; `25_print_areas.csv`; `61_orders.csv`; `64_payment_transactions.csv` | All rows in the cited files | Covers MOQ/capacity, positive placement dimensions, order-money reconciliation, and timestamp ordering. | Đinh An Khánh |

