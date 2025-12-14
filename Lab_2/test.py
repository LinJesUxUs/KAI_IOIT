from equalisation import equalisation

data = [ [2,3],
           [0,4],
           [5,0],
           [0,0] ]

for t in data:
	try: t.append( equalisation(*t) )
	except Exception as e:
		t.append( e )

print("a\tb\tx")
for t in data:
	print(*t,sep='\t')