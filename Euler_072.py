# Problem 72
# Counting fractions

import time
start = time.time()

print("This will take ~15 seconds")

# The answer is the sum of all the lower "no common factors" numbers for each number from 1 to 1,000,000.

def prime_test(x,primes):
    factors = []
    is_prime = True
    temp_x = x
    for prime in primes:
        if x % prime == 0:
            factors.append(prime)
            while temp_x % prime == 0:
                temp_x /= prime
            is_prime = False
    if temp_x > 1:
        factors.append(int(temp_x))
    return is_prime,factors

def rel_primes(x,prime_factors):
    num_rel_primes = x
    for fact in prime_factors:
        num_rel_primes *= (fact - 1) / fact
    return int(num_rel_primes)

reduced_proper_fractions = 1
rangy = 1000001
primes = [2]
prime_factors = [ [] for _ in range(rangy)]
prime_factors[2].append(1)
for x in range(3,rangy):
    is_prime,prime_factors[x] = prime_test(x,primes)
    
    rel_primes_x = rel_primes(x,prime_factors[x])
    if is_prime == True and x < rangy ** 0.5:
        primes.append(x)

    reduced_proper_fractions += rel_primes_x

print(f'Total Reduced Proper Fractions: {reduced_proper_fractions}')
print(f'Done in {time.time() - start} seconds') 
