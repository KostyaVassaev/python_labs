name = ""
while not name or " " in name:
    name = input("Имя: ")
    if not name or " " in name: print("Имя не введено или введено некорректно, введите имя!")
old = -1
while old < 0:
    old = int(input("Возраст: "))
    if old < 0: print("Возраст не введён или введён некорректно, введите возраст!")
print(f"Привет, {name}! Через год тебе будет {old + 1}.")