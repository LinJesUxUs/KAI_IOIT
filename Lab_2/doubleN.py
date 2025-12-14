try:
    n = int(input("Введите число N "))
    step = 1
    if n < 3: step = -1
    print( *[ i*2 for i in range(3,n+step,step) ] )

except: print("Ошибка ввода")