# Problem 87
# Prime power triples

import math
import time
start = time.time()

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

def get_powers(rangy,exponent,primes):
    listy = []
    for x in primes:
        if x ** exponent >= rangy:
            break
        listy.append(x ** exponent)
    return listy

rangy = 5 * 10 ** 7

primes = get_primes(math.ceil(rangy ** 0.5)+1)
print(f'got the primes below {rangy ** 0.5}')

squares = get_powers(rangy,2,primes)
cubes = get_powers(rangy,3,primes)
fourths = get_powers(rangy,4,primes)

print(f'squares length {len(squares)}')
print(f'cubes length {len(cubes)}')
print(f'fourths length {len(fourths)}')
print(f'total potential combinations: {len(squares) * len(cubes) * len(fourths)}\n')

sum_list = []

for sqr in squares:
    for cub in cubes:
        for fou in fourths:
            temp_sum = sqr + cub + fou
            if temp_sum >= 50_000_000:
                break
            sum_list.append(temp_sum)

print(f'\nGot all {len(sum_list)} sums in {time.time() - start} seconds')

sum_set = set(sum_list)
print(f'\nConverted list to set in {time.time() - start} seconds')

final_list = list(sum_set)
print(f'\nConverted set back to FINAL LIST in {time.time() - start} seconds\n')

print(len(final_list))


print(f'Done in {time.time() - start} seconds')

