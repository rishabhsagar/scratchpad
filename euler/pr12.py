#map() , reduce(), filter()
def noOfDivs(n):
	result = []
	noDiv = 1
	# test 2 and all of the odd numbers
	# xrange instead of range avoids constructing the list
	for i in chain([2],xrange(3,n+1,2)):
		s = 0
		while n%i == 0: #if the number is divisible, then this is a prime factor, keep dividing untill possible.
			n /= i
			s += 1
		#result.extend([i]*s) #avoid another for loop
		if s > 0 : 
			result.append([i, s])
			noDiv = noDiv * (s + 1)
	if n==1:
		return noDiv
		#return result

#Utility function for future use.
def factorise(n):
	return filter(lambda x: (n % x) == 0, range(1,((n + 1))))

def tr():
	i = lastTr = 0
	while 1:
		i = i + 1
		lastTr = lastTr + i
		yield lastTr

def pr12():
	from time import gmtime, strftime
	trNos = tr()
	maxCt = ct = 0
	while ct < 500:
		currentNo = trNos.next()
		ct = noOfDivs(currentNo)
		if ( ct > maxCt ):
			maxCt = ct
			print "New max - Number = " + str(currentNo) + "; with total ops " + str(ct)
		if ( (currentNo % 1000) == 0 ):
			print "Analysing " + str(currentNo) + " at " + strftime("%Y-%m-%d %H:%M:%S", gmtime())

	return (trNos.next() - 1)