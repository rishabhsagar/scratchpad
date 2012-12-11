

i = open("C:\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\min_sacalar_prod\\A-large-practice.in","r")
o = open("C:\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\min_sacalar_prod\\A-large-practice.out", "w")

# read the total number of the cases in the input file
test_cases = i.readline()
print "Total number of test cases in this test file : " + test_cases

line_count = 1

for case in range(1,int(test_cases) + 1):

    #read in the total number of points in this vector
    ch_count = i.readline()
    
    # read the vectors, now split into individual points
    v1 = map(lambda x: int(x), i.readline().split())
    v2 = map(lambda x: int(x), i.readline().split())

    #Sort first vector in asc
    v1.sort()
    #Sort the second vector in desc
    v2.sort(reverse=True)

    out = "Case #" +  str(line_count) + ": " + str(reduce(lambda x, y: x + y, map(lambda (x,y): x * y,zip(v1,v2))))

    #Zip the vectors and prod them
    print out
    
    #Write into output file
    o.write(out + "\n")

    #Increment the line count
    line_count += 1

#Close the file handlers
i.close()
o.close()