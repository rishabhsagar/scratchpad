import math


def isPerfectSquare(num):
	if (int(math.sqrt(num)) == math.sqrt(num)):
		return True
	else:
		return False

#Problem can be solved by bruteforcing.