# Problem 70

import time
start = time.time()

print("This will take ~25 seconds")

# Step 1: find the relative primes for each number below 10 ** 7
limit = 10_000_000
array = [x for x in range(limit)]
array[1] = 0
for i in range(2, limit):
    if i == array[i]:
        for j in range(i, limit, i):
            array[j] = array[j] / i * (i-1)

# Step 2: check the array for permutations
pos_max = 0
perm_max = 0
ratio_min = 10
for pos in range(3,limit,2):
    if pos % 3 == 0 or pos % 5 == 0 or pos % 7 == 0:
        continue
    pos_sort = sorted([x for x in str(pos)])
    perms_sort = sorted([x for x in str(int(array[pos]))])
    if pos_sort == perms_sort:
        if pos / array[pos] < ratio_min:
            ratio_min = pos / array[pos]
            pos_max = pos
            perm_max = int(array[pos])

print(f'Final ratio min of {ratio_min} with pos {pos_max} and perms {perm_max}')
print(f'Done in {time.time() - start} seconds')  
