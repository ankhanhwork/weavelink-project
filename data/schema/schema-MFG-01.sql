-- SQLite validation schema for MFG-01.
CREATE TABLE IF NOT EXISTS "users" (
    "user_id" UUID PRIMARY KEY,
    "email" TEXT NOT NULL UNIQUE,
    "full_name" TEXT NOT NULL,
    "password_hash" TEXT NOT NULL,
    "customer_capability" BOOLEAN NOT NULL,
    "verified_at" TIMESTAMPTZ,
    "active" BOOLEAN NOT NULL,
    "closed_at" TIMESTAMPTZ,
    "anonymized_at" TEXT,
    "version" BIGINT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL
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
    "user_id" UUID NOT NULL REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "purpose" TEXT NOT NULL,
    "portal" TEXT,
    "token_hash" TEXT NOT NULL,
    "expires_at" TIMESTAMPTZ NOT NULL,
    "consumed_at" TIMESTAMPTZ,
    "created_at" TIMESTAMPTZ NOT NULL
);
CREATE TABLE IF NOT EXISTS "notifications" (
    "notification_id" UUID PRIMARY KEY,
    "recipient_user_id" UUID NOT NULL REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "source_event_id" UUID NOT NULL REFERENCES "outbox_events" ("outbox_event_id") DEFERRABLE INITIALLY DEFERRED,
    "type" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "body" TEXT NOT NULL,
    "target_route" TEXT,
    "email_delivery_state" TEXT,
    "created_at" TIMESTAMPTZ NOT NULL,
    "read_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "outbox_events" (
    "outbox_event_id" UUID PRIMARY KEY,
    "source_module" TEXT NOT NULL,
    "source_entity_type" TEXT NOT NULL,
    "source_entity_id" UUID NOT NULL,
    "event_type" TEXT NOT NULL,
    "payload_json" JSONB NOT NULL,
    "delivery_state" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL,
    "delivered_at" TIMESTAMPTZ
);
