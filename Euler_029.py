# Problem 29
# Distinct powers

lowerBound = 2
upperBound = 100
aToBPowers = {}

for a in range (lowerBound, upperBound+1):
    for b in range (lowerBound, upperBound+1):
        aToB = a ** b
        aToBPowers[aToB] = 0

print(f'The number of distinct terms is {len(aToBPowers)}.')
