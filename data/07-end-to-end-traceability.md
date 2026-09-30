---
artifact: End-to-end Traceability
step: S7
generated: 2026-09-30
sources: docs/prd.md; docs/spec/specs/spec-MFG-01.md through spec-MFG-12.md; docs/spec/screens/; data/04-data-model.md; data/seed/*.csv
---

# WeaveLink End-to-End Traceability

## 1. Purpose and review method

This derived index lets a reviewer follow an approved requirement without guessing names or ownership:

```text
PRD item → module FR → §5.1 field contract → persisted entity/attribute → seed CSV + primary key → screen acceptance scenario
```

The PRD and module specifications remain the source of truth. A row below never adds a requirement. `Session-only` means the specification expressly prohibits a persistent seed output; the cited synthetic prerequisite is the review fixture instead.

Run the following before review:

```powershell
uv run data/seed/generate_seed.py
uv run data/tools/check_data_package.py
uv run data/tools/check_end_to_end_traceability.py
uv run data/schema/load_seed.py --database data/schema/weavelink-midterm.db
git status --short
```

## 2. Traceability index

| PRD scope | Exact FR IDs | Contract fields to follow | Entity / attributes | Seed evidence | Screen evidence |
|---|---|---|---|---|---|
| M-1, M-2 | MFG-01 FR-001 | route/session context | No write; registration/login view model | `09_users.csv` user `c381a9bb-d175-5a06-be64-7d91163c76c8` is a synthetic verified Customer | S04, S05, S08 |
| M-1 | MFG-01 FR-002–003 | full_name, email, password, confirmation; server user/resend email | `users.email/full_name/password_hash`; `one_time_tokens`; `outbox_events` | `09_users.csv`, `16_one_time_tokens.csv`, `05_outbox_events.csv` event `VerificationQueued` | S04 acceptance scenarios 1–3 |
| M-1, M-2 | MFG-01 FR-004–006 | route/session; email/password/redirect; secure session | `sessions.user_id/token_hash/expiry/revoked_at`; active `staff_accounts` is role authority | `19_sessions.csv` session `3b2b6950-a738-5df7-a36d-f1fbd7a34b3c` | S05, S08 |
| M-1, M-2 | MFG-01 FR-007–011 | email; token; new_password/confirmation | `one_time_tokens.purpose/token_hash/expires_at/consumed_at`; `sessions.revoked_at` | `16_one_time_tokens.csv` reset token `0293f65b-ca19-5925-a366-d3062541af68` has 30-minute TTL | S06, S07, S09, S10 |
| M-11 | MFG-01 FR-012–013 | session/page/page_size/unread_only; notification_id | `notifications.recipient_user_id/source_event_id/read_at`; `outbox_events` | `15_notifications.csv` joins each `source_event_id` to `05_outbox_events.csv` | S13 acceptance scenarios 1–4 |
| SH-7 | MFG-02 FR-001–003 | session; full_name/pending_email/current_password/expected_version | MFG-01-owned `users`; `one_time_tokens` for verified email change | `09_users.csv` and `16_one_time_tokens.csv` `EmailChange` fixture | S11 |
| SH-7 | MFG-02 FR-004–005 | session; old_password/new_password/confirmation/expected_version | MFG-01-owned `users.password_hash/version`, `sessions.revoked_at` | `09_users.csv`, `19_sessions.csv` | S12 |
| C-5 | MFG-03 FR-001–002 | list filters; System Admin session | `staff_accounts.user_id/role/status/version` | `20_staff_accounts.csv` covers Active, Invited, Suspended and Deleted | S48 |
| C-5 | MFG-03 FR-003–004 | staff_account_id/email/role; idempotency key | `staff_invitations.staff_account_id/email_snapshot/role_snapshot/token_hash/expires_at` | `34_staff_invitations.csv` | S48, S08 |
| C-5 | MFG-03 FR-005–008 | staff_account_id; expected_version; confirmation; idempotency key | `staff_accounts`; MFG-01 `sessions`; `audit_events` | `20_staff_accounts.csv`, `10_audit_events.csv` | S48 |
| M-3 | MFG-04 FR-001–003 | category/page/sort; product UUID; keyword/filters | `products`; `product_versions`; catalogue children | `07_products.csv` Published SKU `DEMO-SHIRT-003`, linked `18_product_versions.csv` row `43f4d619-a3f7-593c-b4a6-44ab4449e96a` | S01, S14, S15 |
| SH-6 | MFG-04 FR-012–017 | q/scope/limit; product/version/status | `search_synonym_sets`; current `products` and `product_versions` | `08_search_synonym_sets.csv`; Published/Hidden/Draft/Archived rows in `07_products.csv` | S14 |
| SH-1, SH-2 | MFG-04 FR-018–025 | product IDs/branch; question/catalogue context | `products.branch`; `material_profiles`; `print_methods`; transient chat context | `07_products.csv`, `04_material_profiles.csv`, `06_print_methods.csv`; no persisted chat row by design | S14, S15 |
| SH-8, C-1 | MFG-04 FR-004–011 | Sales Admin session; product fields/version/confirmation | `products` plus all versioned catalogue children | `07_products.csv` and `18_product_versions.csv` through `36_volume_pricing_tiers.csv` | S16, S17, S18, S19 |
| M-4 | MFG-05 FR-001–003 | product/design/options/assets; version/idempotency | `designs`; `design_versions`; `design_placements`; `assets` | `51_designs.csv`, `52_design_versions.csv`, `48_design_placements.csv` | S20 |
| M-5 | MFG-05 FR-004 | page/filter/sort/tab/request/session | `designs.status/current_version`; `design_requests` only for Could tab | `51_designs.csv` Saved fixtures | S25 |
| C-2 | MFG-05 FR-005–009 | product/request/attachment/deadline; assessment action; committed event; queue filters | `design_requests`; `design_request_assets`; MFG-01 `outbox_events/notifications` | `50_design_requests.csv` covers Submitted through Rejected, including Approved and Assigned | S24, S26, S27, S28 |
| C-2 | MFG-05 FR-010–013, FR-017–018, FR-021 | design/request/version; feedback/reply/approval action fields | `design_versions`; `design_feedback`; `staff_replies`; `customer_approvals`; outbox/notification | `42_customer_approvals.csv` approval `060ff8b6-528f-5312-91df-a511ae622b7b`; `44_design_feedback.csv`; `46_staff_replies.csv` | S26, S29, S13 |
| SH-4 | MFG-05 FR-014 | selected asset/mode/tolerance/draft revision | Session-only image review; persisted Asset only after explicit design save | `02_assets.csv` scanned synthetic Asset fixture; no processed result row before save | S21 |
| SH-5 | MFG-05 FR-015 | product/template/options/placements/view/revision | `product_mockup_templates`; `design_placements`; `assets` | `29_product_mockup_templates.csv` Front fixture `2c5e5de0-52b3-5c14-bf6c-2471f833eb47` | S22 |
| SH-3 | MFG-05 FR-016 | person image, explicit consent, design revision, session/job token | Session-only TryOn job; existing design and synthetic Dony template are prerequisites | `52_design_versions.csv` Approved design version `6f032fe3-c433-5c99-a779-acd81fe5597d`; `29_product_mockup_templates.csv` Front fixture and safe PNG Asset `0541bf62-6d82-5a44-afa7-b5a30b241285` | S23 acceptance scenarios 1–6 |
| C-2 | MFG-05 FR-019–020 | source/channel evidence; exact unchanged imported version | `designs`; `design_versions`; `customer_provided_confirmations` | `43_customer_provided_confirmations.csv` | S26, S29 |
| M-6 | MFG-06 FR-001–002 | session/product/design; quantities/address/buyer details/current versions | `quotes`; `quote_size_quantities`; immutable quote snapshots | `55_quotes.csv` quote `39f19a47-1f41-5b4e-881f-7d998497a268`; `57_quote_size_quantities.csv` | S30, S33 |
| M-6, M-7 | MFG-06 FR-003 | action/order_id/quote_id/evidence/tracking/expected_version | `orders`; `order_quote_cycles`; `production_samples`; `order_timeline_events` | `61_orders.csv` `SO-2026-0001`; `59_order_quote_cycles.csv` `0aef4881-a577-5ac6-9562-71f7382b7862` | S30, S33, S35, S37 |
| M-10 | MFG-06 FR-004–005 | order_id/purpose/versions/key; verified provider request | `payment_transactions`; `refund_records`; order payment fields | `64_payment_transactions.csv` DEPOSIT success `12b32ad6-cac8-523f-a0a8-b3bccd8797f3`; `66_refund_records.csv` | S40, S41, S42 |
| M-6, M-7, M-10 | MFG-06 FR-006 | order_id or attempt_id; session | `orders`; timeline; payment/refund summary | `61_orders.csv`, `63_order_timeline_events.csv`, `64_payment_transactions.csv` | S33, S35, S37, S40 |
| M-7 | MFG-07 FR-001–002 | paging/filter/order_id/session | MFG-06-owned `orders`, `order_timeline_events`, contract/payment summaries | `61_orders.csv`; `63_order_timeline_events.csv` | S34, S35 |
| M-7 | MFG-07 FR-003–004 | order_id/reason/version/key; committed cancellation event | MFG-06 `orders`/timeline; MFG-01 outbox/notification | `61_orders.csv` Cancelled fixture; `05_outbox_events.csv` `OrderCancelled` | S35, S13 |
| M-8 | MFG-07 FR-005–007 | role-scoped filters; lifecycle event/evidence/version/key; committed event | MFG-06 `orders`/timeline; MFG-01 outbox/notification; MFG-08 assignment scope | `13_customer_assignments.csv`; `63_order_timeline_events.csv` InProduction event `64054d03-d85a-5ae9-aaea-98c6270e2e27` | S36, S37, S13 |
| C-3 | MFG-08 FR-001–003 | model/filter; consultation_id; sales_user_id/version/key | `consultations`; `customer_assignments`; `stage_histories` | active assignment `5c70bca2-0f56-5d03-8331-becf7cf70e16`; consultation `05f596ea-a8cd-5f6b-b3a1-b066124c1f44` | S27, S28 |
| C-3 | MFG-08 FR-004–008 | committed event; lead/activity filters; pipeline/note/review/scope action fields | MFG-01 outbox/notification; `interaction_logs`, `internal_notes`, `admin_reviews`, `lead_design_links` | `54_interaction_logs.csv`, `23_internal_notes.csv`, `22_admin_reviews.csv`, `53_lead_design_links.csv` | S27, S28, S29, S13 |
| M-9 | MFG-09 FR-001–004 | order/sample/template/version; draft/hash/idempotency | `contract_templates`; `contracts`; Asset PDF reference | Published template `c7e0e3b8-0302-5aea-8b34-242301cb91f7`; Signed contract `37313421-0467-5ebc-ab1f-7f8f91414a4f` | S39 |
| M-9 | MFG-09 FR-005, FR-007, FR-009 | committed Ready/signed event; versioned replacement | MFG-01 outbox/notification; `contracts.status` | `40_contracts.csv` Ready/Superseded/Signed fixtures; `05_outbox_events.csv` `ContractReady` | S38, S39, S13 |
| M-9 | MFG-09 FR-008 | contract ID/version/hash; consent/typed name/session | `signature_evidence.contract_id/signer_user_id` | `41_signature_evidence.csv` bound to a Signed contract | S38 |
| C-4 | MFG-09 FR-006 | template filter/name/content/version | `contract_templates` | `03_contract_templates.csv` Draft/Published/Archived versions | S43, S44, S45 |
| C-8 | MFG-10 FR-001–003 | quote/policy/merge_opt_in/expected_version | `quotes.merge_opt_in/policy_version`; `flexible_preferences` | `56_flexible_preferences.csv` `206e4b10-3f5e-5a39-b40c-0d503e920cfb` joins quote `57a7618c-e870-5951-9445-735228c79ebe`; incentive is 95,000 VND | S31, S32, S33 |
| C-8 | MFG-10 FR-004–006 | Admin session/filter/capacity; batch/order action/version/key | `production_readiness`; `production_capacity_profiles`; `production_batches`; `batch_memberships`; `individual_production_plans` | `65_production_readiness.csv`, `32_production_capacity_profiles.csv`, `37_production_batches.csv`, `39_batch_memberships.csv` | S46 |
| C-8 | MFG-10 FR-007 | committed schedule/membership/start/fallback/completion event | MFG-01-owned outbox/notification, MFG-10 source data | Fixture prerequisites in `37_production_batches.csv` and `39_batch_memberships.csv`; notification emission is verified as an implementation event, not fabricated customer data | S13, S35, S37 |
| SH-11 | MFG-11 FR-001–002 | date/filter/metric/page/session | `analytics_events`; immutable `analytics_results` metadata | `01_analytics_results.csv` result `026ff87b-7760-51b6-8488-d1765e17883d`; `38_analytics_events.csv` | S47 |
| C-7 | MFG-11 FR-003 | dataset/format/result/key/export ID | `export_requests.analytics_result_id/state/private_asset_id` | succeeded export `650333ab-2173-59a7-aa61-5c25d62e5a62` | S47 |
| C-7 | MFG-11 FR-004–005 | unit/template/cutoff/context; prompt/result ID | `product_entries`; `journey_intents`; `analytics_events`; transient AI answer | `38_analytics_events.csv` event `04cfcafc-1767-50c4-a6bf-a79d6c3b21d9`; no persistent conversation by design | S47 |
| Won't | MFG-12 FR-001–005 | audit filters; backup/restore/reauth/version/key | `audit_events`; `backups`; `restore_journals` | ERROR audit `c83e1fea-427f-5a0c-8c1b-869c00b50afd`; `11_backups.csv`; `33_restore_journals.csv` | S49, S50 |
| Won't | MFG-12 FR-006–007 | System Admin session; typed patch/version/reauth | `system_configs.version`, secret references, audit record | config `42545ff6-cdea-56b8-a291-081cae23b116`, version 1 | S49 |
| Won't | MFG-12 FR-008 | committed change log | `system_configs` → MFG-01-owned `outbox_events` → `notifications` | config ID `42545ff6-cdea-56b8-a291-081cae23b116` → outbox `79796306-0951-5218-ac08-def41d8f2523` → notification `fc6f4fe8-f8b8-5d4c-a9ab-e3640912a738` | S49, S13 |

## 3. Three reviewer-ready trace examples

### TR-01 — MFG-12/FR-008: configuration notice

`docs/prd.md` marks system configuration as Won't. `spec-MFG-12.md` FR-008 requires an active-admin notice that names changed keys/version/time but excludes secret values. The I/O contract supplies the committed change log and expects outbox IDs. The data model maps this to `system_configs`, then MFG-01-owned `outbox_events` and `notifications`.

The synthetic trace is exact: SystemConfig `42545ff6-cdea-56b8-a291-081cae23b116` → OutboxEvent `79796306-0951-5218-ac08-def41d8f2523` (`MFG-12`, `ConfigChanged`, payload only `changed_keys`) → Notification `fc6f4fe8-f8b8-5d4c-a9ab-e3640912a738` at `/system/configuration`. Review it in S49 and S13.

### TR-02 — MFG-05/FR-016: virtual try-on stays session-only

`docs/prd.md` SH-3 leads to MFG-05 FR-016. The contract requires a person image, explicit consent, a design revision and a session/job token. The resulting personal image is intentionally absent from the data model and seed because MFG-05 BR-010 prohibits it from entering save/order payloads.

The deterministic input fixture is Approved DesignVersion `6f032fe3-c433-5c99-a779-acd81fe5597d`, plus the Dony Safe PNG Asset `0541bf62-6d82-5a44-afa7-b5a30b241285` and Front ProductMockupTemplate `2c5e5de0-52b3-5c14-bf6c-2471f833eb47`. S23 acceptance scenarios verify consent, session invalidation and no persistence of a person image/result.

### TR-03 — MFG-10/FR-001: flexible production terms

`docs/prd.md` C-8 maps to MFG-10 FR-001. The contract reads an owned quote and policy version. The logical model records `quotes.merge_opt_in/policy_version` and `flexible_preferences.accepted_policy_version/incentive_vnd`; it does not create a production batch at checkout.

Fixture `206e4b10-3f5e-5a39-b40c-0d503e920cfb` links Quote `57a7618c-e870-5951-9445-735228c79ebe` to policy `MFG10-v4` with incentive 95,000 VND. S31 shows the explicit choice and S32 displays the policy; S46 is the later human-planning step.

## 4. Review constraints

- A reviewer may choose any exact FR ID in section 2, follow its matching row, then open the cited source spec for the field-level contract.
- A seed row is evidence of a permitted persistent state, not evidence that application code, provider integration or a live service exists.
- If a feature output is documented as transient or session-only, the trace names its synthetic persisted prerequisite and the screen acceptance scenario instead of inventing a database table.
- Adding a new FR, persisted field, enum value or business rule requires an updated row here, an edge-case register entry and a generator assertion before the submission tag.
