a = "-1"
while True:
    a = input("Минуты: ")
    if not a.isdigit(): print("Введите положительное целое число минут!")
    elif int(a) < 0: print("Введите положительное целое число минут!")
    else: break

m = int(a)
print(f"{m//60:02}:{m%60:02}")