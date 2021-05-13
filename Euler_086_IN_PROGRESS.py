# Problem 86 - attempt for speed
# Cuboid route

import math
import time
start = time.time()

r_max = 1_000
count = 0

for r in range(2,math.floor(r_max)+1,2):
    st = r ** 2 / 2
    for s in range(1,math.floor(st ** 0.5)+1):
        if st % s == 0:
            t = st / s
            a = r + s
            b = r + t
            c = r + s + t
            if a ** 2 + b ** 2 == c ** 2:
                temp_length = int(a + b + c)
                if temp_length <= max_length:
                    length_counter[temp_length] += 1
                    count += 1

    if r % 100 == 0:
        print(f'At M = {st}, count is {count}, found in {time.time() - start} seconds')
    if count >= 1000:
        print(f'\nfound 1000 at M = {st}')
        break


print(f'\nI found {length_counter.count(1)} lengths with exactly 1 right triangle\n')
print(f'I found {count} right triangles within length {max_length} in {time.time() - start} seconds')


