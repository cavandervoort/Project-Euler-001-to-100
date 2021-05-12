# Problem 17
# Number letter counts

# create list of strings

allNums = []
for huns in range(10):
    for tens in range(10):
        for sins in range(10):
            allNums.append(str(huns) + str(tens) + str(sins))

allNums.pop(0)

# count letters

def count(num):
    counter = 0
    if num[1] == '1':
        counter += teens[num[2]]
    else:
        counter += ones[num[2]] + tens[num[1]]
    counter += ones[num[0]]
    if num[0] != '0':
        counter += 7
        if num[1:3] != '00':
            counter += 3
    return counter
    
ones = {'0':0, '1':3, '2':3, '3':5, '4':4, '5':4, '6':3, '7':5, '8':5, '9':4}
tens = {'0':0, '1':0, '2':6, '3':6, '4':5, '5':5, '6':5, '7':7, '8':6, '9':6}
teens = {'0':3, '1':6, '2':6, '3':8, '4':8, '5':7, '6':7, '7':9, '8':8, '9':8}

totLetters = 0

for num in allNums:
    totLetters += count(num)

totLetters += 11 # for one thousand

print(f'Number of letters: {totLetters}')