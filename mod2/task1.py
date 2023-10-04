v = input()
a = ""
b = ""
for i in range(len(v)):
    if v[i] == " ":
        break
a = v[:i-1]
b = v[i+1:]
c = float(a)%float(b)
# Проверим, будет ли результат целым числом, чтобы результат соответствовал формату вывода целых чисел
if str(c*10)[-1] == '0':
    print(int(c))
else:
    print(c)