try:
    t = int(input("Введите 't' "))
    p = int(input("Введите 'p' "))
    t = p = int( not (t == p) )
    print("t = ", t, "\np = ", p)
except:
    print("Ошибка ввода")