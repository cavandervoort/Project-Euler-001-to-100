# Problem 66

'''
I found the Pell equation elsewhere. First time i've imported any code for Euler. I still
need to understand how Pell equation works.

https://www.youtube.com/watch?v=s5RQj_Jcs0U

'''

# Step 1: Create list of D's
D_list = []
D_range = 1000
for x in range(D_range):
    if x ** 0.5 != round(x ** 0.5):
        D_list.append(x)

import math
 
def solvePell(D):
    x = int(math.sqrt(D))
    y, z, r = x, 1, x * 2
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        y = r * z - y
        z = (D - y * y) // z
        r = (x + y) // z
 
        e1, e2 = e2, e1 + e2 * r
        f1, f2 = f2, f1 + f2 * r
 
        a, b = f2 * x + e2, f2
        if a * a - D * b * b == 1:
            return a

max_x = 0
for D in D_list:
    x = solvePell(D)
    if x > max_x:
        max_x = x
        max_D = D
print(max_D)
