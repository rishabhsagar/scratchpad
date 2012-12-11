# Create a file descriptor to read in the file
f = open('C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\amazon\\data\\input00.txt','r')

# Read in total count of numbers and diff from first line
(numCount, diff) = map(lambda x: int(x), f.readline().rstrip().split(' '))

#Read in the input array.
inp = map(lambda x: int(x), f.readline().rstrip().split(' '))

# For each element in the input set; {if (x + 2) -> inputset}, print the element {directly printing length}
print len(filter(lambda x: (x + diff) in inp, inp))

#Close the file descriptor
f.close()