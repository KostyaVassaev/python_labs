def simple_nums_to_n(a, sys):
    if a < 0: raise ValueError("This function converts only non-negative numbers")
    if sys > 26 or sys < 2: raise ValueError("Incorrect base of the number system")
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
    res = ""
    while a > 0:
        res += alphabet[a % sys]
        a //= sys
    return res