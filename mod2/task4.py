n = input()
bin_n = ""
oct_n = ""
hex_n = ""
# Проверим, будет ли целым число
for i in n:
    if i == "." or i == ",":
        print("Неверный ввод")
        exit()
n1 = int(n)
n2 = int(n)
n3 = int(n)
# Проверим, больше нуля число или нет
if int(n) < 0:
    print("Неверный ввод")
else:
# Переводим в двоичную систему
    while n1 > 0:
        bin_n += str(n1%2)
        n1//=2
# Переводим в восьмеричную систему
    while n2 > 0:
        oct_n += str(n2%8)
        n2//=8
# Переводим в шестнадцатеричную систему
    while n3 > 0:
        if n3%16 == 10:
            hex_n += "a"
        elif n3%16 == 11:
            hex_n += "b"
        elif n3%16 == 12:
            hex_n += "c"
        elif n3%16 == 13:
            hex_n += "d"
        elif n3%16 == 14:
            hex_n += "e"
        elif n3%16 == 15:
            hex_n += "f"
        else:
            hex_n += str(n3%16)
        n3//=16
print(bin_n[::-1] + " " + oct_n[::-1] + " " + hex_n[::-1])
