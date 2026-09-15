name = ""
while not name:
    name = input("Имя: ")
    if not name: print("Имя не введено, введите имя!")
old = -1
while old < 0:
    old = int(input("Возраст: "))
    if old < 0: print("Возраст не введён или введён некорректно, введите возраст!")
print(f"Привет, {name}! Через год тебе будет {old + 1}.")