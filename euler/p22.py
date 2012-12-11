import string

#Generate the dict of the values, keyed with characters.
alpha = list(string.uppercase[:26])
d = {}

for i in range(len(alpha)):
	d[alpha[i]] = i+1

#Parse out the names from the data file.
f = open("C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\euler\\p22.data","r")
names = f.readline()
names = names.replace('"','').split(',')
names.sort()
f.close()

print "Total number of names parsed", len(names)

#print "Running tests for 10 names"
#names = names[:10]

val = 0

for seq in range(1, (len(names)+1)):
	nm = names[seq - 1]
	val += seq * (reduce(lambda x,y: x+y, map(lambda x: d[x], nm)))

print "Total values:", val