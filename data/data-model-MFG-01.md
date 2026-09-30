# Data Model and Mockup Data: MFG-01 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-01. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-01 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `users` | Owned by MFG-01; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `sessions` | Owned by MFG-01; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `one_time_tokens` | Owned by MFG-01; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `notifications` | Owned by MFG-01; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `outbox_events` | Owned by MFG-01; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Attribute traceability

| Table | Persisted attributes | Trace source |
|---|---|---|
| `users` | `user_id`, `email`, `full_name`, `password_hash`, `customer_capability`, `verified_at`, `active`, `closed_at`, `anonymized_at`, `version`, `created_at`, `updated_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-01` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `sessions` | `session_id`, `user_id`, `token_hash`, `idle_expires_at`, `absolute_expires_at`, `revoked_at`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-01` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `one_time_tokens` | `token_id`, `user_id`, `purpose`, `portal`, `token_hash`, `expires_at`, `consumed_at`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-01` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `notifications` | `notification_id`, `recipient_user_id`, `source_event_id`, `type`, `title`, `body`, `target_route`, `email_delivery_state`, `created_at`, `read_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-01` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `outbox_events` | `outbox_event_id`, `source_module`, `source_entity_type`, `source_entity_id`, `event_type`, `payload_json`, `delivery_state`, `created_at`, `delivered_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-01` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |

## 4. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `staff_accounts.user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `sessions.user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `one_time_tokens.user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `notifications.recipient_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `notifications.source_event_id` | `outbox_events.outbox_event_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `designs.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_versions.uploader_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.accepted_by_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_feedback.author_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_approvals.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_provided_confirmations.confirmer_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `quotes.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `payment_transactions.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_timeline_events.actor_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_assignments.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `consultations.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_assignments.sales_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_assignments.assigned_by_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `consultations.owner_sales_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `stage_histories.actor_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `interaction_logs.author_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `internal_notes.author_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `admin_reviews.requester_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `admin_reviews.decider_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `signature_evidence.signer_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_entries.owner_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `journey_intents.owner_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `export_requests.actor_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `audit_events.actor_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `backups.creator_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `system_configs.actor_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 5. Diagram check

The canonical Mermaid ERD is `data/03-erd.mmd`; the verbatim copy in `data/04-data-model.md` is the reviewable diagram. This module owns only the tables listed in section 2. Every relationship in section 4 has a matching declared foreign key in `data/schema/`, and the seed loader validates it at commit. The package-level counts and ERD/schema comparison are recorded in `data/04-data-model.md` section **Diagram and schema check**.

## 6. Normalization and rule enforcement

The canonical model records deliberate snapshots and JSON/document exceptions in `data/04-data-model.md` section **Normalization check and deliberate exceptions**. The named enforcement point for every owning specification business rule is in its **Business-rule enforcement map**. This module adds no second owner, duplicate business fact, or unstated persistence requirement.

## 7. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-01.sql`](schema/schema-MFG-01.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys. The generator validates fixtures before writing CSV files.

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
