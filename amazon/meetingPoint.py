# Create a file descriptor to read in the file
f = open('C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\amazon\\data\\meetingP_input00.txt','r')

# Read in total count of numbers and diff from first line
(numCount, diff) = map(lambda x: int(x), f.readline().rstrip().split(' '))