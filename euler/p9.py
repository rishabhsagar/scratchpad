#Problem solved by estimating that:
#	since a + b + c = 1000 and a < b < c; a and b must be less that 500

print (a*b*(1000 - a - b) for a in range(1,501) for b in range(1,501) if (pow(a,2) + pow(b,2) == pow((1000 - a - b),2))).next()