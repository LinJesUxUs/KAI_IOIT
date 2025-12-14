def equalisation(a: float, b: float):
    if (a == 0) and (b == 0):
        raise ValueError("'x' равен любому числу")
    if (b == 0):
        return float(0)
    if (a == 0):
        raise ValueError("Нет решения.(деление на 0)")

    return -b/a

data = [ [2,3]
        ,[0,4]
        ,[5,0]
        ,[0,0] ]

for t in data:
    try: t.append( equalisation(*t) )
    except Exception as e:
        t.append( e )

print("a\tb\tx")
for t in data:
    print(*t,sep='\t')