# Problem 60

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

def concatTest(prime_1, prime_2, primesArr, primesDict):
    test_1 = int(str(prime_1)+str(prime_2))
    test_2 = int(str(prime_2)+str(prime_1))

    if isPrime(test_1,primesArr,primesDict) and isPrime(test_2,primesArr,primesDict):
        return True
    return False

def isPrime(testNum,primesArr,primesDict):
    if testNum < limit:
        return testNum in primesDict
    if testNum in bigPrimesDict:
        return True
    breakNum = testNum ** 0.5
    for prime in primesArr:
        if testNum % prime == 0:
            return False
        elif prime > breakNum:
            bigPrimesDict[testNum] = None
            return True
    return True
    
import time
start = time.time()

print("This will take ~25 seconds")

# Find Primes
limit = 10_000_000
primesArr = getPrimes(limit)
primesDict = {}
bigPrimesDict = {}
for prime in primesArr:
    primesDict[prime] = None 
print(f'Step 1: found primes below {limit} in {time.time() - start} seconds\n')

setMin = 10 ** 25
rangy = 1250

for a in range(rangy):
    if primesArr[a] > setMin / 5:
        break
    for b in range(a+1,rangy):
        if primesArr[b] > (setMin - primesArr[a]) / 4:
            break
        
        elif concatTest(primesArr[a], primesArr[b], primesArr, primesDict) == False:
            continue
        
        for c in range(b+1,rangy):
            if primesArr[c] > (setMin - (primesArr[a] + primesArr[b])) / 3:
                break
            if concatTest(primesArr[a], primesArr[c], primesArr, primesDict) == False:
                continue
            elif concatTest(primesArr[b], primesArr[c], primesArr, primesDict) == False:
                continue
            
            for d in range(c+1,rangy):
                if primesArr[d] > (setMin - (primesArr[a] + primesArr[b] + primesArr[c])) / 2:
                    break
                if concatTest(primesArr[a], primesArr[d], primesArr, primesDict) == False:
                    continue
                elif concatTest(primesArr[b], primesArr[d], primesArr, primesDict) == False:
                    continue
                elif concatTest(primesArr[c], primesArr[d], primesArr, primesDict) == False:
                    continue
                
                for e in range(d+1,rangy):
                    if primesArr[e] > (setMin - (primesArr[a] + primesArr[b] + primesArr[c] + primesArr[d])):
                        break
                    if concatTest(primesArr[a], primesArr[e], primesArr, primesDict) == False:
                        continue
                    elif concatTest(primesArr[b], primesArr[e], primesArr, primesDict) == False:
                        continue
                    elif concatTest(primesArr[c], primesArr[e], primesArr, primesDict) == False:
                        continue
                    elif concatTest(primesArr[d], primesArr[e], primesArr, primesDict) == False:
                        continue
                    else:
                        print(f'5-set of primes: {primesArr[a]}, {primesArr[b]}, {primesArr[c]}, {primesArr[d]}, {primesArr[e]}')
                        sumPrimes = primesArr[a] + primesArr[b] + primesArr[c] + primesArr[d] + primesArr[e]
                        if sumPrimes < setMin:
                            setMin = sumPrimes
                            print(f'new set_min of {setMin}')
                            print(f'Time check: {time.time() - start} seconds\n')
                            
                        
print(f'Done in {time.time() - start} seconds')
