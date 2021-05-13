# Problem 35
# Circular primes

import time
start = time.time()

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

def hasEven(num,evens):
    for char in str(num):
        if char in evens:
            return True
    return False

limit = 1_000_000

# find Primes
primes = getPrimes(1_000_000)
print(f'found the primes below {limit} in {time.time() - start} seconds') 

# remove any primes with an even digit
evens = ['0', '2', '4', '6', '8']
primesDict = {2:None}
for prime in primes:
    if hasEven(prime, evens):
        continue
    else:
        primesDict[prime] = None
print(f'removed primes with an even digit in {time.time() - start} seconds') 

# find circular primes
count = 0
for prime in primesDict:
    isCircular = True
    primeStr = str(prime)
    for shift in range(1, len(primeStr)):
        test = ''
        for pos in range(len(primeStr)):
            test += primeStr[pos-shift]
        if int(test) not in primesDict:
            isCircular = False
            break
    if isCircular:
        count += 1

print(f'found a total of {count} circular primes in {time.time() - start} seconds')
