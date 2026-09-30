-- SQLite validation schema for MFG-11.
CREATE TABLE IF NOT EXISTS "product_entries" (
    "product_entry_id" UUID PRIMARY KEY,
    "owner_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "product_id" UUID REFERENCES "products" ("product_id") DEFERRABLE INITIALLY DEFERRED,
    "source" TEXT,
    "entered_at" TIMESTAMPTZ,
    "product_version" BIGINT
);
CREATE TABLE IF NOT EXISTS "journey_intents" (
    "journey_intent_id" UUID PRIMARY KEY,
    "owner_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "product_entry_id" UUID REFERENCES "product_entries" ("product_entry_id") DEFERRABLE INITIALLY DEFERRED,
    "intent_type" TEXT,
    "parent_intent_id" UUID REFERENCES "journey_intents" ("journey_intent_id") DEFERRABLE INITIALLY DEFERRED,
    "created_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "analytics_events" (
    "analytics_event_id" UUID PRIMARY KEY,
    "schema_version" BIGINT,
    "event_name" TEXT,
    "source_kind" TEXT,
    "entity_type" TEXT,
    "entity_id" UUID,
    "occurred_at" TIMESTAMPTZ,
    "received_at" TIMESTAMPTZ,
    "actor_kind" TEXT,
    "customer_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "product_entry_id" UUID REFERENCES "product_entries" ("product_entry_id") DEFERRABLE INITIALLY DEFERRED,
    "journey_intent_id" UUID REFERENCES "journey_intents" ("journey_intent_id") DEFERRABLE INITIALLY DEFERRED,
    "product_id" UUID REFERENCES "products" ("product_id") DEFERRABLE INITIALLY DEFERRED,
    "design_id" UUID REFERENCES "designs" ("design_id") DEFERRABLE INITIALLY DEFERRED,
    "quote_id" UUID REFERENCES "quotes" ("quote_id") DEFERRABLE INITIALLY DEFERRED,
    "order_id" UUID REFERENCES "orders" ("order_id") DEFERRABLE INITIALLY DEFERRED,
    "request_id" TEXT REFERENCES "design_requests" ("design_request_id") DEFERRABLE INITIALLY DEFERRED,
    "contract_id" UUID REFERENCES "contracts" ("contract_id") DEFERRABLE INITIALLY DEFERRED,
    "bound_versions_json" JSONB,
    "sample_cycle" BIGINT,
    "reason_code" TEXT,
    "source_event_id" UUID,
    "dataset_flags_json" JSONB
);
CREATE TABLE IF NOT EXISTS "analytics_results" (
    "analytics_result_id" UUID PRIMARY KEY,
    "query_context_json" JSONB,
    "unit" TEXT,
    "template" TEXT,
    "cohort" TEXT,
    "observation_mode" TEXT,
    "eligible_count" BIGINT,
    "immature_count" TEXT,
    "cutoff" TIMESTAMPTZ,
    "timezone" TEXT,
    "generated_at" TIMESTAMPTZ,
    "expires_at" TIMESTAMPTZ,
    "source_watermark" TEXT,
    "definition_version" TEXT,
    "coverage_json" JSONB,
    "metrics_json" JSONB
);
CREATE TABLE IF NOT EXISTS "export_requests" (
    "export_request_id" UUID PRIMARY KEY,
    "actor_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "analytics_result_id" UUID REFERENCES "analytics_results" ("analytics_result_id") DEFERRABLE INITIALLY DEFERRED,
    "format" TEXT,
    "dataset" TEXT,
    "watermark" TEXT,
    "created_at" TIMESTAMPTZ,
    "completed_at" TIMESTAMPTZ,
    "expires_at" TIMESTAMPTZ,
    "state" TEXT,
    "private_asset_id" UUID REFERENCES "assets" ("asset_id") DEFERRABLE INITIALLY DEFERRED,
    "row_count" BIGINT,
    "safe_error" TEXT
);
