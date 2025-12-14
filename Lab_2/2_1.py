try:
    x = float(input("Введите 'x' "))
    y = float(input("Введите 'y' "))
    if x == y:
        raise
    halfsum = (x+y)/2
    doublepow = x*y*2
    if x < y:
        x = halfsum
        y = doublepow
    else:
        y = halfsum
        x = doublepow
    print("x = ", x, "\ny = ", y)
except:
    print("Ошибка ввода")