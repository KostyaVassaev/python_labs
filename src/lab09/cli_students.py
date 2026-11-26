from pathlib import Path
import sys
import argparse

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
src_path = project_root / "src"
sys.path.append(str(src_path))

from src.lab08.models import format_student
from lab09.group import (
    add_student,
    find_students,
    list_students,
    remove_student,
    stats,
    update_student,
)

parser = argparse.ArgumentParser(description="CLI для управления базой данных студентов (students.csv)")
parser.add_argument(
        "--db",
        default="data/lab09/students.csv",
        help="Путь к CSV-файлу хранилища (по умолчанию: data/lab09/students.csv)",
    )

subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные команды")

add_parser = subparsers.add_parser("add", help="Добавить нового студента")
add_parser.add_argument("--fio", required=True, help="ФИО студента")
add_parser.add_argument("--birthdate", required=True, help="Дата рождения (YYYY-MM-DD)")
add_parser.add_argument("--group", required=True, help="Учебная группа")
add_parser.add_argument("--gpa", required=True, help="Средний балл (0.0 - 5.0)")

list_parser = subparsers.add_parser("list", help="Вывести список всех студентов")
list_parser.add_argument(
    "--sort",
    choices=["fio", "gpa"],
    default=None,
    help="Поле для сортировки (fio или gpa)",
)

find_parser = subparsers.add_parser("find", help="Найти студентов по подстроке в ФИО")
find_parser.add_argument("--q", required=True, help="Подстрока для поиска")

remove_parser = subparsers.add_parser("remove", help="Удалить студента по точному ФИО")
remove_parser.add_argument("--fio", required=True, help="ФИО студента для удаления")

update_parser = subparsers.add_parser("update", help="Обновить данные существующего студента")
update_parser.add_argument("--fio", required=True, help="ФИО студента")
update_parser.add_argument("--birthdate", help="Дата рождения (YYYY-MM-DD)")
update_parser.add_argument("--group", help="Учебная группа")
update_parser.add_argument("--gpa", help="Средний балл (0.0 - 5.0)")

subparsers.add_parser("stats", help="Показать аналитику по студентам")

args = parser.parse_args()

try:
    if args.command == "add":
        student_data = {
            "fio": args.fio,
            "birthdate": args.birthdate,
            "group": args.group,
            "gpa": args.gpa,
        }
        add_student(args.db, student_data)
        print(f"Студент '{args.fio}' успешно добавлен.")

    elif args.command == "list":
        students = list_students(args.db, sort_by=args.sort)
        for s in students:
            print(format_student(s))

    elif args.command == "find":
        students = find_students(args.db, args.q)
        for s in students:
            print(format_student(s))

    elif args.command == "remove":
        deleted_cnt = remove_student(args.db, args.fio)
        print(f"Удалено записей: {deleted_cnt}")

    elif args.command == "update":
        fields = {}
        if args.birthdate is not None:
            fields["birthdate"] = args.birthdate
        if args.group is not None:
            fields["group"] = args.group
        if args.gpa is not None:
            fields["gpa"] = args.gpa

        if not fields:
            raise ValueError("Не указано ни одного поля для обновления (--birthdate, --group или --gpa).")

        updated = update_student(args.db, args.fio, **fields)
        if updated:
            print(f"Данные студента '{args.fio}' обновлены.")
        else:
            print(f"Студент с ФИО '{args.fio}' не найден.")

    elif args.command == "stats":
        data = stats(args.db)
        print(f"Всего студентов: {data['count']}")
        if data["count"] > 0:
            print(f"GPA: min={data['min_gpa']}, max={data['max_gpa']}, avg={data['avg_gpa']}")
            print("По группам:")
            for grp, cnt in data["groups"].items():
                print(f"  {grp}: {cnt}")
            print("Топ-5 студентов:")
            for st in data["top_5_students"]:
                print(f"  {st['fio']} - {st['gpa']}")

except Exception as e:
    print(f"Ошибка: {e}", file=sys.stderr)
    sys.exit(1)