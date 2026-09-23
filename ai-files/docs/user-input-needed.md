# Thông tin thực tế cần bổ sung

Đây là file duy nhất dành cho thông tin cần chủ dự án trả lời. Các quyết định nghiệp vụ/kỹ thuật đã được chốt trong [system-decisions.md](system-decisions.md), không cần trả lời thêm để dùng specs làm đầu vào lập trình.

| ID | Thông tin | Giá trị hiện tại / cách xử lý | Trả lời của bạn |
|---|---|---|---|
| HUMAN-01 | Họ tên, mã sinh viên và phân công thành viên cho từng MFG | Chưa xác minh; không tự gán tác giả cho sinh viên | Group B |
| HUMAN-02 | Tên chính thức môn học, mã lớp, giảng viên, tên/số nhóm, học kỳ | Ngữ cảnh do bạn cung cấp: DBIZ3; các thông tin hành chính khác chưa xác minh | Tên môn học: DBIZ 3. Các thông tin hành chính khác không cần thiết cho hệ thống |
| HUMAN-03 | Người/đơn vị phê duyệt học phần hoặc khách hàng thực tế, chức danh và ngày phê duyệt | Bạn đã duyệt kế hoạch sửa specs; điều đó không thay cho chữ ký/phê duyệt thực tế của giảng viên hoặc khách hàng | Chưa có người phê duyệt |
| HUMAN-04 | Nếu dùng ngoài demo: tên pháp lý công ty, mã số thuế, địa chỉ, người đại diện, thông tin liên hệ và URL chính thức | Demo dùng dữ liệu giả có nhãn; chưa cấu hình thì ẩn liên kết liên hệ. Không dùng dữ liệu mẫu làm danh tính pháp lý | Không dùng ngoài demo, chỉ dùng trong môn học |
| HUMAN-05 | Nếu cần đối chiếu học phần: vị trí bản gốc DBIZ2, Session 1/Session 3, MVP Scope v3 được nhắc trong tài liệu cũ | Các bản gốc không có trong repo hiện tại; bản đặc tả mới ghi rõ quyết định bổ sung, không tuyên bố đã kiểm chứng các bản gốc | Không cần đối chiếu với DBIZ 2. MVP Scope được xác định theo từng MFG và được bổ sung vào `README.md` |

Không điền mật khẩu, API key, khóa ký hay thông tin bí mật vào file này. Tích hợp thật được cấu hình bằng môi trường triển khai; demo dùng email sink và VNPay sandbox.

---

# MVP Scope

The MVP scope is defined by priority and mapped to the corresponding MFG (Module Feature Group).

| Priority | Feature / Item | MFG | Notes |
|---|---|---|---|
| **Must** | Role-based Authentication & Access (Customer, Sales, Sales Admin) | MFG-01 | Foundation - every other feature depends on secure, role-aware access |
| **Must** | Product Catalog (browse, search, view product detail) | MFG-04 | Seed at least one complete Published product base with variants, option rules, prices and assets; CRUD UI is not required in MVP. |
| **Must** | Product Design Workspace (self-design, upload artwork, preview, save design) | MFG-05 | Self-design/save is Must; assessed Complex design service is a separate Could capability. |
| **Must** | Order & Payment (standard checkout, VNPay deposit and balance, order creation) | MFG-06 | Standard order only; MVP merge_opt_in=false and merge_discount_vnd=0. Requires minimum sample, contract and fulfillment slices. |
| **Should** | Order Tracking & Status Updates | MFG-07 | Full module is Should; MVP requires Customer sample/receipt approvals and manual Sales Admin sample, production and shipping updates. |
| **Should** | Digital Contract Generation & E-signature acknowledgement | MFG-09 | Full module is Should; MVP requires one fixed template and Customer acknowledgement before deposit. |
| **Could** | Order Optimization / Merge (batch small orders into one production run) | MFG-10 | Deferred from MVP; v3 rules activate only when MFG-10 is implemented. |
| **Could** | Assessed Design Service Request (Simple free; accepted Complex fee collected with order) | MFG-05 | Separate from Must self-design; defer assessment/assignment/fee workflows. |
| **Could** | Sales Assignment & Task Dashboard | MFG-08 | Only needed once consultation volume justifies a dedicated queue. |
| **Won't** | Data Analytics Dashboard & Data Export | MFG-11 | Out of scope for MVP; revisit once there is sufficient order history to analyze |
| **Won't** | Dony Staff Accounts & System Operations (internal staff administration, system logs, backup/restore) | MFG-03, MFG-12 | Pre-provision Sales Admin, Sales, System Admin and verified Customer identities; defer staff-management and system-operations screens. |

## MVP Priority Summary

- **Must:** MFG-01, MFG-04, self-design in MFG-05, and MFG-06
- **Should:** full MFG-07/MFG-09 modules; MVP-critical path slices are mandatory
- **Could:** assessed design service in MFG-05, MFG-08, MFG-10
- **Won't:** MFG-03, MFG-11, MFG-12
