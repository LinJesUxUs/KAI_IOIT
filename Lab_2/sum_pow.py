def sum_pow( eDenom: int, operator: str="sum"
            ,stepDenom: int=2, bDenom: int=2
            ,stepNumer: int=0, bNumer: int=1 ):
    buf = 0.0
    if operator == "pow": buf = 1.0
    numer = bNumer
    for i in range(bDenom,eDenom+1,stepDenom):
        if operator == "sum":
            buf += numer/i
        elif operator == "pow":
            buf *= numer/i
        numer += stepNumer
    return buf

from math import cos

def cos_sum(begin: int, end: int, step: int):
    buf = 0.0
    for i in range(begin, end+1, step):
        buf += cos(i)
    return buf

print( cos_sum(1, 10, 1) )
print( sum_pow(20))
print( sum_pow(50,"pow",5,5))
print( sum_pow(10,"sum",2,2,2))
print( sum_pow(21,"pow",2,3))