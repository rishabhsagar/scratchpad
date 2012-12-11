def maxInLine(strOfNums):
	#Given a string of numbers this function return the max number in the string.
	#The string is expected to be delimited by spaces
	nums = map(lambda x: int(x), strOfNums.split(" "))
	nums.sort(reverse=True)
	return nums[0]

def processRow(prevMaxPos, currentRow):
	#Given a string of numbers and pos of prev max number, returns the val and pos of max number in the current row.
	currentMaxPos1 = prevMaxPos
	currentMaxPos2 = prevMaxPos + 1

	maxPos = -1

	currentRowNums = map(lambda x: int(x), currentRow.split(" "))
	if ( currentRowNums[currentMaxPos1] > currentRowNums[currentMaxPos2] ):
		maxPos = currentMaxPos1
	else:
		maxPos = currentMaxPos2
	
	#print "Max position found to be : " + str(maxPos)
	#print "Value at this position :" + str(currentRowNums[maxPos])

	return [maxPos, currentRowNums[maxPos]]


running_total = 0
currentMaxVal = 0
prevPos = -1

with open("C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\euler\\pr18.data", "r") as i:
	all_lines = i.readlines()
	for line in all_lines:
		[prevPos, currentMaxVal] = processRow(prevPos, line)
		print "Traversing through " + str(currentMaxVal)
		running_total = running_total + currentMaxVal
	print running_total

