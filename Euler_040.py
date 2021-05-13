# Problem 40
# Champernowne's constant

digitArr = []
for num in range(200000):
    for char in str(num):
        digitArr.append(char)

val = 1
for power in range(7):
    n = 10 ** power
    val *= int(digitArr[n])

print(f'val is {val}')
