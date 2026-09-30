"""Generate deterministic synthetic WeaveLink seed CSV files.

Run from the repository root:
    python data/seed/generate_seed.py

The generator uses only Python's standard library, a fixed UUID namespace and
fixed timestamps. It never reads or emits real personal data. Every assertion
runs before a CSV is written, so an invalid in-memory fixture cannot replace
the reviewed seed package.
"""

from __future__ import annotations

import csv
import json
import uuid
from datetime import datetime
from pathlib import Path


OUT = Path(__file__).resolve().parent
NS = uuid.UUID("1ebc511e-1c37-4ca6-a15d-a644e9ee9cf0")
ORDER_FILE = OUT / "seed-order.json"


def uid(kind: str, number: int) -> str:
    return str(uuid.uuid5(NS, f"weavelink:{kind}:{number}"))


def js(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def write_table(name: str, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise AssertionError(f"{name}: table must have a header and at least one supported row")
    columns = list(rows[0])
    for row in rows:
        if list(row) != columns:
            raise AssertionError(f"{name}: inconsistent column order")
    rows.sort(key=lambda row: str(row[columns[0]]))
    if not ORDER_FILE.exists():
        raise AssertionError(f"missing deterministic seed order file: {ORDER_FILE}")
    order = json.loads(ORDER_FILE.read_text(encoding="utf-8"))
    if name not in order:
        raise AssertionError(f"missing seed order for table: {name}")
    filename = f"{int(order[name]):02d}_{name}.csv"
    with (OUT / filename).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def base_rows(kind: str, count: int = 7) -> range:
    return range(1, count + 1)


def generate() -> dict[str, list[dict[str, object]]]:
    tables: dict[str, list[dict[str, object]]] = {}

    user_names = [
        "Nguyễn Minh An", "Trần Gia Bình", "Lê Hoài Châu", "Phạm Đức Duy",
        "Võ Khánh Giang", "Đặng Thu Hà", "Bùi Nhật Khang", "Đỗ Mai Lan",
        "Hồ Nam Phương", "Tạ Quang Sơn",
    ]
    tables["users"] = [
        {
            "user_id": uid("user", i),
            "email": f"demo.user{i:02d}@example.invalid",
            "full_name": name,
            "password_hash": f"synthetic-hash-{i:02d}",
            "customer_capability": "true" if i >= 4 else "false",
            "verified_at": "2026-08-01T02:00:00Z",
            "active": "false" if i == 9 else "true",
            "closed_at": "2026-09-20T03:00:00Z" if i == 9 else "",
            "anonymized_at": "",
            "version": 2 if i == 9 else 1,
            "created_at": f"2026-07-{i:02d}T01:00:00Z",
            "updated_at": "2026-09-20T03:00:00Z" if i == 9 else f"2026-08-{i:02d}T02:00:00Z",
        }
        for i, name in enumerate(user_names, 1)
    ]

    roles = ["SalesAdmin", "Sales", "SystemAdmin", "Sales", "Sales", "Sales"]
    states = ["Active", "Active", "Active", "Suspended", "Invited", "Deleted"]
    tables["staff_accounts"] = [
        {
            "staff_account_id": uid("staff", i), "user_id": uid("user", i),
            "role": roles[i - 1], "status": states[i - 1],
            "invited_at": "2026-07-01T01:00:00Z", "activated_at": "" if i == 5 else "2026-07-02T01:00:00Z",
         "deleted_at": "2026-09-20T03:00:00Z" if i == 6 else "", "version": 1,
        }
        for i in range(1, 7)
    ]
    tables["sessions"] = [
        {"session_id": uid("session", i), "user_id": uid("user", i), "token_hash": f"session-hash-{i}",
         "idle_expires_at": "2026-09-28T04:30:00Z", "absolute_expires_at": "2026-09-29T04:00:00Z",
         "revoked_at": "2026-09-28T04:10:00Z" if i == 7 else "", "created_at": "2026-09-28T04:00:00Z"}
        for i in base_rows("session")
    ]
    token_specs = [
        ("EmailVerification", "2026-09-29T03:30:00Z"),
        ("PasswordReset", "2026-09-28T04:00:00Z"),
        ("EmailChange", "2026-09-29T03:30:00Z"),
        ("PasswordReset", "2026-09-28T04:00:00Z"),
        ("StaffInvitation", "2026-09-30T03:30:00Z"),
        ("PasswordReset", "2026-09-28T04:00:00Z"),
        ("EmailVerification", "2026-09-29T03:30:00Z"),
    ]
    tables["one_time_tokens"] = [
        {"token_id": uid("token", i), "user_id": uid("user", (i % 10) + 1), "purpose": purpose,
         "portal": "Staff" if i == 5 else "Customer", "token_hash": f"token-hash-{i}",
         "expires_at": expires_at, "consumed_at": "2026-09-28T04:05:00Z" if i in (2, 5) else "",
         "created_at": "2026-09-28T03:30:00Z"}
        for i, (purpose, expires_at) in enumerate(token_specs, 1)
    ]
    outbox_specs = [
        ("MFG-01", "User", uid("user", 1), "VerificationQueued", uid("user", 1), ""),
        ("MFG-01", "User", uid("user", 2), "PasswordResetQueued", uid("user", 2), ""),
        ("MFG-06", "Order", uid("order", 1), "OrderCreated", uid("user", 5), "/orders/" + uid("order", 1)),
        ("MFG-06", "Order", uid("order", 4), "SampleShipped", uid("user", 6), "/orders/" + uid("order", 4)),
        ("MFG-09", "Contract", uid("contract", 1), "ContractReady", uid("user", 7), "/contracts/" + uid("contract", 1)),
        ("MFG-06", "PaymentTransaction", uid("payment", 1), "DepositSucceeded", uid("user", 8), "/orders/" + uid("order", 5)),
        ("MFG-07", "Order", uid("order", 7), "OrderCancelled", uid("user", 9), "/orders/" + uid("order", 7)),
        ("MFG-12", "SystemConfig", uid("config", 1), "ConfigChanged", uid("user", 3), "/system/configuration"),
    ]
    tables["outbox_events"] = [
        {"outbox_event_id": uid("outbox", i), "source_module": source_module,
         "source_entity_type": source_entity_type, "source_entity_id": source_entity_id,
         "event_type": event_type,
         "payload_json": js({"changed_keys": ["shipping_vnd"]} if event_type == "ConfigChanged" else {"synthetic": True, "sequence": i}),
         "delivery_state": "Failed" if event_type == "OrderCancelled" else "Delivered",
         "created_at": f"2026-09-{10+i:02d}T02:00:00Z", "delivered_at": "" if event_type == "OrderCancelled" else f"2026-09-{10+i:02d}T02:01:00Z"}
        for i, (source_module, source_entity_type, source_entity_id, event_type, _recipient_user_id, _target_route) in enumerate(outbox_specs, 1)
    ]
    tables["notifications"] = [
        {"notification_id": uid("notification", i), "recipient_user_id": recipient_user_id,
         "source_event_id": uid("outbox", i), "type": tables["outbox_events"][i-1]["event_type"],
         "title": f"Thông báo quy trình {i}", "body": f"Cập nhật giả lập an toàn số {i}.",
         "target_route": target_route,
         "email_delivery_state": "Failed" if event_type == "OrderCancelled" else "Delivered", "created_at": f"2026-09-{10+i:02d}T02:01:00Z",
         "read_at": f"2026-09-{10+i:02d}T03:00:00Z" if i <= 3 else ""}
        for i, (_source_module, _source_entity_type, _source_entity_id, event_type, recipient_user_id, target_route) in enumerate(outbox_specs, 1)
    ]
    tables["staff_invitations"] = [
        {"invitation_id": uid("invitation", i), "staff_account_id": uid("staff", ((i-1)%5)+1),
         "email_snapshot": f"staff{i:02d}@example.invalid", "role_snapshot": roles[(i-1)%5],
         "token_hash": f"invitation-hash-{i}", "expires_at": "2026-09-30T02:00:00Z",
         "accepted_at": "2026-09-28T02:00:00Z" if i <= 3 else "", "delivery_status": "Failed" if i == 7 else "Delivered", "version": 1}
        for i in base_rows("invitation")
    ]

    # Assets and catalogue. DEMO-TEE-001 values come directly from MFG-04 §9.
    tables["assets"] = [
        {"asset_id": uid("asset", i), "owner_user_id": "" if i <= 12 else uid("user", 4 + (i % 6)),
         "ownership": "Dony" if i <= 12 else "User", "mime_type": "PDF" if i in (25, 26, 27) else "PNG",
         "scan_status": "Rejected" if i == 30 else "Safe", "storage_key": f"synthetic/assets/{i:03d}",
         "size_bytes": 10485760 if i == 29 else 120000 + i, "created_at": f"2026-08-{((i-1)%28)+1:02d}T01:00:00Z"}
        for i in range(1, 31)
    ]
    product_names = ["Áo thun cổ tròn", "Áo polo doanh nghiệp", "Sơ mi công sở", "Áo khoác đồng phục", "Áo bảo hộ phản quang", "Quần bảo hộ lao động"]
    skus = ["DEMO-TEE-001", "DEMO-POLO-002", "DEMO-SHIRT-003", "DEMO-JACKET-004", "DEMO-WORK-005", "DEMO-PANTS-006"]
    branches = ["Đồng phục"] * 4 + ["Đồ bảo hộ lao động"] * 2
    statuses = ["Published", "Published", "Published", "Hidden", "Draft", "Archived"]
    tables["products"] = [
        {"product_id": uid("product", i), "sku": skus[i-1], "status": statuses[i-1], "current_version": 1,
         "created_at": f"2026-06-{i:02d}T01:00:00Z", "updated_at": f"2026-09-{i:02d}T01:00:00Z"}
        for i in range(1, 7)
    ]
    tables["product_versions"] = [
        {"product_version_id": uid("product_version", i), "product_id": uid("product", i), "version": 1,
         "name": product_names[i-1], "description": f"Mẫu may theo đơn giả lập cho {product_names[i-1].lower()}.",
         "category": ["Thun", "Polo", "Sơ mi", "Khoác", "Bảo hộ", "Bảo hộ"][i-1], "branch": branches[i-1],
         "sub_type": ["Cổ tròn", "Có cổ", "Dài tay", "Áo khoác", "Phản quang", "Quần dài"][i-1],
         "base_unit_price_vnd": 150000 + (i-1)*25000, "min_order_quantity": 10, "max_units_per_order": 10000,
         "keywords": "đồng phục may theo đơn" if i <= 4 else "bảo hộ lao động", "created_at": f"2026-06-{i:02d}T01:00:00Z"}
        for i in range(1, 7)
    ]
    tables["product_sizes"] = [
        {"product_size_id": uid("product_size", p*10+s), "product_version_id": uid("product_version", p), "size_label": label, "display_order": s}
        for p in range(1, 7) for s, label in enumerate(["S", "M", "L", "XL"], 1)
    ]
    colors = ["White", "Navy", "Black"]
    tables["product_colors"] = [
        {"product_color_id": uid("product_color", p*10+c), "product_version_id": uid("product_version", p), "color_label": label, "display_order": c}
        for p in range(1, 7) for c, label in enumerate(colors, 1)
    ]
    material_labels = ["100% cotton", "65/35 cotton-polyester", "Polyester chống nhăn", "Vải kaki bảo hộ", "Vải phản quang"]
    tables["material_profiles"] = [
        {"material_profile_id": uid("material", i), "material_label": label,
         "durability": "High" if i >= 3 else "Medium", "breathability": "High" if i == 1 else "Medium",
         "wash_durability": "High", "wrinkle_resistance": "High" if i >= 2 else "Medium",
         "abrasion_resistance": "High" if i >= 4 else "Medium", "stain_resistance": "High" if i >= 4 else "Medium",
         "suited_occupations_json": js(["văn phòng"] if i < 4 else ["xưởng sản xuất"]),
         "suited_seasons_json": js(["quanh năm"]), "pros_json": js(["dữ liệu demo có căn cứ kỹ thuật"]),
         "cons_json": js(["cần xác nhận mẫu thực tế"])}
        for i, label in enumerate(material_labels, 1)
    ]
    tables["product_materials"] = [
        {"product_material_id": uid("product_material", p*10+m), "product_version_id": uid("product_version", p),
         "material_profile_id": uid("material", m), "material_label_snapshot": material_labels[m-1],
         "option_surcharge_vnd": 0 if m == 1 else 10000*m}
        for p in range(1, 7) for m in ([1, 2] if p <= 4 else [4, 5])
    ]
    tables["print_methods"] = [
        {"print_method_id": uid("print_method", i), "name": name, "multicolor_support": multi,
         "fine_detail_support": fine, "notes": note}
        for i, (name, multi, fine, note) in enumerate([
            ("Direct print", "true", "true", "Supported demo option from MFG-04 §9."),
            ("Embroidery", "true", "false", "Separate decoration referenced by MFG-10."),
        ], 1)
    ]
    tables["volume_pricing_tiers"] = [
        {"tier_id": uid("tier", p*10+t), "product_version_id": uid("product_version", p),
         "quantity_from": [1, 50, 200][t-1], "quantity_to": [49, 199, 10000][t-1],
         "unit_price_vnd": [150000, 130000, 110000][t-1] + (p-1)*25000}
        for p in range(1, 7) for t in range(1, 4)
    ]
    tables["product_options"] = [
        {"product_option_id": uid("option", p*10+side), "product_version_id": uid("product_version", p),
         "option_type": "PrintSide", "option_value": "Front" if side == 1 else "Back",
         "print_method_id": uid("print_method", 1), "option_surcharge_vnd": 15000 if side == 1 else 25000}
        for p in range(1, 7) for side in (1, 2)
    ]
    tables["print_areas"] = [
        {"print_area_id": uid("print_area", p*100+s*10+side), "product_version_id": uid("product_version", p),
         "size_label": size, "side": "Front" if side == 1 else "Back", "width_mm": "300.0", "height_mm": "400.0",
         "origin_x_mm": "0.0", "origin_y_mm": "0.0"}
        for p in range(1, 7) for s, size in enumerate(["S", "M", "L", "XL"], 1) for side in (1, 2)
    ]
    tables["product_images"] = [
        {"product_image_id": uid("product_image", p*10+n), "product_version_id": uid("product_version", p),
         "asset_id": uid("asset", (p-1)*2+n), "display_order": n}
        for p in range(1, 7) for n in (1, 2)
    ]
    tables["search_synonym_sets"] = [{
        "synonym_set_id": uid("synonym", 1), "version": 1,
        "entries_json": js({"somi": ["sơ mi"], "sm": ["sơ mi"], "bh": ["bảo hộ"], "pq": ["phản quang"], "white": ["trắng"]}),
        "updated_by_user_id": uid("user", 1), "updated_at": "2026-09-01T01:00:00Z",
    }]

    # Designs and collaboration.
    design_statuses = ["Saved", "Saved", "Delivered", "ProofDelivered", "Draft", "Delivered", "Saved"]
    tables["designs"] = [
        {"design_id": uid("design", i), "customer_id": uid("user", 4 + (i % 6)), "product_id": uid("product", ((i-1)%6)+1),
         "source_design_request_id": uid("design_request", i) if i in (3,4,6) else "", "status": design_statuses[i-1],
         "current_version": 3 if i == 4 else 1, "created_at": f"2026-08-{i:02d}T03:00:00Z", "updated_at": f"2026-09-{i:02d}T03:00:00Z"}
        for i in base_rows("design")
    ]
    design_versions = []
    for i in base_rows("design"):
        design_versions.append({"design_version_id": uid("design_version", i*10+1), "design_id": uid("design", i), "version": 1,
            "product_version_id": uid("product_version", ((i-1)%6)+1),
            "source": "DonyDesign" if i in (3,4,6) else "CustomerUploaded",
            "review_state": "Superseded" if i == 4 else "Approved", "uploader_user_id": uid("user", 2 if i in (3,4,6) else 4+(i%6)),
            "original_channel": "Email" if i in (3,4,6) else "", "change_note": "Bản thiết kế giả lập đã kiểm tra.",
            "preview_asset_id": uid("asset", 12+i), "created_at": f"2026-08-{i:02d}T04:00:00Z"})
    design_versions.append({"design_version_id": uid("design_version", 42), "design_id": uid("design", 4), "version": 2,
        "product_version_id": uid("product_version", 4), "source": "DonyTechnicalAdjustment", "review_state": "Draft",
        "uploader_user_id": uid("user", 2), "original_channel": "Email", "change_note": "Bản hiệu chỉnh đang chờ chia sẻ.",
        "preview_asset_id": uid("asset", 20), "created_at": "2026-09-10T04:00:00Z"})
    design_versions.append({"design_version_id": uid("design_version", 43), "design_id": uid("design", 4), "version": 3,
        "product_version_id": uid("product_version", 4), "source": "DonyDesign", "review_state": "SharedForReview",
        "uploader_user_id": uid("user", 2), "original_channel": "Email", "change_note": "Bản chia sẻ hiện tại đang chờ khách hàng duyệt.",
        "preview_asset_id": uid("asset", 21), "created_at": "2026-09-11T04:00:00Z"})
    tables["design_versions"] = design_versions
    tables["design_placements"] = [
        {"placement_id": uid("placement", i), "design_version_id": uid("design_version", i*10+1), "asset_id": uid("asset", 12+i),
         "side": "Front" if i % 2 else "Back", "x_mm": "15.0", "y_mm": "20.0", "width_mm": "70.0" if i == 1 else "120.0",
         "height_mm": "80.0", "processing_method": "Original"}
        for i in base_rows("placement")
    ]
    request_states = ["Submitted", "UnderReview", "Delivered", "InProgress", "Cancelled", "FeeProposed", "Rejected", "Approved", "Assigned"]
    tables["design_requests"] = [
        {"design_request_id": uid("design_request", i), "customer_id": uid("user", 4+(i%6)), "product_id": uid("product", ((i-1)%6)+1),
         "requirements": f"Yêu cầu thiết kế giả lập chi tiết cho mẫu số {i}, dùng nội dung tổng hợp.",
         "requested_deadline": "2026-10-15", "committed_due_at": "2026-10-12T10:00:00Z" if i in (3,4) else "",
         "complexity": "Complex" if i in (3,4,6) else ("Simple" if i in (2,8,9) else ""),
         "rationale": "Cần hiệu chỉnh kỹ thuật." if i in (3,4,6) else ("Đủ điều kiện xử lý đơn giản." if i in (2,8,9) else ""), "rejection_reason": "Ngoài phạm vi mẫu." if i == 7 else "",
         "assessed_by_staff_id": uid("staff", 1) if i >= 2 else "", "assessed_at": "2026-09-05T03:00:00Z" if i >= 2 else "",
         "fee_vnd": 200000 if i in (3,4,6) else (0 if i in (2,8,9) else ""), "proposal_version": 1 if i in (3,4,6) else "",
         "accepted_fee_version": 1 if i in (3,4) else "", "accepted_fee_vnd": 200000 if i in (3,4) else "",
         "accepted_by_user_id": uid("user", 4+(i%6)) if i in (3,4) else "", "accepted_at": "2026-09-06T03:00:00Z" if i in (3,4) else "",
         "fee_order_id": uid("order", 3) if i == 3 else "", "fee_allocation_version": 1 if i == 3 else "",
         "state": request_states[i-1], "assignee_staff_id": uid("staff", 2) if i in (3,4,9) else "", "version": 2 if i >= 2 else 1,
         "created_at": f"2026-09-{i:02d}T02:00:00Z"}
        for i in base_rows("design_request", 9)
    ]
    tables["design_request_assets"] = [
        {"design_request_asset_id": uid("request_asset", i), "design_request_id": uid("design_request", i),
         "asset_id": uid("asset", 12+i), "display_order": 1}
        for i in base_rows("request_asset", 9)
    ]
    tables["design_feedback"] = [
        {"feedback_id": uid("feedback", i), "design_version_id": uid("design_version", ((i-1)%7+1)*10+1),
         "author_user_id": uid("user", 4+(i%6)), "decision": "RevisionRequested",
         "change_request_text": f"Vui lòng điều chỉnh chi tiết bố cục giả lập số {i}.", "preferred_colour": colors[(i-1)%3],
         "additional_notes": "Giữ nguyên tỷ lệ logo.", "created_at": f"2026-09-{10+i:02d}T03:00:00Z", "idempotency_key": uid("feedback_key", i)}
        for i in base_rows("feedback")
    ]
    tables["design_feedback_assets"] = [
        {"design_feedback_asset_id": uid("feedback_asset", i), "feedback_id": uid("feedback", i),
         "asset_id": uid("asset", 12+i), "display_order": 1}
        for i in base_rows("feedback_asset")
    ]
    tables["staff_replies"] = [
        {"staff_reply_id": uid("reply", i), "feedback_id": uid("feedback", i), "author_staff_id": uid("staff", 2 if i % 2 else 1),
         "reply_text": f"Đã tiếp nhận yêu cầu điều chỉnh giả lập số {i}.", "created_at": f"2026-09-{10+i:02d}T04:00:00Z",
         "idempotency_key": uid("reply_key", i)} for i in base_rows("reply")
    ]
    tables["staff_reply_assets"] = [
        {"staff_reply_asset_id": uid("reply_asset", i), "staff_reply_id": uid("reply", i),
         "asset_id": uid("asset", 12+i), "display_order": 1}
        for i in base_rows("reply_asset")
    ]
    tables["customer_approvals"] = [
        {"approval_id": uid("approval", i), "design_version_id": uid("design_version", i*10+1), "customer_id": uid("user", 4+(i%6)),
         "approved_at": f"2026-09-{10+i:02d}T05:00:00Z", "request_version": 2, "idempotency_key": uid("approval_key", i)}
        for i in (1,2,3,5,6,7)
    ]
    tables["customer_provided_confirmations"] = [
        {"confirmation_id": uid("source_confirmation", i), "design_version_id": uid("design_version", i*10+1),
         "confirmer_user_id": uid("user", 4+(i%6)), "recorded_by_staff_id": uid("staff", 2), "original_channel": "Email",
         "source_evidence": f"Xác nhận nguồn tệp giả lập {i}.", "confirmed_at": f"2026-09-{10+i:02d}T05:30:00Z",
         "idempotency_key": uid("source_confirmation_key", i)} for i in (1,2,5,7)
    ]
    tables["product_mockup_templates"] = [
        {"mockup_template_id": uid("mockup", p*10+view), "product_version_id": uid("product_version", p),
         "view_id": "Front" if view == 1 else "Back", "base_asset_id": uid("asset", (p-1)*2+view),
         "surface_grid_json": js({"width_mm":300,"height_mm":400}), "masks_json": js([]),
         "material_color_support_json": js({"materials":"product-scoped","colors":"product-scoped"})}
        for p in range(1,7) for view in (1,2)
    ]

    # Quotes and orders. Twelve orders cover every canonical status including Cancelled.
    order_statuses = ["AwaitingDigitalApproval", "DigitalDesignApproved", "SampleInPreparation", "SampleShipped", "PendingContract",
                      "AwaitingDeposit", "Confirmed", "InProduction", "Shipped", "DeliveredAwaitingBalance", "Completed", "Cancelled"]
    tables["quotes"] = []
    tables["quote_size_quantities"] = []
    tables["orders"] = []
    tables["order_size_quantities"] = []
    tables["order_quote_cycles"] = []
    for i in range(1, 13):
        product_index = ((i-1)%6)+1
        design_index = ((i-1)%7)+1
        subtotal = 1650000 + (product_index-1)*250000
        design_fee = 200000 if i == 3 else 0
        total = subtotal + 30000 + design_fee
        tables["quotes"].append({"quote_id": uid("quote", i), "customer_id": uid("user", 4+(i%6)), "journey_intent_id": uid("journey", i),
            "buyer_type": "BusinessBuyer" if i%2 else "ResellerShop", "buyer_legal_name": f"Doanh nghiệp mẫu {i:02d}",
            "buyer_tax_id": f"SYNTH-{i:04d}", "billing_address": f"Địa chỉ thanh toán giả lập {i}, TP.HCM",
            "product_version_id": uid("product_version", product_index), "design_version_id": uid("design_version", design_index*10+1),
            "recipient_name": user_names[(3+i)%10], "phone": f"090000{i:04d}", "address_line": f"Số {i}, đường Mẫu",
            "ward": "Phường Giả Lập", "province": "TP.HCM", "country": "VN", "merchandise_subtotal_vnd": subtotal,
            "merge_discount_vnd": 0, "shipping_vnd": 30000, "tax_vnd": 0, "design_fee_vnd": design_fee, "total_vnd": total,
            "deposit_preview_vnd": total//2, "merge_opt_in": "false", "policy_version": "", "expires_at": "2026-09-28T04:30:00Z",
            "version": 1, "created_at": "2026-09-28T04:00:00Z"})
        tables["quote_size_quantities"].append({"quote_size_quantity_id": uid("quote_qty", i), "quote_id": uid("quote", i), "size_label": "M", "quantity": 10})
        tables["orders"].append({"order_id": uid("order", i), "order_number": f"SO-2026-{i:04d}", "customer_id": uid("user", 4+(i%6)),
            "journey_intent_id": uid("journey", i), "buyer_type": "BusinessBuyer" if i%2 else "ResellerShop",
            "buyer_legal_name": f"Doanh nghiệp mẫu {i:02d}", "buyer_tax_id": f"SYNTH-{i:04d}",
            "billing_address": f"Địa chỉ thanh toán giả lập {i}, TP.HCM", "product_name_snapshot": product_names[product_index-1],
            "sku_snapshot": skus[product_index-1], "material_snapshot": material_labels[0], "options_snapshot_json": js(["Front direct print"]),
            "product_version_id": uid("product_version", product_index), "design_version_id": uid("design_version", design_index*10+1),
            "recipient_name": user_names[(3+i)%10], "phone": f"090000{i:04d}", "address_line": f"Số {i}, đường Mẫu", "ward": "Phường Giả Lập",
            "province": "TP.HCM", "country": "VN", "merchandise_subtotal_vnd": subtotal, "merge_discount_vnd": 0,
            "shipping_vnd": 30000, "tax_vnd": 0, "design_fee_vnd": design_fee, "total_vnd": total, "status": order_statuses[i-1],
            "current_quote_cycle": 1, "approved_sample_id": uid("sample", min(7, i-4)) if i >= 5 and i != 12 else "",
            "contract_id": uid("contract", i) if i >= 6 and i <= 11 else "", "deposit_percent": 50, "contract_total_vnd": total,
            "accepted_deposit_vnd": total//2 if i >= 7 and i <= 11 else 0, "accepted_order_credit_vnd": 0,
            "balance_due_vnd": total-total//2 if i >= 7 and i <= 11 else total-total//2,
            "balance_due_at": "2026-10-05T05:00:00Z" if i >= 10 and i <= 11 else "", "received_at": "2026-09-28T05:00:00Z" if i >= 10 and i <= 11 else "",
            "completed_at": "2026-09-28T06:00:00Z" if i == 11 else "", "received_by_staff_id": uid("staff",1) if i == 10 else "",
            "carrier": "Synthetic Carrier" if i >= 9 and i <= 11 else "", "tracking_number": f"TRACK-{i:04d}" if i >= 9 and i <= 11 else "",
            "shipped_at": "2026-09-25T05:00:00Z" if i >= 9 and i <= 11 else "", "estimated_delivery_from": "2026-09-27" if i >= 9 and i <= 11 else "",
            "estimated_delivery_to": "2026-09-30" if i >= 9 and i <= 11 else "", "delivery_evidence_asset_id": uid("asset",24) if i >= 10 and i <= 11 else "",
            "delivery_evidence_verified_at": "2026-09-28T04:30:00Z" if i >= 10 and i <= 11 else "", "manual_refund_required": "false",
            "version": 2 if i > 1 else 1, "created_at": f"2026-09-{i:02d}T01:00:00Z", "updated_at": "2026-09-28T06:00:00Z"})
        tables["order_size_quantities"].append({"order_size_quantity_id": uid("order_qty", i), "order_id": uid("order", i), "size_label": "M", "quantity": 10})
        tables["order_quote_cycles"].append({"order_quote_cycle_id": uid("cycle", i*10+1), "order_id": uid("order", i), "cycle_number": 1,
            "quote_id": uid("quote", i), "design_version_id": uid("design_version", design_index*10+1),
            "customer_approved_at": f"2026-09-{i:02d}T02:00:00Z" if i >= 2 and i != 12 else "", "created_at": f"2026-09-{i:02d}T01:00:00Z"})
    # A second immutable revision cycle for order 4.
    tables["order_quote_cycles"].append({"order_quote_cycle_id": uid("cycle", 42), "order_id": uid("order", 4), "cycle_number": 2,
        "quote_id": uid("quote", 4), "design_version_id": uid("design_version", 42), "customer_approved_at": "", "created_at": "2026-09-20T01:00:00Z"})
    sample_states = ["InPreparation", "Shipped", "Approved", "RevisionRequested", "Approved", "Approved", "Approved"]
    tables["production_samples"] = [
        {"sample_id": uid("sample", i), "order_quote_cycle_id": uid("cycle", i*10+1), "design_version_id": uid("design_version", ((i-1)%7+1)*10+1),
         "status": sample_states[i-1], "carrier": "Synthetic Carrier" if i >= 2 else "", "tracking_number": f"SAMPLE-{i:04d}" if i >= 2 else "",
         "sent_at": "2026-09-20T02:00:00Z" if i >= 2 else "", "estimated_delivery_from": "2026-09-22" if i >= 2 else "",
         "estimated_delivery_to": "2026-09-24" if i >= 2 else "", "received_at": "2026-09-24T02:00:00Z" if i >= 3 else "",
         "approved_at": "2026-09-24T03:00:00Z" if sample_states[i-1] == "Approved" else "",
         "feedback": "Yêu cầu chỉnh lại mẫu giả lập." if i == 4 else "", "evidence_asset_id": uid("asset", 20+i), "version": 1}
        for i in base_rows("sample")
    ]
    payment_specs = [
        (6,"DEPOSIT","Pending"),(7,"DEPOSIT","Succeeded"),(8,"DEPOSIT","Succeeded"),(9,"DEPOSIT","Succeeded"),
        (10,"DEPOSIT","Succeeded"),(11,"DEPOSIT","Succeeded"),(11,"BALANCE","Succeeded"),(5,"DEPOSIT","Failed"),(12,"DEPOSIT","Expired")]
    tables["payment_transactions"] = []
    for i,(order_no,purpose,status) in enumerate(payment_specs,1):
        order = tables["orders"][order_no-1]
        amount = int(order["contract_total_vnd"])//2
        tables["payment_transactions"].append({"payment_transaction_id": uid("payment", i), "order_id": uid("order",order_no),
            "customer_id": order["customer_id"], "purpose": purpose, "amount_vnd": amount, "currency": "VND", "status": status,
            "provider_reference": f"VNPAY-SYNTH-{i:04d}" if status == "Succeeded" else "", "provider_event_id": f"EVENT-{i:04d}" if status == "Succeeded" else "",
            "paid_at": "2026-09-28T05:00:00Z" if status == "Succeeded" else "", "refund_status": "",
            "expires_at": "2026-09-28T05:15:00Z", "version": 1, "idempotency_key": uid("payment_key",i), "created_at": "2026-09-28T04:45:00Z"})
    tables["refund_records"] = [
        {"refund_id": uid("refund", i), "payment_transaction_id": uid("payment", i+1), "amount_vnd": 840000,
         "status": status, "provider_reference": f"REFUND-SYNTH-{i:03d}" if status == "Succeeded" else "",
         "requested_at": "2026-09-28T07:00:00Z", "settled_at": "2026-09-29T07:00:00Z" if status == "Succeeded" else "",
         "idempotency_key": uid("refund_key",i)} for i,status in enumerate(["Requested","Succeeded","Failed"],1)
    ]
    tables["order_timeline_events"] = []
    for i,status in enumerate(order_statuses,1):
        tables["order_timeline_events"].append({"event_id": uid("timeline",i), "order_id": uid("order",i), "prior_status": "" if i == 1 else order_statuses[max(0,i-2)],
            "target_status": status, "actor_kind": "Customer" if i in (1,2,5,6,10,12) else "Staff",
            "actor_user_id": uid("user",4+(i%6)) if i in (1,2,5,6,10,12) else uid("user",1), "event_source": "MVPWorkflow",
            "bound_entity_type": "Order", "bound_entity_id": uid("order",i), "bound_entity_version": 2,
            "sample_cycle": 1 if i in (3,4,5) else "", "evidence_asset_id": uid("asset",24) if i in (10,11) else "",
            "idempotency_reference": uid("timeline_key",i), "occurred_at": f"2026-09-{min(28,i+10):02d}T06:00:00Z"})

    # CRM.
    tables["customer_assignments"] = [
        {"assignment_id": uid("assignment",i), "customer_id": uid("user",4+(i%6)), "sales_user_id": uid("user",2),
         "assigned_by_user_id": uid("user",1), "assigned_at": f"2026-08-{i:02d}T01:00:00Z", "ended_at": "2026-09-01T01:00:00Z" if i==7 else "",
         "active": "false" if i==7 else "true", "version": 2 if i==7 else 1} for i in base_rows("assignment")
    ]
    pipeline = ["LeadIn","Assigned","Contacted","Qualified","DesignConsultation","ProposalQuotation","ClosedLost"]
    tables["consultations"] = [
        {"consultation_id": uid("consultation",i), "customer_id": uid("user",4+(i%6)), "pipeline_stage": pipeline[i-1],
         "customer_model": "Unclassified" if i==1 else ("B2B" if i%2 else "B2B2C"), "owner_sales_user_id": "" if i==1 else uid("user",2),
         "contact_name": user_names[(3+i)%10], "phone": f"090100{i:04d}", "email": f"lead{i}@example.invalid",
         "requirement_summary": f"Nhu cầu may theo đơn giả lập {i}.", "product_interest": product_names[(i-1)%6], "estimated_quantity": 10*i,
         "requested_deadline": "2026-11-01", "design_source": "CustomerProvided" if i%2==0 else "DonySupportRequired",
         "design_readiness": "ReadyForQuotation" if i>=5 else "NotReady", "technical_adjustment_required": "true" if i==4 else "false",
         "proposal_milestone": "ContractSigned" if i==6 else "", "lost_reason": "Budget" if i==7 else "", "lost_note": "" ,
         "stage_entered_at": f"2026-09-{i:02d}T01:00:00Z", "version":1, "created_at": f"2026-08-{i:02d}T01:00:00Z", "updated_at": f"2026-09-{i:02d}T01:00:00Z"}
        for i in base_rows("consultation")
    ]
    tables["lead_design_links"] = [
        {"lead_design_link_id": uid("lead_design",i), "consultation_id": uid("consultation",i), "design_id": uid("design",i),
         "design_scope": "Dropped" if i==7 else "InScope", "version":1, "created_at": "2026-09-01T01:00:00Z", "updated_at":"2026-09-02T01:00:00Z"}
        for i in base_rows("lead_design")
    ]
    tables["stage_histories"] = [
        {"stage_history_id": uid("stage_history",i), "consultation_id": uid("consultation",i), "from_stage": "LeadIn" if i>1 else "",
         "to_stage": pipeline[i-1], "actor_user_id": uid("user",1 if i==1 else 2), "source":"Manual",
         "reason":"Synthetic progression", "reference":"", "occurred_at": f"2026-09-{i:02d}T02:00:00Z"}
        for i in base_rows("stage_history")
    ]
    channels=["Phone","Email","Zalo","Messenger","Meeting","Other","Email"]
    tables["interaction_logs"]=[
        {"interaction_id":uid("interaction",i),"consultation_id":uid("consultation",i),"type":"DesignDiscussion" if i%2 else "General",
         "channel":channels[i-1],"occurred_at":f"2026-09-{i:02d}T03:00:00Z","summary":f"Tóm tắt trao đổi giả lập {i}.",
         "author_user_id":uid("user",2),"design_version_id":uid("design_version",i*10+1) if i%2 else ""} for i in base_rows("interaction")]
    tables["internal_notes"]=[
        {"note_id":uid("note",i),"consultation_id":uid("consultation",i),"text":f"Ghi chú nội bộ giả lập {i}, không chứa dữ liệu thật.",
         "author_user_id":uid("user",2),"pinned":"true" if i<=3 else "false","created_at":f"2026-09-{i:02d}T04:00:00Z"} for i in base_rows("note")]
    review_status=["Pending","Approved","Rejected","Pending","Approved","Rejected","Pending"]
    tables["admin_reviews"]=[
        {"review_id":uid("admin_review",i),"consultation_id":uid("consultation",i),"type":"CommittedDueDateChange" if i%2 else "Other",
         "requested_value":f"Đề xuất nội bộ giả lập {i}","reason":"Cần quyết định có kiểm soát.","status":review_status[i-1],
         "requester_user_id":uid("user",2),"requested_at":f"2026-09-{i:02d}T05:00:00Z","decider_user_id":uid("user",1) if review_status[i-1]!="Pending" else "",
         "decided_at":f"2026-09-{i+1:02d}T05:00:00Z" if review_status[i-1]!="Pending" else "",
         "decision_note":"Thiếu căn cứ để duyệt." if review_status[i-1]=="Rejected" else ""} for i in base_rows("admin_review")]

    # Contracts.
    template_states=["Published","Draft","Archived","Published","Draft"]
    tables["contract_templates"]=[
        {"contract_template_id":uid("template",i),"template_family_id":uid("template_family",((i-1)//2)+1),"name":f"Mẫu hợp đồng giả lập {((i-1)//2)+1}",
         "version":1 if i%2 else 2,"structured_body":"Nội dung mẫu với các placeholder được cho phép.","status":template_states[i-1],
         "created_at":f"2026-07-{i:02d}T01:00:00Z"} for i in range(1,6)]
    contract_specs=[(5,"Ready"),(6,"Signed"),(7,"Signed"),(8,"Signed"),(9,"Signed"),(10,"Signed"),(11,"Signed")]
    tables["contracts"]=[]
    for i,(order_no,contract_state) in enumerate(contract_specs,1):
        order=tables["orders"][order_no-1]; total=int(order["contract_total_vnd"])
        tables["contracts"].append({"contract_id":uid("contract",order_no),"order_id":uid("order",order_no),"contract_template_id":uid("template",1),
            "buyer_type":order["buyer_type"],"buyer_legal_name":order["buyer_legal_name"],"buyer_tax_id":order["buyer_tax_id"],"billing_address":order["billing_address"],
            "approved_design_version_id":order["design_version_id"],"approved_sample_id":uid("sample",min(7,max(1,order_no-4))),
            "contract_total_vnd":total,"deposit_percent":50,"deposit_due_vnd":total//2,"balance_due_vnd":total-total//2,
            "balance_due_rule":"7 calendar days after recorded receipt","payment_policy_version":"MFG06-BR014-v1","version":1,"template_version":1,
            "content_hash":f"synthetic-contract-hash-{order_no}","pdf_asset_id":uid("asset",25+((i-1)%3)),
            "status":contract_state,"ready_at":"2026-09-25T02:00:00Z",
            "signed_at":"2026-09-26T02:00:00Z" if contract_state=="Signed" else "","voided_at":""})
    # Historical non-current versions cover Draft, Superseded and Voided without
    # weakening the one-current-contract relation on the main order rows.
    for i,(order_no,contract_state) in enumerate([(5,"Draft"),(6,"Superseded"),(12,"Voided")],1):
        order=tables["orders"][order_no-1]; total=int(order["contract_total_vnd"])
        tables["contracts"].append({"contract_id":uid("contract_extra",i),"order_id":uid("order",order_no),"contract_template_id":uid("template",1),
            "buyer_type":order["buyer_type"],"buyer_legal_name":order["buyer_legal_name"],"buyer_tax_id":order["buyer_tax_id"],"billing_address":order["billing_address"],
            "approved_design_version_id":order["design_version_id"],"approved_sample_id":uid("sample",1) if order_no != 12 else "",
            "contract_total_vnd":total,"deposit_percent":50,"deposit_due_vnd":total//2,"balance_due_vnd":total-total//2,
            "balance_due_rule":"7 calendar days after recorded receipt","payment_policy_version":"MFG06-BR014-v1","version":i,"template_version":1,
            "content_hash":f"synthetic-extra-contract-hash-{i}","pdf_asset_id":"" if contract_state=="Draft" else uid("asset",25+((i-1)%3)),
            "status":contract_state,"ready_at":"" if contract_state=="Draft" else "2026-09-24T02:00:00Z","signed_at":"",
            "voided_at":"2026-09-27T02:00:00Z" if contract_state=="Voided" else ""})
    signed_contracts=[row for row in tables["contracts"] if row["status"]=="Signed"]
    tables["signature_evidence"]=[
        {"signature_evidence_id":uid("signature",i),"contract_id":signed_contracts[i-1]["contract_id"],
         "signer_user_id":uid("user",4+(i%6)),"typed_name":user_names[(3+i)%10],"consent_text_version":"consent-v1",
         "contract_hash":signed_contracts[i-1]["content_hash"],"server_timestamp":f"2026-09-{20+i:02d}T03:00:00Z",
         "observed_ip":"192.0.2.10","user_agent":"Synthetic browser","challenge_digest":""} for i in range(1,6)]

    # Production planning.
    tables["flexible_preferences"]=[
        {"flexible_preference_id":uid("preference",i),"quote_id":uid("quote",i),"merge_opt_in":"true" if i<=4 else "false",
         "accepted_policy_version":"MFG10-v4" if i<=4 else "","accepted_at":f"2026-09-{i:02d}T04:00:00Z" if i<=4 else "",
         "incentive_vnd":min((1650000+(i-1)*250000)*5//100,250000) if i<=4 else 0} for i in base_rows("preference")]
    tables["production_readiness"]=[
        {"production_readiness_id":uid("readiness",i),"order_id":uid("order",6+i),"production_ready_at":"2026-09-28T03:00:00Z",
         "readiness_day_1":"2026-09-28","last_waiting_date":"2026-10-06","production_window_first_date":"2026-10-07",
         "production_due_at":"2026-10-26","wait_end_exclusive_at":"2026-10-07T17:00:00Z","calendar_version":"weekday-v1",
         "waiting_workdays":7,"production_window_min_workdays":8,"production_window_max_workdays":14} for i in range(1,6)]
    tables["individual_production_plans"]=[
        {"individual_plan_id":uid("individual_plan",i),"order_id":uid("order",6+i),"approved_by_staff_id":uid("staff",1),
         "approved_at":f"2026-10-{i:02d}T02:00:00Z","started_by_staff_id":uid("staff",1) if i>=2 else "",
         "started_at":f"2026-10-{i+1:02d}T02:00:00Z" if i>=2 else "","status":"Approved" if i==1 else ("Completed" if i==5 else "Started"),
         "retained_incentive_vnd":82500,"version":1} for i in range(1,6)]
    tables["production_capacity_profiles"]=[
        {"capacity_profile_id":uid("capacity",i),"production_type_key":["THUN","POLO","SOMI","KHOAC","BAOHO"][i-1],
         "material_profile_id":uid("material",i),"daily_output_capacity":[50,45,40,35,30][i-1],"active":"true","version":1,
         "updated_by_staff_id":uid("staff",1),"updated_at":"2026-09-28T01:00:00Z"} for i in range(1,6)]
    batch_states=["ScheduledOpen","ScheduledOpen","Locked","InProduction","Completed"]
    tables["production_batches"]=[
        {"batch_id":uid("batch",i),"capacity_profile_id":uid("capacity",i),"kind":"BaseRun" if i==1 else "NewSewingGroup",
         "status":batch_states[i-1],"scheduled_start_at":f"2026-10-{7+i:02d}T01:00:00Z","planned_completion_at":f"2026-10-{17+i:02d}T01:00:00Z",
         "daily_capacity_snapshot":[50,45,40,35,30][i-1],"total_quantity":20+i*10,"required_workdays":1+i//2,
         "approved_by_staff_id":uid("staff",1),"approved_at":"2026-10-01T01:00:00Z","locked_at":"2026-10-02T01:00:00Z" if i>=3 else "",
         "started_at":"2026-10-08T01:00:00Z" if i>=4 else "","version":1} for i in range(1,6)]
    tables["batch_memberships"]=[
        {"batch_membership_id":uid("membership",i),"batch_id":uid("batch",((i-1)%5)+1),"order_id":uid("order",6+i),
         "assigned_at":"2026-10-01T02:00:00Z","released_at":"2026-10-03T02:00:00Z" if i==6 else "",
         "started_at":"2026-10-08T01:00:00Z" if i in (4,5) else "","active":"false" if i==6 else "true","lock_start_version":1}
        for i in range(1,7)]

    # Analytics and system operations.
    tables["product_entries"]=[
        {"product_entry_id":uid("entry",i),"owner_user_id":uid("user",4+(i%6)),"product_id":uid("product",((i-1)%6)+1),
         "source":"catalog","entered_at":f"2026-09-{i:02d}T01:00:00Z","product_version":1} for i in base_rows("entry")]
    intent_types=["SelfDesign","DesignService","Order","SelfDesign","Order","DesignService","Order","Order","SelfDesign","Order","Order","Order"]
    tables["journey_intents"]=[
        {"journey_intent_id":uid("journey",i),"owner_user_id":uid("user",4+(i%6)),"product_entry_id":uid("entry",((i-1)%7)+1),
         "intent_type":intent_types[i-1],"parent_intent_id":uid("journey",i-1) if i in (4,8) else "","created_at":f"2026-09-{min(i,28):02d}T01:30:00Z"}
        for i in range(1,13)]
    event_names=["product_viewed","design_started","design_saved","checkout_started","order_created","contract_ready","contract_signed","deposit_succeeded","sample_approved","shipped","receipt_confirmed","balance_succeeded"]
    tables["analytics_events"]=[
        {"analytics_event_id":uid("analytics_event",i),"schema_version":"1","event_name":event_names[i-1],
         "source_kind":"CommittedBusinessEvent" if i>=5 else "ValidatedInteraction","entity_type":"Order" if i>=5 else "JourneyIntent",
         "entity_id":uid("order",i) if i>=5 else uid("journey",i),"occurred_at":f"2026-09-{min(28,10+i):02d}T02:00:00Z",
         "received_at":f"2026-09-{min(28,10+i):02d}T02:00:01Z","actor_kind":"Customer","customer_id":uid("user",4+(i%6)),
         "product_entry_id":uid("entry",((i-1)%7)+1),"journey_intent_id":uid("journey",i),"product_id":uid("product",((i-1)%6)+1),
         "design_id":uid("design",((i-1)%7)+1) if i>=2 else "","quote_id":uid("quote",i) if i>=4 else "",
         "order_id":uid("order",i) if i>=5 else "","request_id":"","contract_id":uid("contract",i) if i in (6,7) else "",
         "bound_versions_json":js({"version":1}),"sample_cycle":1 if i==9 else "","reason_code":"","source_event_id":uid("timeline",i) if i>=5 else uid("event_source",i),
         "dataset_flags_json":js({"synthetic":True})} for i in range(1,13)]
    tables["analytics_results"]=[
        {"analytics_result_id":uid("analytics_result",i),"query_context_json":js({"range":"2026-09-01/2026-09-29","product":None}),
         "unit":"Orders" if i%2 else "Journeys","template":"Overview" if i<=4 else "Funnel","cohort":"AuthenticatedCustomers",
         "observation_mode":"as_of","eligible_count":10*i,"immature_count":"","cutoff":"2026-09-28T17:00:00Z","timezone":"Asia/Ho_Chi_Minh",
         "generated_at":"2026-09-28T18:00:00Z","expires_at":"2026-10-05T18:00:00Z","source_watermark":f"wm-{i}",
         "definition_version":"metrics-v1","coverage_json":js({"status":"complete","scope":"authenticated-only"}),
         "metrics_json":js({"created_orders":i,"recognized_revenue_vnd":i*1000000})} for i in base_rows("analytics_result")]
    export_states=["Queued","Running","Succeeded","Failed","Succeeded","Succeeded","Failed"]
    tables["export_requests"]=[
        {"export_request_id":uid("export",i),"actor_user_id":uid("user",1),"analytics_result_id":uid("analytics_result",i),
         "format":"CSV" if i%2 else "XLSX","dataset":["revenue","orders","customers","funnel","revenue","orders","funnel"][i-1],
         "watermark":f"wm-{i}","created_at":"2026-09-28T18:05:00Z","completed_at":"2026-09-28T18:06:00Z" if export_states[i-1] in ("Succeeded","Failed") else "",
         "expires_at":"2026-10-05T18:06:00Z" if export_states[i-1]=="Succeeded" else "","state":export_states[i-1],
         "private_asset_id":uid("asset",25+((i-1)%3)) if export_states[i-1]=="Succeeded" else "","row_count":i*10 if export_states[i-1]=="Succeeded" else "",
         "safe_error":"EXPORT_FAILED" if export_states[i-1]=="Failed" else ""} for i in base_rows("export")]
    severity=["INFO","INFO","WARN","ERROR","INFO","WARN","ERROR"]
    tables["audit_events"]=[
        {"audit_event_id":uid("audit",i),"actor_id":uid("user",((i-1)%3)+1),"buyer_organization_context":"",
         "target_type":"SystemConfig" if i%2 else "Order","target_id":uid("config",1) if i%2 else uid("order",i),
         "action":"Update" if i%2 else "Transition","outcome":"Failed" if severity[i-1]=="ERROR" else "Succeeded",
         "severity":severity[i-1],"request_id":f"REQ-{i:04d}","occurred_at":f"2026-09-{i:02d}T01:00:00Z",
         "redacted_details_json":js({"synthetic":True,"secret_values_excluded":True})} for i in base_rows("audit")]
    backup_states=["Succeeded","Succeeded","Succeeded","Succeeded","Succeeded","Failed","Running"]
    tables["backups"]=[
        {"backup_id":uid("backup",i),"created_at":f"2026-09-{20+i:02d}T19:00:00Z","creator_id":uid("user",3) if i==7 else "",
         "state":backup_states[i-1],"manifest_reference":f"manifest-{i}","checksum":f"checksum-{i}" if backup_states[i-1]=="Succeeded" else "",
         "schema_version":"1","asset_count":30,"transaction_log_start":f"log-{i}-start","transaction_log_end":f"log-{i}-end" if backup_states[i-1]=="Succeeded" else "",
         "error_code":"CHECKSUM_FAILED" if backup_states[i-1]=="Failed" else ""} for i in base_rows("backup")]
    tables["system_configs"]=[
        {"system_config_id":uid("config",i),"version":i,"public_company_contacts_json":js({"phone":"0900000000"}),
         "smtp_secret_reference":"secret://smtp-demo","vnpay_secret_reference":"secret://vnpay-demo","design_service_fee_vnd":200000,
         "shipping_vnd":30000,"daily_backup_time":"02:00","daily_retention_count":7,"weekly_retention_count":4,
         "production_notification_email":"ops@example.invalid","activated_at":f"2026-09-{i:02d}T01:00:00Z","actor_id":uid("user",3)}
        for i in range(1,4)]
    restore_states=["Succeeded","Failed","Running"]
    tables["restore_journals"]=[
        {"restore_journal_id":uid("restore",i),"backup_id":uid("backup",i),"committed_watermark":f"wm-restore-{i}","state":restore_states[i-1],
         "started_at":f"2026-09-{20+i:02d}T20:00:00Z","completed_at":f"2026-09-{20+i:02d}T21:00:00Z" if restore_states[i-1]!="Running" else "",
         "payment_event_reference":f"queued-provider-event-{i}" if i==1 else "","error_code":"LOG_GAP" if i==2 else ""}
        for i in range(1,4)]

    return tables


def validate(tables: dict[str, list[dict[str, object]]]) -> list[str]:
    checks: list[str] = []

    if not ORDER_FILE.exists():
        raise AssertionError(f"missing deterministic seed order file: {ORDER_FILE}")
    order = json.loads(ORDER_FILE.read_text(encoding="utf-8"))
    assert set(order) == set(tables), "seed-order.json must cover every generated table exactly once"
    assert len(set(order.values())) == len(order), "seed-order.json has duplicate numeric positions"
    for table, rows in tables.items():
        assert rows, f"{table}: table must have at least one supported row"
        columns = list(rows[0])
        assert columns, f"{table}: table must have a header"
        assert all(list(row) == columns for row in rows), f"{table}: inconsistent column order"
    checks.append("PASS generated table shapes and deterministic seed order")

    def values(table: str, column: str) -> set[str]:
        return {str(row[column]) for row in tables[table]}

    def fk(child: str, column: str, parent: str, parent_column: str) -> None:
        allowed = values(parent, parent_column)
        bad = [row[column] for row in tables[child] if str(row[column]) and str(row[column]) not in allowed]
        if bad:
            raise AssertionError(f"{child}.{column}: missing parent values {bad[:3]}")
        checks.append(f"PASS FK {child}.{column} -> {parent}.{parent_column}")

    for child, column, parent, parent_column in [
        ("staff_accounts","user_id","users","user_id"), ("sessions","user_id","users","user_id"),
        ("one_time_tokens","user_id","users","user_id"), ("notifications","recipient_user_id","users","user_id"),
        ("notifications","source_event_id","outbox_events","outbox_event_id"),
        ("staff_invitations","staff_account_id","staff_accounts","staff_account_id"),
        ("product_versions","product_id","products","product_id"), ("product_sizes","product_version_id","product_versions","product_version_id"),
        ("product_colors","product_version_id","product_versions","product_version_id"),
        ("product_materials","product_version_id","product_versions","product_version_id"),
        ("product_materials","material_profile_id","material_profiles","material_profile_id"),
        ("volume_pricing_tiers","product_version_id","product_versions","product_version_id"),
        ("product_options","product_version_id","product_versions","product_version_id"),
        ("product_options","print_method_id","print_methods","print_method_id"),
        ("print_areas","product_version_id","product_versions","product_version_id"),
        ("product_images","product_version_id","product_versions","product_version_id"),
        ("product_images","asset_id","assets","asset_id"), ("designs","customer_id","users","user_id"),
        ("designs","product_id","products","product_id"), ("designs","source_design_request_id","design_requests","design_request_id"),
        ("design_versions","design_id","designs","design_id"), ("design_versions","product_version_id","product_versions","product_version_id"),
        ("design_versions","uploader_user_id","users","user_id"), ("design_versions","preview_asset_id","assets","asset_id"),
        ("design_placements","design_version_id","design_versions","design_version_id"), ("design_placements","asset_id","assets","asset_id"),
        ("design_requests","customer_id","users","user_id"), ("design_requests","product_id","products","product_id"),
        ("design_requests","assessed_by_staff_id","staff_accounts","staff_account_id"), ("design_requests","accepted_by_user_id","users","user_id"),
        ("design_requests","fee_order_id","orders","order_id"), ("design_requests","assignee_staff_id","staff_accounts","staff_account_id"),
        ("design_request_assets","design_request_id","design_requests","design_request_id"), ("design_request_assets","asset_id","assets","asset_id"),
        ("design_feedback","design_version_id","design_versions","design_version_id"), ("design_feedback","author_user_id","users","user_id"),
        ("design_feedback_assets","feedback_id","design_feedback","feedback_id"), ("design_feedback_assets","asset_id","assets","asset_id"),
        ("staff_replies","feedback_id","design_feedback","feedback_id"), ("staff_replies","author_staff_id","staff_accounts","staff_account_id"),
        ("staff_reply_assets","staff_reply_id","staff_replies","staff_reply_id"), ("staff_reply_assets","asset_id","assets","asset_id"),
        ("customer_approvals","design_version_id","design_versions","design_version_id"), ("customer_approvals","customer_id","users","user_id"),
        ("customer_provided_confirmations","design_version_id","design_versions","design_version_id"),
        ("customer_provided_confirmations","confirmer_user_id","users","user_id"),
        ("customer_provided_confirmations","recorded_by_staff_id","staff_accounts","staff_account_id"),
        ("product_mockup_templates","product_version_id","product_versions","product_version_id"),
        ("product_mockup_templates","base_asset_id","assets","asset_id"),
        ("quotes","customer_id","users","user_id"), ("quote_size_quantities","quote_id","quotes","quote_id"),
        ("quotes","journey_intent_id","journey_intents","journey_intent_id"), ("quotes","product_version_id","product_versions","product_version_id"),
        ("quotes","design_version_id","design_versions","design_version_id"),
        ("orders","customer_id","users","user_id"), ("order_size_quantities","order_id","orders","order_id"),
        ("orders","journey_intent_id","journey_intents","journey_intent_id"), ("orders","product_version_id","product_versions","product_version_id"),
        ("orders","design_version_id","design_versions","design_version_id"), ("orders","approved_sample_id","production_samples","sample_id"),
        ("orders","contract_id","contracts","contract_id"), ("orders","received_by_staff_id","staff_accounts","staff_account_id"),
        ("orders","delivery_evidence_asset_id","assets","asset_id"),
        ("order_quote_cycles","order_id","orders","order_id"), ("order_quote_cycles","quote_id","quotes","quote_id"),
        ("order_quote_cycles","design_version_id","design_versions","design_version_id"),
        ("production_samples","order_quote_cycle_id","order_quote_cycles","order_quote_cycle_id"),
        ("production_samples","design_version_id","design_versions","design_version_id"), ("production_samples","evidence_asset_id","assets","asset_id"),
        ("payment_transactions","order_id","orders","order_id"), ("payment_transactions","customer_id","users","user_id"),
        ("refund_records","payment_transaction_id","payment_transactions","payment_transaction_id"),
        ("order_timeline_events","order_id","orders","order_id"), ("order_timeline_events","actor_user_id","users","user_id"),
        ("order_timeline_events","evidence_asset_id","assets","asset_id"),
        ("customer_assignments","customer_id","users","user_id"), ("consultations","customer_id","users","user_id"),
        ("customer_assignments","sales_user_id","users","user_id"), ("customer_assignments","assigned_by_user_id","users","user_id"),
        ("consultations","owner_sales_user_id","users","user_id"),
        ("lead_design_links","consultation_id","consultations","consultation_id"), ("lead_design_links","design_id","designs","design_id"),
        ("stage_histories","consultation_id","consultations","consultation_id"), ("stage_histories","actor_user_id","users","user_id"),
        ("interaction_logs","consultation_id","consultations","consultation_id"), ("interaction_logs","author_user_id","users","user_id"),
        ("interaction_logs","design_version_id","design_versions","design_version_id"),
        ("internal_notes","consultation_id","consultations","consultation_id"), ("internal_notes","author_user_id","users","user_id"),
        ("admin_reviews","consultation_id","consultations","consultation_id"), ("admin_reviews","requester_user_id","users","user_id"),
        ("admin_reviews","decider_user_id","users","user_id"),
        ("contracts","order_id","orders","order_id"), ("contracts","contract_template_id","contract_templates","contract_template_id"),
        ("contracts","approved_design_version_id","design_versions","design_version_id"),
        ("contracts","approved_sample_id","production_samples","sample_id"), ("contracts","pdf_asset_id","assets","asset_id"),
        ("signature_evidence","contract_id","contracts","contract_id"), ("signature_evidence","signer_user_id","users","user_id"),
        ("flexible_preferences","quote_id","quotes","quote_id"), ("production_readiness","order_id","orders","order_id"),
        ("individual_production_plans","order_id","orders","order_id"),
        ("individual_production_plans","approved_by_staff_id","staff_accounts","staff_account_id"),
        ("individual_production_plans","started_by_staff_id","staff_accounts","staff_account_id"),
        ("production_capacity_profiles","material_profile_id","material_profiles","material_profile_id"),
        ("production_capacity_profiles","updated_by_staff_id","staff_accounts","staff_account_id"),
        ("production_batches","capacity_profile_id","production_capacity_profiles","capacity_profile_id"),
        ("production_batches","approved_by_staff_id","staff_accounts","staff_account_id"),
        ("batch_memberships","batch_id","production_batches","batch_id"), ("batch_memberships","order_id","orders","order_id"),
        ("product_entries","owner_user_id","users","user_id"), ("product_entries","product_id","products","product_id"),
        ("journey_intents","owner_user_id","users","user_id"), ("journey_intents","product_entry_id","product_entries","product_entry_id"),
        ("journey_intents","parent_intent_id","journey_intents","journey_intent_id"),
        ("analytics_events","customer_id","users","user_id"), ("analytics_events","product_entry_id","product_entries","product_entry_id"),
        ("analytics_events","journey_intent_id","journey_intents","journey_intent_id"), ("analytics_events","product_id","products","product_id"),
        ("analytics_events","design_id","designs","design_id"), ("analytics_events","quote_id","quotes","quote_id"),
        ("analytics_events","order_id","orders","order_id"), ("analytics_events","request_id","design_requests","design_request_id"),
        ("analytics_events","contract_id","contracts","contract_id"),
        ("export_requests","analytics_result_id","analytics_results","analytics_result_id"),
        ("export_requests","actor_user_id","users","user_id"), ("export_requests","private_asset_id","assets","asset_id"),
        ("audit_events","actor_id","users","user_id"), ("backups","creator_id","users","user_id"),
        ("system_configs","actor_id","users","user_id"),
        ("restore_journals","backup_id","backups","backup_id"),
    ]:
        fk(child, column, parent, parent_column)

    emails = [row["email"].lower() for row in tables["users"]]
    assert len(emails) == len(set(emails)), "users.email must be unique"
    assert all(email.endswith("@example.invalid") for email in emails), "seed emails must use the reserved example.invalid domain"
    checks.append("PASS unique normalized users.email")
    checks.append("PASS synthetic email domain")
    skus_seen = [row["sku"] for row in tables["products"]]
    assert len(skus_seen) == len(set(skus_seen)), "products.sku must be unique"
    checks.append("PASS unique products.sku")
    order_numbers = [row["order_number"] for row in tables["orders"]]
    assert len(order_numbers) == len(set(order_numbers)), "order_number must be unique"
    checks.append("PASS unique immutable order_number seed values")
    active_profiles = [(row["production_type_key"], row["material_profile_id"]) for row in tables["production_capacity_profiles"] if row["active"] == "true"]
    assert len(active_profiles) == len(set(active_profiles)), "active production profile natural key duplicated"
    checks.append("PASS unique active production_type_key/material profile")
    active_assignments = [row["customer_id"] for row in tables["customer_assignments"] if row["active"] == "true"]
    assert len(active_assignments) == len(set(active_assignments)), "customer has multiple active Sales assignments"
    checks.append("PASS at most one active Sales assignment per Customer")
    active_memberships = [row["order_id"] for row in tables["batch_memberships"] if row["active"] == "true"]
    assert len(active_memberships) == len(set(active_memberships)), "order has multiple active batch memberships"
    checks.append("PASS at most one active BatchMembership per Order")
    pending_attempts = [(row["order_id"], row["purpose"]) for row in tables["payment_transactions"] if row["status"] == "Pending"]
    assert len(pending_attempts) == len(set(pending_attempts)), "multiple Pending attempts for order/purpose"
    checks.append("PASS one active Pending payment attempt per Order/purpose")
    signed_contract_ids = [row["contract_id"] for row in tables["signature_evidence"]]
    assert len(signed_contract_ids) == len(set(signed_contract_ids)), "multiple signature evidence rows for one Contract"
    checks.append("PASS at most one SignatureEvidence per Contract")
    fee_orders = [row for row in tables["orders"] if int(row["design_fee_vnd"]) > 0]
    assert len(fee_orders) == 1, "seed must demonstrate one first-order design-fee allocation"
    checks.append("PASS one design-fee-bearing first Order in covered lineage")
    for row in tables["orders"]:
        expected = int(row["merchandise_subtotal_vnd"]) - int(row["merge_discount_vnd"]) + int(row["shipping_vnd"]) + int(row["tax_vnd"]) + int(row["design_fee_vnd"])
        assert expected == int(row["total_vnd"]), f"order total mismatch: {row['order_number']}"
        assert row["created_at"] <= row["updated_at"], f"order timestamp inconsistency: {row['order_number']}"
    checks.append("PASS order total formula for every Order")
    checks.append("PASS Order created_at <= updated_at")
    for row in tables["users"]:
        assert row["created_at"] <= row["updated_at"], f"user timestamp inconsistency: {row['email']}"
    for row in tables["payment_transactions"]:
        if row["paid_at"]:
            assert row["created_at"] <= row["paid_at"], f"payment timestamp inconsistency: {row['payment_transaction_id']}"
    checks.append("PASS User and PaymentTransaction timestamp ordering")
    assert any(row["status"] == "Cancelled" for row in tables["orders"])
    assert any(row["status"] == "Completed" for row in tables["orders"])
    checks.append("PASS exceptional Cancelled and completed end-to-end Order states")
    occupied_customers = (values("orders","customer_id") | values("designs","customer_id") |
                          values("design_requests","customer_id") | values("consultations","customer_id"))
    assert any(row["customer_capability"] == "true" and row["verified_at"] and row["user_id"] not in occupied_customers for row in tables["users"])
    checks.append("PASS verified Customer empty-state parent with no Design, DesignRequest, Consultation or Order")

    enum_coverage = {
        ("products", "status"): {"Draft", "Published", "Hidden", "Archived"},
        ("staff_accounts", "status"): {"Invited", "Active", "Suspended", "Deleted"},
        ("design_requests", "state"): {"Submitted", "UnderReview", "FeeProposed", "Approved", "Assigned", "InProgress", "Delivered", "Cancelled", "Rejected"},
        ("design_versions", "review_state"): {"Draft", "SharedForReview", "Approved", "Superseded"},
        ("contracts", "status"): {"Draft", "Ready", "Signed", "Superseded", "Voided"},
        ("payment_transactions", "status"): {"Pending", "Succeeded", "Failed", "Expired"},
        ("payment_transactions", "purpose"): {"DEPOSIT", "BALANCE"},
    }
    for (table, column), expected in enum_coverage.items():
        actual = {str(row[column]) for row in tables[table]}
        assert expected <= actual, f"{table}.{column} is missing fixture values: {sorted(expected - actual)}"
    checks.append("PASS required lifecycle and payment enum fixtures")

    token_durations_minutes = {
        "EmailVerification": 24 * 60,
        "PasswordReset": 30,
        "EmailChange": 24 * 60,
        "StaffInvitation": 48 * 60,
    }
    for row in tables["one_time_tokens"]:
        created = datetime.fromisoformat(str(row["created_at"]).replace("Z", "+00:00"))
        expires = datetime.fromisoformat(str(row["expires_at"]).replace("Z", "+00:00"))
        assert (expires - created).total_seconds() == token_durations_minutes[str(row["purpose"])] * 60, (
            f"one_time_tokens TTL mismatch for {row['purpose']}"
        )
    checks.append("PASS verification, reset, email-change and invitation token TTL fixtures")

    expected_outbox_sources = {
        "VerificationQueued": ("MFG-01", "User"),
        "PasswordResetQueued": ("MFG-01", "User"),
        "OrderCreated": ("MFG-06", "Order"),
        "SampleShipped": ("MFG-06", "Order"),
        "ContractReady": ("MFG-09", "Contract"),
        "DepositSucceeded": ("MFG-06", "PaymentTransaction"),
        "OrderCancelled": ("MFG-07", "Order"),
        "ConfigChanged": ("MFG-12", "SystemConfig"),
    }
    actual_outbox_sources = {
        str(row["event_type"]): (str(row["source_module"]), str(row["source_entity_type"]))
        for row in tables["outbox_events"]
    }
    assert actual_outbox_sources == expected_outbox_sources, "outbox seed event ownership must match the owning business module"
    config_event = next(row for row in tables["outbox_events"] if row["event_type"] == "ConfigChanged")
    assert json.loads(str(config_event["payload_json"])) == {"changed_keys": ["shipping_vnd"]}, "config notice must expose only changed key names"
    config_notice = next(row for row in tables["notifications"] if row["source_event_id"] == config_event["outbox_event_id"])
    assert config_notice["recipient_user_id"] == uid("user", 3) and config_notice["target_route"] == "/system/configuration", (
        "MFG-12 configuration notice must target the System Admin fixture"
    )
    checks.append("PASS notification/outbox fixture ownership and config-change privacy")

    phones = [str(row["phone"]) for table in ("quotes", "orders") for row in tables[table]]
    assert all(phone.startswith("0") and phone.isdigit() for phone in phones), "phone fixtures must retain a leading zero as text"
    checks.append("PASS phone fixtures preserve leading zero text")

    assert any(row["ownership"] == "Dony" and row["mime_type"] == "PNG" and row["scan_status"] == "Safe" for row in tables["assets"]), (
        "synthetic Dony PNG asset fixture is required"
    )
    assert {row["view_id"] for row in tables["product_mockup_templates"]} >= {"Front", "Back"}, (
        "try-on/mockup prerequisites require front and back synthetic templates"
    )
    checks.append("PASS synthetic design and try-on prerequisite fixtures")
    return checks


def main() -> None:
    tables = generate()
    checks = validate(tables)
    for name, rows in tables.items():
        write_table(name, rows)
    print(f"Generated {len(tables)} CSV files in data/seed")
    print(f"Generated {sum(len(rows) for rows in tables.values())} rows")
    for check in checks:
        print(check)


if __name__ == "__main__":
    main()
