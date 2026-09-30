# Data Model and Mockup Data: MFG-05 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-05. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-05 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `assets` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `designs` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `design_versions` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `design_placements` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `design_requests` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `design_request_assets` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `design_feedback` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `design_feedback_assets` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `staff_replies` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `staff_reply_assets` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `customer_approvals` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `customer_provided_confirmations` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `product_mockup_templates` | Owned by MFG-05; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Attribute traceability

| Table | Persisted attributes | Trace source |
|---|---|---|
| `assets` | `asset_id`, `owner_user_id`, `ownership`, `mime_type`, `scan_status`, `storage_key`, `size_bytes`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `designs` | `design_id`, `customer_id`, `product_id`, `source_design_request_id`, `status`, `current_version`, `created_at`, `updated_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `design_versions` | `design_version_id`, `design_id`, `version`, `product_version_id`, `source`, `review_state`, `uploader_user_id`, `original_channel`, `change_note`, `preview_asset_id`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `design_placements` | `placement_id`, `design_version_id`, `asset_id`, `side`, `x_mm`, `y_mm`, `width_mm`, `height_mm`, `processing_method` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `design_requests` | `design_request_id`, `customer_id`, `product_id`, `requirements`, `requested_deadline`, `committed_due_at`, `complexity`, `rationale`, `rejection_reason`, `assessed_by_staff_id`, `assessed_at`, `fee_vnd`, `proposal_version`, `accepted_fee_version`, `accepted_fee_vnd`, `accepted_by_user_id`, `accepted_at`, `fee_order_id`, `fee_allocation_version`, `state`, `assignee_staff_id`, `version`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `design_request_assets` | `design_request_asset_id`, `design_request_id`, `asset_id`, `display_order` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `design_feedback` | `feedback_id`, `design_version_id`, `author_user_id`, `decision`, `change_request_text`, `preferred_colour`, `additional_notes`, `created_at`, `idempotency_key` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `design_feedback_assets` | `design_feedback_asset_id`, `feedback_id`, `asset_id`, `display_order` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `staff_replies` | `staff_reply_id`, `feedback_id`, `author_staff_id`, `reply_text`, `created_at`, `idempotency_key` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `staff_reply_assets` | `staff_reply_asset_id`, `staff_reply_id`, `asset_id`, `display_order` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `customer_approvals` | `approval_id`, `design_version_id`, `customer_id`, `approved_at`, `request_version`, `idempotency_key` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `customer_provided_confirmations` | `confirmation_id`, `design_version_id`, `confirmer_user_id`, `recorded_by_staff_id`, `original_channel`, `source_evidence`, `confirmed_at`, `idempotency_key` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `product_mockup_templates` | `mockup_template_id`, `product_version_id`, `view_id`, `base_asset_id`, `surface_grid_json`, `masks_json`, `material_color_support_json` | Canonical table row in `data/04-data-model.md`; owning `MFG-05` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |

## 4. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `product_images.asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `designs.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `designs.product_id` | `products.product_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `designs.source_design_request_id` | `design_requests.design_request_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_versions.design_id` | `designs.design_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_versions.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_versions.uploader_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_versions.preview_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_placements.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_placements.asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.product_id` | `products.product_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.assessed_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.accepted_by_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.fee_order_id` | `orders.order_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.assignee_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_request_assets.design_request_id` | `design_requests.design_request_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_request_assets.asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_feedback.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_feedback.author_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_feedback_assets.feedback_id` | `design_feedback.feedback_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_feedback_assets.asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `staff_replies.feedback_id` | `design_feedback.feedback_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `staff_replies.author_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `staff_reply_assets.staff_reply_id` | `staff_replies.staff_reply_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `staff_reply_assets.asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_approvals.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_approvals.customer_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_provided_confirmations.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_provided_confirmations.confirmer_user_id` | `users.user_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `customer_provided_confirmations.recorded_by_staff_id` | `staff_accounts.staff_account_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_mockup_templates.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_mockup_templates.base_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `quotes.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.delivery_evidence_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_quote_cycles.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_samples.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_samples.evidence_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `order_timeline_events.evidence_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `lead_design_links.design_id` | `designs.design_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `interaction_logs.design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `contracts.approved_design_version_id` | `design_versions.design_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `contracts.pdf_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.design_id` | `designs.design_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.request_id` | `design_requests.design_request_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `export_requests.private_asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 5. Diagram check

The canonical Mermaid ERD is `data/03-erd.mmd`; the verbatim copy in `data/04-data-model.md` is the reviewable diagram. This module owns only the tables listed in section 2. Every relationship in section 4 has a matching declared foreign key in `data/schema/`, and the seed loader validates it at commit. The package-level counts and ERD/schema comparison are recorded in `data/04-data-model.md` section **Diagram and schema check**.

## 6. Normalization and rule enforcement

The canonical model records deliberate snapshots and JSON/document exceptions in `data/04-data-model.md` section **Normalization check and deliberate exceptions**. The named enforcement point for every owning specification business rule is in its **Business-rule enforcement map**. This module adds no second owner, duplicate business fact, or unstated persistence requirement.

## 7. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-05.sql`](schema/schema-MFG-05.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys. The generator validates fixtures before writing CSV files.

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
