# Problem 94
# Almost equilateral triangles

import time
start = time.time()

import math
max_perim = 10 ** 9
sum_count = 0

for a in range(2,math.floor(max_perim/3)+1):
    p = (3 * a - 1) / 2
    area = (p * (p - a) ** 2 * (p - (a - 1))) ** 0.5
    if area == round(area):
        # print(f'A triangle with sides {a}, {a}, & {a - 1}, with area {int(area)}')
        sum_count += int(p * 2)
    
    p += 1
    area = (p * (p - a) ** 2 * (p - (a + 1))) ** 0.5
    if area == round(area):
        # print(f'A triangle with sides {a}, {a}, & {a + 1}, with area {int(area)}')
        sum_count += int(p * 2)
        
    if a % 10_000_000 == 0:
        print(f'a is {a} at {time.time() - start} seconds')
    
print(f'\nThe sum of all perimeters is {sum_count}')    
print(f'\nThis took {time.time() - start} seconds')
