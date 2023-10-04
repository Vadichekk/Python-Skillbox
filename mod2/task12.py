s = input()
sym = "()-"
p_number = ""
p_number += s[0]
for i in range(1,len(s)):
# Проверим есть ли s[i] в sym
    if s[i] not in sym and s[i] != " ":
        p_number += s[i]
print(p_number)