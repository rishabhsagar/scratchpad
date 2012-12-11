def sumOfProperDivs(num):
	#result to be returned.
	result = []

	#proper divs can be found untill num / 2
	maxRange = (num / 2) + 1

	# Sexy list comphrehensions baby! :P
	result = [x for x in range(1,maxRange) if num % x == 0]

	return reduce(lambda x,y: x+y, result)


amiciblePairs = []

for i in range(1,11):
	sopd = sumOfProperDivs(i)
	if ( sopd == sumOfProperDivs(sopd)):
		print i + " and " + sopd + " are amiciblePairs"