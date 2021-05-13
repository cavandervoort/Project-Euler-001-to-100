# Problem 34
# Digit factorials

# create factorials dictionary
factorialsDict = {}
runningFactorial = 1
for i in range(0,10):
    factorialsDict[i] = runningFactorial
    runningFactorial *= i + 1
    
limit = factorialsDict[9]*6 + factorialsDict[3]
curiousNumsSum = 0

for num in range(10,limit):
    factorialsSum = 0
    for char in str(num):
        factorialsSum += factorialsDict[int(char)]
    if num == factorialsSum:
        curiousNumsSum += num
        
print(f'The sum of curious numbers is: {curiousNumsSum}')
