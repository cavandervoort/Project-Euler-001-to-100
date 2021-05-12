# Problem 7
# 10001st prime

primes = [2]
primeCount = 1
num = 3
xthPrime = 10_001
while primeCount < xthPrime:
    isPrime = True
    for prime in primes:
        if num % prime == 0:
            isPrime = False
            break
        elif prime > num ** 0.5:
            break
    if isPrime:
        primes.append(num)
        primeCount += 1
        if primeCount > xthPrime - 1:
            print(f'prime number {primeCount} is {num}')
    num += 1
