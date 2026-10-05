import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold: text = text.casefold()
    else: text = text.lower()

    if yo2e: text = text.replace('ё', 'е').replace('Ё', 'Е')

    text = re.sub(target := r'\s+', ' ', text)

    return text.strip()

def tokenize(text: str) -> list[str]:
    pattern = r'\w+(?:-\w+)*'
    return re.findall(pattern, text)
    # re.findall — извлекает все совпадения из текста и возвращает их в виде списка строк

# \w+ — находит одну или более букв, цифр или символов подчёркивания;
# (?:-\w+)* — это незапоминающая группа (?:...), которая ищет дефис,
# за которым сразу следует еще одна группа \w+. Знак * означает,
# что таких групп в слове может быть ноль или больше
# (например, для слов вроде кое-где-нибудь)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq: freq[token] = freq[token] + 1
        else: freq[token] = 1

    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    lst = freq.items()
    # freq.items() возвращает пары словаря в виде кортежей,
    # т.е. dict[str, int] -> list[tuple[str, int]]
    
    sorted_items = sorted(lst, key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:n]