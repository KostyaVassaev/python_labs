import sys
from pathlib import Path
from collections import Counter
import codecs
import argparse

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
src_path = project_root / "src"
data_path = project_root / "data"
sys.path.append(str(src_path))
sys.path.append(str(data_path))

from io_txt_csv import *
from lib.inp import agreement

# =================================================================

def frequencies_from_text(text: str) -> dict[str, int]:
    if type(text) != str: raise TypeError("This function works only with string")
    from lib.text import normalize, tokenize
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    try:
        return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    except:
        raise TypeError("This function works only with dictionary")

# =================================================================

parser = argparse.ArgumentParser(description="Генератор отчетов по тексту")
parser.add_argument("--in", dest="input_files", type=str, nargs="+", help="Пути к входным файлам через пробел")
parser.add_argument("--encoding", type=str, help="Кодировка всех файлов (одна и та же)")
parser.add_argument("--per-file", dest="per_file", type=str, help="Путь к файлу пофайлового отчёта")
parser.add_argument("--total", type=str, help="Путь к файлу сводного отчёта")
args = parser.parse_args()

# =================================================================

full_file_names = []
if args.input_files:
    for file_name in args.input_files:
        full_file_names.append(project_root / file_name)
else:
    file_names = input("Введите названия файлов и их путь через пробел: ").split()
    for file_name in file_names:
        full_file_names.append(project_root / file_name)

standart_encoding = "utf-8"

per_file_data = []
total_counter = Counter()
total_words_len = 0

for full_file_name in full_file_names:
    s = ""
    if args.encoding:
        try:
            codecs.lookup(args.encoding)
            s = read_text(full_file_name, args.encoding)
            print(f"Файл '{full_file_name.name}' прочитан с помощью кодировки '{args.encoding}'.")
        except Exception as e:
            print(f"Ошибка чтения файла '{full_file_name.name}' с кодировкой {args.encoding}: {e}")
            exit()
    elif agreement(f"Кодировка файла '{full_file_name.name}' является '{standart_encoding}'?"):
        try:
            s = read_text(full_file_name, standart_encoding)
            print(f"Файл '{full_file_name.name}' прочитан.")
        except Exception as e:
            print(f"Ошибка при чтении файла '{full_file_name.name}': {e}\nВыход из программы.")
            exit()
    else:
        encoding_name = input(f"Введите кодировку для файла '{full_file_name.name}': ")
        try:
            codecs.lookup(encoding_name)
            s = read_text(full_file_name, encoding_name)
            print("Файл прочитан с помощью введённой кодировки.")
        except:
            print(f"Что-то пошло не так...")
            try:
                s = read_text(full_file_name, standart_encoding)
                print(f"Кодировка '{encoding_name}' не найдена. Файл прочитан в кодировке '{standart_encoding}'.")
            except Exception as e:
                print(f"Ошибка при чтении файла '{full_file_name.name}': {e}\nВыход из программы.")
                exit()

    file_frequencies = frequencies_from_text(s)
    short_name = full_file_name.name

    for word, count in file_frequencies.items():
        per_file_data.append((short_name, word, count))

    total_counter.update(file_frequencies)

    from lib.text import tokenize
    total_words_len += len(tokenize(s))

# =================================================================

per_file_sorted = sorted(per_file_data, key=lambda x: (x[0], -x[2], x[1]))
total_sorted = sorted_word_counts(total_counter)

# =================================================================

if args.input_files:
    per_file_report_path = project_root / (args.per_file if args.per_file else "data/report_per_file.csv")
    total_report_path = project_root / (args.total if args.total else "data/report_total.csv")
elif agreement("Сохранить отчёты под стандартными именами?"):
    per_file_report_path = "data/report_per_file.csv"
    total_report_path = "data/report_total.csv"
else:
    per_file_report_path = input("Введите название файла для пофайлового отчёта: ")
    total_report_path = input("Введите название файла для сводного отчёта: ")

ensure_parent_dir(per_file_report_path)
ensure_parent_dir(total_report_path)

write_csv(per_file_sorted, str(per_file_report_path), ("file", "word", "count"))
print(f"Пофайловый отчёт сохранён в '{per_file_report_path}'")

write_csv(total_sorted, str(total_report_path), ("word", "count"))
print(f"Сводный отчёт сохранён в '{total_report_path}'")

# =================================================================

print(f"\nВсего слов во всех файлах: {total_words_len}")
print(f"Уникальных слов во всех файлах: {len(total_sorted)}")

print("Сводный топ-5:")
from lib.outputting import table_print
table_print(total_sorted[:5], ("слово", "частота"))