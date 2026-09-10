surname, first_name, patronymic = map(str, input("ФИО: ").split())
length = len(surname) + len(first_name) + len(patronymic) + 2 #2 - кол-во пробелов
print(f"Инициалы: {surname[0] + first_name[0] + patronymic[0]}.\nДлина (символов): {length}")