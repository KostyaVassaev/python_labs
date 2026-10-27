import sys
from pathlib import Path
import argparse

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
src_path = project_root / "src"
sys.path.append(str(src_path))

from lab05.json_csv import *
from lab05.csv_xlsx import *

parser = argparse.ArgumentParser(description="Конвертер файлов.")
subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные подкоманды")

parser_json2csv = subparsers.add_parser("json2csv", help="Конвертация JSON в CSV")
parser_json2csv.add_argument("--in", required=True, dest="input_file", type=str, help="Путь к исходному JSON-файлу")
parser_json2csv.add_argument("--out", required=True, dest="output_file", type=str, help="Путь для сохранения CSV-файла")

parser_csv2json = subparsers.add_parser("csv2json", help="Конвертация CSV в JSON")
parser_csv2json.add_argument("--in", required=True, dest="input_file", type=str, help="Путь к исходному CSV-файлу")
parser_csv2json.add_argument("--out", required=True, dest="output_file", type=str, help="Путь для сохранения JSON-файла")

parser_csv2xlsx = subparsers.add_parser("csv2xlsx", help="Конвертация CSV в XLSX")
parser_csv2xlsx.add_argument("--in", required=True, dest="input_file", type=str, help="Путь к исходному CSV-файлу")
parser_csv2xlsx.add_argument("--out", required=True, dest="output_file", type=str, help="Путь для сохранения XLSX-файла")

args = parser.parse_args()

try:
    if args.command == "json2csv":
        json_to_csv(args.input_file, args.output_file)
    elif args.command == "csv2json":
        csv_to_json(args.input_file, args.output_file)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input_file, args.output_file)
    print("Конвертация успешно выполнена.")
except Exception as e: print(f"Что-то пошло не так: {e}")