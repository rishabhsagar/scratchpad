#Create the initial dictionry required.
wDict = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen", 20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety", 100 : "hundred", 1000 : "onethousand"}

def numToWords(num):
     wNum = ""
     if num in wDict.keys():
          return len(wDict[num])
     elif len(str(num)) == 2:
          return handleTens(num)
     elif len(str(num)) == 3:
          wNum = wDict[(num / 100)]    #Extracts MSB
          wNum += "hundredand"         #adds required chars
          return len(wNum) + handleTens(num - ((num / 100) * 100))

def handleTens(num):
     wNum = ""
     wNum = wDict[(num / 10) * 10]      #Extracts MSB
     if wNum == "zero":
          wNum = ""
     if num % 10 != 0:
          wNum += wDict[num % 10]            #Extracts LSB
     return len(wNum)


ct = 0

for i in range(1,1001):
     ct += numToWords(i)


# ninehundredandtwentythree
# onehundredandtwentythree
# onehundredandsix
# onehundredandninetysix
# fivehundredandfiftyfive
# fourhundredandthirtytwo
# eightyeight
# sixhundredandsix
# ninehundredandnine
# twenty