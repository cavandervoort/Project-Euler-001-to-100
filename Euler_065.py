# Problem 65
# Convergents of e

constants = []
for x in range(1,40):
    constants.append(1)
    constants.append(2 * x)
    constants.append(1)

num = 1
den = 1
count = 0

for x in range(97,-1,-1):
    new_num = den
    den = num + den*constants[x]
    num = new_num

print(f'num {num+den*2}\n-------\nden {den}\n')

digArr = [int(dig) for dig in str(num+den*2)]
print(sum(digArr))
