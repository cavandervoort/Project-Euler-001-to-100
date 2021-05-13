# Problem 92
# Square digit chains

import time
start = time.time()

print("This takes ~25 seconds")

def digitsSquared(i,sqrDict):
    digList = [x for x in str(i)]
    digSum = 0
    for dig in digList:
        digSum += sqrDict[dig]
    return digSum

def goesToTest(i,sqrDict,goesToDict):
    numsSeen = []
    while i != 1 and i != 89:
        if i in goesToDict:
            return goesToDict[i],numsSeen,goesToDict
        numsSeen.append(i)
        i = digitsSquared(i,sqrDict)
    if i == 89:
        numsSeen.append(89)
        return 89,numsSeen,goesToDict
    return 1,numsSeen,goesToDict

sqrDict = {'0':0, '1':1, '2':4, '3':9, '4':16, '5':25, '6':36, '7':49, '8':64, '9':81}
goesToDict = {}

count = 0

for i in range(1,10_000_000):
    goesTo,numsSeen,goesToDict = goesToTest(i,sqrDict,goesToDict)
    for num in numsSeen:
        goesToDict[num] = goesTo

goesTo89 = 0
for key in goesToDict:
    if goesToDict[key] == 89:
        goesTo89 += 1

print(f'Done in {time.time() - start} seconds')
print(goesTo89)
