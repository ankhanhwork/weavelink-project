-- SQLite validation schema for MFG-12.
CREATE TABLE IF NOT EXISTS "audit_events" (
    "audit_event_id" UUID PRIMARY KEY,
    "actor_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "buyer_organization_context" TEXT,
    "target_type" TEXT,
    "target_id" UUID,
    "action" TEXT,
    "outcome" TEXT,
    "severity" TEXT,
    "request_id" TEXT,
    "occurred_at" TIMESTAMPTZ,
    "redacted_details_json" JSONB
);
CREATE TABLE IF NOT EXISTS "backups" (
    "backup_id" UUID PRIMARY KEY,
    "created_at" TIMESTAMPTZ,
    "creator_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "state" TEXT,
    "manifest_reference" TEXT,
    "checksum" TEXT,
    "schema_version" BIGINT,
    "asset_count" BIGINT,
    "transaction_log_start" TEXT,
    "transaction_log_end" TEXT,
    "error_code" TEXT
);
CREATE TABLE IF NOT EXISTS "system_configs" (
    "system_config_id" UUID PRIMARY KEY,
    "version" BIGINT NOT NULL,
    "public_company_contacts_json" JSONB NOT NULL,
    "smtp_secret_reference" TEXT NOT NULL,
    "vnpay_secret_reference" TEXT NOT NULL,
    "design_service_fee_vnd" BIGINT,
    "shipping_vnd" BIGINT,
    "daily_backup_time" TEXT,
    "daily_retention_count" BIGINT,
    "weekly_retention_count" BIGINT,
    "production_notification_email" TEXT,
    "activated_at" TIMESTAMPTZ NOT NULL,
    "actor_id" UUID NOT NULL REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "restore_journals" (
    "restore_journal_id" UUID PRIMARY KEY,
    "backup_id" UUID REFERENCES "backups" ("backup_id") DEFERRABLE INITIALLY DEFERRED,
    "committed_watermark" TEXT,
    "state" TEXT,
    "started_at" TIMESTAMPTZ,
    "completed_at" TIMESTAMPTZ,
    "payment_event_reference" TEXT,
    "error_code" TEXT
);
