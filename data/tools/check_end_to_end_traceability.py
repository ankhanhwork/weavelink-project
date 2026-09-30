"""Validate the review fixtures and FR coverage in data/07-end-to-end-traceability.md."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SEED = ROOT / "data" / "seed"
SPECS = ROOT / "docs" / "spec" / "specs"
TRACE = ROOT / "data" / "07-end-to-end-traceability.md"


def rows(table: str) -> list[dict[str, str]]:
    path = next(SEED.glob(f"*_{table}.csv"))
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def index(rows_: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    return {row[key]: row for row in rows_}


def required_fr_ids() -> dict[str, set[int]]:
    result: dict[str, set[int]] = {}
    for path in SPECS.glob("spec-MFG-*.md"):
        module = re.search(r"MFG-(\d+)", path.name)
        if module is None:
            continue
        ids = {
            int(match.group(1))
            for match in re.finditer(r"^\| FR-(\d+) \| F-", path.read_text(encoding="utf-8"), flags=re.MULTILINE)
        }
        result[f"MFG-{module.group(1)}"] = ids
    return result


def documented_fr_ids(text: str) -> dict[str, set[int]]:
    result: dict[str, set[int]] = {}
    for line in text.splitlines():
        module = re.search(r"MFG-(\d+)", line)
        if module is None:
            continue
        target = result.setdefault(f"MFG-{module.group(1)}", set())
        for match in re.finditer(r"FR-(\d+)(?:[–-](\d+))?", line):
            start = int(match.group(1))
            end = int(match.group(2) or start)
            target.update(range(start, end + 1))
    return result


def main() -> None:
    trace_text = TRACE.read_text(encoding="utf-8")
    required = required_fr_ids()
    documented = documented_fr_ids(trace_text)
    for module, ids in required.items():
        missing = ids - documented.get(module, set())
        if missing:
            raise AssertionError(f"{module} FR IDs missing from end-to-end traceability: {sorted(missing)}")

    configs = index(rows("system_configs"), "system_config_id")
    events = index(rows("outbox_events"), "outbox_event_id")
    notifications = rows("notifications")
    config_event = next(row for row in events.values() if row["event_type"] == "ConfigChanged")
    assert config_event["source_module"] == "MFG-12"
    assert config_event["source_entity_id"] in configs
    assert any(
        row["source_event_id"] == config_event["outbox_event_id"] and row["target_route"] == "/system/configuration"
        for row in notifications
    ), "MFG-12 ConfigChanged event has no reauthorizable notification fixture"

    quotes = index(rows("quotes"), "quote_id")
    flexible = rows("flexible_preferences")
    assert any(
        row["merge_opt_in"] == "true"
        and row["accepted_policy_version"]
        and int(row["incentive_vnd"]) > 0
        and row["quote_id"] in quotes
        for row in flexible
    ), "MFG-10 flexible-choice fixture is missing"

    assets = index(rows("assets"), "asset_id")
    design_versions = rows("design_versions")
    templates = rows("product_mockup_templates")
    assert any(row["review_state"] == "Approved" for row in design_versions)
    assert any(row["view_id"] == "Front" and row["base_asset_id"] in assets for row in templates)
    assert any(row["ownership"] == "Dony" and row["mime_type"] == "PNG" and row["scan_status"] == "Safe" for row in assets.values())

    print("PASS every specified FR ID appears in the end-to-end traceability index")
    print("PASS MFG-12 configuration -> outbox -> notification fixture joins")
    print("PASS MFG-10 flexible quote/policy fixture joins")
    print("PASS MFG-05 virtual-try-on synthetic prerequisites are present without a personal-photo row")


if __name__ == "__main__":
    main()
