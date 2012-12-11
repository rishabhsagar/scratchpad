def listSpiralDiags(limit):
	#Set up intial conditions for the iteration
	hopLen = 2
	run = 1
	current = 1
	elemList = [1]

	while current < limit:
		if run <= 4:
			current = current + hopLen
			run = run + 1
			elemList.append(current)
		else:
			run = 1
			hopLen = hopLen + 2

		#Check if we have reached the limit.
		if current >= limit:
			break

	#Print the elemList and sum up the elements.
	print elemList
	return reduce(lambda x,y: x+y, elemList)