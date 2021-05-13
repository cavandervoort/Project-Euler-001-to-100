# Problem 47
# Distinct primes factors

primes = [2]
int_list = [-8,-6,-4,-2]

for num in range(3,1000000):
    num_check = num
    is_prime = True
    count_distinct = 0
    
    for prime in primes:
        
        if num_check % prime == 0:
            is_prime = False
            count_distinct += 1 
            while num_check % prime == 0:     
                num_check /= prime
            if count_distinct > 4:
                break
        if prime > num_check ** 0.5:
            if num_check > 1:
                count_distinct += 1
            break
    
    if count_distinct == 4:
        int_list.append(num)  
        if int_list[-1] - int_list[-4] == 3:
            print(f'The con-nums are {int_list[-1]}, {int_list[-2]}, {int_list[-3]}, and {int_list[-4]}.')
            break

    elif is_prime == True:
        primes.append(num)
