def primeUpto(n):
	#Start with a known primeList
	primeList = [2]

	#While we don't have enough prime numbers
	while len(primeList) < n:
		#Start from last known prime, and end at 2ice that prime
		invStart = primeList[len(primeList) - 1]
		invEnd = 2 * invStart
		
		#Build required range
		sv = range(invStart, invEnd+1)

		#For each known prime, execute sieve of Eratosthenes (remove multiples of known primes)
		for prime in primeList:
			sv = filter(lambda x: (x % prime) != 0, sv)
		
		#Numbers surviving in the list are primes, add these to known list of primes
		primeList = primeList + sv
	
	#Trim the list to only return required number of primes (last iterations may have yeilded more than required number of primes)
	return primeList[1:n]

if __name__ == "__main__":
	pl = primeUpto(300)
	print pl