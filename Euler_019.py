# Problem 19
# Counting Sundays

lenMon = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

weekday = 2 # 1 Jan 1901 was a Tuesday

firstSundays = 0 # Sundays that fell on the first of the month

for year in range(1901,2001):
    for month in range(12):
        for day in range(lenMon[month+1]):
            if day == 0 and weekday % 7 == 0:
                firstSundays += 1
            weekday += 1

print(firstSundays)