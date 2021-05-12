# Problem 26

import math

cycleMax = [0, 0]
for n in range(1,1000):

    numTemp = 10
    remainder = []
    output = ''
    maxLen = 1
    cycle = 0

    for dig in range(100000):
        output += str(math.floor(numTemp / n))
        numTemp -= math.floor(numTemp / n) * n
        
        if numTemp in remainder:
            for rem in range(0, len(remainder)-1):
                if remainder[-1] == remainder[rem]:
                    cycle = len(remainder) - rem - 1
                    break

        remainder.append(numTemp)
        
        if cycle > 0:
            if cycle > cycleMax[0]:
                cycleMax = [cycle, n]
            break

        numTemp *= 10

print(f'The denominator w/ longest recurring cycle is {cycleMax[1]}')