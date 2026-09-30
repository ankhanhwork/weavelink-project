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

## 3. Relationships and cross-module references

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

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-06.sql`](schema/schema-MFG-06.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
