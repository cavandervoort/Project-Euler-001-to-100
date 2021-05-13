# Problem 50
# Consecutive prime sum

def getPrimes(n):
    primeArray = [0,0] + [1] * (n-1)
    for pos in range(2, int(n ** 0.5)+1):
        if primeArray[pos] == 1:
            testNum = pos * 2
            while testNum < n + 1:
                primeArray[testNum] = 0
                testNum += pos
    primes = []
    for pos in range(2,n+1):
        if primeArray[pos] == 1:
            primes.append(pos)
    return primes

limit = 1_000_000

# Find Primes
primes = getPrimes(limit)
primesDict = {}
for prime in primes:
    primesDict[prime] = None

primeSum = 0
primeCountLimit = 0
while primeSum < limit:
    primeSum += primes[primeCountLimit]
    
    if primeSum > limit:
        break
    primeCountLimit += 1

countMax = 0
sumMax = 0
primeSumHolder = primeSum

for x in range(100):
    primeSum = primeSumHolder

    for num in range(primeCountLimit,0,-1):
        if primeSum in primesDict:
            if num - x > countMax:
                countMax = num - x
                sumMax = primeSum
            break
        primeSum -= primes[num]
        
    primeSumHolder -= primes[x]

print(sumMax)
