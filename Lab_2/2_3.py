try:
    a = int(input("Введите 'a' "))
    b = int(input("Введите 'b' "))
    c = int(input("Введите 'c' "))
    
    lst = [a,b,c]
    s = 0
    for i in lst:
        if i < 0:
            s += 1

    print( s, "отрицательных")
except:
    print("Ошибка ввода")