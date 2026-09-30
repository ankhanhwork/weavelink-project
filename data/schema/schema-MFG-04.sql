-- SQLite validation schema for MFG-04.
CREATE TABLE IF NOT EXISTS "products" (
    "product_id" UUID PRIMARY KEY,
    "sku" TEXT NOT NULL UNIQUE,
    "status" TEXT NOT NULL,
    "current_version" BIGINT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "product_versions" (
    "product_version_id" UUID PRIMARY KEY,
    "product_id" UUID REFERENCES "products" ("product_id") DEFERRABLE INITIALLY DEFERRED,
    "version" BIGINT,
    "name" TEXT,
    "description" TEXT,
    "category" TEXT,
    "branch" TEXT,
    "sub_type" TEXT,
    "base_unit_price_vnd" BIGINT,
    "min_order_quantity" BIGINT,
    "max_units_per_order" BIGINT,
    "keywords" TEXT,
    "created_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "product_sizes" (
    "product_size_id" UUID PRIMARY KEY,
    "product_version_id" UUID REFERENCES "product_versions" ("product_version_id") DEFERRABLE INITIALLY DEFERRED,
    "size_label" TEXT,
    "display_order" BIGINT
);
CREATE TABLE IF NOT EXISTS "product_colors" (
    "product_color_id" UUID PRIMARY KEY,
    "product_version_id" UUID REFERENCES "product_versions" ("product_version_id") DEFERRABLE INITIALLY DEFERRED,
    "color_label" TEXT,
    "display_order" BIGINT
);
CREATE TABLE IF NOT EXISTS "material_profiles" (
    "material_profile_id" UUID PRIMARY KEY,
    "material_label" TEXT,
    "durability" TEXT,
    "breathability" TEXT,
    "wash_durability" TEXT,
    "wrinkle_resistance" TEXT,
    "abrasion_resistance" TEXT,
    "stain_resistance" TEXT,
    "suited_occupations_json" JSONB,
    "suited_seasons_json" JSONB,
    "pros_json" JSONB,
    "cons_json" JSONB
);
CREATE TABLE IF NOT EXISTS "product_materials" (
    "product_material_id" UUID PRIMARY KEY,
    "product_version_id" UUID REFERENCES "product_versions" ("product_version_id") DEFERRABLE INITIALLY DEFERRED,
    "material_profile_id" UUID REFERENCES "material_profiles" ("material_profile_id") DEFERRABLE INITIALLY DEFERRED,
    "material_label_snapshot" TEXT,
    "option_surcharge_vnd" BIGINT
);
CREATE TABLE IF NOT EXISTS "print_methods" (
    "print_method_id" UUID PRIMARY KEY,
    "name" TEXT,
    "multicolor_support" BOOLEAN,
    "fine_detail_support" BOOLEAN,
    "notes" TEXT
);
CREATE TABLE IF NOT EXISTS "volume_pricing_tiers" (
    "tier_id" UUID PRIMARY KEY,
    "product_version_id" UUID REFERENCES "product_versions" ("product_version_id") DEFERRABLE INITIALLY DEFERRED,
    "quantity_from" BIGINT,
    "quantity_to" BIGINT,
    "unit_price_vnd" BIGINT
);
CREATE TABLE IF NOT EXISTS "product_options" (
    "product_option_id" UUID PRIMARY KEY,
    "product_version_id" UUID REFERENCES "product_versions" ("product_version_id") DEFERRABLE INITIALLY DEFERRED,
    "option_type" TEXT,
    "option_value" TEXT,
    "print_method_id" UUID REFERENCES "print_methods" ("print_method_id") DEFERRABLE INITIALLY DEFERRED,
    "option_surcharge_vnd" BIGINT
);
CREATE TABLE IF NOT EXISTS "print_areas" (
    "print_area_id" UUID PRIMARY KEY,
    "product_version_id" UUID REFERENCES "product_versions" ("product_version_id") DEFERRABLE INITIALLY DEFERRED,
    "size_label" TEXT,
    "side" TEXT,
    "width_mm" NUMERIC,
    "height_mm" NUMERIC,
    "origin_x_mm" NUMERIC,
    "origin_y_mm" NUMERIC
);
CREATE TABLE IF NOT EXISTS "product_images" (
    "product_image_id" UUID PRIMARY KEY,
    "product_version_id" UUID REFERENCES "product_versions" ("product_version_id") DEFERRABLE INITIALLY DEFERRED,
    "asset_id" UUID REFERENCES "assets" ("asset_id") DEFERRABLE INITIALLY DEFERRED,
    "display_order" BIGINT
);
CREATE TABLE IF NOT EXISTS "search_synonym_sets" (
    "synonym_set_id" UUID PRIMARY KEY,
    "version" BIGINT,
    "entries_json" JSONB,
    "updated_by_user_id" UUID,
    "updated_at" TIMESTAMPTZ
);
