# Problem 73
# Counting fractions in a range

def get_primes(rangy):
    primes = [2]
    for num in range(3, rangy, 2):  
        is_prime = True
        num_trip = num ** 0.5 + 1
        for prime in primes:
            if num % prime == 0:
                is_prime = False
            elif prime > num_trip:
                break
        if is_prime == True:
            primes.append(num)
    return primes

def get_factors(x,primes):
    factors = []
    temp_x = x
    for prime in primes:
        if x % prime == 0:
            factors.append(prime)
            while temp_x % prime == 0:
                temp_x /= prime
    if temp_x > 1:
        factors.append(int(temp_x))
    # print(f'the factors for {x} are {factors}')
    return factors

import time
start = time.time()

print("This will take ~15 seconds")

rangy = 12000
primes = get_primes(rangy+1)
count = 0
for den in range(2,rangy+1):
    den_factors = get_factors(den,primes)
    for num in range(1,den):
        if num <= den / 3:
            continue
        elif num >= den / 2:
            break
        else:
            is_reduced = True
            for factor in den_factors:
                if num % factor == 0:
                    is_reduced = False
                    break
            if is_reduced == True:
                count += 1
                # print(f'Found one: {num}/{den}')

print(count)
print(f'Done in {time.time() - start} seconds')
