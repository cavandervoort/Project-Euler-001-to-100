# Problem 69
# Totient maximum

# NOTE: I originally solved this by using a spreadsheed and assuming that the number would be 
# made up of only single primes, and i went as high as I could using only the lowest primes. 

# NOTE: On 2/20/2021, I came up with a code-based solution.

import time
start = time.time()

# Step 1: find the relative primes for each number below 10 ** 6
limit = 1000001
array = [x for x in range(limit)]
array[1] = 0
for i in range(2, limit):
    if i == array[i]:
        for j in range(i, limit, i):
            array[j] = array[j] / i * (i-1)

# Step 2: find the value of n ≤ 1,000,000 for which n/totients(n) is a maximum.
pos_max = 0
perm_max = 0
ratio_max = 1
for pos in range(2,limit,2):
    
    if pos / array[pos] > ratio_max:
        ratio_max = pos / array[pos]
        pos_max = pos
        perm_max = int(array[pos])

print(f'Final ratio max of {ratio_max} with pos {pos_max} and perms {perm_max}')
print(f'Done in {time.time() - start} seconds') 
