# The nth term of the sequence of triangle numbers is given by, tn = 0.5 * n(n+1); so the first ten triangle numbers are:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# 
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import string
import math

# Generate a char <-> number dictionary

alpha_dict = {}
for item in zip(string.ascii_uppercase, range(1,199)):
    alpha_dict[item[0]] = item[1]

def word_sum(word):
    return sum(map(lambda char: alpha_dict[char], list(word)))

def isTriangle(num):
    n = (math.sqrt(1.0 + (8.0 * num)) - 1.0) / 2.0
    if ( n == int(n)):
        return True
    else:
        return False

if __name__ == "__main__":
    # Collect words
    f = open("words.txt")
    words = f.readline().replace("\"","").split(",")

    # initialise counter
    num_of_triangles = 0

    # Check words, and maintain counter
    for word in words:
        if ( isTriangle(word_sum(word)) ): num_of_triangles = num_of_triangles + 1

    print "Number of triangle words: ", num_of_triangles
