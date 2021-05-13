# Problem 52
# Permuted multiples

for x in range(1,2000000):
    isWorking = True
    xStringSorted = sorted([char for char in str(x)])
    for multiplier in range(2,7):
        if xStringSorted != sorted([char for char in str(x * multiplier)]):
            isWorking = False
            break
    
    if isWorking == True:
        print(x)
        break
