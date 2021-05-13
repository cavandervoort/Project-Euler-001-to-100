# Problem 32
# Pandigital products

# get list of unusual products

import math
import time
start = time.time()

def is_pandigital(n1, n2, prod):
    digitsStr = str(n1) + str(n2) + str(prod)
    digitsArr = [char for char in digitsStr]
    if len(set(digitsArr)) == 9 and '0' not in digitsArr:
        return True
    else:
        return False
    
pandigitalProducts = []

for p_1 in range(2,99):
    
    range_2_lower = 123
    if p_1 < 10:
        range_2_lower = 1234
    range_2_upper = math.ceil(9999/p_1)+1
        
    for p_2 in range(range_2_lower, range_2_upper):
        prod = p_1 * p_2
        if is_pandigital(p_1, p_2, prod) == True:
            if prod not in pandigitalProducts:
                pandigitalProducts.append(prod)

print(f'The sum of the unusual products is {sum(pandigitalProducts)}')
