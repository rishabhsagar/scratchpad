table = [[int(n) for n in s.split()] for s in open('C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\euler\\p67.data').readlines()]
 
for row in range(len(table)-1, 0, -1):
  for col in range(0, row):
    table[row-1][col] += max(table[row][col], table[row][col+1])
 
print "Answer to PE18 = ", table[0][0]