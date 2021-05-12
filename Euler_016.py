# Problem 16
# Power digit sum

num = 2 ** 1000
strNum = str(num)
digitsSum = 0
for digit in strNum:
    digitsSum += int(digit)

print(digitsSum)