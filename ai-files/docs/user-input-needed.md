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
| **Must** | Role-based Authentication & Access (Customer, Sales Consultant, Company Admin) | MFG-01 | Foundation - every other feature depends on secure, role-aware access |
| **Must** | Product Catalog (browse, search, view product detail) | MFG-04 | Entry point for customers to find a base product to customize |
| **Must** | Product Design Workspace (self-design, upload artwork, preview, save design) | MFG-05 | Core value proposition - replaces scattered email/chat design specifications |
| **Must** | Order & Payment (checkout, VNPay integration, order creation) | MFG-06 | Core revenue flow - must work before "design & order" has any value |
| **Should** | Order Tracking & Status Updates (customer order list/detail, admin status update) | MFG-07 | Solves the reactive customer service pain point, but early orders can still be tracked manually |
| **Should** | Digital Contract Generation & E-signature | MFG-09 | Builds trust for business clients, but an emailed/paper contract is an acceptable stopgap at launch |
| **Could** | Order Optimization / Merge (batch small orders into one production run) | MFG-10 | Directly targets high operational overhead, but only pays off once order volume exists |
| **Could** | Paid Design Service Request (consultant-assisted design) | MFG-05 | Alternative to self-design for complex custom-design clients |
| **Could** | Sales Consultant Assignment & Task Dashboard | MFG-08 | Only needed once consultation volume justifies a dedicated queue |
| **Won't** | Data Analytics Dashboard & Data Export | MFG-11 | Out of scope for MVP; revisit once there is sufficient order history to analyze |
| **Won't** | Company Accounts & System Operations (multi-admin roles, system logs, backup/restore) | MFG-03, MFG-12 | A single admin login is sufficient at launch; defer full account/system administration |

## MVP Priority Summary

- **Must:** MFG-01, MFG-04, MFG-05, MFG-06
- **Should:** MFG-07, MFG-09
- **Could:** MFG-05, MFG-08, MFG-10
- **Won't:** MFG-03, MFG-11, MFG-12
