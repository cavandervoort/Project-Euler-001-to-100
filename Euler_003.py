# Problem 3
# Largest prime factor

primes = [2]
bigNum = 600851475143
largestFactor = 1

for num in range(3,100000,2):
    for prime in primes:
        if num % prime == 0:
            break
        elif prime > num ** 0.5:
            primes.append(num)
            if bigNum % num == 0:
                largestFactor = num
                while bigNum % num == 0:
                    bigNum /= num
            break
    
    if bigNum == 1:
        break
        
print(largestFactor)