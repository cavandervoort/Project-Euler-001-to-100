# Problem 44
# Pentagon numbers

import time
start = time.time()

# create list of pentagonal numbers
pentDict = {}
pentArr = []
i,pentNum = 1,1
limit = 10_000_000
while pentNum < limit:
    pentNum = int(i*(3*i-1)/2)
    pentDict[pentNum] = None
    pentArr.append(pentNum)
    i += 1

# find pairs
minDiff = limit
for pent1 in pentArr:
    for pent2 in pentArr:
        if pent2 >= pent1:
            break
        elif pent1 + pent2 in pentDict:
            if pent1 - pent2 in pentDict:
                diff = pent1 - pent2
                if diff < minDiff:
                    minDiff = diff
                    print(f'I found the minimum D-value: {minDiff} from {pent1} & {pent2}')

print(f'Done. Time elapsed: {time.time() - start}\n')
