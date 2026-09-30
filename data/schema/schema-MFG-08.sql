-- SQLite validation schema for MFG-08.
CREATE TABLE IF NOT EXISTS "customer_assignments" (
    "assignment_id" UUID PRIMARY KEY,
    "customer_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "sales_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "assigned_by_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "assigned_at" TIMESTAMPTZ,
    "ended_at" TIMESTAMPTZ,
    "active" BOOLEAN,
    "version" BIGINT
);
CREATE TABLE IF NOT EXISTS "consultations" (
    "consultation_id" UUID PRIMARY KEY,
    "customer_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "pipeline_stage" TEXT,
    "customer_model" TEXT,
    "owner_sales_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "contact_name" TEXT,
    "phone" TEXT,
    "email" TEXT,
    "requirement_summary" TEXT,
    "product_interest" TEXT,
    "estimated_quantity" BIGINT,
    "requested_deadline" DATE,
    "design_source" TEXT,
    "design_readiness" TEXT,
    "technical_adjustment_required" BOOLEAN,
    "proposal_milestone" TEXT,
    "lost_reason" TEXT,
    "lost_note" TEXT,
    "stage_entered_at" TIMESTAMPTZ,
    "version" BIGINT,
    "created_at" TIMESTAMPTZ,
    "updated_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "lead_design_links" (
    "lead_design_link_id" UUID PRIMARY KEY,
    "consultation_id" UUID REFERENCES "consultations" ("consultation_id") DEFERRABLE INITIALLY DEFERRED,
    "design_id" UUID REFERENCES "designs" ("design_id") DEFERRABLE INITIALLY DEFERRED,
    "design_scope" TEXT,
    "version" BIGINT,
    "created_at" TIMESTAMPTZ,
    "updated_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "stage_histories" (
    "stage_history_id" UUID PRIMARY KEY,
    "consultation_id" UUID REFERENCES "consultations" ("consultation_id") DEFERRABLE INITIALLY DEFERRED,
    "from_stage" TEXT,
    "to_stage" TEXT,
    "actor_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "source" TEXT,
    "reason" TEXT,
    "reference" TEXT,
    "occurred_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "interaction_logs" (
    "interaction_id" UUID PRIMARY KEY,
    "consultation_id" UUID REFERENCES "consultations" ("consultation_id") DEFERRABLE INITIALLY DEFERRED,
    "type" TEXT,
    "channel" TEXT,
    "occurred_at" TIMESTAMPTZ,
    "summary" TEXT,
    "author_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "design_version_id" UUID REFERENCES "design_versions" ("design_version_id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "internal_notes" (
    "note_id" UUID PRIMARY KEY,
    "consultation_id" UUID REFERENCES "consultations" ("consultation_id") DEFERRABLE INITIALLY DEFERRED,
    "text" TEXT,
    "author_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "pinned" BOOLEAN,
    "created_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "admin_reviews" (
    "review_id" UUID PRIMARY KEY,
    "consultation_id" UUID REFERENCES "consultations" ("consultation_id") DEFERRABLE INITIALLY DEFERRED,
    "type" TEXT,
    "requested_value" TEXT,
    "reason" TEXT,
    "status" TEXT,
    "requester_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "requested_at" TIMESTAMPTZ,
    "decider_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "decided_at" TIMESTAMPTZ,
    "decision_note" TEXT
);
