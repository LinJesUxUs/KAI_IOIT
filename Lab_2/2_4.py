try:
    x = float(input("Введите 'x' "))
    y = float(input("Введите 'y' "))
    
    if y > x:
        x, y = y, x

    print("X = ", x, "Y = ", y)
except:
    print("Ошибка ввода")