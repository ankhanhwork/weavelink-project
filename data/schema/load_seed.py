"""Create a SQLite validation database and load deterministic seed CSV files."""

from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = Path(__file__).resolve().parent
SEED = ROOT / "data" / "seed"


def quote_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, required=True, help="SQLite database file to create")
    args = parser.parse_args()
    args.database.parent.mkdir(parents=True, exist_ok=True)
    if args.database.exists():
        args.database.unlink()

    connection = sqlite3.connect(args.database)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        for schema_file in sorted(SCHEMA.glob("schema-MFG-*.sql")):
            connection.executescript(schema_file.read_text(encoding="utf-8"))
        connection.execute("BEGIN")
        for csv_file in sorted(SEED.glob("*.csv")):
            table = csv_file.stem.split("_", 1)[1]
            with csv_file.open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                columns = reader.fieldnames
                if not columns:
                    raise ValueError(f"Seed file has no header: {csv_file}")
                sql = "INSERT INTO " + quote_identifier(table) + " (" + ", ".join(quote_identifier(column) for column in columns) + ") VALUES (" + ", ".join("?" for _ in columns) + ")"
                rows = [tuple(row[column] or None for column in columns) for row in reader]
                connection.executemany(sql, rows)
        connection.commit()
        violations = connection.execute("PRAGMA foreign_key_check").fetchall()
        if violations:
            raise RuntimeError(f"Foreign-key validation failed: {violations[:3]}")
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
    print("PASS SQLite schema creation and filename-order seed load.")


if __name__ == "__main__":
    main()
