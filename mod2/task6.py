s = input()
a = ""
for i in range(-1,-len(s)-1,-1):
    if s[i] != ".":
        a+=s[i]
    if s[i] == ".":
        print(a[::-1])
        a = ""
# конце нет еще одной точки, по этому выводим еще одну строку
print(a[::-1])