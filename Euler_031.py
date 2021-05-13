# Problem 31
# Coin sums

import math
import time
start = time.time()

p_left = 200 # makes it flexible for how many p are left
count = 1 # starts at 1 b/c there is one path if the 200p is used

# start w 100p coin, then 50p coin, through 1p coin

for count_100 in range(math.floor(p_left/100) + 1):
    p_left_100 = p_left - count_100 * 100
    if p_left_100 == 0:
        count += 1
        continue
    for count_50 in range(math.floor(p_left_100/50) + 1):
        p_left_50 = p_left_100 - count_50 * 50
        if p_left_50 == 0:
            count += 1
            continue  
        for count_20 in range(math.floor(p_left_50/20) + 1):
            p_left_20 = p_left_50 - count_20 * 20
            if p_left_20 == 0:
                count += 1
                continue
            for count_10 in range(math.floor(p_left_20/10) + 1):
                p_left_10 = p_left_20 - count_10 * 10
                if p_left_10 == 0:
                    count += 1
                    continue           
                for count_5 in range(math.floor(p_left_10/5) + 1):
                    p_left_5 = p_left_10 - count_5 * 5
                    if p_left_5 == 0:
                        count += 1
                        continue  
                    for count_2 in range(math.floor(p_left_5/2) + 1):
                        p_left_2 = p_left_5 - count_2 * 2
                        if p_left_2 == 0:
                            count += 1
                            continue                      
                        for count_1 in range(math.floor(p_left_2/1) + 1):
                            p_left_1 = p_left_2 - count_1 * 1
                            if p_left_1 == 0:
                                count += 1
                                continue                      

print(f'ways count: {count}')
print(f'it took {time.time() - start} seconds')