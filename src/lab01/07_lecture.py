st = input("in: ")
text = ""

wasUpper = False
for i in range(len(st) - 1):
    if st[i].isupper() and not wasUpper:
        wasUpper = True
        text += st[i]
        firstWordNum = i
    elif st[i].isdigit() and not st[i + 1].isdigit():
        betw = i + 1 - firstWordNum
        break

i = firstWordNum + betw
while i < len(st):
    text += st[i]
    if st[i] == ".": break
    i += betw

print("out:", text)