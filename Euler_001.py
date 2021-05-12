# Problem 1
# Multiples of 3 and 5
runningSum = 0
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        runningSum += num
print(runningSum)