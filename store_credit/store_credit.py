from collections import deque
#funtion to find the key given the value
def find_key(dic, val):
    try:
        return[k for k, v in dic.iteritems() if v == val][0]
    except:
        return 0


#function to find the value given the key
def find_value(dic, val):
    return dic[key]

#function to delte item from
def del_val(dic, key):
    del dic[key]

#Function to add item into shelf
def add_val(dic,key,val):
    dic[key] = val

#Function to determine the credit item pair
def find_pair(dic,credit,case):

    # Create a static copy of the shelf
    current_shelf = dic
    
    # Now iterate thorugh each item to see if there is a match?
    for first_article in current_shelf:
        first_credit = int(dic[first_article]) #Cost of first item
        remainder_credit = str(credit - first_credit) #Search for item with this cost

        #DEBUG: print dic
        #DEBUG: print "\t Store credit : " + str(credit)
        #DEBUG: print "\t First Article location: " + str(first_article) + " costing " + str(dic[first_article])
        
        del_val(dic, first_article) # remove the first article from the shelf, otherwise it may get picked up again.

        #Search for another item with remainder credit
        #DEBUG: print "\t Searching for item of value : " + remainder_credit + " in following shelf."
        #DEBUG: print shelf

        second_article = find_key(dic,int(remainder_credit))

        #DEBUG: print "\t Value found as : " + str(second_article)

        #Add the value back into dic, to synch
        add_val(dic,first_article,first_credit)

        if ( second_article > 0):
            # print results to screen
            #print dic
            print "\t Store credit : " + str(credit)
            print "\t First Article location: " + str(first_article) + " costing " + str(first_credit)
            print "\t Second Article location: " + str(second_article) + " costing " + str(dic[second_article])

            if ((first_credit + dic[second_article]) == credit):
                print "\tCHECK!"

            article_list = []

            article_list.append(str(first_article))
            article_list.append(str(second_article))
            article_list.sort()
            print "Case #" + case + ": " + ' '.join(article_list)
            o.writelines("Case #" + case + ": " + ' '.join(article_list) + "\n")
            break #Can get out now.


# open input file for reading (Remember to close this!)
i = open("C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\store_credit\\A-large-practice.in", "r")
o = open("C:\\Documents and Settings\\ct057688\\My Documents\\Current Data\\self\\jam\\store_credit\\A-large-practice.out", "w")

# Read the total number of test cases in this file.
test_cases = i.readline()
#DEBUG: print "Total number of test cases in this input file : " + test_cases

# For each test case.
for case in range(int(test_cases)):

    #DEBUG: print "Case Number  : " + str(case + 1)

    # Read in the store credit
    store_credit=i.readline().rstrip()

    # Read in the total items in the store
    total_items = i.readline().rstrip()

    #Read in the different articles available
    item_list = i.readline().rstrip()

    shelf = {}
    for location,item in enumerate(item_list.split(" ")):
        shelf[location + 1] = int(item) #To preserve the logical shelf location.

    #DEBUG: print shelf

    find_pair(shelf,int(store_credit),str(case + 1))

    

#close the file handles
i.close()
o.close()
