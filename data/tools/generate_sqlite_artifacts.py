"""Generate SQLite validation-schema artefacts from the deterministic seed package.

This is documentation and validation support for the Session 7 data package, not
application code. It creates one schema file and one data-model index per module.
"""

from __future__ import annotations

import ast
import csv
import json
import uuid
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SEED = ROOT / "data" / "seed"
SCHEMA = ROOT / "data" / "schema"
MODELS = ROOT / "data"
GENERATOR = SEED / "generate_seed.py"

OWNERS = {
    "MFG-01": ["users", "sessions", "one_time_tokens", "notifications", "outbox_events"],
    "MFG-02": [],
    "MFG-03": ["staff_accounts", "staff_invitations"],
    "MFG-04": ["products", "product_versions", "product_sizes", "product_colors", "material_profiles", "product_materials", "print_methods", "volume_pricing_tiers", "product_options", "print_areas", "product_images", "search_synonym_sets"],
    "MFG-05": ["assets", "designs", "design_versions", "design_placements", "design_requests", "design_request_assets", "design_feedback", "design_feedback_assets", "staff_replies", "staff_reply_assets", "customer_approvals", "customer_provided_confirmations", "product_mockup_templates"],
    "MFG-06": ["quotes", "quote_size_quantities", "orders", "order_size_quantities", "order_quote_cycles", "production_samples", "payment_transactions", "refund_records", "order_timeline_events"],
    "MFG-07": [],
    "MFG-08": ["customer_assignments", "consultations", "lead_design_links", "stage_histories", "interaction_logs", "internal_notes", "admin_reviews"],
    "MFG-09": ["contract_templates", "contracts", "signature_evidence"],
    "MFG-10": ["flexible_preferences", "production_readiness", "individual_production_plans", "production_capacity_profiles", "production_batches", "batch_memberships"],
    "MFG-11": ["product_entries", "journey_intents", "analytics_events", "analytics_results", "export_requests"],
    "MFG-12": ["audit_events", "backups", "system_configs", "restore_journals"],
}


def fk_rows() -> list[tuple[str, str, str, str]]:
    tree = ast.parse(GENERATOR.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.For) and isinstance(node.target, ast.Tuple):
            for child in ast.walk(node):
                if isinstance(child, ast.List):
                    rows = []
                    for item in child.elts:
                        if isinstance(item, ast.Tuple) and len(item.elts) == 4 and all(isinstance(x, ast.Constant) and isinstance(x.value, str) for x in item.elts):
                            rows.append(tuple(x.value for x in item.elts))
                    if len(rows) > 40:
                        return rows
    raise RuntimeError("Could not locate foreign-key declarations in seed generator")


def headers() -> dict[str, list[str]]:
    result = {}
    for file in SEED.glob("*.csv"):
        with file.open(encoding="utf-8", newline="") as handle:
            result[file.stem.removeprefix(file.stem[:3]) if len(file.stem) > 3 and file.stem[:2].isdigit() and file.stem[2] == "_" else file.stem] = next(csv.reader(handle))
    return result


def sql_type(column: str, values: list[str]) -> str:
    filled = [value for value in values if value != ""]
    if column.endswith("_json"):
        return "JSONB"
    if column.endswith("_id") and filled and all(is_uuid(value) for value in filled):
        return "UUID"
    if filled and all(value in {"true", "false"} for value in filled):
        return "BOOLEAN"
    if filled and all(value.isdigit() or (value.startswith("-") and value[1:].isdigit()) for value in filled):
        return "BIGINT"
    if filled and all(value.replace(".", "", 1).isdigit() for value in filled) and any("." in value for value in filled):
        return "NUMERIC"
    if filled and all(len(value) == 10 and value[4] == "-" and value[7] == "-" for value in filled):
        return "DATE"
    if filled and all("T" in value and value.endswith("Z") for value in filled):
        return "TIMESTAMPTZ"
    return "TEXT"


def is_uuid(value: str) -> bool:
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False


