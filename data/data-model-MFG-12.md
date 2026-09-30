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

## 3. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `audit_events.actor_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `backups.creator_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `system_configs.actor_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `restore_journals.backup_id` | `backups.backup_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-12.sql`](schema/schema-MFG-12.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
