def format_record(rec: tuple[str, str, float]) -> str:
    if len(list(rec)) != 3: raise TypeError("not valid length of incoming tuple")

    fio, group, gpa = rec[0].split(), rec[1], rec[2]
    if not (2 <= len(fio) <= 3): raise ValueError("not valid fio")
    if not (0.0 <= gpa <= 5.0): raise ValueError("not valid gpa")

    formated_fio = f"{fio[0][0].upper() + fio[0][1:]} "
    for i in range(1, len(fio)):
        formated_fio += f"{fio[i][0].upper()}."

    return f"{formated_fio}, гр. {group.upper()}, GPA {gpa:.2f}"