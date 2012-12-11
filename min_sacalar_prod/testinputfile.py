#Open the input file to read
i = open("C:\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\min_sacalar_prod\\A-small-practice.in","r")

#Read the total number of testcases in this file.

test_cases = i.readline()
print "Total number of test cases : " + test_cases

vector1 = i.readline()

v1 = map(lambda x: int(x),i.readline().split())
v2 = map(lambda x: int(x), i.readline().split())

v1.sort()
v2.sort(reverse=True)

print v1
print v2

print reduce(lambda x, y: x + y, map(lambda (x,y): x * y, zip(v1,v2)))

i.close()
