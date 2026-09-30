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

## 3. Attribute traceability

| Table | Persisted attributes | Trace source |
|---|---|---|
| `product_entries` | `product_entry_id`, `owner_user_id`, `product_id`, `source`, `entered_at`, `product_version` | Canonical table row in `data/04-data-model.md`; owning `MFG-11` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `journey_intents` | `journey_intent_id`, `owner_user_id`, `product_entry_id`, `intent_type`, `parent_intent_id`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-11` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `analytics_events` | `analytics_event_id`, `schema_version`, `event_name`, `source_kind`, `entity_type`, `entity_id`, `occurred_at`, `received_at`, `actor_kind`, `customer_id`, `product_entry_id`, `journey_intent_id`, `product_id`, `design_id`, `quote_id`, `order_id`, `request_id`, `contract_id`, `bound_versions_json`, `sample_cycle`, `reason_code`, `source_event_id`, `dataset_flags_json` | Canonical table row in `data/04-data-model.md`; owning `MFG-11` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `analytics_results` | `analytics_result_id`, `query_context_json`, `unit`, `template`, `cohort`, `observation_mode`, `eligible_count`, `immature_count`, `cutoff`, `timezone`, `generated_at`, `expires_at`, `source_watermark`, `definition_version`, `coverage_json`, `metrics_json` | Canonical table row in `data/04-data-model.md`; owning `MFG-11` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `export_requests` | `export_request_id`, `actor_user_id`, `analytics_result_id`, `format`, `dataset`, `watermark`, `created_at`, `completed_at`, `expires_at`, `state`, `private_asset_id`, `row_count`, `safe_error` | Canonical table row in `data/04-data-model.md`; owning `MFG-11` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |

## 4. Relationships and cross-module references

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

## 5. Diagram check

The canonical Mermaid ERD is `data/03-erd.mmd`; the verbatim copy in `data/04-data-model.md` is the reviewable diagram. This module owns only the tables listed in section 2. Every relationship in section 4 has a matching declared foreign key in `data/schema/`, and the seed loader validates it at commit. The package-level counts and ERD/schema comparison are recorded in `data/04-data-model.md` section **Diagram and schema check**.

## 6. Normalization and rule enforcement

The canonical model records deliberate snapshots and JSON/document exceptions in `data/04-data-model.md` section **Normalization check and deliberate exceptions**. The named enforcement point for every owning specification business rule is in its **Business-rule enforcement map**. This module adds no second owner, duplicate business fact, or unstated persistence requirement.

## 7. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-11.sql`](schema/schema-MFG-11.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys. The generator validates fixtures before writing CSV files.

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
