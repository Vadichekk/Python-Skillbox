s = input()
ch = ""
n = ""
f = True
alfavit = "abcdefghijklmnopqrstuvwxyz"
# Добавим в ch символ
# Проверим на отрицательное число и добавим в n число
for i in s:
    if i == "-":
        f = False
        continue
    if ch == "":
        ch = i
    elif i != ",":
        n += i
n = int(n)
if f == False:
    n = (-1) * n
# Смещение происходит при любых n
for i in range(len(alfavit)):
    if alfavit[i] == ch:
        c = (i+n)//len(alfavit)
        if i + n >= len(alfavit)-1:
            print(alfavit[(i+n)-(len(alfavit)*c)])
            break
        if i + n <= 0:
            print(alfavit[(len(alfavit)*(-c))+(i+n)])
            break
        else:
            print(alfavit[i+n])
            break