def fact(n):
	return reduce(lambda x,y: x*y, range(1,n+1))


result = fact(40) / fact(20) / fact(20)