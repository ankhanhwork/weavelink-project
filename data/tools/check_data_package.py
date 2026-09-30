"""Check consistency across the WeaveLink logical model, ERD, schema and seed.

This is a repository-data validation helper. It does not choose an application
stack or mutate any source file.
"""

from __future__ import annotations

import csv
import re
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
SEED = DATA / "seed"
SCHEMA = DATA / "schema"


def csv_tables() -> set[str]:
    tables: set[str] = set()
    for path in SEED.glob("*.csv"):
        with path.open(encoding="utf-8", newline="") as handle:
            header = next(csv.reader(handle), None)
        if not header:
            raise AssertionError(f"seed file has no header: {path.name}")
        tables.add(path.stem.split("_", 1)[1])
    return tables


def schema_tables() -> set[str]:
    tables: set[str] = set()
    for path in SCHEMA.glob("schema-MFG-*.sql"):
        text = path.read_text(encoding="utf-8")
        tables.update(re.findall(r'CREATE TABLE IF NOT EXISTS "(\w+)"', text))
    return tables


def main() -> None:
    logical_model = (DATA / "04-data-model.md").read_text(encoding="utf-8")
    catalogue = set(re.findall(r"^\| `(\w+)` \|", logical_model, flags=re.MULTILINE))
    erd = (DATA / "03-erd.mmd").read_text(encoding="utf-8").strip()
    embedded = re.search(r"```mermaid\n(.*?)\n```", logical_model, flags=re.DOTALL)
    if embedded is None or embedded.group(1).strip() != erd:
        raise AssertionError("embedded Mermaid ERD differs from data/03-erd.mmd")

    relationships = []
    entities: set[str] = set()
    for line in erd.splitlines():
        match = re.match(r"\s+(\w+)\s+([|o{}]+(?:--|\.\.)[|o{}]+)\s+(\w+)\s*:", line)
        if match:
            entities.update((match.group(1), match.group(3)))
            relationships.append(match.groups())

    seed = csv_tables()
    schema = schema_tables()
    generated = runpy.run_path(str(DATA / "tools" / "generate_sqlite_artifacts.py"))
    owners: dict[str, list[str]] = generated["OWNERS"]
    owner_tables = [table for tables in owners.values() for table in tables]

    assert len(catalogue) == 66, f"logical catalogue count is {len(catalogue)}, expected 66"
    assert len(entities) == 66, f"ERD entity count is {len(entities)}, expected 66"
    assert len(relationships) == 86, f"ERD relationship count is {len(relationships)}, expected 86"
    assert catalogue == seed == schema, "logical model, seed and schema tables must match exactly"
    assert len(owner_tables) == len(set(owner_tables)), "a table has more than one owner module"
    assert set(owner_tables) == seed, "module ownership does not cover every seed table exactly once"

    schema_text = "\n".join(path.read_text(encoding="utf-8") for path in SCHEMA.glob("schema-MFG-*.sql"))
    for table in ("quotes", "orders"):
        table_sql = re.search(rf'CREATE TABLE IF NOT EXISTS "{table}" \((.*?)\n\);', schema_text, flags=re.DOTALL)
        assert table_sql and '"phone" TEXT NOT NULL' in table_sql.group(1), f"{table}.phone must be validated as TEXT"
    for table, column in (("users", "email"), ("staff_accounts", "user_id"), ("products", "sku"), ("orders", "order_number")):
        table_sql = re.search(rf'CREATE TABLE IF NOT EXISTS "{table}" \((.*?)\n\);', schema_text, flags=re.DOTALL)
        assert table_sql and f'"{column}"' in table_sql.group(1) and "UNIQUE" in table_sql.group(1), (
            f"{table}.{column} must retain its documented unique constraint"
        )

    print("PASS 66 catalogue/ERD/schema/seed tables agree")
    print("PASS 86 Mermaid relationships and embedded ERD agree")
    print("PASS exactly one owner module covers every persisted table")
    print("PASS phone text and documented unique schema constraints are present")


if __name__ == "__main__":
    main()
