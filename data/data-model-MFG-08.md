# Data Model and Mockup Data: MFG-08 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-08. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-08 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `customer_assignments` | Owned by MFG-08; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `consultations` | Owned by MFG-08; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `lead_design_links` | Owned by MFG-08; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `stage_histories` | Owned by MFG-08; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `interaction_logs` | Owned by MFG-08; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `internal_notes` | Owned by MFG-08; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `admin_reviews` | Owned by MFG-08; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `customer_assignments.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `consultations.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_assignments.sales_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_assignments.assigned_by_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `consultations.owner_sales_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `lead_design_links.consultation_id` | `consultations.consultation_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `lead_design_links.design_id` | `designs.design_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `stage_histories.consultation_id` | `consultations.consultation_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `stage_histories.actor_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `interaction_logs.consultation_id` | `consultations.consultation_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `interaction_logs.author_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `interaction_logs.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `internal_notes.consultation_id` | `consultations.consultation_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `internal_notes.author_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `admin_reviews.consultation_id` | `consultations.consultation_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `admin_reviews.requester_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `admin_reviews.decider_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-08.sql`](schema/schema-MFG-08.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
