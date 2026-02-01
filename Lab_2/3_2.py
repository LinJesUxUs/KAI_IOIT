def myRange(begin: int, end: int, step: int=1):
	
	def inc_dec(first,second):
		if begin < end: return first <= second
		else: return first >= second

	def stepper(value):
		if (begin < end) ^ (step > 0):
			return value - step
		return value + step
	
	lst = []
	iterator = begin
	
	while( inc_dec(iterator,end) ):
		lst.append(iterator)
		iterator = stepper(iterator)
	return lst

def positiveSum():
	s = 0.0
	for i in range(7):
		buf = 0.0
		try: buf = float(input("Введите число: "))
		except: print("Введено не число! ")
		if buf > 0: s += buf
	print(s)


print(myRange(5,10))
print(myRange(9,1))
print(myRange(0,-15,-3))
print(myRange(2,14,2))

positiveSum()