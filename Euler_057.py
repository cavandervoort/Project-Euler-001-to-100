# Problem 57

num = 1
den = 2
count = 0
for x in range(1000):
    new_num = den
    den = num + den*2
    num = new_num
    if len(str(num+den)) > len(str(den)):
        count += 1

print(count)
