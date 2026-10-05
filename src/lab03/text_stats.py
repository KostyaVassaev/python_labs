import sys
import os

sys.path.append(os.path.abspath("../lib"))

from text import *

inp = ""
while inp != 'y' and inp != 'n':
    inp = input('Ввод из файла или в строке? [y/n]: ').lower()

if inp == 'y':
    file_name = input('Введите полный путь к файлу: ')
    with open(file_name, 'r', encoding='utf-8') as f:
        st = f.read()

else: st = input('Введите строку: ')

st = normalize(st)
words = tokenize(st)
word_dict = count_freq(words)
top_5 = top_n(word_dict, 5)

print(f"Всего слов: {len(words)}")
print(f"Уникальных слов: {len(word_dict)}")

mx_ln = 0
for item in top_5:
    ln = len(item[0])
    if ln > mx_ln: mx_ln = ln

print('\nТоп-5:')
print(f"{'слово':<{mx_ln}} | {'частота'}")
print("-" * (12 + mx_ln))
for word, cnt in top_5: print(f"{word:<{mx_ln}} | {cnt}")