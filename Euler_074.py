# Problem 74
# Digit factorial chains

def count_chain(x,factDict,factFuncDict):
    xOriginal = x
    chainLenDictTemp = {x:None}
    while True:
        x = factFunc(x,factDict,factFuncDict)
        if x in chainLenDictTemp:
            return len(chainLenDictTemp),chainLenDictTemp
        else:
            chainLenDictTemp[x] = 0

def factFunc(i,factDict,factFuncDict):
    if i in factFuncDict:
        return factFuncDict[i]
    iDigArr = [dig for dig in str(i)]
    output = 0
    for dig in iDigArr:
        output += factDict[dig]
    factFuncDict[i] = output
    return output

import time
start = time.time()

print("This will take ~15 seconds")

factFuncDict = {}
factDict = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}
chainLenDict = {}

limit = 1_000_000
count60 = 0
for num in range(limit):
    if num in chainLenDict:
        continue
    else:
        chainSize,chainLenDictTemp = count_chain(num,factDict,factFuncDict)
        chainLenDict.update(chainLenDictTemp)
        if chainSize >= 60:
            count60 += 1

print(count60)
print(f'Done in {time.time() - start} seconds')
