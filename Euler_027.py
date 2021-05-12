# Problem 27
# Quadratic primes

import time
start = time.time()

limit = 1000

# make lists for a and b (a is odd and b is prime)

aList = [x for x in range(-limit+1, limit-1, 2)]
bList = []
primes = []
for num in range(2, int(limit * 10)):
    isPrime = True
    for prime in primes:
        if num % prime == 0:
            isPrime = False
    if isPrime == True:
        if num < 1000:
            bList.append(num)
        primes.append(num)      
        
# go through all the combos

countMax = [10, 0, 0] # [n_max, a, b]

for a in aList:
    for b in bList:
        nMax = 0
        
        for n in range(100):
            if n ** 2 + (a * n) + b not in primes:
                break        
            nMax += 1
        
        if nMax > countMax[0]:
            countMax = [nMax, a, b]

print(f'nMax is {countMax[0]} and product of coefficients is {countMax[1] * countMax[2]}')
