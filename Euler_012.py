# Problem 12
# Highly divisible triangular number

import time
start = time.time()

def get_primes(n):
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

def getPrimeFactors(num,primes):
    primeFactorsDict = {}
    for prime in primes:
        if num % prime == 0:
            factorCount = 0
            while num % prime == 0:
                factorCount += 1
                num /= prime
            primeFactorsDict[prime] = factorCount
            if prime > num ** 0.5:
                break
    num = int(num)
    if num > 1:
        primeFactorsDict[num] = 1
    return primeFactorsDict
    
def countFactors(primeFactors):
    factors = 1
    for key in primeFactors:
        factors *= (primeFactors[key] + 1)
    return factors

# get prime numbers
primeMax = 10_000
primes = get_primes(primeMax)

# while building triangle numbers of increasing size, get prime factors to calc total factors
triNum = 0
factors = 0
count = 1
divisorsSought = 500
while factors <= divisorsSought:
    
    # building triangle numbers
    triNum += count
    count += 1
    
    # get prime factors
    primeFactors = getPrimeFactors(triNum,primes)
    
    # calculate total factors
    factors = countFactors(primeFactors)
        
print(f'Lowest triangle number with > {divisorsSought} divisors: {triNum}')
print(f'Done in {time.time() - start} seconds')