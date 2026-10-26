import sys
from pathlib import Path
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
src_path = project_root / "src"
data_path = project_root / "data"
sys.path.append(str(src_path))
sys.path.append(str(data_path))

from lib.pathwork import ensure_parent_dir

def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path) -> None:
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if csv_path.suffix != ".csv": raise ValueError("Invalid CSV-file extension.")
    if xlsx_path.suffix != ".xlsx": raise ValueError("Invalid XLSX-file extension.")
    if not csv_path.is_file(): raise FileNotFoundError("CSV-file does not exist.")
    
    with open(csv_path, mode="r", encoding="utf-8") as csv_fl:
        reader = csv.reader(csv_fl)
        data = list(reader)

    if not data or not data[0]: raise ValueError("Empty CSV-file.")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in data:
        ws.append(row)

    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        # Правильно получаем букву колонки (например, 'A', 'B'...)
        col_letter = get_column_letter(col[0].column) 
        # Устанавливаем ширину: максимум из длины текста (+ запас) или 8 по ТЗ
        ws.column_dimensions[col_letter].width = max(max_len + 3, 8)

    ensure_parent_dir(xlsx_path)
    wb.save(xlsx_path)