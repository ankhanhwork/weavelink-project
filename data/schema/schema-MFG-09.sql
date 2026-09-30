-- SQLite validation schema for MFG-09.
CREATE TABLE IF NOT EXISTS "contract_templates" (
    "contract_template_id" UUID PRIMARY KEY,
    "template_family_id" UUID,
    "name" TEXT,
    "version" BIGINT,
    "structured_body" TEXT,
    "status" TEXT,
    "created_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "contracts" (
    "contract_id" UUID PRIMARY KEY,
    "order_id" UUID REFERENCES "orders" ("order_id") DEFERRABLE INITIALLY DEFERRED,
    "contract_template_id" UUID REFERENCES "contract_templates" ("contract_template_id") DEFERRABLE INITIALLY DEFERRED,
    "buyer_type" TEXT,
    "buyer_legal_name" TEXT,
    "buyer_tax_id" TEXT,
    "billing_address" TEXT,
    "approved_design_version_id" UUID REFERENCES "design_versions" ("design_version_id") DEFERRABLE INITIALLY DEFERRED,
    "approved_sample_id" UUID REFERENCES "production_samples" ("sample_id") DEFERRABLE INITIALLY DEFERRED,
    "contract_total_vnd" BIGINT,
    "deposit_percent" BIGINT,
    "deposit_due_vnd" BIGINT,
    "balance_due_vnd" BIGINT,
    "balance_due_rule" TEXT,
    "payment_policy_version" TEXT,
    "version" BIGINT,
    "template_version" BIGINT,
    "content_hash" TEXT,
    "pdf_asset_id" UUID REFERENCES "assets" ("asset_id") DEFERRABLE INITIALLY DEFERRED,
    "status" TEXT,
    "ready_at" TIMESTAMPTZ,
    "signed_at" TIMESTAMPTZ,
    "voided_at" TIMESTAMPTZ
);
CREATE TABLE IF NOT EXISTS "signature_evidence" (
    "signature_evidence_id" UUID PRIMARY KEY,
    "contract_id" UUID REFERENCES "contracts" ("contract_id") DEFERRABLE INITIALLY DEFERRED,
    "signer_user_id" UUID REFERENCES "users" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "typed_name" TEXT,
    "consent_text_version" TEXT,
    "contract_hash" TEXT,
    "server_timestamp" TIMESTAMPTZ,
    "observed_ip" TEXT,
    "user_agent" TEXT,
    "challenge_digest" TEXT
);
