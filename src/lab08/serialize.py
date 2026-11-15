import json, csv
from pathlib import Path
from models import student_to_dict, student_from_dict, STUDENT_FIELDS

def students_to_json(students: list[dict], path: str | Path) -> None:
    data = [student_to_dict(s) for s in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str | Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    if not isinstance(raw_data, list):
        raise ValueError("The root element of the JSON must be an array.")

    valid_students = []
    skipped_errors = []

    for idx, item in enumerate(raw_data, start=1):
        try:
            student = student_from_dict(item)
            valid_students.append(student)
        except ValueError as e:
            skipped_errors.append(f"Recording №{idx}: {e}")

    if skipped_errors:
        print(f"Missed broken records: {len(skipped_errors)}")
        for err in skipped_errors:
            print(f"  - {err}")

    return valid_students

def students_from_csv(path: str | Path) -> list[dict]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
    
    valid_students = []
    skipped_errors = []

    if reader.fieldnames is None or not set(STUDENT_FIELDS).issubset(set(reader.fieldnames)):
        raise ValueError(f"Required headers are missing from the CSV. Expected: {', '.join(STUDENT_FIELDS)}")

    for row_num, row in enumerate(reader, start=2):
            try:
                student = student_from_dict(row)
                valid_students.append(student)
            except ValueError as e:
                skipped_errors.append(f"Recording №{row_num}: {e}")

    if skipped_errors:
        print(f"Missed broken records: {len(skipped_errors)}")
        for err in skipped_errors:
            print(f"  - {err}")

    return valid_students