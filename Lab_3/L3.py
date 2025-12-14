# (a-x)/(1-x^2)-(x+b)/(1-x^2)=(x+c)/(x+x^2)
# x=(a-b+c-1+sqrt(((a-b+c-1)^2)-4*c))/2
from math import sqrt
try:
    a = int(input("Введите число a "))
    b = int(input("Введите число b "))
    c = int(input("Введите число c "))
    value = (a-b+c-1)
    value2 = (value**2)-4*c
    success = False
    
    if value2 < 0:
        raise ValueError("Нет решения.#1") # 2,2,2
    
    root = sqrt(value2)
    if (-1 <= root) and (root <= 1):
        print(sqrt(1))
        raise ValueError("Нет решения.#2") # 3,1,1

    x = [(value+root)/2
        ,(value-root)/2]
    
    def check(x):
        val1 = (a-x)/(1-x**2)-(x+b)/(1-x**2)
        val2 = (x+c)/(x+x**2)
        return val1 == val2

    for i in x:
        if -1 > i or i > 1:
            if check(i):
                print("x =", i) # 3,1,3
                success = True

    if not success: print("Нет решения.", *x) # 2,-3,1

except Exception as e:
    print(str(e))