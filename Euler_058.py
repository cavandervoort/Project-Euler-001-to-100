# Problem 58

def get_primes(prime_search_range):
    primes = [2]
    for num in range(3, prime_search_range + 1, 2):  
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

def is_prime(num,primes,prime_search_range):
    if num < prime_search_range:
        if num in primes:
            return True
        else:
            return False        
    num_trip = num ** 0.5 + 1
    for prime in primes:
        if num % prime == 0:
            return False
        elif prime > num_trip:
            return True

import time
start = time.time()
     
count_prime = 0
count_not_prime = 1
circles_max = 100000
prime_search_range = circles_max * 2 + 1
primes = get_primes(prime_search_range)

for circ in range(1,circles_max+1):
    side_length = circ*2+1
    num_list = []
    num_list.append(((2*circ) ** 2 + 1 + (2*circ - 1) ** 2) / 2)
    num_list.append((2*circ) ** 2 + 1)
    num_list.append(((2*circ) ** 2 + 1 + (2*circ + 1) ** 2) / 2)
    num_list.append((2*circ + 1) ** 2)
    
    for num in num_list:
        if is_prime(num,primes,prime_search_range):
            count_prime += 1
        else:
            count_not_prime += 1
        
    if count_prime / (count_prime + count_not_prime) < 0.1:
        break

print (f'At side length {side_length}, the ratio is {count_prime / (count_prime + count_not_prime)}')        
print(f'Done in {time.time() - start} seconds') 
