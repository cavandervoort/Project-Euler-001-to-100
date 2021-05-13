# Problem 85
# Counting rectangles

import time
start = time.time()

temp_sum = 0
leng_dic = {}
for x in range(1,2001):
    temp_sum += x
    leng_dic[x] = temp_sum

x = 2000
y = 1
maxes = []
abs_min = 2000000
while x >= y:
    rectangles = leng_dic[x] * leng_dic[y]
    
    abs_val_temp = abs(rectangles - 2000000)
    if abs_val_temp <= abs_min:
        abs_min = abs_val_temp
        maxes = [x,y,abs_min,x*y]
        # print(f'new record! x = {x} & y = {y}, new min is {abs_min}, and area is {x*y}')
    
    if rectangles >= 2000000:
        x -= 1
    
    if rectangles < 2000000:
        y += 1

print(f'x = {maxes[0]} & y = {maxes[1]}, the abs_diff is {maxes[2]}, and area is {maxes[3]}')

print(f'\ndone in {time.time() - start} seconds') 
