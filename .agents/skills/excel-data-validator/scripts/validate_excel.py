import sys
import pandas as pd
import json

def validate_excel(file_path):
    try:
        # Đọc file Excel
        df = pd.read_excel(file_path)
        errors = []

        # Rule 1: Kiểm tra ô trống (Missing values)
        for row_idx, row in df.iterrows():
            for col_name in df.columns:
                val = row[col_name]
                if pd.isna(val) or str(val).strip() == "":
                    errors.append({
                        "Row": row_idx + 2,  # Cộng 2 vì Excel có Header ở dòng 1 và index bắt đầu từ 0
                        "Column": str(col_name),
                        "Value": "EMPTY",
                        "Issue": "Thiếu dữ liệu bắt buộc",
                        "Fix": "Điền bổ sung thông tin"
                    })

        # Rule 2: Kiểm tra dữ liệu trùng lặp hoàn toàn (Duplicate rows)
        duplicates = df[df.duplicated(keep=False)]
        for row_idx in duplicates.index:
            errors.append({
                "Row": row_idx + 2,
                "Column": "ALL",
                "Value": "DUPLICATE",
                "Issue": "Dòng dữ liệu bị trùng lặp",
                "Fix": "Xóa dòng trùng hoặc kiểm tra lại ID"
            })

        # Xuất kết quả dạng JSON để AI dễ đọc
        summary = {
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "total_errors": len(errors),
            "error_details": errors
        }
        
        print(json.dumps(summary, ensure_ascii=False, indent=2))

    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        validate_excel(sys.argv[1])
    else:
        print(json.dumps({"error": "Vui lòng cung cấp đường dẫn file Excel"}, ensure_ascii=False))