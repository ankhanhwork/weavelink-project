# Data Model and Mockup Data: MFG-07 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-07. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-07 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| None | MFG-07 has no independently persisted entity in the approved model. | Cross-module references only. |

## 3. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| None | None | No persisted relationship is owned by this module. |

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-07.sql`](schema/schema-MFG-07.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
