import sys
from pathlib import Path
import argparse

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
src_path = project_root / "src"
sys.path.append(str(src_path))

from lib.text import *
from lib.outputting import table_print

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные подкоманды")

parser_stats = subparsers.add_parser("stats", help="Анализ частот слов в тексте")
parser_stats.add_argument("--input", required=True, dest="input_file", type=str, help="Путь к исходному файлу")
parser_stats.add_argument("--top", type=int, default=5, help="Длина списка самых частых слов")

parser_cat = subparsers.add_parser("cat", help="Вывод содержимого файла")
parser_cat.add_argument("--input", required=True, dest="input_file", type=str, help="Путь к исходному TXT-файлу")
parser_cat.add_argument("-n", action="store_true", help="Включить нумерацию строк")

args = parser.parse_args()

try:
    if args.command == "stats":
        with open(args.input_file, "r", encoding="utf-8") as fl:
            data = []
            with open(args.input_file, "r", encoding="utf-8") as fl:
                for ln in fl:
                    data += tokenize(normalize(ln))

            freq = count_freq(data)

            print(f"Всего слов: {len(data)}")
            print(f"Уникальных слов: {len(freq)}")
            print(f"\nТоп-{args.top}:")
            table_print(top_n(freq, args.top), ("слово", "частота"))
    
    elif args.command == "cat":
        if args.n:
            with open(args.input_file, "r", encoding="utf-8") as fl:
                i = 0
                for ln in fl:
                    i += 1
                    print(f"{i}. {ln.strip()}")
        else:
            with open(args.input_file, "r", encoding="utf-8") as fl:
                for ln in fl: print(ln.strip())
except Exception as e: print(f"Что-то пошло не так: {e}")