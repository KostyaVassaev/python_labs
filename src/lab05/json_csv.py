from pathlib import Path
import sys
import csv
import json

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
src_path = project_root / "src"
sys.path.append(str(src_path))

from lib.pathwork import ensure_parent_dir

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if csv_path.suffix() != ".csv": raise ValueError("Invalid CSV-file extension.")
    if json_path.suffix() != ".json": raise ValueError("Invalid JSON-file extension.")

    try:
        with open(json_path, mode="r", encoding="utf-8") as json_fl:
            data = json.load(json_fl)
    except Exception as e:
        print(f"Ошибка при чтении JSON-файла: {e}")
        return

    if not data: raise ValueError("Empty JSON-file.")
    
    ensure_parent_dir(csv_path)

    try:
        with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_fl:
            writer = csv.writer(csv_fl, delimiter=",")
            writer.writerows(data)
    except Exception as e:
        print(f"Ошибка при записи CSV-файла: {e}")
    

def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if csv_path.suffix() != ".csv": raise ValueError("Invalid CSV-file extension.")
    if json_path.suffix() != ".json": raise ValueError("Invalid JSON-file extension.")

    try:
        with open(csv_path, mode="r", encoding="utf-8") as csv_fl:
            reader = csv.DictReader(csv_fl)
            data = list(reader)
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return

    if not data: raise ValueError("Empty CSV-file.")
    
    ensure_parent_dir(json_path)

    try:
        with open(json_path, mode="w", encoding="utf-8") as json_fl:
            json.dump(data, json_fl, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Ошибка при записи JSON-файла: {e}")
        return