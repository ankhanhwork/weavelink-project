# Data Model and Mockup Data: MFG-04 Module Data Model

## 1. Scope

This module index assigns data ownership for MFG-04. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables MFG-04 owns and the cross-module references that must remain consistent with it.

## 2. Owned entities

| Table | Ownership decision | Canonical attributes and constraints |
|---|---|---|
| `products` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `product_versions` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `product_sizes` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `product_colors` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `material_profiles` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `product_materials` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `print_methods` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `volume_pricing_tiers` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `product_options` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `print_areas` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `product_images` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |
| `search_synonym_sets` | Owned by MFG-04; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |

## 3. Attribute traceability

| Table | Persisted attributes | Trace source |
|---|---|---|
| `products` | `product_id`, `sku`, `status`, `current_version`, `created_at`, `updated_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `product_versions` | `product_version_id`, `product_id`, `version`, `name`, `description`, `category`, `branch`, `sub_type`, `base_unit_price_vnd`, `min_order_quantity`, `max_units_per_order`, `keywords`, `created_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `product_sizes` | `product_size_id`, `product_version_id`, `size_label`, `display_order` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `product_colors` | `product_color_id`, `product_version_id`, `color_label`, `display_order` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `material_profiles` | `material_profile_id`, `material_label`, `durability`, `breathability`, `wash_durability`, `wrinkle_resistance`, `abrasion_resistance`, `stain_resistance`, `suited_occupations_json`, `suited_seasons_json`, `pros_json`, `cons_json` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `product_materials` | `product_material_id`, `product_version_id`, `material_profile_id`, `material_label_snapshot`, `option_surcharge_vnd` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `print_methods` | `print_method_id`, `name`, `multicolor_support`, `fine_detail_support`, `notes` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `volume_pricing_tiers` | `tier_id`, `product_version_id`, `quantity_from`, `quantity_to`, `unit_price_vnd` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `product_options` | `product_option_id`, `product_version_id`, `option_type`, `option_value`, `print_method_id`, `option_surcharge_vnd` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `print_areas` | `print_area_id`, `product_version_id`, `size_label`, `side`, `width_mm`, `height_mm`, `origin_x_mm`, `origin_y_mm` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `product_images` | `product_image_id`, `product_version_id`, `asset_id`, `display_order` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |
| `search_synonym_sets` | `synonym_set_id`, `version`, `entries_json`, `updated_by_user_id`, `updated_at` | Canonical table row in `data/04-data-model.md`; owning `MFG-04` specification §5.1 input/output contract, §6 key entities, keys, or deliberate audit columns. |

## 4. Relationships and cross-module references

| Referencing table and field | Referenced table and field | Check |
|---|---|---|
| `product_versions.product_id` | `products.product_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_sizes.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_colors.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_materials.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_materials.material_profile_id` | `material_profiles.material_profile_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `volume_pricing_tiers.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_options.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_options.print_method_id` | `print_methods.print_method_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `print_areas.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_images.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_images.asset_id` | `assets.asset_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `designs.product_id` | `products.product_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_versions.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `design_requests.product_id` | `products.product_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_mockup_templates.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `quotes.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `orders.product_version_id` | `product_versions.product_version_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `production_capacity_profiles.material_profile_id` | `material_profiles.material_profile_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `product_entries.product_id` | `products.product_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |
| `analytics_events.product_id` | `products.product_id` | Foreign key in `data/schema/`; validate after every seed regeneration. |

## 5. Diagram check

The canonical Mermaid ERD is `data/03-erd.mmd`; the verbatim copy in `data/04-data-model.md` is the reviewable diagram. This module owns only the tables listed in section 2. Every relationship in section 4 has a matching declared foreign key in `data/schema/`, and the seed loader validates it at commit. The package-level counts and ERD/schema comparison are recorded in `data/04-data-model.md` section **Diagram and schema check**.

## 6. Normalization and rule enforcement

The canonical model records deliberate snapshots and JSON/document exceptions in `data/04-data-model.md` section **Normalization check and deliberate exceptions**. The named enforcement point for every owning specification business rule is in its **Business-rule enforcement map**. This module adds no second owner, duplicate business fact, or unstated persistence requirement.

## 7. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-04.sql`](schema/schema-MFG-04.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys. The generator validates fixtures before writing CSV files.

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
