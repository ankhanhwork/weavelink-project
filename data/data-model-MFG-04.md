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

## 3. Relationships and cross-module references

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

## 4. Schema and seed evidence

The SQLite tables owned by this module are created in [`data/schema/schema-MFG-04.sql`](schema/schema-MFG-04.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.

## 5. Traceability and review

Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.
