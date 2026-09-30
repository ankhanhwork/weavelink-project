# Data Model and Mockup Data: MFG-12 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-12. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-12 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `audit_events` | Owned by MFG-12; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `backups` | Owned by MFG-12; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `system_configs` | Owned by MFG-12; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `restore_journals` | Owned by MFG-12; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Attribute traceability

| Table | Persisted attributes | Trace source |
|---|---|---|
| `audit_events` | `audit_event_id`, `actor_id`, `buyer_organization_context`, `target_type`, `target_id`, `action`, `outcome`, `severity`, `request_id`, `occurred_at`, `redacted_details_json` | Canonical table row in `data/04-data-model.md`; owning `MFG-12` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `backups` | `backup_id`, `created_at`, `creator_id`, `state`, `manifest_reference`, `checksum`, `schema_version`, `asset_count`, `transaction_log_start`, `transaction_log_end`, `error_code` | Canonical table row in `data/04-data-model.md`; owning `MFG-12` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `system_configs` | `system_config_id`, `version`, `public_company_contacts_json`, `smtp_secret_reference`, `vnpay_secret_reference`, `design_service_fee_vnd`, `shipping_vnd`, `daily_backup_time`, `daily_retention_count`, `weekly_retention_count`, `production_notification_email`, `activated_at`, `actor_id` | Canonical table row in `data/04-data-model.md`; owning `MFG-12` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `restore_journals` | `restore_journal_id`, `backup_id`, `committed_watermark`, `state`, `started_at`, `completed_at`, `payment_event_reference`, `error_code` | Canonical table row in `data/04-data-model.md`; owning `MFG-12` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |

## 4. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `audit_events.actor_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `backups.creator_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `system_configs.actor_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `restore_journals.backup_id` | `backups.backup_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 5. Diagram check

The canonical Mermaid ERD is `data/03-erd.mmd`; the verbatim copy in `data/04-data-model.md` is the reviewable diagram. This module owns only the tables listed in section 2. Every relationship in section 4 has a matching declared foreign key in `data/schema/`, and the seed loader validates it at commit. The package-level counts and ERD/schema comparison are recorded in `data/04-data-model.md` section **Diagram and schema check**.

## 6. Normalization and rule enforcement

The canonical model records deliberate snapshots and JSON/document exceptions in `data/04-data-model.md` section **Normalization check and deliberate exceptions**. The named enforcement point for every owning specification business rule is in its **Business-rule enforcement map**. This module adds no second owner, duplicate business fact, or unstated persistence requirement.

## 7. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-12.sql`](schema/schema-MFG-12.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys. The generator validates fixtures before writing CSV files.

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
