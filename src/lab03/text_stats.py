import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
lib_path = project_root / "lib"
sys.path.append(str(lib_path))

from text import *
from inp import *

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
    mx_ln = 0
    for item in top_5:
        ln = len(item[0])
        if ln > mx_ln: mx_ln = ln
    
    print(f"{'слово':<{mx_ln}} | {'частота'}")
    print("-" * (12 + mx_ln))
    for word, cnt in top_5: print(f"{word:<{mx_ln}} | {cnt}")

else:
    for word, cnt in top_5: print(f"{word}: {cnt}")