---
name: excel-data-validator
description: Quy trình kiểm tra, làm sạch và xác thực dữ liệu Excel theo các luật kinh doanh, tự động phát hiện dữ liệu thiếu hoặc bất hợp lý. Kích hoạt khi người dùng yêu cầu validate file Excel hoặc kiểm tra chất lượng dữ liệu.
---

# Excel Data Validation Skill

## When to Use
Kích hoạt skill này khi người dùng yêu cầu:
- Kiểm tra hoặc xác thực file dữ liệu Excel.
- Phát hiện ô trống (missing data), dữ liệu trùng lặp hoặc sai kiểu dữ liệu.
- Chuẩn bị dữ liệu phục vụ tạo Dashboard hoặc Báo cáo.

## Process
1. Inspect Structure: Phân tích cấu trúc bảng, danh sách cột và kiểu dữ liệu.
2. Define Rules: Xác định các quy tắc logic cần kiểm tra.
3. Validate Data:
   - Kiểm tra ô trống (Missing values).
   - Kiểm tra trùng lặp ID/Mã.
   - Kiểm tra tính nhất quán dữ liệu giữa các cột.
4. Output Report:
   - Đưa ra điểm chất lượng dữ liệu (Data Health Score %).
   - Liệt kê bảng lỗi chi tiết (Dòng/Cột/Loại lỗi).
   - Đề xuất phương án làm sạch/sửa lỗi.

## Output Format
- Summary Table (Tổng quan)
- Error Log Table (Danh sách lỗi chi tiết)
- Actionable Next Steps (Khuyến nghị khắc phục)