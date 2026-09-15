name = ""
while not name or " " in name:
    name = input("Имя: ")
    if not name or " " in name: print("Имя не введено или введено некорректно, введите имя!")
old = "-1"
while int(old) < 0:
    old = input("Возраст: ").replace(",", ".")
    if not (200 >= int(old) >= 0) or not old.isdigit() or "." in old:
        print("Возраст не введён или введён некорректно, введите возраст (натуальное число или ноль, не больше 200)!")
print(f"Привет, {name}! Через год тебе будет {int(old) + 1}.")