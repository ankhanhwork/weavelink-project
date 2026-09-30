-- SQLite validation schema for MFG-01.
CREATE TABLE IF NOT EXISTS "users" (
    "user_id" UUID PRIMARY KEY,
    "email" TEXT,
    "full_name" TEXT,
    "password_hash" TEXT,
    "customer_capability" BOOLEAN,
    "verified_at" TIMESTAMPTZ,
    "active" BOOLEAN,
    "closed_at" TIMESTAMPTZ,
    "anonymized_at" TEXT,
    "version" BIGINT,
    "created_at" TIMESTAMPTZ,
    "updated_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "sessions" (
    "session_id" UUID PRIMARY KEY,
    "user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "token_hash" TEXT,
    "idle_expires_at" TIMESTAMPTZ,
    "absolute_expires_at" TIMESTAMPTZ,
    "revoked_at" TIMESTAMPTZ,
    "created_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "one_time_tokens" (
    "token_id" UUID PRIMARY KEY,
    "user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "purpose" TEXT,
    "portal" TEXT,
    "token_hash" TEXT,
    "expires_at" TIMESTAMPTZ,
    "consumed_at" TIMESTAMPTZ,
    "created_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "notifications" (
    "notification_id" UUID PRIMARY KEY,
    "recipient_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "source_event_id" UUID REFERENCES "outbox_events" ("outbox_event_id") DEFERRABLE INITIALLY DEFERRED,
    "type" TEXT,
    "title" TEXT,
    "body" TEXT,
    "target_route" TEXT,
    "email_delivery_state" TEXT,
    "created_at" TIMESTAMPTZ,
    "read_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "outbox_events" (
    "outbox_event_id" UUID PRIMARY KEY,
    "source_module" TEXT,
    "source_entity_type" TEXT,
    "source_entity_id" UUID,
    "event_type" TEXT,
    "payload_json" JSONB,
    "delivery_state" TEXT,
    "created_at" TIMESTAMPTZ,
    "delivered_at" TIMESTAMPTZ
);
