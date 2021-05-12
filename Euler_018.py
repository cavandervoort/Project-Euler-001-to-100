# Problem 18
# Maximum path sum I

# clean up input to create array of all numbers
numsStr = '7595 6417 47 8218 35 87 1020 04 82 47 6519 01 23 75 03 3488 02 77 73 07 63 6799 65 04 28 06 16 70 9241 41 26 56 83 40 80 70 3341 48 72 33 47 32 37 16 94 2953 71 44 65 25 43 91 52 97 51 1470 11 33 28 77 73 17 78 39 68 17 5791 71 52 38 17 14 91 43 58 50 27 29 4863 66 04 68 89 53 67 30 73 16 69 87 40 3104 62 98 27 23 09 70 98 73 93 38 53 60 04 23'
numsStr = numsStr.replace(' ','')
numsCount = int(len(numsStr)/2)

numsIntArr = []
for pos in range(numsCount):
    newNum = int(numsStr[pos*2:pos*2+2])
    numsIntArr.append(newNum)

# build pyramid out of int array
pyramid = []
for row in range(15):
    newRow = []
    for pos in range(row+1):
        newNum = numsIntArr.pop(0)
        newRow.append(newNum)
    pyramid.append(newRow)
    
# moving from bottom to top, calculate running max sum for each position
for row in range(13,-1,-1):
    for pos in range(row+1):
        pyramid[row][pos] += max([pyramid[row+1][pos], pyramid[row+1][pos+1]])

print(pyramid[0][0])