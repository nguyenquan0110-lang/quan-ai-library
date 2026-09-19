---
name: excel-data-validator
description: Kích hoạt khi người dùng yêu cầu kiểm tra, validate, tìm lỗi dữ liệu hoặc rà soát cấu trúc file Excel.
---

# Excel Data Validation Skill

## When to Use
Kích hoạt Skill này khi câu lệnh của người dùng chứa các từ khóa:
- "kiểm tra file Excel này"
- "validate dữ liệu Excel"
- "tìm dòng lỗi / thiếu thông tin"
- "rà soát định dạng Excel"

## Workflow
Thực hiện chính xác theo 5 bước sau:

1. **Structure Inspection**:
   - Kiểm tra tên sheet, danh sách các cột (headers).
   - Xác định tổng số dòng dữ liệu.

2. **Rules Mapping**:
   - Xác định cột bắt buộc không được để trống (Missing values).
   - Kiểm tra kiểu dữ liệu (Số, Ngày tháng, Text, Chuỗi định dạng).

3. **Data Scanning**:
   - Quét từng dòng dữ liệu để phát hiện lỗi logic hoặc sai định dạng.
   - Thống kê danh sách dòng bị lỗi và loại lỗi tương ứng.

4. **Report Generation**:
   - Tạo báo cáo tổng quan dạng bảng gồm các cột: `Dòng` | `Tên Cột` | `Giá trị lỗi` | `Nguyên nhân` | `Cách khắc phục`.

5. **Stop & Confirm**:
   - Dừng lại sau khi xuất báo cáo. Hỏi người dùng có muốn chạy script tự động sửa lỗi không.

## Output Format Standard
Trả về báo cáo theo định dạng Bảng Markdown gọn gàng. Ngăn cách rõ ràng giữa phần Tóm tắt (Executive Summary) và Chi tiết lỗi (Detailed Errors).

---
name: excel-data-validator
description: Kích hoạt khi người dùng yêu cầu kiểm tra, validate, tìm lỗi dữ liệu hoặc rà soát cấu trúc file Excel.
---

# Excel Data Validation Skill

## When to Use
Kích hoạt Skill này khi câu lệnh của người dùng chứa các từ khóa:
- "kiểm tra file Excel này"
- "validate dữ liệu Excel"
- "tìm dòng lỗi / thiếu thông tin trong file [tên_file.xlsx]"

## Tools & Scripts
Skill này đi kèm với script Python tự động hóa nằm tại:
`./scripts/validate_excel.py`

## Workflow

1. **Execute Validation Script**:
   - Chạy lệnh sau trong Terminal/Tool execution của Agent:
     ```bash
     python .agents/skills/excel-data-validator/scripts/validate_excel.py <path_to_excel_file>
     ```

2. **Parse & Analyze Output**:
   - Đọc kết quả JSON trả về từ script.
   - Phân loại các nhóm lỗi chính (ô trống, trùng lặp, dữ liệu bất thường).

3. **Generate Final Report**:
   - Trình bày lại kết quả dưới dạng Bảng Markdown theo cấu trúc:
     | Dòng (Row) | Cột (Column) | Giá trị lỗi | Nguyên nhân | Cách khắc phục |

4. **Stop & Confirm**:
   - Dừng lại sau khi xuất báo cáo. Hỏi người dùng có cần viết script tự động làm sạch (clean) file Excel này không.