# Problem 51 - replacing 3 digits - May 2021
# Prime digit replacements

import time
start = time.time()

def getPrimes(n):
    primeArray = [0,0] + [1] * (n-1)
    for pos in range(2, int(n ** 0.5)+1):
        if primeArray[pos] == 1:
            testNum = pos * 2
            while testNum < n + 1:
                primeArray[testNum] = 0
                testNum += pos
    primes = []
    for pos in range(2,n+1):
        if primeArray[pos] == 1:
            primes.append(pos)
    return primes

limit = 1_000_000

# get the primes below limit
primesArr = getPrimes(limit)
primesDict = {}
for prime in primesArr:
    primesDict[prime] = None     

# check numbers for primes
countMax = 0
for num in range(3,int(limit/1000)):
    if (num % 5 == 0) or (num % 2 == 0):
        continue
    if countMax >= 8:
        break
    
    numStr = str(num)
    numStrLen = len(numStr)
    for xPos in range(numStrLen):
        for yPos in range(xPos + 1, numStrLen + 1):
            for zPos in range(yPos + 1, numStrLen + 2):
                count = 0
                countNot = 0
                for xyzVal in range(9,-1,-1):
                    if xPos == 0 and xyzVal == 0:
                        continue
                    numArr = [char for char in numStr]
                    numArr.insert(xPos, str(xyzVal))
                    numArr.insert(yPos, str(xyzVal))
                    numArr.insert(zPos, str(xyzVal))
                    testNumStr = ''.join(numArr)
                    testNumInt = int(testNumStr)
                    
                    

                    if testNumInt in primesDict:
                        count += 1
                    else:
                        countNot += 1
                        if countNot > 2:
                            break

                if count > countMax:
                    countMax = count
                    if count > 7:
                        print(testNumInt)
                        numDigis = [char for char in numStr]
                        numDigis.insert(xPos, '_')
                        numDigis.insert(yPos, '_')
                        numDigis.insert(zPos, '_')
                        print(f'Family size is {countMax} using {numDigis}')
                    
print(f'Done in {time.time() - start} seconds')
