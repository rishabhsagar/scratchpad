def primeUpto(n):
	#Start with a known primeList
	primeList = [2,3,5,7,11,13]
	invEnd = 0
	while invEnd < n:

		#Start from last known prime, and end at 2ice that prime
		invStart = primeList[len(primeList) - 1]
	
		if pow(invStart,2) < n:
			invEnd = pow(invStart,2)
		else:
			invEnd = n

		
		#Build required range
		sv = range(invStart, invEnd+1)

		#For each known prime, execute sieve of Eratosthenes (remove multiples of known primes)
		for prime in primeList:
			sv = filter(lambda x: (x % prime) != 0, sv)
		
		#Numbers surviving in the list are primes, add these to known list of primes
		primeList = primeList + sv
	
	#Sum of known primes
	return reduce(lambda x, y: x+y, primeList)