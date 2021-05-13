# Helpful Functions

# Find Primes

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

# Get Prime Factors

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

# Greatest Common Divisor

def gcd(a,b):
    while b != 0: 
        print(f'at first, a is {a} and b is {b}, and a % b is {a % b}')
        a, b = b, a % b
        print(f'now, a is {a} and b is {b}')
    return a;

# Timer

import time
start = time.time()

print(f'Done in {time.time() - start} seconds')
