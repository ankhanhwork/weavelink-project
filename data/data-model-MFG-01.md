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

## 3. Relationships and cross-module references

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

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-01.sql`](schema/schema-MFG-01.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
