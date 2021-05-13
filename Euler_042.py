# Problem 42
# Coded triangle numbers

def wordScore(word,letterDict):
    score = 0
    for char in word:
        score += letterDict[char.lower()]
    return score

# create dictionary for letter values
import string
letters = [char for char in string.ascii_lowercase]
count = 1
letterDict = {}
for letter in letters:
    letterDict[letter] = count
    count += 1

# separate array of words
f = open("p042_words.txt", "r")
wordsStr = f.readline()
wordArr = wordsStr[1:-1].split('","')

# build array of triangle numbers
tNums = {}
for n in range(1,60):
    tNums[int(n*(n+1)/2)] = None

# evaluate and count triangle words
countTri = 0
for word in wordArr:
    score = wordScore(word,letterDict)
    if score in tNums:
        countTri += 1
    
print(f'{countTri} triangle words out of {len(wordArr)} words')
