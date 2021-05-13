# Problem 41 - May 2021
# Pandigital prime

import time
start = time.time()

def getPrimes(n):
    primeArray = [0,0] + [1] * (n-1)
    primes = []
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

def isPandigital(n,panArr):
    digList = [char for char in str(n)]
    digList.sort()
    if digList in panArr:
        return True
    return False

limit = 10_000_000

# get primes below limit
primes = getPrimes(limit)
primes.reverse()

# create lists of pandigital digits
panArr = []
tempArr = []
for dig in range(1,10):
    tempArr.append(str(dig))
    panArr.append([char for char in tempArr])

for prime in primes:
    if isPandigital(prime,panArr):
        print(prime)
        break

print(f'Done in {time.time() - start} seconds')
