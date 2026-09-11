price = float(input("price: "))
discount = float(input("discount: "))
vat = float(input("vat: "))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

prints = [
    ("База после скидки:", base),
    ("НДС:", vat_amount),
    ("Итого к оплате:", total)
]

for text, val in prints:
    print(f"{text:<18} {val:.2f}")