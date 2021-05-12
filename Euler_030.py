# Problem 30
# Digit fifth powers

def powNum(num,fifthPowers):
    str_num = str(num)
    sumFifthPowers = 0
    for char in str_num:
        sumFifthPowers += fifthPowers[int(char)]
    return sumFifthPowers

fifthPowers = {}
for dig in range(10):
    fifthPowers[dig] = dig ** 5

sum5thPowerSumNums = 0
for num in range(2,300000): 
    if num == powNum(num,fifthPowers):
        sum5thPowerSumNums += num

print(f'Answer: {sum5thPowerSumNums}')
