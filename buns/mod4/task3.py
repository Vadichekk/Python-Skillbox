a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def ef_alg(a, b):
    if b == 0:
        return a
    else:
        return ef_alg(b, a % b)

result = ef_alg(a, b)

print("Наибольший общий делитель:", result)