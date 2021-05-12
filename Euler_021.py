# Problem 21
# Amicable numbers

# create dictionary of num of divisors for all numbers below limit
limit = 10000
countDivisors = {}
for i in range(1,limit):
    sumDiv = 0
    for div in range(1,round(i / 2 + 1)):
        if i % div == 0:
            sumDiv += div
    countDivisors[i] = sumDiv 

# search for amicable pairs and add any to running sum
sumAmicablePairs = 0
for i in range(1,limit):
    if countDivisors[i] < limit:  
        if i == countDivisors[countDivisors[i]] and i < countDivisors[i]:
            sumAmicablePairs += i + countDivisors[i]

print(f'Sum of amicable numbers under {limit}: {sumAmicablePairs}')