import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
lib_path = project_root / "lib"
sys.path.append(str(lib_path))

from text import *

# normalize
#print(r'"ПрИвЕт\nМИр\t" ->', f'"{normalize("ПрИвЕт\nМИр\t")}"')
#print('"ёжик, Ёлка" ->', f'"{normalize("ёжик, Ёлка")}"')
#print(r'"Hello\r\nWorld ->"', f'"{normalize("Hello\r\nWorld")}"')
#print('"  двойные   пробелы  "', "->", f'"{normalize("  двойные   пробелы  ")}"')

# tokenize
#print('"привет, мир!" ->', f'"{tokenize("привет, мир!")}"')
#print('"hello,world!!!" ->', f'"{tokenize("hello,world!!!")}"')
#print('"по-настоящему круто" ->', f'"{tokenize("по-настоящему круто")}"')
#print('"2025 год" ->', f'"{tokenize("2025 год")}"')
#print('"emoji 😀 не слово" ->', f'"{tokenize("emoji 😀 не слово")}"')

# count_freq + top_n
#freq = count_freq(["a","b","a","c","b","a"])
#print(["a","b","a","c","b","a"], "->", freq)
#print(freq, "->", top_n(freq, 2))

# тай-брейк по слову при равной частоте
#freq2 = count_freq(["bb","aa","bb","aa","cc"])
#print(["bb","aa","bb","aa","cc"], "->", top_n(freq2, 2))