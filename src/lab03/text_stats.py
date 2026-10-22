import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
src_path = project_root / "src"
sys.path.append(str(src_path))

from lib.text import *
from lib.inp import *

file_flag = agreement('Ввод из файла или в строке?')

if file_flag:
    file_name = input('Введите полный путь к файлу: ').strip('\'" ')
    with open(file_name, 'r', encoding='utf-8') as f:
        st = f.read()

else: st = input('Введите строку: ')

st = normalize(st)
words = tokenize(st)
word_dict = count_freq(words)
top_5 = top_n(word_dict, 5)

print(f"Всего слов: {len(words)}")
print(f"Уникальных слов: {len(word_dict)}")

table_flag = agreement('Вывод топа в виде таблицы?') #вывод в виде таблицы или нет

print('\nТоп-5:')
if table_flag:
    from lib.outputting import table_print
    table_print(top_5, ("слово", "частота"))

else:
    for word, cnt in top_5: print(f"{word}: {cnt}")