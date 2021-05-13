# Problem 53
# Combinatoric selections

def create_dic(limit):
    temp_dic = {0:1}
    temp_fact = 1
    for x in range(1,limit+1):
        temp_fact *= x
        temp_dic[x] = temp_fact
    return temp_dic

limit = 100
fact_dic = create_dic(limit)

count = 0
for n in range(1,limit+1):
    for r in range(1,n+1):
        if fact_dic[n] / (fact_dic[r] * fact_dic[n-r]) > 1000000:
            count += 1

print(count)
