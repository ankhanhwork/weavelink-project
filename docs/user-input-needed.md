# Thông tin thực tế cần bổ sung

Đây là file duy nhất dành cho thông tin cần chủ dự án trả lời. Các quyết định nghiệp vụ/kỹ thuật đã được chốt trong [system-decisions.md](system-decisions.md), không cần trả lời thêm để dùng specs làm đầu vào lập trình.

| ID | Thông tin | Giá trị hiện tại / cách xử lý | Trả lời của bạn |
|---|---|---|---|
| HUMAN-01 | Họ tên, mã sinh viên và phân công thành viên cho từng MFG | Chưa xác minh; không tự gán tác giả cho sinh viên | |
| HUMAN-02 | Tên chính thức môn học, mã lớp, giảng viên, tên/số nhóm, học kỳ | Ngữ cảnh do bạn cung cấp: DBIZ3 kế thừa DBIZ2; các thông tin hành chính khác chưa xác minh | |
| HUMAN-03 | Người/đơn vị phê duyệt học phần hoặc khách hàng thực tế, chức danh và ngày phê duyệt | Bạn đã duyệt kế hoạch sửa specs; điều đó không thay cho chữ ký/phê duyệt thực tế của giảng viên hoặc khách hàng | |
| HUMAN-04 | Nếu dùng ngoài demo: tên pháp lý công ty, mã số thuế, địa chỉ, người đại diện, thông tin liên hệ và URL chính thức | Demo dùng dữ liệu giả có nhãn; chưa cấu hình thì ẩn liên kết liên hệ. Không dùng dữ liệu mẫu làm danh tính pháp lý | |
| HUMAN-05 | Nếu cần đối chiếu học phần: vị trí bản gốc DBIZ2, Session 1/Session 3, MVP Scope v3 được nhắc trong tài liệu cũ | Các bản gốc không có trong repo hiện tại; bản đặc tả mới ghi rõ quyết định bổ sung, không tuyên bố đã kiểm chứng các bản gốc | |

Không điền mật khẩu, API key, khóa ký hay thông tin bí mật vào file này. Tích hợp thật được cấu hình bằng môi trường triển khai; demo dùng email sink và VNPay sandbox.
