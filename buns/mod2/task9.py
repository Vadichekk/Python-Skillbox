s = input()
alfavit = "уеёаоыэияю"
count1 = 0
count2 = 0
for i in s:
# Проверим есть ли символ в строке alfavit
    if i in alfavit:
        count1 += 1
    elif i != " ":
        count2 += 1
print(count1, count2)