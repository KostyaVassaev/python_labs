from pathlib import Path
import sys
import csv, json

from lib.pathwork import ensure_parent_dir

def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if json_path.suffix != ".json": raise ValueError("Invalid JSON-file extension.")
    if csv_path.suffix != ".csv": raise ValueError("Invalid CSV-file extension.")
    if not json_path.is_file(): raise FileNotFoundError("JSON-file does not exist.")

    if json_path.stat().st_size == 0:
        raise ValueError("JSON-file is empty.")

    with open(json_path, mode="r", encoding="utf-8") as json_fl:
        try:
            data = json.load(json_fl)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

    if not data: raise ValueError("Empty JSON-file.")
    if not isinstance(data, list):
        raise ValueError("JSON root must be a list.")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON list must contain only dictionaries.")
    
    ensure_parent_dir(csv_path)

    fieldnames = sorted(list(set(key for item in data for key in item.keys())))

    with open(csv_path, mode="w", newline="", encoding="utf-8") as csv_fl:
        writer = csv.DictWriter(csv_fl, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()
        writer.writerows(data)
    

def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    csv_path = Path(csv_path)
    json_path = Path(json_path)

    if csv_path.suffix != ".csv": raise ValueError("Invalid CSV-file extension.")
    if json_path.suffix != ".json": raise ValueError("Invalid JSON-file extension.")
    if not csv_path.is_file(): raise FileNotFoundError("CSV-file does not exist.")

    with open(csv_path, mode="r", encoding="utf-8") as csv_fl:
        reader = csv.DictReader(csv_fl)
        if reader.fieldnames is None or not reader.fieldnames:
            raise ValueError("CSV-file is empty or missing a header.")
        data = list(reader)

    if not data: raise ValueError("Empty CSV-file.")
    
    ensure_parent_dir(json_path)

    with open(json_path, mode="w", encoding="utf-8") as json_fl:
        json.dump(data, json_fl, indent=2, ensure_ascii=False)
