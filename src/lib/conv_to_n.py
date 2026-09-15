def to_n(a, sys):
    if a < 0: raise ValueError("Только положительные числа")
    if sys > 26 or sys < 2: raise ValueError("Некорректное основание системы")
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    res = ""
    while a > 0:
        res += 
        a //= sys