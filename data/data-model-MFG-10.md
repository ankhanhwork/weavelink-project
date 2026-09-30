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

## 3. Attribute traceability

| Table | Persisted attributes | Trace source |
|---|---|---|
| `flexible_preferences` | `flexible_preference_id`, `quote_id`, `merge_opt_in`, `accepted_policy_version`, `accepted_at`, `incentive_vnd` | Canonical table row in `data/04-data-model.md`; owning `MFG-10` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `production_readiness` | `production_readiness_id`, `order_id`, `production_ready_at`, `readiness_day_1`, `last_waiting_date`, `production_window_first_date`, `production_due_at`, `wait_end_exclusive_at`, `calendar_version`, `waiting_workdays`, `production_window_min_workdays`, `production_window_max_workdays` | Canonical table row in `data/04-data-model.md`; owning `MFG-10` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `individual_production_plans` | `individual_plan_id`, `order_id`, `approved_by_staff_id`, `approved_at`, `started_by_staff_id`, `started_at`, `status`, `retained_incentive_vnd`, `version` | Canonical table row in `data/04-data-model.md`; owning `MFG-10` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `production_capacity_profiles` | `capacity_profile_id`, `production_type_key`, `material_profile_id`, `daily_output_capacity`, `active`, `version`, `updated_by_staff_id`, `updated_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-10` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `production_batches` | `batch_id`, `capacity_profile_id`, `kind`, `status`, `scheduled_start_at`, `planned_completion_at`, `daily_capacity_snapshot`, `total_quantity`, `required_workdays`, `approved_by_staff_id`, `approved_at`, `locked_at`, `started_at`, `version` | Canonical table row in `data/04-data-model.md`; owning `MFG-10` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `batch_memberships` | `batch_membership_id`, `batch_id`, `order_id`, `assigned_at`, `released_at`, `started_at`, `active`, `lock_start_version` | Canonical table row in `data/04-data-model.md`; owning `MFG-10` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |

## 4. Relationships and cross-module references

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

## 5. Diagram check

The canonical Mermaid ERD is `data/03-erd.mmd`; the verbatim copy in `data/04-data-model.md` is the reviewable diagram. This module owns only the tables listed in section 2. Every relationship in section 4 has a matching declared foreign key in `data/schema/`, and the seed loader validates it at commit. The package-level counts and ERD/schema comparison are recorded in `data/04-data-model.md` section **Diagram and schema check**.

## 6. Normalization and rule enforcement

The canonical model records deliberate snapshots and JSON/document exceptions in `data/04-data-model.md` section **Normalization check and deliberate exceptions**. The named enforcement point for every owning specification business rule is in its **Business-rule enforcement map**. This module adds no second owner, duplicate business fact, or unstated persistence requirement.

## 7. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-10.sql`](schema/schema-MFG-10.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys. The generator validates fixtures before writing CSV files.

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