def table_sql(table: str, columns: list[str], fks: list[tuple[str, str, str, str]]) -> str:
    file = SEED / f"{table}.csv"
    if not file.exists():
        file = next(SEED.glob(f"*_{table}.csv"))
    with file.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    defs = []
    for index, column in enumerate(columns):
        kind = sql_type(column, [row[column] for row in rows])
        suffix = " PRIMARY KEY" if index == 0 else ""
        for child, child_column, parent, parent_column in fks:
            if child == table and child_column == column:
                suffix += f' REFERENCES "{parent}" ("{parent_column}") DEFERRABLE INITIALLY DEFERRED'
        defs.append(f'    "{column}" {kind}{suffix}')
    return 'CREATE TABLE IF NOT EXISTS "' + table + '" (\n' + ",\n".join(defs) + "\n);\n"


def seed_order(tables: set[str], fks: list[tuple[str, str, str, str]]) -> list[str]:
    dependencies = defaultdict(set)
    for child, _column, parent, _parent_column in fks:
        if child != parent:
            dependencies[child].add(parent)
    remaining = set(tables)
    ordered = []
    while remaining:
        ready = sorted(name for name in remaining if not (dependencies[name] & remaining))
        if not ready:
            ready = [sorted(remaining)[0]]
        for name in ready:
            remaining.remove(name)
            ordered.append(name)
    return ordered


def module_document(module: str, tables: list[str], fks: list[tuple[str, str, str, str]]) -> str:
    relationships = [row for row in fks if row[0] in tables or row[2] in tables]
    title = module + " Module Data Model"
    lines = [f"# Data Model and Mockup Data: {title}", "", "## 1. Scope", "", f"This module index assigns data ownership for {module}. The canonical full attribute catalogue remains `data/04-data-model.md`; this file records which tables {module} owns and the cross-module references that must remain consistent with it.", "", "## 2. Owned entities", "", "| Table | Ownership decision | Canonical attributes and constraints |", "|---|---|---|"]
    if tables:
        lines += [f"| `{table}` | Owned by {module}; no other module owns this entity. | [`data/04-data-model.md`](04-data-model.md) |" for table in tables]
    else:
        lines.append(f"| None | {module} has no independently persisted entity in the approved model. | Cross-module references only. |")
    lines += ["", "## 3. Relationships and cross-module references", "", "| Referencing table and field | Referenced table and field | Check |", "|---|---|---|"]
    if relationships:
        lines += [f"| `{child}.{column}` | `{parent}.{parent_column}` | Foreign key in `data/schema/`; validate after every seed regeneration. |" for child, column, parent, parent_column in relationships]
    else:
        lines.append("| None | None | No persisted relationship is owned by this module. |")
    lines += ["", "## 4. Schema and seed evidence", "", f"The SQLite tables owned by this module are created in [`data/schema/schema-{module}.sql`](schema/schema-{module}.sql). Generated seed rows are loaded in filename order using `data/schema/load_seed.py` and checked with SQLite foreign keys.", "", "## 5. Traceability and review", "", "Each table and attribute traces to the cited module specifications in `data/04-data-model.md`. Any future entity, attribute, relationship, normalization exception, or business-rule enforcement decision must be recorded in both the canonical model and this module index.", ""]
    return "\n".join(lines)


def main() -> None:
    table_headers = headers()
    tables = set(table_headers)
    fks = fk_rows()
    if set(sum(OWNERS.values(), [])) != tables:
        raise RuntimeError("Module ownership map does not cover every seed table exactly once")
    SCHEMA.mkdir(exist_ok=True)
    for module, owned in OWNERS.items():
        sql = [f"-- SQLite validation schema for {module}.\n"]
        sql.extend(table_sql(table, table_headers[table], fks) for table in owned)
        (SCHEMA / f"schema-{module}.sql").write_text("".join(sql), encoding="utf-8", newline="\n")
        (MODELS / f"data-model-{module}.md").write_text(module_document(module, owned, fks), encoding="utf-8", newline="\n")
    order = seed_order(tables, fks)
    (SEED / "seed-order.json").write_text(json.dumps({name: index for index, name in enumerate(order, 1)}, indent=2) + "\n", encoding="utf-8")
    print(f"Generated 12 module model indexes, 12 SQLite schema files, and seed order for {len(order)} tables.")


if __name__ == "__main__":
    main()
