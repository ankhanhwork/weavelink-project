# Data Model and Mockup Data: MFG-10 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-10. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-10 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `flexible_preferences` | Owned by MFG-10; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `production_readiness` | Owned by MFG-10; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `individual_production_plans` | Owned by MFG-10; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `production_capacity_profiles` | Owned by MFG-10; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `production_batches` | Owned by MFG-10; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `batch_memberships` | Owned by MFG-10; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `flexible_preferences.quote_id` | `quotes.quote_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_readiness.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `individual_production_plans.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `individual_production_plans.approved_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `individual_production_plans.started_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_capacity_profiles.material_profile_id` | `material_profiles.material_profile_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_capacity_profiles.updated_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_batches.capacity_profile_id` | `production_capacity_profiles.capacity_profile_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_batches.approved_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `batch_memberships.batch_id` | `production_batches.batch_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `batch_memberships.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-10.sql`](schema/schema-MFG-10.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
