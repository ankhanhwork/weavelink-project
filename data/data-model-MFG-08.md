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

## 3. Attribute traceability

| Table | Persisted attributes | Trace source |
|---|---|---|
| `customer_assignments` | `assignment_id`, `customer_id`, `sales_user_id`, `assigned_by_user_id`, `assigned_at`, `ended_at`, `active`, `version` | Canonical table row in `data/04-data-model.md`; owning `MFG-08` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `consultations` | `consultation_id`, `customer_id`, `pipeline_stage`, `customer_model`, `owner_sales_user_id`, `contact_name`, `phone`, `email`, `requirement_summary`, `product_interest`, `estimated_quantity`, `requested_deadline`, `design_source`, `design_readiness`, `technical_adjustment_required`, `proposal_milestone`, `lost_reason`, `lost_note`, `stage_entered_at`, `version`, `created_at`, `updated_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-08` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `lead_design_links` | `lead_design_link_id`, `consultation_id`, `design_id`, `design_scope`, `version`, `created_at`, `updated_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-08` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `stage_histories` | `stage_history_id`, `consultation_id`, `from_stage`, `to_stage`, `actor_user_id`, `source`, `reason`, `reference`, `occurred_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-08` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `interaction_logs` | `interaction_id`, `consultation_id`, `type`, `channel`, `occurred_at`, `summary`, `author_user_id`, `design_version_id` | Canonical table row in `data/04-data-model.md`; owning `MFG-08` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `internal_notes` | `note_id`, `consultation_id`, `text`, `author_user_id`, `pinned`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-08` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `admin_reviews` | `review_id`, `consultation_id`, `type`, `requested_value`, `reason`, `status`, `requester_user_id`, `requested_at`, `decider_user_id`, `decided_at`, `decision_note` | Canonical table row in `data/04-data-model.md`; owning `MFG-08` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |

## 4. Relationships and cross-module references

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

## 5. Diagram check

The canonical Mermaid ERD is `data/03-erd.mmd`; the verbatim copy in `data/04-data-model.md` is the reviewable diagram. This module owns only the tables listed in section 2. Every relationship in section 4 has a matching declared foreign key in `data/schema/`, and the seed loader validates it at commit. The package-level counts and ERD/schema comparison are recorded in `data/04-data-model.md` section **Diagram and schema check**.

## 6. Normalization and rule enforcement

The canonical model records deliberate snapshots and JSON/document exceptions in `data/04-data-model.md` section **Normalization check and deliberate exceptions**. The named enforcement point for every owning specification business rule is in its **Business-rule enforcement map**. This module adds no second owner, duplicate business fact, or unstated persistence requirement.

## 7. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-08.sql`](schema/schema-MFG-08.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys. The generator validates fixtures before writing CSV files.

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
