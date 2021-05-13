# Problem 37
# Truncatable primes

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

def hasBadDigit(num,badDigits):
    count = 0
    for char in str(num):
        if char in badDigits:
            return True
        elif char == '2' and count != 0:
            return True
        count += 1
    if str(num)[0] == '1' or str(num)[-1] == '1':
        return True
    return False

limit = 1_000_000

# find Primes
primes = getPrimes(limit)
print(f'found the primes below {limit} in {time.time() - start} seconds') 

# remove any primes with a bad digit
badDigits = ['0', '4', '6', '8']
allPrimesDict = {2:None}
primesDict = {2:None}
for prime in primes:
    allPrimesDict[prime] = None
    if hasBadDigit(prime,badDigits):
        continue
    else:
        primesDict[prime] = None
print(f'removed primes with bad digits in {time.time() - start} seconds') 

# sum truncatable primes
primesSum = 0
truncatablePrimes = []
for prime in primesDict:
    if prime < 10:
        continue

    isTruncatable = True

    if isTruncatable:
        # pop from the left
        digitsLeft = [x for x in str(prime)]
        digitsLeft.pop(0)
        while digitsLeft != []:
            testNum = ''.join(digitsLeft)
            if int(testNum) not in allPrimesDict:
                isTruncatable = False
                break
            digitsLeft.pop(0)
    
    if isTruncatable:
        # pop from the right
        digitsRight = [x for x in str(prime)]
        digitsRight.pop(-1)
        while digitsRight != []:
            testNum = ''.join(digitsRight)
            if int(testNum) not in allPrimesDict:
                isTruncatable = False
                break
            digitsRight.pop(-1)
    
    if isTruncatable:
        primesSum += prime
        truncatablePrimes.append(prime)

print(truncatablePrimes)
print(f'the primesSum is {primesSum}')
print(f'all finished in {time.time() - start} seconds')
