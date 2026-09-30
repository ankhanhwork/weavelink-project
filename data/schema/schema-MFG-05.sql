-- SQLite validation schema for MFG-05.
CREATE TABLE IF NOT EXISTS "assets" (
    "asset_id" UUID PRIMARY KEY,
    "owner_user_id" UUID,
    "ownership" TEXT,
    "mime_type" TEXT,
    "scan_status" TEXT,
    "storage_key" TEXT,
    "size_bytes" BIGINT,
    "created_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "designs" (
    "design_id" UUID PRIMARY KEY,
    "customer_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "product_id" UUID REFERENCES "products" ("product_id") DEFERRABLE INITIALLY DEFERRED,
    "source_design_request_id" UUID REFERENCES "design_requests" ("design_request_id") DEFERRABLE INITIALLY DEFERRED,
    "status" TEXT,
    "current_version" BIGINT,
    "created_at" TIMESTAMPTZ,
    "updated_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "design_versions" (
    "design_version_id" UUID PRIMARY KEY,
    "design_id" UUID REFERENCES "designs" ("design_id") DEFERRABLE INITIALLY DEFERRED,
    "version" BIGINT,
    "product_version_id" UUID REFERENCES "product_versions" ("product_version_id") DEFERRABLE INITIALLY DEFERRED,
    "source" TEXT,
    "review_state" TEXT,
    "uploader_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "original_channel" TEXT,
    "change_note" TEXT,
    "preview_asset_id" UUID REFERENCES "assets" ("asset_id") DEFERRABLE INITIALLY DEFERRED,
    "created_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "design_placements" (
    "placement_id" UUID PRIMARY KEY,
    "design_version_id" UUID REFERENCES "design_versions" ("design_version_id") DEFERRABLE INITIALLY DEFERRED,
    "asset_id" UUID REFERENCES "assets" ("asset_id") DEFERRABLE INITIALLY DEFERRED,
    "side" TEXT,
    "x_mm" NUMERIC,
    "y_mm" NUMERIC,
    "width_mm" NUMERIC,
    "height_mm" NUMERIC,
    "processing_method" TEXT
);
CREATE TABLE IF NOT EXISTS "design_requests" (
    "design_request_id" UUID PRIMARY KEY,
    "customer_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "product_id" UUID REFERENCES "products" ("product_id") DEFERRABLE INITIALLY DEFERRED,
    "requirements" TEXT,
    "requested_deadline" DATE,
    "committed_due_at" TIMESTAMPTZ,
    "complexity" TEXT,
    "rationale" TEXT,
    "rejection_reason" TEXT,
    "assessed_by_staff_id" UUID REFERENCES "staff_accounts" ("staff_account_id") DEFERRABLE INITIALLY DEFERRED,
    "assessed_at" TIMESTAMPTZ,
    "fee_vnd" BIGINT,
    "proposal_version" BIGINT,
    "accepted_fee_version" BIGINT,
    "accepted_fee_vnd" BIGINT,
    "accepted_by_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "accepted_at" TIMESTAMPTZ,
    "fee_order_id" UUID REFERENCES "orders" ("order_id") DEFERRABLE INITIALLY DEFERRED,
    "fee_allocation_version" BIGINT,
    "state" TEXT,
    "assignee_staff_id" UUID REFERENCES "staff_accounts" ("staff_account_id") DEFERRABLE INITIALLY DEFERRED,
    "version" BIGINT,
    "created_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "design_request_assets" (
    "design_request_asset_id" UUID PRIMARY KEY,
    "design_request_id" UUID REFERENCES "design_requests" ("design_request_id") DEFERRABLE INITIALLY DEFERRED,
    "asset_id" UUID REFERENCES "assets" ("asset_id") DEFERRABLE INITIALLY DEFERRED,
    "display_order" BIGINT
);
CREATE TABLE IF NOT EXISTS "design_feedback" (
    "feedback_id" UUID PRIMARY KEY,
    "design_version_id" UUID REFERENCES "design_versions" ("design_version_id") DEFERRABLE INITIALLY DEFERRED,
    "author_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "decision" TEXT,
    "change_request_text" TEXT,
    "preferred_colour" TEXT,
    "additional_notes" TEXT,
    "created_at" TIMESTAMPTZ,
    "idempotency_key" TEXT
);
CREATE TABLE IF NOT EXISTS "design_feedback_assets" (
    "design_feedback_asset_id" UUID PRIMARY KEY,
    "feedback_id" UUID REFERENCES "design_feedback" ("feedback_id") DEFERRABLE INITIALLY DEFERRED,
    "asset_id" UUID REFERENCES "assets" ("asset_id") DEFERRABLE INITIALLY DEFERRED,
    "display_order" BIGINT
);
CREATE TABLE IF NOT EXISTS "staff_replies" (
    "staff_reply_id" UUID PRIMARY KEY,
    "feedback_id" UUID REFERENCES "design_feedback" ("feedback_id") DEFERRABLE INITIALLY DEFERRED,
    "author_staff_id" UUID REFERENCES "staff_accounts" ("staff_account_id") DEFERRABLE INITIALLY DEFERRED,
    "reply_text" TEXT,
    "created_at" TIMESTAMPTZ,
    "idempotency_key" TEXT
);
CREATE TABLE IF NOT EXISTS "staff_reply_assets" (
    "staff_reply_asset_id" UUID PRIMARY KEY,
    "staff_reply_id" UUID REFERENCES "staff_replies" ("staff_reply_id") DEFERRABLE INITIALLY DEFERRED,
    "asset_id" UUID REFERENCES "assets" ("asset_id") DEFERRABLE INITIALLY DEFERRED,
    "display_order" BIGINT
);
CREATE TABLE IF NOT EXISTS "customer_approvals" (
    "approval_id" UUID PRIMARY KEY,
    "design_version_id" UUID REFERENCES "design_versions" ("design_version_id") DEFERRABLE INITIALLY DEFERRED,
    "customer_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "approved_at" TIMESTAMPTZ,
    "request_version" BIGINT,
    "idempotency_key" TEXT
);
CREATE TABLE IF NOT EXISTS "customer_provided_confirmations" (
    "confirmation_id" UUID PRIMARY KEY,
    "design_version_id" UUID REFERENCES "design_versions" ("design_version_id") DEFERRABLE INITIALLY DEFERRED,
    "confirmer_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "recorded_by_staff_id" UUID REFERENCES "staff_accounts" ("staff_account_id") DEFERRABLE INITIALLY DEFERRED,
    "original_channel" TEXT,
    "source_evidence" TEXT,
    "confirmed_at" TIMESTAMPTZ,
    "idempotency_key" TEXT
);
CREATE TABLE IF NOT EXISTS "product_mockup_templates" (
    "mockup_template_id" UUID PRIMARY KEY,
    "product_version_id" UUID REFERENCES "product_versions" ("product_version_id") DEFERRABLE INITIALLY DEFERRED,
    "view_id" TEXT,
    "base_asset_id" UUID REFERENCES "assets" ("asset_id") DEFERRABLE INITIALLY DEFERRED,
    "surface_grid_json" JSONB,
    "masks_json" JSONB,
    "material_color_support_json" JSONB
);
