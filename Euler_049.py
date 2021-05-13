# Problem 49
# Prime permutations

rangy = 10000
primes = [2]
for num in range(3, rangy, 2):  
    num_root = round(num ** 0.5 + 1)
    is_prime = True
    for prime in primes:
        if prime > num_root:
            break
        if num % prime == 0:
            is_prime = False
    if is_prime == True:
        primes.append(num)

four_dig_primes = []
for prime in primes:
    list_prime = [char for char in str(prime)]
    if len(list_prime) != 4:
        continue
    else:
        four_dig_primes.append(prime)

concat_list = []
for prime in four_dig_primes:
    perms = []
    for first in range(4):
        for second in range(3):
            for third in range(2):
                temp_list = [char for char in str(prime)]
                temp = ''
                temp += temp_list.pop(first)
                temp += temp_list.pop(second)
                temp += temp_list.pop(third)
                temp += temp_list.pop(0)
                perms.append(int(temp))
                
    perms_set_list = sorted(list(set(perms)))
    
    prime_perms = []
    for perm in perms_set_list:
        if perm in primes:
            prime_perms.append(perm)
    
    for x in range(0,len(prime_perms)-2):
        for y in range(x+1,len(prime_perms)-1):
            for z in range(y+1,len(prime_perms)):
                if prime_perms[z] - prime_perms[y] == prime_perms[y] - prime_perms[x]:
                    concat = str(prime_perms[x]) + str(prime_perms[y]) + str(prime_perms[z])
                    if len(concat) == 12:
                        concat_list.append(concat)

concat_list = sorted(list(set(concat_list)))
print(concat_list[1])
