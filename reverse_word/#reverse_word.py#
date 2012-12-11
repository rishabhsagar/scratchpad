# open input file for reading (Remember to close this!)
f = open("C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\B-large-practice.in", "r")
o = open("C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\B-large-practice.out", "w")

# Read the total number of test cases in this file.
test_cases = f.readline()

#print "Total number of test cases in this input file : " + test_cases

for case in range(1, int(test_cases) + 1):
	current_str = f.readline().rstrip().split(" ")
	current_str.reverse()
	print "Case #" + str(case) + ": "+ ' '.join(current_str) + "\n"
	o.writelines("Case #" + str(case) + ": "+ ' '.join(current_str) + "\n")
f.close()
o.close()
