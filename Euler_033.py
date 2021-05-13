# Problem 33
# Digit cancelling fractions

curious_fracs = []

for numer in range(10,100):
    str_numer = str(numer)
    for denom in range(numer + 1, 100):
        str_denom = str(denom)
        
        if str_numer[0] == str_denom[1]:
            if int(str_numer[1]) / int(str_denom[0]) == numer / denom:
                curious_fracs.append([numer, denom])

        if str_numer[1] == str_denom[0] and int(str_denom[1]) != 0:
            if int(str_numer[0]) / int(str_denom[1]) == numer / denom:
                curious_fracs.append([numer, denom])

print(f'Curious fractions: {curious_fracs}\n')

big_numer = 1
big_denom = 1

for pair in curious_fracs:
    big_numer *= pair[0]
    big_denom *= pair[1]
    
print(f'the product of the curious fractions is: {big_numer}/{big_denom}\n')

primes = []
big_numer_drain = big_numer

for num in range(2,100):
    is_prime = True
    for prime in primes:
        if num % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
        while big_numer % num == 0 and big_denom % num == 0:
            big_numer /= num
            big_denom /= num
        while big_numer_drain % num == 0:
            big_numer_drain /= num
        if big_numer_drain == 1:
            break

print(f'the lowest common terms version of the product is: {int(big_numer)}/{int(big_denom)}') 
