s = input()
n = ""
f = True
for i in s:
    if i != " ":
# Проверим, нет ли такой цифры в n, тогда добавим эту цифру, если есть - выходим из цикла и f = False
        if i not in n:
            n+=i
        else:
            f = False
            break
print(f)
    

