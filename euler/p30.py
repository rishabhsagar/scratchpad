def p30():
	ans = 0
	for number in range(2, 354295):

		# Create temp variable and reset sum to 0
		val = number
		sum = 0
		
		# Sum the fifth power of digits
		while val > 0:
			digit = val % 10
			val = val / 10
			sum = sum + (pow(digit, 5))
		
		if ( sum == number):
			print number
			ans = ans + number

	print "Total is : " + str(ans)

# 4150
# 4151
# 54748
# 92727
# 93084
# 194979
# Total is : 443839