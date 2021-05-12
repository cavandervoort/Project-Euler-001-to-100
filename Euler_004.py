# Problem 4
# Largest palindrome product

palinMax = 0

for x in range(999,99,-1):
    for y in range(x, 99,-1):
        if str(x*y) == str(x*y)[::-1]:
            if x*y > palinMax:
                palinMax = x*y
            break
    if palinMax > x*999:
        break

print(f'answer: {palinMax}')