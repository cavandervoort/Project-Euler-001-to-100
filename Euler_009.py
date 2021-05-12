# Problem 9
# Special Pythagorean triplet

for c in range(400,500):
    for b in range(300,c):
        a = 1000 - c - b
        if c ** 2 == b ** 2 + a ** 2:
            print(f'c is {c}; b is {b}; and a is {a}')
            print(c*b*a)