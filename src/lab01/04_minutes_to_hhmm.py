a = "."
while not a.isdigit():
    a = input("Минуты: ")
    if not a.isdigit(): print("Введите положительное целое число минут!")

m = int(a)
print(f"{m//60:02}:{m%60:02}")