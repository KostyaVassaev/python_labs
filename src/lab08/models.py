from datetime import date
import re

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")

def make_student(fio, birthdate, group, gpa) -> dict:
    rec = {
        STUDENT_FIELDS[0]: fio,
        STUDENT_FIELDS[1]: birthdate,
        STUDENT_FIELDS[2]: group,
        STUDENT_FIELDS[3]: float(gpa) if isinstance(gpa, int) and not isinstance(gpa, bool) else gpa
        }

    validate_student(rec)
    
    return rec

def validate_student(rec: dict) -> None:
    if not isinstance(rec, dict): raise TypeError("Recording type must be dictionary")

    if set(rec.keys()) != set(STUDENT_FIELDS): raise ValueError("Invalid set of write keys")

    if not isinstance(rec[STUDENT_FIELDS[0]], str):
        raise TypeError("The fio field must be a non-empty string")
    elif not rec[STUDENT_FIELDS[0]].strip():
        raise ValueError("The fio field must be a non-empty string")
    if not isinstance(rec[STUDENT_FIELDS[2]], str):
        raise TypeError("The group field must be a non-empty string")
    elif not rec[STUDENT_FIELDS[2]].strip():
        raise ValueError("The group field must be a non-empty string")
    if not isinstance(rec[STUDENT_FIELDS[1]], str):
        raise TypeError("The datebirth field must be a non-empty string")
    elif not rec[STUDENT_FIELDS[1]].strip():
        raise ValueError("The datebirth field must be a non-empty string")

    birthdate = rec[STUDENT_FIELDS[1]]
    
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", birthdate):
        raise ValueError("Wrong date format of birthdate (expects 'YYYY-MM-DD')")

    try: bdate = date.fromisoformat(birthdate)
    except ValueError as e: raise ValueError(f"Invalid calendar date: {e}") from None

    if bdate > date.today():
        raise ValueError("Birthdate cannot be in the future")

    gpa = rec[STUDENT_FIELDS[3]]
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise ValueError("gpa field must be a number")
    try:
        if not 0 <= float(gpa) <= 5:
            raise ValueError
    except (ValueError, TypeError): raise ValueError("gpa field must be a number between 0 and 5") from None

def student_age(rec: dict, today=None) -> int:
    validate_student(rec)

    if today == None: today = date.today()
    elif isinstance(today, str):
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", today):
            raise ValueError("Wrong date format of birthdate (expects 'YYYY-MM-DD')")
        try: today = date.fromisoformat(today)
        except ValueError as e: raise ValueError(f"Invalid calendar date: {e}") from None
    else: raise TypeError("Date of today must be a string (format 'YYYY-MM-DD')")
    
    bdate = date.fromisoformat(rec[STUDENT_FIELDS[1]])
    if bdate.year > today.year: raise ValueError("Wrong birthdate date: year of birth later than today")
    age = today.year - bdate.year
    if (today.month, today.day) < (bdate.month, bdate.day): age -= 1

    return age

def format_student(rec: dict) -> str:
    validate_student(rec)

    fio_parts = rec[STUDENT_FIELDS[0]].split()
    if len(fio_parts) >= 3: fio_form = f"{fio_parts[0]} {fio_parts[1][0]}.{fio_parts[2][0]}."
    elif len(fio_parts) == 2: fio_form = f"{fio_parts[0]} {fio_parts[1][0]}."
    else: fio_form = rec[STUDENT_FIELDS[0]]

    age = student_age(rec)
    if 11 <= age % 100 <= 19: years_str = "лет"
    elif age % 10 == 1: years_str = "год"
    elif age % 10 in (2, 3, 4): years_str = "года"
    else: years_str = "лет"

    gpa_val = float(rec[STUDENT_FIELDS[3]])

    return f"{fio_form} ({rec[STUDENT_FIELDS[2]]}), {age} {years_str}, GPA {gpa_val:.2f}"

def student_to_dict(rec: dict) -> dict:
    validate_student(rec)
    return {
        STUDENT_FIELDS[0]: rec[STUDENT_FIELDS[0]],
        STUDENT_FIELDS[1]: rec[STUDENT_FIELDS[1]],
        STUDENT_FIELDS[2]: rec[STUDENT_FIELDS[2]],
        STUDENT_FIELDS[3]: rec[STUDENT_FIELDS[3]]
    }

def student_from_dict(d: dict) -> dict:
    if not isinstance(d, dict): raise ValueError("Works only with dictionary")

    extracted = {}
    for field in STUDENT_FIELDS:
        if field not in d: raise ValueError(f"There is no required field: {field}")
        extracted[field] = d[field]

    try: extracted[STUDENT_FIELDS[3]] = float(extracted[STUDENT_FIELDS[3]])
    except (ValueError, TypeError): raise ValueError("Failed to cast gpa to float")
    
    validate_student(extracted)
    
    return extracted

def update_student(rec: dict, **fields) -> dict:
    for key in fields:
        if key not in STUDENT_FIELDS:
            raise KeyError(f"Unknown field to update: {key}")

    new_rec = {
        STUDENT_FIELDS[0]: rec[STUDENT_FIELDS[0]],
        STUDENT_FIELDS[1]: rec[STUDENT_FIELDS[1]],
        STUDENT_FIELDS[2]: rec[STUDENT_FIELDS[2]],
        STUDENT_FIELDS[3]: rec[STUDENT_FIELDS[3]]
    }

    new_rec.update(fields)
    validate_student(new_rec)

    return new_rec