from pathlib import Path
import sys
import csv

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
src_path = project_root / "src"
sys.path.append(str(src_path))

from lab08.models import STUDENT_FIELDS, student_from_dict, validate_student
from lab08.serialize import students_from_csv
from lib.text import normalize

def ensure_storage(path: str | Path) -> None:
    path = Path(path)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(STUDENT_FIELDS)

def load_students(path: str | Path) -> list[dict]:
    res = students_from_csv(Path(path))
    return res

def save_students(path: str | Path, students: list[dict]) -> None:
    path = Path(path)
    ensure_storage(path)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=STUDENT_FIELDS)
        writer.writeheader()
        writer.writerows(students)

def add_student(path: str | Path, student: dict) -> None:
    path = Path(path)
    ensure_storage(path)
    validate_student(student)

    students = load_students(path)
    if any(s["fio"] == student["fio"] for s in students):
        raise ValueError(f"A student with the full name '{student['fio']}' already exists")
    students.append(student_from_dict(student))
    save_students(path, students)

def list_students(path: str | Path, sort_by: str = None) -> list[dict]:
    path = Path(path)
    if sort_by not in (None, "fio", "gpa"): raise ValueError(f"Unknown sort field: {sort_by}")

    students = load_students(path)
    if sort_by == "fio":
        return sorted(students, key=lambda s: s["fio"].lower())
    if sort_by == "gpa":
        return sorted(students, key=lambda s: s["gpa"], reverse=True)
    return students

def find_students(path: str | Path, substr: str) -> list[dict]:
    path = Path(path)
    students = load_students(path)
    q = normalize(substr).lower()
    return [s for s in students if q in normalize(s["fio"]).lower()]

def remove_student(path: str | Path, fio: str) -> int:
    path = Path(path)
    students = load_students(path)
    new_students = [s for s in students if s["fio"] != fio]
    removed_cnt = len(students) - len(new_students)

    if removed_cnt > 0:
        save_students(path, new_students)

    return removed_cnt

def update_student(path: str | Path, fio: str, **fields) -> bool:
    path = Path(path)

    for key in fields:
        if key not in STUDENT_FIELDS:
            raise KeyError(f"Unknown field to update: {key}")

    students = load_students(path)
    for i, student in enumerate(students):
        if student["fio"] == fio:
            updated = {**student, **fields}
            validate_student(updated)
            students[i] = student_from_dict(updated)
            save_students(path, students)
            return True

    return False