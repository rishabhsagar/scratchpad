import math

def isPrime(num):
  '''@Summary: Checks if a given number is prime.
     @Returns: Returns True if Prime, else False.
     @Attention: Returns False for 1 and negative numbers.
  '''

  if ( num <= 1 ): return False 

  upperLimit = int(math.sqrt(num) + 1) # Upper limit is the max value to be checked.
  
  for x in range(2, upperLimit):
    if ( (num % x) == 0 ): return False

  return True # If execution comes to this line, then num in Prime.

def rotate(num):
  '''@summary: Rotates a given number's digits.
     @Returns: A list of complete rotated numbers.
  '''

  rot_nums = list() # List to return
  num = str(num) # Convert the number to string type
  for i in range(0, len(num)):
    num = num[1:] + num[0]
    rot_nums.append(int(num))

  return rot_nums

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

    return primeList


if __name__ == "__main__":
  prime_list = primeUpto(1000000) # Create a list of prime numbers upto 1M.
  count = 0
  cir_prime = []

  for prime in prime_list:
    if ( prime in cir_prime ):
      count = count + 1
      print str(prime) + " is a circular prime, pre-cached, did not check."
      continue # known prime, do not check.

    rot_prime = rotate(prime)
    if ( False not in map(isPrime, rot_prime)):
      count = count + 1
      print str(prime) + " is a circular prime."
      cir_prime = cir_prime + rot_prime # Adding all rotations to cir_prime list.  These need not be checked again.

  print "---Found " + str(count) + " circular primes.---"
