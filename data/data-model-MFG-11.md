# Data Model and Mockup Data: MFG-11 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-11. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-11 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `product_entries` | Owned by MFG-11; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `journey_intents` | Owned by MFG-11; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `analytics_events` | Owned by MFG-11; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `analytics_results` | Owned by MFG-11; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `export_requests` | Owned by MFG-11; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `quotes.journey_intent_id` | `journey_intents.journey_intent_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.journey_intent_id` | `journey_intents.journey_intent_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_entries.owner_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_entries.product_id` | `products.product_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `journey_intents.owner_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `journey_intents.product_entry_id` | `product_entries.product_entry_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `journey_intents.parent_intent_id` | `journey_intents.journey_intent_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.product_entry_id` | `product_entries.product_entry_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.journey_intent_id` | `journey_intents.journey_intent_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.product_id` | `products.product_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.design_id` | `designs.design_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.quote_id` | `quotes.quote_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.request_id` | `design_requests.design_request_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.contract_id` | `contracts.contract_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `export_requests.analytics_result_id` | `analytics_results.analytics_result_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `export_requests.actor_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `export_requests.private_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-11.sql`](schema/schema-MFG-11.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
