from pathlib import Path
import csv

def ensure_storage(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def load_students(path: str | Path) -> list[dict]:

def save_students(path: str | Path, students: list[dict]) -> None:

def add_student(path: str | Path, student: dict) -> None:

def list_students(path: str | Path, sort_by: str = None) -> list[dict]:
    if not isinstance(sort_by, str): raise TypeError("")
    if sort_by not in (None, "fio", "gpa"): raise ValueError("")

def find_students(path: str | Path, substr: str) -> list[dict]:

def remove_student(path: str | Path, fio: str) -> int:

def update_student(path: str | Path, fio: str, **fields) -> None: