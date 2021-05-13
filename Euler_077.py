# Problem 77
# Prime summations

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


size = 100
primes = get_primes(size)

# the organization in combos is: combos[the sum of all blocks][size of larges block]
combos = [ [ 0 for highest in range(size) ] for summy in range(size)] 

# for row in range(size):
    # print(combos[row])

count_max = 1

for turn in range(1,size):
    if turn in primes:
        combos[turn][turn] = 1
    
    for new_block in primes:
        
        for old_highest in range(1,new_block+1):
            combos[turn][new_block] += combos[turn-new_block][old_highest]

    final_count = 0
    for highest in range(1,turn):
        final_count += combos[turn][highest]
    
    if final_count > count_max:
        count_max = final_count
        if count_max > 5_000:
            print(f'There are {final_count} ways {turn} can be written as a sum of at least two primes.')
            break
