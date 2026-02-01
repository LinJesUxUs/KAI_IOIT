def equalisation(a: float, b: float):
    if (a == 0) and (b == 0):
        return "'x' равен любому числу"
    if (b == 0):
        return float(0)
    if (a == 0):
        return "Нет решения.(деление на 0)"
    return -b/a

A = int(input("Введите число a "))
B = int(input("Введите число b "))

print(A, B, equalisation(A, B), sep="\t")
