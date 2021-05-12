# Problem 14
# Longest Collatz sequence

import time
start = time.time()

countMax = 0
numMax = 0
numsSeen = {}
numRange = 1_000_000

for num in range(1,numRange):
    
    if num not in numsSeen or numsSeen[num] < 0:
    
        tempNum = num
        tempCount = 1

        while tempNum != 1:

            if tempNum % 2 == 0:
                tempNum /= 2

            elif tempNum % 2 == 1:
                tempNum = tempNum * 3 + 1
                
            if tempNum in numsSeen:
                if numsSeen[tempNum] > 0:
                    tempCount += numsSeen[tempNum]
                    break
            else:
                numsSeen[tempNum] = -1

            tempCount += 1
            
        numsSeen[num] = tempCount

        if tempCount > countMax:
            countMax = tempCount
            numMax = num

print(f'{numMax}: {tempCount}')
print(f'Done in {time.time() - start} seconds')