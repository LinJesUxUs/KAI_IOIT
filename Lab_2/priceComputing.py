try:
    C = float(input("Введите цену единицы C "))
    K = float(input("Введите колличество K "))
    SP = C * K
    if K >= 100:
      SP *= 0.9
    elif K >= 50:
      SP *= 0.95
    print("Сумма =", SP)

except: print("Ошибка ввода")