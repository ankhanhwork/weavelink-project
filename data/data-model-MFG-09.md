# Data Model and Mockup Data: MFG-09 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-09. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-09 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `contract_templates` | Owned by MFG-09; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `contracts` | Owned by MFG-09; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `signature_evidence` | Owned by MFG-09; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Attribute traceability

| Table | Persisted attributes | Trace source |
|---|---|---|
| `contract_templates` | `contract_template_id`, `template_family_id`, `name`, `version`, `structured_body`, `status`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-09` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `contracts` | `contract_id`, `order_id`, `contract_template_id`, `buyer_type`, `buyer_legal_name`, `buyer_tax_id`, `billing_address`, `approved_design_version_id`, `approved_sample_id`, `contract_total_vnd`, `deposit_percent`, `deposit_due_vnd`, `balance_due_vnd`, `balance_due_rule`, `payment_policy_version`, `version`, `template_version`, `content_hash`, `pdf_asset_id`, `status`, `ready_at`, `signed_at`, `voided_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-09` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `signature_evidence` | `signature_evidence_id`, `contract_id`, `signer_user_id`, `typed_name`, `consent_text_version`, `contract_hash`, `server_timestamp`, `observed_ip`, `user_agent`, `challenge_digest` | Canonical table row in `data/04-data-model.md`; owning `MFG-09` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |

## 4. Relationships and cross-module references

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

## 5. Diagram check

The canonical Mermaid ERD is `data/03-erd.mmd`; the verbatim copy in `data/04-data-model.md` is the reviewable diagram. This module owns only the tables listed in section 2. Every relationship in section 4 has a matching declared foreign key in `data/schema/`, and the seed loader validates it at commit. The package-level counts and ERD/schema comparison are recorded in `data/04-data-model.md` section **Diagram and schema check**.

## 6. Normalization and rule enforcement

The canonical model records deliberate snapshots and JSON/document exceptions in `data/04-data-model.md` section **Normalization check and deliberate exceptions**. The named enforcement point for every owning specification business rule is in its **Business-rule enforcement map**. This module adds no second owner, duplicate business fact, or unstated persistence requirement.

## 7. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-09.sql`](schema/schema-MFG-09.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys. The generator validates fixtures before writing CSV files.

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
