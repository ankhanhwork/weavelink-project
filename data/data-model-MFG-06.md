# Data Model and Mockup Data: MFG-06 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-06. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-06 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `quotes` | Owned by MFG-06; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `quote_size_quantities` | Owned by MFG-06; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `orders` | Owned by MFG-06; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `order_size_quantities` | Owned by MFG-06; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `order_quote_cycles` | Owned by MFG-06; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `production_samples` | Owned by MFG-06; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `payment_transactions` | Owned by MFG-06; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `refund_records` | Owned by MFG-06; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `order_timeline_events` | Owned by MFG-06; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Attribute traceability

| Table | Persisted attributes | Trace source |
|---|---|---|
| `quotes` | `quote_id`, `customer_id`, `journey_intent_id`, `buyer_type`, `buyer_legal_name`, `buyer_tax_id`, `billing_address`, `product_version_id`, `design_version_id`, `recipient_name`, `phone`, `address_line`, `ward`, `province`, `country`, `merchandise_subtotal_vnd`, `merge_discount_vnd`, `shipping_vnd`, `tax_vnd`, `design_fee_vnd`, `total_vnd`, `deposit_preview_vnd`, `merge_opt_in`, `policy_version`, `expires_at`, `version`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-06` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `quote_size_quantities` | `quote_size_quantity_id`, `quote_id`, `size_label`, `quantity` | Canonical table row in `data/04-data-model.md`; owning `MFG-06` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `orders` | `order_id`, `order_number`, `customer_id`, `journey_intent_id`, `buyer_type`, `buyer_legal_name`, `buyer_tax_id`, `billing_address`, `product_name_snapshot`, `sku_snapshot`, `material_snapshot`, `options_snapshot_json`, `product_version_id`, `design_version_id`, `recipient_name`, `phone`, `address_line`, `ward`, `province`, `country`, `merchandise_subtotal_vnd`, `merge_discount_vnd`, `shipping_vnd`, `tax_vnd`, `design_fee_vnd`, `total_vnd`, `status`, `current_quote_cycle`, `approved_sample_id`, `contract_id`, `deposit_percent`, `contract_total_vnd`, `accepted_deposit_vnd`, `accepted_order_credit_vnd`, `balance_due_vnd`, `balance_due_at`, `received_at`, `completed_at`, `received_by_staff_id`, `carrier`, `tracking_number`, `shipped_at`, `estimated_delivery_from`, `estimated_delivery_to`, `delivery_evidence_asset_id`, `delivery_evidence_verified_at`, `manual_refund_required`, `version`, `created_at`, `updated_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-06` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `order_size_quantities` | `order_size_quantity_id`, `order_id`, `size_label`, `quantity` | Canonical table row in `data/04-data-model.md`; owning `MFG-06` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `order_quote_cycles` | `order_quote_cycle_id`, `order_id`, `cycle_number`, `quote_id`, `design_version_id`, `customer_approved_at`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-06` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `production_samples` | `sample_id`, `order_quote_cycle_id`, `design_version_id`, `status`, `carrier`, `tracking_number`, `sent_at`, `estimated_delivery_from`, `estimated_delivery_to`, `received_at`, `approved_at`, `feedback`, `evidence_asset_id`, `version` | Canonical table row in `data/04-data-model.md`; owning `MFG-06` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `payment_transactions` | `payment_transaction_id`, `order_id`, `customer_id`, `purpose`, `amount_vnd`, `currency`, `status`, `provider_reference`, `provider_event_id`, `paid_at`, `refund_status`, `expires_at`, `version`, `idempotency_key`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-06` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `refund_records` | `refund_id`, `payment_transaction_id`, `amount_vnd`, `status`, `provider_reference`, `requested_at`, `settled_at`, `idempotency_key` | Canonical table row in `data/04-data-model.md`; owning `MFG-06` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `order_timeline_events` | `event_id`, `order_id`, `prior_status`, `target_status`, `actor_kind`, `actor_user_id`, `event_source`, `bound_entity_type`, `bound_entity_id`, `bound_entity_version`, `sample_cycle`, `evidence_asset_id`, `idempotency_reference`, `occurred_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-06` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |

## 4. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `design_requests.fee_order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `quotes.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `quote_size_quantities.quote_id` | `quotes.quote_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `quotes.journey_intent_id` | `journey_intents.journey_intent_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `quotes.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `quotes.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_size_quantities.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.journey_intent_id` | `journey_intents.journey_intent_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.approved_sample_id` | `production_samples.sample_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.contract_id` | `contracts.contract_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.received_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.delivery_evidence_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_quote_cycles.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_quote_cycles.quote_id` | `quotes.quote_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_quote_cycles.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_samples.order_quote_cycle_id` | `order_quote_cycles.order_quote_cycle_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_samples.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_samples.evidence_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `payment_transactions.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `payment_transactions.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `refund_records.payment_transaction_id` | `payment_transactions.payment_transaction_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_timeline_events.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_timeline_events.actor_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_timeline_events.evidence_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `contracts.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `contracts.approved_sample_id` | `production_samples.sample_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `flexible_preferences.quote_id` | `quotes.quote_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_readiness.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `individual_production_plans.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `batch_memberships.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.quote_id` | `quotes.quote_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 5. Diagram check

The canonical Mermaid ERD is `data/03-erd.mmd`; the verbatim copy in `data/04-data-model.md` is the reviewable diagram. This module owns only the tables listed in section 2. Every relationship in section 4 has a matching declared foreign key in `data/schema/`, and the seed loader validates it at commit. The package-level counts and ERD/schema comparison are recorded in `data/04-data-model.md` section **Diagram and schema check**.

## 6. Normalization and rule enforcement

The canonical model records deliberate snapshots and JSON/document exceptions in `data/04-data-model.md` section **Normalization check and deliberate exceptions**. The named enforcement point for every owning specification business rule is in its **Business-rule enforcement map**. This module adds no second owner, duplicate business fact, or unstated persistence requirement.

## 7. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-06.sql`](schema/schema-MFG-06.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys. The generator validates fixtures before writing CSV files.

## 8. End-to-end traceability

`data/07-end-to-end-traceability.md` links the approved PRD item, module/function requirement, input/output contract, table/attribute, representative seed row and screen. It records when an output is deliberately session-only or derived rather than persisted.

## 9. Validation record

Before the submission tag, run `uv run data/seed/generate_seed.py`, then `uv run data/schema/load_seed.py --database data/schema/weavelink-midterm.db`; both must pass and `git status --short` must remain empty after removing the ignored validation database.

## 10. Source and scope control

This is a derived data document. `docs/prd.md` and `docs/spec/` remain the approved source of requirements; a new persisted entity, field, relationship, normalization exception or enforcement decision requires a cited source and Group B review.

## 11. Privacy declaration

- [x] Every seed row is synthetic and is generated from fixed repository literals; no value is copied from a real person, organization, payment, order or product.
- [x] Email fixtures use the reserved `example.invalid` domain; assets use synthetic storage keys.
- [x] Passwords, tokens and provider credentials are synthetic hashes or secret references, never live values.
- [x] Personal try-on photos and generated results are session-only and never appear in seed, schema or order payloads.
- [x] The generator, schema loader and traceability review are run before the submission tag to detect invalid references, drift or accidental data changes.
