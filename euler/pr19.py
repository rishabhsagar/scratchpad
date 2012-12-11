datesArray = []

leapMonths = [31,29,31,30,31,30,31,31,30,31,30,31]

nonLeapMonths = [31,28,31,30,31,30,31,31,30,31,30,31]

#Build Dates array.
for year in range(1901,2001):
	if ( year % 4 == 0 ):
		for mn in leapMonths:
			for day in range(1, mn + 1):
				datesArray.append(day)
	else:
		for mn in nonLeapMonths:
			for day in range(1,mn + 1):
				datesArray.append(day)


#We know that, 1 Jan 1900 was a Monday; so Jan 6, 1901 was Sunday.  
#So in our datesArray, every [(i * 7) - 2] must be a Sunday

Sunday = []

for day in range(1, len(datesArray) / 7 + 2):
	Sunday.append(datesArray[(day * 7) - 2])

# Now we have a list of all dates on which Sundays fell in the date range.
# filter out the dates when the Sundays fell on 1st.

print len(filter(lambda x: x == 1, Sunday))
