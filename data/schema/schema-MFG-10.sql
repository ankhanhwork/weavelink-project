-- SQLite validation schema for MFG-10.
CREATE TABLE IF NOT EXISTS "flexible_preferences" (
    "flexible_preference_id" UUID PRIMARY KEY,
    "quote_id" UUID REFERENCES "quotes" ("quote_id") DEFERRABLE INITIALLY DEFERRED,
    "merge_opt_in" BOOLEAN,
    "accepted_policy_version" TEXT,
    "accepted_at" TIMESTAMPTZ,
    "incentive_vnd" BIGINT
);
CREATE TABLE IF NOT EXISTS "production_readiness" (
    "production_readiness_id" UUID PRIMARY KEY,
    "order_id" UUID REFERENCES "orders" ("order_id") DEFERRABLE INITIALLY DEFERRED,
    "production_ready_at" TIMESTAMPTZ,
    "readiness_day_1" DATE,
    "last_waiting_date" DATE,
    "production_window_first_date" DATE,
    "production_due_at" DATE,
    "wait_end_exclusive_at" TIMESTAMPTZ,
    "calendar_version" TEXT,
    "waiting_workdays" BIGINT,
    "production_window_min_workdays" BIGINT,
    "production_window_max_workdays" BIGINT
);
CREATE TABLE IF NOT EXISTS "individual_production_plans" (
    "individual_plan_id" UUID PRIMARY KEY,
    "order_id" UUID REFERENCES "orders" ("order_id") DEFERRABLE INITIALLY DEFERRED,
    "approved_by_staff_id" UUID REFERENCES "staff_accounts" ("staff_account_id") DEFERRABLE INITIALLY DEFERRED,
    "approved_at" TIMESTAMPTZ,
    "started_by_staff_id" UUID REFERENCES "staff_accounts" ("staff_account_id") DEFERRABLE INITIALLY DEFERRED,
    "started_at" TIMESTAMPTZ,
    "status" TEXT,
    "retained_incentive_vnd" BIGINT,
    "version" BIGINT
);
CREATE TABLE IF NOT EXISTS "production_capacity_profiles" (
    "capacity_profile_id" UUID PRIMARY KEY,
    "production_type_key" TEXT,
    "material_profile_id" UUID REFERENCES "material_profiles" ("material_profile_id") DEFERRABLE INITIALLY DEFERRED,
    "daily_output_capacity" BIGINT,
    "active" BOOLEAN,
    "version" BIGINT,
    "updated_by_staff_id" UUID REFERENCES "staff_accounts" ("staff_account_id") DEFERRABLE INITIALLY DEFERRED,
    "updated_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "production_batches" (
    "batch_id" UUID PRIMARY KEY,
    "capacity_profile_id" UUID REFERENCES "production_capacity_profiles" ("capacity_profile_id") DEFERRABLE INITIALLY DEFERRED,
    "kind" TEXT,
    "status" TEXT,
    "scheduled_start_at" TIMESTAMPTZ,
    "planned_completion_at" TIMESTAMPTZ,
    "daily_capacity_snapshot" BIGINT,
    "total_quantity" BIGINT,
    "required_workdays" BIGINT,
    "approved_by_staff_id" UUID REFERENCES "staff_accounts" ("staff_account_id") DEFERRABLE INITIALLY DEFERRED,
    "approved_at" TIMESTAMPTZ,
    "locked_at" TIMESTAMPTZ,
    "started_at" TIMESTAMPTZ,
    "version" BIGINT
);
CREATE TABLE IF NOT EXISTS "batch_memberships" (
    "batch_membership_id" UUID PRIMARY KEY,
    "batch_id" UUID REFERENCES "production_batches" ("batch_id") DEFERRABLE INITIALLY DEFERRED,
    "order_id" UUID REFERENCES "orders" ("order_id") DEFERRABLE INITIALLY DEFERRED,
    "assigned_at" TIMESTAMPTZ,
    "released_at" TIMESTAMPTZ,
    "started_at" TIMESTAMPTZ,
    "active" BOOLEAN,
    "lock_start_version" BIGINT
);
