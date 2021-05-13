# Problem 56
# Powerful digit sum

# Considering natural numbers of the form, ab, where a, b < 100, what is
# the maximum digital sum?

def digital_sum(num):
    digit_list = [int(x) for x in str(num)]
    return sum(digit_list)


rangy = 100
max_sum = 0
for a in range(rangy):
    for b in range(rangy):
        new_sum = digital_sum(a ** b)
        if new_sum > max_sum:
            max_sum = new_sum
            # print(f'new biggest sum: {a}^{b} = {a**b} for digital sum of {max_sum}')

print(f'Maximum digital sum: {max_sum}')
