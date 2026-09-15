s = "."
while not s.isdigit():
    s = input("count of students: ")
n = int(s)
cnt_full, cnt_correspondence = 0, 0

for i in range(n):
    lst = list(map(str, input(f"in_{i + 1}: ").split()))
    if len(lst) != 4: continue
    surname, name, age, full_time = lst[0], lst[1], lst[2], lst[3]
    if full_time == "True": cnt_full += 1
    elif full_time == "False": cnt_correspondence += 1

print("out:", cnt_full, cnt_correspondence)