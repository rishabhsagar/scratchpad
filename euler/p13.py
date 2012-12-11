#Very cheap method described below, But I had to leave office early.  Please understad :)

#Open the file containing the digits
#i = open("C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\euler\\p13.data", "r")

# Read the total number of test cases in this file.
#number = long(i.readline())

#Initialise required variables
running_total = 0
current_digit = 49

#read each line and add up the current_digit to running total
with open("C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\euler\\p13.data", "r") as i:
	for ln in range(1,101):
		running_total = running_total + long(i.readline())
	print str(running_total)[:10]
