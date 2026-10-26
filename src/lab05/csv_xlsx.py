from pathlib import Path
import csv
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path) -> None:
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)
    if csv_path.suffix() != ".csv": raise ValueError("Invalid CSV-file extension.")
    if csv_path.suffix() != ".xlsx": raise ValueError("Invalid XLSX-file extension.")
    
    try:
        with open(csv_path, mode="r", encoding="utf-8") as csv_fl:
            reader = csv.reader(csv_fl)
            data = list(reader)
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return

    if not data: raise ValueError("Empty CSV-file.")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in data:
        ws.append(row)

    for col in ws.columns:
        # Ищем максимальную длину значения в колонке (переводя в строку)
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = col[0].column_letter # Получаем букву колонки (A, B, C...)
        # Задаем ширину: максимум из (длины + 3 символа запаса) или 8 (минимальная ширина)
        ws.column_dimensions[col_letter].width = max(max_len + 3, 8)

    try:
        wb.save(xlsx_path)
    except Exception as e:
        print(f"Ошибка при сохранении XLSX-файла: {e}")