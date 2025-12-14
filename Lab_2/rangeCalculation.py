try:
    I = int(input("Введите число I "))
    N = int(input("Введите число N "))
    D = int(input("Введите число D "))
    K = int(input("Введите число K "))
    step = 1
    sumDK = (D+K)
    difDK = (D-K)
    if N < I: step = -1
    print( *[ i * sumDK / difDK
              for i in range(I,N+step,step) ] )

except: print("Ошибка ввода")