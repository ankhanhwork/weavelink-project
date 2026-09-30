# Data Model and Mockup Data: MFG-09 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-09. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-09 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `contract_templates` | Owned by MFG-09; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `contracts` | Owned by MFG-09; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `signature_evidence` | Owned by MFG-09; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `orders.contract_id` | `contracts.contract_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `contracts.order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `contracts.contract_template_id` | `contract_templates.contract_template_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `contracts.approved_design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `contracts.approved_sample_id` | `production_samples.sample_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `contracts.pdf_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `signature_evidence.contract_id` | `contracts.contract_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `signature_evidence.signer_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.contract_id` | `contracts.contract_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-09.sql`](schema/schema-MFG-09.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
