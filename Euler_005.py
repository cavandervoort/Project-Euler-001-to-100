# Problem 5
# Smallest multiple

divisors = []

for num in range(1,21):
    tempNum = num
    for divisor in divisors:
        if tempNum % divisor == 0:
            tempNum /= divisor
    if tempNum > 1:
        divisors.append(int(tempNum))
        # print(f'new divisor ({int(temp_num)}, from {num}) added to divisors, now at {divisors}')

output = 1
for divisor in divisors:
    output *= divisor

print(output)