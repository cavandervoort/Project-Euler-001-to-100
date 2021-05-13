# Problem 97
# Large non-Mersenne prime

# power is 7830457
# multi is 28433
# plus 1

def trim_to_10(i):
    return int(str(i)[-10:])

one_k = trim_to_10(2 ** 1000)    

num = 1
for _ in range(7830):
    num *= one_k
    num = trim_to_10(num)

num *= trim_to_10(2 ** 457)

final = trim_to_10(28433 * num + 1)

print(final)
