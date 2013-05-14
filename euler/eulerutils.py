import math

def isPrime(num):
  '''@Summary: Checks if a given number is prime.
     @Returns: Returns True if Prime, else False.
     @Attention: Returns False for 1 and negative numbers.
  '''

  if ( num <= 1 ): return False 
  if num == 2 : return True
  if ( num % 2 == 0): return False  # Quick check for even numbers.

  upperLimit = int(math.sqrt(num) + 1) # Upper limit is the max value to be checked.
  
  for x in range(2, upperLimit):
    if ( (num % x) == 0 ): return False

  return True # If execution comes to this line, then num in Prime.

#Older, incorrect method.
def primesUpto(num):
    '''
    @Summary: Generates primes upto num.
    @Return: Returns prime numbers upto num 
    '''

    nums = range(2,num) #Generate a list of all nums
    nums = filter(lambda x: x % 2 !=0, nums)    #cuts problem by half.
    primes = [2]   #List of primes, initialised with a few primes.

    while len(nums) != 0:
        nums = filter(lambda x: x % primes[-1] != 0, nums)
        if len(nums) > 0: primes.append(nums[0])

    return primes

def iprimesUpto(limit):
    is_prime = [True] * limit
    for n in range(2, limit):
        if is_prime[n]:
            yield n
            for i in range(n*n, limit, n): # start at ``n`` squared
                is_prime[i] = False
