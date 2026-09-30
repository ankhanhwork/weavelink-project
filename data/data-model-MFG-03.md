# Data Model and Mockup Data: MFG-03 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-03. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-03 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `staff_accounts` | Owned by MFG-03; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `staff_invitations` | Owned by MFG-03; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `staff_accounts.user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `staff_invitations.staff_account_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.assessed_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.assignee_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `staff_replies.author_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_provided_confirmations.recorded_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.received_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `individual_production_plans.approved_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `individual_production_plans.started_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_capacity_profiles.updated_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_batches.approved_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-03.sql`](schema/schema-MFG-03.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
