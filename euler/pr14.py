# The following iterative sequence is defined for the set of positive integers:

# n n/2 (n is even)
# n 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 40 20 10 5 16 8 4 2 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE:Once the chain starts the terms are allowed to go above one million.

#Define the master dictionary
master = {1:1}

def genChain(n):
	currentNo = n
	chain = [n]
	
	while (currentNo != 1):
		if ( isEven(currentNo) ):
			currentNo = currentNo / 2
		else:
			currentNo = (currentNo * 3) + 1
		chain.append(currentNo)
	
	return chain


def isEven(number):
	if ( ( number % 2) == 0):
		return True
	else:
		return False

def CollatzChain(number):
	currentNo = number
	
	while 1:
		# Calculate next number in chain
		if (isEven(currentNo)):
			currentNo = currentNo / 2
		else:
			currentNo = (currentNo * 3) + 1
		
		# Yield next number in chain
		yield currentNo


def printChains(num):
	for i in range(1, num +1):
		print "[",i,",",len(genChain(i)),"] ->", genChain(i)

def noChainExistsFor(num):
	if ( num in master):
		return False
	else:
		return True

#Sample Chain
#master = {34:17, 4:2, 5:16, 7:22, 40:20, 10:5, 11:34, 13:40, 8:4, 16:8, 17:52, 52:26, 22:11, 2:1, 20:10, 26:13}
#Updates the master dict for num
def addToMaster(num):
		cChain = CollatzChain(num)
		currentNo = num
		
		while ( noChainExistsFor(currentNo) ):
			#print "Generating chain for", currentNo
			nextNo = cChain.next()
			master[currentNo] = nextNo

			if ( nextNo == 1):
				break
			else:
				currentNo = nextNo

# Pulls out chain from the master dict.  Number must be a key in the master.
def printFromMaster(num):
	if ( noChainExistsFor(num)):
		print "Master does not hold chain for", num
		return False
	else:
		chain = []
		currentNo = num
		
		while (currentNo != 1):
			chain.append(currentNo)
			currentNo = master[currentNo]
		
		return chain + [1]

# Generates master for all numbers upto num
# REMEBER to zero out a master before generating it.
def genMaster(num):

	for i in range(num, 0, -1):
		addToMaster(i)

# Returns a set of collatz leaf nodes (chain starters).  Master should have been generated.
def listLeafNodes():

	keys = set(master.keys())
	vals = set(master.values())

	#Turns out that the difference operations in sets are shite.
	#return keys.difference(vals)

	return [ x for x in keys if x not in vals]


def maxCollatzSeqSeed(numbers):
	maxSeed = 0
	maxSeqLen = 0

	for i in numbers:
		newLen = len(printFromMaster(i))
		if ( newLen > maxSeqLen):
			maxSeed = i
			maxSeqLen = newLen

	return [maxSeed, maxSeqLen]
