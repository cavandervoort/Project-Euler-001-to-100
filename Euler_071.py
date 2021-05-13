# Problem 71
# Ordered fractions

'''
I first solved this by using some intuition and guess and check. The 
coding solution is similar to my solution to Problem 85. I start with 1/1 
and then keep adding one to the numerator or denominator, based on 
whether I was too high or too low.
'''

n = 1
d = 1
x = 3/7
min_diff = 1
while d <= 1_000_000:
    if n/d < x:
        temp_diff = x - n/d
        if temp_diff < min_diff:
            min_diff = temp_diff
            min_n = n
            min_d = d
        n += 1
    else:
        d += 1
        
print(f'Fraction to the left: {min_n}/{min_d}')
