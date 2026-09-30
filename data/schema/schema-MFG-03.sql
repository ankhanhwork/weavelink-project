-- SQLite validation schema for MFG-03.
CREATE TABLE IF NOT EXISTS "staff_accounts" (
    "staff_account_id" UUID PRIMARY KEY,
    "user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "role" TEXT,
    "status" TEXT,
    "invited_at" TIMESTAMPTZ,
    "activated_at" TIMESTAMPTZ,
    "deleted_at" TEXT,
    "version" BIGINT
);
CREATE TABLE IF NOT EXISTS "staff_invitations" (
    "invitation_id" UUID PRIMARY KEY,
    "staff_account_id" UUID REFERENCES "staff_accounts" ("staff_account_id") DEFERRABLE INITIALLY DEFERRED,
    "email_snapshot" TEXT,
    "role_snapshot" TEXT,
    "token_hash" TEXT,
    "expires_at" TIMESTAMPTZ,
    "accepted_at" TIMESTAMPTZ,
    "delivery_status" TEXT,
    "version" BIGINT
);
