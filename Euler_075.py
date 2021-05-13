# Problem 75
# Singular integer right triangles

import math
import time
start = time.time()

# I would like to improve the speed here
print("This may take around 1 hour, so please be patient")

max_length = 1_500_000
r_max = max_length/5.828
length_counter_dict = {}

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
                    if temp_length in length_counter_dict:
                        length_counter_dict[temp_length] = 0
                    else:
                        length_counter_dict[temp_length] = 1

    if r % 10_000 == 0:
        print(f'{"%.1f" % (100*r/r_max)}% done after {time.time() - start} seconds')

count = 0
for key in length_counter_dict:
    if length_counter_dict[key] == 1:
        count += 1

print(f'\nI found {count} lengths with exactly 1 right triangle in {time.time() - start} seconds')
