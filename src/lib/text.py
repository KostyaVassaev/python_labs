import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if type(text) != str: raise TypeError("normalize works with strings only")

    if casefold: text = text.casefold()
    else: text = text.lower()

    if yo2e: text = text.replace('ё', 'е').replace('Ё', 'Е')

    text = re.sub(target := r'\s+', ' ', text)

    return text.strip()

def tokenize(text: str) -> list[str]:
    if type(text) != str: raise TypeError("tokenize works with strings only")

    pattern = r'\w+(?:-\w+)*'
    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    if type(tokens) != list: raise TypeError("count_freq works with lists only")

    freq = {}
    for token in tokens:
        if type(token) != str: raise TypeError("only list of strings")
        freq[token] = freq.get(token, 0) + 1

    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    lst = freq.items()
    
    sorted_items = sorted(lst, key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:n]